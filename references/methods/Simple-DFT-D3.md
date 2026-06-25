<!-- Source: https://vasp.at/wiki/index.php/Simple-DFT-D3 | revid: 37312 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Simple-DFT-D3


Simple
DFT-D3<sup>[\[1\]](#cite_note-ehlert:joss:2024-1)[\[2\]](#cite_note-sdftd3_1-2)[\[3\]](#cite_note-sdftd3_2-3)</sup>
is an external package that implements the DFT-D3
method<sup>[\[4\]](#cite_note-grimme:jcp:10-4)[\[5\]](#cite_note-grimme:jcc:11-5)</sup>
and can be [linked to
VASP](../misc/Makefile.include.md).
DFT-D3 adds to the DFT energy expression a term that accounts for the
[van der Waals (vdW)
interactions](Category-Van_der_Waals_functionals.md),
which are in principle not included in semilocal and hybrid
exchange-correlation functionals. This is an approximation of the
atom-pairwise type that depends only on the structure of the system,
which allows for a fast computation. Since every functional has
different interactions between atoms, DFT-D3 tailors its adjustable
parameters to the functional. For more information regarding these
parameters, please refer to the DFT-D3
papers<sup>[\[4\]](#cite_note-grimme:jcp:10-4)[\[5\]](#cite_note-grimme:jcc:11-5)</sup>
and simple DFT-D3
websites.<sup>[\[2\]](#cite_note-sdftd3_1-2)[\[3\]](#cite_note-sdftd3_2-3)</sup>

Compared to the implementation in VASP of DFT-D3
([IVDW](../incar-tags/IVDW.md)=11 and 12, see
[DFT-D3](DFT-D3.md)), the simple DFT-D3 package has some
advantages:

- It offers more types of damping functions
  ([SDFTD3_DAMPING](../incar-tags/SDFTD3_DAMPING.md)).
- Allows to activate the three-body Axilrod–Teller–Muto term
  ([VDW_S9](../incar-tags/VDW_S9.md)).
- It has vdW parameters for elements up to lawrencium
  ($Z=103$), while it is up to plutonium
  ($Z=94$) in the VASP implementation.
- It is computationally faster.

|  |
|----|
| **Important:** The use of simple DFT-D3 with VASP is available from VASP.6.6.0 onwards that needs to be compiled with -DSDFTD3. |

|  |
|----|
| **Mind:** simple DFT-D3 may switch to a <a href="https://github.com/dftd3/simple-dftd3/issues/199"
class="external text" rel="nofollow">smooth cutoff</a> by default, which will change results for periodic systems with respect to prior versions and especially compared to VASPs own implementation (see [DFT-D3](DFT-D3.md)). |

## Usage\[<a
href="/wiki/index.php?title=Simple-DFT-D3&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

For some of the common exchange-correlation functionals (e.g., PBE,
SCAN, or HSE06) it is sufficient to set [IVDW](../incar-tags/IVDW.md)=15 and
[SDFTD3_DAMPING](../incar-tags/SDFTD3_DAMPING.md) for the damping
function in the [INCAR](../input-files/INCAR.md) file. Internally, VASP
passes automatically the name of the functional to simple DFT-D3.
However, for other functionals the
[SDFTD3_XC](../incar-tags/SDFTD3_XC.md) tag has to be used to specify
the functional to simple DFT-D3 (the names are listed in the file
param.f90 of the simple DFT-D3 source code). Subsequently, simple DFT-D3
maps the functional name to optimized settings for the adjustable
parameters of the vdW interaction. VASP uses these parameters to compute
the DFT-D3 energies, forces, and stresses in every ionic step and adds
them to the corresponding DFT terms. As a result, you can relax
structures or run
<a href="/wiki/MD" class="mw-redirect" title="MD">MD simulations</a>
with an approximate treatment of vdW interactions.

|  |
|----|
| **Important:** Below, we explain how to tweak the parameters of DFT-D3. Typically, you should not modify them unless you have a very good reason, e.g., because the interface is not implemented for the exchange-correlation functional you use. |

VASP allows setting the following tags in the
[INCAR](../input-files/INCAR.md) file:

- [SDFTD3_DAMPING](../incar-tags/SDFTD3_DAMPING.md) : type of
  damping function.
- [SDFTD3_XC](../incar-tags/SDFTD3_XC.md) : functional name to
  determine the set of vdW parameters.
- [VDW_S6](../incar-tags/VDW_S6.md) : scaling of the dipole-dipole
  dispersion.
- [VDW_S8](../incar-tags/VDW_S8.md) : scaling of the dipole-quadrupole
  dispersion.
- [VDW_SR](../incar-tags/VDW_SR.md) : scaling of the dipole-dipole
  damping.
- [VDW_SR8](../incar-tags/VDW_SR8.md) : scaling of the dipole-quadrupole
  damping.
- [VDW_A1](../incar-tags/VDW_A1.md) : scaling of the critical radii in the
  Becke-Johnson rational damping.
- [VDW_A2](../incar-tags/VDW_A2.md) : offset of the critical radii in the
  Becke-Johnson rational damping.
- [VDW_BETA](../incar-tags/VDW_BETA.md) : offset for damping radius or
  power for the zero-damping component
- [VDW_S9](../incar-tags/VDW_S9.md) : scaling of the three-body dispersion
  energy.
- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md) : two-body interaction
  cutoff.
- [VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md) : coordination
  number cutoff.

## References\[<a
href="/wiki/index.php?title=Simple-DFT-D3&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-ehlert:joss:2024_1-0)
    <a href="https://doi.org/10.21105/joss.07169" class="external text"
    rel="nofollow">S. Ehlert, <em>Simple dft-d3: library first
    implementation of the d3 dispersion correction</em>, J. Open Source
    Softw. <strong>9</strong>, 7169 (2024).</a>
2.  ↑
    <sup>[a](#cite_ref-sdftd3_1_2-0)</sup>
    <sup>[b](#cite_ref-sdftd3_1_2-1)</sup>
    <a href="https://dftd3.readthedocs.io/" class="external text"
    rel="nofollow">https://dftd3.readthedocs.io</a>
3.  ↑
    <sup>[a](#cite_ref-sdftd3_2_3-0)</sup>
    <sup>[b](#cite_ref-sdftd3_2_3-1)</sup>
    <a href="https://github.com/dftd3/" class="external text"
    rel="nofollow">https://github.com/dftd3</a>
4.  ↑
    <sup>[a](#cite_ref-grimme:jcp:10_4-0)</sup>
    <sup>[b](#cite_ref-grimme:jcp:10_4-1)</sup>
    <a href="https://doi.org/10.1063/1.3382344" class="external text"
    rel="nofollow">S. Grimme, J. Antony, S. Ehrlich, and S. Krieg, J. Chem.
    Phys. <strong>132</strong>, 154104 (2010).</a>
5.  ↑
    <sup>[a](#cite_ref-grimme:jcc:11_5-0)</sup>
    <sup>[b](#cite_ref-grimme:jcc:11_5-1)</sup>
    <a href="https://doi.org/10.1002/jcc.21759" class="external text"
    rel="nofollow">S. Grimme, S. Ehrlich, and L. Goerigk, J. Comput. Chem.
    <strong>32</strong>, 1456 (2011).</a>


## Related tags and articles\[<a
href="/wiki/index.php?title=Simple-DFT-D3&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](../incar-tags/IVDW.md),
[SDFTD3_DAMPING](../incar-tags/SDFTD3_DAMPING.md),
[SDFTD3_XC](../incar-tags/SDFTD3_XC.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_S8](../incar-tags/VDW_S8.md),
[VDW_SR](../incar-tags/VDW_SR.md), [VDW_SR8](../incar-tags/VDW_SR8.md),
[VDW_A1](../incar-tags/VDW_A1.md), [VDW_A2](../incar-tags/VDW_A2.md),
[VDW_BETA](../incar-tags/VDW_BETA.md), [VDW_S9](../incar-tags/VDW_S9.md),
[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md),
[DFT-D3](DFT-D3.md), [DFT-D4](DFT-D4.md)



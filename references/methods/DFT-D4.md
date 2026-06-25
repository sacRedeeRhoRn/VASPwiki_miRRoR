<!-- Source: https://vasp.at/wiki/index.php/DFT-D4 | revid: 37311 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DFT-D4


DFT-D4[^caldeweyher:jcp:2019-1][^dftd4_1-2][^dftd4_2-3]
is an external package that can be [linked to
VASP](../misc/Makefile.include.md).
DFT-D4 adds to the DFT energy expression a term that accounts for the
[van der Waals (vdW)
interactions](Category-Van_der_Waals_functionals.md),
which are in principle not included in semilocal and hybrid
exchange-correlation functionals. This is an approximation of the
atom-pairwise type that depends only on the structure of the system,
which allows for a fast computation. Since every functional has
different interactions between atoms, DFT-D4 tailors its adjustable
parameters to the functional. For more information regarding these
parameters, please refer to the DFT-D4
paper[^caldeweyher:jcp:2019-1]
and
websites.[^dftd4_1-2][^dftd4_2-3]

## Usage\[<a href="/wiki/index.php?title=DFT-D4&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

For some of the common exchange-correlation functionals (e.g., PBE,
SCAN, or HSE06) it is sufficient to set [IVDW](../incar-tags/IVDW.md)=13 in
the [INCAR](../input-files/INCAR.md) file. Internally, VASP passes
automatically the name of the functional to DFT-D4. However, for other
functionals the [DFTD4_XC](../incar-tags/DFTD4_XC.md) tag has to be used
to specify the functional to DFT-D4 (the names are listed in the file
param.f90 of the DFT-D4 source code). Subsequently, DFT-D4 maps the
functional name to optimized settings for the adjustable parameters of
the vdW interaction. VASP uses these parameters to compute the DFT-D4
energies, forces, and stresses in every ionic step and adds them to the
corresponding DFT terms. As a result, you can relax structures or run
<a href="/wiki/MD" class="mw-redirect" title="MD">MD simulations</a>
with an approximate treatment of vdW interactions.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span
style="color: var(--vpurple);">Important:</span></strong>
<ul>
<li>The API of DFT-D4 has been modified starting with version 4.0.0. The
adaptation has been made in VASP.6.6.0. Versions of DFT-D4 with the old
API (v3.7.0 and older) can still be compiled with VASP.6.6.0 as
explained <a
href="/wiki/Makefile.include#DFT-D4_and_simple-DFT-D3_.28optional.29"
title="Makefile.include">here</a>.</li>
<li>Below, we explain how to tweak the parameters of DFT-D4. Typically,
you should not modify them unless you have a very good reason, e.g.,
because the interface is not implemented for the exchange-correlation
functional you use.</li>
</ul></td>
</tr>
</tbody>
</table>

|  |
|----|
| **Mind:** DFT-D4 may switch to a <a href="https://github.com/dftd4/dftd4/issues/377"
class="external text" rel="nofollow">smooth cutoff</a> by default, which will change results for periodic systems with respect to prior versions. |

VASP allows setting the following tags in the
[INCAR](../input-files/INCAR.md) file:

- [DFTD4_MODEL](../incar-tags/DFTD4_MODEL.md) : dispersion model
  (available from VASP.6.6.0 onwards).
- [DFTD4_XC](../incar-tags/DFTD4_XC.md) : functional name to determine
  the set of vdW parameters (available from VASP.6.6.0 onwards).
- [VDW_S6](../incar-tags/VDW_S6.md) : scaling of the dipole-dipole
  dispersion.
- [VDW_S8](../incar-tags/VDW_S8.md) : scaling of the dipole-quadrupole
  dispersion.
- [VDW_A1](../incar-tags/VDW_A1.md) : scaling of the critical radii in the
  Becke-Johnson rational damping.
- [VDW_A2](../incar-tags/VDW_A2.md) : offset of the critical radii in the
  Becke-Johnson rational damping.
- [VDW_S9](../incar-tags/VDW_S9.md) : scaling of the three-body dispersion
  energy (available from VASP.6.6.0 onwards).
- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md) : two-body interaction
  cutoff (available from VASP.6.6.0 onwards).
- [VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md) : coordination
  number cutoff (available from VASP.6.6.0 onwards).

## References\[<a href="/wiki/index.php?title=DFT-D4&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
## Related tags and articles\[<a href="/wiki/index.php?title=DFT-D4&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](../incar-tags/IVDW.md),
[DFTD4_MODEL](../incar-tags/DFTD4_MODEL.md),
[DFTD4_XC](../incar-tags/DFTD4_XC.md), [VDW_S6](../incar-tags/VDW_S6.md),
[VDW_S8](../incar-tags/VDW_S8.md), [VDW_A1](../incar-tags/VDW_A1.md),
[VDW_A2](../incar-tags/VDW_A2.md), [VDW_S9](../incar-tags/VDW_S9.md),
[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md),
[DFT-D3](DFT-D3.md),
[simple-DFT-D3](Simple-DFT-D3.md)

[^caldeweyher:jcp:2019-1]: [E. Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, and S. Grimme, J. Chem. Phys. **150**, 154122 (2019).](https://doi.org/10.1063/1.5090222)
[^dftd4_1-2]: [https://dftd4.readthedocs.io](https://dftd4.readthedocs.io/)
[^dftd4_2-3]: [https://github.com/dftd4](https://github.com/dftd4/)

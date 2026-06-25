<!-- Source: https://vasp.at/wiki/index.php/Energy_cutoff_and_FFT_meshes | revid: 35859 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Energy cutoff and FFT meshes


The [plane-wave expansion of the Kohn-Sham (KS)
orbitals](../methods/Projector-augmented-wave_formalism.md)
are associated to a mesh to perform FFTs from real space coordinates
\$\mathbf{r}\$ to reciprocal coordinates \$\mathbf{G}\$ and vice versa.
These have a very large impact on the accuracy of any ab-initio
calculation particularly including basic [electronic minimization
calculations](Setting_up_an_electronic_minimization.md).
The so-called FFT mesh and thus basis-set truncation is a result of the
selected energy cutoff ([ENCUT](../incar-tags/ENCUT.md)). It is one of the
most important parameters for the accuracy. Some indications and
illustrations on how to choose [ENCUT](../incar-tags/ENCUT.md) or other
related tags like [PREC](../incar-tags/PREC.md) are provided below.


## Contents


- [1 Aspects to
  refine the choice of the cutoff energy, FFT mesh and related
  parameters](#aspects-to-refine-the-choice-of-the-cutoff-energy-fft-mesh-and-related-parameters)
  - [1.1 Energy
    cutoff](#energy-cutoff)
  - [1.2 FFT
    mesh](#fft-mesh)
    - [1.2.1 Mesh
      for the KS orbitals (soft mesh or coarse
      mesh)](#mesh-for-the-ks-orbitals-soft-mesh-or-coarse-mesh))
    - [1.2.2 Mesh
      for the densities (fine
      mesh)](#mesh-for-the-densities-fine-mesh))
    - [1.2.3
      Support grid](#support-grid)
- [2 Example:
  volume relaxation and
  pressure](#example-volume-relaxation-and-pressure)
  - [2.1 Related
    tags and articles](#related-tags-and-articles)


# Aspects to refine the choice of the cutoff energy, FFT mesh and related parameters\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Aspects to refine the choice of the cutoff energy, FFT mesh and related parameters">edit</a> \| (./index.php.md)\]

## Energy cutoff\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Energy cutoff">edit</a> \| (./index.php.md)\]

The energy cutoff ([ENCUT](../incar-tags/ENCUT.md)) should be chosen
according to the <a href="/wiki/Pseudopotential" class="mw-redirect"
title="Pseudopotential">pseudopotential</a>
([POTCAR](../input-files/POTCAR.md)) and required accuracy. The default
value for [ENCUT](../incar-tags/ENCUT.md) is the largest among the
**ENMAX** values found in the [POTCAR](../input-files/POTCAR.md) file.
Values smaller than the default should never be used, since it leads to
very large errors. The default minimal value should usually result in an
error in the cohesive energy which is less than 10 meV.

|  |
|----|
| **Tip:** The recommended procedure for choosing [ENCUT](../incar-tags/ENCUT.md) is to perform a series of calculations with different [ENCUT](../incar-tags/ENCUT.md) values (larger than the default one) and to monitor the results for the property of interest. |

Regarding the convergence of the total energy with respect to
[ENCUT](../incar-tags/ENCUT.md), the distinction between the **total
energy** and the **total energy difference** (e.g., between different
geometries during a
<a href="/wiki/Structure_relaxation" class="mw-redirect"
title="Structure relaxation">structure relaxation</a> or of two
polymorphs) should be made. Usually, the total energy difference
converges much faster than the total energies. This is especially true
if both geometries are rather similar (e.g.,
<a href="/wiki/Structure_relaxation" class="mw-redirect"
title="Structure relaxation">structure relaxation</a>), and in this case
the errors due to the finite energy cutoff should to some extent cancel
each other when calculating the energies difference. However, if two
configurations differ strongly from each other, e.g. for the calculation
of the cohesive energy (bulk versus atom), the convergence of the
energies difference with respect to [ENCUT](../incar-tags/ENCUT.md) may be
quite slow.

|  |
|----|
| **Important:** We strongly recommend specifying the energy cutoff ([ENCUT](../incar-tags/ENCUT.md)) always manually in the [INCAR](../input-files/INCAR.md) file to ensure the same accuracy between calculations. Otherwise, the default [ENCUT](../incar-tags/ENCUT.md) may differ among the different calculations if other atomic species are present, with the consequence that the total energies can not be compared. |

## FFT mesh\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: FFT mesh">edit</a> \| (./index.php.md)\]

There are a number of quantities, e.g., the Kohn-Sham orbitals, the
charge density, magnetization, XC potential, etc. that are described on
a real-space mesh in the unit cell. Depending on the relation of the
specific quantity to the KS orbitals the real-space mesh and associated
FFT mesh must be choosen denser.

### Mesh for the KS orbitals (soft mesh or coarse mesh)\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Mesh for the KS orbitals (soft mesh or coarse mesh)">edit</a> \| (./index.php.md)")\]

The FFT mesh for the KS orbitals is the so-called coarse or soft mesh.
The size of the coarse FFT mesh
([NGX](../incar-tags/NGX.md),[NGY](../incar-tags/NGY.md),[NGZ](../incar-tags/NGZ.md))
is determined by [ENCUT](../incar-tags/ENCUT.md) and
[PREC](../incar-tags/PREC.md). [NGX](../incar-tags/NGX.md),
[NGY](../incar-tags/NGY.md) and [NGZ](../incar-tags/NGZ.md) can also be set
manually.

In order to avoid [wrap-around
errors](../theory/Wrap-around_errors.md) the FFT mesh
should contain all wave vectors up to $2G_{\rm cut}$, where $G_{\rm cut}$
is defined by

$E_{\rm cut}=\frac{\hbar^2}{2m_e}G_{\rm cut}^2$

with $E_{\rm cut}$=[ENCUT](../incar-tags/ENCUT.md). It is not always
possible or necessary to use such a large FFT mesh for the KS orbitals,
particularly during the test phase where a lower accuracy may surfize
while other parameters of the calculation are varied and adjusted.
Usually, only high-quality calculations require a mesh that avoids any
<a href="/wiki/Wrap-around_error" class="mw-redirect"
title="Wrap-around error">wrap-around error</a>. Such calculations can
be done with [`PREC`](../incar-tags/PREC.md)` = Accurate`.

For most calculations, and in particular with standard pseudopotentials
with their default cutoff energies, it is sufficient to choose
[NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md) and
[NGZ](../incar-tags/NGZ.md) to $3/4$ of the
required values to avoid most wrap-around errors, i.e., to include only
the wave vectors up to $(3/2)G_{\rm cut}$. This is the case when
[PREC](../incar-tags/PREC.md)=Normal, which is the default.

If [NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md) and
[NGZ](../incar-tags/NGZ.md) are set manually to values that may lead to
sizeable [wrap-around
errors](../theory/Wrap-around_errors.md), a warning will
be printed in [OUTCAR](../output-files/OUTCAR.md) (search for the string
'wrap').

A hint that the [wrap-around
errors](../theory/Wrap-around_errors.md) may be too large
is given by the forces. If there is a considerable drift in the forces,
the FFT mesh should be increased. Search for the string 'total drift' in
the [OUTCAR](../output-files/OUTCAR.md) file that is located beneath the
line *TOTAL-FORCE*:

        total drift:                               -0.002730      0.010480      0.038560

The drift should definitely not exceed the magnitude of the forces, in
general it should be smaller than the size of the forces you are
interested in (usually 0.1 eV/Å).

### Mesh for the densities (fine mesh)\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Mesh for the densities (fine mesh)">edit</a> \| (./index.php.md)")\]

For the representation of the charge density, which contains the KS
orbitals to the power of 2, and other quantities like the augmentation
charges a second finer FFT mesh
([NGXF](../incar-tags/NGXF.md),[NGYF](../incar-tags/NGYF.md),[NGZF](../incar-tags/NGZF.md))
is used. With [PREC](../incar-tags/PREC.md)=Normal and Accurate, this fine
grid has a size
([NGXF](../incar-tags/NGXF.md),[NGYF](../incar-tags/NGYF.md),[NGZF](../incar-tags/NGZF.md))=$2\times$([NGX](../incar-tags/NGX.md),[NGY](../incar-tags/NGY.md),[NGZ](../incar-tags/NGZ.md)),
twice larger than the coarse grid. [NGX](../incar-tags/NGX.md),
[NGY](../incar-tags/NGY.md) and [NGZ](../incar-tags/NGZ.md) can also be set
manually.

The drift in the forces, for instance, may also be reduced by increasing
the number of points of the fine mesh.

Note that the [ENAUG](../incar-tags/ENAUG.md) tag can also be used to set
the size of the fine mesh, however this tag is **deprecated** and should
not be used anymore. Furthermore, it is active only with the
**deprecated** settings
[`PREC`](../incar-tags/PREC.md)` = Low, Medium or High`; otherwise it is
ignored.

### Support grid\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Support grid">edit</a> \| (./index.php.md)\]

For [`ADDGRID`](../incar-tags/ADDGRID.md)` = True`, an additional
'support' grid is used for the evaluation of the augmentation charges.
This grid has a size of $2\times$([NGXF](../incar-tags/NGXF.md),[NGYF](../incar-tags/NGYF.md),[NGZF](../incar-tags/NGZF.md)),
i.e., it has twice more points that the fine grid along each lattice
vector. The support grid often helps to reduce the noise in the forces,
however as explained in more detail in the documentation of
[ADDGRID](../incar-tags/ADDGRID.md) it should be used with caution.

# Example: volume relaxation and pressure\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Example: volume relaxation and pressure">edit</a> \| (./index.php.md)\]

An illustration of the effect of the energy cutoff
([ENCUT](../incar-tags/ENCUT.md)) on the results is given for the
equilibrium volume and pressure of diamond. It clearly shows the noise
induced by using an unconverged value for [ENCUT](../incar-tags/ENCUT.md).
See the how-to pages on [volume
relaxation](../methods/Volume_relaxation.md) and avoiding
[Pulay stress](Pulay_stress.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=Energy_cutoff_and_FFT_meshes&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ENCUT](../incar-tags/ENCUT.md), [PREC](../incar-tags/PREC.md),
[ADDGRID](../incar-tags/ADDGRID.md), [ENAUG](../incar-tags/ENAUG.md),
[NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md), [NGZ](../incar-tags/NGZ.md),
[NGXF](../incar-tags/NGXF.md), [NGYF](../incar-tags/NGYF.md),
[NGZF](../incar-tags/NGZF.md)

[Projector-augmented-wave
formalism](../methods/Projector-augmented-wave_formalism.md),
[wrap-around errors](../theory/Wrap-around_errors.md),
[volume relaxation](../methods/Volume_relaxation.md), [Pulay
stress](Pulay_stress.md)



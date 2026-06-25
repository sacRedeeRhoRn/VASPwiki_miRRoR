<!-- Source: https://vasp.at/wiki/index.php/Computing_the_phonon_dispersion_and_DOS | revid: 36048 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Computing the phonon dispersion and DOS


After computing the force constants using the [finite
differences](Phonons_from_finite_differences.md)
or [density-functional-perturbation
theory](Phonons_from_density-functional-perturbation_theory.md)
(DFPT) approaches, it is possible to compute the phonon dispersion
relation as well as the phonon density of states (DOS). This is
accomplished by Fourier interpolating the interatomic force constants
from a supercell calculation to the primitive cell.


## Contents


- [1 Phonon
  dispersion: Step-by-step
  instructions](#phonon-dispersion-step-by-step-instructions)
  - [1.1 Step 1:
    Compute the force
    constants](#step-1-compute-the-force-constants)
  - [1.2 Step 2:
    Provide **q**-points along a high-symmetry
    path](#step-2-provide-q-points-along-a-high-symmetry-path)
  - [1.3 Step 3:
    Compute the phonon
    dispersion](#step-3-compute-the-phonon-dispersion)
  - [1.4 Reading of
    force constants](#reading-of-force-constants)
- [2 Phonon DOS:
  Step-by-step
  instructions](#phonon-dos-step-by-step-instructions)
  - [2.1 Step 1:
    Compute the force
    constants](#step-1-compute-the-force-constants-1)
  - [2.2 Step 2:
    Specify a uniform **q**-point
    mesh](#step-2-specify-a-uniform-q-point-mesh)
  - [2.3 Step 3:
    Compute the DOS](#step-3-compute-the-dos)
- [3 Polar
  materials](#polar-materials)
  - [3.1 Obtaining
    the dielectric
    properties](#obtaining-the-dielectric-properties)
  - [3.2 Specifying
    the dielectric properties as
    input](#specifying-the-dielectric-properties-as-input)
  - [3.3 LO-TO
    splitting](#lo-to-splitting)
- [4 Practical
  hints](#practical-hints)
- [5 Related tags
  and articles](#related-tags-and-articles)
- [6
  References](#references)


## Phonon dispersion: Step-by-step instructions\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Phonon dispersion: Step-by-step instructions">edit</a> \| (./index.php.md)\]

### Step 1: Compute the force constants\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Compute the force constants">edit</a> \| (./index.php.md)\]

There are two possible approaches for computing the force constants and
then building the dynamical matrix:

1.  Using [finite
    differences](Phonons_from_finite_differences.md)
    with [`IBRION`](../incar-tags/IBRION.md)` = 5, 6`.
2.  Using
    [DFPT](Phonons_from_density-functional-perturbation_theory.md)
    with [`IBRION`](../incar-tags/IBRION.md)` = 7, 8`.

These calculations must be performed in a supercell so that the force
constants vanish at large distances.

|  |
|----|
| **Important:** The phonon frequencies need to be converged with respect to the supercell size. |

### Step 2: Provide **q**-points along a high-symmetry path\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Provide q-points along a high-symmetry path">edit</a> \| (./index.php.md)\]

Create a [QPOINTS](../input-files/QPOINTS.md) file containing a
**q**-points path at which the phonon dispersion is computed. This is
accomplished using the [line
mode](../input-files/KPOINTS.md) of the
[KPOINTS](../input-files/KPOINTS.md)-file format. External
tools[^bilbao:kvec-1][^seekpath-2]
are useful to decide which paths in the Brillouin zone to include. The
tools provide the coordinates and the labels for a given structure.

### Step 3: Compute the phonon dispersion\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Compute the phonon dispersion">edit</a> \| (./index.php.md)\]

To compute the phonon dispersion, set
[`LPHON_DISPERSION`](../incar-tags/LPHON_DISPERSION.md)` = true`
in the [INCAR](../input-files/INCAR.md) file. The amount of information
written to the [OUTCAR](../output-files/OUTCAR.md) file can be tuned using
the [PHON_NWRITE](../incar-tags/PHON_NWRITE.md) tag.

### Reading of force constants\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Reading of force constants">edit</a> \| (./index.php.md)\]

Steps 1-3 can be performed in one VASP calculation. However, generating
the finite displacements in the supercell to compute force constants is
time-consuming. It is possible to skip that step by providing force
constants from a previous run. Rename the
[vaspout.h5](../output-files/Vaspout.h5.md) output file from the
previous calculation to [vaspin.h5](../input-files/Vaspin.h5.md), set

     LPHON_READ_FORCE_CONSTANTS = True 
     LPHON_DISPERSION = True

and provide a [QPOINTS](../input-files/QPOINTS.md) file.

## Phonon DOS: Step-by-step instructions\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Phonon DOS: Step-by-step instructions">edit</a> \| (./index.php.md)\]

### Step 1: Compute the force constants\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Compute the force constants">edit</a> \| (./index.php.md)\]

Same as
[above](#Phonon_dispersion:_Step-by-step_instructions#Step_1:_Compute_the_force_constants).
This can be skipped by providing force constants in
[vaspin.h5](../input-files/Vaspin.h5.md) and setting
[`LPHON_READ_FORCE_CONSTANTS`](../incar-tags/LPHON_READ_FORCE_CONSTANTS.md)` = True`.

### Step 2: Specify a uniform **q**-point mesh\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Specify a uniform q-point mesh">edit</a> \| (./index.php.md)\]

Create a [QPOINTS](../input-files/QPOINTS.md) file that specifies a
sufficiently dense, uniform **q**-point mesh.

### Step 3: Compute the DOS\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Compute the DOS">edit</a> \| (./index.php.md)\]

Set [`PHON_DOS`](../incar-tags/PHON_DOS.md)` > 0` in the
[INCAR](../input-files/INCAR.md) file. The DOS is computed between
$\[\omega_{\text{min}}-5\sigma,\omega_{\text{max}}+5\sigma\]$ with $\omega_{\text{min}}$ and $\omega_{\text{max}}$ the lowest and highest phonon frequency and
$\sigma$ the broadening
([PHON_SIGMA](../incar-tags/PHON_SIGMA.md)).

The number of energy points in this energy range is specified by the
[PHON_NEDOS](../incar-tags/PHON_NEDOS.md) tag. To use a
Gaussian-smearing method for the computation of the DOS set
[`PHON_DOS`](../incar-tags/PHON_DOS.md)` = 1` or to use the tetrahedron
method set [`PHON_DOS`](../incar-tags/PHON_DOS.md)` = 2`.

## Polar materials\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Polar materials">edit</a> \| (./index.php.md)\]

If the material is polar, i.e., two or more atoms in the unit cell carry
non-zero Born effective charge tensors, the long-range dipole-dipole
interaction has to be treated by [Ewald
summation](../theory/Phonons-_Theory.md).
This is achieved by setting
[`LPHON_POLAR`](../incar-tags/LPHON_POLAR.md)` = True`, supplying the
static dielectric tensor
([PHON_DIELECTRIC](../incar-tags/PHON_DIELECTRIC.md)) and the
Born-effective charges
([PHON_BORN_CHARGES](../incar-tags/PHON_BORN_CHARGES.md)). The
values for these dielectric properties have to be obtained from a
separate VASP calculation in the unit cell setting
[LEPSILON](../incar-tags/LEPSILON.md) or
[LCALCEPS](../incar-tags/LCALCEPS.md).

|  |
|----|
| **Important:** Make sure to properly converge this unit-cell calculation with respect to the k-point mesh ([KPOINTS](../input-files/KPOINTS.md)) and the electronic cutoff energy ([ENCUT](../incar-tags/ENCUT.md)) since the optical phonon frequencies depend strongly on the dielectric properties. |

Optionally, specify a reciprocal space cutoff radius
([PHON_G_CUTOFF](../incar-tags/PHON_G_CUTOFF.md)) for the Ewald
summation.

### Obtaining the dielectric properties\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Obtaining the dielectric properties">edit</a> \| (./index.php.md)\]

After a successful linear-response calculation using either
[LEPSILON](../incar-tags/LEPSILON.md) or
[LCALCEPS](../incar-tags/LCALCEPS.md), VASP writes the Born effective
charge tensor and the ion-clamped static dielectric tensor to
[OUTCAR](../output-files/OUTCAR.md),
[vasprun.xml](../output-files/Vasprun.xml.md) and
[vaspout.h5](../output-files/Vaspout.h5.md).

|  |
|----|
| **Mind:** The [vaspout.h5](../output-files/Vaspout.h5.md) file is only available if VASP is compiled with [HDF5 support](../categories/Category-HDF5_support.md). |

Here is an example output for a system consisting of two atoms per cell
(MgO) in the [OUTCAR](../output-files/OUTCAR.md) file:

     MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in DFT)
     ------------------------------------------------------
               3.130368    -0.000000    -0.000000
               0.000000     3.130368     0.000000
              -0.000000     0.000000     3.130368

and

     BORN EFFECTIVE CHARGES (including local field effects) (in |e|, cummulative output)
     ---------------------------------------------------------------------------------
     ion    1
        1     1.97026     0.00000    -0.00000
        2    -0.00000     1.97026     0.00000
        3    -0.00000     0.00000     1.97026
     ion    2
        1    -1.97026    -0.00000     0.00000
        2     0.00000    -1.97026    -0.00000
        3     0.00000    -0.00000    -1.97026

The corresponding XML entries in the
[vasprun.xml](../output-files/Vasprun.xml.md) file can be queried with
the following XPath queries:

    /modeling/calculation/array[@name="born_charges"]
    /modeling/calculation/varray[@name="dielectric_dft"]

Finally, the same information is also available in the
[vaspout.h5](../output-files/Vaspout.h5.md) binary file at the following
dataset locations:

    results/born_charges/born_charges
    results/dielectric/dielectric_dft

### Specifying the dielectric properties as input\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Specifying the dielectric properties as input">edit</a> \| (./index.php.md)\]

Once the Born effective charges and the ion-clamped static dielectric
tensor have been retrieved, they need to be specified in the
[INCAR](../input-files/INCAR.md) file of the supercell calculation via their
respective tags
([PHON_BORN_CHARGES](../incar-tags/PHON_BORN_CHARGES.md) and
[PHON_DIELECTRIC](../incar-tags/PHON_DIELECTRIC.md)). Each tensor
is specified row by row as a list of real numbers. Line breaks can
optionally be inserted using the "`\`" character to improve readability.
For example, the values from the MgO calculation above could be
specified as follows:

    PHON_DIELECTRIC = \
      3.13036840     -0.00000000     -0.00000000 \
      0.00000000      3.13036840      0.00000000 \
     -0.00000000      0.00000000      3.13036840

    PHON_BORN_CHARGES = \
        1.97025920     -0.00000000     -0.00000000 \
        0.00000000      1.97025920      0.00000000 \
       -0.00000000      0.00000000      1.97025920 \
    \
       -1.97025920      0.00000000      0.00000000 \
       -0.00000000     -1.97025920     -0.00000000 \
        0.00000000     -0.00000000     -1.97025920

### LO-TO splitting\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: LO-TO splitting">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:MgO-phonons-LR-comparison.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/3/31/MgO-phonons-LR-comparison.png/400px-MgO-phonons-LR-comparison.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/3/31/MgO-phonons-LR-comparison.png/600px-MgO-phonons-LR-comparison.png 1.5x, /wiki/images/3/31/MgO-phonons-LR-comparison.png 2x"
width="400" height="221" /></a>
<figcaption>Phonon dispersion relation of MgO (rock-salt) comparing
calculations with and without long-range (LR) dipole corrections. Notice
the strong splitting of frequencies at the Γ-point.</figcaption>
</figure>

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:AlN-phonons-LR-comparison.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/fb/AlN-phonons-LR-comparison.png/400px-AlN-phonons-LR-comparison.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/fb/AlN-phonons-LR-comparison.png/600px-AlN-phonons-LR-comparison.png 1.5x, /wiki/images/f/fb/AlN-phonons-LR-comparison.png 2x"
width="400" height="219" /></a>
<figcaption>Phonon dispersion relation of AlN (wurtzite) comparing
calculations with and without long-range (LR) dipole corrections. Notice
the discontinuities around the Γ-point.</figcaption>
</figure>

As described on the [theory
page](../theory/Phonons-_Theory.md),
the presence of long-range electrostatic interactions leads to the
splitting of the longitudinal optical (LO) from the transverse optical
(TO) phonon modes. Once the required dielectric properties are provided
and [`LPHON_POLAR`](../incar-tags/LPHON_POLAR.md)` = True` is set,
VASP automatically considers the long-range dipole-dipole contributions
to the interatomic force constants for phonon calculations.

To illustrate the importance of long-range dipole corrections, we show
two calculations of phonons in polar materials with strong LO-TO
splitting. First is MgO, which forms an ionic rock-salt crystal
structure (face-centered cubic). The corresponding figure shows a
comparison against a calculation that does not include the long-range
dipole corrections. Both calculations were performed in a `4x4x4`
supercell with only the Γ-point in the k-point mesh. In the case of MgO,
the magnitude of the LO-TO splitting is considerably large, on the same
order of magnitude as the LO phonon frequencies. Notice also the
improved smoothness of the phonon bands when long-range corrections are
included. Otherwise the interpolation procedure is prone to
overshooting, resulting in unwanted oscillations.

The second example is AlN in the hexagonal wurtzite structure. This
structure is less isotropic than the rock-salt structure of MgO. In this
case, the Born effective charges and dielectric constants associated
with different spatial directions can be different. The phonon
frequencies obtained by including the long-range dipole corrections are
therefore more dependent on the direction of the phonon wave vector,
$\mathbf{q}$. This results in discontinuities around the
Γ-point when $\mathbf{q} \to \mathbf{0}$, as shown in the accompanying figure.

## Practical hints\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Practical hints">edit</a> \| (./index.php.md)\]

- Bear in mind that the choice of exchange-correlation functional (e.g.,
  GGA or hybrid functionals) can have a big impact on the [Born
  effective
  charges](Born_effective_charges.md) and
  the [dielectric
  function](../categories/Category-Dielectric_properties.md),
  and thereby the LO-TO splitting and phonon dispersion.

## Related tags and articles\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QPOINTS](../input-files/QPOINTS.md),
[LPHON_DISPERSION](../incar-tags/LPHON_DISPERSION.md),
[PHON_NWRITE](../incar-tags/PHON_NWRITE.md),
[LPHON_POLAR](../incar-tags/LPHON_POLAR.md),
[PHON_DIELECTRIC](../incar-tags/PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](../incar-tags/PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](../incar-tags/PHON_G_CUTOFF.md)

## References\[<a
href="/wiki/index.php?title=Computing_the_phonon_dispersion_and_DOS&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^bilbao:kvec-1]: [www.cryst.ehu.es/cryst/get_kvec.html (2022).](https://www.cryst.ehu.es/cryst/get_kvec.html)
[^seekpath-2]: [www.materialscloud.org/work/tools/seekpath (2022).](https://www.materialscloud.org/work/tools/seekpath)

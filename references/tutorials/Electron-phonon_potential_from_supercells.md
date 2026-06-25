<!-- Source: https://vasp.at/wiki/index.php/Electron-phonon_potential_from_supercells | revid: 34109 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Electron-phonon potential from supercells


The computation of the electron-phonon potential,
$\partial_{\nu \mathbf{q}} V(\mathbf{r})$, is a
prerequisite for the calculation of the electron-phonon matrix element:

$g_{mn \mathbf{k}, \nu \mathbf{q}} \equiv \langle \psi_{m \mathbf{k} +
\mathbf{q}} | \partial_{\nu \mathbf{q}} V | \psi_{n \mathbf{k}}
\rangle .$

$\partial_{\nu \mathbf{q}} V$ is computed from a
supercell calculation by means of Fourier interpolation while the Bloch
orbitals, $\psi_{n
\mathbf{k}}(\mathbf{r})$, are computed directly in the
primitive cell. The supercell calculation and the primitive-cell
calculation are performed in two separate VASP runs. This page provides
an overview of the supercell calculation and how the electron-phonon
potential can be calculated. For information regarding the
electron-phonon calculation in the primitive cell, consult the
documentation on [phonon-induced bandstructure
renormalization](Bandgap_renormalization_due_to_electron-phonon_coupling.md)
and on [phonon-limited
transport](Transport_coefficients_including_electron-phonon_scattering.md).

For the theory on the electron-phonon potential, see the end of the
self-energy section of the [theory
page](../theory/Electron-phonon_interactions_theory.md).

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

|  |
|----|
| **Important:** This feature requires [HDF5 support](../categories/Category-HDF5_support.md). |

|  |
|----|
| **Tip:** The entire workflow of initializing a calculation, computing the electron-phonon potential in the supercell and performing subsequent electron-phonon calculations in the primitive cell can be facilitated by `velph`. `velph` is a command-line tool included in the <a href="https://github.com/phonopy/phelel" class="external text"
rel="nofollow">phelel</a> python package. It helps guide you through the process step by step and ensures a certain level of consistency between the required VASP calculations. |


## Contents


- [1 Finite
  displacements in the
  supercell](#finite-displacements-in-the-supercell)
  - [1.1 VASP
    internal driver](#vasp-internal-driver)
  - [1.2 VASP and
    phelel](#vasp-and-phelel)
- [2 Practical
  hints](#practical-hints)
- [3 Related tags
  and articles](#related-tags-and-articles)


## Finite displacements in the supercell\[<a
href="/wiki/index.php?title=Electron-phonon_potential_from_supercells&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Finite displacements in the supercell">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Elphon-workflow.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/44/Elphon-workflow.png/400px-Elphon-workflow.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/44/Elphon-workflow.png/600px-Elphon-workflow.png 1.5x, /wiki/images/thumb/4/44/Elphon-workflow.png/800px-Elphon-workflow.png 2x"
width="400" height="192" /></a>
<figcaption>General workflow when running electron-phonon calculations
using perturbation theory. Notice that both the "VASP only" workflow as
well as the "VASP + phelel" workflow produce the same kind of data in <a
href="/wiki/Phelel_params.hdf5"
title="Phelel params.hdf5">phelel_params.hdf5</a>.</figcaption>
</figure>

The electron-phonon potential is computed from finite atomic
displacements in a sufficiently large supercell. In this case,
sufficient means that the effects of an atomic displacement become
negligible at about half the supercell size. Usually, converging the
phonon frequencies is a good way of finding a supercell that is
sufficiently large. Polar materials can exhibit long-range electrostatic
interactions that go beyond reasonable supercell sizes. In this case, a
[correction
scheme](Bandgap_renormalization_due_to_electron-phonon_coupling.md)
exists that explicitly treats the long-range dipole interactions and
works with smaller cells.

Currently, there are two complementary ways to calculate the
electron-phonon potential. One relies solely on VASP, while the other
uses VASP in combination with
<a href="https://github.com/phonopy/phelel" class="external text"
rel="nofollow">phelel</a>. Both approaches calculate the derivative of
the Kohn-Sham potential in real space via the displacement of atoms.
However, they may differ in terms of flexibility and computational
performance. Below, we describe the general workflow of each approach
and highlight their advantages and disadvantages.

Regardless of which approach is chosen, the output is always written to
the [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
binary file. This file can then be read during a VASP calculation in the
primitive unit cell to compute electron-phonon interactions.

### VASP internal driver\[<a
href="/wiki/index.php?title=Electron-phonon_potential_from_supercells&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: VASP internal driver">edit</a> \| (./index.php.md)\]

This way of calculating the electron-phonon potential is activated by
setting
[`ELPH_POT_GENERATE`](../incar-tags/ELPH_POT_GENERATE.md)` = True`
in the [INCAR](../input-files/INCAR.md) file. It utilizes the VASP-internal
finite-difference driver that is activated by setting
[`IBRION`](../incar-tags/IBRION.md)` = 6` in the
[INCAR](../input-files/INCAR.md) file. The atomic displacement directions
are automatically determined by VASP. As usual,
[POTIM](../incar-tags/POTIM.md) and [NFREE](../incar-tags/NFREE.md) can be
used to control the displacement amount and finite-difference stencil,
respectively. This is the same procedure used to calculate [phonons from
finite
differences](Phonons_from_finite_differences.md)
and many of the same considerations regarding performance and accuracy
apply in this case. Therefore, phonon frequencies are a great way to
test the convergence with respect to supercell size.

|  |
|----|
| **Mind:** Currently, VASP generates more displacements with [`ELPH_POT_GENERATE`](../incar-tags/ELPH_POT_GENERATE.md)` = True` and [`IBRION`](../incar-tags/IBRION.md)` = 6` than would be required in principle. This will be improved in a future version of the code. |

Once the electron-phonon potential is obtained, it is automatically
mapped to the primitive cell. The results are stored in the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. By default, the primitive cell used for this mapping is the one
determined by VASP during the supercell calculation. It is possible to
choose a different primitive unit cell by explicitly specifying its
lattice vectors using the
[ELPH_POT_LATTICE](../incar-tags/ELPH_POT_LATTICE.md)
[INCAR](../input-files/INCAR.md) tag.

|  |
|----|
| **Mind:** The cell specified via [ELPH_POT_LATTICE](../incar-tags/ELPH_POT_LATTICE.md) must be a valid primitive cell of the underlying lattice. |

In any case, the relevant primitive-cell structure is written to the
[CONTCAR_ELPH](../output-files/CONTCAR_ELPH.md) file. This file can be
used as the [POSCAR](../input-files/POSCAR.md) of the subsequent
electron-phonon calculation in the primitive cell. This way, it is
guaranteed that the primitive-cell calculation is compatible with the
information contained in the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file.

The electron-phonon potential is stored on a real-space FFT grid in the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. It is currently necessary to match the FFT grid dimensions of this
potential to the FFT grid dimensions ([NGX](../incar-tags/NGX.md),
[NGY](../incar-tags/NGY.md), [NGZ](../incar-tags/NGZ.md)) of the primitive cell
that is used to perform the subsequent electron-phonon calculation. By
default, VASP determines appropriate FFT grid dimensions automatically
during the supercell calculation based on the current
[ENCUT](../incar-tags/ENCUT.md). The result should be compatible with a
primitive-cell calculation that uses the same
[ENCUT](../incar-tags/ENCUT.md).

|  |
|----|
| **Tip:** The [PREC](../incar-tags/PREC.md) [INCAR](../input-files/INCAR.md) tag influences the size of the FFT mesh. Therefore, it is recommended to choose the same [PREC](../incar-tags/PREC.md) for both the supercell as well as the primitive-cell calculation. |

It is possible to manually supply the FFT grid dimensions of the target
unit cell during the supercell calculation via
[ELPH_POT_FFT_MESH](../incar-tags/ELPH_POT_FFT_MESH.md).

Information regarding the primitive cell and the FFT grid dimensions for
electron-phonon calculations is also reported in the
[OUTCAR](../output-files/OUTCAR.md) file and the
[vaspout.h5](../output-files/Vaspout.h5.md) file. The format is
explained on the
[ELPH_POT_GENERATE](../incar-tags/ELPH_POT_GENERATE.md) page.

### VASP and phelel\[<a
href="/wiki/index.php?title=Electron-phonon_potential_from_supercells&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: VASP and phelel">edit</a> \| (./index.php.md)\]

In this approach to calculating the electron-phonon potential, the ionic
displacements are determined externally using
<a href="https://github.com/phonopy/phelel" class="external text"
rel="nofollow">phelel</a>. For people who are familiar with phonon
calculations using VASP and
<a href="https://github.com/phonopy/phonopy" class="external text"
rel="nofollow">phonopy</a>, this workflow will look very familiar. In
general, this allows for greater flexibility. Here, we demonstrate a
common workflow that suffices for most purposes. For a complete list of
features, we refer to the documentation of
<a href="https://github.com/phonopy/phelel" class="external text"
rel="nofollow">phelel</a>.

As an example,

    phelel -d --dim 2 2 2 -c POSCAR-unitcell --pm

automatically determines displacement directions for a 2x2x2 supercell
based on symmetry considerations.

|  |
|----|
| **Tip:** We recommend the use of the `--pm` option, which generates positive and negative displacements for each displacement direction. |

For each displacement, phelel creates a corresponding supercell
[POSCAR](../input-files/POSCAR.md) file (`POSCAR-XXX`, where `XXX` labels
the different displacements). In addition, the file `SPOSCAR` is created
which contains the supercell geometry in equilibrium.

For each of the generated POSCAR files, create a separate directory and
run VASP there with
[`ELPH_PREPARE`](../incar-tags/ELPH_PREPARE.md)` = True` set in the
[INCAR](../input-files/INCAR.md) file. This setting instructs VASP to write
the potential as well as other important information to disk. Finally,
run phelel to combine all the data from the individual directories to
obtain the electron-phonon potential, for example,

    phelel --fft-mesh 18 18 18 --cd perfect/ disp-001/ disp-002/

Here, `perfect`, `disp-001` and `disp-002` are the directories
corresponding to the equilibrium and displaced supercell calculations,
respectively. `--fft-mesh` specifies the FFT grid dimensions
([NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md), [NGZ](../incar-tags/NGZ.md))
to be used in the final electron-phonon calculation in the primitive
cell. The electron-phonon potential is Fourier interpolated from the FFT
grid in the supercell to the supplied grid via a non-uniform FFT. The
results are written to the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file.

## Practical hints\[<a
href="/wiki/index.php?title=Electron-phonon_potential_from_supercells&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Practical hints">edit</a> \| (./index.php.md)\]

- You cannot know a priori how large a supercell to use; convergence
  tests must be performed. Even very large supercells can have noise, so
  it is important to start with a small cell and then work up to denser
  k- and q-points meshes, as well as larger supercells.
- If you have imaginary frequencies during an electron-phonon
  calculation, the calculation will simply stop. This is an indication
  of improper convergence. You can work around this using
  [ELPH_IGNORE_IMAG_PHONONS](../incar-tags/ELPH_IGNORE_IMAG_PHONONS.md)
  to ignore the imaginary modes. This may be useful even for stable
  structures with small imaginary modes.

## Related tags and articles\[<a
href="/wiki/index.php?title=Electron-phonon_potential_from_supercells&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Band-structure
  renormalization](Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](Transport_coefficients_including_electron-phonon_scattering.md)
- [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
- [Electron-phonon interactions from Monte-Carlo
  sampling](Electron-phonon_interactions_from_Monte-Carlo_sampling.md)



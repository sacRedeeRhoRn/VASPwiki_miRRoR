<!-- Source: https://vasp.at/wiki/index.php/ELPH_POT_GENERATE | revid: 32886 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_POT_GENERATE


ELPH_POT_GENERATE =
\[logical\]  
Default: **ELPH_POT_GENERATE** = False 

Description: Calculates the electron-phonon potential from finite atomic
displacements.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Performing electron-phonon calculations using [many-body perturbation
theory](../categories/Category-Electron-phonon_interactions.md)
requires as input a
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. Setting
`ELPH_POT_GENERATE`` = True`
provides a way to generate the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md) file
directly in VASP by [computing the electron-phonon
potential](../tutorials/Electron-phonon_potential_from_supercells.md).
This is accomplished by using finite atomic displacements in a
supercell. Therefore, in addition to setting
`ELPH_POT_GENERATE`` = True`,
it is necessary to set [`IBRION`](IBRION.md)` = 6` to
activate the finite-difference routines.

|  |
|----|
| **Mind:** We currently do not support all symmetry operations when considering the atomic displacements for `ELPH_POT_GENERATE`` = True`. Therefore, more atomic displacements are generated compared to typical finite-difference calculations using [`IBRION`](IBRION.md)` = 6`. |

When
`ELPH_POT_GENERATE`` = True`,
VASP will additionally produce the
[CONTCAR_ELPH](../output-files/CONTCAR_ELPH.md) file. This file
contains the primitive-cell crystal structure in the
[POSCAR](../input-files/POSCAR.md) format and can directly be used as input
for the subsequent electron-phonon calculation. The primitive cell is
automatically determined by VASP during the supercell calculation, but
can optionally be specified via the
[ELPH_POT_LATTICE](ELPH_POT_LATTICE.md) tag.

Finally, the electron-phonon potential in the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md) file
is computed on a real-space FFT grid that has to match exactly the FFT
grid dimensions ([NGX](NGX.md), [NGY](NGY.md),
[NGZ](NGZ.md)) of the primitive cell used in the subsequent
electron-phonon calculation. The dimensions of the FFT grid used to
compute the electron-phonon potential can be chosen via the
[ELPH_POT_FFT_MESH](ELPH_POT_FFT_MESH.md) tag. If
one does not specify an FFT grid explicitly, VASP will determine the FFT
grid dimensions automatically based on the current
[ENCUT](ENCUT.md). This should produce an FFT mesh for the
electron-phonon potential that is compatible with the FFT mesh used in a
primitive-cell calculation at the same [ENCUT](ENCUT.md).

|  |
|----|
| **Tip:** The [PREC](PREC.md) [INCAR](../input-files/INCAR.md) tag influences the size of the FFT mesh. Therefore, it is recommended to choose the same [PREC](PREC.md) for both the supercell as well as the primitive-cell calculation. |

Basic information about the primitive-cell geometry and FFT grid is
written to the [OUTCAR](../output-files/OUTCAR.md) file in the following
format:

     Generation of phelel_params.hdf5
     ================================

    Primitive cell 
       a1 =     1.78093078    1.78093078    0.00000000
       a2 =     0.00000000    1.78093078    1.78093078
       a3 =     1.78093078    0.00000000    1.78093078

    Primitive FFT mesh =     18    18    18

It is also written to the machine-readable
[vaspout.h5](../output-files/Vaspout.h5.md) file at the following HDF5
paths:

    results/elph_potential/primitive_positions
    results/elph_potential/primitive_fft_mesh

This information is already contained within the generated
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. However, it is mirrored in the standard output to make it easier
for users to check their calculations and to automate workflows.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_POT_GENERATE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_POT_LATTICE](ELPH_POT_LATTICE.md)
- [ELPH_POT_FFT_MESH](ELPH_POT_FFT_MESH.md)
- [IBRION](IBRION.md)
- [Electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)
- [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
- [CONTCAR_ELPH](../output-files/CONTCAR_ELPH.md)



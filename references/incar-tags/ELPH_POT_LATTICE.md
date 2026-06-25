<!-- Source: https://vasp.at/wiki/index.php/ELPH_POT_LATTICE | revid: 32887 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_POT_LATTICE


ELPH_POT_LATTICE = \[3x3
real\] 

Description: Allows specifying an alternative primitive cell for the
mapping of the electron-phonon potential.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Once the electron-phonon potential [has been computed in the
supercell](../tutorials/Electron-phonon_potential_from_supercells.md),
it needs to be mapped to the primitive cell. This is done via
[`ELPH_POT_GENERATE`](ELPH_POT_GENERATE.md)` = True`.
By default, VASP performs the mapping for the primitive cell that is
found by the symmetry routines and that is reported in the
[OUTCAR](../output-files/OUTCAR.md) file. In cases where the primitive cell
needs to be specified manually,
ELPH_POT_LATTICE can be used.

`ELPH_POT_LATTICE`` = a1x a1y a1z a2x a2y a2z a3x a3y a3z`
specifies the three primitive lattice vectors
$\mathbf{a}_1$, $\mathbf{a}_2$ and $\mathbf{a}_3$ in Cartesian coordinates. These lattice vectors are
then used to construct the primitive-cell information in the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file.

|  |
|----|
| **Mind:** The supplied lattice vectors must span a valid primitive cell of the supercell or the code will exit with an error. |

|  |
|----|
| **Tip:** The primitive cell used for mapping is also written to the [CONTCAR_ELPH](../output-files/CONTCAR_ELPH.md) file, which can conveniently be used as the [POSCAR](../input-files/POSCAR.md) input for the subsequent electron-phonon calculation. This ensures that the primitive-cell calculation is consistent with the information in the [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md) file. |

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_POT_LATTICE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_POT_GENERATE](ELPH_POT_GENERATE.md)
- [ELPH_POT_FFT_MESH](ELPH_POT_FFT_MESH.md)
- [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
- [CONTCAR_ELPH](../output-files/CONTCAR_ELPH.md)
- [Electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)



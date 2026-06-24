<!-- Source: https://vasp.at/wiki/index.php/ELPH_POT_FFT_MESH | revid: 29446 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_POT_FFT_MESH
ELPH_POT_FFT_MESH = \[real real real\] 

Description: Specifies the FFT mesh for mapping the electron-phonon
potential to the primitive cell.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Once the electron-phonon potential [has been computed in the
supercell](../tutorials/Electron-phonon_potential_from_supercells.md),
it needs to be mapped to the primitive cell. By default, VASP chooses
the primitive-cell FFT mesh to be consistent with the current
[ENCUT](ENCUT.md). However, sometimes it might be necessary
to specify the FFT grid dimensions manually via ELPH_POT_FFT_MESH.

The chosen values must be the same as the desired
[NGX](NGX.md), [NGY](NGY.md) and
[NGZ](NGZ.md) of the electron-phonon calculation in the
primitive cell.

|  |
|----|
| **Tip:** In order to find the FFT grid dimensions corresponding to the primitive cell, you can start a minimal VASP calculation in the primitive cell and extract the values for [NGX](NGX.md), [NGY](NGY.md) and [NGZ](NGZ.md) from the [OUTCAR](../output-files/OUTCAR.md) file. |

## Related tags and articles
- [ELPH_POT_GENERATE](ELPH_POT_GENERATE.md)
- [ELPH_POT_LATTICE](ELPH_POT_LATTICE.md)
- [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
- [CONTCAR_ELPH](../output-files/CONTCAR_ELPH.md)
- [Electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)

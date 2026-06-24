<!-- Source: https://vasp.at/wiki/index.php/ELPH_PREPARE | revid: 32888 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_PREPARE
ELPH_PREPARE = \[logical\]  
Default: **ELPH_PREPARE** = .FALSE. 

Description: Writes the potential, the force-constants and other
information related to electron-phonon interactions to the
[vaspout.h5](../output-files/Vaspout.h5.md) file.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

In order to calculate electron-phonon interactions, one must first
[perform finite-difference calculations in the
supercell](../tutorials/Electron-phonon_potential_from_supercells.md)
and generate the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. To do this using [phelel](https://github.com/phonopy/phelel), it
is necessary to provide additional supercell information to phelel. This
is accomplished by setting `ELPH_PREPARE`` = True` in each involved
supercell calculation. Afterwards, phelel can be used to calculate the
required derivatives and produce the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. For further information on this workflow, please consult the
online documentation of [phelel](https://github.com/phonopy/phelel).

## Related tags and articles
- [Electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)
- [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)

<!-- Source: https://vasp.at/wiki/index.php/Phelel_params.hdf5 | revid: 32863 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# phelel_params.hdf5
  
The phelel_params.hdf5 file is used to calculate electron-phonon
interactions via [`ELPH_RUN`](../incar-tags/ELPH_RUN.md)` = True`. It
contains information related to the [interatomic force
constants](../redirects/Forces.md) and the
[derivative of the Kohn-Sham
potential](../tutorials/Electron-phonon_potential_from_supercells.md).

To generate the phelel_params.hdf5 file, you can either use the [VASP
internal
driver](../tutorials/Electron-phonon_potential_from_supercells.md)
via
[`ELPH_POT_GENERATE`](../incar-tags/ELPH_POT_GENERATE.md)` = True`
or use VASP in combination with
[phelel](https://github.com/phonopy/phelel).

## Related tags and articles
- [ELPH_POT_GENERATE](../incar-tags/ELPH_POT_GENERATE.md)
- [ELPH_RUN](../incar-tags/ELPH_RUN.md)
- [Electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)
- [HDF5 support](../categories/Category-HDF5_support.md)

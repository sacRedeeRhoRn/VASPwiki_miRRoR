<!-- Source: https://vasp.at/wiki/index.php/Phelel_params.hdf5 | revid: 32863 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# phelel_params.hdf5


  
The phelel_params.hdf5 file is
used to calculate electron-phonon interactions via
[`ELPH_RUN`](../incar-tags/ELPH_RUN.md)` = True`. It contains
information related to the
<a href="/wiki/Forces#Force_constants_and_phonons" class="mw-redirect"
title="Forces">interatomic force constants</a> and the [derivative of
the Kohn-Sham
potential](../tutorials/Electron-phonon_potential_from_supercells.md).

To generate the
phelel_params.hdf5 file, you
can either use the [VASP internal
driver](../tutorials/Electron-phonon_potential_from_supercells.md)
via
[`ELPH_POT_GENERATE`](../incar-tags/ELPH_POT_GENERATE.md)` = True`
or use VASP in combination with
<a href="https://github.com/phonopy/phelel" class="external text"
rel="nofollow">phelel</a>.

## Related tags and articles\[<a
href="/wiki/index.php?title=Phelel_params.hdf5&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_POT_GENERATE](../incar-tags/ELPH_POT_GENERATE.md)
- [ELPH_RUN](../incar-tags/ELPH_RUN.md)
- [Electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)
- [HDF5 support](../categories/Category-HDF5_support.md)



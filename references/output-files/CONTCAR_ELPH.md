<!-- Source: https://vasp.at/wiki/index.php/CONTCAR_ELPH | revid: 32897 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CONTCAR ELPH


The CONTCAR_ELPH file is an
output file of a [supercell
calculation](../tutorials/Electron-phonon_potential_from_supercells.md)
that contains the structural information of the primitive cell required
for [electron-phonon calculations using many-body perturbation
theory](../categories/Category-Electron-phonon_interactions.md).

|  |
|----|
| **Mind:** Available as of VASP 6.5.1 |

This file has the same format as the [CONTCAR](CONTCAR.md)
or [POSCAR](../input-files/POSCAR.md) file. It is typically generated
alongside the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md) file
by setting
[`ELPH_POT_GENERATE`](../incar-tags/ELPH_POT_GENERATE.md)` = True`.
The CONTCAR_ELPH file can be
renamed and used as the [POSCAR](../input-files/POSCAR.md) input for a
subsequent electron-phonon calculation in the primitive cell, e.g.
[band-structure
renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
or [transport coefficients including electron-phonon
scattering](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=CONTCAR_ELPH&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [CONTCAR](CONTCAR.md)
- [POSCAR](../input-files/POSCAR.md)
- [ELPH_POT_GENERATE](../incar-tags/ELPH_POT_GENERATE.md)
- [ELPH_POT_LATTICE](../incar-tags/ELPH_POT_LATTICE.md)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/LPHON_DISPERSION | revid: 18395 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LPHON_DISPERSION


LPHON_DISPERSION = .TRUE. \|
.FALSE. 

|                               |           |     |
|-------------------------------|-----------|-----|
| Default: **LPHON_DISPERSION** | = .FALSE. |     |

Description: LPHON_DISPERSION
requests the calculation of the phonon dispersion along the q-point path
supplied in file [QPOINTS](../input-files/QPOINTS.md) (same format as
[KPOINTS](../input-files/KPOINTS.md)).

------------------------------------------------------------------------

After the computation of the force constants using finite differences
([IBRION](IBRION.md)=5,6) or density-functional perturbation
theory ([IBRION](IBRION.md)=7,8) on a supercell it is
possible to compute the phonon dispersion for the equivalent primitive
cell determined by VASP by setting
LPHON_DISPERSION=.TRUE.

|  |
|----|
| **Mind:** Only available as of VASP 6.3.2. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LPHON_DISPERSION&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QPOINTS](../input-files/QPOINTS.md),
[PHON_NWRITE](PHON_NWRITE.md),
[LPHON_POLAR](LPHON_POLAR.md),
[PHON_DIELECTRIC](PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](PHON_G_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPHON_DISPERSION-_incategory-Examples)



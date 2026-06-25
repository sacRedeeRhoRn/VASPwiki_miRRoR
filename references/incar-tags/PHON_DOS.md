<!-- Source: https://vasp.at/wiki/index.php/PHON_DOS | revid: 18804 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PHON_DOS


PHON_DOS = 0 \| 1 \| 2 

|                       |     |     |
|-----------------------|-----|-----|
| Default: **PHON_DOS** | = 0 |     |

Description: Select the approach to use when computing the phonon
density-of-states (DOS).

------------------------------------------------------------------------

The possible values are

|  |  |
|----|----|
| PHON_DOS | Function |
| 0 | The phonon DOS computation is not performed. |
| 1 | A gaussian broadening function with a width specified by [PHON_SIGMA](PHON_SIGMA.md) is used. |
| 2 | The tetrahedron method is used. |

To get a representative density of states the
[QPOINTS](../input-files/QPOINTS.md) file should specify a regular mesh.
When line mode in the [QPOINTS](../input-files/QPOINTS.md) file and
gaussian smearing (PHON_DOS=1) is used, the phonon density of states
will still be computed but the results are not reliable.

|  |
|----|
| **Mind:** Only available as of VASP 6.4.0. |

## Related tags and articles\[<a href="/wiki/index.php?title=PHON_DOS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QPOINTS](../input-files/QPOINTS.md),
[PHON_NWRITE](PHON_NWRITE.md),
[LPHON_POLAR](LPHON_POLAR.md),
[PHON_DIELECTRIC](PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](PHON_G_CUTOFF.md),
[PHON_SIGMA](PHON_SIGMA.md),
[PHON_NEDOS](PHON_NEDOS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPHON_DISPERSION-_incategory-Examples)



<!-- Source: https://vasp.at/wiki/index.php/PHON_NWRITE | revid: 22586 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PHON_NWRITE


PHON_NWRITE = \[integer\] 

|                          |     |     |
|--------------------------|-----|-----|
| Default: **PHON_NWRITE** | = 1 |     |

Description: PHON_NWRITE
determines how much output is written to the
[OUTCAR](../output-files/OUTCAR.md) file when computing the phonon
dispersion
[LPHON_DISPERSION](LPHON_DISPERSION.md)=.TRUE.

------------------------------------------------------------------------

Positive numbers mean human-readable output, and negative numbers mean
one-line format. The available options are:

|  |  |
|----|----|
| PHON_NWRITE | Description |
| 2 | For each q point, write the same as 1 and then the phonon modes with the displacement of each atom in the three cartesian directions per line. |
| 1 | For each q point, q-point coordinates are written in one line and the phonon frequencies are written one branch per line in different units. |
| 0 | No phonon output is written to OUTCAR. |
| -1 | For each q point, only a single line is written containing q-point coordinates and frequencies. |
| -2 | For each q point, q-point coordinates and frequencies are written in separate blocks and frequencies are reported in different units. |
| -3 | Like -2, but in addition, the phonon eigenvectors are written for each q point. |

|  |
|----|
| **Mind:** Only available as of VASP 6.3.2. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PHON_NWRITE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QPOINTS](../input-files/QPOINTS.md),
[LPHON_DISPERSION](LPHON_DISPERSION.md),
[LPHON_POLAR](LPHON_POLAR.md),
[PHON_DIELECTRIC](PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](PHON_G_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPHON_DISPERSION-_incategory-Examples)



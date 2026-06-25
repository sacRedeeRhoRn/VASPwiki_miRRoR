<!-- Source: https://vasp.at/wiki/index.php/NGYROMAG | revid: 30749 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NGYROMAG


NGYROMAG = \[real array\]  
Default: **NGYROMAG** = NTYP\*1.0 

Description: NGYROMAG
specifies the nuclear gyromagnetic ratios (in MHz, for H<sub>0</sub> = 1
T) for the atomic types on the [POTCAR](../input-files/POTCAR.md) file.

------------------------------------------------------------------------

By means of the NGYROMAG-tag
one can specify the nuclear gyromagnetic ratio:

    NGYROMAG = gamma_1  gamma_2 ... gamma_N

where one should specify one number for each of the *N* species on the
[POSCAR](../input-files/POSCAR.md) file, i.e. if C, H, N, and O are listed
as species in the [POSCAR](../input-files/POSCAR.md) file, then there
should be four numbers in
NGYROMAG, regardless of how
many total atoms there are.

|  |
|----|
| **Important:** If one does not set NGYROMAG in the [INCAR](../input-files/INCAR.md) file, VASP assumes a factor of 1 for each species. |

NGYROMAG is given in units of
MHz/T, see Ref.
[^gyromag:web-1]
for a table of different gyromagnetic ratios. A more extensive list is
available on
[^gyromag:database:web-2]
which converts isotopic magnetic moments from Ref.
[^gyromag:book:2019-3]
and converts them using the definition of the gyromagnetic ratio defined
in Ref.
[^tiesinga:revmodphys:2021-4].

## Related tags and articles\[<a href="/wiki/index.php?title=NGYROMAG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LHYPERFINE](LHYPERFINE.md)

<a href="/wiki/Calculating_the_hyperfine_coupling_constant"
class="mw-redirect"
title="Calculating the hyperfine coupling constant">Calculating the
hyperfine coupling constant</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NGYROMAG-_incategory-Examples)

------------------------------------------------------------------------

[^gyromag:web-1]: [Gyromagnetic ratio, www.wikipedia.org (2025)](https://en.wikipedia.org/wiki/Gyromagnetic_ratio#For_a_nucleus)
[^gyromag:database:web-2]: [Konstantin's gyromagnetic ratio table, https://www.kherb.io (2025)](https://www.kherb.io/docs/nmr_table.html)
[^gyromag:book:2019-3]: [N. J. Stone, *TABLE OF RECOMMENDED NUCLEAR MAGNETIC DIPOLE MOMENTS: PART I, LONG-LIVED STATES*, (2019), p.13-43.](https://www-nds.iaea.org/publications/indc/indc-nds-0794.pdf)
[^tiesinga:revmodphys:2021-4]: [E. Tiesinga, P. Mohr, P. Newell, and B. Taylor, *CODATA recommended values of the fundamental physical constants: 2018\**, Rev. Mod. Phys. **93**, 025010 (2021).](https://doi.org/10.1103/RevModPhys.93.025010)

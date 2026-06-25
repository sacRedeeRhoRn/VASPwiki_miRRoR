<!-- Source: https://vasp.at/wiki/index.php/SMEARINGS | revid: 32811 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SMEARINGS


SMEARINGS = \[real array of
length (2 \* [NSW](NSW.md))\]  
Default: **SMEARINGS** = not set 

Description: SMEARINGS defines
the smearing parameters for [`ISMEAR`](ISMEAR.md)` = -3` in
the calculation of the partial occupancies.

------------------------------------------------------------------------

[`ISMEAR`](ISMEAR.md)` = -3` performs a loop over
smearing-parameters supplied in the [INCAR](../input-files/INCAR.md) file.
With the tag SMEARINGS, you
select which smearings are used

    SMEARINGS = ismear1 sigma1  ismear2 sigma2  ...

|  |
|----|
| **Mind:** You must set [NSW](NSW.md) to the number of different smearings. |

VASP will then read the provided smearings and conduct
([NSW](NSW.md) + 1) calculations with the different smearings.
For the first calculation, VASP uses tetrahedron smearing
[`ISMEAR`](ISMEAR.md)` = -5` to ensure that the tetrahedron
information is present in case any of the selected smearings uses a
tetrahedron method. Since VASP uses the relaxation engine to loop over
the different smearings you cannot combine
SMEARINGS with other
relaxation methods [IBRION](IBRION.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=SMEARINGS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ISMEAR](ISMEAR.md), [SIGMA](SIGMA.md),
[NSW](NSW.md), [IBRION](IBRION.md), [Smearing
technique](../tutorials/Smearing_technique.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SMEARINGS-_incategory-Examples)



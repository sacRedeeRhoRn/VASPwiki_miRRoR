<!-- Source: https://vasp.at/wiki/index.php/ICHIBARE | revid: 29603 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ICHIBARE


ICHIBARE = 1 \| 2 \| 3  
Default: **ICHIBARE** = 1 

Description: determines the order of the finite difference stencil used
to calculate the magnetic susceptibility.

------------------------------------------------------------------------

ICHIBARE specifies the order
of the finite difference stencil used to calculate the magnetic
susceptibility (second order derivative in Eq. 47 of Yates *et
al.*[^yates:prb:2007-1]).
ICHIBARE may be set to 1, 2,
or 3. Often the default
(ICHIBARE=1) is sufficient. A
higher ICHIBARE results in a
substantial increase of the computational load.

## Related tags and articles\[<a href="/wiki/index.php?title=ICHIBARE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md), [DQ](DQ.md),
[LNMR_SYM_RED](LNMR_SYM_RED.md),
[NLSPLINE](NLSPLINE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ICHIBARE-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=ICHIBARE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^yates:prb:2007-1]: [J. R. Yates, C. J. Pickard, and F. Mauri, *Calculation of NMR chemical shifts for extended systems using ultrasoft pseudopotentials*, Phys. Rev. B **76**, 024401 (2007).](https://doi.org/10.1103/PhysRevB.76.024401)

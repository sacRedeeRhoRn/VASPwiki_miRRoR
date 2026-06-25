<!-- Source: https://vasp.at/wiki/index.php/LNMR_SYM_RED | revid: 32804 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNMR_SYM_RED


LNMR_SYM_RED = .TRUE. \|
.FALSE.  
Default: **LNMR_SYM_RED** = .FALSE. 

Description: discard symmetry operations that are not consistent with
the way *k*-space derivatives are calculated in the linear-response
calculations of chemical shifts.

------------------------------------------------------------------------

The star on which the *k*-space derivative is calculated is oriented
along the cartesian directions in *k* space. If the symmetry operations
in *k* space do not map this star onto itself, erroneous results can be
obtained. To check for such operations, set
LNMR_SYM_RED=.TRUE.. VASP then
disregards such operations, and the resulting first Brillouin zone (IBZ)
is larger. This is only relevant if the use of symmetry is switched on,
i.e. [`ISYM`](ISYM.md)` > 0`. In case of any doubt, set
LNMR_SYM_RED=.TRUE.

|  |
|----|
| **Warning:** It matters how the real-space-lattice vectors are set up relative to the cartesian coordinates in the [POSCAR](../input-files/POSCAR.md) file. |

It determines the orientation of the *k*-space star and, hence, can
affect the efficiency via the number of *k*-points in the IBZ.

## Related tags and articles\[<a
href="/wiki/index.php?title=LNMR_SYM_RED&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md), [DQ](DQ.md),
[ICHIBARE](ICHIBARE.md),
[NLSPLINE](NLSPLINE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LNMR_SYM_RED-_incategory-Examples)



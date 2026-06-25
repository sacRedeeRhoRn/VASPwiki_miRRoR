<!-- Source: https://vasp.at/wiki/index.php/LUSE_VDW | revid: 28627 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LUSE_VDW


LUSE_VDW = \[logical\]  
Default: **LUSE_VDW** = .FALSE. 

Description: LUSE_VDW=.TRUE.
switches on the use of a nonlocal vdW-DF functional. These functionals
depend on the electron density at two points in space and model
long-range van der Waals (dispersion) correlation effects.

------------------------------------------------------------------------

|  |
|----|
| **Mind:** In versions of VASP prior to 6.4.0, a meta-GGA functional (e.g., SCAN) could be combined only with the rVV10 nonlocal functional. Conversely, a GGA functional could be combined only with the original nonlocal functional of Dion *et al.*. This restriction is lifted since VASP.6.4.0 thanks to the introduction of the [IVDW_NL](IVDW_NL.md) tag. |

## Related tags and articles\[<a href="/wiki/index.php?title=LUSE_VDW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[GGA](GGA.md), [METAGGA](METAGGA.md),
[IVDW_NL](IVDW_NL.md),
[LSPIN_VDW](LSPIN_VDW.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LUSE_VDW-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/HFSCREEN | revid: 31117 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HFSCREEN


HFSCREEN = \[real\]  
Default: **HFSCREEN** = 0 (none) 

Description: HFSCREEN (in
Å<sup>-1</sup>) specifies the range-separation parameter in
[range-separated hybrid
functionals](../methods/Hybrid_functionals-_formalism.md).

------------------------------------------------------------------------

If [LHFCALC](LHFCALC.md)=.TRUE. and
[GGA](GGA.md)=PE (PBE functional), attributing a value to
HFSCREEN will switch from the
PBE0 functional to, e.g., the closely related
[HSE03](../methods/List_of_hybrid_functionals.md)
(HFSCREEN=0.3) or
[HSE06](../methods/List_of_hybrid_functionals.md)
(HFSCREEN=0.2) functionals. It
also needs to be set for dielectric-dependent hybrid functionals (DDH)
and doubly screened hybrid (DSH) functionals, see
[LMODELHF](LMODELHF.md).

|  |
|----|
| **Mind:** HFSCREEN can be used only when [GGA](GGA.md)=PE, PS or CA. The other [GGA](GGA.md) and [METAGGA](METAGGA.md) functionals have no screened version available in VASP. |

## Related tags and articles\[<a href="/wiki/index.php?title=HFSCREEN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LMODELHF](LMODELHF.md), [AEXX](AEXX.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[LTHOMAS](LTHOMAS.md),
[LRHFCALC](LRHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-HFSCREEN-_incategory-Examples)



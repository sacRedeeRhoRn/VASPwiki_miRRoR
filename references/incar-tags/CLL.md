<!-- Source: https://vasp.at/wiki/index.php/CLL | revid: 28648 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CLL
CLL = \[integer\] 

|                  |     |     |
|------------------|-----|-----|
| Default: **CLL** | = 0 |     |

Description: CLL selects the angular quantum number
$l$ of the excited core electron when
using [ICORELEVEL](ICORELEVEL.md)\>0.

------------------------------------------------------------------------

|  |
|----|
| **Mind:** Currently the spin-orbit coupling is only supported in the valence and conduction states but not in the core states. Hence, the splitting of an absorption edge with the orbital quantum number L\>0 is not captured. For example, the splitting to *L2* and *L3*-edges is not captured in the calculations and instead, a single *L*-edge is shown. |

## Related tags and articles
[ICORELEVEL](ICORELEVEL.md), [CLZ](CLZ.md)
[CLNT](CLNT.md), [CLN](CLN.md), CLL
[LADDER](LADDER.md), [LHARTREE](LHARTREE.md),
[NBANDSV](NBANDSV.md), [NBANDSO](NBANDSO.md),
[OMEGAMAX](OMEGAMAX.md),
[ANTIRES](ANTIRES.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CLL-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/NOMEGA_DUMP | revid: 30229 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NOMEGA_DUMP


NOMEGA_DUMP = \[integer\] 

|                          |      |     |
|--------------------------|------|-----|
| Default: **NOMEGA_DUMP** | = -1 |     |

|  |
|----|
| **Warning:** Available as of version 6.3.2. |

Description: NOMEGA_DUMP
selects the imaginary frequency point of screened potential in
[low-scaling GW
calculations](../methods/Practical_guide_to_GW_calculations.md)
that is written to file.

|  |
|----|
| **Mind:** This tag can be used to obtain [WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) for [BSE calculations](../tutorials/Bethe-Salpeter-equations_calculations.md). |

------------------------------------------------------------------------

NOMEGA_DUMP selects the
imaginary frequency point of the screened Coulomb kernel that is written
to [WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) in [low-scaling
GW
calculations](../methods/Practical_guide_to_GW_calculations.md).
If set to 0, [WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md)
contains the screened Coulomb interaction W at
$\omega=0$. For positive values, these files contain the
screened Coulomb interaction at the corresponding imaginary frequency
point. For negative values,
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) is not written.

## Related tags and articles\[<a
href="/wiki/index.php?title=NOMEGA_DUMP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ALGO](ALGO.md), [NOMEGA](NOMEGA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NOMEGA_DUMP-_incategory-Examples)

------------------------------------------------------------------------



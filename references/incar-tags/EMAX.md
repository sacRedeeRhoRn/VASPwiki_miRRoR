<!-- Source: https://vasp.at/wiki/index.php/EMAX | revid: 26949 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EMAX


EMAX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **EMAX** | = highest KS eigenvalue + $\Delta$ |  |

Description: EMAX specifies
the upper boundary of the energy range for the evaluation of the
electronic <a href="/wiki/Density_of_states" class="mw-redirect"
title="Density of states">density of states</a> (DOS).

------------------------------------------------------------------------

The DOS is evaluated each [NBLOCK](NBLOCK.md) steps,
[DOSCAR](../output-files/DOSCAR.md) is updated each
[NBLOCK](NBLOCK.md)\*[KBLOCK](KBLOCK.md) steps.

## Related tags and articles\[<a href="/wiki/index.php?title=EMAX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[EMIN](EMIN.md), [NEDOS](NEDOS.md),
[DOSCAR](../output-files/DOSCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EMAX-_incategory-Examples)



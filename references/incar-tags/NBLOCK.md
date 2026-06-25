<!-- Source: https://vasp.at/wiki/index.php/NBLOCK | revid: 32796 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBLOCK


NBLOCK = \[integer\]  
Default: **NBLOCK** = 1 

Description: After NBLOCK
ionic steps the pair-correlation function and the DOS are calculated and
the ionic configuration is written to the
[XDATCAR](../output-files/XDATCAR.md)-file.

------------------------------------------------------------------------

It is recommended to leave
NBLOCK to 1, since the
computational overhead to determine the DOS and pair correlation
function is minimal. Only for molecular dynamics simulations with many
1000 steps or when using machine-learned force fields, it might be
expedient to increase NBLOCK
to say 10 or even 100, to avoid large
[XDATCAR](../output-files/XDATCAR.md)-files and the evaluation of the pair
correlation function at every step.

|  |
|----|
| **Tip:** If machine-learned force fields are used in prediction-only mode ([`ML_MODE`](ML_MODE.md)` = run`) prefer to use the [ML_OUTBLOCK](ML_OUTBLOCK.md) tag instead of NBLOCK to control the output frequency. |

In addition

- NBLOCK controls how often
  the kinetic energy is scaled if [`SMASS`](SMASS.md)` = -1`.

<!-- -->

- After
  [`KBLOCK`](KBLOCK.md)` * ``NBLOCK`
  ionic steps the averaged pair correlation function and DOS are written
  to the files [PCDAT](../output-files/PCDAT.md) and
  [DOSCAR](../output-files/DOSCAR.md). The internal accumulators are reset,
  and after another
  [`KBLOCK`](KBLOCK.md)` * ``NBLOCK`
  steps the new averaged quantities are written out.

|  |
|----|
| **Warning:** The product of [KBLOCK](KBLOCK.md) and NBLOCK should not be larger than the number of steps [NSW](NSW.md). If [`KBLOCK`](KBLOCK.md)` * ``NBLOCK`` > `[`NSW`](NSW.md) before starting the main ion loop then [KBLOCK](KBLOCK.md) is automatically reset to 1. Next, if the same conditions is still true, NBLOCK is reset to [NSW](NSW.md). Also, mind that NBLOCK will be at minimum [ML_OUTBLOCK](ML_OUTBLOCK.md) in MLFF prediction-only MD runs. |

## Related tags and articles\[<a href="/wiki/index.php?title=NBLOCK&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[PCDAT](../output-files/PCDAT.md), [DOSCAR](../output-files/DOSCAR.md),
[XDATCAR](../output-files/XDATCAR.md), [KBLOCK](KBLOCK.md),
[ML_OUTBLOCK](ML_OUTBLOCK.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NBLOCK-_incategory-Examples)



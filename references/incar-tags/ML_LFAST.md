<!-- Source: https://vasp.at/wiki/index.php/ML_LFAST | revid: 32849 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LFAST


ML_LFAST = \[logical\] 

|  |  |  |
|----|----|----|
| Default: **ML_LFAST** | = .TRUE. | for [`ML_MODE`](ML_MODE.md)` = refit` |
|  | = .FALSE. | else |

Description: This tag switches on the descriptors for refitting in the
fast execution mode within machine learning force fields. This tag is
usually switched on by [`ML_MODE`](ML_MODE.md)` = refit`
and doesn't need to be set explicitely.

|  |
|----|
| **Mind:** This tag is only available as of VASP.6.4.0 |

------------------------------------------------------------------------

This tag switches on the descriptors for the fast execution mode. To use
the fast execution mode the force field first has to be refit with the
fast descriptors. This is done by setting
[`ML_MODE`](ML_MODE.md)` = refit`, which will automatically
set `ML_LFAST`` = .TRUE.`. As
usual, the resulting [ML_FFN](../output-files/ML_FFN.md) has to be copied to
[ML_FF](../input-files/ML_FF.md) and the fast code will be automatically run
in production mode runs by setting
[`ML_MODE`](ML_MODE.md)` = run`.

The speedup of the fast method compared to the regular method is
increasing with increasing number of local reference configurations.

It should be noted that in the fast version no Bayesian error estimation
is available.

Since the calculation time of the fast version is of the same order of
magnitude as the timing for the output of the molecular-dynamics
results, we advise decreasing the output frequency for molecular
dynamics by the tag [ML_OUTBLOCK](ML_OUTBLOCK.md).
Additionally, the calculation and output of the pair-correlation
function can be suppressed by
[`ML_OUTPUT_MODE`](ML_OUTPUT_MODE.md)` = 0` as
default.

|  |
|----|
| **Deprecated:** If `ML_LFAST`` = .TRUE.` is explicitely used without the [ML_MODE](ML_MODE.md) tag then it can only be used with [`ML_ISTART`](ML_ISTART.md)` = 4` and [`ML_IALGO_LINREG`](ML_IALGO_LINREG.md)` > 1`. |

## Related tags and articles\[<a href="/wiki/index.php?title=ML_LFAST&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
<a href="/wiki/ML_IERR" class="mw-redirect" title="ML IERR">ML_IERR</a>,
[ML_OUTBLOCK](ML_OUTBLOCK.md),
[ML_OUTPUT_MODE](ML_OUTPUT_MODE.md),
[ML_FFN](../output-files/ML_FFN.md)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/ML_CDOUB | revid: 32817 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_CDOUB


ML_CDOUB = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ML_CDOUB** | = 4.0 | for [`ML_MODE`](ML_MODE.md)` = select` |
|  | = 2.0 | else |

Description: This tag controls the criterion for "enforced" DFT
calculations within the machine learning force field method.

------------------------------------------------------------------------

The usage of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).

If at any time, the estimated force errors are
ML_CDOUB times larger than the
Bayesian threshold (i.e. "critically" high), a first principles
calculation is performed and a new force field is immediately generated
(even if the counter for sampling is below the minimum amount of sampled
structures [ML_NMDINT](ML_NMDINT.md)).

## Related tags and articles\[<a href="/wiki/index.php?title=ML_CDOUB&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MCONF_NEW](ML_MCONF_NEW.md),
[ML_CTIFOR](ML_CTIFOR.md),
[ML_NMDINT](ML_NMDINT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_CDOUB-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/ML_NMDINT | revid: 22750 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_NMDINT


ML_NMDINT = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **ML_NMDINT** | = 1 | for [ML_MODE](ML_MODE.md) = SELECT |
|  | = 10 | else |

Description: Tag to control the minimum interval to get training samples
in the machine learning force field method.

------------------------------------------------------------------------

The usage of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field-_Theory.md)

This tag defines a lower threshold for taking new configurations from
the MD, so that as long as the upper threshold for the Bayesian error
(e.g. [ML_CDOUB](ML_CDOUB.md) times
[ML_CTIFOR](ML_CTIFOR.md)) is not exceeded, at least
ML_NMDINT MD steps are
preformed using the MLFF (i.e. no first principles calculation is
performed). This avoids that many nearly identical structures are added.

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_NMDINT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MCONF_NEW](ML_MCONF_NEW.md),
[ML_CDOUB](ML_CDOUB.md),
[ML_CTIFOR](ML_CTIFOR.md),
[ML_MHIS](ML_MHIS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_NMDINT-_incategory-Examples)

------------------------------------------------------------------------



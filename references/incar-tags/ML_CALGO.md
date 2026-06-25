<!-- Source: https://vasp.at/wiki/index.php/ML_CALGO | revid: 27674 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_CALGO


ML_CALGO = \[integer\]  
Default: **ML_CALGO** = 0 

Description: Chooses error estimation type for on-the-fly training or
reselection of local referenc configurations.

------------------------------------------------------------------------

This tag chooes which algorithm is employed for the error estimation in
[ML_MODE](ML_MODE.md)=*TRAIN* or *SELECT*. The following
two choices are available:

- ML_CALGO=0: Bayesian error
  estimation. Constant or variable threshold. Default.
- ML_CALGO=1: Spilling factor.
  Constant threhold.

In both modes an ab-initio calculation is carried out if the value of
the error estimate is above a threshold specified by
[ML_CTIFOR](ML_CTIFOR.md). In both algorithms the
estimators have different units, values and hence defaults for this
threshold. In contrast to the Bayesian error estimation which can be run
in many different modes for the threhold update (see
[ML_ICRITERIA](ML_ICRITERIA.md)), the spilling factor
can only be used with a constant threshold
([ML_ICRITERIA](ML_ICRITERIA.md)=0).

## Related tags and articles\[<a href="/wiki/index.php?title=ML_CALGO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_CTIFOR](ML_CTIFOR.md)

------------------------------------------------------------------------



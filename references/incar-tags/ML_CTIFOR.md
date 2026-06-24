<!-- Source: https://vasp.at/wiki/index.php/ML_CTIFOR | revid: 27675 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_CTIFOR
|  |  |  |
|----|----|----|
| Default: **ML_CTIFOR** | = 0.002 | if [ML_CALGO](ML_CALGO.md) = 0 |
|  | = 0.02 | if [ML_CALGO](ML_CALGO.md) = 1 |

Description: This flag sets the threshold for the error estimation in
the machine learning force field method.

------------------------------------------------------------------------

The use of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).
Generally, first principles calculations are only performed if the error
estimate of one force exceeds the threshold.

The initial threshold is set to the value provided by the tag ML_CTIFOR
(units of eV/Angstrom for [ML_CALGO](ML_CALGO.md)=0 and
unitless for [ML_CALGO](ML_CALGO.md)=1).

For [ML_CALGO](ML_CALGO.md)=0, the threshold can be
updated dynamically during ML. The details of the update are controlled
by [ML_ICRITERIA](ML_ICRITERIA.md). Typically, after
extensive training, attainable values for ML_CTIFOR are 0.02 around
300-500 K, and 0.06 around 1000-2000 K, so temperature but also system
dependent. The initial default 0.002 is only sensible, if ML_CTIFOR is
automatically updated ([ML_ICRITERIA](ML_ICRITERIA.md)
= 1 or 2). If [ML_ICRITERIA](ML_ICRITERIA.md) = 0 is
used, it is necessary to use significantly larger values around
0.02-0.06 for ML_CTIFOR.

For [ML_CALGO](ML_CALGO.md)=1, only a constant threshold
during the calculation is available
([ML_ICRITERIA](ML_ICRITERIA.md)=0).

The related tag [ML_SCLC_CTIFOR](ML_SCLC_CTIFOR.md)
determines how many local reference configurations are chosen from each
first principles calculations.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_CALGO](ML_CALGO.md),
[ML_SCLC_CTIFOR](ML_SCLC_CTIFOR.md) ,
[ML_MHIS](ML_MHIS.md), [ML_CSIG](ML_CSIG.md),
[ML_CSLOPE](ML_CSLOPE.md),
[ML_CDOUB](ML_CDOUB.md), [ML_CX](ML_CX.md),
[ML_NMDINT](ML_NMDINT.md),
[ML_MCONF_NEW](ML_MCONF_NEW.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_CTIFOR-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/ML_CSIG | revid: 25145 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_CSIG
ML_CSIG = \[real\]  
Default: **ML_CSIG** = $0.4$ 

Description: Parameter used in the automatic determination of threshold
[ML_CTIFOR](ML_CTIFOR.md) for error estimation in the
machine learning force field method.

------------------------------------------------------------------------

The usage of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).

The standard error of the history of maximum estimated errors of the
forces ([ML_MHIS](ML_MHIS.md)) and it's slope must be below
ML_CSIG and [ML_CSLOPE](ML_CSLOPE.md) so that an update
of the threshold for the maximum estimated error of forces
[ML_CTIFOR](ML_CTIFOR.md) can take place.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_CSLOPE](ML_CSLOPE.md),
[ML_MHIS](ML_MHIS.md),
[ML_CTIFOR](ML_CTIFOR.md), [ML_CX](ML_CX.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_CSIG-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/ML_CSLOPE | revid: 25143 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_CSLOPE
ML_CSLOPE = \[real\]  
Default: **ML_CSLOPE** = $0.2$ 

Description: Parameter used in the automatic determination of threshold
for error estimation in the machine learning force field method.

------------------------------------------------------------------------

The usage of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).

The standard error of the history of maximum estimated errors of the
forces ([ML_MHIS](ML_MHIS.md)) and it's slope must be below
[ML_CSIG](ML_CSIG.md) and ML_CSLOPE so that an update of
the threshold for the maximum estimated error of forces
[ML_CTIFOR](ML_CTIFOR.md) can take place.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_CSIG](ML_CSIG.md), [ML_MHIS](ML_MHIS.md),
[ML_CX](ML_CX.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_CSLOPE-_incategory-Examples)

------------------------------------------------------------------------

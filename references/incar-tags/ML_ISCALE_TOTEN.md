<!-- Source: https://vasp.at/wiki/index.php/ML_ISCALE_TOTEN | revid: 32823 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_ISCALE_TOTEN
ML_ISCALE_TOTEN = \[integer\]  
Default: **ML_ISCALE_TOTEN** = 2 

Description: This tag specifies how to scale the energy data in the
machine learning force field method.

------------------------------------------------------------------------

The following cases are possible:

- `ML_ISCALE_TOTEN`` = 1`: The total energy is scaled to the total
  energy of the isolated atoms given by
  [ML_EATOM_REF](ML_EATOM_REF.md).
- `ML_ISCALE_TOTEN`` = 2`: The total energy is scaled to the average of
  the training data. This is the default setting.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_EATOM_REF](ML_EATOM_REF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_ISCALE_TOTEN-_incategory-Examples)

------------------------------------------------------------------------

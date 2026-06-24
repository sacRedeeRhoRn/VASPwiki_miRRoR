<!-- Source: https://vasp.at/wiki/index.php/ML_MCONF_NEW | revid: 32822 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MCONF_NEW
ML_MCONF_NEW = \[integer\]  
Default: **ML_MCONF_NEW** = 5 

Description: This tag sets the number of configurations that are stored
temporarily as candidates for the training data in the machine learning
force field method.

------------------------------------------------------------------------

|  |
|----|
| **Warning:** This value is close to optimal for on-the-fly learning, and should usually not be changed. |

The use of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).
If force fields are reparameterized
([`ML_MODE`](ML_MODE.md)` = select`), calculations are
usually more efficient if this parameter is increased to values around
10-16 and setting [`ML_CDOUB`](ML_CDOUB.md)` = 4`. This is
particularly relevant if the ML_AB file is large.

## Related tags and articles
[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_MCONF_NEW-_incategory-Examples)

------------------------------------------------------------------------

[ML_LMLFF](ML_LMLFF.md),
[ML_MCONF](ML_MCONF.md),
[ML_CTIFOR](ML_CTIFOR.md),
[ML_CDOUB](ML_CDOUB.md)

<!-- Source: https://vasp.at/wiki/index.php/ML_SIGW0 | revid: 26081 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_SIGW0
ML_SIGW0 = \[real\]  
Default: none 

|  |  |  |
|----|----|----|
| Default: **ML_SIGW0** | = 1E-7 | for [ML_MODE](ML_MODE.md) = REFIT |
|  | = 1.0 | else |

Description: This flag sets the precision parameter
$s_{\mathrm{w}}$ (see
[here](../methods/Machine_learning_force_field-_Theory.md)
for definition) for the fitting in the machine learning force field
method.

------------------------------------------------------------------------

The default value for [ML_MODE](ML_MODE.md)=*REFIT* works
reliably in most calculations, however, sometimes it is necessary to
increase the regularization parameter to avoid instabilities during
finite temperature molecular dynamics simulations.

Suppose the regularization needs to be controlled manually, like e.g. in
the fitting via singular value decomposition
([ML_MODE](ML_MODE.md)=*REFIT* or
[ML_IALGO_LINREG](ML_IALGO_LINREG.md)=4). The best
is to control the regularization via this parameter and keep the noise
parameter $s_{\mathrm{v}}$ (see
[ML_SIGV0](ML_SIGV0.md)) constant at 1. Useful values for
ML_SIGW0 are typically between 1E-1 and 1E-9. When the value is
increased the regularization is increased. This often slightly increases
the training set error but also reduces potential instabilities. Hence,
if instabilities are observed during molecular-dynamics simulations, one
should try to increase ML_SIGW0 to say 1E-3, then refit, and repeat the
molecular-dynamics simulations.

More on the theory of this regularization parameter can be found in
[this
section](../methods/Machine_learning_force_field-_Theory.md).

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md), [ML_IREG](ML_IREG.md),
[ML_SIGV0](ML_SIGV0.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_SIGW0-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/ML_SIGV0 | revid: 20553 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_SIGV0


ML_SIGV0 = \[real\]  
Default: **ML_SIGV0** = 1.0 

Description: This flag sets the noise parameter
$s_{\mathrm{v}}$ (see
[here](../methods/Machine_learning_force_field-_Theory.md)
for definition) for the fitting in the machine learning force field
method.

------------------------------------------------------------------------

If the regularization needs to be controlled manually, like e.g. in the
fitting via singular value decomposition
([ML_MODE](ML_MODE.md)=*REFIT* or
[ML_IALGO_LINREG](ML_IALGO_LINREG.md)=4), the best
is to keep this parameter constant at 1 and control the regularization
via the precision parameter $s_{\mathrm{w}}$ (see [ML_SIGW0](ML_SIGW0.md)).

For the theory of this regularization parameter see [this
section](../methods/Machine_learning_force_field-_Theory.md).

## Related tags and sections\[<a href="/wiki/index.php?title=ML_SIGV0&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_IREG](ML_IREG.md),
[ML_SIGW0](ML_SIGW0.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_SIGV0-_incategory-Examples)

------------------------------------------------------------------------



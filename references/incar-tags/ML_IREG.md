<!-- Source: https://vasp.at/wiki/index.php/ML_IREG | revid: 16615 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_IREG


ML_IREG = \[integer\]  
Default: **ML_IREG** = 2 

Description: This tag specifies whether the regularization parameters
are kept constant or not in the machine learning force field method.

------------------------------------------------------------------------

The following cases are possible for this tag:

- ML_IREG=1: The (initial)
  precision ([ML_SIGV0](ML_SIGV0.md)) and noise
  ([ML_SIGW0](ML_SIGW0.md)) parameters are kept constant.
- ML_IREG=2: The parameters
  are optimized (default).

For the optimization of the noise parameter $\sigma_{\mathrm{v}}^{2}$ see <a
href="/wiki/Machine_learning_force_fields:_Theory#Bayesian_error_estimation"
class="mw-redirect" title="Machine learning force fields: Theory">this
section</a>.

## Related tags and articles\[<a href="/wiki/index.php?title=ML_IREG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_SIGV0](ML_SIGV0.md),
[ML_SIGW0](ML_SIGW0.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_IREG-_incategory-Examples)

------------------------------------------------------------------------



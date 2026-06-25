<!-- Source: https://vasp.at/wiki/index.php/ML_WTSIF | revid: 16664 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_WTSIF


ML_WTSIF = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ML_WTSIF** | = 5.0 | if [ML_IWEIGHT](ML_IWEIGHT.md)=1 |
|  | = 1.0 | otherwise |

Description: This tag sets the weight for the scaling of the stress in
the training data within the machine learning force field method.

------------------------------------------------------------------------

[ML_IWEIGHT](ML_IWEIGHT.md),
[ML_WTOTEN](ML_WTOTEN.md),
[ML_WTIFOR](ML_WTIFOR.md),
ML_WTSIF form a group of tags
which set the normalization and weighting of ab initio training data,
i.e. energies, forces and stresses of the training structures. The main
control tag is [ML_IWEIGHT](ML_IWEIGHT.md), please also
have a look at its detailed description. If
[ML_IWEIGHT](ML_IWEIGHT.md)=1 the weight has unit kBar
and is used to divide the data by it. For
[ML_IWEIGHT](ML_IWEIGHT.md)=2 and 3 the weights are
unitless and multiplicative.

  

## Related tags and articles\[<a href="/wiki/index.php?title=ML_WTSIF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_IWEIGHT](ML_IWEIGHT.md),
[ML_WTIFOR](ML_WTIFOR.md),
[ML_WTOTEN](ML_WTOTEN.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_WTSIF-_incategory-Examples)

------------------------------------------------------------------------



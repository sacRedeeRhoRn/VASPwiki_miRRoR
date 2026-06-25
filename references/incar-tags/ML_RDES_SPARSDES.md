<!-- Source: https://vasp.at/wiki/index.php/ML_RDES_SPARSDES | revid: 24473 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_RDES_SPARSDES


ML_RDES_SPARSDES = \[real\]  
Default: **ML_RDES_SPARSDES** = 0.5 

Description: Sets the ratio of descriptors kept during
angular-descriptor sparsification.

|  |
|----|
| **Mind:** This tag is only available as of VASP 6.4.3. |

------------------------------------------------------------------------

During [angular-descriptor
sparsification](../methods/Machine_learning_force_field-_Theory.md)
([ML_LSPARSDES](ML_LSPARSDES.md)=T), insignificant
angular descriptors are removed based on a leverage scoring. The
percentage of angular descriptors that are kept is determined by the
value of ML_RDES_SPARSDES,
which must be chosen between $0 < r \leq 1$. In practice, we recommend scanning a range between
0.1 to 0.9. Removing angular descriptors increases the performance of a
force field, but it decreases accuracy at the same time. One method of
finding the optimal tradeoff between accuracy and performance is to do a
Pareto front with run time on the x-axis and accuracy on the y-axis.

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_RDES_SPARSDES&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_LSPARSDES](ML_LSPARSDES.md),
[ML_NRANK_SPARSDES](ML_NRANK_SPARSDES.md),
[ML_DESC_TYPE](ML_DESC_TYPE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_EPS_LOW-_incategory-Examples)



<!-- Source: https://vasp.at/wiki/index.php/ML_LSPARSDES | revid: 26031 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LSPARSDES
ML_LSPARSDES = \[logical\]  
Default: **ML_LSPARSDES** = .FALSE. 

Description: Specifies whether angular-descriptor sparsification is
enabled within the machine learning force field method.

|                                                        |
|--------------------------------------------------------|
| **Mind:** This tag is only available as of VASP 6.4.3. |

------------------------------------------------------------------------

|  |
|----|
| **Warning:** This tag only works for [ML_MODE](ML_MODE.md)=*refit* or *reftbayesian*! |

To use the [sparsification of angular descriptors
set](../methods/Machine_learning_force_field-_Theory.md)
the following tags:

- ML_LSPARSDES=*.TRUE.*.
- The ratio of the selected descriptors to the total number of
  descriptors:
  [ML_RDES_SPARSDES](ML_RDES_SPARSDES.md). This
  tag controls the extent of the sparsification.
- The number of the highest eigenvalues $k$ to which the correlation is measured via the leverage
  scoring:
  [ML_NRANK_SPARSDES](ML_NRANK_SPARSDES.md). This
  parameter usually does not need to be changed.

We advise the user to adjust this parameter carefully and test it
individually for each system. This means e.g. plotting the accuracy of
the calculation against the computational speed (Pareto curves) for
different values of
[ML_RDES_SPARSDES](ML_RDES_SPARSDES.md). The user
can then choose a tradeoff between efficiency and accuracy. The behavior
is system dependent, however, we have experienced the following trends
for our test cases: For
[ML_DESC_TYPE](ML_DESC_TYPE.md)=0 a descriptor
sparsification of 50 percent
[ML_RDES_SPARSDES](ML_RDES_SPARSDES.md)=0.5 leaves
the accuracy almost untouched. If more spars descriptors are used such
as e.g. [ML_DESC_TYPE](ML_DESC_TYPE.md)=1, which
already contain much fewer descriptors than the standard descriptor
[ML_DESC_TYPE](ML_DESC_TYPE.md)=0, a 50 percent
sparsification for [ML_DESC_TYPE](ML_DESC_TYPE.md)=1
results in noticeable accuracy loss.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_RDES_SPARSDES](ML_RDES_SPARSDES.md),
[ML_NRANK_SPARSDES](ML_NRANK_SPARSDES.md),
[ML_DESC_TYPE](ML_DESC_TYPE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_EPS_LOW-_incategory-Examples)

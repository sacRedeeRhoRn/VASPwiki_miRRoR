<!-- Source: https://vasp.at/wiki/index.php/ML_EPS_LOW | revid: 20411 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_EPS_LOW


ML_EPS_LOW = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ML_EPS_LOW** | = 1E-11 | for [ML_MODE](ML_MODE.md) = SELECT, REFIT |
|  | = 1E-9 | else (vasp.6.3.0 default was 1E-10, see comments below) |

Description: Threshold for the CUR algorithm used in the sparsification
of local reference configurations within the machine learning force
fields.

------------------------------------------------------------------------

This value sets the threshold for the eigenvalues that contribute to the
leverage scoring used in the CUR algorithm for the rank compression
("sparsification") of the local configurations (for details see appendix
E of reference
[^jinnouchi2:arx:2019-1]).
Small eigenvalues and those columns (local configurations) that are
strongly connected with these small eigenvalues are removed by the
sparsification routines. The default value is fairly well balanced, and
we do not recommend to increase the threshold to values larger than
1E-7. Also using smaller values than 1E-9 does not improve the MLFF if
Bayesian regression is used (but it can be benficial for SVD).

The description how to choose
ML_EPS_LOW for accurate force
fields is given
[here](../methods/Best_practices_for_machine-learned_force_fields.md).

On the theory of the sparsification of local reference configurations
see
[here](../methods/Machine_learning_force_field-_Theory.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_EPS_LOW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md), [ML_MB](ML_MB.md),
[ML_EPS_REG](ML_EPS_REG.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_EPS_LOW-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=ML_EPS_LOW&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^jinnouchi2:arx:2019-1]: [R. Jinnouchi, F. Karsai, and G. Kresse, Phys. Rev. B **100**, 014105 (2019).](https://doi.org/10.1103/PhysRevB.100.014105)

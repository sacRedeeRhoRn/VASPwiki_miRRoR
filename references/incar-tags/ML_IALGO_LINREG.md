<!-- Source: https://vasp.at/wiki/index.php/ML_IALGO_LINREG | revid: 31448 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_IALGO_LINREG
ML_IALGO_LINREG = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **ML_IALGO_LINREG** | = 4 | if [ML_MODE](ML_MODE.md)=refit |
|  | = 1 | otherwise |

Description: This tag determines the algorithm that is employed to solve
the system of linear equations in the ridge regression method for
machine learning.

------------------------------------------------------------------------

In the ridge regression method for machine learning one needs to solve
for the unknown weights $\mathbf{w}$
minimizing

$|| \mathbf{Y} - \mathbf{\Phi} \mathbf{w} ||
\rightarrow \mbox{min}.$

For the theory of the available methods please see
[here](../methods/Machine_learning_force_field-_Theory.md).

The following options are available to solve for $\mathbf{w}$:

- ML_IALGO_LINREG=1: Bayesian linear regression (see
  [here](../methods/Machine_learning_force_field-_Theory.md)).
  Recommended for [NSW](NSW.md)$\ge$1. Usable with [ML_MODE](ML_MODE.md) = *TRAIN*,
  *SELECT*, and *REFITBAYESIAN*.
- ML_IALGO_LINREG=2: QR factorization. Usable with
  [ML_MODE](ML_MODE.md) = *REFIT* and *REFITBAYESIAN*.
- ML_IALGO_LINREG=3: Singular value decomposition. Usable with
  [ML_MODE](ML_MODE.md) = *REFIT* and *REFITBAYESIAN*.
- ML_IALGO_LINREG=4: Singular value decomposition with Tikhonov
  regularization. The regularization can be controlled via
  [ML_SIGW0](ML_SIGW0.md). Usable with
  [ML_MODE](ML_MODE.md) = *REFIT* and *REFITBAYESIAN*.

For on the fly learning [ML_MODE](ML_MODE.md) = *TRAIN* and
reselection of local reference configurations
[ML_MODE](ML_MODE.md) = *SELECT*, it is strictly necessary
to use Bayesian regression (ML_IALGO_LINREG=1), since uncertainty
estimates are only available for Bayesian regression.

**Refitting**: Although the above modes result in an
[ML_FFN](../output-files/ML_FFN.md) file that could be used for production
runs, we strongly advise to refit the [ML_ABN](../output-files/ML_ABN.md)
files. For that copy the [ML_ABN](../output-files/ML_ABN.md) file to the
[ML_AB](../input-files/ML_AB.md) file and use
[ML_MODE](ML_MODE.md)= *REFIT* (if Bayesian error
estimation is required during production runs
[ML_MODE](ML_MODE.md)= *REFITBAYESIAN* is an option, but at
the cost of significatnly slower calculation time).
[ML_MODE](ML_MODE.md)= *REFIT* employs ML_IALGO_LINREG=4 by
default.

For ML_IALGO_LINREG\>1, ML_IALGO_LINREG=3 and 4 are the most tested
approaches and we use ML_IALGO_LINREG=4 routinely before employing a
machine learned force field. ML_IALGO_LINREG=4 gives more stable force
fields and better fitting accuracy than ML_IALGO_LINREG=3, due to the
regularization term employed (for details please see
[here](../methods/Machine_learning_force_field-_Theory.md)).

ML_IALGO_LINREG=4 dramatically improves the condition number of the
fitting compared to ML_IALGO_LINREG=1 since it directly uses the design
matrix. In contrast ML_IALGO_LINREG=1 requires to use the covariance
matrix (square of the design matrix), which effectively doubles the
condition number. However, ML_IALGO_LINREG=4 needs significantly more
memory than ML_IALGO_LINREG=1 (at least twice that much). Please always
monitor the memory estimates in the
[ML_LOGFILE](../output-files/ML_LOGFILE.md)! It should be also noted
that ML_IALGO_LINREG=4 is computationally somewhat more demanding than
ML_IALGO_LINREG=1, but it typically requires between a few minutes and
an hour. So usually the extra cost is negligible compared to the
original training.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md), [ML_W1](ML_W1.md),
[ML_WTOTEN](ML_WTOTEN.md),
[ML_WTIFOR](ML_WTIFOR.md),
[ML_WTSIF](ML_WTSIF.md),
[ML_SIGW0](ML_SIGW0.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_IALGO_LINREG-_incategory-Examples)

------------------------------------------------------------------------

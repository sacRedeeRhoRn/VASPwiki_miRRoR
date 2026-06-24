<!-- Source: https://vasp.at/wiki/index.php/ML_EPS_REG | revid: 17769 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_EPS_REG
ML_EPS_REG = \[real\]  
Default: **ML_EPS_REG** = 1E-15 

Description: Initial value for the threshold of the eigenvalues of the
covariance matrix in the evidence approximation.

------------------------------------------------------------------------

This threshold is used to determine which eigenvalues
$\lambda_{k}$ of the covariance matrix
$\mathbf{\Phi}^{\mathrm{T}}\mathbf{\Phi}/\sigma^{2}_{\mathrm{v}}$ are used in the optimization of the regularization parameters
$\sigma^{2}_{\mathrm{w}}$ and
$\sigma^{2}_{\mathrm{v}}$ determined by
the following equations

$\sigma^{2}_{\mathrm{w}}=\frac{|\mathbf{\bar{w}}|^{2}}{\gamma},$

$\sigma^{2}_{\mathrm{v}}=\frac{|\mathbf{T}-\mathbf{\phi}\mathbf{\bar{w}}|^{2}}{M-\gamma},$

$\gamma=\sum\limits_{k=1}^{N_{\mathrm{B}}}
\frac{\lambda_{k}}{\lambda_{k}+1/\sigma^{2}_{\mathrm{w}}}$.

All eigenvalues satisfying $\lambda_{i} /
\lambda_{\mathrm{max}}$ \> ML_EPS_REG are included in the
above equations, whereas smaller eigenvalues are disregarded (they are
anyway potentially inaccurate because of loss of significance).

If at any point during iterating the above equations, the quadratic norm
of errors (eight column of `REGR/REGRF` in
[ML_LOGFILE](../output-files/ML_LOGFILE.md)) becomes too large (more
than 1.2 times larger than in previous iterations), the code assumes
that numerical issues (loss of significance) have occurred, and then
ML_EPS_REG is automatically doubled. Furthermore, if the regression does
not converge within 10 steps, ML_EPS_REG is also increased by a factor
of 4. The maximum allowed iteration depths is 50 (the iteration number
is the second entry of `REGR/REGRF` in
[ML_LOGFILE](../output-files/ML_LOGFILE.md)). When 50 iterations are
reached, no force field is created and there is most likely something
seriously wrong in the calculation.

The seventh entry of `REGR/REGRF` in the
[ML_LOGFILE](../output-files/ML_LOGFILE.md) shows the ratio of the
regularization ($\sigma_{v}^{2}/ \sigma_{w}^{2}$) and the largest eigenvalue. Usually this number is a number
with many varying digits. If this number becomes a "well rounded" number
(e.g. 1.00000000E-14), this is an indication that the cap for the
current ML_EPS_REG is reached. That means that regularization becomes
crucial.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md),
[ML_IREG](ML_IREG.md),
[ML_SIGV0](ML_SIGV0.md),
[ML_SIGW0](ML_SIGW0.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_EPS_LOW-_incategory-Examples)

------------------------------------------------------------------------

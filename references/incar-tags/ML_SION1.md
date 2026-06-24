<!-- Source: https://vasp.at/wiki/index.php/ML_SION1 | revid: 16658 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_SION1
ML_SION1 = \[real\]  
Default: **ML_SION1** = 0.5 

Description: This tag specifies the width $\sigma_\text{atom}$ of the Gaussian functions used for
broadening the atomic distributions of the radial descriptor
$\rho^{(2)}_i(r)$ within the machine
learning force field method.

------------------------------------------------------------------------

The radial descriptor is constructed from

$\rho_{i}^{(2)}\left(r\right) = \frac{1}{4\pi}
\int \rho_{i}\left(r\hat{\mathbf{r}}\right) d\hat{\mathbf{r}}, \quad
\text{where} \quad \rho_{i}\left(\mathbf{r}\right) =
\sum\limits_{j=1}^{N_{\mathrm{a}}}
f_{\mathrm{cut}}\left(r_{ij}\right)
g\left(\mathbf{r}-\mathbf{r}_{ij}\right)$

and $g\left(\mathbf{r}\right)$ is the
following approximation of the delta function:

$g\left(\mathbf{r}\right)=\frac{1}{\sqrt{2\sigma_{\mathrm{atom}}\pi}}\mathrm{exp}\left(-\frac{|\mathbf{r}|^{2}}{2\sigma_{\mathrm{atom}}^{2}}\right).$

The tag ML_SION1 sets the width $\sigma_\text{atom}$ of the above Gaussian function (see [this
section](../methods/Machine_learning_force_field-_Theory.md)
for more details).

|  |
|----|
| **Tip:** Our test calculations indicate that ML_SION1 = [ML_SION2](ML_SION2.md) results in an optimal training performance. Furthermore, a value of 0.5 was found to be a good default value for both. However, the best choice is somewhat system-dependent. For instance, a smaller value for ML_SION1 can increase the number of local reference configurations, and hence ultimately the quality of the MLFF. See also [here](../methods/Machine_learning_force_field_calculations-_Basics.md). |

The unit of ML_SION1 is $\AA$.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_SION2](ML_SION2.md),
[ML_RCUT1](ML_RCUT1.md),
[ML_RCUT2](ML_RCUT2.md),
[ML_MRB1](ML_MRB1.md), [ML_MRB2](ML_MRB2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_SION1-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/ML_SION2 | revid: 16660 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_SION2
ML_SION2 = \[real\]  
Default: **ML_SION2** = [ML_SION1](ML_SION1.md) 

Description: This tag specifies the width $\sigma_\text{atom}$ of the Gaussian functions used for
broadening the atomic distributions of the angular descriptor
$\rho^{(3)}_i(r)$ within the machine
learning force field method.

------------------------------------------------------------------------

The angular descriptor is constructed from

$\rho_{i}^{(3)}\left(r,s,\theta\right) = \iint
d\hat{\mathbf{r}} d\hat{\mathbf{s}}
\delta\left(\hat{\mathbf{r}}\cdot\hat{\mathbf{s}} -
\mathrm{cos}\theta\right) \sum\limits_{j=1}^{N_{a}} \sum\limits_{k
\ne j}^{N_{a}} \rho_{ik} \left(r\hat{\mathbf{r}}\right) \rho_{ij}
\left(s\hat{\mathbf{s}}\right), \quad \text{where} \quad
\rho_{ij}\left(\mathbf{r}\right) =
f_{\mathrm{cut}}\left(r_{ij}\right)
g\left(\mathbf{r}-\mathbf{r}_{ij}\right)$

and $g\left(\mathbf{r}\right)$ is the
following approximation of the delta function:

$g\left(\mathbf{r}\right)=\frac{1}{\sqrt{2\sigma_{\mathrm{atom}}\pi}}\mathrm{exp}\left(-\frac{|\mathbf{r}|^{2}}{2\sigma_{\mathrm{atom}}^{2}}\right).$

The tag ML_SION2 sets the width $\sigma_\text{atom}$ of the above Gaussian function (see [this
section](../methods/Machine_learning_force_field-_Theory.md)
for more details).

|  |
|----|
| **Tip:** Our test calculations indicate that [ML_SION1](ML_SION1.md) = ML_SION2 results in an optimal training performance. Furthermore, a value of 0.5 was found to be a good default value for both. However, the best choice is system-dependent, careful testing may improve machine learning results. |

The unit of ML_SION2 is $\AA$.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_SION1](ML_SION1.md),
[ML_RCUT1](ML_RCUT1.md),
[ML_RCUT2](ML_RCUT2.md),
[ML_MRB1](ML_MRB1.md), [ML_MRB2](ML_MRB2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_SION2-_incategory-Examples)

------------------------------------------------------------------------

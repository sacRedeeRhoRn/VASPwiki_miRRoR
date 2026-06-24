<!-- Source: https://vasp.at/wiki/index.php/ML_RCUT1 | revid: 20396 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_RCUT1
ML_RCUT1 = \[real\]  
Default: **ML_RCUT1** = 8.0 

Description: Sets the cutoff radius $R_\text{cut}$ for the radial descriptor $\rho^{(2)}_i(r)$ in $\AA$.

------------------------------------------------------------------------

The radial descriptor for machine-learned force fields is constructed
from

$\rho_{i}^{(2)}\left(r\right) = \frac{1}{4\pi}
\int \rho_{i}\left(r\hat{\mathbf{r}}\right) d\hat{\mathbf{r}}, \quad
\text{where} \quad \rho_{i}\left(\mathbf{r}\right) =
\sum\limits_{j=1}^{N_{\mathrm{a}}}
f_{\mathrm{cut}}\left(r_{ij}\right)
g\left(\mathbf{r}-\mathbf{r}_{ij}\right)$

and $g\left(\mathbf{r}\right)$ is an
approximation of the delta function. A basis set expansion of
$\rho^{(2)}_i(r)$ yields the expansion
coefficients $c_{n00}^{i}$, which are
used in practice to describe the atomic environment; refer to the
[theory of machine-learned force
fields](../methods/Machine_learning_force_field-_Theory.md)
for details. The tag ML_RCUT1 sets the cutoff radius
$R_\text{cut}$ at which the cutoff
function $f_{\mathrm{cut}}\left(r_{ij}\right)$ decays to zero.

|  |
|----|
| **Mind:** The cutoff radius determines how many neighbor atoms $N_\mathrm{a}$ are considered to describe each central atom's environment. Hence, important features may be missed if the cutoff radius is too small. On the other hand, a large cutoff radius increases the computational cost of the descriptor as the cutoff sphere contains more neighbor atoms. A good compromise is always system-dependent. Therefore, different values should be tested to achieve satisfying accuracy **and** speed. |

The unit of the cut-off radius is $\AA$.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_RCUT2](ML_RCUT2.md), [ML_W1](ML_W1.md),
[ML_SION1](ML_SION1.md),
[ML_SION2](ML_SION2.md),
[ML_MRB1](ML_MRB1.md), [ML_MRB2](ML_MRB2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_RCUT1-_incategory-Examples)

------------------------------------------------------------------------

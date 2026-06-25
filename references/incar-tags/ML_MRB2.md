<!-- Source: https://vasp.at/wiki/index.php/ML_MRB2 | revid: 20008 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MRB2


ML_MRB2 = \[integer\]  
Default: **ML_MRB2** = 8 

Description: This tag sets the number $N_\text{R}^l$ (for all $l$) of radial
basis functions used to expand the angular descriptor within the machine
learning force field method.

------------------------------------------------------------------------

The angular descriptor is constructed from

$\rho_{i}^{(3)}\left(r,s,\theta\right) = \iint d\hat{\mathbf{r}}
d\hat{\mathbf{s}} \delta\left(\hat{\mathbf{r}}\cdot\hat{\mathbf{s}} -
\mathrm{cos}\theta\right) \sum\limits_{j=1}^{N_{a}} \sum\limits_{k
\ne j}^{N_{a}} \rho_{ik} \left(r\hat{\mathbf{r}}\right) \rho_{ij}
\left(s\hat{\mathbf{s}}\right), \quad \text{where} \quad
\rho_{ij}\left(\mathbf{r}\right) =
f_{\mathrm{cut}}\left(r_{ij}\right)
g\left(\mathbf{r}-\mathbf{r}_{ij}\right)$

and $g\left(\mathbf{r}\right)$ is an approximation of the delta function. In
practice, the continuous function above is transformed into a discrete
set of numbers $p_{n\nu l}^{i}$ by expanding it into a set of radial basis functions
$\chi_{nl}(r)$ and Legendre polynomials
$P_{l}\left(\mathrm{cos}\theta\right)$ (see [this
section](../methods/Machine_learning_force_field-_Theory.md)
for more details):

$\rho_{i}^{(3)}\left(r,s,\theta\right) =
\sum\limits_{l=1}^{L_{\mathrm{max}}}
\sum\limits_{n=1}^{N^{l}_{\mathrm{R}}}\sum\limits_{\nu=1}^{N^{l}_{\mathrm{R}}}
\sqrt{\frac{2l+1}{2}} p_{n\nu l}^{i}\chi_{nl}\left(r\right)\chi_{\nu
l}\left(s\right)P_{l}\left(\mathrm{cos}\theta\right).$

The tag ML_MRB2 sets the
number $N_\text{R}^l$ of radial basis functions to use in this expansion.
The same number is used for all $l$.

|  |
|----|
| **Mind:** The number of angular descriptor expansion coefficients $p_{n\nu l}^{i}$ scales **quadratically** with $N_\text{R}^l$ set by this tag. It also depends on [ML_LMAX2](ML_LMAX2.md) and the number of elements. |

## Related tags and articles\[<a href="/wiki/index.php?title=ML_MRB2&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_LMAX2](ML_LMAX2.md),
[ML_MRB1](ML_MRB1.md), [ML_W1](ML_W1.md),
[ML_RCUT2](ML_RCUT2.md),
[ML_SION2](ML_SION2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_MRB2-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/ML_MRB1 | revid: 20374 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MRB1


ML_MRB1 = \[integer\]  
Default: **ML_MRB1** = 12 

Description: This tag sets the number $N_\text{R}^0$ of radial basis functions used to expand the radial
descriptor $\rho^{(2)}_i(r)$ within the machine learning force field method.

------------------------------------------------------------------------

The radial descriptor is constructed from

$\rho_{i}^{(2)}\left(r\right) = \frac{1}{4\pi} \int
\rho_{i}\left(r\hat{\mathbf{r}}\right) d\hat{\mathbf{r}}, \quad
\text{where} \quad \rho_{i}\left(\mathbf{r}\right) =
\sum\limits_{j=1}^{N_{\mathrm{a}}}
f_{\mathrm{cut}}\left(r_{ij}\right)
g\left(\mathbf{r}-\mathbf{r}_{ij}\right)$

and $g\left(\mathbf{r}\right)$ is an approximation of the delta function. In
practice, the continuous function above is transformed into a discrete
set of numbers by expanding it into a set of radial basis functions
$\chi_{n0}(r)$ (see [this
section](../methods/Machine_learning_force_field-_Theory.md)
for more details):

$\rho_{i}^{(2)}\left(r\right) = \frac{1}{\sqrt{4\pi}}
\sum\limits_{n=1}^{N^{0}_{\mathrm{R}}} c_{n00}^{i}
\chi_{n0}\left(r\right).$

The tag ML_MRB1 sets the
number $N_\text{R}^0$ of radial basis functions to use in this expansion.

## Related tags and articles\[<a href="/wiki/index.php?title=ML_MRB1&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MRB2](ML_MRB2.md), [ML_W1](ML_W1.md),
[ML_RCUT1](ML_RCUT1.md),
[ML_SION1](ML_SION1.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_MRB1-_incategory-Examples)

------------------------------------------------------------------------



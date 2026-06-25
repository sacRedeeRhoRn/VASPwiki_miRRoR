<!-- Source: https://vasp.at/wiki/index.php/ML_LMAX2 | revid: 20377 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LMAX2


ML_LMAX2 = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **ML_LMAX2** | = 3 | for [ML_LAFILT2](ML_LAFILT2.md) = .TRUE. |
|  | = 6 | else |

Description: This tag specifies the maximum angular momentum quantum
number $L_\max$ of
spherical harmonics used to expand atomic distributions within the
machine learning force field method.

------------------------------------------------------------------------

To construct an atomic environment descriptor the atomic probability
density

$\rho_{i}\left(\mathbf{r}\right) = \sum\limits_{j=1}^{N_{\mathrm{a}}}
f_{\mathrm{cut}}\left(r_{ij}\right)
g\left(\mathbf{r}-\mathbf{r}_{ij}\right),$

where $g\left(\mathbf{r}\right)$ is an approximation of the delta function, is expanded
in terms of radial basis functions $\chi_{nl}(r)$ and spherical harmonics $Y_{lm}\left(\hat{\mathbf{r}}\right)$ (see [this
section](../methods/Machine_learning_force_field-_Theory.md)
for more details):

$\rho_{i} \left( \mathbf{r} \right) =
\sum\limits_{l=1}^{L_{\mathrm{max}}} \sum\limits_{m=-l}^{l}
\sum\limits_{n=1}^{N^{l}_{ \mathrm{R}}} c_{nlm}^{i}\chi_{nl} \left(
r \right) Y_{lm} \left( \hat{\mathbf{r}} \right),$

The tag ML_LMAX2 specifies the
maximum angular momentum quantum number $L_\max$ of
spherical harmonics used in this expansion.

|  |
|----|
| **Mind:** This tag is only relevant for the angular descriptor $\rho^{(3)}_i(r)$. The corresponding number of expansion coefficients $p_{n\nu l}^{i}$ scales **linearly** with $L_\max$ (however the calculation of the spherical harmonics scales quadratically) and is also depending on [ML_MRB2](ML_MRB2.md) and the number of elements present. |

By default an angular filtering (see
[ML_LAFILT2](ML_LAFILT2.md) and
[ML_IAFILT2](ML_IAFILT2.md)) with a filtering parameter
of [ML_AFILT2](ML_AFILT2.md)=0.002 is used where a value
of ML_LMAX2=3 is perfectly
safe for most applications. If you need to improve the accuracy, you
might also try to increase it to
ML_LMAX2=4. If the angular
filter is switched off, we recommend to use a value of
ML_LMAX2=6 (this is then the
default value).

## Related tags and articles\[<a href="/wiki/index.php?title=ML_LMAX2&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MRB1](ML_MRB1.md), [ML_MRB2](ML_MRB2.md),
[ML_LAFILT2](ML_LAFILT2.md),
[ML_IAFILT2](ML_IAFILT2.md),
[ML_AFILT2](ML_AFILT2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LMAX2-_incategory-Examples)

------------------------------------------------------------------------



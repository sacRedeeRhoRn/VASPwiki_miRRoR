<!-- Source: https://vasp.at/wiki/index.php/ML_DESC_TYPE | revid: 32859 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_DESC_TYPE
ML_DESC_TYPE = \[integer\]  
Default: **ML_DESC_TYPE** = 0 

Description: Selects the descriptor type of the three-body descriptor
used in machine learning force fields.

------------------------------------------------------------------------

ML_DESC_TYPE selects how the three-body descriptor is calculated, and
the following options are available:

- `ML_DESC_TYPE`` = 0`: [Standard three-body
  descriptor](#Standard_three-body_descriptor), where the number of
  descriptors in the calculation scales quadratically with the number of
  elements.
- `ML_DESC_TYPE`` = 1`: [Element-reduced
  descriptor](#Element-reduced_descriptor) for which the number of
  descriptors is linearly scaling with respect to the number of chemical
  species.

|                                                                  |
|------------------------------------------------------------------|
| **Mind:** This tag is only available as of VASP 6.4.3 or higher. |

|  |
|----|
| **Mind:** ML_DESC_TYPE is available for all options of [ML_MODE](ML_MODE.md) for VASP \>= 6.5.0. For VASP \< 6.5.0, it was only available for [`ML_MODE`](ML_MODE.md)` = refit` and [`ML_MODE`](ML_MODE.md)` = run`. |

## Contents

- [1 Standard three-body descriptor](#Standard_three-body_descriptor)
- [2 Element-reduced descriptor](#Element-reduced_descriptor)
- [3 Additional sparsification](#Additional_sparsification)
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

## Standard three-body descriptor
The standard three-body descriptor (ML_DESC_TYPE=0) without
self-interaction corrections for the $i$th atom looks like the following

$p_{n\nu l}^{iJJ'}=\sqrt{\frac{8\pi^{2}}{2l+1}}
\sum\limits_{m=-l}^{l} c_{nlm}^{iJ} c_{\nu lm}^{iJ'}.$

Here $n$/$\nu$, $l$ and
$m$ are radial, angular, and magnetic
quantum numbers, respectively. $J$ and
$J'$ are indices for the element types.
Both indices go over all elements in the structure. So one can see that
the number of three-body descriptors grows quadratically with the number
of element types.

## Element-reduced descriptor
Another type of descriptor (ML_DESC_TYPE=1) which was proposed in Ref.
^([\[1\]](#cite_note-csanyi:npj:2022-1)) applies a reduction of one of
the intermediate coefficients $c_{nlm}$
and is written as

$p_{n\nu l}^{iJ}=\sqrt{\frac{8\pi^{2}}{2l+1}}
\sum\limits_{m=-l}^{l} c_{nlm}^{iJ} \sum\limits_{J'}c_{\nu
lm}^{iJ'}.$

In contrast to the standard three-body descriptor $p_{n\nu l}^{iJ}$ depends only linearly on the number of
chemical species, since summing over $J'$ for $c_{\nu lm}^{iJ'}$ is
equivalent to having element agnostic intermediate coefficients. When
using this descriptor everything up to the calculation of the
descriptors takes the same time to calculate as for the standard
descriptor, but everything that comes after that, such as e.g. kernels
and forces, scales linearly with respect to the number of chemical
species. Hence the factor that is gained in computational efficiency is
less than the number of chemical species but the factor increases with
an increasing number of local reference configurations employed in the
calculations. The improved computational efficiency comes at the price
of decreased accuracy. The accuracy loss is system-dependent and is
typically around 5 to 20 percent.

## Additional sparsification
All descriptors can be further combined with [descriptor
sparsification](../methods/Machine_learning_force_field-_Theory.md)
([ML_LSPARSDES](ML_LSPARSDES.md)=**.TRUE.**).
Generally, the sparsification of descriptors results in a trade-off
between accuracy and efficiency. The fraction of descriptors that is
kept is specified by
[ML_RDES_SPARSDES](ML_RDES_SPARSDES.md). We advise
the user to adjust this parameter carefully and test it individually for
each system. However, we have experienced the following trends for our
test cases: For ML_DESC_TYPE=0 a descriptor sparsification of 50 percent
[ML_RDES_SPARSDES](ML_RDES_SPARSDES.md)=0.5 leaves
the accuracy almost untouched. Since ML_DESC_TYPE=1 contains already
much fewer descriptors than ML_DESC_TYPE=0, a 50 percent sparsification
for ML_DESC_TYPE=1 results in noticeable accuracy loss (additionally to
the 5 to 20 percent by the descriptor itself).

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_LSPARSDES](ML_LSPARSDES.md),
[ML_RDES_SPARSDES](ML_RDES_SPARSDES.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_IALGO_LINREG-_incategory-Examples)

## References
1.  [↑](#cite_ref-csanyi:npj:2022_1-0) [J. P. Darby, J. R. Kermode,
    and G. Csanyi, *Compressing local atomic neighbourhood descriptors*,
    New Phys. J. **8**, 166
    (2022).](https://doi.org/10.1038/s41524-022-00847-y)

  

------------------------------------------------------------------------

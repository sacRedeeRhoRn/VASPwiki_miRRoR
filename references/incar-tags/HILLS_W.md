<!-- Source: https://vasp.at/wiki/index.php/HILLS_W | revid: 26681 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HILLS_W
HILLS_W = \[Real\]  
Default: **HILLS_W** = $10^{-3}$ 

Description: HILLS_W specifies the width of the Gaussian hill (in units
of the corresponding collective variable) used in metadynamics (in case
VASP was compiled with
[-Dtbdyn](../redirects/Precompiler_flags.md)).

------------------------------------------------------------------------

In [metadynamics](../theory/Metadynamics.md)
([MDALGO](MDALGO.md)=11 \| 21), the bias potential is given
as

$\tilde{V}(t,\xi) = h \sum_{i=1}^{\lfloor t/t_G
\rfloor} \exp{\left\\ -\frac{|\xi^{(t)}-\xi^{(i \cdot t_G)}|^2}{2 w^2}
\right\}.$

Thre parameters ([HILLS_H](HILLS_H.md), HILLS_W, and
[HILLS_BIN](HILLS_BIN.md)) must be provided by the user.

The width of the Gaussian hills $w$ (in
units of the corresponding collective variable) is set by HILLS_W.

## Related tags and articles
[Metadynamics](../redirects/Category-Metadynamics.md),
[HILLS_H](HILLS_H.md),
[HILLS_BIN](HILLS_BIN.md),
[HILLSPOT](HILLSPOT.md), [MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-HILLS_W-_incategory-Examples)

------------------------------------------------------------------------

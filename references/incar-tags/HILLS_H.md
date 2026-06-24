<!-- Source: https://vasp.at/wiki/index.php/HILLS_H | revid: 26679 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HILLS_H
HILLS_H = \[Real\]  
Default: **HILLS_H** = $10^{-3}$ 

Description: HILLS_H specifies the height of the Gaussian hill (in eV)
used in metadynamics (in case VASP was compiled with
[-Dtbdyn](../redirects/Precompiler_flags.md)).

------------------------------------------------------------------------

In [metadynamics](../theory/Metadynamics.md)
([MDALGO](MDALGO.md)=11 \| 21), the bias potential is given
as

$\tilde{V}(t,\xi) = h \sum_{i=1}^{\lfloor t/t_G
\rfloor} \exp{\left\\ -\frac{|\xi^{(t)}-\xi^{(i \cdot t_G)}|^2}{2 w^2}
\right\}.$

Thre parameters (HILLS_H, [HILLS_W](HILLS_W.md), and
[HILLS_BIN](HILLS_BIN.md)) must be provided by the user.

  
The height of the Gaussian hills $h$ (in
eV) is set by HILLS_H.

## Related tags and articles
[Metadynamics](../redirects/Category-Metadynamics.md),
[HILLS_W](HILLS_W.md),
[HILLS_BIN](HILLS_BIN.md),
[HILLSPOT](HILLSPOT.md), [MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-HILLS_H-_incategory-Examples)

------------------------------------------------------------------------

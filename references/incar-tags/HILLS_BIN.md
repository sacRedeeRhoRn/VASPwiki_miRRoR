<!-- Source: https://vasp.at/wiki/index.php/HILLS_BIN | revid: 36172 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HILLS_BIN


HILLS_BIN = \[Integer\]  
Default: **HILLS_BIN** = [NSW](NSW.md) 

Description: HILLS_BIN sets
the number of steps after which the bias potential is updated in a
metadynamics run (in case VASP was compiled with
<a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">-Dtbdyn</a>).

------------------------------------------------------------------------

In [metadynamics](../theory/Metadynamics.md)
([MDALGO](MDALGO.md)=11 \| 21), the bias potential is given
as

$\tilde{V}(t,\xi) = h \sum_{i=1}^{\lfloor t/t_G \rfloor} \exp{\left\\
-\frac{|\xi^{(t)}-\xi^{(i \cdot t_G)}|^2}{2 w^2} \right\}.$

Three parameters ([HILLS_H](HILLS_H.md),
[HILLS_W](HILLS_W.md), and
HILLS_BIN) must be provided by
the user.

  
The number of steps after which the bias potential is updated is set by
HILLS_BIN.

## Related tags and articles\[<a
href="/wiki/index.php?title=HILLS_BIN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Category:Metadynamics" class="mw-redirect"
title="Category:Metadynamics">Metadynamics</a>,
[HILLS_H](HILLS_H.md), [HILLS_W](HILLS_W.md),
[HILLSPOT](HILLSPOT.md), [MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-HILLS_BIN-_incategory-Examples)

------------------------------------------------------------------------



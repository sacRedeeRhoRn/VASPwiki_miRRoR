<!-- Source: https://vasp.at/wiki/index.php/OMEGATL | revid: 18047 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# OMEGATL


OMEGATL = \[real\]  
Default: **OMEGATL** = 10 $\times$
outermost node in dielectric function $\epsilon(\omega)$ 

Description: OMEGATL specifies
the maximum frequency for the coarse part of the frequency grid.

------------------------------------------------------------------------

For the frequency grid along the real and imaginary axis sophisticated
schemes are used, which are based on simple model functions for the
macroscopic dielectric function. The grid spacing is dense up to roughly
1.3\*[OMEGAMAX](OMEGAMAX.md) and becomes coarser for
larger frequencies. The default has been carefully tested, and it is
recommended to leave it unmodified whenever possible.

## Related tags and articles\[<a href="/wiki/index.php?title=OMEGATL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[OMEGAMAX](OMEGAMAX.md),
[OMEGAMIN](OMEGAMIN.md), [CSHIFT](CSHIFT.md),
[NOMEGA](NOMEGA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-OMEGATL-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/MIXPRE | revid: 27064 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MIXPRE


MIXPRE = 0 \| 1 \| 2 \| 3  
Default: **MIXPRE** = 1 

Description: MIXPRE specifies
the metric in the Broyden mixing scheme([IMIX](IMIX.md)=4).

------------------------------------------------------------------------

- MIXPRE=0

No preconditioning, metric=1

- MIXPRE=1

"Inverse Kerker" metric with automatically determined
[BMIX](BMIX.md) (determined in such a way that the variation
of the preconditioning weights covers a range of a factor 20)

- MIXPRE=2

"Inverse Kerker" metric with automatically determined
[BMIX](BMIX.md) (determined in such a way that the variation
of the preconditioning weights covers a range of a factor 200)

- MIXPRE=3 (implemented for
  test purposes; **not** recommended)

"Inverse Kerker" metric with [BMIX](BMIX.md) from
[INCAR](../input-files/INCAR.md), the weights for the metric are given by

$P\left(G\right)=1+\frac{B^2}{G^2}$

with $B$=[BMIX](BMIX.md).

The preconditioning is done only on the total charge density (i.e.
up+down component) and not on the magnetization charge density (i.e.
up-down component). In our experience, the introduction of a metric
always improves the convergence speed. The best choice is
MIXPRE=1 (i.e. the default).

## Related tags and articles\[<a href="/wiki/index.php?title=MIXPRE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [AMIX](AMIX.md),
[BMIX](BMIX.md), [AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [AMIN](AMIN.md),
[WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-MIXPRE-_incategory-Examples)



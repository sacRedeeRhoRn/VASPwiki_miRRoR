<!-- Source: https://vasp.at/wiki/index.php/SPRING | revid: 27428 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SPRING


SPRING = \[integer\]  
Default: **SPRING** = -5 

Description: SPRING gives the
*spring constant* between the images as used in the elastic band method.

------------------------------------------------------------------------

SPRING has to be set together
with [IMAGES](IMAGES.md) if the elastic band method is used
to calculate energy barriers between two ionic configurations of a
system.

For SPRING = 0, each image is
only allowed to move into the direction perpendicular to the current
hyper-tangent, which is calculated as the normal vector between two
neighboring images. This algorithm keeps the distance between the images
constant to *first order*. It is therefore possible to start with a
dense image spacing around the saddle point to obtain a finer resolution
around this point.

The nudged elastic band
method[^jons95-1][^jons98-2]
is applied when SPRING is set
to a negative value e.g.

    SPRING= -5

This is also the recommended setting. Compared to the previous case,
additional tangential springs are introduced to keep the images
equidistant during the relaxation (remember the constraint is only
conserved to first order otherwise). Do not use too large values,
because this can slow down convergence. The default value usually works
quite reliably.

One problem of the nudged elastic band method is that the constraint
(i.e movements only in the hyper-plane perpendicular to the current
tangent) is non linear. Therefore, the CG algorithm usually fails to
converge, and we recommended to use the RMM-DIIS algorithm
([IBRION](IBRION.md)=1) or the quick-min algorithm
([IBRION](IBRION.md)=3). Additionally, the non-linear
constraint (equidistant images) tends to be violated significantly
during the first few steps (it is only enforced to first order). If this
problem is encountered, a very low dimensionality parameter
([IBRION](IBRION.md)=1, [NFREE](NFREE.md)=2)
should be applied in the first few steps, or a steepest descent
minimization without line optimization
([IBRION](IBRION.md)=3, [SMASS](SMASS.md)=2).
should be used, to pre-converge the images.

## Related tags and articles\[<a href="/wiki/index.php?title=SPRING&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMAGES](IMAGES.md), [IBRION](IBRION.md),
[NFREE](NFREE.md), [SMASS](SMASS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SPRING-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=SPRING&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^jons95-1]: [G. Mills, H. Jonsson and G. K. Schenter, Surface Science, 324, 305 (1995).](http://dx.doi.org/10.1016/0039-6028(94)00731-4)
[^jons98-2]: H. Jonsson, G. Mills and K. W. Jacobsen, *Nudged Elastic Band Method for Finding Minimum Energy Paths of Transitions*, in *Classical and Quantum Dynamics in Condensed Phase Simulations*, ed. B. J. Berne, G. Ciccotti and D. F. Coker (World Scientific, 1998).

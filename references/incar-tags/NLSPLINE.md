<!-- Source: https://vasp.at/wiki/index.php/NLSPLINE | revid: 27292 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NLSPLINE


NLSPLINE = .TRUE. \| .FALSE.  
Default: **NLSPLINE** = .FALSE. 

Description: construct the PAW projectors in reciprocal space using
spline interpolation so that they are *k*-differentiable.

------------------------------------------------------------------------

For NLSPLINE=.TRUE., the PAW
projectors in reciprocal space ([LREAL](LREAL.md)=.FALSE.)
are set up using a spline interpolation so that they are *k*
differentiable. This improves the susceptibility contribution to the
chemical shifts. It only slightly affects the other contributions to the
chemical shifts.

It is advised to set
NLSPLINE=.TRUE. if and only if
PAW projectors are applied in reciprocal space and chemical shifts are
calculated, i.e., if and only if [LREAL](LREAL.md)=.FALSE.
and [LCHIMAG](LCHIMAG.md)=.TRUE. As this option also gives
slightly different total energies, it is advised to use the default
NLSPLINE=.FALSE. in all other
calculations for reasons of compatibility.

Real-space projectors are *k* differentiable by construction, hence do
not require to set
NLSPLINE=.TRUE.

## Related tags and articles\[<a href="/wiki/index.php?title=NLSPLINE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md), [DQ](DQ.md),
[ICHIBARE](ICHIBARE.md),
[LNMR_SYM_RED](LNMR_SYM_RED.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NLSPLINE-_incategory-Examples)

------------------------------------------------------------------------



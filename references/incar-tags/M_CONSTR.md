<!-- Source: https://vasp.at/wiki/index.php/M_CONSTR | revid: 16918 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# M CONSTR


M_CONSTR = \[real array\]  
Default: **M_CONSTR** = 3\*NIONS\*0.0 

Description: M_CONSTR
specifies the desired local magnetic moment (size and/or direction) for
the constrained local moments approach.

------------------------------------------------------------------------

The M_CONSTR tag sets the
desired size and/or direction of the integrated local magnetic moments
in cartesian coordinates.

For each ion 3 coordinates must be specified, i.e., for a system of *N*
ions

    M_CONSTR= M_1x M_1y M_1z  M_2x M_2y M_2z  ....  M_Nx M_Ny M_Nz

For [I_CONSTRAINED_M](I_CONSTRAINED_M.md)=1 the
norm of this vector is meaningless since only the direction will be
constrained. For
[I_CONSTRAINED_M](I_CONSTRAINED_M.md)=2 both the
norm as well as the direction of the moments specified by means of
M_CONSTR are subject to
constraints.

Setting

    M_CONSTR=  ... 0 0 0 ... 

for a certain ion is equivalent to imposing no constraints on the
integrated local magnetic moment at this ionic site.

For an explanation of the constrained local moments approach see the
description of the
[I_CONSTRAINED_M](I_CONSTRAINED_M.md) tag.

## Related tags and articles\[<a href="/wiki/index.php?title=M_CONSTR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[I_CONSTRAINED_M](I_CONSTRAINED_M.md),
[LAMBDA](LAMBDA.md), [RWIGS](RWIGS.md),
[LNONCOLLINEAR](LNONCOLLINEAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-M_CONSTR-_incategory-Examples)

------------------------------------------------------------------------



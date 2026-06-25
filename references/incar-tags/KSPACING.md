<!-- Source: https://vasp.at/wiki/index.php/KSPACING | revid: 35382 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KSPACING


KSPACING = \[real\]  
Default: **KSPACING** = 0.5 

Description: Spacing between **k** points in automatically generated
mesh if the [KPOINTS](../input-files/KPOINTS.md) file is not present.

------------------------------------------------------------------------

KSPACING is the smallest
allowed spacing between **k** points in units of
$\AA^{-1}$. The number of **k** points increases when
the spacing is decreased.

The number of **k** points in the direction of the first, second and
third reciprocal lattice vector is determined by
$N_i= \mathrm{max}(1, \mathrm{ceiling}( | \mathbf{b}_i| 2\pi /
\mathrm{KSPACING} ))$, where
$\mathrm{ceiling}( x )$ returns the least integer that
is equal or larger than $x$. Here,
$\mathbf{b}_i$ are the reciprocal lattice vectors
$\mathbf{b}_i \mathbf{a}_j = \delta_{ij}$.

The generated grid is centered at the $\Gamma$ point
if [`KGAMMA`](KGAMMA.md)` = T` (default), i.e., includes the
$\Gamma$ point. For
[`KGAMMA`](KGAMMA.md)` = F`, the grid is shifted away from
the $\Gamma$ point
as done for Monkhorst-Pack grids.

|  |
|----|
| **Mind:** The definition of $N_i$ is not entirely identical with the deprecated [automatic k-point generation](../input-files/KPOINTS.md) used in the [KPOINTS](../input-files/KPOINTS.md) file. We recommend using the KSPACING tag and avoiding the automatic mode via the [KPOINTS](../input-files/KPOINTS.md) file. |

## Related tags and articles\[<a href="/wiki/index.php?title=KSPACING&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

Tags: [KGAMMA](KGAMMA.md),
[KSPACING_OPT](KSPACING_OPT.md)

Files: [KPOINTS](../input-files/KPOINTS.md),
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-KSPACING-_incategory-HowTo)



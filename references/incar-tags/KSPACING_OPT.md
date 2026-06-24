<!-- Source: https://vasp.at/wiki/index.php/KSPACING_OPT | revid: 35396 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KSPACING_OPT
KSPACING_OPT = \[real\]  
Default: **KSPACING_OPT** = 0.5 

Description: Spacing between **k** points in the automatically generated
mesh for the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) driver if
the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file is not present.

------------------------------------------------------------------------

KSPACING_OPT is used to define the **k**-point mesh of the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) driver, where the wave
functions are computed non-self-consistently. This is useful to obtain
the density of states on a mesh finer than the one used in the SCF run.

KSPACING_OPT is the smallest allowed spacing between **k** points in
units of $\AA^{-1}$. The number of **k**
points increases when the spacing is decreased. The number of **k**
points in the direction of the first, second and third reciprocal
lattice vector is determined by $N_i=
\mathrm{max}(1, \mathrm{ceiling}( | \mathbf{b}_i| 2\pi /
\mathrm{KSPACING\\OPT} ))$, where $\mathrm{ceiling}( x )$ returns the least integer that is equal
or larger than $x$. Here,
$\mathbf{b}_i$ are the reciprocal
lattice vectors $\mathbf{b}_i \mathbf{a}_j =
\delta_{ij}$. The generated grid is centered at the
$\Gamma$ point if
[`KGAMMA`](KGAMMA.md)` = T` (default), i.e., includes the
$\Gamma$ point. For
[`KGAMMA`](KGAMMA.md)` = F`, the grid is shifted away from
the $\Gamma$ point as done for
Monkhorst-Pack grids.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

## Related tags and articles
Tags: [KSPACING](KSPACING.md),
[KGAMMA](KGAMMA.md),
[LKPOINTS_OPT](LKPOINTS_OPT.md)

Files: [KPOINTS](../input-files/KPOINTS.md),
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-KSPACING_OPT-_incategory-HowTo)

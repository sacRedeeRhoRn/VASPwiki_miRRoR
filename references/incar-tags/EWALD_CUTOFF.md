<!-- Source: https://vasp.at/wiki/index.php/EWALD_CUTOFF | revid: 35860 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EWALD_CUTOFF


EWALD_CUTOFF = \[real\] 

|                           |       |     |
|---------------------------|-------|-----|
| Default: **EWALD_CUTOFF** | = 4.0 |     |

Description: EWALD_CUTOFF sets
the unified cutoff radius for the Ewald summation of the electrostatic
interaction. It controls both the number of cells that contribute (in
real space) as well as the number of G-vectors that are considered (in
reciprocal space).

------------------------------------------------------------------------

The default value of
EWALD_CUTOFF is a safe choice
in nearly all cases. For bulk systems, increasing it will not change the
total energy by more than a few \$\mu\$eV.

For surface calculations with large cells and thick vacuum regions,
however, some necessary G-vectors may be cut off for the default value
of EWALD_CUTOFF, and
variations in total energy might increase to the order of 10 meV. This
can spoil convergence with respect to the number of layers or the size
of the vacuum for weakly bound surfaces.

|  |
|----|
| **Tip:** For highly accurate slab calculations, set `EWALD_CUTOFF`` = 6.0`. |

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

## Related tags and articles\[<a
href="/wiki/index.php?title=EWALD_CUTOFF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[2D materials](../categories/Category-2D_materials.md),
[electrostatics](../categories/Category-Electrostatics.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EWALD_CUTOFF-_incategory-HowTo)



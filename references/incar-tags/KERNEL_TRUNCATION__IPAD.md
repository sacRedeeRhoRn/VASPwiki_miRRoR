<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/IPAD | revid: 34843 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/IPAD
KERNEL_TRUNCATION/IPAD = integer 

|  |  |  |
|----|----|----|
| Default: **KERNEL_TRUNCATION/IPAD** | = 3 | if [`KERNEL_TRUNCATION/IDIMENSIONALITY`](KERNEL_TRUNCATION__IDIMENSIONALITY.md)` = 0` |
|  | = 2 | if [`KERNEL_TRUNCATION/IDIMENSIONALITY`](KERNEL_TRUNCATION__IDIMENSIONALITY.md)` = 2` |

**Description:** KERNEL_TRUNCATION/IPAD controls the padding strategy
used for the Coulomb kernel truncation in reciprocal space. Padding
defines how much additional empty space is introduced around the charge
density before applying
truncation.^([\[1\]](#cite_note-vijay:prb:2025-1)) This affects both the
accuracy of the truncated Coulomb potential and the computational cost.

------------------------------------------------------------------------

Setting KERNEL_TRUNCATION/IPAD allows fine control over how much
zero-padding is applied along each reciprocal-space direction. Padding
ensures that the truncated Coulomb kernel does not artificially interact
with its periodic replicas in non-periodic directions.

Typically, increasing KERNEL_TRUNCATION/IPAD improves accuracy at the
expense of computational cost.

[TABLE]

|  |
|----|
| **Warning:** When padding is used, the vaccum is added on the edges of the cell, as such it is very important that the motif is centered in the simulation box. If you encounter problems using Coulomb truncation with padding, try the same calculations without padding (see examples bellow). |

## Example
    KERNEL_TRUNCATION {
         LTRUNCATE       = T
         IDIMENSIONALITY = 2
         ISURFACE        = 3
         IPAD            = 2
         FACTOR          = 1
    }

In this case an additional empty cell is added along the z direction as
padding. The coulomb interaction is truncated beyond a z length. This
ensures maximum usage of the simulation box.

    KERNEL_TRUNCATION {
         LTRUNCATE       = T
         IDIMENSIONALITY = 2
         ISURFACE        = 3
         IPAD            = 1
         FACTOR          = 0.5
    }

This setup corresponds to truncating the Coulomb interaction along the
surface normal (z-direction) for a 2D material, using no vacuum padding
and a truncation length of z/2. In this case, half of the simulation box
is effectively unused, but the algorithm remains simpler. This
configuration can be useful for debugging purposes.

## Related tags and articles
[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/IDIMENSIONALITY](KERNEL_TRUNCATION__IDIMENSIONALITY.md),
[KERNEL_TRUNCATION/LCOARSEN](KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/FACTOR](KERNEL_TRUNCATION__FACTOR.md),
[KERNEL_TRUNCATION/ISURFACE](KERNEL_TRUNCATION__ISURFACE.md)

## References
1.  [↑](#cite_ref-vijay:prb:2025_1-0) [S. Vijay, M. Schlipf, H.
    Miranda, F. Karsai, M. Kaltak, M. Marsman, and G. Kresse, *Efficient
    periodic density functional theory calculations of charged molecules
    and surfaces using Coulomb kernel truncation*, Phys. Rev. B **112**,
    045409 (2025).](https://doi.org/10.1103/cd6s-cdkf)

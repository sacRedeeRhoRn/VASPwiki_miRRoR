<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/ISURFACE | revid: 34868 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/ISURFACE
KERNEL_TRUNCATION/ISURFACE = 1 \| 2 \| 3 

Description: Specifies the non-periodic dimension when performing
calculations with the Coulomb-kernel-truncation method for [2D
materials](../redirects/2D_materials.md).

------------------------------------------------------------------------

When performing Coulomb-kernel truncation
([`KERNEL_TRUNCATION/LTRUNCATE`](KERNEL_TRUNCATION__LTRUNCATE.md)` = T`)
with
[`KERNEL_TRUNCATION/IDIMENSIONALITY`](KERNEL_TRUNCATION__IDIMENSIONALITY.md)` = 2`,
KERNEL_TRUNCATION/ISURFACE specifies which direction is non-periodic. If
the surface normal points in the direction of the x-axis set
`KERNEL_TRUNCATION/ISURFACE`` = 1`, if it is along the y-axis set
`KERNEL_TRUNCATION/ISURFACE`` = 2`, and along the z-axis set
`KERNEL_TRUNCATION/ISURFACE`` = 3`.

[TABLE]

## Related tags and articles
[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/LCOARSEN](KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/IDIMENSIONALITY](KERNEL_TRUNCATION__IDIMENSIONALITY.md),
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md),
[KERNEL_TRUNCATION/FACTOR](KERNEL_TRUNCATION__FACTOR.md)

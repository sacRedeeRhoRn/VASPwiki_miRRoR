<!-- Source: https://vasp.at/wiki/index.php/FMP_SWAPNUM | revid: 27497 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FMP_SWAPNUM
FMP_SWAPNUM = integer  
Default: **FMP_SWAPNUM** = 1 

Description: Number of pairs that are exchanged in a single swapping
event in the [Müller-Plathe
method](../tutorials/Müller-Plathe_method.md).

------------------------------------------------------------------------

FMP_SWAPNUM defines the number of pairs of particles exchanged in a
single swapping event of the reverse nonequilibrium molecular dynamics
run using the [Müller-Plathe
method](../tutorials/Müller-Plathe_method.md). Only
the particles of the same type are selected.

|                                                           |
|-----------------------------------------------------------|
| **Mind:** This tag will only be available from VASP 6.4.4 |

## Related tags and articles
[Müller-Plathe
method](../tutorials/Müller-Plathe_method.md),
[FMP_DIRECTION](FMP_DIRECTION.md),
[FMP_ACTIVE](FMP_ACTIVE.md),
[FMP_SNUMBER](FMP_SNUMBER.md),
[FMP_PERIOD](FMP_PERIOD.md)

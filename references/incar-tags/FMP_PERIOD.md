<!-- Source: https://vasp.at/wiki/index.php/FMP_PERIOD | revid: 27502 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FMP_PERIOD
FMP_PERIOD = integer  
Default: **FMP_PERIOD** = 10 

Description: Number of time steps between two swapping events in the
[Müller-Plathe
method](../tutorials/Müller-Plathe_method.md).

------------------------------------------------------------------------

This tag defines how many MD steps are done between two consecutive
velocity-swapping events. The period is counted in MD steps and not in
simulation time.

|                                                           |
|-----------------------------------------------------------|
| **Mind:** This tag will only be available from VASP 6.4.4 |

## Related tags and articles
[Müller-Plathe
method](../tutorials/Müller-Plathe_method.md),
[FMP_ACTIVE](FMP_ACTIVE.md),
[FMP_DIRECTION](FMP_DIRECTION.md),
[FMP_SNUMBER](FMP_SNUMBER.md),
[FMP_SWAPNUM](FMP_SWAPNUM.md)

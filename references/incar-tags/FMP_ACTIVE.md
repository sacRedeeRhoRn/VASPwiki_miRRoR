<!-- Source: https://vasp.at/wiki/index.php/FMP_ACTIVE | revid: 27496 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FMP_ACTIVE
FMP_ACTIVE = logical (aray) 

|                         |                  |     |
|-------------------------|------------------|-----|
| Default: **FMP_ACTIVE** | = NIONS \* False |     |

Description: Select which atom types in the
[POSCAR](../input-files/POSCAR.md)-file participate in swapping within the
[Müller-Plathe
method](../tutorials/Müller-Plathe_method.md).

------------------------------------------------------------------------

FMP_ACTIVE specifies whether or not (.TRUE. or .FALSE., respectively) an
atomic type allowed for swapping within the [Müller-Plathe
method](../tutorials/Müller-Plathe_method.md). One
item for each of the atomic types defined in
[POSCAR](../input-files/POSCAR.md) must be supplied.

|                                                           |
|-----------------------------------------------------------|
| **Mind:** This tag will only be available from VASP 6.4.4 |

## Related tags and articles
[Müller-Plathe
method](../tutorials/Müller-Plathe_method.md),
[FMP_DIRECTION](FMP_DIRECTION.md),
[FMP_SNUMBER](FMP_SNUMBER.md),
[FMP_SWAPNUM](FMP_SWAPNUM.md),
[FMP_PERIOD](FMP_PERIOD.md)

<!-- Source: https://vasp.at/wiki/index.php/MAXDIS | revid: 36551 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MAXDIS
MAXDIS = \[real\] 

|                     |                      |     |
|---------------------|----------------------|-----|
| Default: **MAXDIS** | = 0.0 (switched off) |     |

Description: This tag sets the maximum distance that an atom is allowed
to travel (in Angstrom) between two ab-initio steps before the charge
density is reset to atomic an atomic charge density.

------------------------------------------------------------------------

At each ionic step, the maximum Cartesian displacement of any atom
(using minimum-image convention) is compared to MAXDIS. If exceeded, the
charge density extrapolation controlled by
[IWAVPR](IWAVPR.md) is skipped and atomic densities are used
instead. Setting MAXDIS=0.0 disables this reset entirely.

MAXDIS is particularly important in [on-the-fly machine learning force
field](../categories/Category-Machine-learned_force_fields.md)
([ML_MODE](ML_MODE.md)=train) calculations, where many
machine-learning-driven ionic steps are executed between successive ab
initio evaluations. This allows atoms to travel a considerable distance
between two DFT calculations, making the charge density from the
previous ab initio step a poor initial guess for the next one —
potentially causing slow or problematic electronic convergence.

## Related tags and articles
[IWAVPR](IWAVPR.md), [IBRION](IBRION.md),
[POTIM](POTIM.md), [ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md)

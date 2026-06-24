<!-- Source: https://vasp.at/wiki/index.php/CUTOFF_SIGMA | revid: 32844 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CUTOFF_SIGMA
CUTOFF_SIGMA = \[real\] ( \[real\] ) 

|                           |       |     |
|---------------------------|-------|-----|
| Default: **CUTOFF_SIGMA** | = 0.1 |     |

Description: CUTOFF_SIGMA specifies the broadening
$\sigma$ in eV for the cutoff function
specified by [CUTOFF_TYPE](CUTOFF_TYPE.md).

------------------------------------------------------------------------

Corresponds to a broadening of the cutoff function used in the [one-shot
method](https://vasp.at/wiki/index.php/Wannier_functions) "Wannier functions")
to obtain Wannier functions. The meaning of $\sigma$ depends on the
[CUTOFF_TYPE](CUTOFF_TYPE.md) tag.

For spin-polarized calculations ([`ISPIN`](ISPIN.md)` = 2`),
two values can be specified for CUTOFF_SIGMA, one for each spin channel.
If only a single value is specified, it will be used for both spin
channels.

## Related tags and articles
[CUTOFF_TYPE](CUTOFF_TYPE.md),
[CUTOFF_MU](CUTOFF_MU.md), [LSCDM](LSCDM.md),
[LOCPROJ](LOCPROJ.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CUTOFF_SIGMA-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/IBAND | revid: 27580 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IBAND
IBAND = \[integer array\]  
Default: **IBAND** = not set 

Description: IBAND sets a list of bands that contribute to calculating
the [partial charge
density](../redirects/Band-decomposed_charge_densities.md).

------------------------------------------------------------------------

IBAND selects a subset of bands for which the partial charge density is
calculated when [LPARD](LPARD.md) = .TRUE.. Partial charge
densities are written to the [PARCHG](../output-files/PARCHG.md) file, or
one of its variants, depending on the setting of
[LSEPB](LSEPB.md) and [LSEPK](LSEPK.md).

|  |
|----|
| **Mind:** Setting IBAND will automatically set [NBMOD](NBMOD.md) = N, where N is the number of bands passed to IBAND, regardless of the [NBMOD](NBMOD.md) setting in the [INCAR](../input-files/INCAR.md) file. |

E.g. if `IBAND = 20 21 22 23 45` the charge density will be calculated
for the four bands 20 to 23 and band 45, and
[NBMOD](NBMOD.md) will be set to 5.

## Related tags and articles
[LPARD](LPARD.md), [NBMOD](NBMOD.md),
[EINT](EINT.md), [KPUSE](KPUSE.md),
[LSEPB](LSEPB.md), [LSEPK](LSEPK.md),
[LPARDH5](LPARDH5.md), [PARCHG](../output-files/PARCHG.md),
[vaspout.h5](../output-files/Vaspout.h5.md), [Band-decomposed charge
densities](../redirects/Band-decomposed_charge_densities.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IBAND-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/KPUSE | revid: 27583 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPUSE
KPUSE = \[integer array\]  
Default: **KPUSE** = not set 

Description: KPUSE sets a list of **k** points that contribute to
calculating the [partial charge
density](../redirects/Band-decomposed_charge_densities.md).

------------------------------------------------------------------------

[IBAND](IBAND.md) selects a subset of *k'* points for which
the partial charge density is calculated when
[LPARD](LPARD.md) = .TRUE.. Partial charge densities are
written to the [PARCHG](../output-files/PARCHG.md) file, or one of its
variants, depending on the setting of [LSEPB](LSEPB.md) and
[LSEPK](LSEPK.md).

|  |
|----|
| **Mind:** All **k** point weights will be internally reset to 1 if KPUSE is specified. Thus results are usually only correct if the groundstate calculation and the partial charge post-processing is performed with [ISYM](ISYM.md) = -1. |

E.g. if `KPUSE = 1 4 7` the charge density will be calculated for the
three **k** points 1, 4, and 7.

## Related tags and articles
[LPARD](LPARD.md), [NBMOD](NBMOD.md),
[EINT](EINT.md), [IBAND](IBAND.md),
[LSEPB](LSEPB.md), [LSEPK](LSEPK.md),
[LPARDH5](LPARDH5.md), [PARCHG](../output-files/PARCHG.md),
[vaspout.h5](../output-files/Vaspout.h5.md), [Band-decomposed charge
densities](../redirects/Band-decomposed_charge_densities.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-KPUSE-_incategory-Examples)

------------------------------------------------------------------------

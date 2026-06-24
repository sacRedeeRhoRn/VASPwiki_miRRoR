<!-- Source: https://vasp.at/wiki/index.php/LPHON_READ_FORCE_CONSTANTS | revid: 18945 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LPHON_READ_FORCE_CONSTANTS
LPHON_READ_FORCE_CONSTANTS = .TRUE. \| .FALSE. 

|                                         |           |     |
|-----------------------------------------|-----------|-----|
| Default: **LPHON_READ_FORCE_CONSTANTS** | = .FALSE. |     |

Description: LPHON_READ_FORCE_CONSTANTS read the force constants from a
vaspin.h5 file containing the force constants computed with a previous
VASP run.

------------------------------------------------------------------------

After the computation of the force constants using finite-differences
([IBRION](IBRION.md)=5,6) or density-functional perturbation
theory ([IBRION](IBRION.md)=7,8) on a supercell the force
constants are written to the vaspout.h5 file. To plot the phonon
dispersion on a different path the user can modify the
[QPOINTS](../input-files/QPOINTS.md) file and read the force constants
computed previously (i.e. without performing the finite-differences
computations on supercells again). To do so copy vaspout.h5 to vaspin.h5
and set LPHON_READ_FORCE_CONSTANTS=.TRUE. in the
[INCAR](../input-files/INCAR.md) file. Note that when this is set only the
phonon dispersion is performed and then VASP quits without running any
additional calculation specified in the [INCAR](../input-files/INCAR.md)
file.

|                                            |
|--------------------------------------------|
| **Mind:** Only available as of VASP 6.4.0. |

## Related tags and articles
[QPOINTS](../input-files/QPOINTS.md),
[LPHON_DISPERSION](LPHON_DISPERSION.md),
[PHON_NWRITE](PHON_NWRITE.md),
[LPHON_POLAR](LPHON_POLAR.md),
[PHON_DIELECTRIC](PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](PHON_G_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPHON_DISPERSION-_incategory-Examples)

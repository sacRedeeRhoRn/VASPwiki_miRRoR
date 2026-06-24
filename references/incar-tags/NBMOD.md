<!-- Source: https://vasp.at/wiki/index.php/NBMOD | revid: 27581 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBMOD
NBMOD = -3 \| -2 \| -1 \| 0 \| \[positive integer\] 

|  |  |  |
|----|----|----|
| Default: **NBMOD** | = n | if [IBAND](IBAND.md) is set and contains n values |
|  | = -2 | if [EINT](EINT.md) is set and [IBAND](IBAND.md) is not set |
|  | = -1 | if neither [EINT](EINT.md) nor [IBAND](IBAND.md) are set |

Description: NBMOD controls how bands are selected when computing
[partial charge
densities](../redirects/Band-decomposed_charge_densities.md).

------------------------------------------------------------------------

NBMOD is used with other tags to define the mode of band selection for
partial charge densities in [PARCHG](../output-files/PARCHG.md),
[vaspout.h5](../output-files/Vaspout.h5.md), or
[CHGCAR](../input-files/CHGCAR.md) files. There are several ways to set
this tag.

- NBMOD = n: Use n bands

If a positive integer is passed, NBMOD represents the number of values
in the array [IBAND](IBAND.md). If
[IBAND](IBAND.md) is specified, NBMOD is set automatically to
the number of values passed in [IBAND](IBAND.md).

|  |
|----|
| **Tip:** There is no good reason to set NBMOD to a positive integer since it will be overwritten regardless if [IBAND](IBAND.md) is set or not. Use the [IBAND](IBAND.md) tag alone to enter this mode. |

- NBMOD = 0: Use all bands

All bands, even unoccupied ones, are contributing to calculating the
partial charge density. E.g. the resulting partial charge density in the
[PARCHG](../output-files/PARCHG.md) file will sum up to twice the value of
the number of total bands [NBANDS](NBANDS.md).

- NBMOD = -1: Use all occupied bands

This mode writes the charge density of all occupied states to the
[CHGCAR](../input-files/CHGCAR.md) file, and no
[PARCHG](../output-files/PARCHG.md) file is produced. In contrast to
producing a [CHGCAR](../input-files/CHGCAR.md) file from the
[WAVECAR](../input-files/WAVECAR.md) input without the partial charges
methodology (e.g. by setting [LPARD](LPARD.md) = .FALSE.,
[ALGO](ALGO.md) = None, and [NELM](NELM.md) = 1),
the [augmentation
occupancies](../methods/Projector-augmented-wave_formalism.md)
is not included in the produced [CHGCAR](../input-files/CHGCAR.md) file for
NBMOD = -1. However, the fine FFT grid's valence charge density is
equivalent.

- NBMOD = -2: Use an absolute energy interval to select contributing
  bands

The partial charge density is calculated for electrons in the energy
interval specified by [EINT](EINT.md).

- NBMOD = -3: Use an energy interval to select contributing bands and
  add the Fermi energy $\epsilon_f$ to
  the passed values

The partial charge density is calculated for electrons in the energy
interval specified by [EINT](EINT.md). In this mode, the
values in [EINT](EINT.md) are interpreted as relative to the
Fermi energy $\epsilon_f$. E.g. if
[EINT](EINT.md) = -0.1 0.5 and $\epsilon_f$ = 2.43, the chosen energy interval will range from
2.33 to 2.93 eV.

## Related tags and articles
[LPARD](LPARD.md), [IBAND](IBAND.md),
[EINT](EINT.md), [KPUSE](KPUSE.md),
[LSEPB](LSEPB.md), [LSEPK](LSEPK.md),
[LPARDH5](LPARDH5.md), [PARCHG](../output-files/PARCHG.md),
[vaspout.h5](../output-files/Vaspout.h5.md), [Band-decomposed charge
densities](../redirects/Band-decomposed_charge_densities.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NBMOD-_incategory-Examples)

------------------------------------------------------------------------

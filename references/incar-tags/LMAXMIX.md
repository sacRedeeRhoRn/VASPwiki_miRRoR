<!-- Source: https://vasp.at/wiki/index.php/LMAXMIX | revid: 27290 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMAXMIX


LMAXMIX = \[integer\]  
Default: **LMAXMIX** = 2 

Description: LMAXMIX controls
up to which *l*-quantum number the one-center PAW charge densities are
passed through the charge density mixer and written to the
[CHGCAR](../input-files/CHGCAR.md) file.

------------------------------------------------------------------------

Higher *l*-quantum numbers
(*l*\>LMAXMIX) are not handled
by the [density
mixer](../categories/Category-Density_mixing.md) (these
components of the one-center charge density are set to the value
corresponding to the present orbitals). Usually, it is not necessary to
increase LMAXMIX, but the
following cases are exceptions:

- [DFT+U calculations](../methods/Category-DFT+U.md) require,
  in many cases, an increase of
  LMAXMIX to 4 for
  *d*-electrons (or 6 for *f*-elements) to obtain fast convergence to
  the ground state.

<!-- -->

- The [CHGCAR](../input-files/CHGCAR.md) file will contain the one-center
  PAW occupancy matrices up to
  LMAXMIX. When the
  [CHGCAR](../input-files/CHGCAR.md) file is read and kept fixed in the
  course of the calculations ([ICHARG](ICHARG.md)=11), the
  results will not necessarily be identical to a self-consistent run.
  The deviations will be large for DFT+U calculations. For the
  calculation of band structures within the DFT+U approach, it is
  strictly required to increase
  LMAXMIX to 4 for
  *d*-elements and to 6 for *f*-elements.

<!-- -->

- [SDFT calculations](../categories/Category-Magnetism.md)
  that consider noncollinear magnetism often require slow mixing of the
  spin density up to 4 for *d*-elements and up to 6 for *f*-elements to
  obtain fast convergence to the ground state.

## Related tags and articles\[<a href="/wiki/index.php?title=LMAXMIX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [BMIX](BMIX.md),
[AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [AMIN](AMIN.md),
[MIXPRE](MIXPRE.md), [WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMAXMIX-_incategory-Examples)



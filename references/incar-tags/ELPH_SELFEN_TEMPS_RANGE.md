<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_TEMPS_RANGE | revid: 32911 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_TEMPS_RANGE


ELPH_SELFEN_TEMPS_RANGE =
\[real array\] 

Description: The range of temperatures (in K) at which to compute the
phonon-mediated electron self-energy and transport coefficients.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This list of temperatures is used to determine the chemical potential,
the occupation factors entering the electron self-energy due to
electron-phonon coupling as well as the transport coefficients in the
context of a [transport
calculation](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

A range of temperatures can be defined using
`ELPH_SELFEN_TEMPS_RANGE`` = l u n`,
where:

- *l* is the lower limit of the temperature range.
- *u* is the upper limit of the temperature range.
- *n* is the number of steps between the two limits.

For example,
`ELPH_SELFEN_TEMPS_RANGE`` = 0 700 41`
would create a list of **41** points from 0 K to 700 K. This is printed
in the [OUTCAR](../output-files/OUTCAR.md) file:

    elph_selfen_temps=
          0.000
         17.500
         35.000
      ...
        665.000
        682.500
        700.000

At each temperature an electron-phonon calculation is performed, rather
than defining it manually using
[ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_TEMPS_RANGE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [Chemical potential in electron-phonon
  interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_MU](ELPH_SELFEN_MU.md)
- [ELPH_SELFEN_MU_RANGE](ELPH_SELFEN_MU_RANGE.md)
- [ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
- [NELECT](NELECT.md)



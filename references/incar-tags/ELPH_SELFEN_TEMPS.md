<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_TEMPS | revid: 32626 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_TEMPS


ELPH_SELFEN_TEMPS = \[real
array\]  
Default: **ELPH_SELFEN_TEMPS** = 0 100 200 300 400 500 

Description: List of temperatures for which to compute the electron
self-energy due to electron-phonon coupling.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This list of temperatures is used to determine the chemical potential,
the occupation factors entering the electron self-energy due to
electron-phonon coupling as well as the transport coefficients in the
context of a [transport
calculation](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

The chemical potential is determined for the list of temperatures
ELPH_SELFEN_TEMPS and carrier
concentrations specified by
[ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
or
[ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md).
You can also express a range of temperatures using
[ELPH_SELFEN_TEMPS_RANGE](ELPH_SELFEN_TEMPS_RANGE.md).
Alternatively, one can specify the chemical potential and determine the
carrier concentration using
[ELPH_SELFEN_MU](ELPH_SELFEN_MU.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_TEMPS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Chemical potential in electron-phonon
  interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_TEMPS_RANGE](ELPH_SELFEN_TEMPS_RANGE.md)
- [ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_SELFEN_MU](ELPH_SELFEN_MU.md)
- [ELPH_SELFEN_MU_RANGE](ELPH_SELFEN_MU_RANGE.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)



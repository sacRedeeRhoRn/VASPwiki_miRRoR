<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_MU_RANGE | revid: 32909 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_MU_RANGE


ELPH_SELFEN_MU_RANGE = \[real
array\] 

Description: List of the range of chemical potentials (in eV) at which
to compute the phonon-mediated electron self-energy and transport
coefficients.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

A set of different chemical potentials can be set using
ELPH_SELFEN_MU_RANGE as a
shift with respect to the Fermi level $E_F$ as an
alternative to [ELPH_SELFEN_MU](ELPH_SELFEN_MU.md).
A range of chemical potentials can be defined using
`ELPH_SELFEN_MU_RANGE`` = l u n`,
where:

- *l* is the lower limit of the chemical potential range.
- *u* is the upper limit of the chemical potential range.
- *n* is the number of steps between the two limits.

For example,
`ELPH_SELFEN_MU_RANGE`` = -1.0 1.0 101`
would create a list of **101** points around the Fermi level between
$E_F - 1.0$ and $E_F + 1.0$.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_MU_RANGE&amp;veaction=edit&amp;section=1"
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
- [ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
- [ELPH_SELFEN_TEMPS_RANGE](ELPH_SELFEN_TEMPS_RANGE.md)
- [NELECT](NELECT.md)



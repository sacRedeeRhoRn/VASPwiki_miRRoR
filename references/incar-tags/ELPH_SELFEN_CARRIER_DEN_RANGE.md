<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_CARRIER_DEN_RANGE | revid: 34575 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_CARRIER_DEN_RANGE


ELPH_SELFEN_CARRIER_DEN_RANGE =
\[real array\] 

Description: List of carrier density ranges in logarithmic scale (in
$cm^{-3}$) at which to compute the phonon-mediated
electron self-energy and transport coefficients.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

From each carrier density specified in the array, a positive (electron
doping) or negative (hole doping) number of electrons is added to the
value of [NELECT](NELECT.md) and the chemical potential
computed. A range of carrier densities can be defined using
`ELPH_SELFEN_CARRIER_DEN_RANGE`` = l u n`,
where:

- *l* is the lower limit of the carrier density range.
- *u* is the upper limit of the carrier density range.
- *n* is the number of steps between the two limits.

The range of carrier densities is used to generate a log-scale mesh of
carrier densities.

|  |
|----|
| **Important:** *l* or *u* must be both positive (*n*-doping) or both negative (*p*-doping). |

You can add the range (*l* *u* *n*) N times, so you can have several
different meshes of holes or electrons or both. For example,
`ELPH_SELFEN_CARRIER_DEN_RANGE`` = -1e20 -1e16 51 1e20 1e16 51`
would create a list of two meshes of carrier densities,
(`-1e20 -1e16 51`) and (`1e20 1e16 51`). The first mesh has `51` carrier
densities of holes between `-1e16` and `-1e20`; the second mesh has `51`
carrier densities of electrons between `1e16` and `1e20`. You could also
include more meshes if you want. You can check the carriers that you
have chosen in the [OUTCAR](../output-files/OUTCAR.md) file:

    Chemical potential calculation:
    ===============================

    elph_ismear=-24
    elph_fermi_nedos=     501
    elph_selfen_carrier_den=
     -0.100E+21
     -0.832E+20
     -0.692E+20
    ...
     -0.145E+17
     -0.120E+17
     -0.100E+17
      0.100E+21
      0.832E+20
      0.692E+20
    ...
      0.145E+17
      0.120E+17
      0.100E+17

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_CARRIER_DEN_RANGE&amp;veaction=edit&amp;section=1"
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
- [ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
- [ELPH_SELFEN_TEMPS_RANGE](ELPH_SELFEN_TEMPS_RANGE.md)
- [NELECT](NELECT.md)



<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_CARRIER_DEN | revid: 32873 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_CARRIER_DEN


ELPH_SELFEN_CARRIER_DEN =
\[real array\]  
Default: **ELPH_SELFEN_CARRIER_DEN** = 0.0 

Description: List of additional carrier densities in units of
$cm^{-3}$ at which to compute the phonon-mediated
electron self-energy and transport coefficients.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

From each carrier density specified in the array, a positive (electron
doping) or negative (hole doping) number of electrons is added to the
value of [NELECT](NELECT.md) and the chemical potential
computed for the list of temperatures specified by
[ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md).

|  |
|----|
| **Important:** The ELPH_SELFEN_CARRIER_DEN adds electrons when positive, i.e., *n*-doping; when negative, ELPH_SELFEN_CARRIER_DEN removes electrons from the system, i.e., *p*-doping. |

For example, if
`ELPH_SELFEN_CARRIER_DEN`` = 1e+16 1e+17 1e+18`
the `Chemical potential` section in the [OUTCAR](../output-files/OUTCAR.md)
file might show something like

                      Number of electrons per cell
                      ----------------------------
    T=      0.00000000    18.00000048    18.00000477    18.00004770
    T=    100.00000000    18.00000048    18.00000477    18.00004770
    T=    200.00000000    18.00000048    18.00000477    18.00004770
    T=    300.00000000    18.00000048    18.00000477    18.00004770
    T=    400.00000000    18.00000048    18.00000477    18.00004770
    T=    500.00000000    18.00000048    18.00000477    18.00004770
                      ----------------------------
                          Chemical potential
                      ----------------------------
    T=      0.00000000     3.59844447     3.63257112     3.70609450
    T=    100.00000000     3.59030071     3.62874001     3.70431410
    T=    200.00000000     3.56867975     3.61741491     3.69897926
    T=    300.00000000     3.56382644     3.60063388     3.69013925
    T=    400.00000000     3.57552043     3.59226062     3.67812706
    T=    500.00000000     3.58994519     3.59815865     3.66491104
                      ----------------------------

In the above tables, the number of elements in
ELPH_SELFEN_CARRIER_DEN
determines the number of columns, while the number of elements in
[ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
determines the number of rows. Specifying more than one carrier density
in ELPH_SELFEN_CARRIER_DEN
creates additional [electron-phonon
accumulators](../misc/Electron-phonon_accumulators.md).

Instead of specifying a carrier density, it is possible to explicitly
specify the additional number of electrons to be added by using the
[ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md)
tag. Alternatively, one can specify the chemical potential directly and
determine the carrier concentration using
[ELPH_SELFEN_MU](ELPH_SELFEN_MU.md).

The information related to the chemical potential calculation can be
found under the `Chemical potential calculation` section in the
[OUTCAR](../output-files/OUTCAR.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_CARRIER_DEN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [Chemical potential in electron-phonon
  interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
- [ELPH_SELFEN_TEMPS_RANGE](ELPH_SELFEN_TEMPS_RANGE.md)
- [ELPH_SELFEN_MU](ELPH_SELFEN_MU.md)
- [ELPH_SELFEN_MU_RANGE](ELPH_SELFEN_MU_RANGE.md)
- [NELECT](NELECT.md)



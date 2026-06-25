<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_CARRIER_PER_CELL | revid: 32875 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_CARRIER_PER_CELL


ELPH_SELFEN_CARRIER_PER_CELL =
\[real array\]  
Default: **ELPH_SELFEN_CARRIER_PER_CELL** = 0.0 

Description: List of additional number of carriers for which to compute
the phonon-mediated electron self-energy and transport coefficients.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Each number of carriers specified in the array is added to the value of
[NELECT](NELECT.md) and the chemical potential computed for
the list of temperatures specified by
[ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md). A
positive number adds electrons (electron doping), while a negative one
removes (hole doping).

For example,
`ELPH_SELFEN_CARRIER_PER_CELL`` = 0.001 0.01 0.1`
means that the number of electrons per cell
[`NELECT`](NELECT.md)` = 18` will be increased by the
specified values which will produce the following table in the
`Chemical potential calculation` section in the
[OUTCAR](../output-files/OUTCAR.md) file

                      Number of electrons per cell
                      ----------------------------
    T=      0.00000000    18.00100000    18.01000000    18.10000000
    T=    100.00000000    18.00100000    18.01000000    18.10000000
    T=    200.00000000    18.00100000    18.01000000    18.10000000
    T=    300.00000000    18.00100000    18.01000000    18.10000000
    T=    400.00000000    18.00100000    18.01000000    18.10000000
    T=    500.00000000    18.00100000    18.01000000    18.10000000
                      ----------------------------
                          Chemical potential
                      ----------------------------
    T=      0.00000000     3.94721622     4.38382135     4.91829386
    T=    100.00000000     3.94656996     4.38304274     4.91799255
    T=    200.00000000     3.94463398     4.38100398     4.91688588
    T=    300.00000000     3.94140548     4.37778815     4.91488514
    T=    400.00000000     3.93688727     4.37341919     4.91204101
    T=    500.00000000     3.93108216     4.36792102     4.90841405
                      ----------------------------

The number of elements in
ELPH_SELFEN_CARRIER_PER_CELL
determines the number of columns in the tables above, while
[ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
determines the number of rows. Specifying more than one carrier density
in
ELPH_SELFEN_CARRIER_PER_CELL
creates additional [electron-phonon
accumulators](../misc/Electron-phonon_accumulators.md).

Instead of specifying the number of carriers, it is possible to specify
an additional carrier density in units of ${m^{-3}}$ via
the
[ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
tag. Alternatively, one can specify the chemical potential and determine
the carrier concentration using
[ELPH_SELFEN_MU](ELPH_SELFEN_MU.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_CARRIER_PER_CELL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [Chemical potential in electron-phonon
  interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_MU](ELPH_SELFEN_MU.md)
- [ELPH_SELFEN_MU_RANGE](ELPH_SELFEN_MU_RANGE.md)
- [ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
- [ELPH_SELFEN_TEMPS_RANGE](ELPH_SELFEN_TEMPS_RANGE.md)
- [NELECT](NELECT.md)



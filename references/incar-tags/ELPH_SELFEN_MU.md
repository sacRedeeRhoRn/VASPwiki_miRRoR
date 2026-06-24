<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_MU | revid: 32878 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_MU
ELPH_SELFEN_MU = \[real array\]  
Default: **ELPH_SELFEN_MU** = 0.0 

Description: List of chemical potentials at which to compute the
phonon-mediated electron self-energy and transport coefficients.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Each chemical potential specified in the list will be added to the Fermi
energy determined for the **k** point grid
[KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md). This Fermi energy
might be different from the one determined in the self-consistent
calculation if the **k** point meshes or
[ELPH_ISMEAR](ELPH_ISMEAR.md) is different from
[ISMEAR](ISMEAR.md). The Fermi energy from the
self-consistent and non-self-consistent calculations can be read from
the [OUTCAR](../output-files/OUTCAR.md) file. For example

    $ grep "Fermi energy" OUTCAR
     Fermi energy:         3.5134142202
     Fermi energy:         3.5314189274 eV (dense k-point grid)

In this example, `ELPH_SELFEN_MU`` = 0.1` means that the chemical
potential will be set to (3.5314189274 + 0.1) eV. This can be verified
`Chemical potential calculation` section of the
[OUTCAR](../output-files/OUTCAR.md) file.

                      Number of electrons per cell
                      ----------------------------
    T=      0.00000000    18.00000452
    T=    100.00000000    18.00000536
    T=    200.00000000    18.00000792
    T=    300.00000000    18.00001223
    T=    400.00000000    18.00001792
    T=    500.00000000    18.00002315

                      ----------------------------
                          Chemical potential
                      ----------------------------
    T=      0.00000000     3.63141893
    T=    100.00000000     3.63141893
    T=    200.00000000     3.63141893
    T=    300.00000000     3.63141893
    T=    400.00000000     3.63141893
    T=    500.00000000     3.63141893
                      ----------------------------

For each of these chemical potentials and temperatures, the number of
electrons per cell is computed and reported. These, in turn, can be
converted to a carrier density by dividing by the volume of the unit
cell. If more than one value is present in ELPH_SELFEN_MU, more columns
are added to the list of chemical potentials above and more instances of
the electron self-energy
[accumulators](../misc/Electron-phonon_accumulators.md)
are created. Alternatively, you can specify a range of chemical
potentials using
[ELPH_SELFEN_MU_RANGE](ELPH_SELFEN_MU_RANGE.md).
The number of rows is set by the list of temperatures in
[ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md).

Alternatively, one can specify the carrier density in units of
${m^{-3}}$ by using the
[ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
tag.

## Related tags and articles
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [Chemical potential in electron-phonon
  interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md)
- [ELPH_SELFEN_TEMPS_RANGE](ELPH_SELFEN_TEMPS_RANGE.md)
- [NELECT](NELECT.md)
- [ELPH_SELFEN_MU_RANGE](ELPH_SELFEN_MU_RANGE.md)

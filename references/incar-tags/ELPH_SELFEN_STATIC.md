<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_STATIC | revid: 27951 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_STATIC
ELPH_SELFEN_STATIC = \[logical\]  
Default: **ELPH_SELFEN_STATIC** = .FALSE. 

Description: Activates the adiabatic approximation for the
phonon-induced electron self-energy.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The adiabatic approximation assumes that the electron dynamics are much
faster than the phonon dynamics. In other words, there is no energy
exchange between the electronic and the phononic subsystems.
Mathematically, this is equivalent to setting the phonon frequencies in
the denominator of the Fan-Migdal self-energy to zero.

|  |
|----|
| **Warning:** The adiabatic approximation is ill-suited for polar materials where it may introduce large errors ^([\[1\]](#cite_note-ponce:jcp:2015-1)). |

## Related tags and articles
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DELTA](ELPH_SELFEN_DELTA.md)

## References
1.  [↑](#cite_ref-ponce:jcp:2015_1-0) [S. Poncé, Y. Gillet, J. Laflamme
    Janssen, A. Marini, M. Verstraete, and X. Gonze, *Temperature
    dependence of the electronic structure of semiconductors and
    insulators*, J. Chem. Phys. **143 (10)**, 102813
    (2015).](https://doi.org/10.1063/1.4927081)

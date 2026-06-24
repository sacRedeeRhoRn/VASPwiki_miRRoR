<!-- Source: https://vasp.at/wiki/index.php/ELPH_IGNORE_IMAG_PHONONS | revid: 32872 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_IGNORE_IMAG_PHONONS
ELPH_IGNORE_IMAG_PHONONS = \[logical\]  
Default: **ELPH_IGNORE_IMAG_PHONONS** = .FALSE. 

Description: If enabled, VASP ignores imaginary phonon frequencies
during electron-phonon calculations.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Imaginary phonon frequencies are often a sign that the system in
question is not well-converged or not well-described by the simulation.
In this case, the system should first be properly converged until stable
(real) phonons are obtained.

|  |
|----|
| **Mind:** Imaginary phonon frequencies can also appear at phase transitions or other lattice instabilities. However, for [perturbative electron-phonon calculations](../tutorials/Electron-phonon_potential_from_supercells.md), you should always choose a stable equilibrium structure. |

If imaginary phonon frequencies are encountered during an
electron-phonon calculation, VASP simply stops. If
`ELPH_IGNORE_IMAG_PHONONS`` = True`, VASP instead skips the q-points at
which the phonon frequencies are imaginary. This can be useful since
even a stable system can sometimes exhibit small imaginary phonon
frequencies around the $\Gamma$-point
due to numerical inaccuracies.

## Related tags and articles
- [ELPH_RUN](ELPH_RUN.md)
- [IFC_ASR](IFC_ASR.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)

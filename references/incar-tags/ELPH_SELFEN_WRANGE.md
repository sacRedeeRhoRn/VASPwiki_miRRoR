<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_WRANGE | revid: 27949 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_WRANGE
ELPH_SELFEN_WRANGE = \[real\]  
Default: **ELPH_SELFEN_WRANGE** = 0 

Description: Together with
[ELPH_SELFEN_NW](ELPH_SELFEN_NW.md) specifies the
energy window in which to evaluate the phonon-induced electron
self-energy.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The electron self-energy, $\Sigma_{n
\mathbf{k}}(\omega)$, depends on the frequency
$\omega$ (or energy
$\hbar \omega$). The tag
ELPH_SELFEN_WRANGE determines the width of the energy window in which to
evaluate the self-energy. However, the location and width of the energy
window is also influenced by the sign of
[ELPH_SELFEN_NW](ELPH_SELFEN_NW.md). For more
information, we refer to the documentation of
[ELPH_SELFEN_NW](ELPH_SELFEN_NW.md).

## Related tags and articles
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)
- [ELPH_SELFEN_NW](ELPH_SELFEN_NW.md)

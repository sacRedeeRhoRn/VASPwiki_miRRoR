<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_G_SKIP | revid: 32738 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_G_SKIP
ELPH_SELFEN_G_SKIP = \[logical\]  
Default: **ELPH_SELFEN_G_SKIP** = .FALSE. 

Description: Skip the computation of the electron-phonon matrix elements
and instead assume their numerical value is 1.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This option is intended for debugging purposes, as it allows testing the
self-energy and transport routines without performing the full
evaluation of the coupling matrix elements.

## Related tags and articles
- [ELPH_SELFEN_IMAG_SKIP](ELPH_SELFEN_IMAG_SKIP.md)
- [ELPH_WF_REDISTRIBUTE](ELPH_WF_REDISTRIBUTE.md)
- [ELPH_RUN](ELPH_RUN.md)

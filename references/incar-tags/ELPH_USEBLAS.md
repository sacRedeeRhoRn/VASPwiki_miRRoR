<!-- Source: https://vasp.at/wiki/index.php/ELPH_USEBLAS | revid: 32880 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_USEBLAS
ELPH_USEBLAS = \[logical\]  
Default: **ELPH_USEBLAS** = .TRUE. 

Description: Toggles the use of BLAS routines for computing
electron-phonon matrix elements.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This is a performance setting that can offer a significant performance
boost. If `ELPH_USEBLAS`` = True`, then VASP uses
[BLAS](https://www.netlib.org/blas/) routines when computing the
electron-phonon matrix elements. Otherwise, VASP-internal routines are
used.

## Related tags and articles
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_DECOMPOSE](ELPH_DECOMPOSE.md)

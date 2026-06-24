<!-- Source: https://vasp.at/wiki/index.php/LSCALAPACK | revid: 16871 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSCALAPACK
LSCALAPACK = \[logical\] 

|  |  |  |
|----|----|----|
| Default: **LSCALAPACK** | = .TRUE. | if VASP is compiled with scaLAPACK support (precompiler flag -DscaLAPACK) |
|  | = .FALSE. | otherwise |

Description: LSCALAPACK controls the use of scaLAPACK.

------------------------------------------------------------------------

For LSCALAPACK=.TRUE., VASP uses scaLAPACK routines for the
orthonormalization of the wave functions and subspace diagonalizations.

The use of scaLAPACK for the LU decomposition in the orthonormalization
of the wave functions may be independently switched off
([LSCALU](LSCALU.md)=.FALSE.).

## Related tags and articles
[NPAR](NPAR.md), [NCORE](NCORE.md),
[LPLANE](LPLANE.md), [NSIM](NSIM.md),
[KPAR](KPAR.md), [LSCALU](LSCALU.md),
[LSCAAWARE](LSCAAWARE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSCALAPACK-_incategory-Examples)

------------------------------------------------------------------------

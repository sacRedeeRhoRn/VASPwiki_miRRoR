<!-- Source: https://vasp.at/wiki/index.php/LSCAAWARE | revid: 16870 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSCAAWARE
LSCAAWARE = \[logical\] 

|  |  |  |
|----|----|----|
| Default: **LSCAAWARE** | = .TRUE. | if VASP is compiled with scaLAPACK support (precompiler flag -DscaLAPACK) |
|  | = .FALSE. | otherwise |

Description: LSCAAWARE controls the distribution of the Hamilton matrix.

------------------------------------------------------------------------

For LSCAAWARE=.TRUE., VASP distributes the Hamilton matrix among the MPI
ranks. For LSCAAWARE=.FALSE., each MPI ranks allocates the complete
Hamiltonain. In both cases [LSCALAPACK](LSCALAPACK.md)
decides if ScaLAPACK routines are used for diagonalization.

## Related tags and articles
[NPAR](NPAR.md), [NCORE](NCORE.md),
[LPLANE](LPLANE.md), [NSIM](NSIM.md),
[KPAR](KPAR.md), [LSCALU](LSCALU.md),
[LSCALAPACK](LSCALAPACK.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSCAAWARE-_incategory-Examples)

------------------------------------------------------------------------

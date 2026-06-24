<!-- Source: https://vasp.at/wiki/index.php/LSCALU | revid: 16874 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSCALU
LSCALU = \[logical\]  
Default: **LSCALU** = .FALSE. 

Description: LSCALU switches on the parallel LU decomposition (using
scaLAPACK) in the orthonormalization of the wave functions.

------------------------------------------------------------------------

For LSCALU=.TRUE. the LU decomposition in the orthormalization of the
wave functions is done in parallel, using scaLAPACK routines. Provided,
of course, [LSCALAPACK](LSCALAPACK.md)=.TRUE. and VASP
was compiled with scaLAPACK support ([precompiler
flag](../redirects/Precompiler_flags.md): -DscaLAPACK).

In many cases, the scaLAPACK LU decomposition based is *slower* than the
serial LU decomposition (compare the timing `ORTHCH` in the respective
[OUTCAR](../output-files/OUTCAR.md) files). Hence the default is
LSCALU=.FALSE. (subspace rotations, however, are still done using
scaLAPACK).

## Related tags and articles
[NPAR](NPAR.md), [NCORE](NCORE.md),
[LPLANE](LPLANE.md), [NSIM](NSIM.md),
[KPAR](KPAR.md), [LSCALAPACK](LSCALAPACK.md),
[LSCAAWARE](LSCAAWARE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSCALU-_incategory-Examples)

------------------------------------------------------------------------

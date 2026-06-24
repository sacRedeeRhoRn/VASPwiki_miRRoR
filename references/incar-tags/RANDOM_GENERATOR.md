<!-- Source: https://vasp.at/wiki/index.php/RANDOM_GENERATOR | revid: 32915 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# RANDOM_GENERATOR
RANDOM_GENERATOR = default \| pcg_32 

Description: Specifies the random-number generator used to initialize
the wavefunction (see [INIWAV](INIWAV.md)) for [electronic
minimization](../redirects/Electronic_minimization.md),
initialize atomic velocities for [molecular
dynamics](../redirects/Molecular_dynamics.md), etc.

------------------------------------------------------------------------

The random-number generator (RNG) generates a sequence of random
numbers, which is initialized by the tag
[RANDOM_SEED](RANDOM_SEED.md). By default the random
number generator uses a very stable, compiler and platform independent
algorithm. It is based on the work: "Toward a Universal Random Number
Generator" by George Marsaglia and Arif Zaman. Florida State University
Report: FSU-SCRI-87-50 (1987) and was later modified by F. James and
publisheed ^([\[1\]](#cite_note-james:rpng:1990-1)). This algorithm is
programmed in serial, not utilizing any threading or parallelism. For
normal system the time to initialize wave functions is negligible, but
for large systems with many bands
[`NBANDS`](NBANDS.md)` > 1000`, and plane wave coefficients
this can take several seconds to minutes.

For such systems it can be advantageous to switch
`RANDOM_GENERATOR`` = pcg_32`, which is threaded (need to enable [OpenMP
threading](../misc/Combining_MPI_and_OpenMP.md) at
compile time) over the number of OpenMP threads. The algorithm is also
guaranteed to produce the same random numbers in each call, but might
depend on the compiler and library used. Compared to the default
generator it is thus not platform independent. Hence, use
`RANDOM_GENERATOR`` = default` for strictly reproducible numbers across
different machines at all steps during the calculation or comparison of
VASP versions.

## Related tags and articles
[RANDOM_SEED](RANDOM_SEED.md),
[INIWAV](INIWAV.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-RANDOM_GENERATOR-_incategory-Howto)

## References
1.  [↑](#cite_ref-james:rpng:1990_1-0) [F. James, Computer Physics Comm.
    **49**, 329 (1990).](https://doi.org/10.1016/0010-4655(90)90032-V)

<!-- Source: https://vasp.at/wiki/index.php/NCORE | revid: 34976 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NCORE
NCORE = \[integer\]  
Default: **NCORE** = 1 

Description: NCORE controls how many MPI ranks collaborate on a single
band, parallelizing the
[FFTs](../tutorials/Energy_cutoff_and_FFT_meshes.md)
for that band.

------------------------------------------------------------------------

|                                       |
|---------------------------------------|
| **Mind:** Available as of VASP 5.2.13 |

VASP distributes the available MPI ranks into band groups that each work
on one band, parallelizing the
[FFTs](../tutorials/Energy_cutoff_and_FFT_meshes.md)
for that band. For the common case that
[`IMAGES`](IMAGES.md)` = 1` and no other algorithm-dependent
parallelization (e.g., [NOMEGAPAR](NOMEGAPAR.md)) is
active:

$\text{available ranks} = \frac{\text{total MPI
ranks}}{\text{KPAR}}$

NCORE sets the size of each band group. The number of bands treated in
parallel is then:

[NPAR](NPAR.md) = $\text{available
ranks}$ / NCORE

This makes NCORE and [NPAR](NPAR.md) strict inverses of one
another for a given number of available ranks. **Do not set NCORE and
[NPAR](NPAR.md) at the same time.** If both are present in the
[INCAR](../input-files/INCAR.md), [NPAR](NPAR.md) takes precedence
for legacy reasons. Nevertheless, we strongly encourage using NCORE
instead of [NPAR](NPAR.md) for all modern VASP versions.

## Common settings
- NCORE = $\sim \sqrt{\text{available ranks}}$: each band group of NCORE ranks parallelizes its FFTs
  internally. This reduces both memory requirements (projector functions
  are shared within the group) and the cost of orthogonalization. **This
  is the recommended regime for modern multi-core machines.**

&nbsp;

- `NCORE`` = 1` (default): each band is handled by a single rank. The
  maximum number of bands is treated in parallel, but the non-local
  projector functions must be stored in full on every rank, leading to
  high memory usage. In addition, orthogonalizing the bands requires
  heavy all-to-all communication between all ranks. This setting is
  appropriate for small unit cells or machines with limited
  communication bandwidth.

&nbsp;

- NCORE = $\text{available ranks}$: all
  ranks collaborate on a single band, distributing only the plane-wave
  coefficients. No band parallelization occurs. This is almost always
  very slow and should be avoided.

|  |
|----|
| **Warning:** When running with [OpenMP threading](../misc/Combining_MPI_and_OpenMP.md) or any of the [GPU-offloaded code paths](../misc/GPU_ports_of_VASP.md), NCORE is automatically reset to `NCORE`` = 1`, regardless of the value set in the [INCAR](../input-files/INCAR.md) file. FFT parallelization is then handled by OpenMP threads or the GPU. Use the number of OpenMP threads per rank for fine-grained control over FFT parallelization in those cases. |

## Recommendations
|  |
|----|
| **Tip:** Consult the [optimizing the parallelization](../tutorials/Optimizing_the_parallelization.md) page for a step-by-step guide on how to optimize your parallelization. The examples below are only rough guidelines. For any non-trivial production run, perform a short benchmarking scan over a few values of NCORE before committing to one setting. |

General guidelines:

- **Small systems or slow networks** (up to ~8 cores, Gbit Ethernet
  interconnect): use `NCORE`` = 1`. The limited number of ranks and slow
  interconnect make FFT parallelization within band groups inefficient.

&nbsp;

- **Modern multi-core clusters** (Infiniband or equivalent fast
  interconnect): set NCORE to a value between 2 and the number of cores
  per node. NCORE should be a factor of the number of cores per node to
  ensure that all intra-group FFT communication stays within a single
  node. As a rule of thumb, `NCORE`` = 4` works well for ~100 atoms;
  `NCORE`` = 12`–`NCORE`` = 16` is often better for unit cells with more
  than 400 atoms.

&nbsp;

- **NUMA-aware setting**: setting NCORE equal to the number of cores per
  [NUMA
  domain](../tutorials/Optimizing_the_parallelization.md)
  is often a particularly good choice, because all intra-group FFT
  communication then stays within the fastest memory domain of the
  hardware. Use `lstopo` or `numactl --hardware` to determine the NUMA
  layout of your machine.

## Related tags and articles
[NPAR](NPAR.md), [KPAR](KPAR.md),
[LPLANE](LPLANE.md), [LSCALU](LSCALU.md),
[NSIM](NSIM.md), [LSCALAPACK](LSCALAPACK.md),
[LSCAAWARE](LSCAAWARE.md),

[GPU ports of VASP](../misc/GPU_ports_of_VASP.md),
[Combining MPI and
OpenMP](../misc/Combining_MPI_and_OpenMP.md),

[Optimizing the
parallelization](../tutorials/Optimizing_the_parallelization.md),
[Parallelization](../redirects/Parallelization.md), [Energy
cutoff and FFT
meshes](../tutorials/Energy_cutoff_and_FFT_meshes.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NCORE-_incategory-HowTo)

<!-- Source: https://vasp.at/wiki/index.php/NPAR | revid: 34975 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NPAR


NPAR = \[integer\]  
Default: **NPAR** = available ranks 

Description: NPAR determines
the number of bands that are treated in parallel. This is a legacy tag;
use [NCORE](NCORE.md) instead.

------------------------------------------------------------------------

|  |
|----|
| **Warning:** [NCORE](NCORE.md) is the recommended tag for controlling band-level parallelization and has been available since VASP.5.2.13. It is more intuitive and directly expresses the size of each band group. Only use NPAR if you have a specific reason to prefer it. If both NPAR and [NCORE](NCORE.md) are specified in the [INCAR](../input-files/INCAR.md) file, NPAR takes precedence. |

## Relationship to NCORE\[<a href="/wiki/index.php?title=NPAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Relationship to NCORE">edit</a> \| (./index.php.md)\]

VASP distributes the available MPI ranks into band groups that each work
on one band, parallelizing the
[FFTs](../tutorials/Energy_cutoff_and_FFT_meshes.md)
for that band. For the common case that
[`IMAGES`](IMAGES.md)` = 1` and no other algorithm-dependent
parallelization (e.g., [NOMEGAPAR](NOMEGAPAR.md)) is
active::

$\text{available ranks} = \frac{\text{total MPI ranks}}{\text{KPAR}}$

NPAR sets the number of band
groups; [NCORE](NCORE.md) sets the size of each band group.
They are strict inverses:

$\text{NPAR} \times \text{NCORE} = \text{available ranks}$

The default (NPAR = available
ranks) is equivalent to [`NCORE`](NCORE.md)` = 1`: each band
is handled by a single rank.

|  |
|----|
| **Warning:** Setting `NPAR`` = 1` means all available ranks collaborate on a single band (plane-wave coefficient distribution only). No band parallelization occurs. This is almost always very slow and should be avoided. |

|  |
|----|
| **Tip:** See the [optimizing the parallelization](../tutorials/Optimizing_the_parallelization.md) page for a step-by-step guide to finding the best parallelization setup for your system, and [NCORE](NCORE.md) for information on how to parallelize over [FFTs](../tutorials/Energy_cutoff_and_FFT_meshes.md) in particular. |

## Related tags and articles\[<a href="/wiki/index.php?title=NPAR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NCORE](NCORE.md), [KPAR](KPAR.md),
[LPLANE](LPLANE.md), [LSCALU](LSCALU.md),
[NSIM](NSIM.md), [LSCALAPACK](LSCALAPACK.md),
[LSCAAWARE](LSCAAWARE.md)

[GPU ports of VASP](../misc/GPU_ports_of_VASP.md),
[Combining MPI and
OpenMP](../misc/Combining_MPI_and_OpenMP.md),

[Optimizing the
parallelization](../tutorials/Optimizing_the_parallelization.md),
<a href="/wiki/Parallelization" class="mw-redirect"
title="Parallelization">Parallelization</a>, [Energy cutoff and FFT
meshes](../tutorials/Energy_cutoff_and_FFT_meshes.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NPAR-_incategory-HowTo)



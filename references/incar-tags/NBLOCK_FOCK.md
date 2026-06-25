<!-- Source: https://vasp.at/wiki/index.php/NBLOCK_FOCK | revid: 35690 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBLOCK_FOCK


NBLOCK_FOCK = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **NBLOCK_FOCK** | = 64 | **CPU build** |
|  | = 32 | **GPU build** (OpenACC/OpenMP offload)) |
|  | = `OMP_NUM_THREADS` | **CPU build** that is compiled with [OpenMP support](../misc/Precompiler_options.md) and threading is active (`OMP_NUM_THREADS` \> 1) |

Description: Sets the number of orbitals that are processed
simultaneously when computing the action of the Fock potential.

------------------------------------------------------------------------

Instead of computing the action of the Fock potential on one orbital at
a time, up to NBLOCK_FOCK
orbitals are gathered and processed at once. This enables the use of
matrix-matrix operations rather than matrix-vector operations, which is
beneficial for performance on modern hardware.

Tuning NBLOCK_FOCK can
significantly affect both the performance and memory consumption of
hybrid functional calculations. Especially on GPUs,
NBLOCK_FOCK should be tuned
carefully to achieve optimal performance.

|  |
|----|
| **Tip:** On GPU architectures, the optimal value of NBLOCK_FOCK depends strongly on the specific hardware and the number of bands. It is recommended to experiment with values in the range 16-64. |

## Related tags and articles\[<a
href="/wiki/index.php?title=NBLOCK_FOCK&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NSIM](NSIM.md), [LHFCALC](LHFCALC.md),
[AEXX](AEXX.md), [HFSCREEN](HFSCREEN.md),
[NCORE](NCORE.md), [NPAR](NPAR.md),
[KPAR](KPAR.md), [PRECFOCK](PRECFOCK.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NBLOCK_FOCK-_incategory-HowTo)



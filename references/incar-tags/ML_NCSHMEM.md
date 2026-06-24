<!-- Source: https://vasp.at/wiki/index.php/ML_NCSHMEM | revid: 35190 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_NCSHMEM
ML_NCSHMEM = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **ML_NCSHMEM** | = komplex see below | VASP.6.6.0 or higher |
|  | = Number of available ranks per computational node | else |

Description: Specifies the number of MPI ranks that share a single
shared memory segment.

------------------------------------------------------------------------

|  |
|----|
| **Warning:** When compiling with shared memory MPI support (-Duse_shmem), it is utterly important to pin the MPI ranks to the physical cores of the node. For guidance on how to understand the hardware topology of your system and how to correctly set up rank pinning accordingly, refer to [here](../tutorials/Optimizing_the_parallelization.md). |

**Default**: The default is chosen such that the number of available
ranks per computational node are divided by 2 (maximum up to three
times) until the value is lower than or equal to 24 or the value cannot
be subdivided further since it becomes an odd number. E.g. 128 becomes
16, 48 becomes 24, 80 becomes 20, 86 becomes 43 and 16 stays 16.

The total number of memory segments created equals the number of cores
per node divided by ML_NCSHMEM. All memory segments have identical
sizes, so a larger number of segments results in higher total memory
consumption.

However, on systems with multiple NUMA domains, performance can degrade
significantly during machine-learned force field inference if all
domains access the same memory segment. For optimal performance, each
NUMA domain should have its own dedicated shared memory segment. For
more details, we refer to [NCSHMEM](NCSHMEM.md).

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md), [NCSHMEM](NCSHMEM.md),
[Shared memory](../methods/Shared_memory.md)

------------------------------------------------------------------------

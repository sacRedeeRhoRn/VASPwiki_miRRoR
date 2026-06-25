<!-- Source: https://vasp.at/wiki/index.php/NCSHMEM | revid: 33892 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NCSHMEM


NCSHMEM = \[integer\]  
Default: **NCSHMEM** = 1 

Description: Specifies the number of MPI ranks that share a single
shared memory segment in the non-cubic scaling GW routines.

------------------------------------------------------------------------

By default, shared memory is not used in the non-cubic scaling GW
routines ([ALGO](ALGO.md)=EVGW, EVGW0, QPGW and QPGW0). To use
shared-memory MPI in the non-cubic scaling GW, set NCSHMEM to -1 or a
positive integer. If NCSHMEM is set to -1, VASP will automatically
determine how many MPI tasks physically share memory and set NCSHMEM to
that number. For instance, if the machine has 48 or 128 cores per node
(and one core is assigned to each MPI task), NCSHMEM will default to 48
or 128, respectively. Note that larger numbers can degrade performance,
particularly on NUMA architectures and multi socket machines very
significantly (up to a factor 4). In this case, it is often necessary to
manually decrease NCSHMEM to a value between 8 and 32 in order to strike
a balance between memory savings and performance. Specifically, most
EPYC HPC clusters are configured with a mode that divides the memory
into four NUMA domains per socket, with slower communication between the
NUMA domains. Therefore, if you use a machine with 64 cores per socket,
each NUMA domain will consist of 16 cores and NCSHMEM=16 will yield the
best performance (in this case, memory will not be shared between NUMA
domains). The performance penalty may be particularly significant if
memory is shared between sockets.

## Related tags and articles\[<a href="/wiki/index.php?title=NCSHMEM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Shared memory](../methods/Shared_memory.md),
[ML_NCSHMEM](ML_NCSHMEM.md), [ALGO](ALGO.md),
[Practical guide to GW
calculations](../methods/Practical_guide_to_GW_calculations.md)



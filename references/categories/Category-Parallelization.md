<!-- Source: https://vasp.at/wiki/index.php/Category:Parallelization | revid: 35533 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Parallelization


VASP makes use of parallel machines splitting the calculation into many
tasks, that communicate with each other using MPI. Since a single core
cannot perform enough operations, for many complex problems, this
parallelization is necessary to finish the calculation in a reasonable
time.


## Contents


- [1
  Theory](#theory)
  - [1.1 Basic
    parallelization](#basic-parallelization)
  - [1.2
    Communication
    patterns](#communication-patterns)
  - [1.3 MPI
    setup](#mpi-setup)
  - [1.4 File
    handling](#file-handling)
  - [1.5
    Terminology in high-performance computing
    (HPC)](#terminology-in-high-performance-computing-hpc))
- [2 How
  to](#how-to)
  - [2.1 Optimizing
    the parallelization](#optimizing-the-parallelization)
  - [2.2
    OpenMP/OpenACC](#openmpopenacc)
- [3 Additional
  parallelization options](#additional-parallelization-options)


## Theory\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theory">edit</a> \| (./index.php.md)\]

### Basic parallelization\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Basic parallelization">edit</a> \| (./index.php.md)\]

By default, VASP distributes the number of bands
([NBANDS](../incar-tags/NBANDS.md)) over the available MPI ranks. But it
is often beneficial to add parallelization of the FFTs
([NCORE](../incar-tags/NCORE.md)), parallelization over **k** points
([KPAR](../incar-tags/KPAR.md)), and parallelization over separate
calculations ([IMAGES](../incar-tags/IMAGES.md)). All these tags default
to 1 and divide the number of MPI ranks among the parallelization
options. Additionally, there are some parallelization options for
specific algorithms in VASP, e.g.,
[NOMEGAPAR](../incar-tags/NOMEGAPAR.md). In summary, VASP parallelizes
with

$\text{total ranks} = \text{ranks parallelizing bands} \times
\text{NCORE} \times \text{KPAR} \times \text{IMAGES} \times \text{other
algorithm-dependent tags}.$

In addition to the parallelization using MPI, VASP can make use of
[OpenMP
threading](../misc/Combining_MPI_and_OpenMP.md)
and/or [offloading to
GPUs](../misc/GPU_ports_of_VASP.md). Note that running on
multiple OpenMP threads and/or GPUs switches off the
[NCORE](../incar-tags/NCORE.md) parallelization.

### Communication patterns\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Communication patterns">edit</a> \| (./index.php.md)\]

<a href="/wiki/File:Communication.png" class="mw-file-description"
title="VASP divides the available MPI ranks into images, k-point groups, and band groups"><img
src="https://vasp.at/wiki/images/thumb/1/19/Communication.png/513px-Communication.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/1/19/Communication.png/769px-Communication.png 1.5x, /wiki/images/thumb/1/19/Communication.png/1025px-Communication.png 2x"
width="513" height="300"
alt="VASP divides the available MPI ranks into images, k-point groups, and band groups" /></a>
<a href="/wiki/File:Communication2.png" class="mw-file-description"
title="VASP divides the available MPI ranks into images, k-point groups, and band groups"><img
src="https://vasp.at/wiki/images/thumb/0/08/Communication2.png/513px-Communication2.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/08/Communication2.png/769px-Communication2.png 1.5x, /wiki/images/thumb/0/08/Communication2.png/1025px-Communication2.png 2x"
width="513" height="300"
alt="VASP divides the available MPI ranks into images, k-point groups, and band groups" /></a>

The aforementioned parallelization levels directly map onto MPI
communicators. Initially, VASP divides all available ranks into
[IMAGES](../incar-tags/IMAGES.md) equally-sized images. Setting
[KPAR](../incar-tags/KPAR.md) splits each of these images further into
groups of **k** points. Properties involving all **k** points (e.g.
density, Fermi energy) require then a communication over these
**k**-point groups. VASP divides the **k**-point group into band groups
of size [NCORE](../incar-tags/NCORE.md). The band group parallelizes the
FFTs and triggers the most frequent communications. To evaluate
properties involving multiple bands (e.g. Hamiltonian,
orthonormalization) communication between the band groups occurs.

### MPI setup\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: MPI setup">edit</a> \| (./index.php.md)\]

<a href="/wiki/File:Good_process_binding.png"
class="mw-file-description"
title="All ranks associated with a particular band group are on the same node. All communication for the FFTs is intranode."><img
src="https://vasp.at/wiki/images/thumb/7/7f/Good_process_binding.png/380px-Good_process_binding.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/7f/Good_process_binding.png/570px-Good_process_binding.png 1.5x, /wiki/images/7/7f/Good_process_binding.png 2x"
width="380" height="300"
alt="All ranks associated with a particular band group are on the same node. All communication for the FFTs is intranode." /></a>
<a href="/wiki/File:Bad_process_binding.png" class="mw-file-description"
title="Ranks of some band groups extend over multiple nodes. Every FFT requires internode communication."><img
src="https://vasp.at/wiki/images/thumb/5/5d/Bad_process_binding.png/380px-Bad_process_binding.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/5/5d/Bad_process_binding.png/570px-Bad_process_binding.png 1.5x, /wiki/images/5/5d/Bad_process_binding.png 2x"
width="380" height="300"
alt="Ranks of some band groups extend over multiple nodes. Every FFT requires internode communication." /></a>

The MPI setup determines the placement of the ranks onto the nodes. VASP
assumes the ranks first fill up a node before the next node is occupied.
As an example when running with 20 ranks on two nodes, VASP expects rank
1–10 on node 1 and rank 11–20 on node 2. If the ranks are placed
differently, communication between the nodes occurs for every parallel
FFT. Because FFTs are essential to VASP's speed, this deteriorates the
performance of the calculation. A manifestation is an increase in
computing time when the number of nodes is increased from 1 to 2. If
[NCORE](../incar-tags/NCORE.md) is not used this issue is less severe but
will still reduce the performance.

To address this issue, please check the setup of the MPI library and the
submitted job script. It is usually possible to overwrite the placement
by setting environment variables or command-line arguments. When in
doubt, contact the HPC administration of your machine to investigate the
behavior.

### File handling\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: File handling">edit</a> \| (./index.php.md)\]

When VASP is started it reads the file [INCAR](../input-files/INCAR.md) in
the root directory. Because the MPI setup needs to happen early in the
general setup of the calculation the following tags are processed before
any of the other settings:
[NCORE_IN_IMAGE1](../incar-tags/NCORE_IN_IMAGE1.md),
[IMAGES](../incar-tags/IMAGES.md), [KPAR](../incar-tags/KPAR.md),
[NCORE](../incar-tags/NCORE.md), [NPAR](../incar-tags/NPAR.md),
[NCSHMEM](../incar-tags/NCSHMEM.md),
[LUSENCCL](../incar-tags/LUSENCCL.md). When
[IMAGES](../incar-tags/IMAGES.md) are used, subsequently any input given
in the root directory is superseded by the same file in subdirectories
01, 02, ... Any file not present in these subdirectories will be read
from the root directory. The output files are always written to the
subdirectories.

### Terminology in high-performance computing (HPC)\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Terminology in high-performance computing (HPC)">edit</a> \| (./index.php.md)")\]

CPU  
The central processing unit of a computer. A CPU may consist of multiple
*cores*. One or more CPUs can be combined with accelerators like *GPUs*
to form a *node*. Desktop computers typically contain a single CPU.

GPU  
The graphical processing unit. A GPU is very efficient at matrix and
vector operations and may accelerate a program by transferring
particularly suitable tasks from the *CPU* to the GPU.

Core  
When a *CPU* has the option to execute multiple tasks in parallel, we
refer to this as a multi-core CPU. Because these computational cores are
physically close, they typically exhibit a fast communication between
them.

Node  
The node constitutes a physical entity consisting of one or more *CPUs*
potentially accelerated by *GPUs*. The communication between nodes is
much slower compared to the communication within a single node.

NUMA (Non-Uniform Memory Access) domain  
these are distinct regions within a computer system where each core or
group of cores has its own local memory that can be accessed faster than
memory connected to other cores. In a NUMA architecture, memory access
times vary depending on the proximity of the memory to the CPU core
requesting it — local memory access is quicker, while remote access
across domains incurs latency.

Socket  
*Processes* communicate via sockets. Each socket corresponds to an
endpoint in this communication.

Process  
A process is a program executing on one or more *cores*. Multiple
processes may distribute work via communication. Each process may spawn
multiple *threads* to execute their task.

OpenMP thread  
These threads live on a single *node*. *Processes* can instantiate these
threads for loops or other parallel tasks.

Message Passing Interface (MPI)  
A communication protocol to facilitate parallel execution of multiple
*processes*. The *processes* send messages among them to synchronize
parallel tasks when necessary.

Rank  
Each rank corresponds to one *process* participating in the *MPI*
communication. These ranks determine which particular task a *process*
works on and identify senders and receivers of messages.

Memory  
*Processes* store the data they work on in the dynamic random access
memory (DRAM) or random access memory (RAM). From there it propagates to
the execution *cores* via the *cache*.

Cache  
The cache is physically much closer to the *CPU* than the *memory*.
Therefore, data is moved from the *memory* to the cache before
processing.

|  |
|----|
| **Warning:** The terminology of nodes, cores, CPUs, threads, etc. is not universal. For instance, some refer to a single core as a CPU, others refer to an entire node as a CPU. |

|  |
|----|
| **Tip:** There is a lecture on <a href="https://youtu.be/KzIuL_e0zz8" class="external text"
rel="nofollow">high-performance computing (HPC)</a> in VASP available on our YouTube channel. |

## How to\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

### Optimizing the parallelization\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Optimizing the parallelization">edit</a> \| (./index.php.md)\]

The performance of a specific parallelization depends on the system,
i.e., the number of ions, the elements, the size of the cell, etc.
Different algorithms ([density-functional
theory](Category-Electronic_minimization.md),
[many-body perturbation
theory](Category-Many-body_perturbation_theory.md),
or [molecular
dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics))
require a separate optimization of the parallel setup. To obtain
publishable results, many projects require performing many similar
calculations, i.e., calculations with similar input and using the same
algorithms. Therefore, we recommend optimizing the parallelization to
make the most of the available compute time. This optimization process
depends greatly on the hardware and [compiler
toolchain](../misc/Toolchains.md) on which you run your
calculation. Hence, make sure to verify your setup when switching one of
these.

|  |
|----|
| **Tip:** Run a few test calculations varying the parallel setup and use the optimal choice of parameters for the rest of the calculations. |

For more detailed advice, check the following:

- How to [optimize the
  parallelization](../tutorials/Optimizing_the_parallelization.md)
  in a nutshell

### OpenMP/OpenACC\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: OpenMP/OpenACC">edit</a> \| (./index.php.md)\]

Both [OpenMP](../misc/Combining_MPI_and_OpenMP.md)
and [offloading to GPUs](../misc/GPU_ports_of_VASP.md)
parallelize the FFTs and therefore disregard any conflicting
specification of [NCORE](../incar-tags/NCORE.md). When running any of the
[GPU ports of VASP](../misc/GPU_ports_of_VASP.md), the
offloaded code path takes precedence, but any code not ported to GPU
benefits from the additional OpenMP threads on the CPU. This approach is
relevant because the recommended NVIDIA Collective Communications
Library requires a single MPI rank per GPU (as does RCCL for AMD). Learn
more about the OpenMP and OpenACC parallelization in these sections

- How to [parallelize with multiple OpenMP threads per MPI
  rank](../misc/Combining_MPI_and_OpenMP.md)
- How to [run on GPUs](../misc/GPU_ports_of_VASP.md)

## Additional parallelization options\[<a
href="/wiki/index.php?title=Category:Parallelization&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Additional parallelization options">edit</a> \| (./index.php.md)\]

[KPAR](../incar-tags/KPAR.md)  
For Laplace transformed MP2 this tag [has a different
meaning](../tutorials/LTMP2_-_Tutorial.md).

[NCORE_IN_IMAGE1](../incar-tags/NCORE_IN_IMAGE1.md)  
Defines how many ranks work on the first image in the thermodynamic
coupling constant integration
([VCAIMAGES](../incar-tags/VCAIMAGES.md)).

[NOMEGAPAR](../incar-tags/NOMEGAPAR.md)  
Parallelize over imaginary frequency points in
$GW$ and RPA calculations.

[NTAUPAR](../incar-tags/NTAUPAR.md)  
Parallelize over imaginary time points in $GW$ and RPA
calculations.



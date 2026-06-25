<!-- Source: https://vasp.at/wiki/index.php/Precompiler_options | revid: 35707 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Precompiler options


Precompiler flags are used to activate/deactivate certain code features
at the time of compilation, e.g., the use of MPI, the advanced molecular
dynamics features, etc. Many precompiler flags are set by default in the
[templates provided for the makefile.include
file](Makefile.include.md). The
commands are as follows:

CPP  
The command to invoke the precompiler you want to use, for instance:

- Using Intel's Fortran precompiler:

    CPP=fpp -f_com=no -free -w0 $*$(FUFFIX) $*$(SUFFIX) $(CPP_OPTIONS)

- Using cpp:

<!-- -->

    CPP=/usr/bin/cpp -P -C -traditional $*$(FUFFIX) >$*$(SUFFIX) $(CPP_OPTIONS)

|  |
|----|
| **Mind:** This variable has to include `$(CPP_OPTIONS)`. If not, `CPP_OPTIONS` will be ignored! |

CPP_OPTIONS  
Specify the precompiler flags:

<!-- -->

    CPP_OPTIONS=[-Dflag1 [-Dflag2] ... ]

|  |
|----|
| **Mind:** `CPP_OPTIONS` is only used in [makefile.include](Makefile.include.md), where it is added to the `CPP` variable. |


## Contents


- [1
  Default](#Default)
  - [1.1
    -DHOST=\[string\]](#-DHOST=%5Bstring%5D)
  - [1.2
    -DMPI](#-DMPI)
  - [1.3
    -Duse_collective](#-Duse_collective)
  - [1.4
    -DMPI_BLOCK=\[integer\]](#-DMPI_BLOCK=%5Binteger%5D)
  - [1.5
    -DscaLAPACK](#-DscaLAPACK)
  - [1.6
    -DCACHE_SIZE=\[integer\]](#-DCACHE_SIZE=%5Binteger%5D)
  - [1.7
    -Davoidalloc](#-Davoidalloc)
  - [1.8
    -Dvasp6](#-Dvasp6)
  - [1.9
    -Dtbdyn](#-Dtbdyn)
  - [1.10
    -Dfock_dblbuf](#-Dfock_dblbuf)
  - [1.11
    -D_OPENMP](#-D_OPENMP)
- [2 Specific for
  the OpenACC port to NVIDIA
  GPUs](#Specific_for_the_OpenACC_port_to_NVIDIA_GPUs)
  - [2.1
    -DACC_OFFLOAD](#-DACC_OFFLOAD)
  - [2.2
    -DNVCUDA](#-DNVCUDA)
  - [2.3
    -DUSENCCL](#-DUSENCCL)
  - [2.4
    -Dqd_emulate](#-Dqd_emulate)
  - [2.5
    -DCRAY_MPICH](#-DCRAY_MPICH)
- [3 Specific for
  the OpenMP port to AMD and Intel
  GPUs](#Specific_for_the_OpenMP_port_to_AMD_and_Intel_GPUs)
  - [3.1
    -DOMP_OFFLOAD](#-DOMP_OFFLOAD)
  - [3.2
    -D_OPENMP](#-D_OPENMP_2)
  - [3.3
    -DINTELMKL](#-DINTELMKL)
  - [3.4
    -DCRAYHIP](#-DCRAYHIP)
  - [3.5
    -DUSENCCL](#-DUSENCCL_2)
- [4
  Optional](#Optional)
  - [4.1
    -DVASP_HDF5](#-DVASP_HDF5)
  - [4.2
    -Duse_shmem](#-Duse_shmem)
  - [4.3
    -Dshmem_bcast_buffer](#-Dshmem_bcast_buffer)
  - [4.4
    -Dshmem_rproj](#-Dshmem_rproj)
  - [4.5
    -Dsysv](#-Dsysv)
  - [4.6
    -DVASP2WANNIER90](#-DVASP2WANNIER90)
  - [4.7
    -Dlibbeef](#-Dlibbeef)
  - [4.8
    -DDFTD4](#-DDFTD4)
  - [4.9
    -DDFTD4_API_V3](#-DDFTD4_API_V3)
  - [4.10
    -DSDFTD3](#-DSDFTD3)
  - [4.11
    -DLIBMBD](#-DLIBMBD)
  - [4.12
    -DSCPC](#-DSCPC)
  - [4.13
    -DPROFILING](#-DPROFILING)
  - [4.14
    -DUSELIBXC](#-DUSELIBXC)
  - [4.15
    -DELPA](#-DELPA)
  - [4.16
    -DLAPACK36](#-DLAPACK36)
- [5 Specific to
  the experimental VASPml
  library](#Specific_to_the_experimental_VASPml_library)
  - [5.1
    -Dlibvaspml](#-Dlibvaspml)
  - [5.2
    -DVASPML_ENABLE_GRACE](#-DVASPML_ENABLE_GRACE)
  - [5.3
    -DVASPML_USE_MKL /
    -DVASPML_NO_MKL](#-DVASPML_USE_MKL_/_-DVASPML_NO_MKL)
  - [5.4
    -DVASPML_DEBUG_LEVEL=\[0\|1\|2\|3\]](#-DVASPML_DEBUG_LEVEL=%5B0%7C1%7C2%7C3%5D)
  - [5.5
    -DVASPML_USE_CBLAS](#-DVASPML_USE_CBLAS)
- [6
  Deprecated](#Deprecated)
  - [6.1
    -D_OPENACC](#-D_OPENACC)
  - [6.2
    -DUSENCCLP2P](#-DUSENCCLP2P)
  - [6.3
    -DnoAugXCmeta](#-DnoAugXCmeta)
  - [6.4
    -DVASP2WANNIER90 and
    -DVASP2WANNIER90v2](#-DVASP2WANNIER90_and_-DVASP2WANNIER90v2)
- [7 Related
  articles](#Related_articles)


## Default\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Default">edit</a> \| (./index.php.md)\]

### -DHOST=\[string\]\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: -DHOST=[string]">edit</a> \| (./index.php.md)\]

A string (20 characters max.) that describes the platform on which VASP
is compiled, e.g., ` -DHOST=\"LinuxIFC\"` for a Linux host using an
Intel Fortran compiler.

### -DMPI\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: -DMPI">edit</a> \| (./index.php.md)\]

(Mandatory) Set this to compile the parallel version of VASP.

### -Duse_collective\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: -Duse_collective">edit</a> \| (./index.php.md)\]

Set this to use MPI collectives in the all-to-all communication and
global summations.

In case one specifies this, the value of MPI_BLOCK (below) will be
meaningless.

### -DMPI_BLOCK=\[integer\]\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: -DMPI_BLOCK=[integer]">edit</a> \| (./index.php.md)\]

Specifies the block size used by the in-house MPI all-to-all
communication and global summations.

### -DscaLAPACK\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: -DscaLAPACK">edit</a> \| (./index.php.md)\]

Set this to use scaLAPACK.

### -DCACHE_SIZE=\[integer\]\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: -DCACHE_SIZE=[integer]">edit</a> \| (./index.php.md)\]

Specifies the size of the cache memory. Only used by the in-house
real-to-complex FFT routines (fft3dlib.F).

By default these are no longer used, instead we use the real-to-complex
FFT routines from fftw3.

### -Davoidalloc\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: -Davoidalloc">edit</a> \| (./index.php.md)\]

Set this to use automatic instead of allocatable arrays in many routines
related to the real space projection operators. This option is by
default set in all our provided makefiles, and is highly suggested to
enable this option.

### -Dvasp6\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: -Dvasp6">edit</a> \| (./index.php.md)\]

Set this to activate all VASP.6.X.X specific features.

### -Dtbdyn\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: -Dtbdyn">edit</a> \| (./index.php.md)\]

Adds the advanced molecular dynamics routines.

### -Dfock_dblbuf\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: -Dfock_dblbuf">edit</a> \| (./index.php.md)\]

Uses double buffer technique for the computation of exchange potential.
Available as of VASP.6, N/A for the CUDA-C GPU-port.

### -D_OPENMP\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: -D_OPENMP">edit</a> \| (./index.php.md)\]

(Optional ) Switch on [a combination of MPI and OpenMP for the
parallelization](Combining_MPI_and_OpenMP.md).

## Specific for the OpenACC port to NVIDIA GPUs\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Specific for the OpenACC port to NVIDIA GPUs">edit</a> \| (./index.php.md)\]

### -DACC_OFFLOAD\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: -DACC_OFFLOAD">edit</a> \| (./index.php.md)\]

Mandatory for openACC starting from version 6.5.0: Activate all
OpenACC-related code paths.

### -DNVCUDA\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: -DNVCUDA">edit</a> \| (./index.php.md)\]

Mandatory: Activate when compiling the OpenACC offloading with the
Nvidia compiler suite nvhpc (new in VASP version 6.5.0).

### -DUSENCCL\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: -DUSENCCL">edit</a> \| (./index.php.md)\]

Mandatory: Use the NVIDIA Collective Communications Library (NCCL)
instead of MPI for relevant instances of collective reduction operations
(MPI_Allreduce).

### -Dqd_emulate\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: -Dqd_emulate">edit</a> \| (./index.php.md)\]

Mandatory: To compile the OpenACC GPU-port you need either the NVIDIA
HPC-SDK or a recent version (\>= 19.10) of PGI's Compilers & Tools. Both
of these compilers do not natively support quadruple precision and
require the use of the QD library to emulate quadruple precision
arithmetic.

### -DCRAY_MPICH\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: -DCRAY_MPICH">edit</a> \| (./index.php.md)\]

Mandatory for Cray machines: When compiling on a Cray machine, this flag
deactivates a check to determine if the MPI version used is CUDA aware,
which fails for MPICH. If MPICH is not used, this flag should not be
set.

## Specific for the OpenMP port to AMD and Intel GPUs\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: Specific for the OpenMP port to AMD and Intel GPUs">edit</a> \| (./index.php.md)\]

### -DOMP_OFFLOAD\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: -DOMP_OFFLOAD">edit</a> \| (./index.php.md)\]

Mandatory for openMP GPU port: Activate all OpenMP-offload related code
paths.

### -D_OPENMP\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=21"
class="mw-editsection-visualeditor"
title="Edit section: -D_OPENMP">edit</a> \| (./index.php.md)\]

Mandatory for openMP activation on CPU and GPU.

### -DINTELMKL\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=22"
class="mw-editsection-visualeditor"
title="Edit section: -DINTELMKL">edit</a> \| (./index.php.md)\]

Mandatory for Intel GPU offloading using the Intel compiler.

### -DCRAYHIP\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=23"
class="mw-editsection-visualeditor"
title="Edit section: -DCRAYHIP">edit</a> \| (./index.php.md)\]

Mandatory for AMD GPU offloading using the Cray compiler.

### -DUSENCCL\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=24"
class="mw-editsection-visualeditor"
title="Edit section: -DUSENCCL">edit</a> \| (./index.php.md)\]

Recommended for AMD, not supported for Intel GPUs: Use the RocM
Collective Communications Library (RCCL) instead of MPI for relevant
instances of collective reduction operations (MPI_Allreduce).

## Optional\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=25"
class="mw-editsection-visualeditor"
title="Edit section: Optional">edit</a> \| (./index.php.md)\]

### -DVASP_HDF5\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=26"
class="mw-editsection-visualeditor"
title="Edit section: -DVASP_HDF5">edit</a> \| (./index.php.md)\]

(Strongly recommended) Set this to add [HDF5
support](../categories/Category-HDF5_support.md). This
option has been available since VASP 6.2.0.

**N.B.**: one needs to [add HDF5 to
makefile.include](Makefile.include.md).

### -Duse_shmem\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=27"
class="mw-editsection-visualeditor"
title="Edit section: -Duse_shmem">edit</a> \| (./index.php.md)\]

Use [shared-memory](../methods/Shared_memory.md) segments to
reduce the memory demands of [GW (ALGO = EVGW0, EVGW, QPGW0, and
QPGW)](../incar-tags/ALGO.md) and
[machine-learned–force-field](../methods/Machine_learning_force_field_calculations-_Basics.md)
calculations.

### -Dshmem_bcast_buffer\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=28"
class="mw-editsection-visualeditor"
title="Edit section: -Dshmem_bcast_buffer">edit</a> \| (./index.php.md)\]

Use [shared-memory](../methods/Shared_memory.md) segments to
reduce the amount of MPI communication in hybrid-functional
calculations.

### -Dshmem_rproj\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=29"
class="mw-editsection-visualeditor"
title="Edit section: -Dshmem_rproj">edit</a> \| (./index.php.md)\]

Use [shared-memory](../methods/Shared_memory.md) segments to
reduce the storage demands of the [real-space PAW
projectors](../incar-tags/LREAL.md).

### -Dsysv\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=30"
class="mw-editsection-visualeditor"
title="Edit section: -Dsysv">edit</a> \| (./index.php.md)\]

Use `ipcs` [shared-memory](../methods/Shared_memory.md) segments
and `system-V` semaphores.

### -DVASP2WANNIER90\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=31"
class="mw-editsection-visualeditor"
title="Edit section: -DVASP2WANNIER90">edit</a> \| (./index.php.md)\]

Set this to include the interface between VASP and Wannier90.

|  |
|----|
| **Deprecated:** For VASP\<6.2.0, see [-DVASP2WANNIER90 and -DVASP2WANNIER90v2](#-DVASP2WANNIER90_and_-DVASP2WANNIER90v2) in the deprecated section below! |

### -Dlibbeef\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=32"
class="mw-editsection-visualeditor"
title="Edit section: -Dlibbeef">edit</a> \| (./index.php.md)\]

Set this to include the GGA BEEF functional (corresponds to
[GGA](../incar-tags/GGA.md)=BF).

**N.B.**: one needs to [add libbeef to
makefile.include](Makefile.include.md).

|  |
|----|
| **Mind:** LibBEEF is **not** supported in any of the [GPU ports of VASP](GPU_ports_of_VASP.md). |

### -DDFTD4\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=33"
class="mw-editsection-visualeditor"
title="Edit section: -DDFTD4">edit</a> \| (./index.php.md)\]

Set this to link to the package of van der Waals
[DFT-D4](../methods/DFT-D4.md) methods.

**Note** that you need to [install DFT-D4 and add it to the
makefile.include](Makefile.include.md).

### -DDFTD4_API_V3\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=34"
class="mw-editsection-visualeditor"
title="Edit section: -DDFTD4_API_V3">edit</a> \| (./index.php.md)\]

Set this to link to version 3.7.0 (or older) of the
[DFT-D4](../methods/DFT-D4.md) package when using VASP.6.6.0 or newer
versions.

**Note** that you need to [install DFT-D4 and add it to the
makefile.include](Makefile.include.md).

### -DSDFTD3\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=35"
class="mw-editsection-visualeditor"
title="Edit section: -DSDFTD3">edit</a> \| (./index.php.md)\]

Set this to link to the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package of van der
Waals DFT-D3 methods.

**Note** that you need to [install simple-DFT-D3 and add it to the
makefile.include](Makefile.include.md).

### -DLIBMBD\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=36"
class="mw-editsection-visualeditor"
title="Edit section: -DLIBMBD">edit</a> \| (./index.php.md)\]

Set this to include the library libMBD of many-body dispersion (MBD)
methods for van der Waals interactions.

**Note** that you need to [install LibMBD and add it to the
makefile.include](Makefile.include.md).

### -DSCPC\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=37"
class="mw-editsection-visualeditor"
title="Edit section: -DSCPC">edit</a> \| (./index.php.md)\]

Set this to include the self-consistent potential-correction (SCPC)
method.

**Note** that you need to install SCPC and add it to the
makefile.include.

### -DPROFILING\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=38"
class="mw-editsection-visualeditor"
title="Edit section: -DPROFILING">edit</a> \| (./index.php.md)\]

Switches on detailed profiling of the code. This carries a (slight)
performance penalty.

### -DUSELIBXC\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=39"
class="mw-editsection-visualeditor"
title="Edit section: -DUSELIBXC">edit</a> \| (./index.php.md)\]

Set this to include the library of exchange-correlation functionals
Libxc.

**Note** that you need to install Libxc \>= 5.2.0 (or the master version
from <a href="https://gitlab.com/libxc/libxc" class="external text"
rel="nofollow">gitlab</a> for the latest implemented functionals) with
the option `--disable-fhc` and [add this to the
makefile.include](Makefile.include.md).

|  |
|----|
| **Mind:** LibXC is **not** supported in any of the [GPU ports of VASP](GPU_ports_of_VASP.md). |

### -DELPA\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=40"
class="mw-editsection-visualeditor"
title="Edit section: -DELPA">edit</a> \| (./index.php.md)\]

Set this to include the library of ELPA eigenvalue solvers.

**N.B.**: one needs to [add ELPA to
makefile.include](Makefile.include.md).

### -DLAPACK36\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=41"
class="mw-editsection-visualeditor"
title="Edit section: -DLAPACK36">edit</a> \| (./index.php.md)\]

Required for <a href="http://www.netlib.org/lapack/lapack-3.6.0.html"
class="external text" rel="nofollow"><code>LAPACK-3.6.0</code></a> and
newer to replaced deprecated routine `DGEGV` by `DGGEV`.

## Specific to the experimental VASPml library\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=42"
class="mw-editsection-visualeditor"
title="Edit section: Specific to the experimental VASPml library">edit</a> \| (./index.php.md)\]

### -Dlibvaspml\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=43"
class="mw-editsection-visualeditor"
title="Edit section: -Dlibvaspml">edit</a> \| (./index.php.md)\]

Set this to automatically compile and link the [VASPml
library](../methods/VASPml_library.md) together with VASP.
Without `-Dlibvaspml` the remaining options in this section are ignored.

### -DVASPML_ENABLE_GRACE\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=44"
class="mw-editsection-visualeditor"
title="Edit section: -DVASPML_ENABLE_GRACE">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Mind:** This option is available as of VASP 6.6.0 |

Set this to enable support for [GRACE machine-learned force fields
inside
VASP](../methods/Running_GRACE_force_fields_in_VASP.md).

### -DVASPML_USE_MKL / -DVASPML_NO_MKL\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=45"
class="mw-editsection-visualeditor"
title="Edit section: -DVASPML_USE_MKL / -DVASPML_NO_MKL">edit</a> \| (./index.php.md)\]

This options enforces (`.._USE_..`) or prevents (`.._NO_..`) the use of
Intel's MKL library inside the VASPml library. As of VASP 6.6.0 the
default behavior is that `-DVASPML_USE_MKL` is automatically assumed if
an Intel compiler (`icpc, icpx`) is used. On the other hand, for any
other compiler MKL will not be used by default (`-DVASPML_NO_MKL` is
implied). Hence, these options are required only for builds which
reverse this logic, e.g.,

- to link a GCC compiler build to MKL, add `-DVASPML_USE_MKL`, or,
- to avoid the MKL library for an Intel build, add `-DVASPML_NO_MKL`.

|  |
|----|
| **Deprecated:** Earlier versions of VASP (6.5.X) do not provide this automatism and the `-DVASPML_NO_MKL` is not available. There, the `-DVASPML_USE_MKL` option is mandatory even if an Intel compiler is used to build the VASPml library. |

### -DVASPML_DEBUG_LEVEL=\[0\|1\|2\|3\]\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=46"
class="mw-editsection-visualeditor"
title="Edit section: -DVASPML_DEBUG_LEVEL=[0|1|2|3]">edit</a> \| (./index.php.md)\]

If set to 1, 2 or 3 enables various sanity checks during runtime with
low, medium and high impact on performance, respectively. Setting it to
0 or omitting the flag disables runtime checks.

|  |
|----|
| **Mind:** Do not use this flag for production runs as it may decrease performance. |

### -DVASPML_USE_CBLAS\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=47"
class="mw-editsection-visualeditor"
title="Edit section: -DVASPML_USE_CBLAS">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Deprecated:** This option is only required for VASP 6.5.X and is automatically implied for newer verions. |

Set this to use CBLAS (C interface for BLAS routines) for linear algebra
inside the VASPml library.

## Deprecated\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=48"
class="mw-editsection-visualeditor"
title="Edit section: Deprecated">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Deprecated:** `-DNGZhalf`, `-DwNGZhalf`, `-DNGXhalf`, `-DwNGXhalf` are deprecated options. Building the standard, gamma-only, or non-collinear version of the code is specified through an additional argument to the make command as discussed in [Installing VASP.6.X.X](Installing_VASP.6.X.X.md). |

### -D_OPENACC\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=49"
class="mw-editsection-visualeditor"
title="Edit section: -D_OPENACC">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Deprecated:** This precompiler flag has been deprecated since version 6.5.0. It has been replaced by -DACC_OFFLOAD |

Mandatory for openACC before version 6.5.0: Activate all OpenACC-related
code paths.

### -DUSENCCLP2P\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=50"
class="mw-editsection-visualeditor"
title="Edit section: -DUSENCCLP2P">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Deprecated:** This precompiler flag has been deprecated since version 6.4.0. |

Optional but strongly recommended for VASP versions \< 6.4.0; (requires
NCCL \>= 2.7.8): Use the NVIDIA Collective Communications Library (NCCL)
instead of MPI for relevant instances of all-to-all operations
(MPI_Alltoallv).

### -DnoAugXCmeta\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=51"
class="mw-editsection-visualeditor"
title="Edit section: -DnoAugXCmeta">edit</a> \| (./index.php.md)\]

This option was added to compute the meta-GGA contributions from the
non-augmented pseudo density (instead of the augmented density). There
is a condition concerning the behavior of the von-Weizsäcker kinetic
energy density (calculated using the first derivative of the charge
density) and the kinetic energy density computed from the orbitals
ingrained into TPSS and revTPSS. This condition can be strongly violated
when one augments the charge density. For the TPSS and revTPSS the
functionals can become unstable in those cases. SCAN and its derivates
(RSCAN, R2SCAN, etc) do not assume the aforementioned conditions to be
met and remain stable for the augmented density as well so this option
should not be used as it may negatively affect the final results.

### -DVASP2WANNIER90 and -DVASP2WANNIER90v2\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=52"
class="mw-editsection-visualeditor"
title="Edit section: -DVASP2WANNIER90 and -DVASP2WANNIER90v2">edit</a> \| (./index.php.md)\]

Set this to include the interface between VASP and Wannier90.

Up to VASP 6.1.x you need to set -DVASP2WANNIER90 to interface with
Wannier90 v.1.x, and -DVASP2WANNIER90v2 for Wannier90 v.2.x, and add the
Wannier90 library to
[makefile.include](Makefile.include.md).

Since VASP 6.2.0 you need to set -DVASP2WANNIER90 to interface with
Wannier90 v.2.x or v.3.x.

## Related articles\[<a
href="/wiki/index.php?title=Precompiler_options&amp;veaction=edit&amp;section=53"
class="mw-editsection-visualeditor"
title="Edit section: Related articles">edit</a> \| (./index.php.md)\]

[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md),
[makefile.include](Makefile.include.md), [Compiler
options](Compiler_options.md), [Linking to
libraries](Linking_to_libraries.md), [GPU
ports of VASP](GPU_ports_of_VASP.md),
[Toolchains](Toolchains.md), [Validation
tests](Validation_tests.md), [VASPml
library](../methods/VASPml_library.md), [Known
issues](Known_issues.md)

------------------------------------------------------------------------



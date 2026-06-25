<!-- Source: https://vasp.at/wiki/index.php/GPU_ports_of_VASP | revid: 35713 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GPU ports of VASP


VASP offers two different GPU ports. An OpenACC port targeting NVIDIA
GPUs, and an OpenMP offloading port for AMD and Intel GPUs.

<u>*NVIDIA*</u>

With VASP.6.2.0 we officially released the OpenACC GPU-port of VASP for
NVIDIA GPUs: Official in the sense that we now strongly recommend using
this OpenACC version to run VASP on NVIDIA GPU-accelerated systems.

The previous [CUDA-C GPU-port of
VASP](CUDA-C_GPU_port_of_VASP.md) is
considered to be deprecated and is no longer actively developed,
maintained, or supported. As of VASP.6.3.0, the CUDA-C GPU-port of VASP
has been dropped completely.

<u>*AMD and Intel*</u>

With VASP.6.6.0 we released an experimental OpenMP GPU-port of VASP,
targeting AMD and Intel datacenter GPUs. Experimental in the sense that
we have not fully documented the port. We have thoroughly tested the
port on several HPC clusters, but without some adoption by the user base
and the port being tested in real scientific workloads, we expect some
bugs to remain in edge case problems. The OpenMP offload GPU-port is
based on the well-tested and widely adopted port for NVIDIA GPUs, but a
substantial amount of code has been optimized for the specific vendors.


## Contents


- [1
  Requirements](#requirements)
  - [1.1 Software
    stacks](#software-stacks)
    - [1.1.1 NVIDIA
      GPUs](#nvidia-gpus)
    - [1.1.2 AMD
      GPUs](#amd-gpus)
    - [1.1.3 Intel
      GPUs](#intel-gpus)
  - [1.2
    Hardware](#hardware)
    - [1.2.1 NVIDIA
      GPUs](#nvidia-gpus-1)
    - [1.2.2 AMD
      GPUs](#amd-gpus-1)
    - [1.2.3 Intel
      GPUs](#intel-gpus-1)
- [2
  Building](#building)
- [3 Features and
  limitations](#features-and-limitations)
- [4 Running the
  GPU versions](#running-the-gpu-versions)
  - [4.1
    Environment
    variables](#environment-variables)
    - [4.1.1
      MPI](#mpi)
    - [4.1.2 OpenMP
      Offloading](#openmp-offloading)
      - [4.1.2.1
        AMD](#amd)
      - [4.1.2.2
        Intel](#intel)
- [5
  Credits](#credits)
- [6 Related
  articles](#related-articles)
- [7
  References](#references)


## Requirements\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Requirements">edit</a> \| (./index.php.md)\]

### Software stacks\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Software stacks">edit</a> \| (./index.php.md)\]

#### NVIDIA GPUs\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: NVIDIA GPUs">edit</a> \| (./index.php.md)\]

<u>*Compiler*</u>

- To compile the OpenACC version of VASP you need a recent version of
  the
  <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
  rel="nofollow">NVIDIA HPC-SDK</a> (\>=21.2).

In principle, any compiler that supports at least OpenACC standard 2.6
should do the trick, but we have only tried and tested the
aforementioned ones.

|  |
|----|
| **Warning:** the NVIDIA HPC-SDK versions 22.1 and 22.2 have a serious bug that prohibits the execution of the OpenACC version in conjunction with OpenMP-threading. When using these compiler versions you should compile without OpenMP support. This bug is fixed as of NVIDIA HPC-SDK version 22.3. |

<u>*Libraries*</u>

- Numerical libraries: FFTW, BLAS, LAPACK, and scaLAPACK. In case you
  are using the
  <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
  rel="nofollow">NVIDIA HPC-SDK</a> the only numerical library you will
  have to install yourself is
  <a href="http://www.fftw.org" class="external text"
  rel="nofollow">FFTW</a>. The latter three (BLAS, LAPACK, and
  scaLAPACK) are shipped with the SDK. Alternatively, you can link
  against an installation of <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html"
  class="external text" rel="nofollow">Intel's oneAPI MKL</a> library
  that provides all four.
- <a href="https://developer.nvidia.com/cuda-toolkit"
  class="external text" rel="nofollow">The NVIDIA CUDA Toolkit</a>
  (\>=10.0). All necessary CUDA Toolkit components are shipped as part
  of the NVIDIA HPC-SDK.
- A CUDA-aware version of MPI. The OpenMPI installations that are
  packaged with the NVIDIA HPC-SDK are CUDA-aware. MPICH will also work
  on Cray machines, but the precompiler flag
  [-DCRAY_MPICH](Precompiler_options.md)
  has to be added to the
  [makefile.include](Makefile.include.md).
- <a href="https://developer.nvidia.com/nccl" class="external text"
  rel="nofollow">The NVIDIA Collective Communications Library (NCCL)</a>
  (\>=2.7.8). This library is not a strict requirement but its use is
  highly recommended for performance reasons. Suitable installations of
  NCCL are shipped as part of the NVIDIA HPC-SDK.

<u>*Drivers*</u>

- You need a CUDA driver that supports at least CUDA-10.0. Note that you
  have to adapt the
  [makefile.include](Makefile.include.md) for your
  specific CUDA version. You can query it, e.g., by `nvcc --version`.
- You will also need to specify for which GPU architectures you want to
  generate device code for in the
  [makefile.include](Makefile.include.md). Consult
  the <a href="https://developer.nvidia.com/cuda/gpus%7C"
  class="external text" rel="nofollow">CUDA GPU Compute Capability</a>
  chart to select the compute capabilities (cc), e.g., `cc80,cc89` for
  compute capability 8.0 (A series datacenter GPUs) and 8.9 (RTX Ada
  series workstation GPUs). Selecting more compute capabilities will
  make your executable more portable, but will increase compile time. If
  you are compiling on a compute node directly, you can also use
  `ccnative`.

#### AMD GPUs\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: AMD GPUs">edit</a> \| (./index.php.md)\]

<u>*Compiler*</u>

- To compile the OpenMP offload version of VASP for AMD GPUs, the
  <a href="https://cpe.ext.hpe.com/docs/25.03/cce/index.html"
  class="external text" rel="nofollow">HPE Cray compiler environment</a>
  (CCE \>= 19.0) is needed. This compiler is only available on HPE HPC
  clusters and cannot be obtained as a stand-alone product.
  <sup>[\[1\]](#cite_note-1)</sup>

<u>*Libraries*</u>

- Numerical libraries: FFTW, BLAS, LAPACK, and scaLAPACK. These are all
  provided via
  <a href="https://www.amd.com/en/products/software/rocm/hpc.html"
  class="external text" rel="nofollow">AMDs ROCm</a> software stack,
  which includes hipFFT, hipBLAS, hipSolver, and more. We have tested
  ROCm versions 6.1, 6.3, and 6.4.

|  |
|----|
| **Important:** We have seen dramatically improved performance in LAPACK and BLAS calls for ROCm versions 6.3 and 6.4 compared to earlier versions. For good performance, the latest ROCm install available in the CCE is highly recommended. |

- A HIP-aware version of MPI. On CCE, this will be
  <a href="https://www.mpich.org/" class="external text"
  rel="nofollow">MPICH</a> (\>=4).
- <a href="https://rocm.docs.amd.com/projects/rccl/en/latest/"
  class="external text" rel="nofollow">The ROCm Communication Collectives
  Library (RCCL)</a>. This library is not a strict requirement, but its
  use is highly recommended for performance reasons. Suitable
  installations of RCCL are shipped as part of ROCm.

<u>*Drivers*</u>

- GPU drivers for AMD datacenter GPUs are baked into the OS on HPC
  machines. The HIP-runtime and other parts of the user-space compute
  layer are shipped with ROCm. If you need to install your own drivers
  please follow the official <a
  href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#"
  class="external text" rel="nofollow">guide from AMD</a>.

#### Intel GPUs\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Intel GPUs">edit</a> \| (./index.php.md)\]

<u>*Compiler*</u>

- To compile the OpenMP offload version of VASP for AMD GPUS, the <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler.html"
  class="external text" rel="nofollow">Intel Fortran Compiler IFX</a>
  (\>=2025.3.0) is needed. It is distributed via the <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit.html"
  class="external text" rel="nofollow">oneAPI HPC Toolkit</a>.

|  |
|----|
| **Warning:** Older versions of the compiler might compile the code, but will lead to slow execution and/or wrong results at runtime. Thus, version 2025.3.0 or higher is a strict requirement! |

<u>*Libraries*</u>

- Numerical libraries: FFTW, BLAS, LAPACK, and scaLAPACK. These are
  provided via the <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html"
  class="external text" rel="nofollow">Intel Math Kernel Library
  (oneMKL)</a>, which is distributed in the <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html"
  class="external text" rel="nofollow">oneAPI Base Toolkit</a>, and the
  <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit.html"
  class="external text" rel="nofollow">oneAPI HPC Toolkit</a>.
- A GPU-enabled version of MPI. We have both tested <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html"
  class="external text" rel="nofollow">Intel-MPI</a>, as distributed via
  the <a
  href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit.html"
  class="external text" rel="nofollow">oneAPI HPC Toolkit</a> and
  <a href="https://www.mpich.org/" class="external text"
  rel="nofollow">MPICH</a> successfully.

<u>*Drivers*</u>

- GPU drivers for Intel datacenter GPUs are baked into the OS on HPC
  machines. We recommend using whatever your HPC center provides. If
  this is not possible or you want to install you own drivers, please
  follow the official <a
  href="https://dgpu-docs.osgc.infra-host.com/driver/installation-lts2.html#installing-gpu-drivers"
  class="external text" rel="nofollow">Intel guide</a> and make sure
  that your OS is supported.

### Hardware\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Hardware">edit</a> \| (./index.php.md)\]

#### NVIDIA GPUs\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: NVIDIA GPUs">edit</a> \| (./index.php.md)\]

We have only tested the OpenACC GPU-port of VASP with the following
NVIDIA GPUs:

- NVIDIA datacenter GPUs: P100 (Pascal), V100 (Volta), A30 & A100
  (Ampere), and H100 (Hopper).
- NVIDIA Quadro GPUs: GP100 (Pascal), and GV100 (Volta).

|  |
|----|
| **Important:** Running VASP on other NVIDIA GPUs (e.g., "gaming" hardware) is technically possible but not advisable: these GPUs are not well suited since they do not offer fast double-precision floating-point arithmetic (FP64) performance and in general have smaller memories without error correction code (ECC) capabilities. |

#### AMD GPUs\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: AMD GPUs">edit</a> \| (./index.php.md)\]

We have only tested the OpenMP offloading GPU-port of VASP with the
following AMD datacenter GPUs:

- AMD Instinct MI210 & MI250x (CDNA 2), and MI300A (CDNA 3).

|  |
|----|
| **Important:** Running VASP on other AMD GPUs (e.g., Radeon PRO workstation cards, or "gaming" hardware) has not been tested at all to date |

#### Intel GPUs\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Intel GPUs">edit</a> \| (./index.php.md)\]

We have only tested the OpenMP offloading GPU-port of VASP with the
following Intel datacenter GPUs:

- Intel Max 1100 and Intel Max 1150 (Ponte Veccio).

|  |
|----|
| **Important:** Running VASP on other Intel GPUs (e.g., Intel Flex datacenter GPUs, Arc PRO workstation cards, or Arc "gaming" hardware) has not been tested at all to date |

## Building\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Building">edit</a> \| (./index.php.md)\]

To build any GPU port of VASP it is best to base your `makefile.include`
file on one of the [archetypical
templates](Makefile.include.md) and adapt these to
the particulars of your system.

- For NVIDIA GPUs start from either `makefile.include.nvhpc_acc`,
  `makefile.include.nvhpc_omp_acc`, or
  `makefile.include.nvhpc_ompi_mkl_omp_acc`.
- For AMD GPUs start from `makefile.include.cray_omp_off`.
- For Intel GPUs start from `makefile.include.oneapi_omp_off`.

## Features and limitations\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Features and limitations">edit</a> \| (./index.php.md)\]

- Most features of VASP have been ported to GPU using OpenACC (NVIDIA),
  with the notable exception of everything involving the RPA: GW and
  ACFDT. This is work in progress. For the OpenMP offloading port (AMD &
  Intel), a few more features, e.g., [linear
  response](../categories/Category-Linear_response.md)
  and
  [BSE](../tutorials/Bethe-Salpeter-equations_calculations.md),
  are still missing.

|  |
|----|
| **Mind:** Unported features can still be used in the GPU build. They will just not run on the GPU, but on the host CPU. |

- The use of parallel FFTs of the wave functions
  ([NCORE](../incar-tags/NCORE.md)\>1) should be avoided for performance
  reasons. Currently, all GPU versions will automatically switch to
  [NCORE](../incar-tags/NCORE.md)=1 even if otherwise specified in the
  [INCAR](../input-files/INCAR.md) file.

<!-- -->

- **The GPU versions of VASP may only be executed using a single
  MPI-rank per available GPU:**

Using NCCL/RCCL has large performance benefits in the majority of cases,
but it limits the number of ranks to one per device.

|  |
|----|
| **Mind:** Some GPUs (e.g., AMD Mi250, Intel Max 1150) have 2 tiles or GCDs per physical device. Both those tiles will count as a separate GPU for this purpose, and VASP will allow, e.g., 8 ranks to run on 4 Mi250 GPUs, with a total of 8 GCDs. |

## Running the GPU versions\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Running the GPU versions">edit</a> \| (./index.php.md)\]

1.  Use a single MPI rank per GPU.
2.  Use OpenMP threads in addition to MPI ranks to leverage more of the
    available CPU power. The GPU versions are currently limited to the
    use of 1 MPI-rank/GPU, which means that potentially quite a bit of
    CPU power remains unused. Since there are still parts of the code
    that run CPU-side it can be beneficial to allow for the use of
    multiple OpenMP threads per MPI rank:
    - The OpenMP offloading GPU port requires compilation with OpenMP
      and can use OpenMP on the CPU in those sections of the code that
      are not ported to GPU.
    - To see how to build VASP with OpenACC- *and* OpenMP-CPU-support
      have a look at the
      [makefile.include.nvhpc_ompi_mkl_omp_acc](Makefile.include.nvhpc_ompi_mkl_omp_acc.md)
      file.

    <table class="vasp-dark-link-panel"
    style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><strong><span
    style="color: var(--vpurple);">Important:</span></strong> Here we link
    against Intel's MKL library for CPU-sided FFTW, BLAS, LAPACK, and
    scaLAPACK calls and the Intel OpenMP runtime library
    (<code>libiomp5.so</code>). This is strongly recommended when compiling
    for Intel CPUs, especially when using multiple threads. To ensure that
    MKL uses the Intel OpenMP runtime library you need to set an environment
    variable, either by:
    <pre><code>export MKL_THREADING_LAYER=INTEL</code></pre>
    or by adding:
    <pre><code>-x MKL_THREADING_LAYER=INTEL</code></pre>
    as an option to your <code>mpirun</code> command.</td>
    </tr>
    </tbody>
    </table>

    - Correct [placement and pinning of OpenMPI ranks and OpenMP threads
      onto the CPU
      cores](Combining_MPI_and_OpenMP.md)
      can be a bit tricky, and depends on the particular flavor of MPI
      one uses.
3.  To achieve the best performance, it is important to choose
    [KPAR](../incar-tags/KPAR.md) and [NSIM](../incar-tags/NSIM.md) wisely.
    Unfortunately, the ideal values will depend on the particulars of
    your system, both in the sense of workload as well as hardware, so
    you will have to experiment with different settings. However, as a
    rule of thumb, one can say:
    - Set [KPAR](../incar-tags/KPAR.md) to the number of GPUs (= MPI-ranks)
      you are going to use. This only makes sense, though, when the
      number of irreducible **k**-points in your calculation is more or
      less evenly divisible by [KPAR](../incar-tags/KPAR.md), otherwise the
      distribution of the work over the MPI-ranks will be strongly
      imbalanced. This means your options in choosing this parameter are
      somewhat limited.
    - [NSIM](../incar-tags/NSIM.md) determines the number of bands that are
      optimized simultaneously in many of the electronic solvers (e.g
      RMM-DIIS and blocked-Davidson). As a rule, one should choose this
      parameter larger to get good performance on GPUs than one would
      for CPU-based execution.

    |  |
    |----|
    | **Warning:** For optimal CPU-based execution of VASP, one would normally experiment with different settings for [NCORE](../incar-tags/NCORE.md) as well. When running on GPUs, anything different from [NCORE](../incar-tags/NCORE.md)=1 will adversely affect performance, and VASP will automatically switch to [NCORE](../incar-tags/NCORE.md)=1, even if otherwise specified in the [INCAR](../input-files/INCAR.md) file. |

### Environment variables\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Environment variables">edit</a> \| (./index.php.md)\]

#### MPI\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: MPI">edit</a> \| (./index.php.md)\]

In contrast to OpenMPI, MPICH and Intel MPI have environment variables
that can toggle GPU-aware MPI execution. Use the following settings:

- MPICH: `MPICH_GPU_SUPPORT_ENABLED=1`
- Intel MPI: `I_MPI_OFFLOAD=1` must be set to ensure that the GPUs can
  communicate directly.

#### OpenMP Offloading\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: OpenMP Offloading">edit</a> \| (./index.php.md)\]

- For GPU offloading, the OMP_STACKSIZE needs to be large. Set:
  `OMP_STACKSIZE=2048m`
- Both MKL and ROCm can leverage CPU threads in library calls that run
  on the GPU. Make sure you have enough threads (4-8) available.

##### AMD\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: AMD">edit</a> \| (./index.php.md)\]

- The cray compilers uses normal OpenMP threads that are set via:
  `OMP_NUM_THREADS=8`
- By default threads spin at 100% load in the cray omp runtime. You can
  safely disable this to give more headroom to ROCm helper threads by
  setting `export OMP_WAIT_POLICY=PASSIVE`
- Currently VASP 6.6.0 cannot use shared memory as available on MI300A
  cards. Make sure that the feature is disabled at runtime via
  `export HSA_XNACK=0`
- To run on multiple AMD GPUs each MPI rank should only see its own GPU
  via `ROCR_VISIBLE_DEVICES` (will be fixed in future releases). To do
  so write a small wrapper script that is put in front of the VASP
  executable in your SLURM / PBS command:

<table
style="width:100%; table-layout: fixed; border-spacing: 0; padding: 0; margin: 0; background-color: var(--vCB-bg); color: var(--vdefault-text); border-width: 1px; border-style: solid; border-color: var(--vCB-border);">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre
style="margin: 0; padding: 1em; background: none; border: none; white-space: pre; overflow-x: auto; font-family: monospace;"><code>#!/bin/bash
myGPU=${SLURM_LOCALID}
# for PBS use this:
#myGPU=${PMI_RANK}                                                                                 
export ROCR_VISIBLE_DEVICES=${myGPU}
exec $*</code></pre></td>
</tr>
</tbody>
</table>

##### Intel\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Intel">edit</a> \| (./index.php.md)\]

- For Intel MKL, `MKL_NUM_THREADS` might be set. If it is too small, it
  can hurt performance, The savest way is to `unset MKL_NUM_THREADS` so
  that it defaults to `OMP_NUM_THREADS`, and set that.

## Credits\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: Credits">edit</a> \| (./index.php.md)\]

Special thanks go out to:

- Stefan Maintz, Markus Wetzstein, Alexey Romanenko, and Andreas Hehn
  from NVIDIA for all their help in porting VASP to GPU using OpenACC!
- Mahdieh Ghazimirsaeed, Justin Chang, Christopher Kime, and Leopold
  Grinberg from AMD, as well as Pierre Carrier and Luke Roskop from HPE,
  for their help with the OpenMP offload port for AMD GPUs.
- Jeongnim Kim, Tobias Klöffel, Abhinav Gaba, Rakesh Krishnaiyer,
  Patrick Steinbrecher, and Harald Servat from Intel, for their help
  with the OpenMP offload port for Intel GPUs.

## Related articles\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: Related articles">edit</a> \| (./index.php.md)\]

[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md),
[makefile.include](Makefile.include.md), [Compiler
options](Compiler_options.md), [Precompiler
options](Precompiler_options.md), [Linking to
libraries](Linking_to_libraries.md),
[Toolchains](Toolchains.md), [Combining MPI and
OpenMP](Combining_MPI_and_OpenMP.md),
[Validation tests](Validation_tests.md), [Known
issues](Known_issues.md)

------------------------------------------------------------------------

## References\[<a
href="/wiki/index.php?title=GPU_ports_of_VASP&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-1)
    We are working alongside AMD to also
    support <a
    href="https://rocm.blogs.amd.com/ecosystems-and-partners/fortran-journey/README.html"
    class="external text" rel="nofollow">AMDs next-gen Fortran compiler</a>,
    to offer an open-source alternative to CCE, but this effort is still
    in the very early stages.



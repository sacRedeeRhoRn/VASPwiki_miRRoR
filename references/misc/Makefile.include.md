<!-- Source: https://vasp.at/wiki/index.php/Makefile.include | revid: 35708 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include


  
Writing a `makefile.include` file from scratch is not easy, so we
suggest taking one of [archetypical files](#Archetypical_files) that
closely resembles your system as a starting point. It is necessary to
customize it anyways to set appropriate paths etc. Optionally, you can
enable additional features by setting precompiler flags or linking VASP
to other libraries. For instance, we strongly recommend enabling HDF5
support.

|  |
|----|
| **Mind:** Always use `makefile.include` files released together with the version of VASP that you are compiling. Old [archetypical files](#Archetypical_files) may not work for newer releases and vice versa. |


## Contents


- [1 Archetypical
  files](#Archetypical_files)
  - [1.1 Intel
    Composer suite and oneAPI HPC toolkit for CPU and
    GPU](#Intel_Composer_suite_and_oneAPI_HPC_toolkit_for_CPU_and_GPU)
  - [1.2 GNU
    compilers for CPUs](#GNU_compilers_for_CPUs)
  - [1.3 NVIDIA
    HPC-SDK for CPU and GPU](#NVIDIA_HPC-SDK_for_CPU_and_GPU)
  - [1.4 Cray
    compiler environment (CCE) for CPU and
    GPU](#Cray_compiler_environment_(CCE)_for_CPU_and_GPU)
  - [1.5
    Others](#Others)
- [2
  Customize](#Customize)
  - [2.1 HDF5
    support (strongly recommended, and mandatory for some
    features)](#HDF5_support_(strongly_recommended,_and_mandatory_for_some_features))
  - [2.2 fftlib
    (recommended when using
    OpenMP)](#fftlib_(recommended_when_using_OpenMP))
  - [2.3 Wannier90
    (optional)](#Wannier90_(optional))
  - [2.4 Libxc
    (optional)](#Libxc_(optional))
  - [2.5 Libbeef
    (optional)](#Libbeef_(optional))
  - [2.6 DFT-D4 and
    simple-DFT-D3
    (optional)](#DFT-D4_and_simple-DFT-D3_(optional))
  - [2.7 ELPA
    (optional)](#ELPA_(optional))
  - [2.8 libMBD
    (optional)](#libMBD_(optional))
  - [2.9 Plugins
    (optional)](#Plugins_(optional))
  - [2.10 SCPC
    (optional)](#SCPC_(optional))
  - [2.11 VASPml
    (experimental)](#VASPml_(experimental))
    - [2.11.1 GRACE
      support](#GRACE_support)
- [3 Related
  articles](#Related_articles)


## Archetypical files\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Archetypical files">edit</a> \| (./index.php.md)\]

The templates contain information such as [precompiler
options](Precompiler_options.md), [compiler
options](Compiler_options.md), and [how to link
libraries](Linking_to_libraries.md). Choose
the template based on the compiler, parallelization etc. from the list
below and mind the description:

### Intel Composer suite and <a
href="https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html"
class="external text" rel="nofollow">oneAPI HPC toolkit</a> for CPU and GPU\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Intel Composer suite and oneAPI HPC toolkit for CPU and GPU">edit</a> \| (./index.php.md)\]

- [makefile.include.oneapi](Makefile.include.oneapi.md):
  Parallelized using MPI, combined with MKL using the newer IFX
  compiler.
- [makefile.include.oneapi_omp](Makefile.include.oneapi_omp.md):
  Parallelized using MPI + OpenMP, combined with MKL, using the newer
  IFX compiler.
- [makefile.include.oneapi_omp_off](Makefile.include.oneapi_omp_off.md):
  [OpenMP offloading](GPU_ports_of_VASP.md) port
  for Intel datacenter GPUs.
- [makefile.include.intel](Makefile.include.intel.md):
  Parallelized using MPI, combined with MKL, using the older IFC
  compiler.
- [makefile.include.intel_omp](Makefile.include.intel_omp.md):
  Parallelized using MPI + OpenMP, combined with MKL, using the older
  IFC compiler.
- [makefile.include.intel_ompi_mkl_omp](Makefile.include.intel_ompi_mkl_omp.md):
  Parallelized using OpenMPI + OpenMP, combined with MKL, using the
  older IFC compiler.
- [makefile.include.intel_serial](Makefile.include.intel_serial.md):
  Not parallelized, strongly reduced feature-set, i.e., not suitable for
  production.

### GNU compilers for CPUs\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: GNU compilers for CPUs">edit</a> \| (./index.php.md)\]

- [makefile.include.gnu](Makefile.include.gnu.md):
  Parallelized using MPI, Free and Open-Source Software (FOSS) stack.
- [makefile.include.gnu_omp](Makefile.include.gnu_omp.md):
  Parallelized using MPI + OpenMP, FOSS stack.
- [makefile.include.gnu_ompi_mkl_omp](Makefile.include.gnu_ompi_mkl_omp.md):
  Parallelized using OpenMPI + OpenMP, combined with MKL.
- [makefile.include.gnu_ompi_aocl](Makefile.include.gnu_ompi_aocl.md):
  Parallelized using OpenMPI, combined with AMD Optimizing CPU Libraries
  (AOCL).
- [makefile.include.gnu_ompi_aocl_omp](Makefile.include.gnu_ompi_aocl_omp.md):
  Parallelized using OpenMPI + OpenMP, combined with AOCL.

### <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC-SDK</a> for CPU and GPU\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: NVIDIA HPC-SDK for CPU and GPU">edit</a> \| (./index.php.md)\]

- [makefile.include.nvhpc](Makefile.include.nvhpc.md):
  CPU version parallelized using MPI.
- [makefile.include.nvhpc_omp](Makefile.include.nvhpc_omp.md):
  CPU version parallelized using MPI + OpenMP.
- [makefile.include.nvhpc_ompi_mkl_omp](Makefile.include.nvhpc_ompi_mkl_omp.md):
  CPU version parallelized using OpenMPI + OpenMP, combined with MKL.
- [makefile.include.nvhpc_acc](Makefile.include.nvhpc_acc.md):
  Ported to GPUs using
  [OpenACC](GPU_ports_of_VASP.md), parallelized
  using MPI .
- [makefile.include.nvhpc_omp_acc](Makefile.include.nvhpc_omp_acc.md):
  Ported to GPUs using
  [OpenACC](GPU_ports_of_VASP.md), parallelized
  using MPI + OpenMP.
- [makefile.include.nvhpc_ompi_mkl_omp_acc](Makefile.include.nvhpc_ompi_mkl_omp_acc.md):
  Ported to GPUs using
  [OpenACC](GPU_ports_of_VASP.md), parallelized
  using OpenMPI + OpenMP, combined with MKL.

### Cray compiler environment (CCE) for CPU and GPU\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Cray compiler environment (CCE) for CPU and GPU">edit</a> \| (./index.php.md) for CPU and GPU")\]

- [makefile.include.cray](Makefile.include.cray.md):
  Parallelized using MPI for CPU
- [makefile.include.cray_omp](Makefile.include.cray_omp.md):
  Parallelized using MPI + OpenMP for CPU
- [makefile.include.cray_omp_off](Makefile.include.cray_omp_off.md):
  [OpenMP offloading](GPU_ports_of_VASP.md) port
  for AMD datacenter GPUs.

### Others\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Others">edit</a> \| (./index.php.md)\]

- [makefile.include.nec_aurora](Makefile.include.nec_aurora.md)

<!-- -->

- [makefile.include.fujitsu_a64fx](Makefile.include.fujitsu_a64fx.md)
- [makefile.include.fujitsu_a64fx_omp](Makefile.include.fujitsu_a64fx_omp.md)
- [makefile.include.aocc_ompi_aocl](Makefile.include.aocc_ompi_aocl.md)
- [makefile.include.aocc_ompi_aocl_omp](Makefile.include.aocc_ompi_aocl_omp.md)
- [makefile.include.amdflang](Makefile.include.amdflang.md)
- [makefile.include.amdflang_omp](Makefile.include.amdflang_omp.md)

An advanced system administrator might benefit from a more detailed
discussion about the [precompiler
options](Precompiler_options.md), [compiler
options](Compiler_options.md), and [how to link
libraries](Linking_to_libraries.md).

## Customize\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Customize">edit</a> \| (./index.php.md)\]

Open the selected template of the [archetypical
files](#Archetypical_files) and add the required information as
explained in the comments towards the end of the file. Then, add any
optional feature as listed below. For more details see the [list of
precompiler options](Precompiler_options.md).

### HDF5 support (strongly recommended, and mandatory for some features)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: HDF5 support (strongly recommended, and mandatory for some features)">edit</a> \| (./index.php.md)")\]

------------------------------------------------------------------------

The HDF5 library is is needed for reading and writing HDF5 files such as
[vaspin.h5](../input-files/Vaspin.h5.md),
[vaspout.h5](../output-files/Vaspout.h5.md) and
[vaspwave.h5](../output-files/Vaspwave.h5.md). The library is available
for download on the
<a href="https://www.hdfgroup.org/solutions/hdf5/" class="external text"
rel="nofollow">HDF5 official website</a>. To activate [HDF5
support](../categories/Category-HDF5_support.md) add the
following in the VASP `makefile.include`

    CPP_OPTIONS+= -DVASP_HDF5
    HDF5_ROOT  ?= /path/to/your/hdf5/installation
    LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
    INCS       += -I$(HDF5_ROOT)/include

Available for VASP \>= 6.2.0.

|  |
|----|
| **Mind:** If you are statically linking to HDF5, you will need to include: **`-I$(HDF5_ROOT)/mod/static`** after `INCS += -I$(HDF5_ROOT)/include `. |

|  |
|----|
| **Warning:** This is required to perform some features of VASP, e.g. [electron-phonon coupling](../categories/Category-Electron-phonon_interactions.md), and is required for py4vasp. |

### fftlib (recommended when using OpenMP)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: fftlib (recommended when using OpenMP)">edit</a> \| (./index.php.md)")\]

------------------------------------------------------------------------

When you plan to [run VASP on multiple OpenMP
threads](Combining_MPI_and_OpenMP.md) and
you are not using the FFTs from the Intel-MKL library, you should link
against `fftlib` (included in the VASP distribution). To do so,
uncomment the corresponding sections in the [makefile.include.\*\_omp
files](#Archetypical_files). In
[makefile.include.gnu_omp](Makefile.include.gnu_omp.md),
for instance, that would be:

    # For the fftlib library (recommended)
    CPP_OPTIONS+= -Dsysv
    FCL        += fftlib.o
    CXX_FFTLIB  = g++ -fopenmp -std=c++11 -DFFTLIB_THREADSAFE
    INCS_FFTLIB = -I./include -I$(FFTW_ROOT)/include
    LIBS       += fftlib
    LLIBS      += -ldl

### Wannier90 (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Wannier90 (optional)">edit</a> | (./index.php.md)")\]

------------------------------------------------------------------------

To include the Wannier90 program, download the library from
<a href="http://www.wannier.org" class="external text"
rel="nofollow">the source</a> and compile `libwannier.a`.

|  |
|----|
| **Important:** In case of Wannier90 3.x, you should compile a serial version by removing `COMMS=mpi` in the `make.inc` of Wannier90. |

Then, execute `make lib` to build the Wannier90 library. To activate
this feature set the following:

    CPP_OPTIONS    += -DVASP2WANNIER90
    WANNIER90_ROOT ?= /path/to/your/wannier90/installation
    LLIBS          += -L$(WANNIER90_ROOT)/lib -lwannier

|  |
|----|
| **Mind:** VASP version \<= 6.1.x are compatible with Wannier90 \<= 1.2. To interface VASP 6.1.x with Wannier90 2.x, set [-DVASP2WANNIER90v2](Precompiler_options.md) instead. As of VASP 6.2.x only Wannier90 2.x and 3.x are supported. |

### Libxc (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Libxc (optional)">edit</a> \| (./index.php.md)")\]

------------------------------------------------------------------------

To include the Libxc library of exchange-correlation functionals,
install the library from
<a href="https://libxc.gitlab.io/download/" class="external text"
rel="nofollow">the source</a> and install it. Note that to get correct
results with meta-GGA functionals (see discussion at
[LTBOUNDLIBXC](../incar-tags/LTBOUNDLIBXC.md)), it is necessary to
use Libxc from version 5.2.0 onwards (or the master version from
<a href="https://gitlab.com/libxc/libxc" class="external text"
rel="nofollow">gitlab</a> for the latest implemented functionals) and to
compile it with the option `--disable-fhc`. For instance, with GNU
Autotools the steps to compile Libxc are

    autoreconf -i (necessary is the executable configure is not already present)
    ./configure --prefix=PATH/TO/LIBXC --disable-fhc
    make
    make install

Then, add the following in the VASP `makefile.include`

    CPP_OPTIONS += -DUSELIBXC
    LIBXC_ROOT  ?= /path/to/your/libxc/installation
    LLIBS       += -L$(LIBXC_ROOT)/lib -lxcf03 -lxc
    INCS        += -I$(LIBXC_ROOT)/include

### Libbeef (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Libbeef (optional)">edit</a> \| (./index.php.md)")\]

------------------------------------------------------------------------

To include the BEEF van der Waals functionals, install the library from
<a href="https://github.com/vossjo/libbeef" class="external text"
rel="nofollow">the source on GitHub</a> and add the following in the
VASP `makefile.include`

    CPP_OPTIONS  += -Dlibbeef
    LIBBEEF_ROOT ?= /path/to/your/libbeef/installation
    LLIBS        += -L$(LIBBEEF_ROOT)/lib -lbeef

### DFT-D4 and simple-DFT-D3 (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: DFT-D4 and simple-DFT-D3 (optional)">edit</a> | (./index.php.md)")\]

------------------------------------------------------------------------

To link to the [DFT-D4](../methods/DFT-D4.md) and/or
[simple-DFT-D3](../methods/Simple-DFT-D3.md) packages of van der
Waals methods, install

- the modular computation tool chain library (mctc-lib) from
  <a href="https://github.com/grimme-lab/mctc-lib" class="external free"
  rel="nofollow">https://github.com/grimme-lab/mctc-lib</a> (must be
  installed before [DFT-D4](../methods/DFT-D4.md) and
  [simple-DFT-D3](../methods/Simple-DFT-D3.md))
- the [DFT-D4](../methods/DFT-D4.md) package from
  <a href="https://github.com/dftd4/dftd4" class="external free"
  rel="nofollow">https://github.com/dftd4/dftd4</a>, which should in
  principle find the mctc-lib pre-installation
- the [simple-DFT-D3](../methods/Simple-DFT-D3.md) package from
  <a href="https://github.com/dftd3/simple-dftd3" class="external free"
  rel="nofollow">https://github.com/dftd3/simple-dftd3</a>, which should
  in principle find the mctc-lib pre-installation

Then, the VASP `makefile.include` should include the following lines:

    # DFT-D4
    CPP_OPTIONS += -DDFTD4
    DFTD4_ROOT  ?= /path/to/your/dft4/installation
    LLIBS       += -L$(DFTD4_ROOT)/lib64 -ldftd4 -lmulticharge
    INCS        += -I$(DFTD4_ROOT)/include
    # simple-DFT-D3
    CPP_OPTIONS += -DSDFTD3
    SDFTD3_ROOT ?= /path/to/your/simple-dft3/installation
    LLIBS       += -L$(SDFTD3_ROOT)/lib64 -ls-dftd3
    INCS        += -I$(SDFTD3_ROOT)/include
    # mctc-lib
    MCTC_ROOT   ?= /path/to/your/mctc-lib/installation
    LLIBS       += -L$(MCTC_ROOT)/lib64 -lmctc-lib
    INCS        += -I$(MCTC_ROOT)/include

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>The API of DFT-D4 has been modified starting with version 4.0.0. The
adaptation has been made in VASP.6.6.0. Versions of DFT-D4 with the old
API (v3.7.0 and older) can still be compiled with VASP.6.6.0 by using <a
href="/wiki/Precompiler_options#-DDFTD4_API_V3"
title="Precompiler options">-DDFTD4_API_V3</a> instead of <a
href="/wiki/Precompiler_options#-DDFTD4"
title="Precompiler options">-DDFTD4</a>.</li>
<li>The pre-installation of mctc-lib is not strictly required. If it is
not the case, then it will be installed automatically during the
installation of <a href="/wiki/DFT-D4" title="DFT-D4">DFT-D4</a> and <a
href="/wiki/Simple-DFT-D3" title="Simple-DFT-D3">simple-DFT-D3</a>.
However, it is strongly recommended to pre-install mctc-lib, otherwise
problems with the GNU compiler may occur if both <a href="/wiki/DFT-D4"
title="DFT-D4">DFT-D4</a> and <a href="/wiki/Simple-DFT-D3"
title="Simple-DFT-D3">simple-DFT-D3</a> are installed.</li>
</ul></td>
</tr>
</tbody>
</table>

### ELPA (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: ELPA (optional)">edit</a> | (./index.php.md)")\]

------------------------------------------------------------------------

To include the ELPA eigenvalue solvers, install the library from
<a href="https://gitlab.mpcdf.mpg.de/elpa/elpa" class="external text"
rel="nofollow">the source on GitLab</a> and add the following in the
VASP `makefile.include`

    CPP_OPTIONS += -DELPA
    ELPA_ROOT   ?= /path/to/your/elpa/installation
    LLIBS       += -L$(ELPA_ROOT)/lib -lelpa
    INCS        += -I$(ELPA_ROOT)/include/elpa-<version>/elpa
    INCS        += -I$(ELPA_ROOT)/include/elpa-<version>/modules

|  |
|----|
| **Mind:** In the above you need to replace `<version>` by the correct designation of your ELPA version. |

### libMBD (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: libMBD (optional)">edit</a> \| (./index.php.md)")\]

------------------------------------------------------------------------

To include the library libMBD of many-body dispersion methods, install
the library from
<a href="https://github.com/libmbd/libmbd" class="external text"
rel="nofollow">the source on GitHub</a> and add the following in the
VASP `makefile.include`

    CPP_OPTIONS += -DLIBMBD 
    LIBMBD_ROOT ?= /path/to/your/libMBD/installation
    LLIBS       += -L$(LIBMBD_ROOT)/build/src -lmbd
    INCS        += -I$(LIBMBD_ROOT)/build/src/modules/

|  |
|----|
| **Mind:** To run a calculation the path to `libmbd.so` has to be added (either in .bashrc or in the terminal): `LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/your/libMBD/installation/build/src`. Alternatively you need to compile libmbd with `cmake -DBUILD_SHARED_LIBS=OFF` which will produce a static library `libmbd.a` |

|  |
|----|
| **Important:** It is recommended to compile libMBD without ScaLAPACK/MPI using `cmake -DENABLE_SCALAPACK_MPI=OFF`, otherwise nudged elastic bands (NEB) calculations will not run properly and produce wrong results. |

### Plugins (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Plugins (optional)">edit</a> | (./index.php.md)")\]

------------------------------------------------------------------------

Create a new <a
href="https://conda.io/projects/conda/en/latest/user-guide/getting-started.html"
class="external text" rel="nofollow">conda</a> environment. Alternative
environment creation packages should work, but we have not tested them.

       conda create -n vasp_plugin python=3.10

Enter the create `vasp_plugin` conda environment

       conda activate vasp_plugin

Navigate to the `plugins` directory within VASP source code,

       cd </path/to/vasp/source/code>/src/plugins

Install the VASP Python package through
<a href="https://pip.pypa.io/en/stable/installation"
class="external text" rel="nofollow">pip</a>

       pip install .

|  |
|----|
| **Mind:** Make sure to be within the conda environment when you compile VASP. |

Add the following lines to your `makefile.include`

       CPP_OPTIONS+= -DPLUGINS
       LLIBS      += $(shell python3-config --ldflags --embed) -lstdc++
       CXX_FLAGS   = $(shell python3 -m pybind11 --includes) -std=c++11

|  |
|----|
| **Mind:** When running VASP with the Python interface you will need to add the lib directory of your Python to LD_LIBRARY_PATH. You can do this by running `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(python3-config --prefix)/lib` |

### SCPC (optional)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: SCPC (optional)">edit</a> | (./index.php.md)")\]

------------------------------------------------------------------------

The [Self-Consistent Potential
Correction](Self-Consistent_Potential_Correction.md)
(SCPC) method is implemented in VASP version 6.2 and later. A patch to
add SCPC functionality to VASP 5.4.4, along with various bug fixes for
the implementation in VASP 6, can be obtained from the
<a href="https://github.com/aradi/SCPC-Method" class="external text"
rel="nofollow">authors</a>.

To compile the VASP with SCPC support, you need the
<a href="https://bitbucket.org/dlmgteam/dl_mg_code_public/downloads/"
class="external text" rel="nofollow">DL_MG</a> and
<a href="https://code.ornl.gov/reubendb/pspfft" class="external text"
rel="nofollow">PSPFFT</a> libraries to solve the Poisson equations and
handle isolated potentials. After downloading and compiling these
libraries, activate SCPC support during VASP compilation by adding the
following snippet to the end of the `makefile.include` file, adjusting
the paths to match your DL_MG and PSPFFT installation:

     # SCPC METHOD
     CPP_OPTIONS += -DSCPC
     SCPC_LIBEXT  = /scpc/libext 
     DLMGROOT   = $(SCPC_LIBEXT)/dl_mg 
     PSPFFTROOT = $(SCPC_LIBEXT)/pspfft 
     INCS      += -I$(DLMGROOT)/include 
     INCS      += -I$(PSPFFTROOT)/include 
     LLIBS     += -L$(DLMGROOT)/lib -ldlmg 
     LLIBS     += -L$(PSPFFTROOT)/lib -lpspfft

### VASPml (experimental)\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: VASPml (experimental)">edit</a> | (./index.php.md)")\]

------------------------------------------------------------------------

The [VASPml library](../methods/VASPml_library.md) is a
VASP-internal C++ library, providing functionality related to
[machine-learned force
fields](../categories/Category-Machine-learned_force_fields.md).
The VASPml library is automatically built alongside VASP if
`-Dlibvaspml` is added to the `CPP_OPTIONS` [precompiler
options](Precompiler_options.md)
in the makefile.include file.
In addition, a few more compiler settings regarding the C++ compiler,
include paths and VASPml options may be required. The
<a href="#Archetypical_files"
class="mw-selflink-fragment">makefile.include templates</a> provided in
VASP's `arch` directory contain pre-filled blocks corresponding to the
VASPml build. Uncomment the VASPml-related lines and fill with values
according to your [toolchain](Toolchains.md). For
example, when using the GCC toolchain with OpenBLAS the makefile.include
section may look like this:

    ...
    # For machine learning library VASPml (experimental)
    CPP_OPTIONS += -Dlibvaspml
    CXX_ML       = mpic++
    CXXFLAGS_ML  = -O3 -std=c++17 -Wall -Wextra
    INCLUDE_ML   = -I$(OPENBLAS_ROOT)/include
    ...

Apart from the mandatory `-Dlibvaspml` and [optional precompiler
flags](Precompiler_options.md)
VASPml requires to set its own compiler, flags and include path:

- `CXX_ML`: This should be a C++17-compatible C++ compiler with MPI
  support (usually an MPI wrapper corresponding to the selected
  toolchain, e.g. `mpic++`, `mpicxx`, `mpicpx` or `mpinc++`).
- `CXXFLAGS_ML`: Specifies the flags for the C++ compiler. Typically,
  here the optimization level (`-O3`) and the compliance with C++17 is
  specified.
- `INCLUDE_ML`: Include flags for the required dependencies should be
  added here.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vblue); --box-emph-color: var(--vblue); padding: 5px; color: var(--vdefault-text-nb); background: var(--vblue-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vblue);">Tip:</span></strong> For
some <a href="/wiki/Toolchains" title="Toolchains">toolchains</a> it is
not necessary to explicitly add paths here because the compilers
automatically include the correct directories (e.g. Intel oneAPI,
NVHPC). In other cases (e.g. GNU compiler with openBLAS) the given path
must contain the desired C++ headers of the dependencies:
<ul>
<li>CBLAS: <code>cblas.h</code></li>
<li>LAPACKE: <code>lapacke.h</code></li>
</ul></td>
</tr>
</tbody>
</table>

The VASPml project (source code and related files) is located within the
`src/vaspml` directory relative to the VASP root folder. Upon
compilation it is copied to the `build/std`, `build/gam` and/or
`build/ncl` build folders, just like all other VASP sources. If the
VASPml library was successfully compiled `libvaspml.a` will be located
in `build/std/vaspml/lib/` (similarly for the `gam` and `ncl` versions).
However, it is usually not necessary to check its presence because the
VASP build will handle this (and fail if VASPml cannot be built).

#### GRACE support\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: GRACE support">edit</a> \| (./index.php.md)\]

Optionally, VASPml may be compiled with support for [GRACE
machine-learned force
fields](../methods/Running_GRACE_force_fields_in_VASP.md).
However, there are two additional dependencies to third-party software
(<a href="https://www.tensorflow.org/install/lang_c"
class="external text" rel="nofollow">libtensorflow</a> and
<a href="https://github.com/serizba/cppflow" class="external text"
rel="nofollow">cppflow</a>) which must be installed beforehand:

- **<a href="https://www.tensorflow.org/install/lang_c"
  class="external text" rel="nofollow">libtensorflow</a>**: This is a
  pre-compiled C library which runs TensorFlow models. Its website
  provides downloadable archives but we actually recommend a simpler way
  of installing it (and all of its dependencies) via <a
  href="https://conda.io/projects/conda/en/latest/user-guide/getting-started.html"
  class="external text" rel="nofollow">conda</a> and `pip`:

<table
style="width:100%; table-layout: fixed; border-spacing: 0; padding: 0; margin: 0; background-color: var(--vCB-bg); color: var(--vdefault-text); border-width: 1px; border-style: solid; border-color: var(--vCB-border);">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre
style="margin: 0; padding: 1em; background: none; border: none; white-space: pre; overflow-x: auto; font-family: monospace;"><code>conda create -n tf python=3.12
conda activate tf
pip install --upgrade pip
pip install tensorflow[and-cuda]</code></pre></td>
</tr>
</tbody>
</table>

This will install all necessary libraries and header files into a
directory which can be identified by running

<table
style="width:100%; table-layout: fixed; border-spacing: 0; padding: 0; margin: 0; background-color: var(--vCB-bg); color: var(--vdefault-text); border-width: 1px; border-style: solid; border-color: var(--vCB-border);">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre
style="margin: 0; padding: 1em; background: none; border: none; white-space: pre; overflow-x: auto; font-family: monospace;"><code>dirname $(python -c &#39;import tensorflow as tf; print(tf.__file__)&#39; 2&gt;/dev/null)</code></pre></td>
</tr>
</tbody>
</table>

in a shell while the conda environment is still active. This path is
required below in the `TENSORFLOW_ROOT` variable.

- **<a href="https://github.com/serizba/cppflow" class="external text"
  rel="nofollow">cppflow</a>**: This is a C++ library which simplifies
  loading of TensorFlow models. Because it is a header-only library, no
  separate build process and linking is required to use it. To prepare
  its use for VASPml, just download it from its website and save it to a
  directory of your preference. For example, use
  `git clone git@github.com:serizba/cppflow.git` or download and unpack
  an archive from
  <a href="https://github.com/serizba/cppflow/releases/tag/v2.0.0"
  class="external text" rel="nofollow">here</a>.

Finally, with the mandatory dependencies installed, extra lines need to
be added in the
makefile.include to build VASP
with GRACE support. As of VASP 6.6.0 the `makefile.include.gnu` contains
an example block, similar to this:

    ...
    # Support for GRACE force fields (requires VASPml, experimental)
    CPP_OPTIONS     += -DVASPML_ENABLE_GRACE
    CPPFLOW_ROOT    ?= /path/to/your/cppflow/installation
    TENSORFLOW_ROOT ?= /path/to/your/tensorflow/installation
    INCLUDE_ML      += -I$(CPPFLOW_ROOT)/include -I$(TENSORFLOW_ROOT)/include
    LLIBS           += $(TENSORFLOW_ROOT)/libtensorflow_cc.so.2 $(TENSORFLOW_ROOT)/libtensorflow_framework.so.2
    LLIBS           += -Wl,-rpath,$(TENSORFLOW_ROOT)
    ...

|  |
|----|
| **Tip:** The conda environment created for downloading the libtensorflow library is neither required for compiling nor for running VASP! With the line `LLIBS += -Wl,-rpath,$(TENSORFLOW_ROOT)` the path to the Tensorflow library is imprinted into the VASP binary and hence no environment is required to load it at runtime. |

## Related articles\[<a
href="/wiki/index.php?title=Makefile.include&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: Related articles">edit</a> \| (./index.php.md)\]

[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md),
[Compiler options](Compiler_options.md),
[Precompiler options](Precompiler_options.md),
[Linking to
libraries](Linking_to_libraries.md), [GPU
ports of VASP](GPU_ports_of_VASP.md), [VASPml
library](../methods/VASPml_library.md),
[Toolchains](Toolchains.md), [Validation
tests](Validation_tests.md), [Known
issues](Known_issues.md)

------------------------------------------------------------------------



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

- [1 Archetypical files](#Archetypical_files)
  - [1.1 Intel Composer suite and oneAPI HPC toolkit for CPU and
    GPU](#Intel_Composer_suite_and_oneAPI_HPC_toolkit_for_CPU_and_GPU)
  - [1.2 GNU compilers for CPUs](#GNU_compilers_for_CPUs)
  - [1.3 NVIDIA HPC-SDK for CPU and
    GPU](#NVIDIA_HPC-SDK_for_CPU_and_GPU)
  - [1.4 Cray compiler environment (CCE) for CPU and
    GPU](#Cray_compiler_environment_(CCE)_for_CPU_and_GPU)
  - [1.5 Others](#Others)
- [2 Customize](#Customize)
  - [2.1 HDF5 support (strongly recommended, and mandatory for some
    features)](#HDF5_support_(strongly_recommended,_and_mandatory_for_some_features))
  - [2.2 fftlib (recommended when using
    OpenMP)](#fftlib_(recommended_when_using_OpenMP))
  - [2.3 Wannier90 (optional)](#Wannier90_(optional))
  - [2.4 Libxc (optional)](#Libxc_(optional))
  - [2.5 Libbeef (optional)](#Libbeef_(optional))
  - [2.6 DFT-D4 and simple-DFT-D3
    (optional)](#DFT-D4_and_simple-DFT-D3_(optional))
  - [2.7 ELPA (optional)](#ELPA_(optional))
  - [2.8 libMBD (optional)](#libMBD_(optional))
  - [2.9 Plugins (optional)](#Plugins_(optional))
  - [2.10 SCPC (optional)](#SCPC_(optional))
  - [2.11 VASPml (experimental)](#VASPml_(experimental))
    - [2.11.1 GRACE support](#GRACE_support)
- [3 Related articles](#Related_articles)

## Archetypical files
The templates contain information such as [precompiler
options](Precompiler_options.md), [compiler
options](Compiler_options.md), and [how to link
libraries](Linking_to_libraries.md). Choose
the template based on the compiler, parallelization etc. from the list
below and mind the description:

### Intel Composer suite and [oneAPI HPC toolkit](https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html) for CPU and GPU
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

### GNU compilers for CPUs
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

### [NVIDIA HPC-SDK](https://developer.nvidia.com/hpc-sdk) for CPU and GPU
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

### Cray compiler environment (CCE) for CPU and GPU
- [makefile.include.cray](Makefile.include.cray.md):
  Parallelized using MPI for CPU
- [makefile.include.cray_omp](Makefile.include.cray_omp.md):
  Parallelized using MPI + OpenMP for CPU
- [makefile.include.cray_omp_off](Makefile.include.cray_omp_off.md):
  [OpenMP offloading](GPU_ports_of_VASP.md) port
  for AMD datacenter GPUs.

### Others
- [makefile.include.nec_aurora](Makefile.include.nec_aurora.md)

&nbsp;

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

## Customize
Open the selected template of the [archetypical
files](#Archetypical_files) and add the required information as
explained in the comments towards the end of the file. Then, add any
optional feature as listed below. For more details see the [list of
precompiler options](Precompiler_options.md).

### HDF5 support (strongly recommended, and mandatory for some features)
------------------------------------------------------------------------

The HDF5 library is is needed for reading and writing HDF5 files such as
[vaspin.h5](../input-files/Vaspin.h5.md),
[vaspout.h5](../output-files/Vaspout.h5.md) and
[vaspwave.h5](../output-files/Vaspwave.h5.md). The library is available
for download on the [HDF5 official
website](https://www.hdfgroup.org/solutions/hdf5/). To activate [HDF5
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

### fftlib (recommended when using OpenMP)
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

### Wannier90 (optional)
------------------------------------------------------------------------

To include the Wannier90 program, download the library from [the
source](http://www.wannier.org) and compile `libwannier.a`.

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

### Libxc (optional)
------------------------------------------------------------------------

To include the Libxc library of exchange-correlation functionals,
install the library from [the source](https://libxc.gitlab.io/download/)
and install it. Note that to get correct results with meta-GGA
functionals (see discussion at
[LTBOUNDLIBXC](../incar-tags/LTBOUNDLIBXC.md)), it is necessary to
use Libxc from version 5.2.0 onwards (or the master version from
[gitlab](https://gitlab.com/libxc/libxc) for the latest implemented
functionals) and to compile it with the option `--disable-fhc`. For
instance, with GNU Autotools the steps to compile Libxc are

    autoreconf -i (necessary is the executable configure is not already present)
    ./configure --prefix=PATH/TO/LIBXC --disable-fhc
    make
    make install

Then, add the following in the VASP `makefile.include`

    CPP_OPTIONS += -DUSELIBXC
    LIBXC_ROOT  ?= /path/to/your/libxc/installation
    LLIBS       += -L$(LIBXC_ROOT)/lib -lxcf03 -lxc
    INCS        += -I$(LIBXC_ROOT)/include

### Libbeef (optional)
------------------------------------------------------------------------

To include the BEEF van der Waals functionals, install the library from
[the source on GitHub](https://github.com/vossjo/libbeef) and add the
following in the VASP `makefile.include`

    CPP_OPTIONS  += -Dlibbeef
    LIBBEEF_ROOT ?= /path/to/your/libbeef/installation
    LLIBS        += -L$(LIBBEEF_ROOT)/lib -lbeef

### DFT-D4 and simple-DFT-D3 (optional)
------------------------------------------------------------------------

To link to the [DFT-D4](../methods/DFT-D4.md) and/or
[simple-DFT-D3](../methods/Simple-DFT-D3.md) packages of van der
Waals methods, install

- the modular computation tool chain library (mctc-lib) from
  [https://github.com/grimme-lab/mctc-lib](https://github.com/grimme-lab/mctc-lib)
  (must be installed before [DFT-D4](../methods/DFT-D4.md) and
  [simple-DFT-D3](../methods/Simple-DFT-D3.md))
- the [DFT-D4](../methods/DFT-D4.md) package from
  [https://github.com/dftd4/dftd4](https://github.com/dftd4/dftd4),
  which should in principle find the mctc-lib pre-installation
- the [simple-DFT-D3](../methods/Simple-DFT-D3.md) package from
  [https://github.com/dftd3/simple-dftd3](https://github.com/dftd3/simple-dftd3),
  which should in principle find the mctc-lib pre-installation

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

[TABLE]

### ELPA (optional)
------------------------------------------------------------------------

To include the ELPA eigenvalue solvers, install the library from [the
source on GitLab](https://gitlab.mpcdf.mpg.de/elpa/elpa) and add the
following in the VASP `makefile.include`

    CPP_OPTIONS += -DELPA
    ELPA_ROOT   ?= /path/to/your/elpa/installation
    LLIBS       += -L$(ELPA_ROOT)/lib -lelpa
    INCS        += -I$(ELPA_ROOT)/include/elpa-<version>/elpa
    INCS        += -I$(ELPA_ROOT)/include/elpa-<version>/modules

|  |
|----|
| **Mind:** In the above you need to replace `<version>` by the correct designation of your ELPA version. |

### libMBD (optional)
------------------------------------------------------------------------

To include the library libMBD of many-body dispersion methods, install
the library from [the source on
GitHub](https://github.com/libmbd/libmbd) and add the following in the
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

### Plugins (optional)
------------------------------------------------------------------------

Create a new
[conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
environment. Alternative environment creation packages should work, but
we have not tested them.

       conda create -n vasp_plugin python=3.10

Enter the create `vasp_plugin` conda environment

       conda activate vasp_plugin

Navigate to the `plugins` directory within VASP source code,

       cd </path/to/vasp/source/code>/src/plugins

Install the VASP Python package through
[pip](https://pip.pypa.io/en/stable/installation)

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

### SCPC (optional)
------------------------------------------------------------------------

The [Self-Consistent Potential
Correction](Self-Consistent_Potential_Correction.md)
(SCPC) method is implemented in VASP version 6.2 and later. A patch to
add SCPC functionality to VASP 5.4.4, along with various bug fixes for
the implementation in VASP 6, can be obtained from the
[authors](https://github.com/aradi/SCPC-Method).

To compile the VASP with SCPC support, you need the
[DL_MG](https://bitbucket.org/dlmgteam/dl_mg_code_public/downloads/) and
[PSPFFT](https://code.ornl.gov/reubendb/pspfft) libraries to solve the
Poisson equations and handle isolated potentials. After downloading and
compiling these libraries, activate SCPC support during VASP compilation
by adding the following snippet to the end of the `makefile.include`
file, adjusting the paths to match your DL_MG and PSPFFT installation:

     # SCPC METHOD
     CPP_OPTIONS += -DSCPC
     SCPC_LIBEXT  = /scpc/libext 
     DLMGROOT   = $(SCPC_LIBEXT)/dl_mg 
     PSPFFTROOT = $(SCPC_LIBEXT)/pspfft 
     INCS      += -I$(DLMGROOT)/include 
     INCS      += -I$(PSPFFTROOT)/include 
     LLIBS     += -L$(DLMGROOT)/lib -ldlmg 
     LLIBS     += -L$(PSPFFTROOT)/lib -lpspfft

### VASPml (experimental)
------------------------------------------------------------------------

The [VASPml library](../methods/VASPml_library.md) is a
VASP-internal C++ library, providing functionality related to
[machine-learned force
fields](../categories/Category-Machine-learned_force_fields.md).
The VASPml library is automatically built alongside VASP if
`-Dlibvaspml` is added to the `CPP_OPTIONS` [precompiler
options](Precompiler_options.md)
in the makefile.include file. In addition, a few more compiler settings
regarding the C++ compiler, include paths and VASPml options may be
required. The [makefile.include templates](#Archetypical_files) provided
in VASP's `arch` directory contain pre-filled blocks corresponding to
the VASPml build. Uncomment the VASPml-related lines and fill with
values according to your [toolchain](Toolchains.md). For
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

[TABLE]

The VASPml project (source code and related files) is located within the
`src/vaspml` directory relative to the VASP root folder. Upon
compilation it is copied to the `build/std`, `build/gam` and/or
`build/ncl` build folders, just like all other VASP sources. If the
VASPml library was successfully compiled `libvaspml.a` will be located
in `build/std/vaspml/lib/` (similarly for the `gam` and `ncl` versions).
However, it is usually not necessary to check its presence because the
VASP build will handle this (and fail if VASPml cannot be built).

#### GRACE support
Optionally, VASPml may be compiled with support for [GRACE
machine-learned force
fields](../methods/Running_GRACE_force_fields_in_VASP.md).
However, there are two additional dependencies to third-party software
([libtensorflow](https://www.tensorflow.org/install/lang_c) and
[cppflow](https://github.com/serizba/cppflow)) which must be installed
beforehand:

- **[libtensorflow](https://www.tensorflow.org/install/lang_c)**: This
  is a pre-compiled C library which runs TensorFlow models. Its website
  provides downloadable archives but we actually recommend a simpler way
  of installing it (and all of its dependencies) via
  [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
  and `pip`:

[TABLE]

This will install all necessary libraries and header files into a
directory which can be identified by running

[TABLE]

in a shell while the conda environment is still active. This path is
required below in the `TENSORFLOW_ROOT` variable.

- **[cppflow](https://github.com/serizba/cppflow)**: This is a C++
  library which simplifies loading of TensorFlow models. Because it is a
  header-only library, no separate build process and linking is required
  to use it. To prepare its use for VASPml, just download it from its
  website and save it to a directory of your preference. For example,
  use `git clone git@github.com:serizba/cppflow.git` or download and
  unpack an archive from
  [here](https://github.com/serizba/cppflow/releases/tag/v2.0.0).

Finally, with the mandatory dependencies installed, extra lines need to
be added in the makefile.include to build VASP with GRACE support. As of
VASP 6.6.0 the `makefile.include.gnu` contains an example block, similar
to this:

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

## Related articles
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

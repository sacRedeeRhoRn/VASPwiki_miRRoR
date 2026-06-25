<!-- Source: https://vasp.at/wiki/index.php/Linking_to_libraries | revid: 34714 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Linking to libraries


The link is specified by linker variables and then the linker is invoked
as:

    $(FCL) -o vasp  ..all-objects.. $(LLIBS)

It is mandatory to link VASP to a library for Fast-Fourier
transformations (FFT), the lib library, the parser library, and the
linear algebra libraries BLAS, LAPACK, and scaLAPACK, as well as for the
OpenACC GPU port
<a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC-SDK</a> (≧21.2). Other libraries, e.g., the
HDF5 library and Wannier90, are optional.


## Contents


- [1 Linker
  variables](#Linker_variables)
  - [1.1
    FCL](#FCL)
  - [1.2
    LLIBS](#LLIBS)
- [2 Libraries for
  linear algebra
  (mandatory)](#Libraries_for_linear_algebra_(mandatory))
- [3 fftw library
  (mandatory)](#fftw_library_(mandatory))
  - [3.1
    OBJECTS](#OBJECTS)
  - [3.2
    INCS](#INCS)
  - [3.3 Special
    rules for the optimization level of FFT related
    objects](#Special_rules_for_the_optimization_level_of_FFT_related_objects)
- [4 lib library
  (mandatory)](#lib_library_(mandatory))
  - [4.1
    CPP_LIB](#CPP_LIB)
  - [4.2
    FC_LIB](#FC_LIB)
  - [4.3
    FFLAGS_LIB](#FFLAGS_LIB)
  - [4.4
    FREE_LIB](#FREE_LIB)
  - [4.5
    CC_LIB](#CC_LIB)
  - [4.6
    CFLAGS_LIB](#CFLAGS_LIB)
  - [4.7
    OBJECTS_LIB](#OBJECTS_LIB)
- [5 parser library
  (mandatory)](#parser_library_(mandatory))
  - [5.1
    CXX_PARS](#CXX_PARS)
- [6 QD
  library](#QD_library)
- [7 Optional
  libraries](#Optional_libraries)
  - [7.1 Related
    articles](#Related_articles)


# Linker variables\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Linker variables">edit</a> \| (./index.php.md)\]

### FCL\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: FCL">edit</a> \| (./index.php.md)\]

The command that invokes the linker. In most cases:

    FCL=$(FC) [+ some options]

- Using the Intel Composer suite (Fortran compiler + MKL libraries),
  typically:

<!-- -->

    FCL=$(FC) -mkl=sequential

### LLIBS\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: LLIBS">edit</a> \| (./index.php.md)\]

Specify libraries and/or objects to be linked against, in the usual way:

    LLIBS=[-L/path/to/installation/lib -llibrary] [/path/to/file/library.a] [/path/to/file/object.o]

One has to specify several numerical libraries (BLAS, LAPACK or
scaLAPACK, etc).

For instance, using the Intel Composer suite (and compiling with
`CPP_OPTIONS= .. -DscaLAPACK ..`) this yields:

> MKL_PATH   = $(MKLROOT)/lib/intel64
>     BLACS      = -lmkl_blacs_intelmpi_lp64
>     SCALAPACK  = $(MKL_PATH)/libmkl_scalapack_lp64.a $(BLACS)
>     LLIBS      += $(SCALAPACK)

The list of default objects required to compile VASP is given by the
variable `SOURCE` in the `/path/to/vasp.X.X.X/src/.objects` file.
Objects to be added to this list can be specified in `makefile.include`
by means of:

    OBJECTS= .. your list of objects ..

In practice, several objects *must* be added in this manner, e.g., [FFT
libraries](#Fast-Fourier_transformation_(mandatory)).

# Libraries for linear algebra (mandatory)\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Libraries for linear algebra (mandatory)">edit</a> \| (./index.php.md)")\]

To build VASP, you need to link against BLAS, LAPACK, and scaLAPACK.
Some compiler suites, e.g., the Intel Composer suite, pre-package these
libraries, so there is no need to download and build them yourself.

- Using the Intel Composer suite, linking against the BLAS, LAPACK, and
  scaLAPACK libraries that are part of MKL is done as follows:

> FCL        = mpiifort -mkl=sequential
>
>     MKL_PATH   = $(MKLROOT)/lib/intel64
>     BLAS       =
>     LAPACK     =
>     BLACS      = -lmkl_blacs_intelmpi_lp64
>     SCALAPACK  = $(MKL_PATH)/libmkl_scalapack_lp64.a $(BLACS)
>
>     LLIBS     += $(SCALAPACK) $(LAPACK) $(BLAS)

In case you use Intel's compilers with OpenMPI instead of Intel-MPI
replace the `BLACS` line above by:

    BLACS       = -lmkl_blacs_openmpi_lp64

- For
  <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
  rel="nofollow">NVIDIA HPC-SDK</a> (\>=21.2) that is:

> BLAS       = -lblas
>     LAPACK     = -llapack
>     SCALAPACK  = -Mscalapack
>
>     LLIBS     += $(SCALAPACK) $(LAPACK) $(BLAS)

- When you have built BLAS, LAPACK, and scaLAPACK yourself, you should
  link against the corresponding shared-objects (`lib*.so`) as follows:

> LIBDIR     = /path/to/my/libs/
>     BLAS       = -L$(LIBDIR) -lrefblas
>     LAPACK     = -L$(LIBDIR) -ltmglib -llapack
>     SCALAPACK  = -L$(LIBDIR) -lscalapack
>
>     LLIBS     += $(SCALAPACK) $(LAPACK) $(BLAS)

To link against a static library object (`*.a`), for instance for
scaLAPACK, replace the `SCALAPACK` line above by:

    SCALAPACK  = $(LIBDIR)/libscalapack.a

# fftw library (mandatory)\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: fftw library (mandatory)">edit</a> \| (./index.php.md)")\]

This library provides routines to perform Fast Fourier transformations
(FFTs).

### OBJECTS\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: OBJECTS">edit</a> \| (./index.php.md)\]

Add the objects to be compiled (or linked against) that provide the FFTs
(may include static libraries of objects `*.a`).

Most probably you are building with `-DMPI` and want use the FFTs from
some `fftw` library (recommended). In that case:

    OBJECTS = fftmpiw.o fftmpi_map.o fftw3d.o fft3dlib.o

### INCS\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: INCS">edit</a> \| (./index.php.md)\]

For the `fftw` library, i.e.,

    OBJECTS= .. fftw3d.o fftmpiw.o ..

the variable `INCS` must be set to include the directory that holds
`fftw3.f`:

    INCS+=-I/path/to/fftw/installation

This is needed because `fftw3d.F` and `fftmpiw.F` include `fftw3.f`.

|  |
|----|
| **Mind:** If `INCS` for `fftw` library is not set, then `fftw3.f` has to be present in `/path/to/vasp.X.X.X/src`. |

Common choices are:

- When building with the Intel Composer suite it is best to link against
  the MKL `fftw` wrappers of Intel's FFTs:

> FCL = $(FC) -mkl=sequential
>
>     OBJECTS = fftmpiw.o fftmpi_map.o fftw3d.o fft3dlib.o
>     INCS   += -I$(MKLROOT)/include/fftw

- To explicitly link against an `fftw` library (in this case
  `fftw-3.3.4`):

> OBJECTS = fftmpiw.o fftmpi_map.o fftw3d.o fft3dlib.o
>     FFTW       ?= /path/to/your/fftw-3.3.4
>     LLIBS      += -L$(FFTW)/lib -lfftw3
>     INCS       += -I$(FFTW)/include

- For other configurations, please take lead from the
  `makefile.include.your_choice` files in `/path/to/vasp.x.x.x/arch` or
  look at the
  [makefile.include](Makefile.include.md).

## Special rules for the optimization level of FFT related objects\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Special rules for the optimization level of FFT related objects">edit</a> \| (./index.php.md)\]

Based on past experience the optimization level for the compilation of
the FFT-related objects is set explicitly. This is done as follows:

    OBJECTS_O1 += fft3dfurth.o fftw3d.o fftmpi.o fftmpiw.o
    OBJECTS_O2 += fft3dlib.o

# lib library (mandatory)\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: lib library (mandatory)">edit</a> \| (./index.php.md)")\]

The source of this library is included in the VASP distribution. The
following variables are related to its configuration:

### CPP_LIB\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: CPP_LIB">edit</a> \| (./index.php.md)\]

The command to invoke the precompiler. In most cases, it is set to:

    CPP_LIB=$(CPP)

### FC_LIB\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: FC_LIB">edit</a> | (./index.php.md)\]

The command to invoke your Fortran compiler. Usually, set to:

    FC_LIB=$(FC)

|  |
|----|
| **Mind:** The library can be compiled without MPI support, i.e., when `FC=mpif90`, FC_LIB may specify a Fortran compiler without MPI support, e.g.,`FC_LIB=ifort`. |

### FFLAGS_LIB\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: FFLAGS_LIB">edit</a> \| (./index.php.md)\]

Fortran compiler flags, including a specification of the level of
optimization. In most cases:

    FFLAGS_LIB=-O1

### FREE_LIB\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: FREE_LIB">edit</a> \| (./index.php.md)\]

Specifies the options that the Fortran compiler requires to accept
free-form source layout, without line-length limitation. In most cases,
it will suffise to set:

    FREE_LIB=$(FREE)

### CC_LIB\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: CC_LIB">edit</a> | (./index.php.md)\]

The command to invoke your C compiler, e.g., gcc, icc, etc.

|  |
|----|
| **Mind:** The `lib` library can be compiled without MPI support. |

### CFLAGS_LIB\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: CFLAGS_LIB">edit</a> | (./index.php.md)\]

C compiler flags, including a specification of the level of
optimization. In most cases:

    CFLAGS_LIB=-O

### OBJECTS_LIB\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: OBJECTS_LIB">edit</a> | (./index.php.md)\]

List of "non-standard" objects to be added to the library. In most
cases:

    OBJECTS_LIB= linpack_double.o

When compiling VASP with
[-Duse_shmem](Precompiler_options.md),
one has to add `getshmem.o` as well, i.e., add the following line:

    OBJECTS_LIB+= getshmem.o

# parser library (mandatory)\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: parser library (mandatory)">edit</a> | (./index.php.md)")\]

The source of this library is included in the VASP distribution. The
following variables are related to its configuration:

### CXX_PARS\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: CXX_PARS">edit</a> | (./index.php.md)\]

The command to invoke your C++ compiler, e.g., g++, icpc, etc.

The `parser` needs to be linked against a *C++ Standard* library. If
this is not already part of the definition of `FCL` it can be added to
the [compiler option](Compiler_options.md)
`LLIBS`. When using the Intel Composer suite this would amount to:

    LLIBS += -lstdc++

# QD library\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: QD library">edit</a> | (./index.php.md)\]

The QD library is included in
<a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC SDK</a> ≧ 21.2 and supports quadruple
precision arithmetic. Add the following lines to your
[makefile.include](Makefile.include.md):

    NVROOT     ?= /path/to/nvidia/hpc_sdk/Linux_x86_64/version
    QD         ?= $(NVROOT)/compilers/extras/qd
    LLIBS      += -L$(QD)/lib -lqdmod -lqd
    INCS       += -I$(QD)/include/qd

|  |
|----|
| **Tip:** The following line might help to find the NVIDIA root: |

    NVROOT      =$(shell which nvfortran | awk -F /compilers/bin/nvfortran '{ print $$1 }')

|  |
|----|
| **Important:** As of <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC SDK</a> = 21.2, the library path of the QD library needs to be added manually to the system environment: |

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(NVROOT)/compilers/extras/qd/lib

# Optional libraries\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: Optional libraries">edit</a> \| (./index.php.md)\]

See [how to customize the makefile.include
file](Makefile.include.md) to find an
overview of optional libraries.

## Related articles\[<a
href="/wiki/index.php?title=Linking_to_libraries&amp;veaction=edit&amp;section=21"
class="mw-editsection-visualeditor"
title="Edit section: Related articles">edit</a> \| (./index.php.md)\]

[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md),
[makefile.include](Makefile.include.md), [Compiler
options](Compiler_options.md), [Precompiler
options](Precompiler_options.md), [GPU ports of
VASP](GPU_ports_of_VASP.md),
[Toolchains](Toolchains.md), [Validation
tests](Validation_tests.md), [Known
issues](Known_issues.md)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.nvhpc_omp | revid: 35427 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.nvhpc_omp


    # Default precompiler options
    CPP_OPTIONS = -DHOST=\"LinuxNV\" \
                  -DMPI -DMPI_BLOCK=8000 -Duse_collective \
                  -DscaLAPACK \
                  -DCACHE_SIZE=4000 \
                  -Davoidalloc \
                  -Dvasp6 \
                  -Dtbdyn \
                  -Dqd_emulate \
                  -Dfock_dblbuf \
                  -D_OPENMP

    CPP         = nvfortran -Mpreprocess -Mfree -Mextend -E $(CPP_OPTIONS) $*$(FUFFIX)  > $*$(SUFFIX)

    FC          = mpif90 -mp
    FCL         = mpif90 -mp -c++libs

    FREE        = -Mfree

    FFLAGS      = -Mbackslash -Mlarge_arrays

    OFLAG       = -fast

    DEBUG       = -Mfree -O0 -traceback

    # Redefine the standard list of O1 and O2 objects
    SOURCE_O1  := pade_fit.o minimax_dependence.o wave_window.o
    SOURCE_O2  := pead.o

    # For what used to be vasp.5.lib
    CPP_LIB     = $(CPP)
    FC_LIB      = nvfortran
    CC_LIB      = nvc -w
    CFLAGS_LIB  = -O
    FFLAGS_LIB  = -O1 -Mfixed
    FREE_LIB    = $(FREE)

    OBJECTS_LIB = linpack_double.o

    # For the parser library
    CXX_PARS    = nvc++ --no_warnings

    ##
    ## Customize as of this point! Of course you may change the preceding
    ## part of this file as well if you like, but it should rarely be
    ## necessary ...
    ##
    # When compiling on the target machine itself , change this to the
    # relevant target when cross-compiling for another architecture
    VASP_TARGET_CPU ?= -tp host
    FFLAGS     += $(VASP_TARGET_CPU)

    # Specify your NV HPC-SDK installation (mandatory)
    #... first try to set it automatically
    NVROOT      =$(shell which nvfortran | awk -F /compilers/bin/nvfortran '{ print $$1 }')

    # If the above fails, then NVROOT needs to be set manually
    #NVHPC      ?= /opt/nvidia/hpc_sdk
    #NVVERSION   = 21.11
    #NVROOT      = $(NVHPC)/Linux_x86_64/$(NVVERSION)

    # Software emulation of quadruple precsion (mandatory)
    QD         ?= $(NVROOT)/compilers/extras/qd
    LLIBS      += -L$(QD)/lib -lqdmod -lqd
    INCS       += -I$(QD)/include/qd

    # BLAS (mandatory)
    BLAS        = -lblas

    # LAPACK (mandatory)
    LAPACK      = -llapack

    # scaLAPACK (mandatory)
    SCALAPACK   = -Mscalapack

    LLIBS      += $(SCALAPACK) $(LAPACK) $(BLAS)

    # FFTW (mandatory)
    FFTW_ROOT  ?= /path/to/your/fftw/installation
    LLIBS      += -L$(FFTW_ROOT)/lib -lfftw3 -lfftw3_omp
    INCS       += -I$(FFTW_ROOT)/include

    # HDF5-support (optional but strongly recommended, and mandatory for some features)
    #CPP_OPTIONS+= -DVASP_HDF5
    #HDF5_ROOT  ?= /path/to/your/hdf5/installation
    #LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
    #INCS       += -I$(HDF5_ROOT)/include

    # For the VASP-2-Wannier90 interface (optional)
    #CPP_OPTIONS    += -DVASP2WANNIER90
    #WANNIER90_ROOT ?= /path/to/your/wannier90/installation
    #LLIBS          += -L$(WANNIER90_ROOT)/lib -lwannier

    # For the fftlib library (recommended)
    #CPP_OPTIONS+= -Dsysv
    #FCL        += fftlib.o
    #CXX_FFTLIB  = nvc++ -mp --no_warnings -std=c++11 -DFFTLIB_THREADSAFE
    #INCS_FFTLIB = -I./include -I$(FFTW_ROOT)/include
    #LIBS       += fftlib
    #LLIBS      += -ldl

    # For machine learning library VASPml (experimental)
    #CPP_OPTIONS += -Dlibvaspml
    #CXX_ML       = mpic++ -mp
    #CXXFLAGS_ML  = -O3 -std=c++17 -Wall -Wextra
    #INCLUDE_ML   =
    ## This may be required for the C++17 filesystem library if the underlying
    ## system compiler is older than GNU 9.1. For newer versions this can be removed.
    #LLIBS       += -lstdc++fs

------------------------------------------------------------------------

[makefile.include](Makefile.include.md)



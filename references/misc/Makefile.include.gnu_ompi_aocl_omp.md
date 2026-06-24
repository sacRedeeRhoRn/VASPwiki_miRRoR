<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.gnu_ompi_aocl_omp | revid: 35425 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.gnu_ompi_aocl_omp
    # Default precompiler options
    CPP_OPTIONS = -DHOST=\"LinuxGNU\" \
                  -DMPI -DMPI_BLOCK=8000 -Duse_collective \
                  -DscaLAPACK \
                  -DCACHE_SIZE=4000 \
                  -Davoidalloc \
                  -Dvasp6 \
                  -Dtbdyn \
                  -Dfock_dblbuf \
                  -D_OPENMP

    CPP         = gcc -E -C -w $*$(FUFFIX) >$*$(SUFFIX) $(CPP_OPTIONS)

    FC          = mpif90 -fopenmp
    FCL         = mpif90 -fopenmp

    FREE        = -ffree-form -ffree-line-length-none

    FFLAGS      = -w -ffpe-summary=none

    OFLAG       = -O2
    OFLAG_IN    = $(OFLAG)
    DEBUG       = -O0

    # For what used to be vasp.5.lib
    CPP_LIB     = $(CPP)
    FC_LIB      = $(FC)
    CC_LIB      = gcc
    CFLAGS_LIB  = -O
    FFLAGS_LIB  = -O1
    FREE_LIB    = $(FREE)

    OBJECTS_LIB = linpack_double.o

    # For the parser library
    CXX_PARS    = g++
    LLIBS       = -lstdc++

    ##
    ## Customize as of this point! Of course you may change the preceding
    ## part of this file as well if you like, but it should rarely be
    ## necessary ...
    ##

    # When compiling on the target machine itself, change this to the
    # relevant target when cross-compiling for another architecture
    VASP_TARGET_CPU ?= -march=native
    FFLAGS     += $(VASP_TARGET_CPU)

    # For gcc-10 and higher (comment out for older versions)
    FFLAGS     += -fallow-argument-mismatch

    # BLAS (mandatory)
    AMDBLIS_ROOT ?= /path/to/your/amdblis/installation
    BLAS        = -L${AMDBLIS_ROOT}/lib -lblis-mt

    # LAPACK (mandatory)
    AMDLIBFLAME_ROOT ?= /path/to/your/amdlibflame/installation
    LAPACK      = -L${AMDLIBFLAME_ROOT}/lib -lflame

    # scaLAPACK (mandatory)
    AMDSCALAPACK_ROOT ?= /path/to/your/amdscalapack/installation
    SCALAPACK   = -L${AMDSCALAPACK_ROOT}/lib -lscalapack

    LLIBS      += $(SCALAPACK) $(LAPACK) $(BLAS)

    # FFTW (mandatory)
    AMDFFTW_ROOT  ?= /path/to/your/amdfftw/installation
    LLIBS      += -L$(AMDFFTW_ROOT)/lib -lfftw3 -lfftw3_omp
    INCS       += -I$(AMDFFTW_ROOT)/include

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
    #CXX_FFTLIB  = g++ -fopenmp -std=c++11 -DFFTLIB_THREADSAFE
    #INCS_FFTLIB = -I./include -I$(AMDFFTW_ROOT)/include
    #LIBS       += fftlib
    #LLIBS      += -ldl

    # For machine learning library VASPml (experimental)
    #CPP_OPTIONS += -Dlibvaspml
    #CXX_ML       = mpic++ -fopenmp
    #CXXFLAGS_ML  = -O3 -std=c++17 -Wall -Wextra
    #INCLUDE_ML   = -I${AMDBLIS_ROOT}/include/blis -I${AMDLIBFLAME_ROOT}/include

------------------------------------------------------------------------

[makefile.include](Makefile.include.md)

<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.gnu | revid: 35421 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.gnu
    # Default precompiler options
    CPP_OPTIONS = -DHOST=\"LinuxGNU\" \
                  -DMPI -DMPI_BLOCK=8000 -Duse_collective \
                  -DscaLAPACK \
                  -DCACHE_SIZE=4000 \
                  -Davoidalloc \
                  -Dvasp6 \
                  -Dtbdyn \
                  -Dfock_dblbuf

    CPP         = gcc -E -C -w $*$(FUFFIX) >$*$(SUFFIX) $(CPP_OPTIONS)

    FC          = mpif90
    FCL         = mpif90

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

    # BLAS and LAPACK (mandatory)
    OPENBLAS_ROOT ?= /path/to/your/openblas/installation
    BLASPACK    = -L$(OPENBLAS_ROOT)/lib -lopenblas

    # scaLAPACK (mandatory)
    SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
    SCALAPACK   = -L$(SCALAPACK_ROOT)/lib -lscalapack

    LLIBS      += $(SCALAPACK) $(BLASPACK)

    # FFTW (mandatory)
    FFTW_ROOT  ?= /path/to/your/fftw/installation
    LLIBS      += -L$(FFTW_ROOT)/lib -lfftw3
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

    # For machine learning library VASPml (experimental)
    #CPP_OPTIONS += -Dlibvaspml
    #CXX_ML       = mpic++
    #CXXFLAGS_ML  = -O3 -std=c++17 -Wall -Wextra
    #INCLUDE_ML   = -I$(OPENBLAS_ROOT)/include

    # Support for GRACE force fields (requires VASPml, experimental)
    #CPP_OPTIONS     += -DVASPML_ENABLE_GRACE
    #CPPFLOW_ROOT    ?= /path/to/your/cppflow/installation
    ## Auto-detect tensorflow root directory from python if available from current environment.
    ## Alternatively, enter /path/to/your/tensorflow/installation manually.
    #TENSORFLOW_ROOT ?= $(shell dirname `python -c 'import tensorflow as tf; print(tf.__file__)' 2>/dev/null`)
    #INCLUDE_ML      += -I$(CPPFLOW_ROOT)/include -I$(TENSORFLOW_ROOT)/include
    #LLIBS           += $(TENSORFLOW_ROOT)/libtensorflow_cc.so.2 $(TENSORFLOW_ROOT)/libtensorflow_framework.so.2
    #LLIBS           += -Wl,-rpath,$(TENSORFLOW_ROOT)

------------------------------------------------------------------------

[makefile.include](Makefile.include.md)

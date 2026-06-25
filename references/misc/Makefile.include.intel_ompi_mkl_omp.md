<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.intel_ompi_mkl_omp | revid: 35420 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.intel_ompi_mkl_omp


    # Default precompiler options
    CPP_OPTIONS = -DHOST=\"LinuxIFC\" \
                  -DMPI -DMPI_BLOCK=8000 -Duse_collective \
                  -DscaLAPACK \
                  -DCACHE_SIZE=4000 \
                  -Davoidalloc \
                  -Dvasp6 \
                  -Dtbdyn \
                  -Dfock_dblbuf \
                  -D_OPENMP

    CPP         = fpp -f_com=no -free -w0  $*$(FUFFIX) $*$(SUFFIX) $(CPP_OPTIONS)

    FC          = mpif90 -qopenmp
    FCL         = mpif90

    FREE        = -free -names lowercase

    FFLAGS      = -assume byterecl -w

    OFLAG       = -O2
    OFLAG_IN    = $(OFLAG)
    DEBUG       = -O0

    # For what used to be vasp.5.lib
    CPP_LIB     = $(CPP)
    FC_LIB      = $(FC)
    CC_LIB      = icc
    CFLAGS_LIB  = -O
    FFLAGS_LIB  = -O1
    FREE_LIB    = $(FREE)

    OBJECTS_LIB = linpack_double.o

    # For the parser library
    CXX_PARS    = icpc
    LLIBS       = -lstdc++

    ##
    ## Customize as of this point! Of course you may change the preceding
    ## part of this file as well if you like, but it should rarely be
    ## necessary ...
    ##

    # When compiling on the target machine itself, change this to the
    # relevant target when cross-compiling for another architecture
    VASP_TARGET_CPU ?= -xHOST
    FFLAGS     += $(VASP_TARGET_CPU)
     
    # Intel MKL for FFTW, BLAS, LAPACK, and scaLAPACK
    # (Note: for Intel Parallel Studio's MKL use -mkl instead of -qmkl)
    FCL        += -qmkl
    MKLROOT    ?= /path/to/your/mkl/installation
    INCS        =-I$(MKLROOT)/include/fftw

    # Use a separate scaLAPACK installation (optional but recommended in combination with OpenMPI)
    # Comment out the two lines below if you want to use scaLAPACK from MKL instead
    SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
    LLIBS      += -L${SCALAPACK_ROOT}/lib -lscalapack

    # HDF5-support (optional but strongly recommended, and mandatory for some features)
    #CPP_OPTIONS+= -DVASP_HDF5
    #HDF5_ROOT  ?= /path/to/your/hdf5/installation
    #LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
    #INCS       += -I$(HDF5_ROOT)/include

    # For the VASP-2-Wannier90 interface (optional)
    #CPP_OPTIONS    += -DVASP2WANNIER90
    #WANNIER90_ROOT ?= /path/to/your/wannier90/installation
    #LLIBS          += -L$(WANNIER90_ROOT)/lib -lwannier

    # For the fftlib library (hardly any benefit in combination with MKL's FFTs)
    #CPP_OPTIONS+= -Dsysv
    #FCL         = mpif90 fftlib.o -qmkl
    #CXX_FFTLIB  = icpc -qopenmp -std=c++11 -DFFTLIB_USE_MKL -DFFTLIB_THREADSAFE
    #INCS_FFTLIB = -I./include -I$(MKLROOT)/include/fftw
    #LIBS       += fftlib

    # For machine learning library VASPml (experimental)
    #CPP_OPTIONS += -Dlibvaspml
    #CXX_ML       = mpic++ -qopenmp
    #CXXFLAGS_ML  = -O3 -std=c++17 -Wall
    #INCLUDE_ML   =
    ## This may be required for the C++17 filesystem library if the underlying
    ## system compiler is older than GNU 9.1. For newer versions this can be removed.
    #LLIBS       += -lstdc++fs

------------------------------------------------------------------------

[makefile.include](Makefile.include.md)



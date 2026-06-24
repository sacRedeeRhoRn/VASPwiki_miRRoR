<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.nec_aurora | revid: 35433 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.nec_aurora
    # Default precompiler options
    CPP_OPTIONS = -DHOST=\"SXAurora\" \
                  -D__NEC__ \
                  -D__NEC_TUNE__ \
                  -DMPI \
                  -DMPI_INPLACE \
                  -DMPI_BLOCK=8000 \
                  -Duse_collective \
                  -DscaLAPACK \
                  -DCACHE_SIZE=32768 \
                  -Davoidalloc \
                  -Dvasp6 \
                  -Dtbdyn \
                  -Dfock_dblbuf \
                  -DCRREXP_inline \
                  -DRPROMU_DGEMV \
                  -DUSE_ERF

    CPP         = gcc -E -C -w $*$(FUFFIX) >$*$(SUFFIX) $(CPP_OPTIONS)

    FC          = mpinfort
    FCL         = mpinfort

    FREE        = -ffree-form -Wall

    FTRACE      = -no-ftrace
    INLINE      = -finline-functions -finline-file=random.f90
    REPORT      = -fdiag-parallel=0 -fdiag-vector=0 -fdiag-inline=0 -w

    FFLAGS      = $(FTRACE) $(INLINE) $(REPORT)
    OFLAG       = -O3
    OFLAG_IN    = $(OFLAG)
    DEBUG       = -O0

    # For what used to be vasp.5.lib
    CPP_LIB     = $(CPP)
    FC_LIB      = $(FC)
    CC_LIB      = ncc
    CFLAGS_LIB  = -O
    FFLAGS_LIB  = -O1
    FREE_LIB    = $(FREE)

    OBJECTS_LIB = linpack_double.o

    # For the parser library
    CXX_PARS    = nc++

    ##
    ## Customize as of this point! Of course you may change the preceding
    ## part of this file as well if you like, but it should rarely be
    ## necessary ...
    ##

    # BLAS, LAPACK, scaLAPACK, and FFTW from NEC Numeric Library Collection (NEC NLC)
    NLC_ROOT   ?= /path/to/your/nlc/installation
    BLAS        = -L$(NLC_ROOT)/lib -lblas_sequential -lcblas
    LAPACK      = -L$(NLC_ROOT)/lib -llapack
    SCALAPACK   = -L$(NLC_ROOT)/lib -lscalapack

    FFTW        = -L$(NLC_ROOT)/lib -laslfftw3_mpi -lasl_mpi_sequential -cxxlib -static -static-nec
    INCS        = -I$(NLC_ROOT)/include

    LLIBS       = $(SCALAPACK) $(LAPACK) $(BLAS) $(FFTW)
     
    # Uncomment the following to use ELPA
    #CPP_OPTIONS+= -DELPA
    #ELPA_ROOT  ?= <path-to-your-elpa-2021.05.001-installation>
    #LLIBS      := -L$(ELPA_ROOT)/lib -lelpa $(LLIBS)
    #INCS       += -I$(ELPA_ROOT)/include/elpa-2021.05.001/modules
    #
    # HDF5-support (optional but strongly recommended, and mandatory for some features)
    #CPP_OPTIONS+= -DVASP_HDF5
    #HDF5_ROOT  ?= /path/to/your/hdf5/installation
    #LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran -lhdf5 -lsz -lz
    #INCS       += -I$(HDF5_ROOT)/include

    # For the VASP-2-Wannier90 interface (optional)
    #CPP_OPTIONS    += -DVASP2WANNIER90
    #WANNIER90_ROOT ?= /path/to/your/wannier90/installation
    #LLIBS          += -L$(WANNIER90_ROOT)/lib -lwannier

    # For machine learning library VASPml (experimental)
    #CPP_OPTIONS += -Dlibvaspml
    #CXX_ML       = mpinc++
    #CXXFLAGS_ML  = -O3 -std=gnu++17 -Wall
    #INCLUDE_ML   = -I$(NLC_ROOT)/include
    #CPP_DEP      = $(CPP)

------------------------------------------------------------------------

[makefile.include](Makefile.include.md)

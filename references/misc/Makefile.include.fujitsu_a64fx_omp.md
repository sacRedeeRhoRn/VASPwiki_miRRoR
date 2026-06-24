<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.fujitsu_a64fx_omp | revid: 35435 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.fujitsu_a64fx_omp
    # Default precompiler options
    CPP_OPTIONS = -DHOST=\"FJ-A64FX\" \
                  -DMPI -DMPI_BLOCK=8000 -Duse_collective \
                  -DscaLAPACK \
                  -DCACHE_SIZE=4000 \
                  -Davoidalloc \
                  -Dvasp6 \
                  -Dtbdyn \
                  -Dfock_dblbuf \
                  -D_OPENMP

    CPP         = frt -Ccpp -E $(CPP_OPTIONS) $*$(FUFFIX) > $*$(SUFFIX)

    # N.B.: to cross-compile for A64FX on X86_64 replace mpifrt, frt, fcc, and FCC
    #       by mpifrtpx, frtpx, fccpx, and FCCpx, respectively.
    FC          = mpifrt -Kopenmp,simd_nouse_multiple_structures -X03
    FCL         = mpifrt -Kfz,openmp,simd_nouse_multiple_structures

    FREE        =

    FFLAGS      = -Koptmsg=2
    OFLAG       = -Kfast
    OFLAG_IN    = $(OFLAG)
    DEBUG       = -O0 -g
    OFLAG_1     = -O1
    OFLAG_2     = -O2
    OFLAG_3     = -Kfast

    OBJECTS_O1 += minimax_dependence.o elphon_common.o screened_2e.o
    OBJECTS_O2 += nonl.o vdw_nl.o

    # For what used to be vasp.5.lib
    CPP_LIB     = $(CPP)
    FC_LIB      = frt  -Ksimd_nouse_multiple_structures
    CC_LIB      = fcc -Nclang
    CFLAGS_LIB  = -O3
    FFLAGS_LIB  = $(OFLAG)
    FREE_LIB    = $(FREE)

    OBJECTS_LIB = linpack_double.o

    # For the parser library
    CXX_PARS    = FCC -Nclang -stdlib=libc++
    LLIBS       = --linkstl=libc++

    ##
    ## Customize as of this point! Of course you may change the preceding
    ## part of this file as well if you like, but it should rarely be
    ## necessary ...
    ##

    # BLAS, LAPACK, and SCALAPACK (mandatory)
    LLIBS      += -SSL2BLAMP -SCALAPACK

    # HINT: Fujitsu maintains its own fftw fork on GitHub
    #       (https://github.com/fujitsu/fftw3)
    FFTW       ?= /path/to/your/fujitsu/fftw3
    LLIBS      += -L$(FFTW)/lib64 -lfftw3 -lfftw3_omp
    INCS        = -I$(FFTW)/include

    # HDF5-support (optional but strongly recommended, and mandatory for some features)
    #CPP_OPTIONS+= -DVASP_HDF5
    #HDF5_ROOT  ?= /path/to/your/hdf5/installation
    #LLIBS      += -L$(HDF5_ROOT)/lib64 -lhdf5_fortran -lhdf5
    #INCS       += -I$(HDF5_ROOT)/include

    # For the fftlib library (recommended)
    #CPP_OPTIONS+= -Dsysv
    #FCL        += fftlib.o
    #CXX_FFTLIB  = FCC -Nclang -stdlib=libc++ -fopenmp -DFFTLIB_THREADSAFE
    #INCS_FFTLIB = -I./include -I$(FFTW)/include
    #LIBS       += fftlib
    #LLIBS      += -ldl

    # For the VASP-2-Wannier90 interface (optional)
    #CPP_OPTIONS    += -DVASP2WANNIER90
    #WANNIER90_ROOT ?= /path/to/your/wannier90/installation
    #LLIBS          += -L$(WANNIER90_ROOT)/lib64 -lwannier

    # For machine learning library VASPml (experimental)
    #CPP_OPTIONS += -Dlibvaspml
    #CXX_ML       = mpiFCC -Nclang -fopenmp
    #CXXFLAGS_ML  = -O3 -std=c++17 -stdlib=libc++
    #INCLUDE_ML   =
    #FJSV_ROOT   ?= /path/to/your/fujitsu/compilers/suite
    #LLIBS       += $(FJSV_ROOT)/lib64/libc++fs.a

    # Python plugin (experimental, requires python 3.10 or newer with pybind11 and numpy packages)
    #CPP_OPTIONS+= -DPLUGINS
    #LLIBS      += $(shell python3-config --ldflags --embed)
    #CXX_FLAGS   = $(shell python3 -m pybind11 --includes) -std=c++11 -stdlib=libc++

------------------------------------------------------------------------

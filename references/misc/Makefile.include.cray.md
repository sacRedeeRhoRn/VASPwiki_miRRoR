<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.cray | revid: 34586 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.cray
    # Precompiler options
    CPP_OPTIONS = -DHOST=\"LinuxFTN\" \
                  -DMPI -DMPI_BLOCK=8000 -Duse_collective \
                  -DscaLAPACK \
                  -DCACHE_SIZE=4000 \
                  -Davoidalloc \
                  -DMPI_INPLACE \
                  -Dvasp6 \
                  -Dtbdyn \
                  -Dfock_dblbuf

    CPP        = cpp --traditional -E -P -Wno-endif-labels $*$(FUFFIX) >$*$(SUFFIX) $(CPP_OPTIONS)

    FC         = ftn
    FCL        = $(FC)

    FREE       = -ffree -N 1023

    FFLAGS     = -dC -rmo -emEb
    # suppress warnings
    FFLAGS     += -m 4 

    # O1 is recommended, higher opt levels cause compiler problems, performance difference between O1 and O2 is negligible
    OFLAG      = -O1
    OFLAG_IN   = $(OFLAG)
    DEBUG      = -O0

    # fine grain control over lapack, by default ftn will link libsci with the appropriate configuration
    # LAPACK     = -L${CRAY_LIBSCI_PREFIX_DIR}/lib -lsci_cray_mpi
    # LLIBS      = $(LAPACK)

    FFTW_ROOT  ?= /opt/cray/pe/fftw/default/x86_milan
    LLIBS      += -L$(FFTW_ROOT)/lib -lfftw3
    INCS       = -I$(FFTW_ROOT)/include

    #
    # For what used to be vasp.5.lib
    CPP_LIB    = $(CPP)
    FC_LIB     = $(FC)
    CC_LIB     = cc
    CFLAGS_LIB = -O
    FFLAGS_LIB = -O1
    FREE_LIB   = $(FREE)

    OBJECTS_LIB= linpack_double.o getshmem.o

    # For the parser library
    CXX_PARS   = CC
    LLIBS      += -lstdc++

    # Normally no need to change this
    SRCDIR     = ../../src
    BINDIR     = ../../bin

    # HDF5-support (optional but strongly recommended, and mandatory for some features)
    #CPP_OPTIONS+= -DVASP_HDF5
    #HDF5_ROOT  ?= /path/to/your/hdf5/installation
    #LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
    #INCS       += -I$(HDF5_ROOT)/include

    # For the VASP-2-Wannier90 interface (optional)
    #CPP_OPTIONS    += -DVASP2WANNIER90
    #WANNIER90_ROOT ?= /path/to/your/wannier90/installation
    #LLIBS          += -L$(WANNIER90_ROOT)/lib -lwannier

    # special cray workarounds
    CRAYFTNVER=$(shell crayftn --version 2>/dev/null | grep "Version" | sed -n 's/.*Version \([0-9]\+\)\..*/\1/p')
    CPP_OPTIONS += -D__DCRAYFTN_VERSION=$(CRAYFTNVER)

------------------------------------------------------------------------

[makefile.include](Makefile.include.md)

<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.intel_serial | revid: 27602 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# makefile.include.intel_serial


    # Precompiler options
    CPP_OPTIONS = -DHOST=\"LinuxIFC\"\
                  -DCACHE_SIZE=4000 \
                  -Davoidalloc \
                  -Dtbdyn \
                  -Dfock_dblbuf

    CPP         = fpp -f_com=no -free -w0  $*$(FUFFIX) $*$(SUFFIX) $(CPP_OPTIONS)

    FC          = ifort
    FCL         = ifort -qmkl=sequential

    FREE        = -free -names lowercase

    FFLAGS      = -assume byterecl -w

    OFLAG       = -O2
    OFLAG_IN    = $(OFLAG)
    DEBUG       = -O0

    INCS        =-I$(MKLROOT)/include/fftw

    # For what used to be vasp.5.lib
    CPP_LIB     = $(CPP)
    FC_LIB      = $(FC)
    CC_LIB      = icc
    CFLAGS_LIB  = -O
    FFLAGS_LIB  = -O1
    FREE_LIB    = $(FREE)

    OBJECTS_LIB = linpack_double.o

    # For the parser library
    CXX_PARS   = icpc
    LLIBS      = -lstdc++

    # When compiling on the target machine itself, change this to the
    # relevant target when cross-compiling for another architecture
    VASP_TARGET_CPU ?= -xHOST
    FFLAGS     += $(VASP_TARGET_CPU)

------------------------------------------------------------------------

[makefile.include](Makefile.include.md)



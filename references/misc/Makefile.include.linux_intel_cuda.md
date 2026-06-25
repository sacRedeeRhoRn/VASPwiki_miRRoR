<!-- Source: https://vasp.at/wiki/index.php/Makefile.include.linux_intel_cuda | revid: 9896 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Makefile.include.linux intel cuda


    # Precompiler options                                                                                                                                                                                          
    CPP_OPTIONS= -DMPI -DHOST=\"LinuxIFC\" -DIFC \                                                                                                                                                                 
                 -DCACHE_SIZE=4000 -DPGF90 -Davoidalloc \                                                                                                                                                          
                 -DMPI_BLOCK=8000 -Duse_collective \                                                                                                                                                               
                 -Duse_bse_te \                                                                                                                                                                      
                 -Dkind8                                                                                                                                                                               
                                                                                                                                                                                                                   
    CPP        = fpp -f_com=no -free -w0  $*$(FUFFIX) $*$(SUFFIX) $(CPP_OPTIONS)

    FC         = mpiifort
    FCL        = mpiifort -mkl -lstdc++

    FREE       = -free -names lowercase

    FFLAGS     = -assume byterecl
    OFLAG      = -O2
    OFLAG_IN   = $(OFLAG)
    DEBUG      = -O0

    MKL_PATH   = $(MKLROOT)/lib/intel64
    BLAS       =
    LAPACK     =
    BLACS      = -lmkl_blacs_intelmpi_lp64
    SCALAPACK  = $(MKL_PATH)/libmkl_scalapack_lp64.a $(BLACS)

    OBJECTS    = fftmpiw.o fftmpi_map.o fft3dlib.o fftw3d.o \
                 $(MKLROOT)/interfaces/fftw3xf/libfftw3xf_intel.a

    INCS       =-I$(MKLROOT)/include/fftw

    LLIBS      = $(SCALAPACK) $(LAPACK) $(BLAS)


    #OBJECTS_O1 += fft3dfurth.o fftw3d.o fftmpi.o fftmpiw.o
    OBJECTS_O1 += fftw3d.o fftmpi.o fftmpiw.o
    OBJECTS_O2 += fft3dlib.o

    # For what used to be vasp.5.lib
    CPP_LIB    = $(CPP)
    FC_LIB     = $(FC)
    CC_LIB     = icc
    CFLAGS_LIB = -O
    FFLAGS_LIB = -O1
    FREE_LIB   = $(FREE)

    OBJECTS_LIB= linpack_double.o getshmem.o

    # Normally no need to change this
    SRCDIR     = ../../src
    BINDIR     = ../../bin

    #================================================
    # GPU Stuff

    CPP_GPU    = -DCUDA_GPU -DRPROMU_CPROJ_OVERLAP -DUSE_PINNED_MEMORY -DCUFFT_MIN=28

    OBJECTS_GPU = fftmpiw.o fftmpi_map.o fft3dlib.o fftw3d_gpu.o fftmpiw_gpu.o \
                  $(MKLROOT)/interfaces/fftw3xf/libfftw3xf_intel.a

    CUDA_ROOT  := /usr/local/cuda/
    NVCC       := $(CUDA_ROOT)/bin/nvcc
    CUDA_LIB   := -L$(CUDA_ROOT)/lib64 -lnvToolsExt -lcudart -lcuda -lcufft -lcublas

    GENCODE_ARCH    := -gencode=arch=compute_30,code=\"sm_30,compute_30\" -gencode=arch=compute_35,code=\"sm_35,compute_35\"

    MPI_INC    =/opt/intel/impi_latest/include64



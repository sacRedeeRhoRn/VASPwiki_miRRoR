<!-- Source: https://vasp.at/wiki/index.php/Personal_computer_installation | revid: 34290 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Personal computer installation


Here you will find instructions on how to install VASP on some
widely-used Linux distributions. For the sake of simplicity the
suggested build processes rely as much as possible on compilers and
libraries provided by the operating system's package manager. The focus
is on minimizing the effort to obtain working VASP binaries with only
little changes required to the provided
[`makefile.include`](Makefile.include.md)
templates in the `arch` directory.

|  |
|----|
| **Warning:** These short and convenient installation instructions may come at the cost of performance. They are not optimized with respect to compilers, libraries and hardware. Please consider benchmarking and optimizing your build process prior to large-scale production runs. |

In order to verify each build we run the FAST category tests of the
[testsuite](Validation_tests.md).

|  |
|----|
| **Tip:** All build instructions presented here include [HDF5 support](Makefile.include.md) "Makefile.include") to allow post-processing of results with <a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a>. |

The build instructions have been tested on clean installations (virtual
machines or docker images) of the operating systems in the following
table. Search for your desired combination of OS and VASP and click on
the provided link to get directly to the corresponding section on this
page:

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Operating system |  | VASP |  |  |  |
| Name | Version | 6.3.0 - 6.3.1 | 6.3.2 | 6.4.X | 6.5.0 |
| [Debian](#debian) | 11 | [Link](#building-vasp-63x-to-64x-on-debian-11) |  |  |  |
|  | 12 |  |  | [Link](#building-vasp-64x-to-650-on-debian-12) |  |
| [Ubuntu](#ubuntu) | 20.04 | [Link](#building-vasp-630---631-on-ubuntu-2004) |  |  |  |
|  | 22.04 | [Link](#building-vasp-63x-to-64x-on-ubuntu-2204) |  |  |  |
|  | 24.04 |  |  |  | [Link](#building-vasp-650-on-ubuntu-2404) |
| [Fedora](#fedora) | 35 | [Link](#building-vasp-630---631-on-fedora-35) |  |  |  |
|  | 37 - 38 |  |  | [Link](#building-vasp-64x-on-fedora-37-to-38) |  |
|  | 41 |  |  |  | [Link](#building-vasp-650-on-fedora-41) |
| [Rocky Linux](#rocky-linux) | 8.5 | [Link](#building-vasp-630---631-on-rocky-linux-85) |  |  |  |
|  | 9.0 |  | [Link](#building-vasp-632-on-rocky-linux-90) |  |  |
|  | 9.2 |  |  | [Link](#building-vasp-64x-on-rocky-linux-92) |  |
|  | 9.3 |  |  |  | [Link](#building-vasp-650-on-rocky-linux-93) |
| [Mac OS X](#mac-os-x) | M1/2/3/4 |  |  |  | [Link](#building-vasp-651-on-mac-os-x-apple-silicon-m1234)) |

A  red box background indicates
that there are known issues with the used compiler/library versions (see
the individual instructions for details). The table and corresponding
instructions will be updated when either a new version of VASP or a
major release of the operating systems is available. However, not all
combinations will be tested and hence some fields will stay blank. In
these cases it may still be helpful to start from instructions for
close-by tested combinations.

  


## Contents


- [1
  Debian](#debian)
  - [1.1 Building
    VASP 6.3.X to 6.4.X on Debian
    11](#building-vasp-63x-to-64x-on-debian-11)
  - [1.2 Building
    VASP 6.4.X to 6.5.0 on Debian
    12](#building-vasp-64x-to-650-on-debian-12)
- [2
  Ubuntu](#ubuntu)
  - [2.1 Building
    VASP 6.3.0 - 6.3.1 on Ubuntu
    20.04](#building-vasp-630---631-on-ubuntu-2004)
  - [2.2 Building
    VASP 6.3.X to 6.4.X on Ubuntu
    22.04](#building-vasp-63x-to-64x-on-ubuntu-2204)
  - [2.3 Building
    VASP 6.5.0 on Ubuntu
    24.04](#building-vasp-650-on-ubuntu-2404)
- [3
  Fedora](#fedora)
  - [3.1 Building
    VASP 6.3.0 - 6.3.1 on Fedora
    35](#building-vasp-630---631-on-fedora-35)
  - [3.2 Building
    VASP 6.4.X on Fedora 37 to
    38](#building-vasp-64x-on-fedora-37-to-38)
  - [3.3 Building
    VASP 6.5.0 on Fedora 41](#building-vasp-650-on-fedora-41)
- [4 Rocky
  Linux](#rocky-linux)
  - [4.1 Building
    VASP 6.3.0 - 6.3.1 on Rocky Linux
    8.5](#building-vasp-630---631-on-rocky-linux-85)
  - [4.2 Building
    VASP 6.3.2 on Rocky Linux
    9.0](#building-vasp-632-on-rocky-linux-90)
  - [4.3 Building
    VASP 6.4.X on Rocky Linux
    9.2](#building-vasp-64x-on-rocky-linux-92)
  - [4.4 Building
    VASP 6.5.0 on Rocky Linux
    9.3](#building-vasp-650-on-rocky-linux-93)
- [5 Mac OS
  X](#mac-os-x)
  - [5.1 Building
    VASP 6.5.1 on Mac OS X (Apple Silicon
    M1/2/3/4)](#building-vasp-651-on-mac-os-x-apple-silicon-m1234))
- [6 Footnotes and
  references](#footnotes-and-references)


## Debian\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Debian">edit</a> \| (./index.php.md)\]

### Building VASP 6.3.X to 6.4.X on Debian 11\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.3.X to 6.4.X on Debian 11">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-10.2.1 | openmpi-4.1.0 | fftw-3.3.8 | openblas-0.3.13 |  | netlib-scalapack-2.1.0 | hdf5-1.10.6 | Memory-leak[^ompi-bug-1-1] |

These packages can be installed directly from the command line like
this:

    sudo apt install rsync make build-essential g++ gfortran libopenblas-dev libopenmpi-dev libscalapack-openmpi-dev libfftw3-dev libhdf5-openmpi-dev

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack-openmpi

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -L/usr/lib/x86_64-linux-gnu/hdf5/openmpi/ -lhdf5_fortran
      INCS       += -I/usr/include/hdf5/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.4.X to 6.5.0 on Debian 12\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.4.X to 6.5.0 on Debian 12">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-12.2.0 | openmpi-4.1.4 | fftw-3.3.10 | openblas-0.3.21 |  | netlib-scalapack-2.2.1 | hdf5-1.10.8 |  |

These packages can be installed directly from the command line like
this:

    sudo apt install rsync make build-essential g++ gfortran libopenblas-dev libopenmpi-dev libscalapack-openmpi-dev libfftw3-dev libhdf5-openmpi-dev

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack-openmpi

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -L/usr/lib/x86_64-linux-gnu/hdf5/openmpi/ -lhdf5_fortran
      INCS       += -I/usr/include/hdf5/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

## Ubuntu\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Ubuntu">edit</a> \| (./index.php.md)\]

### Building VASP 6.3.0 - 6.3.1 on Ubuntu 20.04\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.3.0 - 6.3.1 on Ubuntu 20.04">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-9.4.0 | openmpi-4.0.3 | fftw-3.3.8 | openblas-0.3.8 |  | netlib-scalapack-2.1.0 | hdf5-1.10.4 | \- |

These packages can be installed directly from the command line like
this:

    sudo apt install make build-essential g++ gfortran libopenblas-dev libopenmpi-dev libscalapack-openmpi-dev libfftw3-dev libhdf5-openmpi-dev

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the line adding `-fallow-argument-mismatch` to the
  variable `FFLAGS`:

      # For gcc-10 and higher (comment out for older versions)
      #FFLAGS     += -fallow-argument-mismatch

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack-openmpi

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -L/usr/lib/x86_64-linux-gnu/hdf5/openmpi/ -lhdf5_fortran
      INCS       += -I/usr/include/hdf5/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.3.X to 6.4.X on Ubuntu 22.04\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.3.X to 6.4.X on Ubuntu 22.04">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-11.2.0 | openmpi-4.1.2 | fftw-3.3.8 | openblas-0.3.20 |  | netlib-scalapack-2.1.0 | hdf5-1.10.7 | \- |

These packages can be installed directly from the command line like
this:

    sudo apt install rsync make build-essential g++ gfortran libopenblas-dev libopenmpi-dev libscalapack-openmpi-dev libfftw3-dev libhdf5-openmpi-dev

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack-openmpi

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -L/usr/lib/x86_64-linux-gnu/hdf5/openmpi/ -lhdf5_fortran
      INCS       += -I/usr/include/hdf5/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.5.0 on Ubuntu 24.04\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.5.0 on Ubuntu 24.04">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-13.3.0 | openmpi-4.1.6 | fftw-3.3.10 | openblas-0.3.26 |  | netlib-scalapack-2.2.1 | hdf5-1.10.10 | \- |

These packages can be installed directly from the command line like
this:

    sudo apt install rsync make build-essential g++ gfortran libopenblas-dev libopenmpi-dev libscalapack-openmpi-dev libfftw3-dev libhdf5-openmpi-dev

If this fails, you may run the following command and then try again

    sudo apt-get update

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack-openmpi

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -L/usr/lib/x86_64-linux-gnu/hdf5/openmpi/ -lhdf5_fortran
      INCS       += -I/usr/include/hdf5/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

## Fedora\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Fedora">edit</a> \| (./index.php.md)\]

### Building VASP 6.3.0 - 6.3.1 on Fedora 35\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.3.0 - 6.3.1 on Fedora 35">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-11.2.1 | openmpi-4.1.1 | fftw-3.3.8 | openblas-0.3.19 |  | netlib-scalapack-2.1.0 | hdf5-1.10.7 | Memory-leak[^ompi-bug-1-1] |

These packages can be installed directly from the command line like
this:

    sudo yum install gcc gcc-c++ gcc-gfortran openblas-devel openmpi-devel scalapack-openmpi-devel fftw-devel hdf5-openmpi-devel

Add the following lines to your `.bashrc` file located in your home
directory:

    export PATH=${PATH}:/usr/lib64/openmpi/bin/
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64/openmpi/lib

and either open a new shell or run this command to activate the lines
above:

    source ~/.bashrc

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -lhdf5_fortran
      INCS       += -I/usr/lib64/gfortran/modules/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.4.X on Fedora 37 to 38\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.4.X on Fedora 37 to 38">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|
| OS version | Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| 37 | gcc-12.3.1 | openmpi-4.1.4 | fftw-3.3.10 | openblas-0.3.21 |  | netlib-scalapack-2.2.0 | hdf5-1.12.1 |  |
| 38 | gcc-13.2.1 | openmpi-4.1.4 | fftw-3.3.10 | openblas-0.3.21 |  | netlib-scalapack-2.2.0 | hdf5-1.12.1 |  |

These packages can be installed directly from the command line like
this:

    sudo yum install rsync gcc gcc-c++ gcc-gfortran openblas-devel openmpi-devel scalapack-openmpi-devel fftw-devel hdf5-openmpi-devel

Add the following lines to your `.bashrc` file located in your home
directory:

    export PATH=${PATH}:/usr/lib64/openmpi/bin/
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64/openmpi/lib

and either open a new shell or run this command to activate the lines
above:

    source ~/.bashrc

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -lhdf5_fortran
      INCS       += -I/usr/lib64/gfortran/modules/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.5.0 on Fedora 41\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.5.0 on Fedora 41">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|
| OS version | Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| 41 | gcc-14.2.1 | openmpi-5.0.5 | fftw-3.3.10 | openblas-0.3.26 |  | netlib-scalapack-2.2.0 | hdf5-1.12.1 |  |

These packages can be installed directly from the command line like
this:

    sudo yum install rsync gcc gcc-c++ gcc-gfortran openblas-devel openmpi-devel scalapack-openmpi-devel fftw-devel hdf5-openmpi-devel

Add the following lines to your `.bashrc` file located in your home
directory:

    export PATH=${PATH}:/usr/lib64/openmpi/bin/
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64/openmpi/lib

and either open a new shell or run this command to activate the lines
above:

    source ~/.bashrc

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -lhdf5_fortran
      INCS       += -I/usr/lib64/gfortran/modules/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

## Rocky Linux\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Rocky Linux">edit</a> \| (./index.php.md)\]

### Building VASP 6.3.0 - 6.3.1 on Rocky Linux 8.5\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.3.0 - 6.3.1 on Rocky Linux 8.5">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-11.2.1 | openmpi-4.1.1 | fftw-3.3.5 | openblas-0.3.12 |  | netlib-scalapack-2.0.2 | hdf5-1.10.5 | Memory-leak[^ompi-bug-1-1] |

Some of these packages are available from the default package sources:

    sudo dnf install openmpi-devel fftw-devel

Unfortunately the GCC version 8.5 provided by default is not suitable
for compiling VASP. As an alternative we can use a newer version from
the <a href="https://docs.fedoraproject.org/en-US/epel/"
class="external text" rel="nofollow">EPEL repositories</a>:

    sudo dnf install epel-release
    sudo dnf install gcc-toolset-11-gcc gcc-toolset-11-gcc-c++ gcc-toolset-11-gcc-gfortran

Furthermore, some required libraries are available within the
"PowerTools" repositories:

    sudo dnf install dnf-plugins-core
    sudo dnf config-manager --set-enabled powertools
    sudo dnf install openblas-devel scalapack-openmpi-devel hdf5-openmpi-devel

Add the following lines to your `.bashrc` file located in your home
directory:

    export PATH=/opt/rh/gcc-toolset-11/root/bin/:/usr/lib64/openmpi/bin/:${PATH}

and either open a new shell or run this command to activate the lines
above:

    source ~/.bashrc

|  |
|----|
| **Mind:** As long as the path `/opt/rh/gcc-toolset-11/root/bin/` is in the `PATH` variable the system's default compiler binaries (`gcc`, `g++`, `gfortran`,...) are "hidden" behind the newer ones. |

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -lhdf5_fortran
      INCS       += -I/usr/lib64/gfortran/modules/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.3.2 on Rocky Linux 9.0\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.3.2 on Rocky Linux 9.0">edit</a> | (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-11.2.1 | openmpi-4.1.1 | fftw-3.3.8 | openblas-0.3.15 |  | netlib-scalapack-2.2.0 | hdf5-1.12.1 | Memory-leak[^ompi-bug-1-1] |

Some of these packages are available from the default package sources:

    sudo dnf install gcc gcc-c++ gcc-gfortran openmpi-devel fftw-devel

Some required libraries are available within the "CRB" ("Code Ready
Builder") and <a href="https://docs.fedoraproject.org/en-US/epel/"
class="external text" rel="nofollow">EPEL repositories</a> repositories:

    sudo dnf config-manager --set-enabled crb
    sudo dnf install openblas-devel
    sudo dnf install epel-release
    sudo dnf install scalapack-openmpi-devel hdf5-openmpi-devel

Add the following lines to your `.bashrc` file located in your home
directory:

    export PATH=${PATH}:/usr/lib64/openmpi/bin/
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64/openmpi/lib

and either open a new shell or run this command to activate the lines
above:

    source ~/.bashrc

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -lhdf5_fortran
      INCS       += -I/usr/lib64/gfortran/modules/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.4.X on Rocky Linux 9.2\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.4.X on Rocky Linux 9.2">edit</a> | (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-11.3.1 | openmpi-4.1.1 | fftw-3.3.8 | openblas-0.3.21 |  | netlib-scalapack-2.2.0 | hdf5-1.12.1 | Memory-leak[^ompi-bug-1-1] |

Some of these packages are available from the default package sources:

    sudo dnf install rsync gcc gcc-c++ gcc-gfortran openmpi-devel fftw-devel

Some required libraries are available within the "CRB" ("Code Ready
Builder") and <a href="https://docs.fedoraproject.org/en-US/epel/"
class="external text" rel="nofollow">EPEL repositories</a> repositories:

    sudo dnf install 'dnf-command(config-manager)'
    sudo dnf config-manager --set-enabled crb
    sudo dnf install openblas-devel
    sudo dnf install epel-release
    sudo dnf install scalapack-openmpi-devel hdf5-openmpi-devel

Add the following lines to your `.bashrc` file located in your home
directory:

    export PATH=${PATH}:/usr/lib64/openmpi/bin/
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64/openmpi/lib

and either open a new shell or run this command to activate the lines
above:

    source ~/.bashrc

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -lhdf5_fortran
      INCS       += -I/usr/lib64/gfortran/modules/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

### Building VASP 6.5.0 on Rocky Linux 9.3\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.5.0 on Rocky Linux 9.3">edit</a> | (./index.php.md)\]

------------------------------------------------------------------------

First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we install the following compiler and
libraries from the system's package manager:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFT | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-11.5.0 | openmpi-4.1.1 | fftw-3.3.8 | openblas-0.3.26 |  | netlib-scalapack-2.2.0 | hdf5-1.12.1 | Memory-leak[^ompi-bug-1-1] |

Some of these packages are available from the default package sources:

    sudo dnf install rsync gcc gcc-c++ gcc-gfortran openmpi-devel fftw-devel

Some required libraries are available within the "CRB" ("Code Ready
Builder") and <a href="https://docs.fedoraproject.org/en-US/epel/"
class="external text" rel="nofollow">EPEL repositories</a> repositories:

    sudo dnf install 'dnf-command(config-manager)'
    sudo dnf config-manager --set-enabled crb
    sudo dnf install openblas-devel
    sudo dnf install epel-release
    sudo dnf install scalapack-openmpi-devel hdf5-openmpi-devel

Add the following lines to your `.bashrc` file located in your home
directory:

    export PATH=${PATH}:/usr/lib64/openmpi/bin/
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64/openmpi/lib

and either open a new shell or run this command to activate the lines
above:

    source ~/.bashrc

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu_omp` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu_omp makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -lfftw3 -lfftw3_omp
      INCS       += -I/usr/include

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -lhdf5_fortran
      INCS       += -I/usr/lib64/gfortran/modules/openmpi/

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j

Once the build process is complete the binaries are located in the VASP
`bin` subfolder. They were compiled with [OpenMP-threading
support](Combining_MPI_and_OpenMP.md).
Before running VASP please always check if the `OMP_NUM_THREADS`
environment variable is set according to your needs. For example, if you
require only pure MPI parallelization without OpenMP threading add

    export OMP_NUM_THREADS=1

in your `~/.bashrc` file.

## Mac OS X\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Mac OS X">edit</a> | (./index.php.md)\]

### Building VASP 6.5.1 on Mac OS X (Apple Silicon M1/2/3/4)\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: Building VASP 6.5.1 on Mac OS X (Apple Silicon M1/2/3/4)">edit</a> | (./index.php.md)")\]

------------------------------------------------------------------------

VASP can be compiled on recent Apple Silicon hardware running Mac OS.
First, we need to make sure that the
[prerequisites](Installing_VASP.6.X.X.md)
for building VASP are met. Here, we use the package manager
<a href="https://brew.sh/" class="external text"
rel="nofollow">homebrew</a> to install all required dependencies:

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Compiler | MPI | FFTW | BLAS | LAPACK | ScaLAPACK | HDF5 | Known issues |
| gcc-14.2.0 | openmpi-5.0.7 | fftw-3.3.10 | openblas-0.3.29 |  | netlib-scalapack-2.2.2 | hdf5-1.14.5 | some test fail with precision loss |

These packages can be installed directly from the command line after
<a href="https://brew.sh/" class="external text"
rel="nofollow">homebrew</a> is installed:

    brew install gfortran gcc fftw hdf5 openmpi openblas scalapack qd

|  |
|----|
| **Important:** Since the `brew` command will install the latest available versions of the packages their version numbers may not match with the ones in the table above. Only the package versions in this table have been checked to work correctly. Please consult the [list of validated toolchains](Toolchains.md) for known incompatibilities. To install a specific version the `@` syntax can be used, e.g., `brew install gfortran@14` will install the last `gfortran` package of the GCC 14 series. |

Make sure that all brew packages are linked to the default install
location, i.e. you can run `brew link -n openblas` to check whether brew
already linked all library and include files.

Next, unpack the VASP source code to a location of your choice. Then
change into the VASP base directory and use the
`arch/makefile.include.gnu` template as basis for the
[`makefile.include`](Makefile.include.md):

    cp arch/makefile.include.gnu makefile.include

Search for the paragraph in `makefile.include` starting with
`## Customize as of this point!` and apply the following changes below:

- Define a new variable `BREW_ROOT = /opt/homebrew/`

- Comment out the `OPENBLAS_ROOT` variable (not needed) and set
  `BLASPACK`:

      # BLAS and LAPACK (mandatory)
      #OPENBLAS_ROOT ?= /path/to/your/openblas/installation
      BLASPACK    = -L$(BREW_ROOT)/lib -lopenblas

- Comment out the `SCALAPACK_ROOT` variable (not needed) and set
  `SCALAPACK`:

      # scaLAPACK (mandatory)
      #SCALAPACK_ROOT ?= /path/to/your/scalapack/installation
      SCALAPACK   = -L$(BREW_ROOT)/lib -lscalapack

- Comment out the `FFTW_ROOT` variable (not needed). Set `LLIBS` and
  `INCS` in the FFTW section:

      # FFTW (mandatory)
      #FFTW_ROOT  ?= /path/to/your/fftw/installation
      LLIBS      += -L$(BREW_ROOT)/lib -lfftw3
      INCS       += -I$(BREW_ROOT)/include 

- Quad precision support with OpenMPI in brew seems to be broken (test
  failures in GW tests). To fix this we have to link explicitly against
  the qd library by adding the <a
  href="https://www.vasp.at/wiki/index.php/Precompiler_options#-Dqd_emulate"
  class="external text" rel="nofollow">following lines</a> in the
  makefile:

      CPP_OPTIONS += -Dqd_emulate
      LLIBS       += -L$(BREW_ROOT)/lib -lqdmod
      INCS        += -I$(BREW_ROOT)/include/qd

- Enable HDF5 support by adding `-DVASP_HDF5` to the `CPP_OPTIONS`
  variable. Leave `HDF5_ROOT` variable commented out (not needed). Set
  `LLIBS` and `INCS` in the HDF5 section:

      # HDF5-support (optional but strongly recommended)
      CPP_OPTIONS+= -DVASP_HDF5
      #HDF5_ROOT  ?= /path/to/your/hdf5/installation
      LLIBS      += -L$(BREW_ROOT)/lib -lhdf5_fortran
      INCS       += -I$(BREW_ROOT)/include

Save your `makefile.include` and compile VASP:

    make DEPS=1 -j N

where N is the number of threads you want to use for building. Once the
build process is complete the binaries are located in the VASP `bin`
subfolder. OpenMP support can be enabled but there are no performance
gains for standard SCF calculations. The Apple provided "Accelerate"
LAPACK implementation does compile `-framework Accelerate` but crashes
upon execution.

The hardware seems to benefit from small [NCORE](../incar-tags/NCORE.md)
and high [KPAR](../incar-tags/KPAR.md) settings. To increase performance
avoid using the efficiency cores, i.e. run VASP only with number of MPI
ranks equivalent to the number of performance cores.

## Footnotes and references\[<a
href="/wiki/index.php?title=Personal_computer_installation&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: Footnotes and references">edit</a> \| (./index.php.md)\]

[^ompi-bug-1-1]: A bug in OpenMPI versions 4.0.4-4.1.1 causes a memory leak in some ScaLAPACK calls. This mainly affects long [molecular-dynamics](/wiki/Category:Molecular_dynamics "Category:Molecular dynamics") runs. This issue is fixed as of openmpi-4.1.2.

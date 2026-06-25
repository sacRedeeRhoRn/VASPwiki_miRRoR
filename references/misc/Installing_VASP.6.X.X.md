<!-- Source: https://vasp.at/wiki/index.php/Installing_VASP.6.X.X | revid: 34713 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Installing VASP.6.X.X


As a <a href="https://vasp.at%7C" class="external text"
rel="nofollow">license holder</a>, you can download the source code of
VASP from the
<a href="https://vasp.at%7C" class="external text" rel="nofollow">VASP
Portal</a>. If your system fulfills the [requirements](#requirements),
you can install VASP.6.X.X by following the [steps
below](#install-vasp-with-makefileinclude). There are two separate ways
to install VASP:

1.  With the traditional makefile.include templates included in the
    `/path/to/vasp.x.x.x/arch` directory. See section
    <a href="#Install_VASP_with_makefile.include"
    class="mw-selflink-fragment">Install VASP with makefile.include</a>.
2.  Using the CMake build system. See section
    <a href="#Install_VASP_with_CMake" class="mw-selflink-fragment">Install
    VASP with CMake</a>.

There is a separate [guide to installing
VASP.5.X.X](Installing_VASP.5.X.X.md).


## Contents


- [1
  Requirements](#requirements)
- [2 Install VASP
  with makefile.include](#install-vasp-with-makefileinclude)
  - [2.1 Step 1:
    Download](#step-1-download)
  - [2.2 Step 2:
    Prepare makefile.include](#step-2-prepare-makefileinclude)
  - [2.3 Step 3:
    Make](#step-3-make)
  - [2.4 Step 4:
    Test](#step-4-test)
  - [2.5 Step 5:
    Install](#step-5-install)
- [3 Install VASP
  with CMake](#install-vasp-with-cmake)
  - [3.1 Step 1:
    Download VASP](#step-1-download-vasp)
  - [3.2 Step 2:
    Download CMake files](#step-2-download-cmake-files)
  - [3.3 Step 3:
    CMake Configure](#step-3-cmake-configure)
  - [3.4 Step 4:
    Build](#step-4-build)
  - [3.5 Step 5:
    Test](#step-5-test)
  - [3.6 Step 6:
    Install](#step-6-install)
- [4 Subdirectories
  in vasp.6.x.x](#subdirectories-in-vasp6xx)
- [5 Validated
  Toolchains via CI](#validated-toolchains-via-ci)
- [6 Install on a
  common Linux
  distribution](#install-on-a-common-linux-distribution)
- [7 Related
  sections](#related-sections)


## Requirements\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Requirements">edit</a> \| (./index.php.md)\]

For the compilation of VASP one needs:

- Compilers for Fortran (at least F2008 compliant), C, and C++. For
  instance, one of the following compiler suites:

\- <a href="https://gcc.gnu.org" class="external text"
rel="nofollow">gcc</a>

\- <a
href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#base-kit"
class="external text" rel="nofollow">intel-oneapi-base-kit</a>+<a
href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#hpc-kit"
class="external text" rel="nofollow">intel-oneapi-hpc-kit</a>

\- <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC-SDK</a>

\- <a href="https://developer.amd.com/amd-aocc" class="external text"
rel="nofollow">AOCC</a> (for AMD CPUs)

|  |
|----|
| **Mind:** For the [GPU ports of VASP](GPU_ports_of_VASP.md) on must use the compilers from the <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC-SDK</a> (\>=21.2) (to run on NVIDIA GPUs), the <a href="https://cpe.ext.hpe.com/docs/25.03/cce/index.html"
class="external text" rel="nofollow">HPE Cray compiler environment
CCE</a> (\>= 19.0) (to run on AMD GPUs), or the Intel <a
href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler.html"
class="external text" rel="nofollow">Intel Fortran Compiler IFX</a> (\>=2025.3.0) (to run on Intel GPUs) |

- Numerical libraries: FFTW, BLAS, LAPACK, and ScaLAPACK. For example,
  one of the following combinations:

\- <a
href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#base-kit"
class="external text" rel="nofollow">intel-oneapi-mkl</a>

\- <a href="http://www.fftw.org" class="external text"
rel="nofollow">FFTW</a> +
<a href="https://www.openblas.net" class="external text"
rel="nofollow">OpenBLAS</a> +
<a href="http://www.netlib.org/scalapack" class="external text"
rel="nofollow">ScaLAPACK</a>

\- <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC-SDK</a> (comes with OpenBLAS and ScaLAPACK) +
<a href="http://www.fftw.org" class="external text"
rel="nofollow">FFTW</a>

\- <a href="https://developer.amd.com/amd-aocl" class="external text"
rel="nofollow">AOCL</a> (for AMD CPUs)

- An implementation of the Message Passing Interface (MPI). For
  instance, one of the following:

\- <a
href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#hpc-kit"
class="external text" rel="nofollow">intel-oneapi-mpi</a>

\- <a href="https://www.open-mpi.org" class="external text"
rel="nofollow">OpenMPI</a>

\- <a href="https://developer.nvidia.com/hpc-sdk" class="external text"
rel="nofollow">NVIDIA HPC-SDK</a> (comes with OpenMPI)

These are the required components to build VASP. Additionally, we
strongly recommend enabling HDF5 support by providing a suitable HDF5
library in the makefile.include file (see the [HDF5 section
here](Makefile.include.md) "Makefile.include")).
Optional features available through external libraries such as libxc,
libbeef, and others can also be found
[here](Makefile.include.md).

To find a combination of compilers and libraries that works, have a look
at [our list of validated toolchains](Toolchains.md). On
a personal computer, i.e., your desktop machine or laptop, you may use
[these validated
instructions](Personal_computer_installation.md).

## Install VASP with makefile.include\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Install VASP with makefile.include">edit</a> \| (./index.php.md)\]

### Step 1: Download\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Download">edit</a> \| (./index.php.md)\]

Download the source code of VASP from the
<a href="https://vasp.at%7C" class="external text" rel="nofollow">VASP
Portal</a>, copy it to the desired location on your machine, and unzip
the file to obtain the folder `/path/to/vasp.x.x.x` and reveal [its
content](#subdirectories-in-vasp6xx).

### Step 2: Prepare [makefile.include](Makefile.include.md)\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Prepare makefile.include">edit</a> \| (./index.php.md)\]

Create a makefile.include starting from a template in
`/path/to/vasp.x.x.x/arch` that resembles your system:

    cp arch/makefile.include.your_choice  ./makefile.include

[Adapt your makefile.include
file](Makefile.include.md) to your system and
select optional features.

### Step 3: Make\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Make">edit</a> \| (./index.php.md)\]

Build VASP with

    make DEPS=1 -jN <target>

where ` DEPS=1 -jN` is optional and selects the parallel mode of make
with `N` being the number of jobs you want to run, and `<target>`
corresponds to `std`, `gam`, `ncl` or `all`. This builds the standard,
gamma-only, noncollinear or all versions of VASP. The executables are
`vasp_std`, `vasp_gam`, and `vasp_ncl`, respectively, which are located
at `/path/to/vasp.X.X.X/bin/`.

### Step 4: Test\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 4: Test">edit</a> \| (./index.php.md)\]

Run the [test suite](Validation_tests.md) with

    make test

to confirm the build was successful.

|  |
|----|
| **Tip:** If there are issues, the VASP Forum \[<a href="https://www.vasp.at/forum/viewforum.php?f=2"
class="external text" rel="nofollow">installation issues</a>\] is the appropriate place to seek support. |

|  |
|----|
| **Warning:** VASP.6.1.0, VASP.6.1.1, and VASP.6.1.2 have a potentially serious issue related to the test suite. Please read about it in the [known issues](Validation_tests.md). |

### Step 5: Install\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Step 5: Install">edit</a> \| (./index.php.md)\]

Copy the executables to the system `$PATH` or append
`/path/to/vasp.x.x.x/bin/` to the environment variable with

    export PATH=$PATH:/path/to/vasp.x.x.x/bin

for instance in your `~/.bashrc`. Consider also setting ulimit -s
unlimited and OMP_STACKSIZE=512m before running the program (or put it
in your job script / `~/.bashrc`) to ensure sufficient stack memory for
each OpenMP thread (if [OpenMP
support](Precompiler_options.md) was
activated) and prevent segmentation faults caused by large stack
allocations in the code.

## Install VASP with CMake\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Install VASP with CMake">edit</a> \| (./index.php.md)\]

As an alternative to the <a href="#Install_VASP_with_makefile.include"
class="mw-selflink-fragment">traditional Makefile-based build</a>
system, VASP can also be compiled using the
<a href="https://cmake.org/" class="external text"
rel="nofollow">CMake</a> build infrastructure provided on
<a href="https://github.com/vasp-dev/cmake" class="external text"
rel="nofollow">github.com/vasp-dev/cmake</a>. This method configures the
build automatically detecting compilers and external libraries on the
fly. Requires cmake version 3.24 or later.

### Step 1: Download VASP\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Download VASP">edit</a> \| (./index.php.md)\]

Download the VASP source code from the
<a href="https://vasp.at%7C" class="external text" rel="nofollow">VASP
Portal</a> and unpack:

    tar -xf vasp.X.X.X.tgz
    cd vasp.X.X.X

### Step 2: Download CMake files\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Download CMake files">edit</a> \| (./index.php.md)\]

Next obtain the CMake build infrastructure from our
<a href="https://github.com/vasp-dev/cmake" class="external text"
rel="nofollow">github repository</a>:

    git clone -b 6.6.x https://github.com/vasp-dev/cmake.git

run now the following command to prepare the build system:

    bash cmake/setup.sh

this will create symbolic links of the `CMakeLists.txt` files in the
source directory.

### Step 3: CMake Configure\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: CMake Configure">edit</a> \| (./index.php.md)\]

Create a separate build directory and configure the project using CMake:

    mkdir cmake_build
    cd cmake_build
    cmake /your/vasp/directory \
      -DVASP_OPENMP=ON \
      -DVASP_HDF5=ON

During configuration CMake automatically searches for required
dependencies such as MPI, BLAS/LAPACK, ScaLAPACK, and FFTW. If
necessary, their locations can be provided using standard CMake
variables (e.g. `BLA_VENDOR` for BLAS/LAPACK configuration).

Optional features (e.g. HDF5 support) can be enabled via additional
CMake options, `-DVASP_HDF5=ON` etc. See also the README.md file in the
cmake repository for more details on available options.

### Step 4: Build\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Step 4: Build">edit</a> \| (./index.php.md)\]

Compile VASP using:

    make -jN

where \`N\` is the number of parallel build jobs. This will by default
build all targets. You can specify which VASP version is build via
targets" \`vasp_std\`, \`vasp_gam\`, or \`vasp_ncl\`.

This produces the standard VASP executables (e.g. \`vasp_std\`,
\`vasp_gam\`, and \`vasp_ncl\`) in the build/bin directory.

### Step 5: Test\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Step 5: Test">edit</a> \| (./index.php.md)\]

Run the [test suite](Validation_tests.md) to
verify the installation:

    make test

Note, that cmake will copy the testsuite into the build dir for running
the testsuite.

### Step 6: Install\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Step 6: Install">edit</a> \| (./index.php.md)\]

Optionally install the executables to a chosen location via
\`-DCMAKE_INSTALL_PREFIX\` during configuration, and then run:

    make install

Alternatively, copy the generated executables to a directory included in
your \`\$PATH\`. Consider also setting ulimit -s unlimited and
OMP_STACKSIZE=512m before running the program (or put it in your job
script / `~/.bashrc`) to ensure sufficient stack memory for each OpenMP
thread (if [OpenMP
support](Precompiler_options.md) was
activated) and prevent segmentation faults caused by large stack
allocations in the code.

## Subdirectories in vasp.6.x.x\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Subdirectories in vasp.6.x.x">edit</a> \| (./index.php.md)\]

The build system of VASP (as of versions \>= 5.4.1) comprises the
following subdirectories:

                      vasp.x.x.x (root directory)
                                   |
             ------------------------------------------------
            |        |        |         |          |         |
           arch     bin     build      src     testsuite   tools
                                        |
                                  ----------------------
                                 |      |      |        |       
                                lib   parser  fftlib  vaspml

/path/to/vasp.x.x.x/  
Holds the high-level makefile and several subdirectories.

<!-- -->

/path/to/vasp.x.x.x/src  
Holds the source files of VASP and a low-level makefile.

<!-- -->

/path/to/vasp.x.x.x/src/lib  
Holds the source of the VASP library (used to be vasp.X.lib) and a
low-level makefile.

<!-- -->

/path/to/vasp.x.x.x/src/parser  
Holds the source of the [LOCPROJ](../incar-tags/LOCPROJ.md) parser (as of
versions \>= 5.4.4) and a low-level makefile.

<!-- -->

/path/to/vasp.x.x.x/src/fftlib  
Holds the source of the `fftlib` library that may be used to cache
`fftw` plans.

<!-- -->

/path/to/vasp.x.x.x/src/vaspml  
Holds the source of the [`vaspml`
library](../methods/VASPml_library.md) containing
machine-learning features (versions \>= 6.5.0).

<!-- -->

/path/to/vasp.x.x.x/arch  
Holds a collection of `makefile.include.*` files.

<!-- -->

/path/to/vasp.x.x.x/build  
The different versions of VASP, i.e., the standard, gamma-only,
non-collinear versions will be built in separate subdirectories of this
directory.

<!-- -->

/path/to/vasp.x.x.x/bin  
Here make will store the executables.

<!-- -->

/path/to/vasp.x.x.x/testsuite  
Holds a suite of correctness tests to check your build.

<!-- -->

/path/to/vasp.x.x.x/tools  
Holds several python scripts related to the use of HDF5 input/output
files.

## Validated Toolchains via CI\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Validated Toolchains via CI">edit</a> \| (./index.php.md)\]

Please find on this [toolchains page](Toolchains.md) a
comprehensive guid on which software stacks and versions are validated
by our CI. Makefiles for those validated toolchains can be found in the
arch subdirectory in VASP, or on this [separate
page](Makefile.include.md).

## Install on a common Linux distribution\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Install on a common Linux distribution">edit</a> \| (./index.php.md)\]

If you plan to install VASP on any of the big linux distributions e.g.
Debian, Ubuntu, Fedora, or Rocky Linux, please take a closer look on the
separate page for [Personal computer
installations](Personal_computer_installation.md).
There you also find instructions for Max OS X on M-series chips. For
installation under Windows 11, please use WSL to install one of the
supported distributions first.

## Related sections\[<a
href="/wiki/index.php?title=Installing_VASP.6.X.X&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: Related sections">edit</a> \| (./index.php.md)\]

[Toolchains](Toolchains.md),
[makefile.include](Makefile.include.md),
[Precompiler options](Precompiler_options.md),
[Compiler options](Compiler_options.md), [Linking
to libraries](Linking_to_libraries.md),
[Validation tests](Validation_tests.md), [GPU
ports of VASP](GPU_ports_of_VASP.md)



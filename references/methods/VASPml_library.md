<!-- Source: https://vasp.at/wiki/index.php/VASPml_library | revid: 35680 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VASPml library


VASPml is a C++ library accompanying VASP 6.5.0 and above, providing
functionality related to [machine-learned force
fields](../categories/Category-Machine-learned_force_fields.md).
It is supposed to extend, and eventually replace, the original Fortran
machine learning code inside VASP. Currently, it does not yet offer any
training capabilities but rather focuses on inference. At this point
VASPml is in a beta-testing stage and provides its first application, an
interface to the popular molecular dynamics (MD) software
<a href="https://www.lammps.org" class="external text"
rel="nofollow">LAMMPS</a>. This allows users to combine VASP-generated
machine-learned force fields with the large amount of MD-related
features provided by LAMMPS, some of which may not be offered in VASP
directly.

|  |
|----|
| **Warning:** As of VASP 6.5.0 the VASPml library is experimental and results should be carefully checked against the standard Fortran code (compile without `-Dlibvaspml` or set [`ML_LIB`](../incar-tags/ML_LIB.md)` = .FALSE.`). |


## Contents


- [1 Supported
  features](#supported-features)
- [2
  Restrictions](#restrictions)
- [3
  Dependencies](#dependencies)
- [4 Build
  instructions](#build-instructions)
- [5 Standalone
  build instructions](#standalone-build-instructions)
  - [5.1 Step 1:
    Separate VASPml
    directory](#step-1-separate-vaspml-directory)
  - [5.2 Step 2:
    Modify makefile.include](#step-2-modify-makefileinclude)
  - [5.3 Step 3:
    Build](#step-3-build)
- [6 Internal
  validation tests](#internal-validation-tests)


# Supported features\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Supported features">edit</a> \| (./index.php.md)\]

- [Running machine-learned force fields in
  LAMMPS](Running_machine-learned_force_fields_in_LAMMPS.md)
- Fast prediction-only mode in VASP
  ([`ML_MODE`](../incar-tags/ML_MODE.md)` = run`)

If VASP is compiled with the VASPml library and a requested feature is
supported by both, the original Fortran code **and** the C++ VASPml
implementation, then the latter code path is used by default. To
override this behavior and explicitly avoid the use of the VASPml
library set [`ML_LIB`](../incar-tags/ML_LIB.md)` = .FALSE.` in the
[INCAR](../input-files/INCAR.md) file.

# Restrictions\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Restrictions">edit</a> \| (./index.php.md)\]

Since the VASPml library is still under development some features of the
original Fortran code are not yet available:

- No machine learning related file output (e.g.
  [ML_LOGFILE](../output-files/ML_LOGFILE.md))

|  |
|----|
| **Tip:** For running the fast prediction-only mode in VASP there is currently no performance gain from the VASPml library. Hence, if file output is important (e.g. when monitoring the [spilling factor](Best_practices_for_machine-learned_force_fields.md)) we recommend using the original Fortran code ([`ML_LIB`](../incar-tags/ML_LIB.md)` = .FALSE.`). |

- Thermodynamic integration
  ([ML_LCOUPLE](../incar-tags/ML_LCOUPLE.md))
- Heat flux calculation ([ML_LHEAT](../incar-tags/ML_LHEAT.md))

Due to the experimental nature of the VASPml library some bugs may slip
through our testing. Until VASPml can be considered stable already
identified bugs and workarounds will be collected here:

- VASPml from VASP 6.5.0 is unable to read in
  [ML_FFs](../input-files/ML_FF.md) created with VASP 6.5.0. Force fields
  created from older versions (VASP 6.4.3 and before) work fine (this
  issue will be fixed in VASP 6.5.1). A simple workaround which
  circumvents the broken version check requires a minimal source code
  change: in `/path/to/vasp/src/vaspml/src/libvaspml/IoHandlerML_FF.hpp`
  line 169 increase the maximum allowed [ML_FF](../input-files/ML_FF.md)
  version to 0.2.4:

<table
style="width:100%; table-layout: fixed; border-spacing: 0; padding: 0; margin: 0; background-color: var(--vCB-bg); color: var(--vdefault-text); border-width: 1px; border-style: solid; border-color: var(--vCB-border);">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre
style="margin: 0; padding: 0.5em; background: none; border: none; white-space: pre; overflow-x: auto; font-family: monospace;"><code>    const SemanticVersion versionMax = SemanticVersion(0, 2, 4);</code></pre></td>
</tr>
</tbody>
</table>

After complete recompilation of VASP the newer force fields should also
be accepted. This bug and workaround also apply to the LAMMPS interface.
In case the workaround is applied please also recompile LAMMPS.

- If VASP 6.5.0 is compiled with the VASPml library the [validation
  tests](../misc/Validation_tests.md) for prediction-only
  runs, i.e., all tests labelled `ML_..._ISTART2`, fail because the
  provided [ML_FF](../input-files/ML_FF.md) files are too old. This issue is
  fixed in VASP 6.5.1. Updated tests for
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = run` are work in progress.

# Dependencies\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Dependencies">edit</a> \| (./index.php.md)\]

The VASPml library depends on the following compilers and external
libraries:

- C++ compiler supporting the C++17 language standard
- MPI
- BLAS and the corresponding C interface CBLAS
- LAPACK and the corresponding C interface LAPACKE

These requirements are usually already covered by the [VASP
requirements](../misc/Installing_VASP.6.X.X.md).
Additionally, for compiling the optional [internal validation
tests](#internal-validation-tests) the following external library is
required:

- <a href="http://boost.org/libs/test" class="external text"
  rel="nofollow">Boost.test</a>

# Build instructions\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Build instructions">edit</a> \| (./index.php.md)\]

The VASPml library is automatically built alongside VASP if
`-Dlibvaspml` is added to the `CPP_OPTIONS` [precompiler
option](../misc/Precompiler_options.md) in the
[makefile.include](../misc/Makefile.include.md) file. In
addition, a few more compiler settings regarding the C++ compiler,
include paths and VASPml options may be required. The [makefile.include
templates](../misc/Makefile.include.md)
provided in VASP's `arch` directory contain pre-filled blocks
corresponding to the VASPml build. Uncomment the VASPml-related lines
and fill with values according to your
[toolchain](../misc/Toolchains.md). For example, when using the
GCC toolchain with OpenBLAS the makefile.include section may look like
this:

    ...
    # For machine learning library vaspml (experimental)
    CPP_OPTIONS += -Dlibvaspml
    CPP_OPTIONS += -DVASPML_USE_CBLAS
    #CPP_OPTIONS += -DVASPML_DEBUG_LEVEL=3
    CXX_ML      = mpic++
    CXXFLAGS_ML = -O3 -std=c++17 -pedantic-errors -Wall -Wextra
    INCLUDE_ML  = -I$(OPENBLAS_ROOT)/include
    ...

Apart from the mandatory `-Dlibvaspml` flag there are the following
possible `CPP_OPTIONS`:

- `-DVASPML_USE_CBLAS`: Use CBLAS (C interface for BLAS routines) for
  linear algebra. This is the default and should always be used.
- `-DVASPML_DEBUG_LEVEL=[0|1|2|3]`: If set to 1, 2 or 3 enables various
  sanity checks during runtime with low, medium and high impact on
  performance, respectively. Setting it to 0 or omitting the flag
  disables runtime checks.

|  |
|----|
| **Mind:** Do not use this flag for production runs as it may decrease performance. |

- `-DVASPML_USE_MKL`: Use Intel MKL for linear algebra (must be used in
  combination with `-DVASPML_USE_CBLAS`).

In addition, VASPml requires to set its own compiler, flags and include
path:

- `CXX_ML`: This should be a C++17-compatible C++ compiler with MPI
  support (usually an MPI wrapper corresponding to the selected
  toolchain, e.g. `mpic++`, `mpicxx`, `mpicpx` or `mpinc++`).
- `CXXFLAGS_ML`: Specifies the flags for the C++ compiler. Typically,
  here the optimization level (`-O3`) and the compliance with C++17 is
  specified.
- `INCLUDE_ML`: Include flags for the required dependencies should be
  added here.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vblue); --box-emph-color: var(--vblue); padding: 5px; color: var(--vdefault-text-nb); background: var(--vblue-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vblue);">Tip:</span></strong> For
some <a href="/wiki/Toolchains" title="Toolchains">toolchains</a> it is
not necessary to explicitly add paths here because the compilers
automatically include the correct directories (e.g. Intel oneAPI,
NVHPC). In other cases (e.g. GNU compiler with openBLAS) the given path
must contain the desired C++ headers of the dependencies:
<ul>
<li>CBLAS: <code>cblas.h</code></li>
<li>LAPACKE: <code>lapacke.h</code></li>
</ul></td>
</tr>
</tbody>
</table>

The VASPml project (source code and related files) is located within the
`src/vaspml` directory relative to the VASP root folder. Upon
compilation it is copied to the `build/std`, `build/gam` and/or
`build/ncl` build folders, just like all other VASP sources. If the
VASPml library was successfully compiled `libvaspml.a` will be located
in `build/std/vaspml/lib/` (similarly for the `gam` and `ncl` versions).
However, it is usually not necessary to check its presence because the
VASP build will handle this (and fail if VASPml cannot be built).

# Standalone build instructions\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Standalone build instructions">edit</a> \| (./index.php.md)\]

Although VASPml is typically part of the VASP build process as described
above it is also possible to compile it independently. This can be
useful, for example, if VASP is deliberately compiled without VASPml but
the `libvaspml` library is still necessary to build [LAMMPS with VASPml
patch](Running_machine-learned_force_fields_in_LAMMPS.md).
For a standalone build of VASPml follow these steps:

### Step 1: Separate VASPml directory\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Separate VASPml directory">edit</a> \| (./index.php.md)\]

First, copy the entire `vaspml` subdirectory to a separate location and
move into the new `vaspml` directory:

    cp -r /path/to/vasp/src/vaspml /some/other/location/
    cd /some/other/location/vaspml

Inside you will find a similar folder structure as in VASP. For example,
the source code is located in `src` and will be copied and compiled in
the `build` directory. Moreover, also VASPml requires to enter compiler
details and library paths into a file named `makefile.include` before
the standalone build process can be started. The `arch` folder contains
template files for typical compiler toolchains.

|  |
|----|
| **Mind:** The `makefile.include` files inside VASPml's `arch` directory are only required for the standalone build described here. For a regular VASP build they must not be used because then compilers and flags are taken from VASP's `makefile.include` (for this purpose, the special file `makefile.include.vasp` is used **automatically**). |

### Step 2: Modify `makefile.include`\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Modify makefile.include">edit</a> \| (./index.php.md)\]

Pick one of the `makefile.include` files in the `arch` folder which is
closest to your toolchain and copy it to the base directory, e.g.

    cp arch/makefile.include.gnu makefile.include

Next, modify the file according to your actual compiler and library
paths. The most important variables here have a counterpart in VASP's
`makefile.include`, please also review the [regular VASP build
instructions](#build-instructions) for details:

- `CXX`: C++17-compatible C++ compiler with MPI support, corresponds to
  `CXX_ML` in VASP's `makefile.include`.
- `CXXFLAGS`: Flags for the C++ compiler, corresponds to `CXXFLAGS_ML` +
  `VASP_TARGET_CPU` in VASP's `makefile.include`.
- `INCLUDE`: Include flags for the required dependencies, corresponds to
  `INCLUDE_ML` in VASP's `makefile.include`.
- `CPP_OPTIONS`: Specific build options, same as in [VASP's
  `makefile.include`](../misc/Precompiler_options.md).
  Only options starting with `-DVASPML_` are relevant. Do not use any of
  `-DMPI -D_OPENMP -DHOST` here as this may result in a compile error.

Usually, these are all the variables requiring changes for a successful
standalone build of the VASPml library and you may now proceed with step
3 below. However, for more fine-grained control and other purposes, like
the [internal validation tests](#internal-validation-tests), it may be
necessary to review also the remaining variables in the template files:

- `LD`: Specifies the linker to use when building applications linked to
  `libvaspml`. Usually the same as the compiler `CXX`.
- `LDFLAGS`: Flags in addition to `CXXFLAGS` to pass to the linker. This
  is where the flags for BLAS and LAPACK are added.
- `CPP_DEP`: Dependency generator, usually the same as the compiler
  `CXX`.
- `AR`: Executable generating archives ("\*.a" files) from multiple
  object files. Used to generate the static library `libvaspml.a` from
  the compiled object files.
- `ARFLAGS`: Flags passed to the archiver `AR`.

Some additional variables are only used when the [internal validation
tests of VASPml](#internal-validation-tests) are compiled and executed:

- `BOOST_ROOT`: If not already defined via a shell environment variable,
  you may specify the base path to the Boost.test library here.
- `BOOST_INCLUDE`: Include directory for Boost.test library (must
  contain the files `boost/test/unit_test.hpp`,
  `boost/test/data/test_case.hpp` and
  `boost/test/data/monomorphic.hpp`).
- `BOOST_LIB`: Flags required for linking the Boost.test library
  `libboost_unit_test_framework`.

Finally, the screen output during the build process can be influenced
with the following flags:

- `MAKE_OPTIONS`: Here we can add multiple special options to configure
  the screen output:
  - `--no-color`: Disables colored output of makefiles.
  - `--no-logo`: Disables the VASPml logo output.

For example, to disable both the color output and the logo use:
`MAKE_OPTIONS = --no-color --no-logo`.

- `VERBOSE`: Setting this to any value, e.g. `VERBOSE=1`, will echo all
  executed commands to the screen.

### Step 3: Build\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Build">edit</a> \| (./index.php.md)\]

After modifying the `makefile.include` file we can finally build the
VASPml library by executing

    make libvaspml

In order to parallelize the build process it is possible to add the `-j`
flag. The library will be located in `lib/libvaspml.a`. To completely
remove all compiled files and build folders you may use `make clean`.

# Internal validation tests\[<a
href="/wiki/index.php?title=VASPml_library&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Internal validation tests">edit</a> \| (./index.php.md)\]

VASPml comes with its own set of tests (unit tests, integration tests,
regression tests) to validate the correctness of the build. They are
located in the `test` subfolder relative to the base directory.

|  |
|----|
| **Mind:** Currently, the VASPml internal tests are not executed as part of the [VASP validation tests](../misc/Validation_tests.md). They can only be built and executed with a [standalone build of VASPml](#standalone-build-instructions). |

In addition to the regular dependencies of VASPml (CBLAS, LAPACKE) the
tests require the external library
<a href="http://boost.org/libs/test" class="external text"
rel="nofollow">Boost.test</a> to be present on your system. The
corresponding include and linking flags must be added to the
`BOOST_INCLUDE` and `BOOST_LIB` variables in the `makefile.include` file
(see [step 2](#step-2-modify-makefileinclude) above). Before
continuing please make sure the VASPml library was correctly built. To
build and execute the tests change to the `test` directory and run
`make`:

    cd test
    make

Optionally, use the `-j` flag to parallelize the build process. The
`make` command will first build multiple test binaries which will then
be executed sequentially. Each binary may execute multiple tests which
is summarized on the screen like this:

    Running test executable                                                        ====>                         test_TypeMap.x
    Running 2 test cases...
    Entering test module "TypeMap"
    test_TypeMap.cpp(16): Entering test suite "UnitTests"
    test_TypeMap.cpp(18): Entering test case "RandomOrderMapping_CorrectMapping"
    test_TypeMap.cpp(18): Leaving test case "RandomOrderMapping_CorrectMapping"; testing time: 169us
    test_TypeMap.cpp(65): Entering test case "IllegalTypeCombination_ThrowError"
    test_TypeMap.cpp(65): Leaving test case "IllegalTypeCombination_ThrowError"; testing time: 145us
    test_TypeMap.cpp(16): Leaving test suite "UnitTests"; testing time: 340us
    Leaving test module "TypeMap"; testing time: 353us

    *** No errors detected

The message
**`*** No errors detected`** should
be present for all test binaries. If this is not the case, please file a
bug report with the error message, your `makefile.include` and a
description of your toolchain to the
<a href="https://www.vasp.at/forum/" class="external text"
rel="nofollow">VASP forum</a>, thank you! The `test` directory can be
cleaned up from binaries and build folders with the `make clean`
command.



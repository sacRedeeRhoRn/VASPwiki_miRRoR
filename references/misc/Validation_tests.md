<!-- Source: https://vasp.at/wiki/index.php/Validation_tests | revid: 34982 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Validation tests


As of VASP.6.1.0, each release contains a testsuite for validation.

|  |
|----|
| **Warning:** VASP.6.1.0, VASP.6.1.1, and VASP.6.1.2 have a potentially serious issue related to the test suite. Please read about it <a href="#Known_issues" class="mw-selflink-fragment">here</a>. |


## Contents


- [1
  Testsuite](#testsuite)
- [2 Running the
  tests](#running-the-tests)
  - [2.1 Run the
    tests with make
    (recommended)](#run-the-tests-with-make-recommended))
  - [2.2
    Configuring the testsuite
    manually](#configuring-the-testsuite-manually)
    - [2.2.1
      Categories](#categories)
  - [2.3 Directly
    execute the runtest
    script](#directly-execute-the-runtest-script)
    - [2.3.1
      Configuration
      templates](#configuration-templates)
- [3 The output of
  the tests](#the-output-of-the-tests)
- [4 What if tests
  fail](#what-if-tests-fail)
- [5 Known
  issues](#known-issues)
- [6 Related
  Sections](#related-sections)


## Testsuite\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Testsuite">edit</a> \| (./index.php.md)\]

The VASP testsuite is located in \`root/testsuite\` where \`root\` is
the root directory of the build system.

                            vasp.X.X.X (root directory)
                                     |
             ----------------------------------------------
            |              |            |          |       |
           arch           bin       testsuite     build    src
                                        |
                         ------------------------------------------
                        |      |         |         |        |      |
                      tests  README.md  tools   POTCARS  runtest makefile
                        |           
               ------------------   
              |      |           |   
            test1  test2  ...  testN

testsuite/  
Testsuite root directory. Holds several subdirectories and the main
bash-script `runtest` that runs the tests and validates the results.

<!-- -->

testsuite/tests  
Holds a whole bunch of subdirectories that in turn contain the input
files ([INCAR](../input-files/INCAR.md)`.?.*`,
[KPOINTS](../input-files/KPOINTS.md), and
[POSCAR](../input-files/POSCAR.md)), and reference output
([OUTCAR](../output-files/OUTCAR.md)`.ref`,
[OSZICAR](../output-files/OSZICAR.md)`.ref` etc.) for the test
calculations.

<!-- -->

testsuite/POTCARS  
Holds the [POTCAR](../input-files/POTCAR.md) files (potentials), one for
each individual test calculation. The naming convention for these files
is:

    POTCAR.name-of-test-subdirectory

<!-- -->

testsuite/tools  
Contains a bash-script (`call_compare`) and a Fortran source file
(`compare_numbertable_new.f90`). The latter is compiled as:

    $(FC) -o compare_numbertable_new compare_numbertable_new.f90

where the `$(FC)` is the Fortran compiler binary path that has to be set
in `root/makefile.include` (see the [compiler variables section of
Installing
VASP](Installing_VASP.6.X.X.md)).

<!-- -->

testsuite/runtest  
Main execution script that orchestrates which tests are executed based
on set environment variables.

<!-- -->

testsuite/makefile  
Autoconf makefile containing some simple rules that either compile
`compare_numbertable_new.f90` (`make numbertable`), execute a small
selection of tests (`make test`) or execute all test (`make test_all`).

  

## Running the tests\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Running the tests">edit</a> \| (./index.php.md)\]

### Run the tests with `make` (recommended)\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Run the tests with make (recommended)">edit</a> \| (./index.php.md)")\]

------------------------------------------------------------------------

After building the `vasp_std`, `vasp_gam`, and `vasp_ncl` executables
(e.g. by means of `make all`), you can test your build by means of:

    make test

(either in `root` or `root/testsuite`). The above will run a subset of
tests from the testsuite (the so-called `FAST` category of tests) that
will take roughly 1.5 hours to complete on 4 cores.

The full testsuite may be executed by means of:

    make test_all

The output of the tests (`stdout+stderr`) is written to
`root/testsuite/testsuite.log`.

Tests that fail write an `ERROR` to `root/testsuite/testsuite.log` and
the tests that were not passed successfully will be listed at the end of
this file (and `make` will exit in error).

To clean up after running the testsuite, execute:

    make cleantest

in `root/testsuite`.

  

### Configuring the testsuite manually\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Configuring the testsuite manually">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

Configured the testsuite by setting several environment variables (with
the naming convention: `VASP_TESTSUITE_*`).

- `VASP_TESTSUITE_EXE_STD`:

The command that runs the standard version of VASP.

Default:

    VASP_TESTSUITE_EXE_STD="mpirun -np 4 root/bin/vasp_std"

**N.B.**: Specify the absolute path your *standard* executable (e.g.
`vasp_std` or `vasp_gpu`).

- `VASP_TESTSUITE_EXE_GAM`:

The command that runs the gamma-only version of VASP.

Default:

    VASP_TESTSUITE_EXE_GAM="mpirun -np 4 root/bin/vasp_gam"

**N.B.**: Specify the absolute path to your *gamma-only* executable
(e.g. `vasp_gam`).

- `VASP_TESTSUITE_EXE_NCL`:

The command that runs the non-collinear version of VASP.

Default:

    VASP_TESTSUITE_EXE_NCL="mpirun -np 4 root/bin/vasp_ncl"

**N.B.**: Specify the absolute path to your *non-collinear* executable
(e.g. `vasp_ncl` or `vasp_gpu_ncl`).

- `VASP_TESTSUITE_CUDA`:

Set `VASP_TESTSUITE_CUDA=Y` to exclude all tests that can not be
executed with the CUDA-GPU port of VASP.

Default:

    VASP_TESTSUITE_CUDA=

- `VASP_TESTSUITE_INCAR_PREPEND`:

Additional INCAR tags used for every execution of VASP in the testsuite.

Default:

    VASP_TESTSUITE_INCAR_PREPEND=

- `VASP_TESTSUITE_TESTS`:

Selection of tests to be executed.

Default:

    VASP_TESTSUITE_TESTS=

**N.B.**: A convenient way to execute a specific test is to set
`VASP_TESTSUITE_TESTS` to a particular test, e.g. by means of:

    export VASP_TESTSUITE_TESTS="bulk_GaAs_ACFDT"

and to run `make test` from the `root` or `root/testsuite` directory.

- `VASP_TESTSUITE_SKIP_TESTS`:

Selection of tests to be skipped.

Default:

    VASP_TESTSUITE_SKIP_TESTS=

- `VASP_TESTSUITE_POTENTIALS`:

Path to the POTCAR files.

Default:

    VASP_TESTSUITE_POTENTIALS=root/testsuite/POTCARS

  

#### Categories\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Categories">edit</a> \| (./index.php.md)\]

A variety of environment variables can be set to run or exclude tests
belonging to specific categories. Default: not set

For instance:

- `VASP_TESTSUITE_SKIP_LREAL`:

Skips all tests that use the real space PAW projection scheme
([LREAL](../incar-tags/LREAL.md)`/=F`) if set to: `Y`, i.e.,

    export VASP_TESTSUITE_SKIP_LREAL=Y

or

- `VASP_TESTSUITE_RUN_LREAL`:

Runs only tests that use the real space PAW projection scheme
([LREAL](../incar-tags/LREAL.md)`=A` or
[LREAL](../incar-tags/LREAL.md)`=.TRUE.`) if set to: `Y`.

    export VASP_TESTSUITE_RUN_LREAL=Y

The following variables may be set to skip categories of tests:

- `VASP_TESTSUITE_SKIP_NOCUDA`:

Skip all tests that can not be excuted with the CUDA-GPU port.

- `VASP_TESTSUITE_SKIP_HYB`:

Skip all hybrid functional tests.

- `VASP_TESTSUITE_SKIP_GAMMA`:

Skip all tests of the gamma-only version.

- `VASP_TESTSUITE_SKIP_NCL`:

Skip all tests of the non-collinear version.

- `VASP_TESTSUITE_SKIP_SOC`:

Skip all tests involving Spin-Orbit Coupling.

- `VASP_TESTSUITE_SKIP_MD`:

Skip all Molecular Dynamics tests.

- `VASP_TESTSUITE_SKIP_TBMD`:

Skip all constrained molecular dynamics tests.

- `VASP_TESTSUITE_SKIP_RPA`:

Skip all tests that involve the Random-Phase Approximation (GW and
ACFDT).

- `VASP_TESTSUITE_SKIP_GW`:

Skip all GW tests.

- `VASP_TESTSUITE_SKIP_ACFDT`:

Skip all ACFDT tests.

- `VASP_TESTSUITE_SKIP_CRPA`:

Skip all tests of the Constrained-RPA.

- `VASP_TESTSUITE_SKIP_BSE`:

Skip all Bethe-Salpeter-Equation tests.

- `VASP_TESTSUITE_SKIP_NOSYM`:

Skip all tests that do not use symmetry.

- `VASP_TESTSUITE_SKIP_LREAL`:

Skip all tests that use the real-space PAW projection scheme.

- `VASP_TESTSUITE_SKIP_LRESP`:

Skip all linear response tests.

- `VASP_TESTSUITE_SKIP_PEAD`:

Skip all tests that use the PEAD method.

- `VASP_TESTSUITE_SKIP_NCORE1`:

Skip all tests that may only be executed with
[NCORE](../incar-tags/NCORE.md)`=1`.

- `VASP_TESTSUITE_SKIP_WAN90`:

Skip all tests that need to execute `wannier90`.

  
The following variables may be set to run only tests that belong to a
specific category (or categories):

- `VASP_TESTSUITE_RUN_HYB`
- `VASP_TESTSUITE_RUN_GAMMA`
- `VASP_TESTSUITE_RUN_NCL`
- `VASP_TESTSUITE_RUN_SOC`
- `VASP_TESTSUITE_RUN_MD`
- `VASP_TESTSUITE_RUN_TBMD`
- `VASP_TESTSUITE_RUN_RPA`
- `VASP_TESTSUITE_RUN_GW`
- `VASP_TESTSUITE_RUN_ACFDT`
- `VASP_TESTSUITE_RUN_CRPA`
- `VASP_TESTSUITE_RUN_BSE`
- `VASP_TESTSUITE_RUN_NOSYM`
- `VASP_TESTSUITE_RUN_LREAL`
- `VASP_TESTSUITE_RUN_FAST`
- `VASP_TESTSUITE_RUN_LRESP`
- `VASP_TESTSUITE_RUN_PEAD`
- `VASP_TESTSUITE_RUN_NCORE1`
- `VASP_TESTSUITE_RUN_WAN90`

### Directly execute the `runtest` script\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Directly execute the runtest script">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

Besides by means of `make` the testsuite may be invoked by executing the
`root/testsuite/runtest` script directly. There are two ways to execute
the `runtest` script:

1\. Change into the `root/testsuite` directory and run the tests in the
`FAST` category by means of:

    ./runtest -f

or ALL tests with

    ./runtest -a

2\. Change into `root/testsuite`, adapt one of the example configuration
files in `root/testsuite` and run the testsuite with:

    ./runtest your-config-file

**N.B.I**: To pipe the full output to a file (`testsuite.log`) add
`> testsuite.log 2>&1` to the commands above.

**N.B.II**: We maintain
<a href="#Configuration_templates" class="mw-selflink-fragment">a small
collection of configuration templates</a>.

**N.B.III**: When you want to run the testsuite by executing the
`runtest` directly you will *first* have to build the
`compare_numbertable_new` utility, by means of:

    make numbertable

(in `root/testsuite`).

For each test that fails `runtest` writes an `ERROR` to `stdout` and the
tests that were not passed successfully will be listed at the end of the
run.

In case of a successful run, `runtest` script will exit with error code
0 (indicates successful exit on Unix-based OS), otherwise the error code
1 is returned.

  

#### Configuration templates\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Configuration templates">edit</a> \| (./index.php.md)\]

The following configuration files are to be seen as templates to help
you construct your own:

<u>*General*</u>

- [all.conf](All.conf.md) : runs all tests
- [fast.conf](Fast.conf.md): runs the `FAST` category of
  tests

<u>*Running with MPI + OpenMP*</u>

- [impi+omp.conf](Impi+omp.conf.md): for OpenMP +
  Intel-MPI
- [ompi+omp.conf](Ompi+omp.conf.md): for OpenMP +
  OpenMPI

<u>*To test the CUDA-GPU executables*</u>

- [cuda.conf](Cuda.conf.md)

**N.B.**: these configuration files are sourced by the `runtest`
bash-script. In principle they only set (`export`) some environment
variables. Setting these environment variables by hand and invoking
`make test` (or `make test_all`) amount to the same as running these
configuration files with `runtest`.

  

## The output of the tests\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: The output of the tests">edit</a> \| (./index.php.md)\]

If one runs the tests by means of `make`, as recommended
<a href="#Run_the_tests_with_make_.28recommended.29"
class="mw-selflink-fragment">above</a> all output (`stdout+stderr`) will
be written to `root/testsuite/testsuite.log`.

Tests that fail write an `ERROR` to `root/testsuite/testsuite.log` and
the tests that were not passed successfully will be listed at the end of
this file (and `make` will exit in error).

  

## What if tests fail\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: What if tests fail">edit</a> \| (./index.php.md)\]

We have successfully run the testsuite (on 1, 2, 4, 6, and 8 MPI-ranks)
using executables built with [various
toolchains](Toolchains.md).

When you run into trouble, *i.e.*, your testsuite runs report failing
tests, we'd ask you to reproduce these errors with one of the
aforementioned [toolchains](Toolchains.md) if possible.
If your problems persist with a validated toolchain or you have no
access to any of these toolchains, please submit a bug report to the
<a href="https://www.vasp.at/forum" class="external text"
rel="nofollow">VASP-forum</a> and we will look into the matter.

**N.B.**: This bug report should contain all information we need to try
to reproduce the problem: a list of the compilers and libraries you have
used to build VASP and the logfile with the `stdout+stderr` output of
your testsuite run. Please keep the other output
([OUTCAR](../output-files/OUTCAR.md) files. etc) of your failing tests as
well since we might need to inspect these in addition to the logfile in
the course of trying to solve your problem.

## Known issues\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Known issues">edit</a> \| (./index.php.md)\]

The testsuite scripts in vasp.6.1.0, vasp.6.1.1 and vasp.6.1.2 releases
have a potentially serious issue that can lead to loss of user data
unrelated to vasp in the home directory! This issue has yet been only
observed on MacOS and BSD systems, but might affect other OS as well.
Avoid to use

    make test
    make test_all
    make cleantest

or the use of any script called

    cleanall 

on MacOS or BSD systems (and potentially other OS) until we release a
fix.

This script is used to clean the files produced by VASP after running
the test suite. The `readlink` and `dirname` commands take different
arguments on Linux and BSD systems including macOS. On BSD systems this
results in the `$dir` variable becoming empty, `cd` to the home folder
and removing ALL files recursively that do not match the pre-defined
patterns.

## Related Sections\[<a
href="/wiki/index.php?title=Validation_tests&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Related Sections">edit</a> \| (./index.php.md)\]

[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md)

------------------------------------------------------------------------



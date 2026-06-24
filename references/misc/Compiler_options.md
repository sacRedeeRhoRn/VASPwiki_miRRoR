<!-- Source: https://vasp.at/wiki/index.php/Compiler_options | revid: 34710 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Compiler options
The compiler options are specified by compiler variables that set the
compiler and compiler flags. The Fortran compiler will then be invoked
as:

    $(FC) $(FREE) $(FFLAGS) $(OFLAG) $(INCS)

## Contents

- [1 Compiler variables](#Compiler_variables)
  - [1.1 FC](#FC)
  - [1.2 FCL](#FCL)
  - [1.3 OFLAG](#OFLAG)
  - [1.4 FFLAGS](#FFLAGS)
  - [1.5 OFLAG_IN](#OFLAG_IN)
  - [1.6 DEBUG](#DEBUG)
  - [1.7 INCS](#INCS)
  - [1.8 FREE](#FREE)
  - [1.9 MPI + OpenMP parallelization](#MPI_+_OpenMP_parallelization)
- [2 Special rules](#Special_rules)
  - [2.1 FFLAGS_x](#FFLAGS_x)
  - [2.2 OFLAG_x](#OFLAG_x)
  - [2.3 INCS_x](#INCS_x)
  - [2.4 Related articles](#Related_articles)

# Compiler variables
### FC
The command to invoke your Fortran compiler (e.g. `gfortran`, `ifort`,
`mpif90`, `mpiifort`, ... ).

### FCL
The command that invokes the linker. In most cases:

    FCL=$(FC) [+ some options]

### OFLAG
The general level of optimization (default: `OFLAG=-O2`).

### FFLAGS
Additional compiler flags. To enable debugging, for instance, the
following line could be added:

    FFLAGS+=-g 

### OFLAG_IN
(default: `-O2`) In the vast majority of `makefile.include` files this
variable is set:

    OFLAG_IN=$(OFLAG)

### DEBUG
The optimization level with which the main program (main.F) will be
compiled, usually:

    DEBUG=-O0

### INCS
Use this variable to specify objects to be included in the sense of:

    INCS=-I/path/to/directory-with-files-to-be-included

### FREE
Specify the options that your Fortran compiler needs for it to accept
free-form source layout, without line-length limitation. For instance:

- Using Intel's Fortran compiler:

&nbsp;

    FREE=-free -names lowercase

- Using gfortran:

&nbsp;

    FREE=-ffree-form -ffree-line-length-none

## MPI + OpenMP parallelization
To compile VASP with OpenMP support, add the following to the list of
[precompiler
flags](Installing_VASP.6.X.X.md)
in your `makefile.include` file:

    CPP_OPTIONS += -D_OPENMP

In addition, you will have to add some compiler-specific options to the
command that invokes your Fortran compiler (and sometimes to the linker
as well).

When using an Intel toolchain (ifort + Intel MPI), for instance:

    FC = mpiifort -qopenmp

# Special rules
The current `src/makefile` contains a set of recipes to allow for the
compilation of objects at different levels of optimization other than
the general level specified by `OFLAG`. In these recipes, the compiler
will be invoked as:

    $(FC) $(FREE) $(FFLAGS_x) $(OFLAG_x) $(INCS_x) 

where `x` stands for: 1, 2, 3, or IN.

### FFLAGS_x
Default: `FFLAGS_x=$(FFLAGS)`, for x=1, 2, 3, and IN.

### OFLAG_x
Default: `OFLAG_x=-Ox` (for x=1, 2, 3), and `OFLAG_IN=-O2`

### INCS_x
Default: `INCS_x=$(INCS)`, for x=1, 2, 3, and IN.

The objects to be compiled in accordance with these recipes have to be
specified by means of the variables: `OBJECTS_O1`, `OBJECTS_O2`,
`OBJECTS_O3`, `OBJECTS_IN`

Several objects are compiled at `-O1` and `-O2` by default. These lists
of objects are specified in the **/path/to/vasp.X.X.X/src/.objects**
file through the variables: `SOURCE_O1`, `SOURCE_O2`, `SOURCE_IN`.

To completely overrule a default setting (for instance for the `-O1`
special rules) you can use the following construct:

    SOURCE_O1  =
    OBJECTS_O1 = .. your list of objects ..

## Related articles
[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md),
[makefile.include](Makefile.include.md),
[Precompiler options](Precompiler_options.md),
[Linking to
libraries](Linking_to_libraries.md), [GPU
ports of VASP](GPU_ports_of_VASP.md),
[Toolchains](Toolchains.md), [Validation
tests](Validation_tests.md), [Known
issues](Known_issues.md)

------------------------------------------------------------------------

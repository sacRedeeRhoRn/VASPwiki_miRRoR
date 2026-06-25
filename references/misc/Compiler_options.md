<!-- Source: https://vasp.at/wiki/index.php/Compiler_options | revid: 34710 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Compiler options


The compiler options are specified by compiler variables that set the
compiler and compiler flags. The Fortran compiler will then be invoked
as:

    $(FC) $(FREE) $(FFLAGS) $(OFLAG) $(INCS)


## Contents


- [1 Compiler
  variables](#compiler-variables)
  - [1.1
    FC](#fc)
  - [1.2
    FCL](#fcl)
  - [1.3
    OFLAG](#oflag)
  - [1.4
    FFLAGS](#fflags)
  - [1.5
    OFLAG_IN](#OFLAG_IN)
  - [1.6
    DEBUG](#debug)
  - [1.7
    INCS](#incs)
  - [1.8
    FREE](#free)
  - [1.9 MPI +
    OpenMP parallelization](#MPI_+_OpenMP_parallelization)
- [2 Special
  rules](#special-rules)
  - [2.1
    FFLAGS_x](#FFLAGS_x)
  - [2.2
    OFLAG_x](#OFLAG_x)
  - [2.3
    INCS_x](#INCS_x)
  - [2.4 Related
    articles](#related-articles)


# Compiler variables\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Compiler variables">edit</a> | (./index.php.md)\]

### FC\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: FC">edit</a> | (./index.php.md)\]

The command to invoke your Fortran compiler (e.g. `gfortran`, `ifort`,
`mpif90`, `mpiifort`, ... ).

### FCL\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: FCL">edit</a> | (./index.php.md)\]

The command that invokes the linker. In most cases:

    FCL=$(FC) [+ some options]

### OFLAG\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: OFLAG">edit</a> \| (./index.php.md)\]

The general level of optimization (default: `OFLAG=-O2`).

### FFLAGS\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: FFLAGS">edit</a> \| (./index.php.md)\]

Additional compiler flags. To enable debugging, for instance, the
following line could be added:

    FFLAGS+=-g 

### OFLAG_IN\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: OFLAG_IN">edit</a> \| (./index.php.md)\]

(default: `-O2`) In the vast majority of `makefile.include` files this
variable is set:

    OFLAG_IN=$(OFLAG)

### DEBUG\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: DEBUG">edit</a> | (./index.php.md)\]

The optimization level with which the main program (main.F) will be
compiled, usually:

    DEBUG=-O0

### INCS\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: INCS">edit</a> | (./index.php.md)\]

Use this variable to specify objects to be included in the sense of:

    INCS=-I/path/to/directory-with-files-to-be-included

### FREE\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: FREE">edit</a> | (./index.php.md)\]

Specify the options that your Fortran compiler needs for it to accept
free-form source layout, without line-length limitation. For instance:

- Using Intel's Fortran compiler:

<!-- -->

    FREE=-free -names lowercase

- Using gfortran:

<!-- -->

    FREE=-ffree-form -ffree-line-length-none

## MPI + OpenMP parallelization\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: MPI + OpenMP parallelization">edit</a> | (./index.php.md)\]

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

# Special rules\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Special rules">edit</a> | (./index.php.md)\]

The current `src/makefile` contains a set of recipes to allow for the
compilation of objects at different levels of optimization other than
the general level specified by `OFLAG`. In these recipes, the compiler
will be invoked as:

    $(FC) $(FREE) $(FFLAGS_x) $(OFLAG_x) $(INCS_x) 

where `x` stands for: 1, 2, 3, or IN.

### FFLAGS_x\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: FFLAGS_x">edit</a> \| (./index.php.md)\]

Default: `FFLAGS_x=$(FFLAGS)`, for x=1, 2, 3, and IN.

### OFLAG_x\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: OFLAG_x">edit</a> | (./index.php.md)\]

Default: `OFLAG_x=-Ox` (for x=1, 2, 3), and `OFLAG_IN=-O2`

### INCS_x\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: INCS_x">edit</a> | (./index.php.md)\]

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

## Related articles\[<a
href="/wiki/index.php?title=Compiler_options&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Related articles">edit</a> \| (./index.php.md)\]

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



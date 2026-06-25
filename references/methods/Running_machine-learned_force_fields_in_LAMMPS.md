<!-- Source: https://vasp.at/wiki/index.php/Running_machine-learned_force_fields_in_LAMMPS | revid: 35682 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Running machine-learned force fields in LAMMPS


<a href="https://www.lammps.org" class="external text"
rel="nofollow">LAMMPS</a> is a very popular molecular dynamics (MD)
package which implements lots of advanced simulation methods. Although
VASP itself also offers [MD
simulations](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
LAMMPS provides more flexibility and additional methods (e.g.
thermostats/barostats, grouping atoms, etc.). This page describes how to
make pre-trained VASP machine-learned force fields available within
LAMMPS. On a technical level this is achieved by patching the LAMMPS
source code in such way that a new
<a href="https://docs.lammps.org/pair_style.html" class="external text"
rel="nofollow"><code>pair_style</code></a> named `vasp` is available in
the LAMMPS script language. The patched LAMMPS source is compiled and
then linked to the [VASPml
library](VASPml_library.md). The first section
describes in detail how to patch and compile LAMMPS. The second section
explains how the VASP [ML_FF](../input-files/ML_FF.md) file can be loaded in
a LAMMPS script.

|  |
|----|
| **Warning:** The VASPml library available as of VASP 6.5.0 and therefore also the LAMMPS interface are experimental features. Please carefully check results and, if feasible, compare against similar VASP MD simulations. |


## Contents


- [1 Building
  LAMMPS with VASPml patch](#building-lammps-with-vaspml-patch)
  - [1.1 Using
    traditional make (only for VASP
    6.5.X)](#using-traditional-make-only-for-vasp-65x))
  - [1.2 Using
    CMake (VASP 6.6.0 and
    later)](#using-cmake-vasp-660-and-later))
- [2 Setting up a
  LAMMPS MD run](#setting-up-a-lammps-md-run)


# Building LAMMPS with VASPml patch\[<a
href="/wiki/index.php?title=Running_machine-learned_force_fields_in_LAMMPS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Building LAMMPS with VASPml patch">edit</a> \| (./index.php.md)\]

The LAMMPS packages offers two distinct build pathways: via
<a href="https://cmake.org/" class="external text"
rel="nofollow">CMake</a> or via traditional makefiles. While the latter
was available at the time of the first VASPml release in VASP 6.5.0, it
since has been slowly phased out. Hence, starting with VASP 6.6.0
building LAMMPS with VASPml patch is only supported via CMake.

## Using traditional make (only for VASP 6.5.X)\[<a
href="/wiki/index.php?title=Running_machine-learned_force_fields_in_LAMMPS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Using traditional make (only for VASP 6.5.X)">edit</a> \| (./index.php.md)")\]

Before starting the LAMMPS build please either compile [VASP with the
VASPml
library](../misc/Makefile.include.md) "Makefile.include"),
or alternatively, keep your VASP installation untouched and perform a
[standalone
build](VASPml_library.md)
of the VASPml library. To confirm that everything is ready we can check
for the presence of the following files:

- For a VASP build with VASPml:
  - `/path/to/vasp/build/VERSION/vaspml/lib/libvaspml.a`
  - `/path/to/vasp/build/VERSION/vaspml/include/InterfaceLAMMPS.hpp`

where `VERSION` is any of `std`, `gam` or `ncl`. It does not matter
which VASP build version is used because the VASPml library will be
identical in all three cases.

- Or, alternatively, for a [VASPml standalone
  build](VASPml_library.md)
  please check:
  - `/path/to/vaspml/lib/libvaspml.a`
  - `/path/to/vaspml/include/InterfaceLAMMPS.hpp`

Next, we need to obtain the LAMMPS source code with the patch for
VASPml. Please clone the following repository to your hard disk and
change into the LAMMPS root directory:

    git clone https://github.com/vasp-dev/lammps
    cd lammps

At this point looking around in the git repository will show the files
from the `develop` branch (the main development branch of LAMMPS).
However, the patch files are located in another branch, hence we need to
switch with this command:

    git checkout vasp-mlff

Then, while still in the LAMMPS root directory we need to create a
symbolic link from `lammps/lib/vasp/vaspml` to the actual location of
the VASPml folder.

- In case of a VASP build with VASPml:

<table
style="width:100%; table-layout: fixed; border-spacing: 0; padding: 0; margin: 0; background-color: var(--vCB-bg); color: var(--vdefault-text); border-width: 1px; border-style: solid; border-color: var(--vCB-border);">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre
style="margin: 0; padding: 1em; background: none; border: none; white-space: pre; overflow-x: auto; font-family: monospace;"><code>ln -s /path/to/vasp/build/std/vaspml lib/vasp/</code></pre></td>
</tr>
</tbody>
</table>

Again, it is not important which of the three VASP build directories
(`std`, `gam` or `ncl`) is used because the VASPml library is the same.

- Alternatively, for a standalone VASPml build:

<table
style="width:100%; table-layout: fixed; border-spacing: 0; padding: 0; margin: 0; background-color: var(--vCB-bg); color: var(--vdefault-text); border-width: 1px; border-style: solid; border-color: var(--vCB-border);">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre
style="margin: 0; padding: 1em; background: none; border: none; white-space: pre; overflow-x: auto; font-family: monospace;"><code>ln -s /path/to/vaspml lib/vasp/</code></pre></td>
</tr>
</tbody>
</table>

For the remaining steps we need to change into the `src` directory:

    cd src

The source files for the `pair_style vasp` are part of the optional
package `ML-VASP` which can be activated with this command:

    make yes-ml-vasp

Before we can finally start the build process it is necessary to adapt
the LAMMPS makefile in `MAKE/Makefile.mpi`. Modify the `CC` and `LINK`
variables to match the compiler used during the [VASPml build
process](VASPml_library.md)
(`CXX_ML` variable). Also match the compiler flags in `CCFLAGS` and
`LINKFLAGS` to `CXXFLAGS_ML`. Flags do not need to be identical but at
least compatible compiler features should be used. Since VASPml requires
BLAS and LAPACK we may also need to complete the `LIB` variable with the
required libraries and their paths. For the GNU compiler with openBLAS
it may look like this:

    ...
    CC =    mpic++
    CCFLAGS = -g -O3 -std=c++17
    ...
    LINK =    mpic++
    LINKFLAGS = -g -O3 -std=c++17
    LIB = -L${OPENBLAS_ROOT}/lib -lopenblas

Finally, compile the LAMMPS source code with this command:

    make mpi

Optionally, add the `-j` flag to perform a parallel build (faster). If
the build process succeeds the LAMMPS executable `lmp_mpi` will be
located in the `lammps/src` directory.

## Using CMake (VASP 6.6.0 and later)\[<a
href="/wiki/index.php?title=Running_machine-learned_force_fields_in_LAMMPS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Using CMake (VASP 6.6.0 and later)">edit</a> \| (./index.php.md)")\]

Before starting the LAMMPS build please either compile [VASP with the
VASPml
library](../misc/Makefile.include.md) "Makefile.include"),
or alternatively, keep your VASP installation untouched and perform a
[standalone
build](VASPml_library.md)
of the VASPml library. Optionally, if you want to confirm that
everything is ready you can check for the presence of the following
files:

- `/path/to/vaspml/lib/libvaspml.a`,
- `/path/to/vaspml/build/libvaspml/InterfaceLAMMPS.hpp`,

where, in case of a build together with VASP, VASPml is located inside
of `/path/to/vasp/build/VERSION`, where `VERSION` is any of `std`, `gam`
or `ncl`. It does not matter which VASP build version is used because
the VASPml library will be identical in all three cases.

Next, we need to obtain the LAMMPS source code with the patch for
VASPml. Please clone the following repository to your hard disk and
change into the LAMMPS root directory:

    git clone https://github.com/vasp-dev/lammps
    cd lammps

At this point looking around in the git repository will show the files
from the `develop` branch (the main development branch of LAMMPS).
However, the patch files are located in another branch, hence we need to
switch with this command:

    git checkout vasp-mlff-6.6.0

Now we configure the
<a href="https://docs.lammps.org/Build_cmake.html" class="external text"
rel="nofollow">LAMMPS build with CMake</a> where `PKG_ML-VASP` and
`VASPML_DIR` need to be set:

    cmake -S cmake -B build -DPKG_ML-VASP=yes -DVASPML_DIR=/path/to/vaspml

With this command CMake checks the available compilers and libraries and
reports if anything is missing. Please check if the output is consistent
with the toolchain selected for building VASP or standalone VASPml. In
case CMake does not correctly determine the compiler and libraries it
may be necessary to pass them explicitly with <a
href="https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html"
class="external text" rel="nofollow">standard CMake variables</a>, like
`-DCMAKE_CXX_COMPILER=...` and `-DCMAKE_CXX_FLAGS=...` for specifying
the C++ compiler and command line arguments, respectively. Finally, in
the output you should see these lines confirming that VASPml has been
found:

    -- Found VASPml: /path/to/vaspml  
    -- Found VASPml library: /path/to/vaspml/lib/libvaspml.a
    -- Found VASPml include directory: /path/to/vaspml/build/libvaspml

If the previous CMake command exited successfully, LAMMPS can be built
with

    cmake --build build

Adding the `-j` flag allows the build process to run in parallel. The
LAMMPS executable `lmp` will be located inside the `build` directory.

# Setting up a LAMMPS MD run\[<a
href="/wiki/index.php?title=Running_machine-learned_force_fields_in_LAMMPS&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Setting up a LAMMPS MD run">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Warning:** Please always review the current [limitations and bug reports](VASPml_library.md). |

LAMMPS comes with its own powerful script language which allows the user
to specify all relevant MD simulation parameters in a single file.
Please consult the <a href="https://docs.lammps.org/Commands_input.html"
class="external text" rel="nofollow">LAMMPS documentation</a> for
details. Within the LAMMPS script language the commands `pair_style` and
`pair_coeff` are responsible for selecting a force field. The `ML-VASP`
package introduces a new `pair_style` called `vasp`. The
`pair_style vasp` command does not have any additional arguments, all
configurable settings are given as arguments to the `pair_coeff` command
in this format:

    pair_style vasp
    pair_coeff * * file types

The `pair_coeff` command must be followed by `* *`, then followed by the
name of the VASP force field file, typically `ML_FF`. Finally, there
comes a mapping from LAMMPS atom types to VASP force-field types, e.g.,
`H O Na Cl` means that LAMMPS types `1`, `2`, `3` and `4` are mapped to
VASP types `H`, `O`, `Na` and `Cl`, respectively. A valid example may
look like this:

    pair_style vasp
    pair_coeff * * ML_FF Pb Br Cs

This will map the LAMMPS atom types `1`, `2` and `3` in the
<a href="https://docs.lammps.org/read_data.html" class="external text"
rel="nofollow">input data file</a> to the types `Pb`, `Br` and `Cs` for
which a pre-trained machine-learned force field should be present in the
`ML_FF` file in the execution directory. A summary of the type mapping
is provided in the screen output and the `log.lammps` file, e.g. for the
example above it looks like this:

       LAMMPS       pair_coeff      VASP      |             VASP force field
        types       names           subtypes  |     types       names        subtypes
    ----------------------------------------- | -------------------------------------
            1 <---> Pb        <---> 0         |         0 <---> Pb     <---> 0        
            2 <---> Br        <---> 1         |         1 <---> Br     <---> 1        
            3 <---> Cs        <---> 2         |         2 <---> Cs     <---> 2  

On the left side we find the mapping, the right side gives an overview
of types present in the force field file. In this example, there is a
one-to-one mapping, hence, the table looks pretty obvious and contains
somewhat redundant information. However, it is also possible to leave
out a mapping from specified LAMMPS types by supplying `NULL` instead of
a valid VASP type name. This can be helpful when multiple force fields
should be combined, see
<a href="https://docs.lammps.org/pair_hybrid.html" class="external text"
rel="nofollow"><code>pair_style hybrid</code></a>. Furthermore, multiple
LAMMPS types may be mapped to the same VASP types. Finally, the force
field file may contain types which are not used in the current MD
simulation. Therefore, a more complicated example may look like this:

    pair_coeff * * vasp ML_FF NULL Cs NULL Br Pb Br

and the corresponding table could contain this information:

       LAMMPS       pair_coeff      VASP      |             VASP force field
        types       names           subtypes  |     types       names        subtypes
    ----------------------------------------- | -------------------------------------
            1 <---> unmapped! <---> unmapped! |         0 <---> Ca     <---> unused!
            2 <---> Cs        <---> 2         |         1 <---> Pb     <---> 0        
            3 <---> unmapped! <---> unmapped! |         2 <---> O      <---> unused!
            4 <---> Br        <---> 1         |         3 <---> Br     <---> 1        
            5 <---> Pb        <---> 0         |         4 <---> Cs     <---> 2        
            6 <---> Br        <---> 1         |

|  |
|----|
| **Mind:** Always ensure that the type mapping is correctly set up because mixed-up types may not immediately result in errors. An MD simulation may still run and only post-processing may ultimately reveal inconsistencies which can be tedious to trace back to type-mapping mistakes. |

The `pair_style vasp` expects input coordinates to be in the units of
Ångström and returns energies and forces with the energy unit of eV.
Hence, it is only compatible with the LAMMPS setting `units metal` in
the input script, otherwise an error will occur.



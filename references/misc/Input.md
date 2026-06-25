<!-- Source: https://vasp.at/wiki/index.php/Input | revid: 15029 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Input



[Overview](Input_and_Output_-_Tutorial.md) \>
Input \>
[Preparing a Super
Cell](../tutorials/Preparing_a_Super_Cell.md) \>[Output](../output-files/Output.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


VASP basically needs 4 input files for standard production runs:


## Contents


- [1
  INCAR](#incar)
- [2
  POSCAR](#poscar)
- [3
  KPOINTS](#kpoints)
- [4
  POTCAR](#potcar)


## [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=Input&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

The [INCAR](../input-files/INCAR.md) file holds the input parameters which
"steer" the calculation.

- The default values set by VASP itself are a clever choice to do
  standard calculations.
- These standard settings can be modified to specify:
  - What do you want to do? (SCF calculation, DOS, dielectric properties
    ...)
  - You can give parameters to fulfill your requirements concerning
    required precision, requested convergence, calculation time ...

  

## [POSCAR](../input-files/POSCAR.md)\[<a href="/wiki/index.php?title=Input&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

The [POSCAR](../input-files/POSCAR.md) file contains the information on the
structure.

- A simple [POSCAR](../input-files/POSCAR.md) file may look like this:

<!-- -->

    fcc:  Ni
    3.53
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    Ni
    1
    Selective Dyn
    Cartesian
    0 0 0  T T T

- The description of each line is given as follows:
  - 1: Header (comment).
  - 2: Overall scaling constant.
  - 3-6: Bravais matrix.
  - 4: Name(s) of the atom(s).
  - 5: Number of the atoms (of each atom type).
  - 6: (optional: selective dynamics).
  - 7: Specifies which coordinate system is used ("cartesian" or
    "direct").
  - 8-x: Positions of the atoms.

  

## [KPOINTS](../input-files/KPOINTS.md)\[<a href="/wiki/index.php?title=Input&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

The [KPOINTS](../input-files/KPOINTS.md) file determines the sampling of
the 1st Brillouin zone.

- A typical [KPOINTS](../input-files/KPOINTS.md) file:

<!-- -->

    Automatic mesh
    0
    G (M)
    4 4 4
    0.  0.  0.

- The description of each line is given as follows:
  - 1: Header (comment).
  - 2: Specifies the k mesh generation type. $N_{\overrightarrow{k}} =
    0$: automatic generation scheme.
  - 3: $\Gamma$-centered (Monkhorst-Pack) grid.
  - 4: Number of subdivisions in each direction.
  - 5: Optional shift of the mesh.

  

## [POTCAR](../input-files/POTCAR.md)\[<a href="/wiki/index.php?title=Input&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: POTCAR">edit</a> \| (./index.php.md)\]

The [POTCAR](../input-files/POTCAR.md) file contains the relevant
information concerning the pseudopotentials that are necessary to run
the calculation:

- Data that was required for generating the pseudopotentials.
- Number of valence electrons.
- Atomic mass.
- Energy cut-off.

If the cell contains different atomic species, the corresponding
[POTCAR](../input-files/POTCAR.md) files have to be concatenated, in the
same order as the atomic species are given in the
[POSCAR](../input-files/POSCAR.md) file.

**N.B.**: Different XC-types must not be mixed.


[Overview](Input_and_Output_-_Tutorial.md) \>
Input \>
[Preparing a Super
Cell](../tutorials/Preparing_a_Super_Cell.md) \>[Output](../output-files/Output.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


Back to the [main page](The_VASP_Manual.md).



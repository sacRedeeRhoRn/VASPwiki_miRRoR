<!-- Source: https://vasp.at/wiki/index.php/POSCAR | revid: 32299 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# POSCAR
The POSCAR file is a mandatory VASP input file. It is a plain text file
and contains at least the lattice geometry and the ionic positions.
Optionally, also starting velocities for a
[molecular-dynamics](../categories/Category-Molecular_Dynamics.md)
simulation can be provided here. This file shares its format with VASP
output file [CONTCAR](../output-files/CONTCAR.md). That may contain an
additional section with predictor-corrector coordinates necessary for
restarting
[molecular-dynamics](../categories/Category-Molecular_Dynamics.md)
runs.

Creating a POSCAR file is often the starting point of VASP-supported
research. It can be written manually or obtained from various online
materials and crystallographic databases providing a download in the
POSCAR file format. POSCAR files can be visualized using a variety of
softwares, including [VESTA](https://jp-minerals.org/vesta/en/),
[Jmol](https://jmol.sourceforge.net/), [OVITO](https://www.ovito.org/),
and the [Atomic Simulation
Environment](https://wiki.fysik.dtu.dk/ase//gettingstarted/gettingstarted.html)
(ASE).

## Contents

- [1 Basic introduction (minimal
  example)](#Basic_introduction_(minimal_example))
- [2 Full format specification](#Full_format_specification)
- [3 Precision and symmetry](#Precision_and_symmetry)
  - [3.1 Examples](#Examples)
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

## Basic introduction (minimal example)
In its simplest form the POSCAR file contains basic information about
the lattice, per-species number of ions and their positions. This is
sufficient in most situation where a VASP calculation is started from
scratch. Have a look at this example for cubic boron nitride:

    Cubic BN
    3.57
    0.0 0.5 0.5
    0.5 0.0 0.5
    0.5 0.5 0.0
    B N
    1 1
    Direct
    0.00 0.00 0.00 
    0.25 0.25 0.25

As indicated by the text coloring there are four blocks corresponding to
the following file contents:

***Comment line***

The first line is reserved for a free user comment, e.g. a system
description.

***Scaling factor and lattice***

In this block the first line specifies a universal lattice scaling
factor $s$. The next three lines define
the lattice vectors. Each line holds the unscaled Cartesian components
of one lattice vector. The actual lattice vectors ${\vec a}_1, {\vec a}_2$ and ${\vec
a}_3$ (in $\AA$) are the
product of the given numbers with the lattice scaling factor. Set the
universal scaling factor to 1 if you want to enter the lattice vectors
directly and avoid any additional scaling.

***Ion species and numbers:***

This section defines how many ions of each species are present. The
first line lists the species names, the second specifies the number of
ions for each species. The given order should match the order of species
appearing in the [POTCAR](POTCAR.md) file.

|  |
|----|
| **Warning:** If machine-learned force fields are used ([ML_LMLFF](../incar-tags/ML_LMLFF.md)=.TRUE.), it is not possible to give the same name to different groups of atoms in the POSCAR file. |

***Ion positions:***

Finally, the ion positions ${\vec R}$
(in $\AA$) are listed in this section.
The first line selects one of the two possible modes how the coordinates
$x_1, x_2$ and $x_3$ given in the following lines are interpreted:

- "Direct" means the positions are provided in direct (fractional)
  coordinates:

  ${\vec R} = x_1 {\vec a}_1 + x_2 {\vec a}_2 +
  x_3 {\vec a}_3,$

  where ${\vec R}$ is the position
  vector of an ion.

&nbsp;

- "Cartesian" specifies that positions are provided in a Cartesian
  coordinate system. However, the actual ion positions are also
  multiplied with the universal scaling factor, i.e.

  ${\vec R} = s \left( \begin{array}{c}x_1 \\ x_2
  \\ x_3\end{array} \right).$

The total number of lines with positions must match the total number of
ions given in the previous section. The ion species are also derived
from there, i.e. in the example above it is implied that the list of
positions contains one boron ion, followed by one nitrogen nuclei.

## Full format specification
The POSCAR file format is constructed from multiple sections arranged in
a predefined order. Some sections contain only a single line, others
span over many lines, some may even be omitted. The following list
defines the section order and their contents:

[![](https://vasp.at/wiki/images/thumb/2/28/Poscar.png/500px-Poscar.png)](https://vasp.at/wiki/File:Poscar.png)

Layout of POSCAR file.

- **Comment** - *(1 line), mandatory*

  - The first line is reserved for a free user comment, e.g. a system
    description. The maximum line length is 40 characters, extra
    characters are truncated.
- **Scaling factor(s)** - *(1 line), mandatory*

  - This line may contain one or three numbers. If one number is
    provided it specifies a universal lattice scaling factor
    $s$. It is multiplied with the three
    vectors in the following section to obtain the lattice vectors of
    the unit cell. Also, the ion positions are scaled with this factor
    if the "Cartesian" mode is selected (see section "Ion positions").
    If the number is negative, it is interpreted as the desired cell
    volume. Then, the scaling factor $s$
    is computed automatically to obtain the desired volume. If three
    numbers are provided in this line they act as individual scaling
    factors for the x-,y- and z-Cartesian components for the lattice
    vectors (and "Cartesian" mode ion positions). In this case all three
    numbers must be positive.
- **Lattice** - *(3 lines), mandatory*

  - This sections contains three lines defining the lattice vectors.
    Each line holds the unscaled Cartesian components of one lattice
    vector. The actual lattice vectors ${\vec
    a}_1, {\vec a}_2$ and ${\vec a}_3$ (in $\AA$) are the
    product of the given numbers with the lattice scaling factor `s`.
    Set the universal scaling factor to 1 if you want to enter the
    lattice vectors directly and avoid any additional scaling.
- **Species names** - *(1 line), optional*

  - This line lists the species of the present ions. The given order
    should match the order of species appearing in the
    [POTCAR](POTCAR.md) file. This line is optional, if
    omitted the species names are taken from the
    [POTCAR](POTCAR.md) file.

[TABLE]

- **Ions per species** - *(1 line), mandatory*

  - This mandatory line lists how many ions of each species are present.
    The given order should match the order of species appearing in the
    [POTCAR](POTCAR.md) file.
- **Selective dynamics** - *(1 line), optional*

  - If the line after the "Ions per species" section contains
    `Selective dynamics` it enables the "selective dynamics" feature
    (actually only the first character is relevant and must be *S* or
    *s*). This allows to provide extra flags for each atom signaling
    whether the respective coordinate(s) of this atom will be allowed to
    change during the ionic relaxation (or MDs). This setting is useful
    if only certain shells around a defect or layers near a surface
    should relax. See also the [structure
    optimization](../tutorials/Structure_optimization.md)
    tips.
- **Ion positions** - *(1 line + \#atoms), mandatory*

  - Here, the ion positions ${\vec R}$
    (in $\AA$) are listed. The first
    line selects one of the two possible modes how the coordinates
    $x_1, x_2$ and
    $x_3$ given in the following lines
    are interpreted:
    - "Direct" means the positions are provided in direct (fractional)
      coordinates:

      ${\vec R} = x_1 {\vec a}_1 + x_2 {\vec
      a}_2 + x_3 {\vec a}_3,$

      where ${\vec R}$ is the position
      vector of an ion.

    - "Cartesian" specifies that positions are provided in a Cartesian
      coordinate system. However, the actual ion positions are also
      multiplied with the universal scaling factor, i.e.

      ${\vec R} = s \left( \begin{array}{c}x_1 \\
      x_2 \\ x_3\end{array} \right).$

Actually, only the first character on the line is significant and the
only key characters recognized are `C`, `c`, `K` or `k` for switching to
the "Cartesian" mode. Everything else will be interpreted as "Direct"
mode.

The total number of lines with positions must match the total number of
ions given in the "Ions per species" section. The ion species are also
derived from there, e.g. if the "Ions per species" section lists `5 8`,
then there must be five ion position lines for the first species,
followed by eight ions of the second species. If your are not sure
whether you have a correct input please check the
[OUTCAR](../output-files/OUTCAR.md) file, which contains both the final
Cartesian components of the vector ${\vec R}$ and the positions in direct (fractional) coordinates.

If the selective dynamics feature is enabled on each coordinate triplet
is followed by three additional logical flags, i.e. each is either `T`
or `F` for true and false, respectively. This determines whether to
allow changes of the coordinates or not. If the line selective dynamics
is removed from the POSCAR file this flag will be ignored (and
internally set to `T`).

|  |
|----|
| **Mind:** The flags refer to the positions of the ions in direct coordinates, no matter whether the positions are entered in "Cartesian" or "Direct" coordinate modes. |

For example, consider the following ion specification:

    ...
    Selective dynamics
    Cartesian
    0.00 0.00 0.00 T F T
    1.27 0.98 0.32 F T F
    ...

Here, the first atom is allowed to move into the direction of the first
and third direct lattice vector. The second atom may only move in the
second lattice vector direction.

If no initial velocities are provided, the file may end here.

- **Lattice velocities** - *(8 lines), optional - from
  [CONTCAR](../output-files/CONTCAR.md) only¹*

  - Contains the lattice vectors ${\vec a}_1,
    {\vec a}_2$ and ${\vec a}_3$ and their velocities. Lattice velocities occur when in
    molecular dynamics simulations, lattice vectors are treated as
    dynamic variables, i.e., are allowed to change over time
    ([IBRION](../incar-tags/IBRION.md)=0 together with
    [ISIF](../incar-tags/ISIF.md)=3), e.g., [Nosé-Hoover
    thermostat](../tutorials/Nosé-Hoover_thermostat.md).
    When written to the [CONTCAR](../output-files/CONTCAR.md) file the
    section starts with a line containing the string
    `Lattice velocities and vectors`. While reading in the POSCAR file
    upon restarting only the first character of the line is checked for
    `L` or `l`. The following line specifies the initialization state of
    the lattice velocities (usually just the integer 1). The next three
    lines contain the velocities corresponding to the three lattice
    vectors divided by the time step given via the
    [POTIM](../incar-tags/POTIM.md) tag. The remaining three lines repeat
    the actual lattice vectors ${\vec a}_1, {\vec
    a}_2$ and ${\vec a}_3$
    where multiplication with the scaling factor $s$ has already been taken into account.
- **Ion velocities** - *(1 line + \#atoms), optional*

  - Here initial velocities for all ions can be provided. The input
    format is similar to the section "Ion positions" above. The first
    line determines the input mode which is either "Direct" or
    "Cartesian". In contrast to the reading of ion positions, there is
    no multiplication with the scaling factor $s$ applied in the "Cartesian" mode. Another minor difference
    is the interpretation of the contents of the first line in this
    section. In addition to `C`, `c`, `K` or `k` as the first character
    also an empty line switches on the "Cartesian" mode. Everything else
    enables the "Direct" mode instead. The velocity section written out
    to the [CONTCAR](../output-files/CONTCAR.md) file always starts with an
    empty line and velocities are given in "Cartesian" mode. The
    following lines contain the velocity vectors of each ion defined in
    the "Ion positions" section. Velocities must be provided in units
    "direct lattice vector/timestep" or $\AA$/fs for "Direct" or "Cartesian" mode, respectively.

|  |
|----|
| **Tip:** Entering velocities by hand is rarely done because a simple alternative to set initial velocities is provided via the [TEBEG](../incar-tags/TEBEG.md) tag. |

[TABLE]

- **MD extra** - *(variable line number), optional - from
  [CONTCAR](../output-files/CONTCAR.md) only¹*

  - The predictor-corrector coordinates are only provided to continue a
    molecular dynamics run from a [CONTCAR](../output-files/CONTCAR.md)
    file of a previous run, they cannot be entered by hand. There is
    first a blank line after the ion velocities, the second line is the
    initialization state of the predictor-corrector coordinates, and the
    third line is the time step in MD [POTIM](../incar-tags/POTIM.md). The
    fourth line is the [Nosé-Hoover
    thermostat](../tutorials/Nosé-Hoover_thermostat.md)
    for the (*n*)th and (*n+1*)th iteration ($s_{n+1}, \dot{s}_{n+1}, \dot{s}_{n}, s_n$). Finally,
    the predictor-corrector coordinates are printed.

¹ "from [CONTCAR](../output-files/CONTCAR.md) only": This section is
usually not entered manually by the user. It appears in the
[CONTCAR](../output-files/CONTCAR.md) file output at the end of VASP runs
which involve ionic steps and is intended for restarting a previous
calculation.

## Precision and symmetry
VASP determines the symmetry of the system from the POSCAR file. It is a
common mistake to enter the positions with insufficient precision (too
few digits). To make the best use of the symmetry routines in VASP, it
is strongly recommended to specify the positions (and lattice
parameters) in the POSCAR file with at least 7 significant digits (but
preferably more). Internal tests for symmetry operations are done
against a user-supplied value for the precision, specified by
[SYMPREC](../incar-tags/SYMPREC.md) (defaults to 10⁻⁵). Hence, 5
significant digits are absolutely borderline and can cause serious
issues in the automatic symmetry determination, for instance, finding
some but not all generators for the symmetry group. Also, "noise" in the
positions might grow during relaxations, so that sometimes, upon reading
the [CONTCAR](../output-files/CONTCAR.md) file, some symmetry operations
are not found. All these issues are best avoided by making the initial
POSCAR file as accurate as possible.

If you have a POSCAR file with the positions written with low precision
and would like to reconstruct with higher precision, we recommend using
a symmetry package, such as spglib^([\[1\]](#cite_note-spglib-1)), to
find the symmetries given a certain precision, symmetrizing the lattice
vectors and positions and writing the POSCAR file with a higher number
of significant digits. This can be done using
pymatgen^([\[2\]](#cite_note-pymatgen-2)) (which interfaces with
spglib^([\[1\]](#cite_note-spglib-1))) to symmetrize the structure and
write it to a POSCAR file, see [example on
github](https://gist.github.com/henriquemiranda/e4a1b616693aac339ef011af6484f890).

### Examples
    Cubic BN
    3.57
    0.00000000 0.50000000 0.50000000
    0.50000000 0.00000000 0.50000000
    0.50000000 0.50000000 0.00000000
    B N
    1 1
    Selective dynamics
    Cartesian
    0.00000000 0.00000000 0.00000000 T T F
    0.25000000 0.25000000 0.25000000 F F F
    Cartesian
    0.01000000 0.01000000 0.01000000
    0.00000000 0.00000000 0.00000000
    optionally predictor-corrector coordinates 
       given on file CONTCAR of MD-run
      ....
      ....

    fcc Si
    3.9
     0.50000000 0.50000000 0.00000000
     0.00000000 0.50000000 0.50000000
     0.50000000 0.00000000 0.50000000
      1
    cartesian
    0.00000000 0.00000000 0.00000000

    MgO Fm-3m (No. 225)
    1.0
     2.606553 0.000000 1.504894
     0.868851 2.457482 1.504894
     0.000000 0.000000 3.009789
     Mg O
     1 1
    direct
     0.000000 0.000000 0.000000 Mg
     0.500000 0.500000 0.500000 O

## Related tags and articles
[structure
optimization](../tutorials/Structure_optimization.md),
[SYMPREC](../incar-tags/SYMPREC.md), [IBRION](../incar-tags/IBRION.md),
[CONTCAR](../output-files/CONTCAR.md), [POTCAR](POTCAR.md)

## References
1.  ↑ ^([a](#cite_ref-spglib_1-0)) ^([b](#cite_ref-spglib_1-1))
    [https://spglib.github.io/spglib/
    (2022).](https://spglib.github.io/spglib/)
2.  [↑](#cite_ref-pymatgen_2-0) [https://pymatgen.org/
    (2022).](https://pymatgen.org/)

------------------------------------------------------------------------

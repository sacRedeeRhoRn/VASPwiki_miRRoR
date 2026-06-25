<!-- Source: https://vasp.at/wiki/index.php/Input_and_Output_-_a_short_Intro | revid: 31484 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Input and Output - a short Intro



## Contents


- [1
  Input](#Input)
  - [1.1
    INCAR](#INCAR)
  - [1.2
    POSCAR](#POSCAR)
  - [1.3
    KPOINTS](#KPOINTS)
  - [1.4
    POTCAR](#POTCAR)
- [2
  Output](#Output)
  - [2.1
    OUTCAR](#OUTCAR)
  - [2.2 OSZICAR
    and stdout](#OSZICAR_and_stdout)
  - [2.3
    CONTCAR](#CONTCAR)
  - [2.4
    XDATCAR](#XDATCAR)
  - [2.5
    DOSCAR](#DOSCAR)
  - [2.6
    CHGCAR](#CHGCAR)
  - [2.7
    WAVECAR](#WAVECAR)


# Input\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

VASP basically needs 4 input files for standard production runs:

## [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

The [INCAR](../input-files/INCAR.md) file holds the input parameters which
"steer" the calculation.

- The default values set by VASP itself are a clever choice to do
  standard calculations.
- These standard settings can be modified to specify:
  - What do you want to do? (scf calculation, DOS, dielectric properties
    ...)
  - You can give parameters to fulfill your requirements concerning
    required precision, requested convergence, calculation time ...

  

## [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=3"
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

  

## [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=4"
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

  

## [POTCAR](../input-files/POTCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: POTCAR">edit</a> \| (./index.php.md)\]

The [POTCAR](../input-files/POTCAR.md) file contains the relevant
information concerning the pseudo potentials that are necessary to run
the calculation:

- Data that was required for generating the pseudo potentials.
- Number of valence electrons.
- Atomic mass.
- Energy cutoff.

If the cell contains different atomic species, the corresponding
[POTCAR](../input-files/POTCAR.md) files have to be concatenated, in the
same order as the atomic species are given in the
[POSCAR](../input-files/POSCAR.md) file.

**N.B.**: Different XC-types must not be mixed.

  

# Output\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

VASP gives several different output files, depending on which task is
performed. The most important files that are produced in (almost) every
calculation are described in the following:

## [OUTCAR](../output-files/OUTCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: OUTCAR">edit</a> \| (./index.php.md)\]

The [OUTCAR](../output-files/OUTCAR.md) file gives detailed output of a VASP
run, including:

- A summary of the used input parameters.
- Information about the electronic steps: $E_{\mathrm{Fermi}}$, KS-eigenvalues.
- Stress tensors.
- Forces on the atoms.
- Local charges and magnetic moments.
- Dielectric properties

The amount of output written onto the [OUTCAR](../output-files/OUTCAR.md)
file can be chosen by modifying the [NWRITE](../incar-tags/NWRITE.md) tag
in the [INCAR](../input-files/INCAR.md) file.

## [OSZICAR](../output-files/OSZICAR.md) and stdout\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: OSZICAR and stdout">edit</a> \| (./index.php.md)\]

The [OSZICAR](../output-files/OSZICAR.md) file gives a short summary of the
results:

- Chosen SCF algorithm.
- Convergence of the total energy, charge- and spin densities.
- Free energies.
- Magnetic moments of the cell.

## [CONTCAR](../output-files/CONTCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: CONTCAR">edit</a> \| (./index.php.md)\]

The [CONTCAR](../output-files/CONTCAR.md) file gives the updated geometry
data at the end of a run:

- Lattice parameter.
- Bravais matrix.
- Ionic positions.
- (Optionally velocities).

The format of the [CONTCAR](../output-files/CONTCAR.md) file is the same as
of the [POSCAR](../input-files/POSCAR.md) file, hence it can be used
directly for continuation runs after having been copied to the
[POSCAR](../input-files/POSCAR.md) file.

## [XDATCAR](../output-files/XDATCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: XDATCAR">edit</a> \| (./index.php.md)\]

The [XDATCAR](../output-files/XDATCAR.md) file contains updated ionic
positions of each ionic step.

## [DOSCAR](../output-files/DOSCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: DOSCAR">edit</a> \| (./index.php.md)\]

The [DOSCAR](../output-files/DOSCAR.md) file contains the total and
integrated DOS and optionally the local partial DOS.

## [CHGCAR](../input-files/CHGCAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: CHGCAR">edit</a> \| (./index.php.md)\]

The [CHGCAR](../input-files/CHGCAR.md) file contains the charges
$\rho \* V$.

## [WAVECAR](../input-files/WAVECAR.md)\[<a
href="/wiki/index.php?title=Input_and_Output_-_a_short_Intro&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: WAVECAR">edit</a> \| (./index.php.md)\]

The [WAVECAR](../input-files/WAVECAR.md) file contains the wave function
coefficients. This file can be used to continue from a previous run.

Back to the [main page](The_VASP_Manual.md).



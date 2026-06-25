<!-- Source: https://vasp.at/wiki/index.php/Output | revid: 29866 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Output



[Overview](../misc/Input_and_Output_-_Tutorial.md) \>
[Input](../misc/Input.md) \>
[Preparing a Super
Cell](../tutorials/Preparing_a_Super_Cell.md) \>Output \>
[List of tutorials](../categories/Category-Tutorials.md)


VASP gives several different output files, depending on which task is
performed. The most important files that are produced in (almost) every
calculation are described in the following:


## Contents


- [1
  OUTCAR](#OUTCAR)
- [2 OSZICAR and
  stdout](#OSZICAR_and_stdout)
- [3
  CONTCAR](#CONTCAR)
- [4
  XDATCAR](#XDATCAR)
- [5
  DOSCAR](#DOSCAR)
- [6
  CHGCAR](#CHGCAR)
- [7
  WAVECAR](#WAVECAR)


## [OUTCAR](OUTCAR.md)\[<a href="/wiki/index.php?title=Output&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: OUTCAR">edit</a> \| (./index.php.md)\]

The [OUTCAR](OUTCAR.md) file gives detailed output of a VASP
run, including:

- A summary of the used input parameters.
- Information about the electronic steps: $E_{\mathrm{Fermi}}$, KS-eigenvalues.
- Stress tensors.
- Forces on the atoms.
- Local charges and magnetic moments.
- Dielectric properties

The amount of output written onto the [OUTCAR](OUTCAR.md)
file can be chosen by modifying the [NWRITE](../incar-tags/NWRITE.md) tag
in the [INCAR](../input-files/INCAR.md) file.

## [OSZICAR](OSZICAR.md) and stdout\[<a href="/wiki/index.php?title=Output&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: OSZICAR and stdout">edit</a> \| (./index.php.md)\]

The [OSZICAR](OSZICAR.md) file gives a short summary of the
results:

- Chosen SCF algorithm.
- Convergence of the total energy, charge- and spin densities.
- Free energies.
- Magnetic moments of the cell.

## [CONTCAR](CONTCAR.md)\[<a href="/wiki/index.php?title=Output&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: CONTCAR">edit</a> \| (./index.php.md)\]

The [CONTCAR](CONTCAR.md) file gives the updated geometry
data at the end of a run:

- Lattice parameter.
- Bravais matrix.
- Ionic positions.
- (Optionally velocities).

The format of the [CONTCAR](CONTCAR.md) file is the same as
of the [POSCAR](../input-files/POSCAR.md) file, hence it can be used
directly for continuation runs after having been copied to the
[POSCAR](../input-files/POSCAR.md) file.

## [XDATCAR](XDATCAR.md)\[<a href="/wiki/index.php?title=Output&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: XDATCAR">edit</a> \| (./index.php.md)\]

The [XDATCAR](XDATCAR.md) file contains updated ionic
positions of each ionic step.

## [DOSCAR](DOSCAR.md)\[<a href="/wiki/index.php?title=Output&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: DOSCAR">edit</a> \| (./index.php.md)\]

The [DOSCAR](DOSCAR.md) file contains the total and
integrated DOS and optionally the local partial DOS.

## [CHGCAR](../input-files/CHGCAR.md)\[<a href="/wiki/index.php?title=Output&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: CHGCAR">edit</a> \| (./index.php.md)\]

The [CHGCAR](../input-files/CHGCAR.md) file contains the charges
$\rho \* V$.

## [WAVECAR](../input-files/WAVECAR.md)\[<a href="/wiki/index.php?title=Output&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: WAVECAR">edit</a> \| (./index.php.md)\]

The [WAVECAR](../input-files/WAVECAR.md) file contains the wave function
coefficients. This file can be used to continue from a previous run.


[Overview](../misc/Input_and_Output_-_Tutorial.md) \>
[Input](../misc/Input.md) \>
[Preparing a Super
Cell](../tutorials/Preparing_a_Super_Cell.md) \>Output \>
[List of tutorials](../categories/Category-Tutorials.md)


Back to the [main page](../misc/The_VASP_Manual.md).



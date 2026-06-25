<!-- Source: https://vasp.at/wiki/index.php/CO_partial_DOS | revid: 10413 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CO partial DOS



[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](O_atom.md) \>
[O atom
spinpolarized](O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](O_dimer.md) \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \>
CO partial
DOS \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \>
[H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#Task)
- [2
  Input](#Input)
  - [2.1
    POSCAR](#POSCAR)
  - [2.2
    INCAR](#INCAR)
  - [2.3
    KPOINTS](#KPOINTS)
- [3
  Calculation](#Calculation)
  - [3.1
    PROCAR](#PROCAR)
- [4
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the DOS of a CO molecule (using p4vasp)

## Input\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    CO molecule in a box
     1.0          ! universal scaling parameters
     8.0 0.0 0.0  ! lattice vector  a(1)
     0.0 8.0 0.0  ! lattice vector  a(2)
     0.0 0.0 8.0  ! lattice vector  a(3)
    1 1           ! number of atoms for each species
    sel           ! selective degrees of freedom are changed
    cart          ! positions in cartesian coordinates
     0 0 0       F F T  ! first atom
     0 0 1.143   F F T  ! second atom

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    SYSTEM = CO molecule in a box
    ISMEAR = 0   ! Gaussian smearing
    LORBIT = 11

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

## Calculation\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- The [PROCAR](../output-files/PROCAR.md) file gives valuable information of
  the character of the one electron states:

|  |  |
|----|----|
| [LORBIT](../incar-tags/LORBIT.md)=10 | [DOSCAR](../output-files/DOSCAR.md) and l decomposed [PROCAR](../output-files/PROCAR.md) file |
| [LORBIT](../incar-tags/LORBIT.md)=11 | [DOSCAR](../output-files/DOSCAR.md) and lm decomposed [PROCAR](../output-files/PROCAR.md) file |

- We'll use [LORBIT](../incar-tags/LORBIT.md)=11 and see if we can
  distinguish $p_{x}$ and
  $p_{z}$ states.

### [PROCAR](../output-files/PROCAR.md)\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: PROCAR">edit</a> \| (./index.php.md)\]

    band   3 # energy  -11.46540832 # occ.  2.00000000
      
    ion      s     py     pz     px    dxy    dyz    dz2    dxz    dx2    tot
      1  0.000  0.510  0.000  0.036  0.000  0.000  0.000  0.000  0.000  0.546
      2  0.000  0.146  0.000  0.010  0.000  0.000  0.000  0.000  0.000  0.157
    tot  0.000  0.656  0.000  0.047  0.000  0.000  0.000  0.000  0.000  0.703
      
    band   4 # energy  -11.46540832 # occ.  2.00000000
      
    ion      s     py     pz     px    dxy    dyz    dz2    dxz    dx2    tot
      1  0.000  0.036  0.000  0.510  0.000  0.000  0.000  0.000  0.000  0.546
      2  0.000  0.010  0.000  0.146  0.000  0.000  0.000  0.000  0.000  0.157
    tot  0.000  0.047  0.000  0.656  0.000  0.000  0.000  0.000  0.000  0.703

    band   5 # energy   -8.76483386 # occ.  2.00000000
     
    ion      s     py     pz     px    dxy    dyz    dz2    dxz    dx2    tot
      1  0.001  0.000  0.135  0.000  0.000  0.000  0.000  0.000  0.000  0.136
      2  0.172  0.000  0.261  0.000  0.000  0.000  0.000  0.000  0.000  0.433
    tot  0.173  0.000  0.396  0.000  0.000  0.000  0.000  0.000  0.000  0.569

- To plot the DOS start p4vasp:

<a href="/wiki/File:Fig_CO_1.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/0/07/Fig_CO_1.png/1000px-Fig_CO_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/07/Fig_CO_1.png/1500px-Fig_CO_1.png 1.5x, /wiki/images/0/07/Fig_CO_1.png 2x"
width="1000" height="700" /></a>

## Download\[<a
href="/wiki/index.php?title=CO_partial_DOS&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/9/95/COstates.tgz" class="internal"
title="COstates.tgz">COstates.tgz</a>


[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](O_atom.md) \>
[O atom
spinpolarized](O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](O_dimer.md) \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \>
CO partial
DOS \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \>
[H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



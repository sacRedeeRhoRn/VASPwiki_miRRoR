<!-- Source: https://vasp.at/wiki/index.php/H2O_vibration | revid: 10435 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# H2O vibration



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
[CO partial
DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \>
H2O
vibration \> [H2O
molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2
  Input](#input)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    INCAR](#incar)
  - [2.3
    KPOINTS](#kpoints)
- [3
  Calculation](#calculation)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=H2O_vibration&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the vibrational frequencies of a
$\mathrm{H}_{2}\mathrm{O}$ molecule.

## Input\[<a
href="/wiki/index.php?title=H2O_vibration&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=H2O_vibration&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    H2O _2                                                                          
    1.0000000
      8.0000000   0.0000000   0.0000000
      0.0000000   8.0000000   0.0000000
      0.0000000   0.0000000   8.0000000
       1    2
    cart
      0.0000000   0.0000000   0.0000000
      0.5960812  -0.7677068   0.0000000
      0.5960812   0.7677068   0.0000000

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=H2O_vibration&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    SYSTEM = H2O vibration
    PREC = A
    # IBRION = 1 ; NSW = 10 ; NFREE = 2 ; EDIFFG = -1E-4
    ENMAX = 400
    ISMEAR = 0    # Gaussian smearing
    IBRION = 6    # finite differences with symmetry
    NFREE = 2     # central differences (default)
    POTIM = 0.015 # default as well
    EDIFF = 1E-8 
    NSW = 1       # ionic steps > 0

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=H2O_vibration&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

## Calculation\[<a
href="/wiki/index.php?title=H2O_vibration&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

How many zero frequency modes should be observed and why? Try to use the
linear response code ([IBRION](../incar-tags/IBRION.md)=8 and
[EDIFF](../incar-tags/EDIFF.md)=1E-8) to obtain reference results. For
finite differences, are the results sensitive to the step width
[POTIM](../incar-tags/POTIM.md). In this specific case, the drift in the
forces is too large to obtain the zero frequency modes "exactly", and it
is simplest to increase the cutoff [ENCUT](../incar-tags/ENCUT.md) to 800
eV. The important and physically meaningful frequencies are, however,
insensitive to the choice of the cutoff.

## Download\[<a
href="/wiki/index.php?title=H2O_vibration&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/5/5c/H2Ovib.tgz" class="internal"
title="H2Ovib.tgz">H2Ovib.tgz</a>


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
[CO partial
DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \>
H2O
vibration \> [H2O
molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



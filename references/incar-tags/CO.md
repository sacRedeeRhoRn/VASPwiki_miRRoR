<!-- Source: https://vasp.at/wiki/index.php/CO | revid: 10412 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CO



[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](../misc/O_atom.md) \>
[O atom
spinpolarized](../misc/O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](../misc/O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](../misc/O_dimer.md) \>
CO \>
[CO
vibration](../misc/CO_vibration.md) \>
[CO partial
DOS](../misc/CO_partial_DOS.md) \>
[H2O](H2O.md) \> [H2O
vibration](../misc/H2O_vibration.md) \>
[H2O molecular
dynamics](../misc/H2O_molecular_dynamics.md) \>
[Further things to try](../misc/At_and_mol_further.md)
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
  - [2.4
    POTCAR](#POTCAR)
- [3
  Calculation](#Calculation)
- [4
  Download](#Download)


## Task\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Relaxation of the bond length in a CO molecule.

## Input\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    CO molecule in a box
     1.0          ! universal scaling parameters
     8.0 0.0 0.0  ! lattice vector  a(1)
     0.0 8.0 0.0  ! lattice vector  a(2)
     0.0 0.0 8.0  ! lattice vector  a(3)
    1 1           ! number of atoms for each species
    cart          ! positions in cartesian coordinates
     0 0 0        ! first atom
     0 0 1.12     ! second atom

### [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    SYSTEM = CO molecule in a box
    ISMEAR = 0 ! Gaussian smearing
    NSW = 5    ! 5 ionic steps
    IBRION = 2 ! use the conjugate gradient algorithm

### [KPOINTS](../input-files/KPOINTS.md)\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

### [POTCAR](../input-files/POTCAR.md)\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: POTCAR">edit</a> \| (./index.php.md)\]

The [POTCAR](../input-files/POTCAR.md) file is created by the concatenation
of two individual [POTCAR](../input-files/POTCAR.md) files corresponding to
O and C, e.g.:

    cat  .../O/POTCAR  .../C POTCAR  > POTCAR

## Calculation\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- A similar relaxation as in the previous case
  ([O_dimer](../misc/O_dimer.md)) is performed but in this case
  more steps are required, since the first estimate for the minimum is
  not very accurate. The trial steps are much too long
  ([POTIM](POTIM.md) parameter).

<!-- -->

       1 F= -.14764064E+02 E0= -.14764064E+02  d E =-.147641E+02
     curvature:   0.00 expect dE= 0.000E+00 dE for cont linesearch  0.000E+00
     trial: gam= 0.00000 g(F)=  0.820E+00 g(S)=  0.000E+00 ort = 0.000E+00 (trialstep = 0.100E+01)
     search vector abs. value=  0.820E+00
     bond charge predicted
    ...         ...      ...
    ...         ...      ...
    ...         ...      ...
       2 F= -.12660858E+02 E0= -.12660858E+02  d E =0.210321E+01
     trial-energy change:    2.103205  1 .order    1.311207   -0.819873    3.442288
     step:   0.1924(harm=  0.1924)  dis= 0.02705  next Energy=   -14.842919 (dE=-0.789E-01)
     bond charge predicted
    ...         ...      ...
    ...         ...      ...
    ...         ...      ...
       3 F= -.14747869E+02 E0= -.14747869E+02  d E =0.161943E-01
     curvature:  -0.10 expect dE=-0.902E-01 dE for cont linesearch -0.902E-01
     ZBRENT: interpolating
     opt :   0.0929  next Energy=   -14.802162 (dE=-0.381E-01)
     bond charge predicted
    ...         ...      ...
    ...         ...      ... 
    ...         ...      ...
       4 F= -.14796822E+02 E0= -.14796822E+02  d E =-.327586E-01
     curvature:  -0.04 expect dE=-0.330E-03 dE for cont linesearch -0.330E-03
     trial: gam= 0.00000 g(F)=  0.814E-02 g(S)= 0.000E+00 ort =-0.817E-01 (trialstep = 0.819E+00)
     search vector abs. value=  0.814E-02
     reached required accuracy - stopping structural energy minimisation

## Download\[<a href="/wiki/index.php?title=CO&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/a/a3/CO.tgz" class="internal"
title="CO.tgz">CO.tgz</a>


[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](../misc/O_atom.md) \>
[O atom
spinpolarized](../misc/O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](../misc/O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](../misc/O_dimer.md) \>
CO \>
[CO
vibration](../misc/CO_vibration.md) \>
[CO partial
DOS](../misc/CO_partial_DOS.md) \>
[H2O](H2O.md) \> [H2O
vibration](../misc/H2O_vibration.md) \>
[H2O molecular
dynamics](../misc/H2O_molecular_dynamics.md) \>
[Further things to try](../misc/At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



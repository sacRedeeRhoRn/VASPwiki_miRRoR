<!-- Source: https://vasp.at/wiki/index.php/H2O | revid: 10433 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# H2O



[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](../misc/O_atom.md) \>
[O atom
spinpolarized](../misc/O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](../misc/O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](../misc/O_dimer.md) \>
[CO](CO.md) \> [CO
vibration](../misc/CO_vibration.md) \>
[CO partial
DOS](../misc/CO_partial_DOS.md) \>
H2O \>
[H2O
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
- [3
  Calculation](#Calculation)
- [4
  Download](#Download)


## Task\[<a href="/wiki/index.php?title=H2O&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Relaxation of an $\mathrm{H}_{2}\mathrm{O}$ molecule.

## Input\[<a href="/wiki/index.php?title=H2O&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a href="/wiki/index.php?title=H2O&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    H2O _2
    0.52918   ! scaling parameter
     15 0 0
     0 15 0
     0 0 15
    1 2
    select
    cart
         0.00     0.00     0.00 F F F
         1.10    -1.43     0.00 T T F
         1.10     1.43     0.00 T T F

All coordinates are scaled by the factor 0.52918.

### [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=H2O&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    PREC = Normal    ! standard precision 
    ENMAX = 400      ! cutoff should be set manually
    ISMEAR = 0 ; SIGMA = 0.1
    IBRION = 1       ! use DIIS algorithm to converge
    NFREE = 2        ! 2 independent degrees of freedom
    NSW = 10         ! 10 ionic steps
    EDIFFG = -0.02   ! forces smaller 0.02 A/eV

### [KPOINTS](../input-files/KPOINTS.md)\[<a href="/wiki/index.php?title=H2O&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

## Calculation\[<a href="/wiki/index.php?title=H2O&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- Use [PREC](PREC.md)=*Normal* (Default for VASP.5.X)
- It is strongly urged that the energy cutoffs are set manually in the
  [INCAR](../input-files/INCAR.md) file, as it provides more control over
  the calculations.
- For the ionic optimization the DIIS algorithm is used. This algorithm
  builds an approximation of the Hessian matrix and converges usually
  faster than the conjugate gradient algorithm. It is however
  recommended to set the independent degrees of freedom manually.
  \*[EDIFFG](EDIFFG.md) determines when to terminate the
  relaxation. Positive values: energy change between steps must be less
  than the value set by [EDIFFG](EDIFFG.md). Negative
  values: $|\mathbf{F}_{i}| <
  |\mathrm{EDIFFG}| \forall i=1,N_{\mathrm{ions}}$.

## Download\[<a href="/wiki/index.php?title=H2O&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/8/85/H2O.tgz" class="internal"
title="H2O.tgz">H2O.tgz</a>


[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](../misc/O_atom.md) \>
[O atom
spinpolarized](../misc/O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](../misc/O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](../misc/O_dimer.md) \>
[CO](CO.md) \> [CO
vibration](../misc/CO_vibration.md) \>
[CO partial
DOS](../misc/CO_partial_DOS.md) \>
H2O \>
[H2O
vibration](../misc/H2O_vibration.md) \>
[H2O molecular
dynamics](../misc/H2O_molecular_dynamics.md) \>
[Further things to try](../misc/At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



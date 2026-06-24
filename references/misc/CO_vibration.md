<!-- Source: https://vasp.at/wiki/index.php/CO_vibration | revid: 10281 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CO vibration
[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> [O
atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O dimer](O_dimer.md) \> [CO](../incar-tags/CO.md) \> CO
vibration \> [CO partial DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \> [H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Calculation](#Calculation)
  - [3.1 OUTCAR](#OUTCAR)
- [4 Download](#Download)

## Task
Calculation of the vibrational frequencies of a CO molecule.

## Input
### [POSCAR](../input-files/POSCAR.md)
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

Alternatively, try to fix one of the atoms completely.

### [INCAR](../input-files/INCAR.md)
    SYSTEM = CO molecule in a box
    ISMEAR = 0   ! Gaussian smearing
    IBRION = 5   ! calculate second derivatives, Hessian matrix, and phonon frequencies
                 ! from finite differences
    NFREE = 2    ! central differences
    POTIM = 0.02 ! 0.02 A stepwidth 
    NSW = 1      ! ionic steps > 0

### [KPOINTS](../input-files/KPOINTS.md)
    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

## Calculation
- The selected degrees of freedom are displaced once in the direction
  $\hat{x}$ and once in
  $-\hat{x}$ by 0.02
  $\AA$ ([POTIM](../incar-tags/POTIM.md)).

&nbsp;

- In the present case this makes 4 displacements plus the equilibrium
  positions (i.e. a total of five ionic configurations).

### [OUTCAR](../output-files/OUTCAR.md)
At the end of the [OUTCAR](../output-files/OUTCAR.md) file the following
output should be obtained:

    SECOND DERIVATIVES (NOT SYMMETRIZED)
    ------------------------------------
                  1Z          2Z
     1Z  -114.737304  114.737304
     2Z   114.458316 -114.458316
      
      
    Eigenvectors and eigenvalues of the dynamical matrix
    ----------------------------------------------------
       
      
      1 f  =   63.887522 THz   401.417139 2PiTHz 2131.058277 cm-1   264.217647 meV
                X         Y         Z           dx          dy          dz
         0.000000  0.000000  0.000000            0           0   -0.655280
         0.000000  0.000000  1.143000            0           0    0.755386

      2 f/i=    0.038494 THz     0.241864 2PiTHz    1.284016 cm-1     0.159198 meV
                X         Y         Z           dx          dy          dz
         0.000000  0.000000  0.000000            0           0   -0.755386
         0.000000  0.000000  1.143000            0           0   -0.655280

## Download
[COvib.tgz](https://vasp.at/wiki/images/1/1d/COvib.tgz "COvib.tgz")

[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> [O
atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O dimer](O_dimer.md) \> [CO](../incar-tags/CO.md) \> CO
vibration \> [CO partial DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \> [H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

Back to the [main page](The_VASP_Manual.md).

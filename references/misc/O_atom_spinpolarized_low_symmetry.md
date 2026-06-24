<!-- Source: https://vasp.at/wiki/index.php/O_atom_spinpolarized_low_symmetry | revid: 10454 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# O atom spinpolarized low symmetry
[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> O
atom spinpolarized low symmetry \> [O dimer](O_dimer.md) \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \> [CO partial
DOS](CO_partial_DOS.md) \> [H2O](../incar-tags/H2O.md) \>
[H2O vibration](H2O_vibration.md) \> [H2O molecular
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
- [4 Further things to try](#Further_things_to_try)
- [5 Download](#Download)

## Task
Performing a spin-polarized low symmetry calculation of a single oxygen
atom in a non cubic box to get the right energy minimum.

## Input
### [POSCAR](../input-files/POSCAR.md)
    O atom in a box
     1.0          ! universal scaling parameters
     7.0 0.0 0.0  ! lattice vector  a(1)
     0.0 7.5 0.0  ! lattice vector  a(2)
     0.0 0.0 8.0  ! lattice vector  a(3)
    1             ! number of atoms
    cart          ! positions in cartesian coordinates
     0 0 0

  

### [INCAR](../input-files/INCAR.md)
    SYSTEM = O atom in a box
    ISMEAR = 0  ! Gaussian smearing
    SIGMA  = 0.01
    ISPIN =  2  ! spin polarized calculation

### [KPOINTS](../input-files/KPOINTS.md)
    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

## Calculation
- In the GGA most atoms are characterized by a symmetry broken solution.
  VASP, however, symmetrizes the charge density according to the
  determined symmetry of the cell. Check the
  [OUTCAR](../output-files/OUTCAR.md) file, to see what symmetry VASP is
  using.

&nbsp;

- To lower the symmetry, simply change the lattice parameters to 7.0,
  7.5 and 8.0 in the [POSCAR](../input-files/POSCAR.md) file (see the
  example file above) and reduce [SIGMA](../incar-tags/SIGMA.md) to
  [SIGMA](../incar-tags/SIGMA.md)=0.01 in the [INCAR](../input-files/INCAR.md)
  file.

&nbsp;

- By rerunning VASP one finds a much lower energy:

&nbsp;

    vasp.5.4.1 05Feb16 (build Aug 22 2016 16:46:23) complex
    ...   ...   . ..
    DAV:  15    -0.189071145737E+01   -0.29321E-03   -0.39183E-05    48   0.478E-02    0.995E-03
    DAV:  16    -0.189071145737E+01   -0.27775E-03   -0.39294E-05    40   0.290E-02    0.541E-03
    DAV:  17    -0.189104076616E+01   -0.51555E-04   -0.34087E-06    48   0.132E-02    
       1 F= -.18910408E+01 E0= -.18910408E+01  d E =-.309633E-20  mag=     1.9998

## Further things to try
- How does the energy change when one decreases
  [SIGMA](../incar-tags/SIGMA.md) to [SIGMA](../incar-tags/SIGMA.md)=0.01 in
  the [INCAR](../input-files/INCAR.md) file? Why?

## Download
[Oatomspinlowsym.tgz](https://vasp.at/wiki/images/1/14/Oatomspinlowsym.tgz "Oatomspinlowsym.tgz")

[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> O
atom spinpolarized low symmetry \> [O dimer](O_dimer.md) \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \> [CO partial
DOS](CO_partial_DOS.md) \> [H2O](../incar-tags/H2O.md) \>
[H2O vibration](H2O_vibration.md) \> [H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

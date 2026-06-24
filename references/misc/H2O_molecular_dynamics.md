<!-- Source: https://vasp.at/wiki/index.php/H2O_molecular_dynamics | revid: 32309 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# H2O molecular dynamics
[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> [O
atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O dimer](O_dimer.md) \> [CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \> [CO partial
DOS](CO_partial_DOS.md) \> [H2O](../incar-tags/H2O.md) \>
[H2O vibration](H2O_vibration.md) \> H2O molecular
dynamics \> [Further things to
try](At_and_mol_further.md)  \> [List of
tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Calculation](#Calculation)
- [4 Download](#Download)

## Task
Molecular dynamics calculation for a $\mathrm{H}_{2}\mathrm{O}$ molecule.

## Input
### [POSCAR](../input-files/POSCAR.md)
    H2O _2
    0.52918   ! scaling parameter
     12 0 0
     0 12 0
     0 0 12
    1 2
    select
    cart
         0.00     0.00     0.00 T T F
         1.10    -1.43     0.00 T T F
         1.10     1.43     0.00 T T F

To save time the box size is reduced to 12 a.u.

### [INCAR](../input-files/INCAR.md)
    PREC = Normal    ! standard precision 
    ENMAX = 400      ! cutoff should be set manually
    ISMEAR = 0 ; SIGMA = 0.1
    ISYM = 0         ! strongly recommended for MD
    IBRION = 0       ! molecular dynamics
    NSW = 100        ! 100 steps
    POTIM = 1.0      ! timestep 1 fs
    SMASS = -3       ! Nosé Hoover thermostat
    TEBEG =  2000 ; TEEND = 2000 ! temperature

  

### [KPOINTS](../input-files/KPOINTS.md)
    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

## Calculation
- An example [OSZICAR](../output-files/OSZICAR.md) file (with 1000 steps
  and a step size of 0.5 fs) looks like this:

&nbsp;

    1 T=  2134. E= -.13655511E+02 F= -.14207209E+02 E0=.. EK= 0.55170E+00 SP= 0.00E+00 SK= 0.00E+00
    2 T=  1971. E= -.13643254E+02 F= -.14152912E+02 E0=.. EK= 0.50966E+00 SP= 0.00E+00 SK= 0.00E+00
    3 T=  1336. E= -.13629241E+02 Fd, which just encloses the cutoff sphere corresponding to the plane wave cutoff, is used. This accelerates the calculations by roughly a factor two to three, but causes slight changes in the tot= -.13974630E+02 E0=.. EK= 0.34539E+00 SP= 0.00E+00 SK= 0.00E+00
    4 T=  1011. E= -.13624149E+02 F= -.13885486E+02 E0=.. EK= 0.26134E+00 SP= 0.00E+00 SK= 0.00E+00
    5 T=  1307. E= -.13629772E+02 F= -.13967549E+02 E0=.. EK= 0.33778E+00 SP= 0.00E+00 SK= 0.00E+00

[![](https://vasp.at/wiki/images/thumb/d/dd/Fig_H2O_1.png/800px-Fig_H2O_1.png)](https://vasp.at/wiki/File:Fig_H2O_1.png)

- The pair correlation function can be visualized using e.g. the
  following script:

&nbsp;

- plot_PCDAT

&nbsp;

    awk <PCDAT >PCDAT.dat '
    NR==8 { pcskal=$1}
    NR==9 { pcfein=$1}
    NR>=13 {
     line=line+1
     if (line==257)  {
        print " "
        line=0
     }
     else
        print (line-0.5)*pcfein/pcskal,$1
    }
    '
    cat >plotfile<<!
    # set term postscript enhanced colour lw 2 "Helvetica" 20
    # set output "pair_correlation.eps"
    set title "pair-correlation of H2O at 2000 K"
    set xlabel "r [Angstrom]"
    set ylabel "g(r)"
    plot [0:15] "PCDAT.dat"  w lines
    !
    gnuplot -persist plotfile

## Download
[H2Omd.tgz](https://vasp.at/wiki/images/a/a1/H2Omd.tgz "H2Omd.tgz")

[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> [O
atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O dimer](O_dimer.md) \> [CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \> [CO partial
DOS](CO_partial_DOS.md) \> [H2O](../incar-tags/H2O.md) \>
[H2O vibration](H2O_vibration.md) \> H2O molecular
dynamics \> [Further things to
try](At_and_mol_further.md)  \> [List of
tutorials](../categories/Category-Tutorials.md)

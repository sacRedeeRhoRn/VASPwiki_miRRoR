<!-- Source: https://vasp.at/wiki/index.php/Fcc_Ni_DOS_with_hybrid_functional | revid: 14725 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Ni DOS with hybrid functional
[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
[MgO optimum mixing](MgO_optimum_mixing.md) \>
fcc Ni DOS with hybrid functional \> [Si
bandstructure](Si_bandstructure.md)  \> [List of
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
Calculate fcc Ni DOS using HSE and PBE0 (comparison with PBE).

## Input
### [POSCAR](../input-files/POSCAR.md)
    fcc Ni
     3.53
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0

### [INCAR](../input-files/INCAR.md)
    ## Plot the spin-polarized DOS of fcc Ni 
    ## at HSE and PBE0 level, and compare with
    ## standard PBE.
    ## Better preconverge with PBE first!
        
     SYSTEM = fcc Ni
     ISMEAR = -5
     LORBIT = 11
         
     ISPIN = 2
     MAGMOM = 1
         
    ## Selects the HSE06 hybrid functional
    #LHFCALC = .TRUE. ; HFSCREEN = 0.2 ;
    #ALGO = D ; TIME = 0.4 ; LSUBROT = .TRUE.
         
    ## Selects the PBE0  hybrid functional
    #LHFCALC = .TRUE. ;
    #ALGO = D ; TIME = 0.4 ; LSUBROT = .TRUE.

  

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
    0
    Gamma
      5  5  5
      0  0  0

## Calculation
## Download
[fccNi_hybrid_DOS.tgz](https://vasp.at/wiki/images/2/2b/FccNi_hybrid_DOS.tgz "FccNi hybrid DOS.tgz")

[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
[MgO optimum mixing](MgO_optimum_mixing.md) \>
fcc Ni DOS with hybrid functional \> [Si
bandstructure](Si_bandstructure.md)  \> [List of
tutorials](../categories/Category-Tutorials.md)

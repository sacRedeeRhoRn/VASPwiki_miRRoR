<!-- Source: https://vasp.at/wiki/index.php/Cd_Si_relaxation | revid: 10309 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Cd Si relaxation
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
cd Si relaxation \> [beta-tin Si](Beta-tin_Si.md) \>
[fcc Ni](Fcc_Ni.md) \> [graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Calculation](#Calculation)
- [4 Download](#Download)

## Task
Relaxation of the internal coordinates of a perturbed cd Si structure.

## Input
### [POSCAR](../input-files/POSCAR.md)
    cubic diamond
       5.5
     0.0    0.5     0.5
     0.5    0.0     0.5
     0.5    0.5     0.0
      2
    Direct
     -0.125 -0.125 -0.125
      0.125  0.125  0.130

- Break of symmetry in standard diamond structure: change z position
  from 0.125 to 0.130.

### [INCAR](../input-files/INCAR.md)
    System = diamond Si
    ISTART = 0 ; ICHARG=2
    ENCUT  =    240
    ISMEAR = 0; SIGMA = 0.1;
    NSW    =  10; IBRION =  2
    ISIF   =  2
    EDIFFG = -0.0001

- 10 relaxation steps ([NSW](../incar-tags/NSW.md)=10).
- Conjugate-gradient algorithm ([IBRION](../incar-tags/IBRION.md)=2).
- Relaxation only of internal parameters ([ISIF](../incar-tags/ISIF.md)=2).

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

## Calculation
- Example output after 10 relaxation steps:

&nbsp;

    POSITION                                       TOTAL-FORCE (eV/Angst)
    -----------------------------------------------------------------------------------
         4.81253      4.81253      4.81250        -0.000724     -0.000724     -0.000031
         0.68747      0.68747      0.68750         0.000724      0.000724      0.000031
    -----------------------------------------------------------------------------------
       total drift:                                0.000000      0.000000      0.000000

- Files to watch during relaxations:
  - stdout (terminal): each electronic step is written to the terminal:
  - [OSZICAR](../output-files/OSZICAR.md): a copy of the terminal output.
  - [OUTCAR](../output-files/OUTCAR.md): more detailed information on every
    electronic and ionic step.

&nbsp;

- Other important files:
  - [CONTCAR](../output-files/CONTCAR.md): holds the structure of the last
    ionic step and at the end the structural result (also very important
    for restarting a relaxation).
  - [STOPCAR](../incar-tags/STOPCAR.md): stops a relaxation.

## Download
[diamondSirel.tgz](https://vasp.at/wiki/images/e/eb/DiamondSirel.tgz "DiamondSirel.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
cd Si relaxation \> [beta-tin Si](Beta-tin_Si.md) \>
[fcc Ni](Fcc_Ni.md) \> [graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

Back to the [main page](The_VASP_Manual.md).

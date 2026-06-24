<!-- Source: https://vasp.at/wiki/index.php/Beta-tin_Si | revid: 10311 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Beta-tin Si
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
beta-tin Si \> [fcc Ni](Fcc_Ni.md) \> [graphite TS binding
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
Relaxation of the internal coordinates, volume and cell shape in
beta-tin Si.

## Input
### [POSCAR](../input-files/POSCAR.md)
    beta Sn
        4.9000000000000
     1.0    0.0     0.0
     0.0    1.0     0.0
     0.5    0.5     0.26
      2
    Direct
     -0.125 -0.375  0.25
      0.125  0.375 -0.25

### [INCAR](../input-files/INCAR.md)
    System = beta Si
    ISMEAR = 0; SIGMA = 0.1;
    ENMAX  =  240
    IBRION=2; ISIF=3 ; NSW=15
    EDIFF  = 0.1E-04
    EDIFFG = -0.01

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

## Calculation
This example is completely analagous to [cd Si volume
relaxation](Cd_Si_volume_relaxation.md).

## Download
[2_5_beta-tinSi.tgz](https://vasp.at/wiki/images/5/5f/2_5_beta-tinSi.tgz "2 5 beta-tinSi.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
beta-tin Si \> [fcc Ni](Fcc_Ni.md) \> [graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

Back to the [main page](The_VASP_Manual.md).

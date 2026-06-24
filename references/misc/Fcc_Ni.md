<!-- Source: https://vasp.at/wiki/index.php/Fcc_Ni | revid: 10422 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Ni
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> fcc Ni \> [graphite TS
binding
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
Lattice parameter optimization, calculation of the DOS and bandstructure
in (spin-polarized) fcc Ni.

## Input
### [POSCAR](../input-files/POSCAR.md)
    fcc:
     3.53 
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0

### [INCAR](../input-files/INCAR.md)
      SYSTEM = fcc Ni
      ISTART = 0 ; ICHARG=2
      ENCUT  =    270
      ISMEAR =    1  ; SIGMA = 0.2
      LORBIT = 11
      ISPIN = 2
      MAGMOM = 1

- Initial charge-density from overlapping atoms in starting job.
- Default energy cutoff of 270 eV used
  ([ENCUT](../incar-tags/ENCUT.md)=270).
- MP smearing used since we have a metal.
- Spin-polarized calculation [ISPIN](../incar-tags/ISPIN.md)=2, initial
  moments of 1 ([MAGMOM](../incar-tags/MAGMOM.md)=1).
- Static calculation.

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

- Equally spaced k mesh with 56 points in the IBZ.
- Odd, $\Gamma$-centered mesh.

## Calculation
- The calculations are carried out in analogy to [cd
  Si](Cd_Si.md). Please follow the instructions in that
  example.

&nbsp;

- Here is a sample output of the results:

[![](https://vasp.at/wiki/images/thumb/2/27/Fig_Ni_1.png/800px-Fig_Ni_1.png)](https://vasp.at/wiki/File:Fig_Ni_1.png)

## Download
[fccNi.tgz](https://vasp.at/wiki/images/c/c0/FccNi.tgz "FccNi.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> fcc Ni \> [graphite TS
binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

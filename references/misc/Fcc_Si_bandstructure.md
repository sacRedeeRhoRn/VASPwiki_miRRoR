<!-- Source: https://vasp.at/wiki/index.php/Fcc_Si_bandstructure | revid: 10937 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Si bandstructure
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> fcc Si bandstructure \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> [fcc
Ni](Fcc_Ni.md) \> [graphite TS binding
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
  - [2.4 CHGCAR](#CHGCAR)
- [3 CALCULATION](#CALCULATION)
- [4 Download](#Download)

## Task
Computation of the bandstructure in fcc Si along L-Γ-X-U and K-Γ.

## Input
### [POSCAR](../input-files/POSCAR.md)
    fcc Si:
     3.9
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0

### [INCAR](../input-files/INCAR.md)
    System = fcc Si 
    ICHARG = 11 #charge read file
    ENCUT  =    240
    ISMEAR = 0; SIGMA = 0.1;
    LORBIT = 11

### [KPOINTS](../input-files/KPOINTS.md)
    k-points for bandstructure L-G-X-U K-G
     10
    line
    reciprocal
      0.50000  0.50000  0.50000    1
      0.00000  0.00000  0.00000    1

      0.00000  0.00000  0.00000    1
      0.00000  0.50000  0.50000    1

      0.00000  0.50000  0.50000    1
      0.25000  0.62500  0.62500    1

      0.37500  0.7500   0.37500    1
      0.00000  0.00000  0.00000    1

- k points along the line $L - \Gamma - X - U K -
  \Gamma$.
- 10 points per line.
- Keyword *line* to generate bandstructure.
- In reciprocal coordinates.
- All points with weight 1.
- Example bandstructure should look like this:

[![](https://vasp.at/wiki/images/thumb/b/b7/Fig_Si_5.png/300px-Fig_Si_5.png)](https://vasp.at/wiki/File:Fig_Si_5.png)

### [CHGCAR](../input-files/CHGCAR.md)
This calculation needs a converged charge density as input
([ICHARG](../incar-tags/ICHARG.md)=11). You may use the
[CHGCAR](../input-files/CHGCAR.md) file of the [fcc Si
DOS](Fcc_Si_DOS.md) example.

## CALCULATION
- To copy the self-consistent charge density of example fccSidos to your
  current working directory, type:

&nbsp;

    cp ../fccSidos/CHGCAR .

- You must do this otherwise VASP can not read the
  [CHGCAR](../input-files/CHGCAR.md) and will terminate.

&nbsp;

- To plot the bandstructure use p4vasp:

[![](https://vasp.at/wiki/images/thumb/f/f8/Fig_Si_6.png/800px-Fig_Si_6.png)](https://vasp.at/wiki/File:Fig_Si_6.png)

**Mind**: For this calculations you need the
[CHGCAR](../input-files/CHGCAR.md) file of the [fcc Si DOS
example](Fcc_Si_DOS.md).

## Download
[fccSiband.tgz](https://vasp.at/wiki/images/9/9c/FccSiband.tgz "FccSiband.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> fcc Si bandstructure \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> [fcc
Ni](Fcc_Ni.md) \> [graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

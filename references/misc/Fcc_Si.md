<!-- Source: https://vasp.at/wiki/index.php/Fcc_Si | revid: 10427 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Si
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
fcc Si \> [fcc Si DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
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
- [3 Calculation](#Calculation)
- [4 Download](#Download)

## Task
Lattice constant optimization for fcc Si.

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

- Fcc Si lattice constant of 3.9 $\AA$.
- 1 atom per unit cell.

### [INCAR](../input-files/INCAR.md)
    System = fcc Si
    ISTART = 0 ; ICHARG = 2
    ENCUT = 240
    ISMEAR = 0; SIGMA = 0.1

- Initial charge density form overlapping atoms.
- Energy cutoff of 240 eV from [POTCAR](../input-files/POTCAR.md) file.

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

- Equally spaced k mesh.
- Odd number of k points in each direction results in a
  $\Gamma$ centered mesh.
- 56 k points in IBZ.

## Calculation
- Calculate energy for different lattice parameters.
- Fit to some equation of states to obtain the equilibrium volume.

&nbsp;

- The bash-script `loop.sh` runs fcc Si at several different lattice
  constants (3.5-4.3 Å) and collects free energy versus lattice constant
  into the file SUMMARY.fcc

&nbsp;

    #! /bin/bash
    BIN=/path/to/your/vasp/executable
    rm WAVECAR SUMMARY.fcc
    for i in  3.5 3.6 3.7 3.8 3.9 4.0 4.1 4.2 4.3 ; do
    cat >POSCAR <<!
    fcc:
       $i
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0
    !
    echo "a= $i" ; mpirun -np 2 $BIN
    E=`awk '/F=/ {print $0}' OSZICAR` ; echo $i $E  >>SUMMARY.fcc
    done
    cat SUMMARY.fcc

The output for the SUMMARY.fcc file within this example should look like
this:

    3.5 1 F= -.44256712E+01 E0= -.44233993E+01 d E =-.454388E-02
    3.6 1 F= -.46614699E+01 E0= -.46600410E+01 d E =-.285796E-02
    3.7 1 F= -.47979864E+01 E0= -.47959298E+01 d E =-.411323E-02
    3.8 1 F= -.48645042E+01 E0= -.48630063E+01 d E =-.299564E-02
    3.9 1 F= -.48773847E+01 E0= -.48758538E+01 d E =-.306176E-02
    4.0 1 F= -.48487436E+01 E0= -.48481092E+01 d E =-.126878E-02
    4.1 1 F= -.47852634E+01 E0= -.47844854E+01 d E =-.155599E-02
    4.2 1 F= -.46936947E+01 E0= -.46922530E+01 d E =-.288339E-02
    4.3 1 F= -.45831167E+01 E0= -.45811837E+01 d E =-.386598E-02

- To make a quick plot of SUMMARY.fcc try:

&nbsp;

    gnuplot
    gnuplot> plot "SUMMARY.fcc" using ($1):($4) w lp

- The equilibrium lattice constant is found at roughly 3.9 Å. Adjust
  your [POSCAR](../input-files/POSCAR.md) file to reflect this and rerun
  VASP.

&nbsp;

- Keep your [CHGCAR](../input-files/CHGCAR.md) file from this run. We will
  need it in the following examples.

&nbsp;

- A quick look at the results:

[![](https://vasp.at/wiki/images/thumb/f/ff/Fig_Si_1.png/800px-Fig_Si_1.png)](https://vasp.at/wiki/File:Fig_Si_1.png)

**Mind**: You will have to set the correct path to your VASP executable
(i.e., `BIN`), and invoke VASP with the correct command (e.g., in the
above: `mpirun -np 2`).

## Download
[fccSi.tgz](https://vasp.at/wiki/images/6/6a/FccSi.tgz "FccSi.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
fcc Si \> [fcc Si DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
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

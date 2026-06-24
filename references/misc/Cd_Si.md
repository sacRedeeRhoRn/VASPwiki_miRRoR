<!-- Source: https://vasp.at/wiki/index.php/Cd_Si | revid: 10305 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Cd Si
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> cd
Si \> [cd Si volume
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
  - [3.1 Volume relaxation](#Volume_relaxation)
  - [3.2 DOS](#DOS)
  - [3.3 Bandstructure](#Bandstructure)
- [4 Download](#Download)

## Task
Volume relaxtion and the calculation of the DOS and bandstructure within
cubic diamond (cd) Si.

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
      0.125  0.125  0.125

- Cubic diamond Si starting lattice constant of 5.5
  $\AA$.
- Fcc cell.
- 2 atoms in cell.

### [INCAR](../input-files/INCAR.md)
    System = diamond Si
    ISTART = 0 ; ICHARG=2
    ENCUT  =    240
    ISMEAR = 0; SIGMA = 0.1

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

## Calculation
The calculation of the optimized volume. DOS and bandstructure is
similar as in the examples [fcc_Si](Fcc_Si.md),
[fcc_Si_DOS](Fcc_Si_DOS.md) and
[fcc_Si_bandstructure](Fcc_Si_bandstructure.md),
respectively.

### Volume relaxation
- The bash-script `loop.sh` runs Si in the cubic diamond (cd) structure
  at several different lattice constants (5.1-5.7 Å) and collects free
  energy versus lattice constant into the file SUMMARY.dia:

&nbsp;

    #! /bin/bash
    BIN=/path/to/your/vasp/executable
    rm WAVECAR SUMMARY.dia
    for i in  5.1 5.2 5.3 5.4 5.5 5.6 5.7 ; do
    cat >POSCAR <<!
    cubic diamond
       $i 
     0.0    0.5     0.5
     0.5    0.0     0.5
     0.5    0.5     0.0
      2
    Direct
     -0.125 -0.125 -0.125
      0.125  0.125  0.125
    !
    echo "a= $i" ; mpirun -n 2 $BIN
    E=`awk '/F=/ {print $0}' OSZICAR` ; echo $i $E  >>SUMMARY.dia
    done
    cat SUMMARY.dia

- Example output of SUMMARY.dia:

&nbsp;

    5.2 1 F= -.10528151E+02 E0= -.10528137E+02 d E =-.274709E-04
    5.3 1 F= -.10713281E+02 E0= -.10713280E+02 d E =-.218410E-05
    5.4 1 F= -.10806685E+02 E0= -.10806685E+02 d E =-.114401E-06
    5.5 1 F= -.10823039E+02 E0= -.10823039E+02 d E =-.429842E-08
    5.6 1 F= -.10775102E+02 E0= -.10775102E+02 d E =-.204668E-09
    5.7 1 F= -.10673578E+02 E0= -.10673578E+02 d E =-.112715E-10
    5.8 1 F= -.10528393E+02 E0= -.10528393E+02 d E =-.552513E-11

- To make a quick plot of SUMMARY.dia try:

&nbsp;

    gnuplot
    gnuplot> plot "SUMMARY.dia" using ($1):($4) w lp

- Extracted lattice parameter should be at 5.465 $\AA$.

### DOS
- Enter (approximate) volume of 5.5 $\AA$ into the [POSCAR](../input-files/POSCAR.md) file.

&nbsp;

- Change the [INCAR](../input-files/INCAR.md) according to DOS calculation
  (or use INCAR.dos):

&nbsp;

    System = diamond Si
    ISTART = 0 ; ICHARG=2
    ENCUT  =    240
    ISMEAR = -5
    LORBIT = 11

- Use p4vasp or run the script *dos.sh* to calculate the DOS.

&nbsp;

- The example DOS should look like this:

[![](https://vasp.at/wiki/images/thumb/f/f2/Fig_cdSi_1.png/300px-Fig_cdSi_1.png)](https://vasp.at/wiki/File:Fig_cdSi_1.png)

### Bandstructure
- Enter (approximate) volume of 5.5 $\AA$ into the [POSCAR](../input-files/POSCAR.md) file.

&nbsp;

- Change the [INCAR](../input-files/INCAR.md) according to bandstructure
  calculation (or use INCAR.band):

&nbsp;

    System = diamond Si
    ISTART = 0 ; ICHARG=11
    ENCUT  =    240
    ISMEAR = 0; SIGMA = 0.1;
    LORBIT = 11

- Use p4vasp or run the script *band.sh* to calculate the bandstructure.

&nbsp;

- The example bandstructure should look like this:

[![](https://vasp.at/wiki/images/thumb/0/0c/Fig_cdSi_2.png/300px-Fig_cdSi_2.png)](https://vasp.at/wiki/File:Fig_cdSi_2.png)

- For "fat" bands (or orbital character of bands) use p4vasp:

[![](https://vasp.at/wiki/images/thumb/8/8d/Fig_cdSi3.png/800px-Fig_cdSi3.png)](https://vasp.at/wiki/File:Fig_cdSi3.png)

**Mind**: You will have to set the correct path to your VASP executable
(i.e., `BIN`), and invoke VASP with the correct command (e.g., in the
above: `mpirun -np 2`).

## Download
[diamondSi.tgz](https://vasp.at/wiki/images/b/be/DiamondSi.tgz "DiamondSi.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> cd
Si \> [cd Si volume
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

Back to the [main page](The_VASP_Manual.md).

<!-- Source: https://vasp.at/wiki/index.php/Fcc_Si_DOS | revid: 10428 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Si DOS
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> fcc Si DOS \> [fcc Si
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
Calculation of the DOS in fcc Si.

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
    # ICHARG = 11 #charge read file
    ENCUT  =    240
    ISMEAR = -5 #tetrahedron
    LORBIT = 11

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
     0
    Monkhorst Pack
     21 21 21
     0  0  0

## Calculation
- Perform a static ([NSW](../incar-tags/NSW.md)=0,
  [IBRION](../incar-tags/IBRION.md)=-1) self consistent calculation for
  the DOS (the DOS is found in the [DOSCAR](../output-files/DOSCAR.md) file.

&nbsp;

- For large systems:
  - Converge with a small number of k points.
  - Increase the number of k points for the DOS and set
    [ICHARG](../incar-tags/ICHARG.md)=11 (charge density from the last
    self-consistent run). [ICHARG](../incar-tags/ICHARG.md)=11 treats each
    k point independently and keeps the charge density and the potential
    fixed.

&nbsp;

- Read [CHGCAR](../input-files/CHGCAR.md) from previous run. To copy the
  self-consistent charge density of example
  [fcc_Si](Fcc_Si.md) to your current working

directory (assumed to be fccSidos), type: \$ cp ../fccSi/CHGCAR . You
must do this otherwise VASP can not read the
[CHGCAR](../input-files/CHGCAR.md) and will terminate.

- The smearing of the k points is set to the tetrahedron method with
  Blöchl corrections ([ISMEAR](../incar-tags/ISMEAR.md)=-5 to fi the
  problem

[![](https://vasp.at/wiki/images/thumb/0/05/Fig_Si_2.png/300px-Fig_Si_2.png)](https://vasp.at/wiki/File:Fig_Si_2.png)

- To plot the DOS use p4vasp:

[![](https://vasp.at/wiki/images/thumb/f/fe/Fig_Si_3.png/600px-Fig_Si_3.png)](https://vasp.at/wiki/File:Fig_Si_3.png)

  

- Alternatively the bash-script `plotdos.sh` invokes *awk* and *gnuplot*
  to get the DOS from the [vasprun.xml](../output-files/Vasprun.xml.md)
  file and plot it.

&nbsp;

    awk 'BEGIN{i=1} /dos>/,\
                    /\/dos>/ \
                     {a[i]=$2 ; b[i]=$3 ; i=i+1} \
         END{for (j=12;j<i-5;j++) print a[j],b[j]}' vasprun.xml > dos.dat

    ef=`awk '/efermi/ {print $3}' vasprun.xml`

    cat >plotfile<<!
    # set term postscript enhanced eps colour lw 2 "Helvetica" 20
    # set output "optics.eps"
    plot "dos.dat" using (\$1-$ef):(\$2) w lp
    ! 

    gnuplot -persist plotfile

    rm dos.dat plotfile

[![](https://vasp.at/wiki/images/thumb/c/c1/Fig_Si_4.png/600px-Fig_Si_4.png)](https://vasp.at/wiki/File:Fig_Si_4.png)

## Download
[fccSidos.tgz](https://vasp.at/wiki/images/6/65/FccSidos.tgz "FccSidos.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> fcc Si DOS \> [fcc Si
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

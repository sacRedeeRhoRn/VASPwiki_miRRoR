<!-- Source: https://vasp.at/wiki/index.php/STM_of_graphene | revid: 10463 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# STM of graphene
[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \> [Ni 111
surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of graphite](STM_of_graphite.md) \> STM of
graphene \> [collective jumps of a Pt adatom on fcc-Pt (001): Nudged
Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
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
Generation of an STM image of a graphene surface.

## Input
### [POSCAR](../input-files/POSCAR.md)
    C: Graphite Lattice
    1.0
     +2.4410462393  +0.0000000000  +0.0000000000 
     -1.2205231197  +2.1140080551  +0.0000000000 
     +0.0000000000  +0.0000000000 +10.0000000000 
      2
    Cartesian
     +0.0000000000  +0.0000000000  +0.0000000000 
     +0.0000000000  +1.4093387034  +0.0000000000 

### [INCAR](../input-files/INCAR.md)
    general:
      SYSTEM = Graphite surface slap
      ENMAX  = 400
      ISMEAR =    2  ; SIGMA = 0.2
      ALGO = Fast
       
    partial charge densities:
      LPARD = .TRUE.
      LSEPK = .FALSE.
      LSEPB = .FALSE.
      NBMOD = -3
      EINT = -0.1 0.1
        
    #DOS:
      #ISTART = 0
      #ICHARG = 2
      #LORBIT = 11

### [KPOINTS](../input-files/KPOINTS.md)
    K-Points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation
- This example is carried out in complete analogy to the example [STM of
  graphite](STM_of_graphite.md).

&nbsp;

- The sample output for the graphite (left) and graphene (right) STM
  images should look like the following:

[![](https://vasp.at/wiki/images/thumb/4/43/Fig_graphene_STM_1.png/800px-Fig_graphene_STM_1.png)](https://vasp.at/wiki/File:Fig_graphene_STM_1.png)

## Download
[Graphene_STM.tgz](https://vasp.at/wiki/images/e/e0/Graphene_STM.tgz "Graphene STM.tgz")

[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \> [Ni 111
surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of graphite](STM_of_graphite.md) \> STM of
graphene \> [collective jumps of a Pt adatom on fcc-Pt (001): Nudged
Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of tutorials](../categories/Category-Tutorials.md)

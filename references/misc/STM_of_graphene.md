<!-- Source: https://vasp.at/wiki/index.php/STM_of_graphene | revid: 10463 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# STM of graphene



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \>
[Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of
graphite](STM_of_graphite.md) \>
STM of
graphene \> [collective
jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#Task)
- [2
  Input](#Input)
  - [2.1
    POSCAR](#POSCAR)
  - [2.2
    INCAR](#INCAR)
  - [2.3
    KPOINTS](#KPOINTS)
- [3
  Calculation](#Calculation)
- [4
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=STM_of_graphene&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Generation of an STM image of a graphene surface.

## Input\[<a
href="/wiki/index.php?title=STM_of_graphene&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=STM_of_graphene&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    C: Graphite Lattice
    1.0
     +2.4410462393  +0.0000000000  +0.0000000000 
     -1.2205231197  +2.1140080551  +0.0000000000 
     +0.0000000000  +0.0000000000 +10.0000000000 
      2
    Cartesian
     +0.0000000000  +0.0000000000  +0.0000000000 
     +0.0000000000  +1.4093387034  +0.0000000000 

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=STM_of_graphene&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

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

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=STM_of_graphene&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    K-Points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation\[<a
href="/wiki/index.php?title=STM_of_graphene&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- This example is carried out in complete analogy to the example [STM of
  graphite](STM_of_graphite.md).

<!-- -->

- The sample output for the graphite (left) and graphene (right) STM
  images should look like the following:

<a href="/wiki/File:Fig_graphene_STM_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/43/Fig_graphene_STM_1.png/800px-Fig_graphene_STM_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/43/Fig_graphene_STM_1.png/1200px-Fig_graphene_STM_1.png 1.5x, /wiki/images/4/43/Fig_graphene_STM_1.png 2x"
width="800" height="603" /></a>

## Download\[<a
href="/wiki/index.php?title=STM_of_graphene&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/e/e0/Graphene_STM.tgz" class="internal"
title="Graphene STM.tgz">Graphene_STM.tgz</a>


[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \>
[Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of
graphite](STM_of_graphite.md) \>
STM of
graphene \> [collective
jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of
tutorials](../categories/Category-Tutorials.md)



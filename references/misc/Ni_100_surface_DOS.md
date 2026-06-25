<!-- Source: https://vasp.at/wiki/index.php/Ni_100_surface_DOS | revid: 10441 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Ni 100 surface DOS



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
Ni 100 surface
DOS \> [Ni 100 surface
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
[STM of
graphene](STM_of_graphene.md) \>
[collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
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
href="/wiki/index.php?title=Ni_100_surface_DOS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the local density of states (LDOS) of a Ni (100) surface.

## Input\[<a
href="/wiki/index.php?title=Ni_100_surface_DOS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_DOS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    fcc (100) surface                       
       3.53000000000000     
         0.5000000000000000    0.5000000000000000    0.0000000000000000
        -0.5000000000000000    0.5000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    5.0000000000000000
       Ni
         5
    Selective dynamics
    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000   F   F   F
      0.5000000000000000  0.5000000000000000  0.1000000000000014   F   F   F
      0.0000000000000000  0.0000000000000000  0.2000000000000028   F   F   F
      0.5000000000000000  0.5000000000000000  0.3004245271852446   T   T   T
      0.0000000000000000 -0.0000000000000000  0.3959414474619545   T   T   T
     
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00

  

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_DOS&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    general:
      SYSTEM = clean (100) Ni surface
      ENMAX = 270
      ISMEAR =   -5
      ALGO = Normal 
        
    spin:
      ISPIN = 2
      MAGMOM = 5*1   
        
      LORBIT = 11  # lm and site decomposed DOS inside PAW spheres

- Using the tetrahedron method (with Blöchl corrections).
- LM and site decomposed DOS.
- N.B.: We want to use the optimized structure of [Ni 100 surface
  relaxation](Ni_100_surface_relaxation.md).
  Normally this would mean copying the
  [CONTCAR](../output-files/CONTCAR.md) file of [Ni 100 surface
  relaxation](Ni_100_surface_relaxation.md)
  to the [POSCAR](../input-files/POSCAR.md) file in the directory where you
  want to run Ni 100 surface
  DOS.

In this case, however, that has already been taken care of and the
[POSCAR](../input-files/POSCAR.md) file from the downloadable tar file is
the correct one.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_DOS&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation\[<a
href="/wiki/index.php?title=Ni_100_surface_DOS&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- At the end of the
  <a href="/wiki/index.php?title=OUCAR&amp;action=edit&amp;redlink=1"
  class="new" title="OUCAR (page does not exist)">OUCAR</a> file the
  information on the local charge and magnetization is given.

<!-- -->

     total charge
    # of ion     s       p       d       tot
    ----------------------------------------
      1        0.461   0.316   8.331   9.108
      2        0.483   0.466   8.323   9.273
      3        0.484   0.462   8.324   9.270
      4        0.490   0.481   8.329   9.300
      5        0.472   0.337   8.341   9.150
    ----------------------------------------
    tot        2.390   2.062  41.648  46.100
      
     
     total charge
    # of ion     s       p       d       tot
    ----------------------------------------
      1       -0.003  -0.019   0.715   0.692
      2       -0.008  -0.023   0.619   0.588
      3       -0.007  -0.024   0.620   0.589
      4       -0.008  -0.024   0.622   0.591
      5       -0.004  -0.020   0.705   0.681
    ----------------------------------------
    tot       -0.030  -0.110   3.281   3.141

- Using [LORBIT](../incar-tags/LORBIT.md)=1 and changing
  [RWIGS](../incar-tags/RWIGS.md) the total number of electrons within the
  spheres coud be adapted (nickel pseudo-potential has a valence of 10).

<!-- -->

- Enhancement of the magnetic moment at the surface.

<!-- -->

- Magnetic moment int the center "bulk like".

<!-- -->

- The surface and bulk projected-DOS plotted for each spin component
  spearately should show a band narrowing and larger exchange splitting
  at the surface:

<a href="/wiki/File:Fig_Ni_100_surfDOS_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/d/d7/Fig_Ni_100_surfDOS_1.png/500px-Fig_Ni_100_surfDOS_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/d/d7/Fig_Ni_100_surfDOS_1.png/750px-Fig_Ni_100_surfDOS_1.png 1.5x, /wiki/images/d/d7/Fig_Ni_100_surfDOS_1.png 2x"
width="500" height="420" /></a>

- The DOS of can be plotted using p4vasp:

<a href="/wiki/File:Fig_Ni_100_surfDOS_2.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/40/Fig_Ni_100_surfDOS_2.png/800px-Fig_Ni_100_surfDOS_2.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/40/Fig_Ni_100_surfDOS_2.png/1200px-Fig_Ni_100_surfDOS_2.png 1.5x, /wiki/images/thumb/4/40/Fig_Ni_100_surfDOS_2.png/1600px-Fig_Ni_100_surfDOS_2.png 2x"
width="800" height="523" /></a>

## Download\[<a
href="/wiki/index.php?title=Ni_100_surface_DOS&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/6/63/Ni100clean_LDOS.tgz" class="internal"
title="Ni100clean LDOS.tgz">Ni100clean_LDOS.tgz</a>


[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
Ni 100 surface
DOS \> [Ni 100 surface
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
[STM of
graphene](STM_of_graphene.md) \>
[collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of
tutorials](../categories/Category-Tutorials.md)



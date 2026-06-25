<!-- Source: https://vasp.at/wiki/index.php/Ni_100_surface_bandstructure | revid: 10440 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Ni 100 surface bandstructure



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
Ni 100 surface
bandstructure \> [Ni
111 surface
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
  Task](#task)
- [2
  Input](#input)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    INCAR](#incar)
  - [2.3
    KPOINTS](#kpoints)
- [3
  Calculation](#calculation)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Ni_100_surface_bandstructure&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the bandstructure of a Ni (100) surface.

## Input\[<a
href="/wiki/index.php?title=Ni_100_surface_bandstructure&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_bandstructure&amp;veaction=edit&amp;section=3"
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
href="/wiki/index.php?title=Ni_100_surface_bandstructure&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

      ICHARG = 11
    general:
      SYSTEM = clean (100) nickel surface
      ENMAX  = 270
      ISMEAR = 2 ; SIGMA = 0.2
      ALGO = Normal
        
    spin:
      ISPIN = 2
      MAGMOM = 5*1
        
      LORBIT = 11

- [ICHARG](../incar-tags/ICHARG.md)=11: Read in charge density (1) and do
  not update it (+10) - non-selfconsistent run.
- N.B.: You need to topy the [CHGCAR](../input-files/CHGCAR.md) file of
  example [Ni 100 surface
  DOS](Ni_100_surface_DOS.md) into the directory
  where you want to run this calculation.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_bandstructure&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    kpoints for band-structure G-X-M-G
      13
    reziprok
       .00000   .00000   .00000    1
       .12500   .00000   .00000    1
       .25000   .00000   .00000    1
       .37500   .00000   .00000    1
       .50000   .00000   .00000    1

       .50000   .12500   .00000    1
       .50000   .25000   .00000    1
       .50000   .37500   .00000    1
       .50000   .50000   .00000    1

       .37500   .37500   .00000    1
       .25000   .25000   .00000    1
       .12500   .12500   .00000    1
       .00000   .00000   .00000    1

<a href="/wiki/File:Fig_Ni_100_surfband_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/5/5b/Fig_Ni_100_surfband_1.png/200px-Fig_Ni_100_surfband_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/5/5b/Fig_Ni_100_surfband_1.png/300px-Fig_Ni_100_surfband_1.png 1.5x, /wiki/images/thumb/5/5b/Fig_Ni_100_surfband_1.png/400px-Fig_Ni_100_surfband_1.png 2x"
width="200" height="273" /></a>

- 13 k points along line $\Gamma - X - M - \Gamma$.
- The coordinates are given in reciprocal coordinates.
- Each point has weight 1.

## Calculation\[<a
href="/wiki/index.php?title=Ni_100_surface_bandstructure&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- In the [OUTCAR](../output-files/OUTCAR.md) file the status message on the
  actual job (non-selfconsistent calculation) is given:

<!-- -->

    ...
    Static calculation
    charge density remains constant during run
    spin polarized calculation
    ...

- The bandstructure can be plotted using p4vasp:

<a href="/wiki/File:Fig_Ni_100_surfband_3.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/e/ec/Fig_Ni_100_surfband_3.png/800px-Fig_Ni_100_surfband_3.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/e/ec/Fig_Ni_100_surfband_3.png/1200px-Fig_Ni_100_surfband_3.png 1.5x, /wiki/images/e/ec/Fig_Ni_100_surfband_3.png 2x"
width="800" height="540" /></a>

## Download\[<a
href="/wiki/index.php?title=Ni_100_surface_bandstructure&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/8/81/Ni100clean_band.tgz" class="internal"
title="Ni100clean band.tgz">Ni100clean_band.tgz</a>


[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
Ni 100 surface
bandstructure \> [Ni
111 surface
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



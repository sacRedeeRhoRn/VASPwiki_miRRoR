<!-- Source: https://vasp.at/wiki/index.php/CO_on_Ni_111_surface | revid: 31461 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CO on Ni 111 surface



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
CO on Ni 111
surface \> [Ni 111
surface high
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
href="/wiki/index.php?title=CO_on_Ni_111_surface&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Adsorbtion of a CO molecule at the top site of a Ni (111) surface.

## Input\[<a
href="/wiki/index.php?title=CO_on_Ni_111_surface&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=CO_on_Ni_111_surface&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    Ni - (111) + CO on-top
      3.53
       .70710678  .0000000  .000000
     -0.35355339 0.6123724  .000000
       .000000    .000000  5.1961524
        5 1 1
    selective dynamics
    direct
       .00000000   .00000000   .00000000  F  F  F
       .33333333   .66666667   .11111111  F  F  F
       .66666667   .33333333   .22222222  F  F  F
       .00000000   .00000000   .33333333  T  T  T
       .33333333   .66666667   .44444444  T  T  T
       .33333333   .66666667   .54029062  T  T  T
       .33333333   .66666667   .60298866  T  T  T

- CO molecule put above surface atom "on-top".
- $z_{\mathrm{C}}=(.540-.444)\cdot 5.196 \cdot 3.53 \approx 1.76$ $\AA$.
- $d_{\mathrm{CO}}=(.603-.540)\cdot 5.196 \cdot 3.53 \approx 1.16$ $\AA$.

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=CO_on_Ni_111_surface&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

      ISTART = 0
      ICHARG = 2
         
    general:
      SYSTEM = CO adsorption on Ni(111)
      ENMAX  = 400
      ISMEAR =    2  ; SIGMA = 0.2
      ALGO= Fast
      EDIFF = 1E-6
        
    dynamic:
      NSW=100
      POTIM = 0.2
      IBRION = 1

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=CO_on_Ni_111_surface&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    K-Points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation\[<a
href="/wiki/index.php?title=CO_on_Ni_111_surface&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- Two additional atom types (C and O) in the calculations: append C and
  O potentials to the [POTCAR](../input-files/POTCAR.md) file.

<!-- -->

- The sample output for the forces should look like the following:

<!-- -->

    POSITION                                       TOTAL-FORCE (eV/Angst)
    -----------------------------------------------------------------------------------
         0.00000      0.00000      0.00000         0.000000      0.000000      0.175780
         0.00000      1.44112      2.03805         0.000000      0.000000     -0.104008
         1.24804      0.72056      4.07609         0.000000      0.000000     -0.036305
         0.00000      0.00000      6.10852         0.000000      0.000000     -0.083336
         0.00000      1.44112      8.15366         0.000000      0.000000      0.009539
         0.00000      1.44112      9.90873         0.000000      0.000000      0.011228
         0.00000      1.44112     11.06339         0.000000      0.000000      0.027102
    -----------------------------------------------------------------------------------
       total drift:                               -0.000093     -0.000213      0.019852

- Small outward relaxation of surface due to adsorption:
  $\Delta d_{12} = (8.154-6.109)/2.038 = 0.4 \\$.

<!-- -->

- CO geometry change: $d_{\mathrm{CO}} = 11.063 -
  9.909 = 1.155$ $\AA$;
  $z_{\mathrm{C}} = 9.909 -8.154 = 1.755$
  $\AA$.

<!-- -->

- Visualize the structure using p4vasp:

<a href="/wiki/File:Fig_CO_on_Ni111_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/f3/Fig_CO_on_Ni111_1.png/500px-Fig_CO_on_Ni111_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/f3/Fig_CO_on_Ni111_1.png/750px-Fig_CO_on_Ni111_1.png 1.5x, /wiki/images/f/f3/Fig_CO_on_Ni111_1.png 2x"
width="500" height="662" /></a>

## Download\[<a
href="/wiki/index.php?title=CO_on_Ni_111_surface&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/a/a8/COonNi111_rel.tgz" class="internal"
title="COonNi111 rel.tgz">COonNi111_rel.tgz</a>


[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
CO on Ni 111
surface \> [Ni 111
surface high
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


Back to the [main page](The_VASP_Manual.md).



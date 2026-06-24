<!-- Source: https://vasp.at/wiki/index.php/CO_on_Ni_111_surface | revid: 31461 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CO on Ni 111 surface
[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
CO on Ni 111 surface \> [Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of graphite](STM_of_graphite.md) \> [STM of
graphene](STM_of_graphene.md) \> [collective jumps
of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
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
Adsorbtion of a CO molecule at the top site of a Ni (111) surface.

## Input
### [POSCAR](../input-files/POSCAR.md)
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
- $z_{\mathrm{C}}=(.540-.444)\cdot 5.196 \cdot
  3.53 \approx 1.76$ $\AA$.
- $d_{\mathrm{CO}}=(.603-.540)\cdot 5.196 \cdot
  3.53 \approx 1.16$ $\AA$.

### [INCAR](../input-files/INCAR.md)
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

### [KPOINTS](../input-files/KPOINTS.md)
    K-Points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation
- Two additional atom types (C and O) in the calculations: append C and
  O potentials to the [POTCAR](../input-files/POTCAR.md) file.

&nbsp;

- The sample output for the forces should look like the following:

&nbsp;

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

&nbsp;

- CO geometry change: $d_{\mathrm{CO}} = 11.063 -
  9.909 = 1.155$ $\AA$;
  $z_{\mathrm{C}} = 9.909 -8.154 = 1.755$ $\AA$.

&nbsp;

- Visualize the structure using p4vasp:

[![](https://vasp.at/wiki/images/thumb/f/f3/Fig_CO_on_Ni111_1.png/500px-Fig_CO_on_Ni111_1.png)](https://vasp.at/wiki/File:Fig_CO_on_Ni111_1.png)

## Download
[COonNi111_rel.tgz](https://vasp.at/wiki/images/a/a8/COonNi111_rel.tgz "COonNi111 rel.tgz")

[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
CO on Ni 111 surface \> [Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of graphite](STM_of_graphite.md) \> [STM of
graphene](STM_of_graphene.md) \> [collective jumps
of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of tutorials](../categories/Category-Tutorials.md)

Back to the [main page](The_VASP_Manual.md).

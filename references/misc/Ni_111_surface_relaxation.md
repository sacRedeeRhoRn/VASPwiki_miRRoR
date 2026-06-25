<!-- Source: https://vasp.at/wiki/index.php/Ni_111_surface_relaxation | revid: 10444 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Ni 111 surface relaxation



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
Ni 111 surface
relaxation \> [CO on Ni
111
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
href="/wiki/index.php?title=Ni_111_surface_relaxation&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Relaxation of the first two layers of a Ni (111) surface.

## Input\[<a
href="/wiki/index.php?title=Ni_111_surface_relaxation&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Ni_111_surface_relaxation&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

     fcc (111) surface
      3.53
       .70710678  .0000000  .000000
     -0.35355339 0.6123724  .000000
       .000000    .000000  5.1961524
        5
    selective dynamics
    direct
       .00000000   .00000000   .00000000  F  F  F
       .33333333   .66666667   .11111111  F  F  F
       .66666667   .33333333   .22222222  F  F  F
       .00000000   .00000000   .33333333  T  T  T
       .33333333   .66666667   .44444444  T  T  T

- Similar setup as for [Ni 100 surface
  relaxation](Ni_100_surface_relaxation.md).
- Again 2 of 5 layers relaxed.
- $(1-.444)\cdot 5.196 \cdot 3.53 \approx 10.2$
  $\AA$ of vacuum.

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Ni_111_surface_relaxation&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    general:
      ISTART = 0
      ICHARG = 2
      SYSTEM = clean (111) surface
      ENMAX = 270
      ISMEAR = 2 ; SIGMA = 0.2
      ALGO = Fast
      EDIFF = 1E-6
        
    dynamic:
      NSW = 100
      POTIM = 0.8
      IBRION = 1

- Same [INCAR](../input-files/INCAR.md) file as for [Ni 100 surface
  relaxation](Ni_100_surface_relaxation.md),
  but spin polarization neglected.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Ni_111_surface_relaxation&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation\[<a
href="/wiki/index.php?title=Ni_111_surface_relaxation&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- N.B.: The setup for the calculation of the "bulk" energy can be found
  in the *Ni111clean_rel/bulk* subdirectory of the tar file.

<!-- -->

- The sample output for the forces should look like the following:

<!-- -->

    POSITION                                       TOTAL-FORCE (eV/Angst)
    -----------------------------------------------------------------------------------
         0.00000      0.00000      0.00000         0.000000      0.000000      0.178848
         0.00000      1.44112      2.03805         0.000000      0.000000     -0.060127
         1.24804      0.72056      4.07609         0.000000      0.000000      0.004418
         0.00000      0.00000      6.11522         0.000000      0.000000      0.036384
         0.00000      1.44112      8.14905         0.000000      0.000000     -0.159523
    -----------------------------------------------------------------------------------
       total drift:                               -0.000084      0.000107     -0.017457

- Forces are already small at the beginning (small relaxations for
  compact surfaces).

<!-- -->

- For surface energy non-spin-polarized bulk nickel as reference:
  - $\sigma^{\mathrm{unrel}} =
    \frac{1}{2} (-25.731 - 5 \cdot (-5.407)) = 0.65$
    eV.
  - \(111\) surface more stable than (100) surface.

## Download\[<a
href="/wiki/index.php?title=Ni_111_surface_relaxation&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/1/11/Ni111clean_rel.tgz" class="internal"
title="Ni111clean rel.tgz">Ni111clean_rel.tgz</a>


[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
Ni 111 surface
relaxation \> [CO on Ni
111
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



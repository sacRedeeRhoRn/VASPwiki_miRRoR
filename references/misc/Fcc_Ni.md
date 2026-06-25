<!-- Source: https://vasp.at/wiki/index.php/Fcc_Ni | revid: 10422 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Ni



[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
[fcc Si
bandstructure](Fcc_Si_bandstructure.md) \>
[cd
Si](Cd_Si.md) \>
[cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si
relaxation](Cd_Si_relaxation.md) \>
[beta-tin
Si](Beta-tin_Si.md) \>
fcc
Ni \> [graphite TS
binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
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


## Task\[<a href="/wiki/index.php?title=Fcc_Ni&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Lattice parameter optimization, calculation of the DOS and bandstructure
in (spin-polarized) fcc Ni.

## Input\[<a href="/wiki/index.php?title=Fcc_Ni&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a href="/wiki/index.php?title=Fcc_Ni&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    fcc:
     3.53 
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0

### [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=Fcc_Ni&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

      SYSTEM = fcc Ni
      ISTART = 0 ; ICHARG=2
      ENCUT  =    270
      ISMEAR =    1  ; SIGMA = 0.2
      LORBIT = 11
      ISPIN = 2
      MAGMOM = 1

- Initial charge-density from overlapping atoms in starting job.
- Default energy cutoff of 270 eV used
  ([ENCUT](../incar-tags/ENCUT.md)=270).
- MP smearing used since we have a metal.
- Spin-polarized calculation [ISPIN](../incar-tags/ISPIN.md)=2, initial
  moments of 1 ([MAGMOM](../incar-tags/MAGMOM.md)=1).
- Static calculation.

### [KPOINTS](../input-files/KPOINTS.md)\[<a href="/wiki/index.php?title=Fcc_Ni&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

- Equally spaced k mesh with 56 points in the IBZ.
- Odd, $\Gamma$-centered mesh.

## Calculation\[<a href="/wiki/index.php?title=Fcc_Ni&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- The calculations are carried out in analogy to [cd
  Si](Cd_Si.md). Please follow the instructions in that
  example.

<!-- -->

- Here is a sample output of the results:

<a href="/wiki/File:Fig_Ni_1.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/2/27/Fig_Ni_1.png/800px-Fig_Ni_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/2/27/Fig_Ni_1.png/1200px-Fig_Ni_1.png 1.5x, /wiki/images/2/27/Fig_Ni_1.png 2x"
width="800" height="596" /></a>

## Download\[<a href="/wiki/index.php?title=Fcc_Ni&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/c/c0/FccNi.tgz" class="internal"
title="FccNi.tgz">fccNi.tgz</a>


[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
[fcc Si
bandstructure](Fcc_Si_bandstructure.md) \>
[cd
Si](Cd_Si.md) \>
[cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si
relaxation](Cd_Si_relaxation.md) \>
[beta-tin
Si](Beta-tin_Si.md) \>
fcc
Ni \> [graphite TS
binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



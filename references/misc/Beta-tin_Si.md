<!-- Source: https://vasp.at/wiki/index.php/Beta-tin_Si | revid: 10311 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Beta-tin Si



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
beta-tin
Si \> [fcc
Ni](Fcc_Ni.md) \>
[graphite TS binding
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


## Task\[<a
href="/wiki/index.php?title=Beta-tin_Si&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Relaxation of the internal coordinates, volume and cell shape in
beta-tin Si.

## Input\[<a
href="/wiki/index.php?title=Beta-tin_Si&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Beta-tin_Si&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    beta Sn
        4.9000000000000
     1.0    0.0     0.0
     0.0    1.0     0.0
     0.5    0.5     0.26
      2
    Direct
     -0.125 -0.375  0.25
      0.125  0.375 -0.25

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Beta-tin_Si&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    System = beta Si
    ISMEAR = 0; SIGMA = 0.1;
    ENMAX  =  240
    IBRION=2; ISIF=3 ; NSW=15
    EDIFF  = 0.1E-04
    EDIFFG = -0.01

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Beta-tin_Si&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

## Calculation\[<a
href="/wiki/index.php?title=Beta-tin_Si&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

This example is completely analagous to [cd Si volume
relaxation](Cd_Si_volume_relaxation.md).

## Download\[<a
href="/wiki/index.php?title=Beta-tin_Si&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/5/5f/2_5_beta-tinSi.tgz" class="internal"
title="2 5 beta-tinSi.tgz">2_5_beta-tinSi.tgz</a>


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
beta-tin
Si \> [fcc
Ni](Fcc_Ni.md) \>
[graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


Back to the [main page](The_VASP_Manual.md).



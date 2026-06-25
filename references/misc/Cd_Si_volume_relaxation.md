<!-- Source: https://vasp.at/wiki/index.php/Cd_Si_volume_relaxation | revid: 10307 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Cd Si volume relaxation



[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
[fcc Si
bandstructure](Fcc_Si_bandstructure.md) \>
[cd
Si](Cd_Si.md) \>
cd Si volume
relaxation \> [cd Si
relaxation](Cd_Si_relaxation.md) \>
[beta-tin
Si](Beta-tin_Si.md) \>
[fcc
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
  - [3.1
    Summary](#summary)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Relaxation of the internal coordinates, volume and cell shape in cd Si.

## Input\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    cubic diamond
       5.5
     0.0    0.5     0.5
     0.5    0.0     0.5
     0.5    0.5     0.0
      2
    Direct
     -0.125 -0.125 -0.125
      0.125  0.125  0.125

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    System = diamond Si
    ISMEAR = 0; SIGMA = 0.1;
    ENMAX  =  240
    IBRION = 2; ISIF=3 ; NSW=15
    EDIFF  = 0.1E-04
    EDIFFG = -0.01

- [IBRION](../incar-tags/IBRION.md)=2 conjugate-gradient algorithm.
- [ISIF](../incar-tags/ISIF.md)=3 change of internal parameter, shape and
  volume simultaneously.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

## Calculation\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- To determine the equilibrium volume we can:
  - Fit the energz over a certain volume range to an equation of state
    (see [cd_Si](Cd_Si.md)).
  - Alternatively we relax the structure with VASP "on the fly"
    ([IBRION](../incar-tags/IBRION.md)=2 and [ISIF](../incar-tags/ISIF.md)=3)

<!-- -->

- From equation of states we determine lattice parameter of
  $a=5.4687$ Å (volume scan plus Murnaghan EOS using
  <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>=400).

<!-- -->

- From relaxations using [IBRION](../incar-tags/IBRION.md)=2 and
  [ISIF](../incar-tags/ISIF.md)=3 we get $a=5.4684$
  Å.

<!-- -->

- Difference can be due to pulay stress (especially when the relaxation
  starts far away from equilibrium):

<!-- -->

    -------------------------------------------------------------------------------------
    Total       0.00155     0.00155     0.00155    -0.00000     -0.00000      0.00000
    in kB       0.06056     0.06056     0.06056    -0.00000     -0.00000      0.00000
    external pressure =        0.06 kB  Pullay stress =          0.00 kB
       
       
    VOLUME and BASIS-vectors are now :
    -----------------------------------------------------------------------------
     energy-cutoff :      400.00
     volume of cell :      40.88
         direct lattice vectors                 reciprocal lattice vectors
        0.000000000  2.734185321  2.734185321    -0.182869828  0.182869828  0.182869828
        2.734185321  0.000000000  2.734185321     0.182869828 -0.182869828  0.182869828
        2.734185321  2.734185321  0.000000000     0.182869828  0.182869828 -0.182869828

  

- To remedy this increase the plane wave cutoff by at least 30% (here we
  used
  <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>=400
  instead of 240) and use a small [EDIFF](../incar-tags/EDIFF.md).

### Summary\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Summary">edit</a> \| (./index.php.md)\]

- Calculation of the equilibrium volume:
  - FIt the energy over a certain volume range to an equation of state.
  - When internal degrees of freedom exist (e.g. c/a), the structure
    must be optimized. Use a conjugate-gradient algorithm
    ([IBRION](../incar-tags/IBRION.md)=2) and at each volume do e.g. 10
    ionic steps ([NSW](../incar-tags/NSW.md)=10) and allow change of internal
    parameters and shape ([ISIF](../incar-tags/ISIF.md)=4).

<!-- -->

- Simpler but less reliable: relaxing all degrees of freedom including
  volume.
  - To relax all degrees of freedom use [ISIF](../incar-tags/ISIF.md)=3
    (internal coordinates, shape and volume).
  - Mind pulay stress problem. Increase plane wave cutoff by 25-30% when
    the volume is allowed to change.

## Download\[<a
href="/wiki/index.php?title=Cd_Si_volume_relaxation&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/0/08/DiamondSivolrel.tgz" class="internal"
title="DiamondSivolrel.tgz">diamondSivolrel.tgz</a>


[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
[fcc Si
bandstructure](Fcc_Si_bandstructure.md) \>
[cd
Si](Cd_Si.md) \>
cd Si volume
relaxation \> [cd Si
relaxation](Cd_Si_relaxation.md) \>
[beta-tin
Si](Beta-tin_Si.md) \>
[fcc
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



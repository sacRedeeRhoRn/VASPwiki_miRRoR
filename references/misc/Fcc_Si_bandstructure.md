<!-- Source: https://vasp.at/wiki/index.php/Fcc_Si_bandstructure | revid: 10937 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Si bandstructure



[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
fcc Si
bandstructure \> [cd
Si](Cd_Si.md) \>
[cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si
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
  - [2.4
    CHGCAR](#chgcar)
- [3
  CALCULATION](#calculation)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Computation of the bandstructure in fcc Si along L-Γ-X-U and K-Γ.

## Input\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    fcc Si:
     3.9
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    System = fcc Si 
    ICHARG = 11 #charge read file
    ENCUT  =    240
    ISMEAR = 0; SIGMA = 0.1;
    LORBIT = 11

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points for bandstructure L-G-X-U K-G
     10
    line
    reciprocal
      0.50000  0.50000  0.50000    1
      0.00000  0.00000  0.00000    1

      0.00000  0.00000  0.00000    1
      0.00000  0.50000  0.50000    1

      0.00000  0.50000  0.50000    1
      0.25000  0.62500  0.62500    1

      0.37500  0.7500   0.37500    1
      0.00000  0.00000  0.00000    1

- k points along the line $L - \Gamma - X - U K -
  \Gamma$.
- 10 points per line.
- Keyword *line* to generate bandstructure.
- In reciprocal coordinates.
- All points with weight 1.
- Example bandstructure should look like this:

<a href="/wiki/File:Fig_Si_5.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/b/b7/Fig_Si_5.png/300px-Fig_Si_5.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/b/b7/Fig_Si_5.png/450px-Fig_Si_5.png 1.5x, /wiki/images/b/b7/Fig_Si_5.png 2x"
width="300" height="207" /></a>

### [CHGCAR](../input-files/CHGCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: CHGCAR">edit</a> \| (./index.php.md)\]

This calculation needs a converged charge density as input
([ICHARG](../incar-tags/ICHARG.md)=11). You may use the
[CHGCAR](../input-files/CHGCAR.md) file of the [fcc Si
DOS](Fcc_Si_DOS.md) example.

## CALCULATION\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: CALCULATION">edit</a> \| (./index.php.md)\]

- To copy the self-consistent charge density of example fccSidos to your
  current working directory, type:

<!-- -->

    cp ../fccSidos/CHGCAR .

- You must do this otherwise VASP can not read the
  [CHGCAR](../input-files/CHGCAR.md) and will terminate.

<!-- -->

- To plot the bandstructure use p4vasp:

<a href="/wiki/File:Fig_Si_6.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/f8/Fig_Si_6.png/800px-Fig_Si_6.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/f8/Fig_Si_6.png/1200px-Fig_Si_6.png 1.5x, /wiki/images/f/f8/Fig_Si_6.png 2x"
width="800" height="567" /></a>

**Mind**: For this calculations you need the
[CHGCAR](../input-files/CHGCAR.md) file of the [fcc Si DOS
example](Fcc_Si_DOS.md).

## Download\[<a
href="/wiki/index.php?title=Fcc_Si_bandstructure&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/9/9c/FccSiband.tgz" class="internal"
title="FccSiband.tgz">fccSiband.tgz</a>


[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
fcc Si
bandstructure \> [cd
Si](Cd_Si.md) \>
[cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si
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



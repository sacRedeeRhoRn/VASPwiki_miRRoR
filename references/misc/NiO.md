<!-- Source: https://vasp.at/wiki/index.php/NiO | revid: 10445 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NiO



[Overview](../tutorials/Magnetism_-_Tutorial.md) \>
[fcc Ni
(revisited)](https://vasp.at/wiki/index.php/Fcc_Ni_(revisited) "Fcc Ni (revisited)") \>
NiO \>
[NiO
LSDA+U](NiO_LSDA+U.md) \>
[Spin-orbit coupling in a Ni
monolayer](Spin-orbit_coupling_in_a_Ni_monolayer.md) \>
[Spin-orbit coupling in a Fe
monolayer](Spin-orbit_coupling_in_a_Fe_monolayer.md) \>[constraining
local magnetic
moments](Constraining_local_magnetic_moments.md)
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


## Task\[<a href="/wiki/index.php?title=NiO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of NiO, an antiferromagnet.

## Input\[<a href="/wiki/index.php?title=NiO&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a href="/wiki/index.php?title=NiO&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    AFM  NiO
     4.17
     1.0 0.5 0.5
     0.5 1.0 0.5
     0.5 0.5 1.0
     2 2
    Cartesian
     0.0 0.0 0.0
     1.0 1.0 1.0
     0.5 0.5 0.5
     1.5 1.5 1.5

- AFM coupling: 4 atoms in the basis (instead of 2).

### [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=NiO&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    SYSTEM = NiO    
     
    ISTART = 0
     
    ISPIN = 2
    MAGMOM = 2.0 -2.0 2*0 
         
    ENMAX = 250.0
    EDIFF = 1E-3
        
    ISMEAR = -5
        
    AMIX = 0.2
    BMIX = 0.00001
    AMIX_MAG = 0.8
    BMIX_MAG = 0.00001
        
    LORBIT = 11

- Initial magnetic moments of 2μB (Ni) and 0μB (O).
- [AMIX](../incar-tags/AMIX.md)=0.2 and
  [AMIX_MAG](../incar-tags/AMIX_MAG.md)=0.8 (default),
  [BMIX](../incar-tags/BMIX.md) and [BMIX_MAG](../incar-tags/BMIX_MAG.md)
  practically zero, i.e. linear mixing.

### [KPOINTS](../input-files/KPOINTS.md)\[<a href="/wiki/index.php?title=NiO&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
     0
    gamma
     4  4  4 
     0  0  0

## Calculation\[<a href="/wiki/index.php?title=NiO&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- The total magnetic moment should be 0 in the
  [OSZICAR](../output-files/OSZICAR.md) file:

<!-- -->

    DAV:  13    -0.267936242334E+02    0.12794E-03   -0.12638E-04   552   0.298E-01    0.169E-02
    DAV:  14    -0.267936352231E+02   -0.10990E-04   -0.21775E-05   520   0.107E-01
       1 F= -.26793635E+02 E0= -.26793635E+02  d E =0.000000E+00  mag=     0.0000

- The partial and integrated magnetic moments within the PAW spheres are
  given in the [OUTCAR](../output-files/OUTCAR.md) file:

<!-- -->

     magnetization (x)
      
    # of ion     s       p       d       tot
    ----------------------------------------
      1       -0.012  -0.014   1.245   1.219
      2        0.012   0.014  -1.242  -1.216
      3        0.000  -0.001   0.000  -0.001
      4        0.000  -0.001   0.000  -0.001
    -----------------------------------------------
    tot        0.000  -0.003   0.003   0.000

- The example total DOS and the partial l-decomposed DOS for the d
  orbitals of Ni should look like the following:

<a href="/wiki/File:Fig_NiO_1.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/fc/Fig_NiO_1.png/1000px-Fig_NiO_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/fc/Fig_NiO_1.png/1500px-Fig_NiO_1.png 1.5x, /wiki/images/f/fc/Fig_NiO_1.png 2x"
width="1000" height="406" /></a>

## Download\[<a href="/wiki/index.php?title=NiO&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/6/62/4_2_NiO.tgz" class="internal"
title="4 2 NiO.tgz">4_2_NiO.tgz</a>


[Overview](../tutorials/Magnetism_-_Tutorial.md) \>
[fcc Ni
(revisited)](https://vasp.at/wiki/index.php/Fcc_Ni_(revisited) "Fcc Ni (revisited)") \>
NiO \>
[NiO
LSDA+U](NiO_LSDA+U.md) \>
[Spin-orbit coupling in a Ni
monolayer](Spin-orbit_coupling_in_a_Ni_monolayer.md) \>
[Spin-orbit coupling in a Fe
monolayer](Spin-orbit_coupling_in_a_Fe_monolayer.md) \>[constraining
local magnetic
moments](Constraining_local_magnetic_moments.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



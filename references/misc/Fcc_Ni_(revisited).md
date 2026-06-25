<!-- Source: https://vasp.at/wiki/index.php/Fcc_Ni_%28revisited%29 | revid: 10548 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Ni (revisited)



[Overview](../tutorials/Magnetism_-_Tutorial.md) \>
fcc Ni
(revisited) \>
[NiO](NiO.md) \> [NiO
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
  - [3.1 Collinear
    case](#Collinear_case)
  - [3.2
    Noncollinear case](#Noncollinear_case)
- [4
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)&action=edit&section=1 "Edit section's source code: Task")\]

Calculation of the partial DOS of spin-polarized fcc Ni, a ferromagnet.

## Input\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)&action=edit&section=2 "Edit section's source code: Input")\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)&action=edit&section=3 "Edit section's source code: POSCAR")\]

    fcc:                             
     -10.93    
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1  
    Cartesian
    0 0 0

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)&action=edit&section=4 "Edit section's source code: INCAR")\]

    SYSTEM  = Ni fcc bulk 
    ISTART  = 0
    ISPIN   = 2
    MAGMOM  = 1.0
    ISMEAR  = -5
    VOSKOWN = 1 
    LORBIT  = 11

- Spin-polarized calculation with initial magnetic moment of 1 µB.
- Interpolation scheme of Vosko, Wilk and Nusair is used (see
  [VOSKOWN](../incar-tags/VOSKOWN.md)=1).
- lm-decomposed [DOSCAR](../output-files/DOSCAR.md) is created.
- Tetrahedron method with Blöchl's corrections used for k-mesh
  integration.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)&action=edit&section=5 "Edit section's source code: KPOINTS")\]

    k-points
    0
    Gamma
     11 11 11
      0  0  0

## Calculation\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)&action=edit&section=6 "Edit section's source code: Calculation")\]

### Collinear case\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Collinear case">edit</a> \| (./index.php.md)&action=edit&section=7 "Edit section's source code: Collinear case")\]

- The output for the magnetic moments in the
  [OSZICAR](../output-files/OSZICAR.md) should look like the following:

<!-- -->

           N        E
    DAV:   1     0.139935173959E+02    0.13994E+02   -0.35801E+03  2338   0.828E+02
    DAV:   2    -0.623612680591E+01   -0.20230E+02   -0.19281E+02  2282   0.123E+02
    DAV:   3    -0.643764005251E+01   -0.20151E+00   -0.19906E+00  2536   0.140E+01
    DAV:   4    -0.643786482872E+01   -0.22478E-03   -0.22442E-03  2344   0.459E-01
    DAV:   5    -0.643786514671E+01   -0.31798E-06   -0.31687E-06  1832   0.173E-02    0.793E+00
    ...
    DAV:   9    -0.545953126374E+01    0.48409E-02   -0.96206E-03  2946   0.839E-01    0.847E-02
    DAV:  10    -0.545946513577E+01    0.66128E-04   -0.77007E-05  1364   0.126E-01
       1 F= -.54594651E+01 E0= -.54594651E+01  d E =0.000000E+00  mag=     0.5781

- The l decomposed parts of the magnetic moment are written in the
  [OUTCAR](../output-files/OUTCAR.md) file:

<!-- -->

     magnetization (x)

  

    # of ion     s       p       p       tot
    ----------------------------------------
      1       -0.007  -0.026   0.625   0.591

- The example output for the spin up and down DOS shows an exchange
  splitting of approximately 0.5 eV:

<a href="/wiki/File:Fig_fccNi_revised_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/78/Fig_fccNi_revised_1.png/700px-Fig_fccNi_revised_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/78/Fig_fccNi_revised_1.png/1050px-Fig_fccNi_revised_1.png 1.5x, /wiki/images/7/78/Fig_fccNi_revised_1.png 2x"
width="700" height="452" /></a>

- Proper initialization of magnetic moments is very important:
  - Too small initial magnetic moments will/may lead to nonmagnetic
    solution (by starting with an initial moment of 0.0 we arrive only
    to a magnetic of 0.002).
  - Badly initialized calculations take longer to converge.
  - Coexistence of low- and high spin solutions.

### Noncollinear case\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Noncollinear case">edit</a> \| (./index.php.md)&action=edit&section=8 "Edit section's source code: Noncollinear case")\]

- For a noncollinear calculation replace [ISPIN](../incar-tags/ISPIN.md)=2
  and [MAGMOM](../incar-tags/MAGMOM.md)=1.0 in the
  [INCAR](../input-files/INCAR.md) file by the following:

<!-- -->

    LNONCOLLINEAR = .TRUE.
    MAGMOM        = 0.0 0.0 1.0

- The last three lines of the [OSZICAR](../output-files/OSZICAR.md) file
  using this parameter should look like the following:

<!-- -->

    DAV:   9    -0.546480633680E+01    0.41628E-02   -0.49402E-04  7532   0.330E-01    0.695E-02
    DAV:  10    -0.546475032360E+01    0.56013E-04   -0.52286E-05  4328   0.446E-02
       1 F= -.54647503E+01 E0= -.54647503E+01  d E =0.000000E+00  mag= 0.0000   0.0000   0.5792

- By using [MAGMOM](../incar-tags/MAGMOM.md) = 1.0 0.0 0.0 we get the
  following output:

<!-- -->

    DAV:   9    -0.546481348871E+01    0.41496E-02   -0.50294E-04  7548   0.330E-01    0.692E-02
    DAV:  10    -0.546474438319E+01    0.69106E-04   -0.51451E-05  4288   0.432E-02
       1 F= -.54647444E+01 E0= -.54647444E+01  d E =0.000000E+00  mag= 0.5792   0.0000   0.0000

- Analogously if we set [MAGMOM](../incar-tags/MAGMOM.md) = 0.0 1.0 0.0 we
  get the following output:

<!-- -->

    DAV:   9    -0.546481179459E+01    0.41515E-02   -0.50430E-04  7552   0.330E-01    0.692E-02
    DAV:  10    -0.546474640011E+01    0.65394E-04   -0.51658E-05  4292   0.434E-02
       1 F= -.54647464E+01 E0= -.54647464E+01  d E =0.000000E+00  mag= 0.0000   0.5792   0.0000

## Download\[<a
href="/wiki/index.php?title=Fcc_Ni_(revisited)&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)&action=edit&section=9 "Edit section's source code: Download")\]

<a href="/wiki/images/1/11/4_1_Ni.tgz" class="internal"
title="4 1 Ni.tgz">4_1_Ni.tgz</a>


[Overview](../tutorials/Magnetism_-_Tutorial.md) \>
fcc Ni
(revisited) \>
[NiO](NiO.md) \> [NiO
LSDA+U](NiO_LSDA+U.md) \>
[Spin-orbit coupling in a Ni
monolayer](Spin-orbit_coupling_in_a_Ni_monolayer.md) \>
[Spin-orbit coupling in a Fe
monolayer](Spin-orbit_coupling_in_a_Fe_monolayer.md) \>[constraining
local magnetic
moments](Constraining_local_magnetic_moments.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



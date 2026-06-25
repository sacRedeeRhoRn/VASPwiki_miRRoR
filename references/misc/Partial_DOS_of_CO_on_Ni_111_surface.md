<!-- Source: https://vasp.at/wiki/index.php/Partial_DOS_of_CO_on_Ni_111_surface | revid: 10456 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Partial DOS of CO on Ni 111 surface



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \>
[Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
partial DOS of CO on Ni 111
surface \> [vibrational
frequencies of CO on Ni 111
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
  - [3.1
    DOS](#DOS)
  - [3.2 Work
    function](#Work_function)
- [4
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the work function and partial DOS of a CO@Ni (111)
surface, adsorbed on top.

## Input\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    Ni - (111) + CO ontop
       3.53000000000000     
         0.7071067800000000    0.0000000000000000    0.0000000000000000
        -0.3535533900000000    0.6123724000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    5.1961523999999998
       5   1   1
    Selective dynamics
    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000   F   F   F
      0.3333333300000021  0.6666666699999979  0.1111111100000031   F   F   F
      0.6666666699999979  0.3333333300000021  0.2222222199999990   F   F   F
      0.0000000000000000  0.0000000000000000  0.3330391292438326   T   T   T
      0.3333333300000021  0.6666666699999979  0.4445422014835692   T   T   T
      0.3333333300000021  0.6666666699999979  0.5402025044116211   T   T   T
      0.3333333300000021  0.6666666699999979  0.6031536532245922   T   T   T
     
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00

N.B.: this [POSCAR](../input-files/POSCAR.md) is essentially the result
([CONTCAR](../output-files/CONTCAR.md) file) of the relaxation performed in
the [CO on Ni 111
surface](CO_on_Ni_111_surface.md) example.

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    general:
      ENMAX = 400
      SYSTEM = CO adsorption on Ni(111)
      ISMEAR = -5
      ALGO = Fast
        
    LDOS:
      LORBIT = 11
        
    workfunction:
      IDIPOL = 3
      LDIPOL = .TRUE.
      LVHAR = .TRUE.
    #  LVTOT = .TRUE.

- For the calculation of the DOS we use a tetrahedron method with Blöchl
  corrections ([ISMEAR](../incar-tags/ISMEAR.md)=-5).
- By setting [LVHAR](../incar-tags/LVHAR.md)=*.TRUE.* the Hartree part of
  the local potential is written to the file
  [LOCPOT](../output-files/LOCPOT.md).
- By setting [LVTOT](../incar-tags/LVTOT.md)=*.TRUE.* the total local
  potential is written tot the file [LOCPOT](../output-files/LOCPOT.md).
- By setting [IDIPOL](../incar-tags/IDIPOL.md)=3 dipole corrections in the
  direction of the third lattice vector are enabled.
- We have active dipole corrections to potential (=dipole layer).

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

### DOS\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: DOS">edit</a> \| (./index.php.md)\]

- The lm-decomposed DOS helps to analyze the bonding:

<a href="/wiki/File:Fig_CO_on_Ni111_LDOS_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/a/a4/Fig_CO_on_Ni111_LDOS_1.png/400px-Fig_CO_on_Ni111_LDOS_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/a/a4/Fig_CO_on_Ni111_LDOS_1.png/600px-Fig_CO_on_Ni111_LDOS_1.png 1.5x, /wiki/images/a/a4/Fig_CO_on_Ni111_LDOS_1.png 2x"
width="400" height="344" /></a>

- CO $5\sigma, 1\pi, 2\pi^{\*}$ bonds.
- From comparison with substrate LDOS:
  - Hybridization with Ni-$d_{3z^{2}-r^{2}}$.
  - No interaction with $d_{xy}$
    due to symmetry.

### Work function\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Work function">edit</a> \| (./index.php.md)\]

- The planar average of the potential for this example should look like
  the following:

<a href="/wiki/File:Fig_CO_on_Ni111_LDOS_2.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/a/a6/Fig_CO_on_Ni111_LDOS_2.png/300px-Fig_CO_on_Ni111_LDOS_2.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/a/a6/Fig_CO_on_Ni111_LDOS_2.png/450px-Fig_CO_on_Ni111_LDOS_2.png 1.5x, /wiki/images/thumb/a/a6/Fig_CO_on_Ni111_LDOS_2.png/600px-Fig_CO_on_Ni111_LDOS_2.png 2x"
width="300" height="418" /></a>

- $\epsilon_{\mathrm{F}} = 1.65$ eV (from
  [OUTCAR](../output-files/OUTCAR.md) file.

<!-- -->

- Vacuum-potential at 8.24/6.77 eV: $\Phi_{\mathrm{CO}}=6.58,\Phi_{\mathrm{clean}}=5.11$
  eV.

<!-- -->

- Too small result for clean surface due to too small vacuum ...

## Download\[<a
href="/wiki/index.php?title=Partial_DOS_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/7/7b/COonNi111_LDOS.tgz" class="internal"
title="COonNi111 LDOS.tgz">COonNi111_LDOS.tgz</a>


[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \>
[Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
partial DOS of CO on Ni 111
surface \> [vibrational
frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of
graphite](STM_of_graphite.md) \>
[STM of
graphene](STM_of_graphene.md) \>
[collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of
tutorials](../categories/Category-Tutorials.md)



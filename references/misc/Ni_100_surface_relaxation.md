<!-- Source: https://vasp.at/wiki/index.php/Ni_100_surface_relaxation | revid: 10442 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Ni 100 surface relaxation



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
Ni 100 surface
relaxation \> [Ni 100
surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
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
href="/wiki/index.php?title=Ni_100_surface_relaxation&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Relaxation of the first two layers of a Ni (100) surface.

## Input\[<a
href="/wiki/index.php?title=Ni_100_surface_relaxation&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_relaxation&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    fcc (100) surface
     3.53
       .50000   .50000   .00000
      -.50000   .50000   .00000
       .00000   .00000  5.00000
      5
    Selective Dynamics
    Kartesisch
       .00000   .00000   .00000 F F F
       .00000   .50000   .50000 F F F
       .00000   .00000  1.00000 F F F
       .00000   .50000  1.50000 T T T
       .00000   .00000  2.00000 T T T

- Ni lattice constant of 3.53$\AA$.
- 1 atom per layer: p(1x1) cell.
- 5 nickel layers.
- First two layers (of one side) relaxed.
- $3\times3.53 = 10.59 \AA$ vacuum.

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_relaxation&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

      ISTART = 0; ICHARG = 2
        
    general:
      SYSTEM = clean Ni(100) surface
      ENCUT = 270 
      ISMEAR = 2 ; SIGMA = 0.2
      ALGO = Fast
      EDIFF = 1E-6
        
    spin:
      ISPIN=2
      MAGMOM = 5*1
        
    dynamic:
      NSW = 100
      POTIM = 0.8
      IBRION = 1

- Initial charge-density in startjob from overlapping atoms.
- Default energy cut-off of 270 eV.
- MP-smearing (metal).
- Spin-polarized calculation with initial moment of 1.
- Ionic relaxation used.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Ni_100_surface_relaxation&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

- Equally spaced mesh.
- Odd mesh, centered on $\Gamma$.
- 15 k points in irreducible Brillouin zone (IBZ).
- Only one k point in z-direction for surface.

## Calculation\[<a
href="/wiki/index.php?title=Ni_100_surface_relaxation&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- The sample output for the forces in the
  [OUTCAR](../output-files/OUTCAR.md) file should look like this (first and
  last step):

First step:

    POSITION                                       TOTAL-FORCE  (eV/Angst)
    -----------------------------------------------------------------------------------
         0.00000      0.00000      0.00000         0.000000      0.000000      0.391352
         0.00000      1.76500      1.76500         0.000000      0.000000     -0.397024
         0.00000      0.00000      3.53000         0.000000      0.000000      0.005117
         0.00000      1.76500      5.29500         0.000000      0.000000      0.391161
         0.00000      0.00000      7.06000         0.000000      0.000000     -0.390607
    -----------------------------------------------------------------------------------
       total drift:                                0.000000      0.000000      0.016391

Last step:

    POSITION                                       TOTAL-FORCE  (eV/Angst)
    -----------------------------------------------------------------------------------
         0.00000      0.00000      0.00000         0.000000      0.000000      0.399012
         0.00000      1.76500      1.76500         0.000000      0.000000     -0.377003
         0.00000      0.00000      3.53000         0.000000      0.000000      0.105799
         0.00000      1.76500      5.32685         0.000000      0.000000     -0.062054
         0.00000      0.00000      7.02377         0.000000      0.000000     -0.065753
    -----------------------------------------------------------------------------------
       total drift:                                0.000000      0.000000     -0.042925

- Energy changes during relaxation from -25.556 to -25.571 eV which
  gives a relaxation energy of $E^{\mathrm{rel}} = -15$ meV. Use p4vasp to check the convergence:

<a href="/wiki/File:Fig_Ni_100_surfrel_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/9/9c/Fig_Ni_100_surfrel_1.png/600px-Fig_Ni_100_surfrel_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/9/9c/Fig_Ni_100_surfrel_1.png/900px-Fig_Ni_100_surfrel_1.png 1.5x, /wiki/images/thumb/9/9c/Fig_Ni_100_surfrel_1.png/1200px-Fig_Ni_100_surfrel_1.png 2x"
width="600" height="491" /></a>

- The surface energy of 0.86 eV for the unrelaxed surface is calculated
  in the following:

$\sigma^{\mathrm{unrel}} = \frac{1}{2}
(E_{\mathrm{surf}}-N_{\mathrm{atoms}} \cdot E_{\mathrm{bulk}}) =
\frac{1}{2} (-25.556-5\cdot(-5.457))= 0.86$ eV.

- The surface energy of 0.84 eV for the relaxed surface is then
  calculated as:

$\sigma = \sigma^{\mathrm{unrel}} + E^{\mathrm{rel}} = 0.84$ eV.

- The final geometry (from the [CONTCAR](../output-files/CONTCAR.md) or
  [OUTCAR](../output-files/OUTCAR.md) file) should look as follows:

<!-- -->

    fcc (100) surface
       3.53000000000000
         0.5000000000000000      0.5000000000000000      0.000000000000000
        -0.5000000000000000      0.5000000000000000      0.000000000000000
         0.0000000000000000      0.0000000000000000      5.000000000000000
       Ni
         5
    Selective Dynamics
    Direct
    0.0000000000000000   0.0000000000000000   0.0000000000000000 F F F
    0.0000000000000000   0.5000000000000000   0.1000000000000014 F F F
    0.0000000000000000   0.0000000000000000   0.2000000000000028 F F F
    0.5000000000000000   0.5000000000000000   0.3018043743226639 T T T
    0.0000000000000000   0.0000000000000000   0.3979474020596729 T T T 

- Inward relaxation of surface layers:
  - $\Delta d_{12}$ = ((0.3979-0.3018)-0.1)/0.1\*100=-3.9%.
  - $\Delta d_{12}$ = ((0.3018-0.2000)-0.1)/0.1\*100=+1.8%.

<!-- -->

- Use p4vasp to visualize the relaxation:

<a href="/wiki/File:Fig_Ni_100_surfrel_2.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/8/83/Fig_Ni_100_surfrel_2.png/800px-Fig_Ni_100_surfrel_2.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/8/83/Fig_Ni_100_surfrel_2.png/1200px-Fig_Ni_100_surfrel_2.png 1.5x, /wiki/images/8/83/Fig_Ni_100_surfrel_2.png 2x"
width="800" height="541" /></a>

## Download\[<a
href="/wiki/index.php?title=Ni_100_surface_relaxation&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/d/d5/Ni100clean_rel.tgz" class="internal"
title="Ni100clean rel.tgz">Ni100clean_rel.tgz</a>


[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
Ni 100 surface
relaxation \> [Ni 100
surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
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



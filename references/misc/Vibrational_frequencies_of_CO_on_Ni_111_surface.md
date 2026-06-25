<!-- Source: https://vasp.at/wiki/index.php/Vibrational_frequencies_of_CO_on_Ni_111_surface | revid: 10469 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Vibrational frequencies of CO on Ni 111 surface



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
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
vibrational frequencies of CO on Ni
111 surface \> [STM of
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
href="/wiki/index.php?title=Vibrational_frequencies_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the vibrational frequencies of CO@Ni(111) (on top).

## Input\[<a
href="/wiki/index.php?title=Vibrational_frequencies_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Vibrational_frequencies_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    Ni - (111) + CO on-top                  
       3.53000000000000     
         0.7071067800000000    0.0000000000000000    0.0000000000000000
        -0.3535533900000000    0.6123724000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    5.1961523999999999
       Ni   C    O 
         5     1     1
    Selective dynamics
    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000   F   F   F
      0.3333333300000021  0.6666666699999979  0.1111111100000031   F   F   F
      0.6666666699999979  0.3333333300000021  0.2222222199999990   F   F   F
     -0.0000000000000000  0.0000000000000000  0.3326227833039623   F   F   F
      0.3333333300000021  0.6666666699999979  0.4445699380869117   F   F   F
      0.3333333300000021  0.6666666699999979  0.5403264650180125   F   F   T
      0.3333333300000021  0.6666666699999979  0.6032949698060487   F   F   T
     
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00

- Frequencies only for the CO molecule and the z-direction (z- and (x,y)
  are independent).

N.B.: this [POSCAR](../input-files/POSCAR.md) is essentially the result
([CONTCAR](../output-files/CONTCAR.md) file) of the relaxation performed in
the [CO on Ni 111
surface](CO_on_Ni_111_surface.md) example.

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Vibrational_frequencies_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

     SYSTEM = CO on Ni111 - frequencies
        
    general:
      ENMAX  = 400
      ISMEAR =    2  ; SIGMA = 0.2
      ALGO   = Fast
      EDIFF  = 1E-6
      MAXMIX = 60  # reuse the mixer between ionic steps, saves time
        
    dynamic:
      NSW = 100
      IBRION = 5
      NFREE  = 2

- Small termination criterion ([EDIFF](../incar-tags/EDIFF.md)).
- Automatic frequency calculation (displacement 0.04
  $\AA$).
- Reuse of the mixer between ionic steps
  ([MAXMIX](../incar-tags/MAXMIX.md)) to save time.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Vibrational_frequencies_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation\[<a
href="/wiki/index.php?title=Vibrational_frequencies_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- Finite differences give the following additional output in the
  [OUTCAR](../output-files/OUTCAR.md) fiel for frequency calculations:

<!-- -->

    Finite differences progress:
     Degree of freedom:   1/  2
     Displacement:        1/  2
     Total:               1/  4

- After the first calculation for the equilibrium geometry,
  [NFREE](../incar-tags/NFREE.md) displacements
  ($\pm$[POTIM](../incar-tags/POTIM.md)) are performed for
  each degree of freedom. From these displacements the dynamical matrix
  is set up and diagonalized.

<!-- -->

- At the end of the [OUTCAR](../output-files/OUTCAR.md) file the following
  are listed:
  - Forces.
  - The dynamical matrix and finally.
  - The eigenfrequencies.
  - Eigenvectors (first normalized and then mass-weighted).

<!-- -->

- The example output for the eigenvectors and eigenvalues of the
  dynamical matrix from the [OUTCAR](../output-files/OUTCAR.md) file should
  look like the following:

<!-- -->

    Eigenvectors and eigenvalues of the dynamical matrix
    ----------------------------------------------------
      1 f  =   63.914144 THz   401.584411 2PiTHz 2131.946301 cm-1   264.327748 meV
                X         Y         Z           dx          dy          dz
         0.000000  0.000000  0.000000            0           0           0
         0.000000  1.441116  2.038046            0           0           0
         1.248043  0.720558  4.076093            0           0           0
         0.000000  0.000000  6.108743            0           0           0
         0.000000  1.441116  8.153979            0           0           0
         0.000000  1.441116  9.908620            0           0   -0.761748
         0.000000  1.441116 11.063296            0           0    0.623594
       
       
      2 f  =   12.467410 THz    78.335050 2PiTHz  415.868035 cm-1    51.561083 meV
                X         Y         Z           dx          dy          dz
         0.000000  0.000000  0.000000            0           0           0
         0.000000  1.441116  2.038046            0           0           0
         1.248043  0.720558  4.076093            0           0           0
         0.000000  0.000000  6.108743            0           0           0
         0.000000  1.441116  8.153979            0           0           0
         0.000000  1.441116  9.908620            0           0   -0.623594
         0.000000  1.441116 11.063296            0           0   -0.781748

As one can see the first vibrational mode is the so-called *CO stretch*
mode (stretching and contracting the C-O bond), whereas the second mode
shows the CO molecule moving w.r.t. to the metallic surface
(*CO-metal*).

- Try to change the selective dynamics tag such that displacements

in x and y direction are allowed as well for CO (note that the selective
dynamics flags always refer to cartesian coordinates), i.e,

     0.3333333300000021  0.6666666699999979  0.5403264650180125   F   F   T
     0.3333333300000021  0.6666666699999979  0.6032949698060487   F   F   T

to

     0.3333333300000021  0.6666666699999979  0.5403264650180125   T   T   T
     0.3333333300000021  0.6666666699999979  0.6032949698060487   T   T   T

Also test whether you need to decrease [EDIFF](../incar-tags/EDIFF.md) to
1E-8.

## Download\[<a
href="/wiki/index.php?title=Vibrational_frequencies_of_CO_on_Ni_111_surface&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/4/40/COonNi111_freq.tgz" class="internal"
title="COonNi111 freq.tgz">COonNi111_freq.tgz</a>


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
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
vibrational frequencies of CO on Ni
111 surface \> [STM of
graphite](STM_of_graphite.md) \>
[STM of
graphene](STM_of_graphene.md) \>
[collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of
tutorials](../categories/Category-Tutorials.md)



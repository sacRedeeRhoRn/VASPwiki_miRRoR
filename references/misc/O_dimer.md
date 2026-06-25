<!-- Source: https://vasp.at/wiki/index.php/O_dimer | revid: 35867 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# O dimer



[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](O_atom.md) \>
[O atom
spinpolarized](O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
O
dimer \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \>
[CO partial
DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \>
[H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
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
    stdout](#stdout)
- [4
  Download](#Download)


## Task\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Relaxation of the bond length of an oxygen dimer.

## Input\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    O dimer in a box
     1.0          ! universal scaling parameters
     8.0 0.0 0.0  ! lattice vector  a(1)
     0.0 8.0 0.0  ! lattice vector  a(2)
     0.0 0.0 8.0  ! lattice vector  a(3)
    2             ! number of atoms
    cart          ! positions in cartesian coordinates
     0 0 0        ! first atom
     0 0 1.22     ! second atom

### [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    SYSTEM = O2 dimer in a box
    ISMEAR = 0 ! Gaussian smearing
    ISPIN  = 2 ! spin polarized calculation
    NSW = 5    ! 5 ionic steps
    IBRION = 2 ! use the conjugate gradient algorithm

### [KPOINTS](../input-files/KPOINTS.md)\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

  

  

## Calculation\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- We have selected in the [INCAR](../input-files/INCAR.md) file that
  geometry relaxation should be performed. In this case 5 ionic steps
  ([NSW](../incar-tags/NSW.md)=5) should be done at most. For the relaxation
  a conjugate gradient (CG) algorithm is used
  ([IBRION](../incar-tags/IBRION.md)=2).

<!-- -->

- The CG algorithm requires line minimizations along the search
  direction. This is done using a variant of Brent's algorithm. (Picture
  missing)
  - Trial step along search direction (gradient scaled by
    [POTIM](../incar-tags/POTIM.md))
  - Quadratic or cubic interpolation using energies and forces at
    $\mathbf{x}_{0}$ and $\mathbf{x}_{1}$ allows to determine the approximate minimum
  - Continue minimization, if app. minimum is not accurate enough

<a href="/wiki/File:Fig_O2_dimer_1.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/e/e0/Fig_O2_dimer_1.png/400px-Fig_O2_dimer_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/e/e0/Fig_O2_dimer_1.png/600px-Fig_O2_dimer_1.png 1.5x, /wiki/images/thumb/e/e0/Fig_O2_dimer_1.png/800px-Fig_O2_dimer_1.png 2x"
width="400" height="87" /></a>

### stdout\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: stdout">edit</a> \| (./index.php.md)\]

    DAV:   1     0.517118590134E+02    0.51712E+02    -0.31393E+03    80   0.366E+02
    ...    ...   ...
    ...    ...   ...
    DAV:  14    -0.985349953776E+01   -0.15177E-03    -0.57546E-06    64   0.125E-02    0.371E-03
    DAV:  15    -0.985357023804E+01   -0.70700E-04    -0.22439E-06    64   0.741E-03
       1 F= -.98535702E+01 E0= -.98535702E+01  d E =-.985357E+01  mag=     2.0000
     curvature:   0.00 expect dE= 0.000E+00 dE for cont linesearch  0.000E+00
     trial: gam= 0.00000 g(F)=  0.113E+00 g(S)=  0.000E+00 ort = 0.000E+00 (trialstep = 0.100E+01)
     search vector abs. value=  0.113E+00
     bond charge predicted
    ...    ...   ...
    ...    ...   ...
       2 F= -.96234585E+01 E0= -.96234585E+01  d E =0.230112E+00  mag=      2.0000
     trial-energy change:    0.230112  1 .order    0.190722   -0.113406    0.494850
     step:   0.1397(harm=  0.1864)  dis= 0.00731  next Energy=    -9.861386 (dE=-0.782E-02)
     bond charge predicted
    ...    ...   ...
    ...    ...   ...
       3 F= -.98607735E+01 E0= -.98607735E+01  d E =-.720327E-02  mag=      2.0000
     curvature:  -0.09 expect dE=-0.900E-05 dE for cont linesearch -0.900E-05
     trial: gam= 0.00000 g(F)=  0.969E-04 g(S)=  0.000E+00 ort =-0.331E-02 (trialstep = 0.828E+00)
     search vector abs. value=  0.969E-04
     reached required accuracy - stopping structural energy minimisation

Explanation of the output:

- The quantitiy *trial-energy change* is the change of the energy in the
  trial step.

<!-- -->

- The first value after 1. order is the expected energy change
  calculated from the forces $((\mathbf{F}(\textrm{start})+\mathbf{F}(\textrm{trial}))/2\times$ change of positions - central difference.

<!-- -->

- The second and third value correspond to $\mathbf{F}(\mathrm{start})
  \times$ change of positions and
  $\mathbf{F} (\mathrm{trial}) \times$ change of
  position.

<!-- -->

- The value *step* is the estimated size of the step leading to a line
  minimization along the current search direction. *harm* is the optimal
  step using a second order (or harmonic) interpolation.

<!-- -->

- The trial step size can be controlled by the paramter
  [POTIM](../incar-tags/POTIM.md) (the value *step* times the present
  [POTIM](../incar-tags/POTIM.md) is usually optimal).

<!-- -->

- The final positions after the optimization are stored in the
  [CONTCAR](../output-files/CONTCAR.md) file. One can copy
  [CONTCAR](../output-files/CONTCAR.md) to [POSCAR](../input-files/POSCAR.md)
  and continue the relaxation.

## Download\[<a href="/wiki/index.php?title=O_dimer&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/8/8b/Odimer.tgz" class="internal"
title="Odimer.tgz">Odimer.tgz</a>


[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O
atom](O_atom.md) \>
[O atom
spinpolarized](O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
O
dimer \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \>
[CO partial
DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \>
[H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)



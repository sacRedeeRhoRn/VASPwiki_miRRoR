<!-- Source: https://vasp.at/wiki/index.php/EFOR | revid: 27938 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EFOR


EFOR = \[real array\] 

|                   |                     |     |
|-------------------|---------------------|-----|
| Default: **EFOR** | = 3 \* NIONS \* 0.0 |     |

Description: EFOR sets
external forces in eV/Å on each atom in the cartesian x-, y-, and
z-directions. The order of the ions is equivalent to the order in the
[POSCAR](../input-files/POSCAR.md) file, and for each ion, x-, y-, and
z-components have to be given.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The array of external forces will be added to the
<a href="/wiki/Forces" class="mw-redirect" title="Forces">forces</a>
computed internally for each ionic step
(<a href="/wiki/Ionic_minimization" class="mw-redirect"
title="Ionic minimization">ionic minimization</a> or
<a href="/wiki/Molecular_dynamics" class="mw-redirect"
title="Molecular dynamics">molecular dynamics</a>). If an
<a href="/wiki/Ionic_minimization" class="mw-redirect"
title="Ionic minimization">ionic minimization</a> is performed with
non-zero external forces, the converged structures will be only at a
minimum accounting for the constraint of the external forces. Regardless
of whether the [convergence criterion](EDIFFG.md) is set to
minimize total forces, or converge the total energy.

|  |
|----|
| **Warning:** The sum of all external forces set with EFOR must be 0 to avoid drift. |

While the total sum of all external forces in all directions must be
zero, it is possible to achieve this by putting balancing forces on an
ion that is fixed by the [selective
dynamics](../input-files/POSCAR.md) feature in
the [POSCAR](../input-files/POSCAR.md) file.


## Contents


- [1
  Format](#Format)
- [2 Symmetry and
  periodic boundary
  conditions](#Symmetry_and_periodic_boundary_conditions)
  - [2.1 Symmetry
    considerations](#Symmetry_considerations)
  - [2.2 Periodic
    boundary conditions](#Periodic_boundary_conditions)
- [3 External
  forces during on-the-fly
  learning](#External_forces_during_on-the-fly_learning)
- [4
  Output](#Output)
- [5
  Example](#Example)
- [6 Related Tags
  and Sections](#Related_Tags_and_Sections)


## Format\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Format">edit</a> \| (./index.php.md)\]

EFOR can be a very long array,
as 3 values need to be set for each ion in the system. The format is
equivalent to setting the magnetic moments in the noncollinear case
using [MAGMOM](MAGMOM.md), so it is possible to use an `N*F`
syntax to indicate that the next **N** entries in the array should be of
value **F**. E.g.:

     EFOR = 2*0.0 1.0 188*0.0 -1.0

In this example, we have 64 ions, so we have to set 3\*64=192 values in
the array. Only the cartesian z components of the first and last ion
should be non-zero, which enables a compact [INCAR](../input-files/INCAR.md)
line.

If more force components are non-zero, readability is increased by
utilizing the [multi-line option](../input-files/INCAR.md) in the
[INCAR](../input-files/INCAR.md) file. This is achieved by using backslashes
(**\\**) to negate line breaks or put the multi-line expression in
quotes (**"**). E.g. for a 32 atom system with forces in the x- and
z-directions on the first and last 8 atoms:

     EFOR = "2.0 0.0 1.0
             2.0 0.0 1.0
             2.0 0.0 1.0
             2.0 0.0 1.0
             0.0 0.0 1.0
             0.0 0.0 1.0
             0.0 0.0 1.0
             0.0 0.0 1.0
             48*0.0     
            -1.0 0.0 -1.0
            -1.0 0.0 -1.0
            -1.0 0.0 -1.0
            -1.0 0.0 -1.0
            -1.0 0.0 -1.0
            -1.0 0.0 -1.0
            -1.0 0.0 -1.0
            -1.0 0.0 -1.0"

## Symmetry and periodic boundary conditions\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Symmetry and periodic boundary conditions">edit</a> \| (./index.php.md)\]

### Symmetry considerations\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Symmetry considerations">edit</a> \| (./index.php.md)\]

Setting external forces will, in most cases, break some symmetries of
the system, resulting in more [irreducible **k**
points](../input-files/KPOINTS.md) and thus
increased computational effort.

If any non-zero external forces are set, the symmetry reduction is
reported in the OUTCAR after all other symmetry operations. E.g.:

    Analysis of structural, dynamic, and magnetic symmetry & ext. forces:
    =====================================================================
     Subroutine PRICEL returns:
     Original cell was already a primitive cell.
      
      
     Routine SETGRP: Setting up the symmetry group for a 
     hexagonal supercell.
      
       
     Subroutine GETGRP returns: Found  6 space group operations
     (whereof  6 operations were pure point group operations)
     out of a pool of 24 trial point group operations.
      
       
     The overall configuration with ext. forces has the point symmetry S_6 .
     Periodic boundary conditions apply in all VASP calculations.

### Periodic boundary conditions\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Periodic boundary conditions">edit</a> \| (./index.php.md)\]

All VASP calculations are performed under periodic boundary conditions.
When external forces are applied to bulk systems, this can lead to
unexpected results. E.g. pushing an atom towards another atom in the
same unit cell might pull it further away from the same atom in a
neighboring unit cell. Thus external forces cannot be used to uniformly
compress or strain a bulk system along a specific axis. This can however
be achieved by lengthening or shortening the relevant lattice vector.

On the other hand, external forces should be used if strain needs to be
applied to a slab, a molecule, or any other system in which a vacuum
region is used. When e.g. a surface slab needs to be compressed in the
direction normal to the surface plane, the lattice vector cannot be
shortened because this would collapse the vacuum. External forces on the
atoms at the surfaces can achieve the desired effect.

|  |
|----|
| **Tip:** External forces are typically only used if there is a vacuum region in the simulation cell. |

## External forces during on-the-fly learning\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: External forces during on-the-fly learning">edit</a> \| (./index.php.md)\]

External forces can be used during on-the-fly training for
<a href="/wiki/Machine-learned_force_fields" class="mw-redirect"
title="Machine-learned force fields">machine-learned force fields</a>.
In that case, the external forces will be only used during the ionic
updates but will be removed for the training. This ensures that only
forces arising from interatomic interactions will contribute to the
force field and the resulting force field can be used without, or with
different external forces.

## Output\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The external forces are printed to the [OUTCAR](../output-files/OUTCAR.md)
file after the positions of ions. E.g.:

    external forces on ions in cartesian coordinates  (eV/Angst):
      0.00000000  0.00000000  0.50000000
      0.00000000  0.00000000  0.00000000
      0.00000000  0.00000000  0.00000000
      0.00000000  0.00000000 -0.50000000

After each ionic step, the external forces are included in the reported
TOTAL-FORCE array, but not separately listed, since they are not updated
during a VASP run.:

    POSITION                                       TOTAL-FORCE (eV/Angst)
    -----------------------------------------------------------------------------------
        -0.00000     -0.00000     20.27571         0.000000      0.000000      0.001257
         1.43189      0.82670     22.42983        -0.000000     -0.000000     -0.008077
         2.86378      1.65341     24.58497         0.000000      0.000000      0.008077
         0.00000      0.00000     26.73909        -0.000000     -0.000000     -0.001257
    -----------------------------------------------------------------------------------
       total drift:                                0.000000     -0.000000     -0.000000

## Example\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Example">edit</a> \| (./index.php.md)\]

As an example, the compression of an Al(001) slab under 4 GPa of
pressure is chosen. At ~39500 times the atmospheric pressure at sea
level, this is considerable, but pressures in
<a href="https://en.wikipedia.org/wiki/Diamond_anvil_cell"
class="external text" rel="nofollow">diamond anvil cells</a> can be two
orders of magnitude larger. The four-layer thick slab corresponding to
the following [POSCAR](../input-files/POSCAR.md) is already relaxed without
external forces:

     Al 001 slab
      1.00000000000000     
        4.0472922325000000    0.0000000000000000    0.0000000000000000
        0.0000000000000000    4.0472922325000000    0.0000000000000000
        0.0000000000000000    0.0000000000000000   16.0709387330000000
      Al
      8
     Selective dynamics
     Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000   F   F   F
      0.4999999999382325  0.4999999999382325  0.0000000000000000   F   F   F
      0.0000000000000000  0.4999999999382325  0.1291914423155097   T   T   T
      0.4999999999382325 -0.0000000000000000  0.1291914423155097   T   T   T
      0.0000000000000000  0.0000000000000000  0.2574944356749768   T   T   T
      0.4999999999382325  0.4999999999382325  0.2574944356749768   T   T   T
      0.0000000000000000  0.4999999999382325  0.3864211449750742   T   T   T
      0.4999999999382325  0.0000000000000000  0.3864211449750742   T   T   T

The pressure has to be converted into the correct units. Forces in VASP
are given in eV/Å, and an area in Å<sup>2</sup>, thus GPa needs to be
converted to (eV/Å)/Å<sup>2</sup>, or eV Å<sup>-3</sup>:

$\mathrm{GPa} = 10^9 \mathrm{Pa} = 10^9 \frac{\mathrm{N}}{\mathrm{m}^2} =
10^9 \frac{\mathrm{Nm}}{\mathrm{m}^3} = 10^9 \frac{6.2415 \times
10^{18}\mathrm{eV}}{10^{30} \AA^3} = 6.2415 \times 10^{-3}
\frac{\mathrm{eV}/\AA}{\AA^2}$

With a lattice parameter of 4.047Å, the surface area A of the slab is
about 16.381 Å<sup>2</sup>. Thus the total force in eV/Å we have to put
on the top layer to compress the slab with 4 GPa of pressure is:

$4
\times A \times 6.2415 \times 10^{-3} \simeq 0.409 \quad ,$

or 0.20448 eV/Å per surface atom. The [INCAR](../input-files/INCAR.md) file
can now be written:

     ENCUT = 250
     ISMEAR = 1
     SIGMA = 0.1
     NELMIN = 4
     NSW = 60
     ISIF = 2
     IBRION = 1
     POTIM = 0.75
     EDIFFG = -0.01
     EDIFF = 1E-6
     EFOR = 2*0 0.40896 17*0 -0.20448 2*0 -0.20448

Note that the forces on the top atoms are balanced by putting the
opposing force on one atom only. This is feasible since both atoms in
the bottom layer are fixed by selective dynamics flags.

Using a 5x5x1 Γ-centered mesh in the [KPOINTS](../input-files/KPOINTS.md)
file, and the standard PBE Al [POTCAR](../input-files/POTCAR.md), the
calculation converges in less than 10 ionic steps.

The slab is compressed by less than 2%, from 6.21 Å to 6.10 Å. This
relatively small compression at relatively high pressure is due to three
factors:

- 4 GPa corresponds to forces of ~0.2 eV/Å, which is only 20 times the
  negligible force limit of 0.01 eV/Å in this calculation.
- We do not allow the material to
  <a href="https://en.wikipedia.org/wiki/Poisson%27s_ratio"
  class="external text" rel="nofollow">expand in the direction normal to
  the pressure</a> by keeping the cell shape fixed with
  [ISIF](ISIF.md) = 2.
- Intra-atomic forces in perfect close-packed metallic crystals are
  powerful, and lattice imperfections usually mediate deformations in
  real materials.

For layered materials, molecules on surfaces, and other, less
strongly-bound systems, similar forces will have larger effects,
however.

## Related Tags and Sections\[<a href="/wiki/index.php?title=EFOR&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[ICONST](../input-files/ICONST.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EFOR-_incategory-Examples)

------------------------------------------------------------------------



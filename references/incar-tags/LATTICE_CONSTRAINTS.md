<!-- Source: https://vasp.at/wiki/index.php/LATTICE_CONSTRAINTS | revid: 28162 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LATTICE_CONSTRAINTS


LATTICE_CONSTRAINTS =
\[logical\]\[logical\]\[logical\] 

Description: Sets three boolean to selectively allow changes in the
lattice vectors.

------------------------------------------------------------------------

The lattice vectors $\mathbf{a}_{1}$, $\mathbf{a}_{2}$, $\mathbf{a}_{3}$ defined in the [POSCAR](../input-files/POSCAR.md) file
can be represented by following matrix:

$\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} &
a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}.$

LATTICE_CONSTRAINTS is used to
constrain certain entries of this matrix during an MD run.

## Orthorhombic case\[<a
href="/wiki/index.php?title=LATTICE_CONSTRAINTS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Orthorhombic case">edit</a> \| (./index.php.md)\]

For orthorhombic unit cells $\mathbf{A}$
is of diagonal form:

$\mathbf{A} = \begin{bmatrix} a_{11} & 0 & 0 \\ 0 & a_{22} & 0 \\ 0 & 0
& a_{33} \end{bmatrix},$

Therefore by setting one of the entries of
LATTICE_CONSTRAINTS to FALSE
the lattice parameter in this direction will not be allowed to change.
For <a href="/wiki/MD" class="mw-redirect" title="MD">MD simulations</a>
([IBRION](IBRION.md)=0), we recommend using
LATTICE_CONSTRAINTS for
(orthorhombic) liquids in the isobaric-isothermal
([NpT](../misc/NpT_ensemble.md)) ensemble in the following
way:

    LATTICE_CONSTRAINTS = .FALSE. .FALSE. .TRUE.

Here, the first two lattice constants are not allowed to change. The
third lattice constant needs to be free to allow volume changes for the
barostat. The system is then like a piston. The constraints are
necessary for liquids in [NpT](../misc/NpT_ensemble.md)
simulations because if all lattice degrees of freedom are allowed to
relax, irreversible deformations of the cell are very likely to happen.
This can lead to undesirable results like a very flat supercell, which
cannot be used to obtain valid MD trajectories.

For <a href="/wiki/Ionic_minimization" class="mw-redirect"
title="Ionic minimization">structure relaxation</a>
([IBRION](IBRION.md)=1,2),
LATTICE_CONSTRAINTS is useful
to relax the lattice constants of 2D materials. In case of a slab in the
$\mathbf{a}_1$-$\mathbf{a}_2$ plane, add vacuum padding along
$\mathbf{a}_3$ and set

    LATTICE_CONSTRAINTS = .TRUE. .TRUE. .FALSE.

## Non-orthorhombic case\[<a
href="/wiki/index.php?title=LATTICE_CONSTRAINTS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Non-orthorhombic case">edit</a> \| (./index.php.md)\]

For non-orthorhombic boxes
LATTICE_CONSTRAINTS is more
complicated to use. The tag will set certain rows and columns of the
stress tensor

$\mathbf{\sigma} = \begin{bmatrix} xx & xy & xz \\ yx & yy & yz \\ zx &
zy & zz \end{bmatrix},$

to zero. By setting certain entries of the stress tensor to zero the
corresponding entries of the lattice $\mathbf{A}$
will not be updated. For example when setting
LATTICE_CONSTRAINTS
= .FALSE. .TRUE. .TRUE. the used stress tensor will look like

$\mathbf{\sigma} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & yy & yz \\ 0 & zy &
zz \end{bmatrix},$

and therefore the first row and the first column of the lattice
$\mathbf{A}$ will not change. Another example would be
to set
LATTICE_CONSTRAINTS
= .FALSE. .TRUE. .FALSE. resulting in the following stress tensor

$\mathbf{\sigma} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & yy & 0 \\ 0 & 0 & 0
\end{bmatrix}$

So only the $yy$/$a_{22}$
entry of the lattice $\mathbf{A}$
will change.

|  |
|----|
| **Mind:** Note that for non-orthorhombic boxes the angles between the lattice vectors $\mathbf{a}_{1}$, $\mathbf{a}_{2}$, $\mathbf{a}_{3}$ will not be conserved. |

|  |
|----|
| **Mind:** LATTICE_CONSTRAINTS in combination with [IBRION](IBRION.md)=1,2 is available from VASP 6.4.3. |

|  |
|----|
| **Mind:** LATTICE_CONSTRAINTS in combination with [ISIF](ISIF.md)=4,5 is available from VASP 6.5.1. |

|  |
|----|
| **Warning:** Be aware of a bug in versions \< 6.5.0 as described in following forum post<a href="https://www.vasp.at/forum/viewtopic.php?p=29882#p29882"
class="external autonumber" rel="nofollow">[1]</a>. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LATTICE_CONSTRAINTS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBRION](IBRION.md), [MDALGO](MDALGO.md),
[Interface
pinning](../categories/Category-Interface_pinning.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LATTICE_CONSTRAINTS-_incategory-Examples)

------------------------------------------------------------------------



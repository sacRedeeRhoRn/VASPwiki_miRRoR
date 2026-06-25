<!-- Source: https://vasp.at/wiki/index.php/LCALCEPS | revid: 33371 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LCALCEPS


LCALCEPS = .TRUE. \| .FALSE.  
Default: **LCALCEPS** = .FALSE. 

Description: for
LCALCEPS=.TRUE. the
macroscopic ion-clamped static dielectric tensor, Born effective charge
tensors, and the ion-clamped piezoelectric tensor of the system are
determined from the response to finite electric fields.

------------------------------------------------------------------------

For LCALCEPS=.TRUE., VASP
calculates the ion-clamped static dielectric tensor

$\epsilon^\infty_{ij}=\delta_{ij}+
\frac{4\pi}{\epsilon_0}\frac{\partial P_i}{\partial \mathcal{E}_j},
\qquad {i,j=x,y,z}$

the Born effective charge tensors

$Z^\*_{ij}=\frac{\Omega}{e}\frac{\partial P_i}{\partial u_j}
=\frac{1}{e}\frac{\partial F_j}{\partial \mathcal{E}_i}, \qquad
{i,j=x,y,z}$

and the ion-clamped piezoelectric tensor of the system

$e^{(0)}_{ij}=-\frac{\partial \sigma_i}{\partial \mathcal{E}_j}, \qquad
{i=xx, yy, zz, xy, yz, zx}\quad{j=x,y,z}$

from the [self-consistent response to a finite electric
field](../theory/Berry_phases_and_finite_electric_fields.md)
*ε*. In this case, the "response" of
the system is the change in the polarization **P**, the Hellmann-Feynman
forces **F**, and the stress tensor σ. Mind the [definition/sign
convention of the stress tensor](ISIF.md).

If this is combined with [IBRION](IBRION.md)=6, the
contribution from the ionic relaxations to the piezoelectric and
dielectric tensors are calculated as well.

To this end VASP will perform essentially three successive calculations,
with:

    EFIELD_PEAD= εx 0 0

    EFIELD_PEAD= 0 εy 0

    EFIELD_PEAD= 0 0 εz 

where, by default, VASP chooses
*ε*<sub>x</sub>=*ε*<sub>y</sub>=*ε*<sub>z</sub>=0.01
eV/Å.

This default may be overwritten by specifying

    EFIELD_PEAD= εx εy εz

in the [INCAR](../input-files/INCAR.md) file.

The relevant output is found in the [OUTCAR](../output-files/OUTCAR.md)
file, immediately following the lines (see the description of
[LEPSILON](LEPSILON.md)=.TRUE. as well):

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects) 

    BORN EFFECTIVE CHARGES (including local field effects) 

    PIEZOELECTRIC TENSOR (including local field effects) 

In the above, "including local field effects" pertains to the fact that
changes in the orbitals due to the electric field induce changes in the
Hartree- and exchange-correlation potential. One may choose to limit
this to changes in the Hartree potential alone, by specifying:

    LRPA=.TRUE.

This is commonly referred to as the response within the "Random Phase
Approximation" (RPA), or the "neglect of local field effects". The
OUTCAR file will now contain additional sections, headed by the lines:

    MACROSCOPIC STATIC DIELECTRIC TENSOR (excluding local field effects) 

    BORN EFFECTIVE CHARGES (excluding local field effects) 

    PIEZOELECTRIC TENSOR (excluding local field effects)

------------------------------------------------------------------------

|  |
|----|
| **Important:** For standard DFT functionals, ε<sub>∞</sub>, *Z*<sup>\*</sup>, and *e*<sup>(0)</sup> may be more easily calculated from density functional perturbation theory (see [`LEPSILON`](LEPSILON.md)` = .TRUE.`). For functionals that depend not only on the density but also explicitly on the orbitals, like [hybrid functionals](../methods/Category-Hybrid_functionals.md), density functional perturbation theory is presently not implemented and [`LEPSILON`](LEPSILON.md)` = .TRUE.` is not applicable. |

|  |
|----|
| **Warning:** The piezoelectric tensor has the wrong sign in Vasp 5.4.4 and older. The bug is fixed with <a href="http://cms.mpi.univie.ac.at/patches/patch.5.4.4.16052018.gz"
class="external text" rel="nofollow">patch.5.4.4.16052018.gz</a>. |

## Related tags and articles\[<a href="/wiki/index.php?title=LCALCEPS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LEPSILON](LEPSILON.md),
[LCALCPOL](LCALCPOL.md),
[EFIELD_PEAD](EFIELD_PEAD.md),
[LPEAD](LPEAD.md), [IPEAD](IPEAD.md),
[LBERRY](LBERRY.md), [IGPAR](IGPAR.md),
[NPPSTR](NPPSTR.md), [DIPOL](DIPOL.md),
[IBRION](IBRION.md), [Berry phases and finite electric
fields](../theory/Berry_phases_and_finite_electric_fields.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LCALCEPS-_incategory-Examples)

------------------------------------------------------------------------



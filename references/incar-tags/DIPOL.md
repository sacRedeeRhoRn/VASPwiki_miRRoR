<!-- Source: https://vasp.at/wiki/index.php/DIPOL | revid: 32772 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DIPOL


DIPOL = \[real array\] 

Description: specifies the center of the cell in direct lattice
coordinates with respect to which the total dipole-moment in the cell is
calculated.

------------------------------------------------------------------------

The center of the cell w.r.t. which the total dipole-moment in the cell
is calculated is specified as

    DIPOL=Rx Ry Rz

where **R**<sub>x</sub>, **R**<sub>y</sub> and **R**<sub>z</sub> are
given in direct lattice coordinates.

Calculations using the dipole correction, i.e. using tags
[IDIPOL](IDIPOL.md) or [LDIPOL](LDIPOL.md),
require a definition of the center of the cell. Results of the computed
dipole moment might differ for different positions. The reason for this
difference is that the definition of the dipole 'destroys' the
translational symmetry, i.e., the dipole is defined as

$\int ({\mathbf r}-{\mathbf R}_{\rm center}) \rho_{\rm
ions+valence}({\mathbf r}) d^3 {\mathbf r}.$

This measure will provide consistent values only if
$\rho_{\rm ions+valence}$ drops to zero at some
distance from $\mathbf R_{\rm center}$. If this is not the case, the values are extremely
sensitive with respect to changes in $\mathbf R_{\rm center}$. In such cases, it might be beneficial to increase the
size of the cell along the vacuum dimension (for surfaces) or for the
entire cell (for isolated molecules). For practical purposes this means
that for slab calculations or surfaces the position specified by
DIPOL should roughly
correspond to the center of mass of the atoms in the cell, so that there
is enough vacuum for the field to dissipate. See the [Electrostatic
corrections](../tutorials/Electrostatic_corrections.md)
page for an example.

  

|  |
|----|
| **Mind:** If the flag is not set, VASP determines where the charge density averaged over one plane drops to a minimum and calculates the center of the charge distribution by adding half of the lattice vector perpendicular to the plane where the charge density has a minimum (this is a rather reliable approach for orthorhombic cells) |

|  |
|----|
| **Tip:** For calculations of isolated molecules and surfaces with the dipole correction, use DIPOL as the center of mass of the atoms in your cell. Additionally, note that for surfaces, only the component normal to the surface is meaningful. |

## Related tags and articles\[<a href="/wiki/index.php?title=DIPOL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NELECT](NELECT.md), [EPSILON](EPSILON.md),
[IDIPOL](IDIPOL.md), [LDIPOL](LDIPOL.md),
[LMONO](LMONO.md), [EFIELD](EFIELD.md),
<a href="/wiki/Monopole_Dipole_and_Quadrupole_corrections"
class="mw-redirect"
title="Monopole Dipole and Quadrupole corrections">Monopole, Dipole and
Quadrupole corrections</a>, [Electrostatic
corrections](../tutorials/Electrostatic_corrections.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-DIPOL-_incategory-Examples)

------------------------------------------------------------------------



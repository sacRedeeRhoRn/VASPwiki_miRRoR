<!-- Source: https://vasp.at/wiki/index.php/IDIPOL | revid: 28126 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IDIPOL
IDIPOL = 1 \| 2 \| 3 \| 4 

Description: IDIPOL switches on monopole/dipole and quadrupole
corrections to the total energy in a specific direction (1-3) or all
directions (4)

------------------------------------------------------------------------

## IDIPOL = 1-3
The dipole moment will be calculated only parallel to the direction of
the first, second or third lattice vector, respectively. The corrections
for the total energy are calculated as the energy difference between a
monopole/dipole and quadrupole in the current supercell and the same
dipole placed in a super cell with the corresponding lattice vector
approaching infinity.

|  |
|----|
| **Tip:** This flag should be used for slab calculations, with the surface normal being the direction in which the IDIPOL is set, and optionally specifying the center of mass of the slab with the [DIPOL](DIPOL.md) tag. |

## IDIPOL = 4
For IDIPOL=4 the full dipole moment in all directions will be
calculated, and the corrections to the total energy are calculated as
the energy difference between a monopole/dipole/quadrupole in the
current supercell and the same monopole/dipole/quadrupole placed in a
vacuum.

|                                                                 |
|-----------------------------------------------------------------|
| **Tip:** Use this flag for calculations for isolated molecules. |

**Note**: strictly speaking quadrupole corrections is not the proper
wording. The relevant quantity is

$\int d^3{\mathbf r} \rho(\mathbf r) \Vert \mathbf
r\Vert^2.$

## Related tags and articles
[Monopole Dipole and Quadrupole
corrections](https://vasp.at/wiki/index.php/Monopole_Dipole_and_Quadrupole_corrections),
[NELECT](NELECT.md), [EPSILON](EPSILON.md),
[DIPOL](DIPOL.md), [LDIPOL](LDIPOL.md),
[LMONO](LMONO.md), [EFIELD](EFIELD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IDIPOL-_incategory-Examples)

------------------------------------------------------------------------

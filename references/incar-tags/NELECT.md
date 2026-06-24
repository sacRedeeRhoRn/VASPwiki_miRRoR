<!-- Source: https://vasp.at/wiki/index.php/NELECT | revid: 32552 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NELECT
NELECT = \[real\]  
Default: **NELECT** = number of valence electrons 

Description: NELECT sets the number of electrons.

------------------------------------------------------------------------

|  |
|----|
| **Warning:** Unless you would like to perform a charged calculation, you should not set this line. |

The number of electrons is determined automatically from the
[POTCAR](../input-files/POTCAR.md) (ZVAL of the element) and
[POSCAR](../input-files/POSCAR.md) file (number of the atoms of the
respective atom type) assuming the cell is charge-neutral. If the number
of electrons is not compatible with the number derived from the valence
and the number of atoms a homogeneous background charge is assumed. If
the number of ions specified in the [POSCAR](../input-files/POSCAR.md) file
is 0 and NELECT=n, then the energy of a homogeneous electron gas is
calculated.

## Charged calculations
|  |
|----|
| **Warning:** Using the NELECT tag without the use of an appropriate correction leads to a very slow convergence of energies with respect to the size *L* of the supercell. |

The required first-order correction to the energy caused by an excess
charge is given by

$\frac{e^2q^2\alpha}{L\epsilon}$

where *q* is the net charge of the system, α the Madelung constant of a
point charge *q* placed in a homogeneous background charge *-q*, and ε
the dielectric constant of the system. For atoms or molecules surrounded
by vacuum, ε takes on the vacuum value ε=1. VASP can automatically
correct this leading error, see [Electrostatic
corrections](../tutorials/Electrostatic_corrections.md)
for further information. It is important to emphasize that the total
energy cannot be corrected for charged slabs, since a charged slab
results in an electrostatic potential that grows with the distance from
the slab. This non-convergence of the potential is a result of the
interaction between the charged slab and the compensating background. A
practical consequence of this non-convergence is that the total energy
depends linearly on the width of the vacuum.

|  |
|----|
| **Warning:** Presently, no simple *a posteriori* correction scheme is implemented in VASP for slab calculations. Total energies from charged slab calculations must be used with care. In certain cases, relative energies between two charged surface calculations may be useful |

## Related tags and articles
[Monopole Dipole and Quadrupole
corrections](https://vasp.at/wiki/index.php/Monopole_Dipole_and_Quadrupole_corrections),
[EPSILON](EPSILON.md), [DIPOL](DIPOL.md),
[IDIPOL](IDIPOL.md), [LMONO](LMONO.md),
[LDIPOL](LDIPOL.md), [EFIELD](EFIELD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NELECT-_incategory-Examples)

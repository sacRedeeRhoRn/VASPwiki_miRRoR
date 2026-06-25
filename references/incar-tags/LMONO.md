<!-- Source: https://vasp.at/wiki/index.php/LMONO | revid: 22411 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMONO


LMONO = .TRUE. \| .FALSE.  
Default: **LMONO** = .FALSE. 

Description: LMONO switches on
monopole-monopole corrections for the total energy.

------------------------------------------------------------------------

The flag switches on monopole corrections for charged systems. The
correction is calculated only a posteriori for the total energy. No
correction to the potential is calculated.

|  |
|----|
| **Tip:** If corrections for the potential are desired as well, please use [LDIPOL](LDIPOL.md) instead (when using [LDIPOL](LDIPOL.md), VASP automatically determines whether the system is charged and activates the monopole corrections automatically). |

The primary use of this flag is for defect calculations in charged
supercells, as well as charged 0D systems (molecules and atoms). VASP
also automatically calculates corrections to the total energy related to
repeated dipoles ([IDIPOL](IDIPOL.md)=4). The user then
needs to decide whether those are sensible or not. Specifically, for
super cells using periodic boundary conditions, it is often not possible
to determine the dipole at the defect site accurately, whereas for 0D
systems (i.e. atoms and molecules) the dipole can be determined
accurately.

## Related tags and articles\[<a href="/wiki/index.php?title=LMONO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Monopole_Dipole_and_Quadrupole_corrections"
class="mw-redirect"
title="Monopole Dipole and Quadrupole corrections">Monopole Dipole and
Quadrupole corrections</a>, [NELECT](NELECT.md),
[EPSILON](EPSILON.md), [IDIPOL](IDIPOL.md),
[DIPOL](DIPOL.md), [LDIPOL](LDIPOL.md),
[EFIELD](EFIELD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMONO-_incategory-Examples)

------------------------------------------------------------------------



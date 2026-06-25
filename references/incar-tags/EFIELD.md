<!-- Source: https://vasp.at/wiki/index.php/EFIELD | revid: 32770 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EFIELD


EFIELD = \[real\] 

Description: EFIELD controls
the magnitude of the applied electric force field.

------------------------------------------------------------------------

It is possible to apply an external electrostatic field in slab, or
molecular calculations. Presently only a single value can be supplied
and the field is applied in the direction selected by
[IDIPOL](IDIPOL.md)=1-4. The electric force field is
supplied in units of eV/Å. Dipole corrections to the potential
([LDIPOL](LDIPOL.md)=.TRUE.) can and should be turned on to
avoid interactions between the periodically repeated images.

|  |
|----|
| **Mind:** The electric field is defined opposite to the common definition. So electrons will move along the direction of the electric field. |

## Related tags and articles\[<a href="/wiki/index.php?title=EFIELD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Monopole_Dipole_and_Quadrupole_corrections"
class="mw-redirect"
title="Monopole Dipole and Quadrupole corrections">Monopole Dipole and
Quadrupole corrections</a>, [NELECT](NELECT.md),
[EPSILON](EPSILON.md), [IDIPOL](IDIPOL.md),
[DIPOL](DIPOL.md), [LMONO](LMONO.md),
[LDIPOL](LDIPOL.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EFIELD-_incategory-Howto)

------------------------------------------------------------------------



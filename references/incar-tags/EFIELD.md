<!-- Source: https://vasp.at/wiki/index.php/EFIELD | revid: 32770 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EFIELD
EFIELD = \[real\] 

Description: EFIELD controls the magnitude of the applied electric force
field.

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

## Related tags and articles
[Monopole Dipole and Quadrupole
corrections](https://vasp.at/wiki/index.php/Monopole_Dipole_and_Quadrupole_corrections),
[NELECT](NELECT.md), [EPSILON](EPSILON.md),
[IDIPOL](IDIPOL.md), [DIPOL](DIPOL.md),
[LMONO](LMONO.md), [LDIPOL](LDIPOL.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EFIELD-_incategory-Howto)

------------------------------------------------------------------------

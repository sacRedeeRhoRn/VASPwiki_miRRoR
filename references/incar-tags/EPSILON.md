<!-- Source: https://vasp.at/wiki/index.php/EPSILON | revid: 22413 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EPSILON


EPSILON = \[real\]  
Default: **EPSILON** = 1 

Description: EPSILON sets the
dielectric constant of the medium.

------------------------------------------------------------------------

VASP uses this flag only to scale the calculated
<a href="/wiki/Monopole_Dipole_and_Quadrupole_corrections"
class="mw-redirect"
title="Monopole Dipole and Quadrupole corrections">monopole and dipole
corrections</a>. EPSILON
defaults to 1, which is the proper value for isolated atoms and
molecules. For solids, the screening properties can and should be
determined using the linear response routines of VASP (see
[LEPSILON](LEPSILON.md) and/or
[LCALCEPS](LCALCEPS.md)). Ionic contributions to the
dielectric tensor should be included, if the ions are allowed to relax.
Ionic contributions to the dielectric tensor can be calculated using
[IBRION](IBRION.md)=8.

## Related tags and articles\[<a href="/wiki/index.php?title=EPSILON&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Monopole_Dipole_and_Quadrupole_corrections"
class="mw-redirect"
title="Monopole Dipole and Quadrupole corrections">Monopole Dipole and
Quadrupole corrections</a>, [NELECT](NELECT.md),
[DIPOL](DIPOL.md), [IDIPOL](IDIPOL.md),
[LDIPOL](LDIPOL.md), [LMONO](LMONO.md),
[EFIELD](EFIELD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EPSILON-_incategory-Examples)

------------------------------------------------------------------------



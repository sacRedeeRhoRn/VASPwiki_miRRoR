<!-- Source: https://vasp.at/wiki/index.php/POMASS | revid: 26981 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# POMASS


POMASS = \[real array\]  
Default: **POMASS** = values read from [POTCAR](../input-files/POTCAR.md) 

Description: Array of masses of the atoms in atomic units.

------------------------------------------------------------------------

POMASS determines the atomic
mass of each atomic species. For standard calculations this tag should
be omitted since the atomic masses for each species are read from the
[POTCAR](../input-files/POTCAR.md) file (they are also called
POMASS there). However if one
needs to change the atomic mass of some species, e.g., the mass of
Hydrogen atoms in <a href="/wiki/Molecular_dynamics" class="mw-redirect"
title="Molecular dynamics">molecular dynamics</a> calculations, the
atomic masses of all species need to be set with this tag in the order
they appear on the [POTCAR](../input-files/POTCAR.md) file. After setting
POMASS to different values in
the [INCAR](../input-files/INCAR.md) file than on the
[POTCAR](../input-files/POTCAR.md) file the following message will occur on
stdout when running VASP, informing the user that the mass has changed:

` WARNING: mass on POTCAR and INCAR are incompatible. `

If any incompatibilities exist, e.g. the number of entries doesn't agree
with that on the [POTCAR](../input-files/POTCAR.md), VASP will stop.

## Related tags and sections\[<a href="/wiki/index.php?title=POMASS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[ZVAL](ZVAL.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-POMASS-_incategory-Examples)



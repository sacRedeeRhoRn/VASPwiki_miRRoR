<!-- Source: https://vasp.at/wiki/index.php/LORBMOM | revid: 36605 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LORBMOM


LORBMOM = .TRUE. \| .FALSE.  
Default: **LORBMOM** = .FALSE. 

Description: Specifies whether the orbital moments are written out. Only
applicable in a calculation using [LSORBIT](LSORBIT.md) =
True .

------------------------------------------------------------------------

If LORBMOM=.TRUE. is set, VASP
will use the projectors of the PAW potentials to calculate the orbital
angular moment within the PAW spheres, and write them to the
[OUTCAR](../output-files/OUTCAR.md) file. Look for

     orbital moment (x)

to find the orbital- and site-resolved table.

## Related tags and articles\[<a href="/wiki/index.php?title=LORBMOM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LSORBIT](LSORBIT.md), [LORBIT](LORBIT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LORBMOM-_incategory-Examples)

------------------------------------------------------------------------



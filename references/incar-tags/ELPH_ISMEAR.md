<!-- Source: https://vasp.at/wiki/index.php/ELPH_ISMEAR | revid: 32980 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_ISMEAR


ELPH_ISMEAR = -15 \| -14 \| -5
\| -4 \| -1 \| 0 \| \[integer\]\>0  
Default: **ELPH_ISMEAR** = 0 

Description: Chooses the smearing method to determine the fermi level
and chemical potential before an electron-phonon calculation.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

ELPH_ISMEAR is very similar to
[ISMEAR](ISMEAR.md). The difference is that
ELPH_ISMEAR is used to
determine the chemical potential in the context of electron-phonon
calculation. The Kohn-Sham states for which to calculate the chemical
potential correspond to the **k**-point grid specified via the
[KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md) file.

The chemical potential is determined for the list of temperatures
[ELPH_SELFEN_TEMPS](ELPH_SELFEN_TEMPS.md) and
carrier concentrations specified by
[ELPH_SELFEN_CARRIER_DEN](ELPH_SELFEN_CARRIER_DEN.md)
or
[ELPH_SELFEN_CARRIER_PER_CELL](ELPH_SELFEN_CARRIER_PER_CELL.md).
Alternatively, one can specify the chemical potential and determine the
carrier concentration using
[ELPH_SELFEN_MU](ELPH_SELFEN_MU.md).

## Tag options\[<a
href="/wiki/index.php?title=ELPH_ISMEAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Tag options">edit</a> \| (./index.php.md)\]

`ELPH_ISMEAR`` > 1`  
Method of Methfessel-Paxton of order
ELPH_ISMEAR (for details see
[ISMEAR](ISMEAR.md))

`ELPH_ISMEAR`` = 0`  
Gaussian smearing (for details see [ISMEAR](ISMEAR.md))

`ELPH_ISMEAR`` = -1`  
Fermi-Dirac smearing (for details see [ISMEAR](ISMEAR.md))

`ELPH_ISMEAR`` = -4`  
Tetrahedron method (zero temperature) (for details see
[ISMEAR](ISMEAR.md))

`ELPH_ISMEAR`` = -5`  
Tetrahedron method (zero temperature) with Blöchl corrections (for
details see [ISMEAR](ISMEAR.md))

`ELPH_ISMEAR`` = -14`  
Tetrahedron method (finite temperature)

`ELPH_ISMEAR`` = -15`  
Tetrahedron method (finite temperature) with Blöchl corrections

`ELPH_ISMEAR`` = -24`  
Tetrahedron method (finite temperature) - same as -14 but using a faster
and memory saving algorithm

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_ISMEAR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ISMEAR](ISMEAR.md)
- [ELPH_SELFEN_MU](ELPH_SELFEN_MU.md)
- [KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md)



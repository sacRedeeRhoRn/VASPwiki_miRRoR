<!-- Source: https://vasp.at/wiki/index.php/KGAMMA | revid: 35395 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KGAMMA


KGAMMA = \[logical\]  
Default: **KGAMMA** = .TRUE. 

Description: Whether the automatically generated **k**-point mesh is
centered at the $\Gamma$
point.

------------------------------------------------------------------------

If `KGAMMA`` = .TRUE.`
(default), the **k**-point mesh is centered at the
$\Gamma$ point, i.e., it always includes the
$\Gamma$ point. If
`KGAMMA`` = .FALSE.`, the mesh
is shifted away from the $\Gamma$ point
as in a Monkhorst-Pack grid. The number of **k** points on the mesh is
controlled by [KSPACING](KSPACING.md) and
[KSPACING_OPT](KSPACING_OPT.md).

|  |
|----|
| **Important:** If a [KPOINTS](../input-files/KPOINTS.md) file is present, VASP ignores the KGAMMA and [KSPACING](KSPACING.md) tags. Likewise, if a [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file is present, VASP ignores KGAMMA and [KSPACING_OPT](KSPACING_OPT.md). |

## Related tags and articles\[<a href="/wiki/index.php?title=KGAMMA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[KSPACING](KSPACING.md),
[KSPACING_OPT](KSPACING_OPT.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-KGAMMA-_incategory-HowTo)



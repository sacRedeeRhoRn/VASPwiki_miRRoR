<!-- Source: https://vasp.at/wiki/index.php/KPOINTS_WAN | revid: 35408 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINTS WAN


KPOINTS_WAN is an optional
input file to obtain eigenstates and eigenenergies at the specified
**k** points from [Wannier
functions](../categories/Category-Wannier_functions.md).
The format is the same as for the [KPOINTS](KPOINTS.md)
file.

|  |
|----|
| **Important:** The VASP calculation must include the construction of [Wannier functions](../categories/Category-Wannier_functions.md), e.g., using [LSCDM](../incar-tags/LSCDM.md) or [LWANNIER90](../incar-tags/LWANNIER90.md). |

KPOINTS_WAN is read
automatically when present. To avoid this, set
[LKPOINTS_WAN](../incar-tags/LKPOINTS_WAN.md)`=.FALSE.` in the
[INCAR](INCAR.md) file. VASP writes corresponding fields in
the [vaspout.h5](../output-files/Vaspout.h5.md) file and
[vasprun.xml](../output-files/Vasprun.xml.md) file indicated by the
keyword *kpoints_wan*.

|  |
|----|
| **Mind:** Available as of VASP 6.3.0. |

## Related tags and sections\[<a
href="/wiki/index.php?title=KPOINTS_WAN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[KPOINTS](KPOINTS.md),
[KPOINTS_OPT](KPOINTS_OPT.md),
[LKPOINTS_WAN](../incar-tags/LKPOINTS_WAN.md),
<a href="/wiki/index.php?title=PROCAR_WAN&amp;action=edit&amp;redlink=1"
class="new" title="PROCAR WAN (page does not exist)">PROCAR_WAN</a>,
[LSCDM](../incar-tags/LSCDM.md),
[LWANNIER90](../incar-tags/LWANNIER90.md),
[LOCPROJ](../incar-tags/LOCPROJ.md)



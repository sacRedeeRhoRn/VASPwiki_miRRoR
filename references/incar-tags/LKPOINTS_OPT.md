<!-- Source: https://vasp.at/wiki/index.php/LKPOINTS_OPT | revid: 35399 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LKPOINTS_OPT


LKPOINTS_OPT = .TRUE.\|
.FALSE. 

|  |  |  |
|----|----|----|
| Default: **LKPOINTS_OPT** | = .TRUE. | if [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file is present. |

Description: Enable reading the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file.

------------------------------------------------------------------------

To avoid reading the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file
without removing it from the working directory, set
`LKPOINTS_OPT`` = .FALSE.` in
the [INCAR](../input-files/INCAR.md) file.

## Related tags and articles\[<a
href="/wiki/index.php?title=LKPOINTS_OPT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

Tags: [KSPACING_OPT](KSPACING_OPT.md)

Files: [KPOINTS_OPT](../input-files/KPOINTS_OPT.md),
[PROCAR_OPT](../output-files/PROCAR_OPT.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LKPOINTS_OPT-_incategory-HowTo)



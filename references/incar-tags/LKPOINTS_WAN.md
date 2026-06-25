<!-- Source: https://vasp.at/wiki/index.php/LKPOINTS_WAN | revid: 35410 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LKPOINTS WAN


LKPOINTS_WAN = .TRUE.\|
.FALSE. 

|  |  |  |
|----|----|----|
| Default: **LKPOINTS_WAN** | = .TRUE. | if [KPOINTS_WAN](../input-files/KPOINTS_WAN.md) file is present. |

Description: LKPOINTS_WAN
controlls whether VASP reads the
[KPOINTS_WAN](../input-files/KPOINTS_WAN.md) file.

------------------------------------------------------------------------

To avoid reading the [KPOINTS_WAN](../input-files/KPOINTS_WAN.md) file
without removing it from the working directory, the
LKPOINTS_WAN tag can be set to
`.FALSE.` in the [INCAR](../input-files/INCAR.md) file.

## Related tags and articles\[<a
href="/wiki/index.php?title=LKPOINTS_WAN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[KPOINTS_WAN](../input-files/KPOINTS_WAN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LKPOINTS_WAN-_incategory-Examples)

------------------------------------------------------------------------



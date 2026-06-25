<!-- Source: https://vasp.at/wiki/index.php/LCHARG | revid: 37108 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LCHARG


LCHARG = \[logical\]  
Default: **LCHARG** = .True. 

Description: Determines whether the charge density is written.

------------------------------------------------------------------------

For LCHARG = T  (default), the
files [CHGCAR](../input-files/CHGCAR.md) and [CHG](../output-files/CHG.md) are
written. If [LH5](LH5.md) = T , the charge density is instead
written to [vaspwave.h5](../output-files/Vaspwave.h5.md).

|  |
|----|
| **Mind:** For VASP version 6.0 to 6.4.2 the default for LCHARG = .NOT.[LH5](LH5.md)  |

## Related tags and articles\[<a href="/wiki/index.php?title=LCHARG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[LWAVE](LWAVE.md), [LCHARGH5](LCHARGH5.md),
[LH5](LH5.md), [LTAU](LTAU.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LCHARG-_incategory-Howto)



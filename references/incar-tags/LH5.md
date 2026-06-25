<!-- Source: https://vasp.at/wiki/index.php/LH5 | revid: 37113 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LH5


LH5 = \[logical\]  
Default: **LH5** = .FALSE. 

Description: LH5 determines
whether the output is written to the legacy files
([CHGCAR](../input-files/CHGCAR.md), [CHG](../output-files/CHG.md),
[WAVECAR](../input-files/WAVECAR.md)) or the
[vaspwave.h5](../output-files/Vaspwave.h5.md) file. Hence, setting
LH5=.TRUE. will suppress
legacy file output all together. Whether or not the charge density or
wave functions are written to
[vaspwave.h5](../output-files/Vaspwave.h5.md) is then determined by
setting [LCHARG](LCHARG.md) and [LWAVE](LWAVE.md)
accordingly.

------------------------------------------------------------------------

|  |
|----|
| **Mind:** H5 support is available as of VASP version 6.0 |

|  |
|----|
| **Mind:** Additional datasets are written to this file as of 6.6.0. |

## Related tags and articles\[<a href="/wiki/index.php?title=LH5&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[LWAVE](LWAVE.md), [LCHARG](LCHARG.md),
[LCHARGH5](LCHARGH5.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LH5-_incategory-Examples)



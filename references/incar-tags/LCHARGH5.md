<!-- Source: https://vasp.at/wiki/index.php/LCHARGH5 | revid: 37114 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LCHARGH5


LCHARGH5 = \[logical\]  
Default: **LCHARGH5** = [LH5](LH5.md) 

Description: Determines whether the charge densities are written to
[vaspwave.h5](../output-files/Vaspwave.h5.md).

------------------------------------------------------------------------

In most case it is enough to set [LH5](LH5.md) and/or
[LCHARG](LCHARG.md) with the following exception: Explicitly
set

     LCHARGH5=True
     LH5=False

in order to get the charge density to the
[vaspwave.h5](../output-files/Vaspwave.h5.md) for plotting with
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> while running a
calculation where restart information (wave functions, etc) is written
to legacy files ([WAVECAR](../input-files/WAVECAR.md)).

|  |
|----|
| **Mind:** LCHARGH5 is available as of VASP version 6.0 |

## Related tags and articles\[<a href="/wiki/index.php?title=LCHARGH5&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[LWAVE](LWAVE.md), [LWAVEH5](LWAVEH5.md),
[LCHARG](LCHARG.md), [LH5](LH5.md)



<!-- Source: https://vasp.at/wiki/index.php/LPOSNICS | revid: 34598 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LPOSNICS


LPOSNICS = .TRUE.\| .FALSE. 

|  |  |  |
|----|----|----|
| Default: **LPOSNICS** | = .TRUE. | if [POSNICS](POSNICS.md) file is present. |

Description: LPOSNICS controls
if VASP reads the [POSNICS](POSNICS.md) file.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

To avoid reading the [POSNICS](POSNICS.md) file without
removing it from the working directory, the
LPOSNICS tag can be set to
`.FALSE.` in the [INCAR](../input-files/INCAR.md) file.

## Related tags and articles\[<a href="/wiki/index.php?title=LPOSNICS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md), [NUCIND](NUCIND.md),
[POSNICS](POSNICS.md),
<a href="https://www.vasp.at/tutorials/latest/nmr/part3/#NMR-e09"
class="external text" rel="nofollow">tutorial</a>



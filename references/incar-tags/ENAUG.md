<!-- Source: https://vasp.at/wiki/index.php/ENAUG | revid: 26953 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENAUG


ENAUG = \[real\]  
Default: **ENAUG** = largest *EAUG* read from the
[POTCAR](../input-files/POTCAR.md) file 

Description: Specifies the cutoff energy of the plane-wave
representation of the augmentation charges in eV.

------------------------------------------------------------------------

ENAUG determines
[NGXF](NGXF.md), [NGYF](NGYF.md), and
[NGZF](NGZF.md) in accordance with the
[PREC](PREC.md) tag.

|  |
|----|
| **Deprecated:** ENAUG is considered as deprecated and should not be used anymore. |

|  |
|----|
| **Warning:** Setting ENAUG has an effect only if [PREC](PREC.md) is set to one of the old settings (Low, Medium or High), otherwise it is ignored. |

## Related tags and articles\[<a href="/wiki/index.php?title=ENAUG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NGXF](NGXF.md), [NGYF](NGYF.md),
[NGZF](NGZF.md), [ENCUT](ENCUT.md),
[PREC](PREC.md), [PRECFOCK](PRECFOCK.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ENAUG-_incategory-Examples)



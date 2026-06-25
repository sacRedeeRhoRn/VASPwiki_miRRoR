<!-- Source: https://vasp.at/wiki/index.php/IMAGE_1 | revid: 37294 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IMAGE_1


IMAGE_1 = block construct  
Default: **IMAGE_1** = None 

Description: Group [INCAR](../input-files/INCAR.md) settings for
calculations using [IMAGES](IMAGES.md).

------------------------------------------------------------------------

IMAGE_1 defines the
[INCAR](../input-files/INCAR.md) settings used for a calculation in an image
calculation, e.g., `01` for [nudged elastic
band](../tutorials/Nudged_elastic_bands.md) calculations,
[parallel tempering](LTEMPER.md), and [thermodynamic
integration](VCAIMAGES.md), cf.
[IMAGES](IMAGES.md) for use cases of the tag.

|  |
|----|
| **Important:** Replace `_1`, `_2`, ... with the desired image index (the same index VASP uses for the per-image subdirectories `01`, `02`, ...). The number of usable indices is bounded by [IMAGES](IMAGES.md). |

## Related tags and articles\[<a href="/wiki/index.php?title=IMAGE_1&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMAGES](IMAGES.md),
[NCORE_IN_IMAGE1](NCORE_IN_IMAGE1.md),
[IMAGES](IMAGES.md),
[VCAIMAGES](VCAIMAGES.md)

## References\[<a href="/wiki/index.php?title=IMAGE_1&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]



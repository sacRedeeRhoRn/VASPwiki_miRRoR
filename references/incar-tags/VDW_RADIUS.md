<!-- Source: https://vasp.at/wiki/index.php/VDW_RADIUS | revid: 34376 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VDW_RADIUS


VDW_RADIUS = \[real\] 

|  |  |  |
|----|----|----|
| Default: **VDW_RADIUS** | = 50 | if [IVDW](IVDW.md)=1, 2, 3, 4, or 21 |
|  | = 50.20 | if [IVDW](IVDW.md)=11, 12, or 15 |
|  | = 31.75 | if [IVDW](IVDW.md)=13 |

Description: VDW_RADIUS (in Å)
sets the two-body interaction cutoff in van der Waals methods.

------------------------------------------------------------------------

VDW_RADIUS (in Å) allows to
set the two-body interaction cutoff for the
[DFT-D2](../methods/DFT-D2.md), DFT-D3 ([DFT-D3](../methods/DFT-D3.md)
and [simple-DFT-D3](../methods/Simple-DFT-D3.md)
implementations), [DFT-D4](../methods/DFT-D4.md),
[DFT-ulg](../methods/DFT-ulg.md),
[DDsC](../methods/DDsC_dispersion_correction.md),
and Tkatchenko-Scheffler methods.

|  |
|----|
| **Mind:** Available for the [DFT-D4](../methods/DFT-D4.md) and [simple-DFT-D3](../methods/Simple-DFT-D3.md) packages since VASP.6.6.0. |

## Related tags and articles\[<a
href="/wiki/index.php?title=VDW_RADIUS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md),
[VDW_CNRADIUS](VDW_CNRADIUS.md),
[DFT-D2](../methods/DFT-D2.md), [DFT-D3](../methods/DFT-D3.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md),
[DFT-D4](../methods/DFT-D4.md), [DFT-ulg](../methods/DFT-ulg.md),
[DDsC](../methods/DDsC_dispersion_correction.md),
[Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
[Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](../methods/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VDW_RADIUS-_incategory-Examples)

------------------------------------------------------------------------



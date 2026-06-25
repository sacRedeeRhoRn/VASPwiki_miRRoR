<!-- Source: https://vasp.at/wiki/index.php/VDW_S6 | revid: 34373 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VDW_S6


VDW_S6 = \[real\] 

Description: VDW_S6 sets a
parameter in the damping function of van der Waals methods.

------------------------------------------------------------------------

VDW_S6 allows to set the value
of a parameter in the following methods:

- Scaling $s_{6}$ of
  the dipole-dipole dispersion of the [DFT-D2](../methods/DFT-D2.md)
  ([IVDW](IVDW.md)=1), DFT-D3, [DFT-D4](../methods/DFT-D4.md)
  ([IVDW](IVDW.md)=13), [DFT-ulg](../methods/DFT-ulg.md)
  ([IVDW](IVDW.md)=3), and Tkatchenko-Scheffler methods
  ([IVDW](IVDW.md)=2 and 21).
  VDW_S6 can be used for both
  implementations of DFT-D3: [DFT-D3](../methods/DFT-D3.md)
  ([IVDW](IVDW.md)=11 or 12) and
  [simple-DFT-D3](../methods/Simple-DFT-D3.md)
  ([IVDW](IVDW.md)=15).
- Steepness factor $a_0$ in
  [DDsC](../methods/DDsC_dispersion_correction.md)
  ([IVDW](IVDW.md)=4).

|  |
|----|
| **Mind:** The setting of $s_{6}$ with VDW_S6 when [IVDW](IVDW.md)=11 or 12 (VASP implementation of [DFT-D3](../methods/DFT-D3.md)) is possible since VASP.6.6.0. |

## Related tags and articles\[<a href="/wiki/index.php?title=VDW_S6&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md), [VDW_S8](VDW_S8.md),
[DFT-D2](../methods/DFT-D2.md), [DFT-D3](../methods/DFT-D3.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md),
[DFT-D4](../methods/DFT-D4.md), [DFT-ulg](../methods/DFT-ulg.md),
[Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
[Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](../methods/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
[DDsC](../methods/DDsC_dispersion_correction.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VDW_S6-_incategory-Examples)

------------------------------------------------------------------------



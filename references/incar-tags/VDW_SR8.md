<!-- Source: https://vasp.at/wiki/index.php/VDW_SR8 | revid: 34368 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VDW_SR8
VDW_SR8 = \[real\] 

Description: VDW_SR8 sets the radii scaling $s_{r,8}$ in the dipole-quadrupole zero-damping function of
the DFT-D3 method.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

VDW_SR8 allows to set the radii scaling $s_{r,8}$ in the dipole-quadrupole zero-damping function of the DFT-D3
method. VDW_SR8 can be used for both implementations of DFT-D3:
[DFT-D3](../methods/DFT-D3.md) ([IVDW](IVDW.md)=11) and
[simple-DFT-D3](../methods/Simple-DFT-D3.md)
([IVDW](IVDW.md)=15 with
[SDFTD3_DAMPING](SDFTD3_DAMPING.md)=zero or mzero).

## Related tags and articles
[IVDW](IVDW.md), [VDW_SR](VDW_SR.md),
[DFT-D3](../methods/DFT-D3.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VDW_SR8-_incategory-Examples)

------------------------------------------------------------------------

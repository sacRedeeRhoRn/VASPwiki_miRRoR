<!-- Source: https://vasp.at/wiki/index.php/DFTD4_XC | revid: 34410 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DFTD4_XC


DFTD4_XC = \[string\]  
Default: **DFTD4_XC** = The functional set by the
[GGA](GGA.md), [METAGGA](METAGGA.md) or
[XC](XC.md) tag. 

Description: DFTD4_XC sets the
exchange-correlation functional which determines the van der Waals
parameters used in the DFT-D4 method implemented in the
[DFT-D4](../methods/DFT-D4.md) package.

------------------------------------------------------------------------

DFTD4_XC allows to choose the
exchange-correlation functional that determines which set of van der
Waals parameters is used in the DFT-D4 method implemented in the
[DFT-D4](../methods/DFT-D4.md) package ([IVDW](IVDW.md)=13).

The possible choices (e.g.,
DFTD4_XC=pbe, hse06, ...) are
listed in the file param.f90 of the [DFT-D4](../methods/DFT-D4.md)
source code.

|  |
|----|
| **Mind:** The DFTD4_XC tag is available from VASP.6.6.0 onwards |

## Related tags and articles\[<a href="/wiki/index.php?title=DFTD4_XC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md), [GGA](GGA.md),
[METAGGA](METAGGA.md), [XC](XC.md),
[SDFTD3_XC](SDFTD3_XC.md),
[DFT-D4](../methods/DFT-D4.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-DFTD4_XC-_incategory-Examples)

------------------------------------------------------------------------



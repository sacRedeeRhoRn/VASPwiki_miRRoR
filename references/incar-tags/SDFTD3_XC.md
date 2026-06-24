<!-- Source: https://vasp.at/wiki/index.php/SDFTD3_XC | revid: 34411 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SDFTD3_XC
SDFTD3_XC = \[string\]  
Default: **SDFTD3_XC** = The functional set by the
[GGA](GGA.md), [METAGGA](METAGGA.md) or
[XC](XC.md) tag. 

Description: SDFTD3_XC sets the exchange-correlation functional which
determines the van der Waals parameters used in the DFT-D3 method
implemented in the [simple-DFT-D3](../methods/Simple-DFT-D3.md)
package.

------------------------------------------------------------------------

SDFTD3_XC allows to choose the exchange-correlation functional that
determines which set of van der Waals parameters is used in the DFT-D3
method implemented in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package
([IVDW](IVDW.md)=15).

The possible choices (e.g., SDFTD3_XC=pbe, hse06, ...) depend on the
damping function selected with the
[SDFTD3_DAMPING](SDFTD3_DAMPING.md) tag and are
listed in the file param.f90 of the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) source code.

[TABLE]

## Related tags and articles
[IVDW](IVDW.md),
[SDFTD3_DAMPING](SDFTD3_DAMPING.md),
[GGA](GGA.md), [METAGGA](METAGGA.md),
[XC](XC.md), [DFTD4_XC](DFTD4_XC.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SDFTD3_XC-_incategory-Examples)

------------------------------------------------------------------------

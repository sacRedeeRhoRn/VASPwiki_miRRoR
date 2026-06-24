<!-- Source: https://vasp.at/wiki/index.php/NPACO | revid: 16356 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NPACO
NPACO = \[integer\]  
Default: **NPACO** = 256 

Description: NPACO sets the number of slots in the pair-correlation
function written to [PCDAT](../output-files/PCDAT.md).

------------------------------------------------------------------------

VASP evaluates the pair-correlation function each
[NBLOCK](NBLOCK.md) steps and writes the PC-function after
[NBLOCK](NBLOCK.md)×[KBLOCK](KBLOCK.md) steps to
the [PCDAT](../output-files/PCDAT.md) file.

## Related tags and articles
[APACO](APACO.md), [NBLOCK](NBLOCK.md),
[KBLOCK](KBLOCK.md), [PCDAT](../output-files/PCDAT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NPACO-_incategory-Examples)

------------------------------------------------------------------------

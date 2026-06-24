<!-- Source: https://vasp.at/wiki/index.php/LWAVEH5 | revid: 37115 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWAVEH5
LWAVEH5 = \[logical\]  
Default: **LWAVEH5** = [LH5](LH5.md) 

Description: Determines whether the wavefunctions are written to
[vaspwave.h5](../output-files/Vaspwave.h5.md) file at the end of a run.

------------------------------------------------------------------------

If `LWAVEH5`` = True`, the Kohn-Sham orbitals, i.e., wavefunctions, are
written to the [vaspwave.h5](../output-files/Vaspwave.h5.md) file at
the end of the calculation. This can be used to restart VASP.

|  |
|----|
| **Deprecated:** LWAVEH5 is deprecated as of VASP 6.4.3 and is not read/used by the code. It was introduced in VASP 6.1.0. |

## Related tags and articles
[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[LCHARG](LCHARG.md), [LCHARGH5](LCHARGH5.md),
[LWAVE](LWAVE.md), [LH5](LH5.md)

  
[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWAVEH5-_incategory-Examples)

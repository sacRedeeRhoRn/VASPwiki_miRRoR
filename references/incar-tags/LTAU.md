<!-- Source: https://vasp.at/wiki/index.php/LTAU | revid: 37116 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LTAU
LTAU = .True. \| .False. 

|  |  |  |
|----|----|----|
| Default: **LTAU** | = .False. |  |
|  | = .True. | if the [XC functional](../redirects/XC_functional.md) depends on the kinetic energy density (see [metaGGAs](METAGGA.md)). |

Description: Request evaluation of the kinetic energy density.

------------------------------------------------------------------------

By default only [metaGGAs](METAGGA.md) that depend on the
kinetic energy density compute it. However, setting `LTAU`` = T` in the
[INCAR](../input-files/INCAR.md) file alows to write the kinetic energy
density to file even in case the [XC
functional](../redirects/XC_functional.md) is independent of the
kinetic energy density. [LCHARG](LCHARG.md) controls whether
the charge density and the kinetic energy density are written.

## Related tags and articles
[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[LCHARG](LCHARG.md), [LH5](LH5.md),
[LCHARGH5](LCHARGH5.md), [TAUCAR](../input-files/TAUCAR.md),
[vaspwave.h5](../output-files/Vaspwave.h5.md)

  
[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LCHARG-_incategory-Howto)

<!-- Source: https://vasp.at/wiki/index.php/NMRCURBX | revid: 35871 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NMRCURBX
|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

The NMRCURBX file contains the NMR current density in atomic units
(hartree bohr$^2$). It is written if
[WRT_NMRCUR](../incar-tags/WRT_NMRCUR.md) is set. The format is the
same as [CHGCAR](../input-files/CHGCAR.md) with a header to define the grid
and then 3 blocks that correspond to $j_x$, $j_y$, and
$j_z$.

## Related tags and articles
[WRT_NMRCUR](../incar-tags/WRT_NMRCUR.md),
[LCHIMAG](../incar-tags/LCHIMAG.md), [LLRAUG](../incar-tags/LLRAUG.md)

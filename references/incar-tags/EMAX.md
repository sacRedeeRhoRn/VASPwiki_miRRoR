<!-- Source: https://vasp.at/wiki/index.php/EMAX | revid: 26949 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EMAX
EMAX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **EMAX** | = highest KS eigenvalue + $\Delta$ |  |

Description: EMAX specifies the upper boundary of the energy range for
the evaluation of the electronic [density of
states](../redirects/Density_of_states.md) (DOS).

------------------------------------------------------------------------

The DOS is evaluated each [NBLOCK](NBLOCK.md) steps,
[DOSCAR](../output-files/DOSCAR.md) is updated each
[NBLOCK](NBLOCK.md)\*[KBLOCK](KBLOCK.md) steps.

## Related tags and articles
[EMIN](EMIN.md), [NEDOS](NEDOS.md),
[DOSCAR](../output-files/DOSCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EMAX-_incategory-Examples)

<!-- Source: https://vasp.at/wiki/index.php/EMIN | revid: 26951 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EMIN
EMIN = \[real\] 

|  |  |  |
|----|----|----|
| Default: **EMIN** | = lowest KS eigenvalue - $\Delta$ |  |

Description: EMIN specifies the lower boundary of the energy range for
the evaluation of the electronic [density of
states](../redirects/Density_of_states.md) (DOS).

------------------------------------------------------------------------

The DOS is evaluated each [NBLOCK](NBLOCK.md) steps,
[DOSCAR](../output-files/DOSCAR.md) is updated each
[NBLOCK](NBLOCK.md)\*[KBLOCK](KBLOCK.md) steps.

|  |
|----|
| **Tip:** Set EMIN to a value larger than [EMAX](EMAX.md), if you are not sure where the region of interest lies. |

## Related tags and articles
[EMAX](EMAX.md), [NEDOS](NEDOS.md),
[DOSCAR](../output-files/DOSCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EMIN-_incategory-Examples)

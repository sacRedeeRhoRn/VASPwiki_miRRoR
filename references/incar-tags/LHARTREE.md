<!-- Source: https://vasp.at/wiki/index.php/LHARTREE | revid: 33015 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LHARTREE
LHARTREE = \[logical\]  
Default: **LHARTREE** = .TRUE. 

Description: Controls whether the bubble diagrams are included in the
[BSE](../redirects/BSE.md) calculation.

------------------------------------------------------------------------

[LADDER](LADDER.md) is used together with LHARTREE. If
[LADDER](LADDER.md)=*.FALSE.*, the ladder diagrams, i.e.,
the exchange terms related to $W$ or the
screened exchange, are not included. If LHARTREE=*.FALSE.*, the Hartree
diagrams or bubble diagrams are not included. The following table
summarizes all possible combinations:

|  |  |  |
|----|----|----|
| LHARTREE | [LADDER](LADDER.md) |  |
| .TRUE. | .TRUE. | full BSE / TDHF |
| .FALSE. | .TRUE. | only excitonic effects (ladders) |
| .TRUE. | .FALSE. | random phase approximation (rings = bubbles only) |
| .FALSE. | .FALSE. | independent particle picture |

The last combination can be useful for sanity checks: the results must
be identical to the results obtained using
[LOPTICS](LOPTICS.md)=*.TRUE.* in the preceding
calculations. If this is not the case, it usually implies that the
one-electron energies have been updated in the
[WAVECAR](../input-files/WAVECAR.md) file, or that the
[WAVEDER](../input-files/WAVEDER.md) file is not properly set up. The end
of [BSE](../redirects/BSE_calculations.md) explains how to
recalculate the [WAVEDER](../input-files/WAVEDER.md) file from an existing
[WAVECAR](../input-files/WAVECAR.md) file.

## Related tags and articles
[LADDER](LADDER.md), [LOPTICS](LOPTICS.md),
[BSE calculations](../redirects/BSE_calculations.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LHARTREE-_incategory-Howto)

------------------------------------------------------------------------

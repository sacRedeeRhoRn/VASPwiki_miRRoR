<!-- Source: https://vasp.at/wiki/index.php/LADDER | revid: 33016 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LADDER


LADDER = \[logical\]  
Default: **LADDER** = .NOT. [LRPA](LRPA.md) 

Description: Controls whether the ladder diagrams are included in the
<a href="/wiki/BSE" class="mw-redirect" title="BSE">BSE</a> calculation.
Note that the default for [LRPA](LRPA.md) and therefore LADDER
is somewhat convoluted; so better to always double-check the
[OUTCAR](../output-files/OUTCAR.md) file whether VASP behaves as expected.
Generally, VASP will select ladder diagrams whenever this seems
reasonable. This is for instance the case for
[ALGO](ALGO.md)="BSE" or "TDHF" calculations.

------------------------------------------------------------------------

LADDER is used together with
[LHARTREE](LHARTREE.md). If
LADDER=*.FALSE.*, the ladder
diagrams (i.e. the exchange terms related to $W$ or the
screened exchange) are not included. If
[LHARTREE](LHARTREE.md)=*.FALSE.*, the Hartree diagrams or
bubble diagrams are not included. The following table summarizes all
possible combinations:

|  |  |  |
|----|----|----|
| [LHARTREE](LHARTREE.md) | LADDER |  |
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
of <a href="/wiki/BSE" class="mw-redirect" title="BSE">BSE</a> explains
how to recalculate the [WAVEDER](../input-files/WAVEDER.md) file from an
existing [WAVECAR](../input-files/WAVECAR.md) file.

## Related tags and articles\[<a href="/wiki/index.php?title=LADDER&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LHARTREE](LHARTREE.md),
[LOPTICS](LOPTICS.md),

<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LADDER-_incategory-Howto)

------------------------------------------------------------------------



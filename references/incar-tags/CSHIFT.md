<!-- Source: https://vasp.at/wiki/index.php/CSHIFT | revid: 26978 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CSHIFT


CSHIFT = \[real\] 

|  |  |  |
|----|----|----|
| Default: **CSHIFT** | = 0.1 | for [LOPTICS](LOPTICS.md) |
|  | = [OMEGAMAX](OMEGAMAX.md)\*1.3 / max([NOMEGA](NOMEGA.md),40) | for <a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a> |
|  | = 0.1 | for <a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>/[Casida TDDFT calculations](../methods/Time-dependent_density-functional_theory_calculations.md) |
|  | = 0.1 | for <a href="/wiki/Time_Evolution" class="mw-redirect"
title="Time Evolution">Time Evolution TDDFT calculations</a> |

Description: CSHIFT sets a
Lorentzian broadening in eV of the dielectric tensor via the complex
shift η in the [Kramers-Kronig
transformation](LOPTICS.md) of the response
function.

------------------------------------------------------------------------

The default CSHIFT=0.1 is
perfectly acceptable for most calculations and causes a slight smoothing
of the real part of the dielectric function. If the gap is very small
(i.e. approaching two times
CSHIFT), slight inaccuracies
in the static dielectric constant are possible, which can be remedied by
decreasing CSHIFT. If
CSHIFT is further decreased,
it is strongly recommended to increase the frequency grid by setting
[NEDOS](NEDOS.md) to values around 2000.

|  |
|----|
| **Mind:** For the quartic-scaling GW algorithm, one should manually check that CSHIFT is at least as large as the grid spacing at low frequencies. If CSHIFT is smaller than the grid spacing, the QP energies might show erratic behavior (for instance large re-normalization factors Z). |

## Related tags and articles\[<a href="/wiki/index.php?title=CSHIFT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[OMEGAMIN](OMEGAMIN.md),
[OMEGAMAX](OMEGAMAX.md),
[LOPTICS](LOPTICS.md), [Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CSHIFT-_incategory-Examples)

------------------------------------------------------------------------



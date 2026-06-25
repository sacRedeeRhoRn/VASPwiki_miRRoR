<!-- Source: https://vasp.at/wiki/index.php/NSTORB | revid: 35870 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NSTORB


NSTORB = \[integer\] 

|                     |      |     |
|---------------------|------|-----|
| Default: **NSTORB** | = -1 |     |

Description: NSTORB specifies
the number of stochastic orbitals per cycle in the stochastic MP2
algorithm.

------------------------------------------------------------------------

NSTORB
defines the number of stochastic orbitals per cycle, i.e., the number of
stochastic orbitals that define one stochastic sample. If the sample is
not large enough, the calculations are repeated until the accuracy,
defined by ESTOP, is reached.

As a rule of thumb, we recommend setting

$\texttt{NSTORB} = \sqrt{\texttt{NBANDS}} \\.$

See [here](../theory/Stochastic_LTMP2.md) for a small
tutorial on stochastic Laplace transformed MP2 calculations.

## Related tags and articles\[<a href="/wiki/index.php?title=NSTORB&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NOMEGA](NOMEGA.md), [ESTOP](ESTOP.md),
[LSMP2LT](LSMP2LT.md), [LMP2LT](LMP2LT.md),
[NBANDS](NBANDS.md), [KPAR](KPAR.md),
[ALGO](ALGO.md)

------------------------------------------------------------------------



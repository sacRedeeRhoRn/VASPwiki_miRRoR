<!-- Source: https://vasp.at/wiki/index.php/LSMP2LT | revid: 24263 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSMP2LT


LSMP2LT = .FALSE. \| .TRUE. 

|                      |           |     |
|----------------------|-----------|-----|
| Default: **LSMP2LT** | = .FALSE. |     |

Description: LSMP2LT selects a
stochastic Laplace transformed MP2 algorithm.

------------------------------------------------------------------------

If LSMP2LT=.TRUE. and
[ALGO](ALGO.md)=ACFTDRK is set, a quartic scaling stochastic
Laplace transformed MP2 algorithm is
selected.[^schaefer:JCP2017-1]

This tag should be used in combination with [KPAR](KPAR.md) to
tweak parallelization as described in this
[tutorial](../theory/Stochastic_LTMP2.md).

## Related tags and articles\[<a href="/wiki/index.php?title=LSMP2LT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NOMEGA](NOMEGA.md), [ESTOP](ESTOP.md),
[NSTORB](NSTORB.md), [KPAR](KPAR.md),
[ALGO](ALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMP2LT-_incategory-Examples)

------------------------------------------------------------------------

[^schaefer:JCP2017-1]: [T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys. **146**, 104101 (2017).](https://doi.org/10.1063/1.4976937)

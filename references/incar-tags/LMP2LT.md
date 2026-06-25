<!-- Source: https://vasp.at/wiki/index.php/LMP2LT | revid: 24259 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMP2LT


LMP2LT = .FALSE. \| .TRUE. 

|                     |           |     |
|---------------------|-----------|-----|
| Default: **LMP2LT** | = .FALSE. |     |

Description: LMP2LT selects a
Laplace transformed MP2 algorithm.

------------------------------------------------------------------------

If LMP2LT=.TRUE. and
[ALGO](ALGO.md)=ACFTDRK is set, a quartic scaling Laplace
transformed MP2 algorithm is
selected.<sup>[\[1\]](#cite_note-schaefer:JCP2017-1)</sup>

This tag should be used in combination with [KPAR](KPAR.md) to
tweak parallelization as described in this
[tutorial](../tutorials/LTMP2_-_Tutorial.md).

## Related tags and articles\[<a href="/wiki/index.php?title=LMP2LT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NOMEGA](NOMEGA.md), [ALGO](ALGO.md),
[LSMP2LT](LSMP2LT.md), [KPAR](KPAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMP2LT-_incategory-Examples)

------------------------------------------------------------------------


1.  [↑](#cite_ref-schaefer:JCP2017_1-0)
    <a href="https://doi.org/10.1063/1.4976937" class="external text"
    rel="nofollow">T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys.
    <strong>146</strong>, 104101 (2017).</a>



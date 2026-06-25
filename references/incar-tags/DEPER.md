<!-- Source: https://vasp.at/wiki/index.php/DEPER | revid: 26938 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DEPER


DEPER = \[real\]  
Default: **DEPER** = 0.3 

Description: DEPER specifies a
relative stopping criterion for the optimization of an eigenvalue.

------------------------------------------------------------------------

The tags DEPER,
[WEIMIN](WEIMIN.md), and [EBREAK](EBREAK.md)
allow fine tuning of the iterative matrix diagonalization, and are best
not changed. They are optimized for a large variety of systems, and
changing one of the parameters usually decreases performance or can even
screw up the iterative matrix diagonalization totally. In general, these
tags control when the optimization of a single band is stopped within
the iterative matrix diagonalization schemes:

DEPER specifies a relative
break-criterion: the optimization of a band is stopped after the energy
change becomes smaller than
DEPER multiplied with the
energy change in the first iterative optimization step. The maximum
number of optimization steps is always 4.

## Related tags and articles\[<a href="/wiki/index.php?title=DEPER&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[WEIMIN](WEIMIN.md), [EBREAK](EBREAK.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-DEPER-_incategory-Examples)



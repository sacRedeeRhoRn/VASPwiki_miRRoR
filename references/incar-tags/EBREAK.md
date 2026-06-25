<!-- Source: https://vasp.at/wiki/index.php/EBREAK | revid: 16726 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EBREAK


EBREAK = \[real\]  
Default: **EBREAK** =
[EDIFF](EDIFF.md)/[NBANDS](NBANDS.md)/4 

Description: EBREAK specifies
an absolute stopping criterion for the optimization of an eigenvalue.

------------------------------------------------------------------------

The tags EBREAK,
[DEPER](DEPER.md), and [WEIMIN](WEIMIN.md) allow
fine tuning of the iterative matrix diagonalization, and are best not
changed. They are optimized for a large variety of systems, and changing
one of the parameters usually decreases performance or can even screw up
the iterative matrix diagonalization totally. In general, these tags
control when the optimization of a single band is stopped within the
iterative matrix diagonalization schemes:

EBREAK determines whether a
band is fully converged or not. Optimization of an
eigenvalue/eigenvectors pair is stopped if the change in the eigenenergy
is smaller than EBREAK.

## Related tags and articles\[<a href="/wiki/index.php?title=EBREAK&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[WEIMIN](WEIMIN.md), [DEPER](DEPER.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EBREAK-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/WEIMIN | revid: 27056 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WEIMIN


WEIMIN = \[real\] 

|                     |         |                                        |
|---------------------|---------|----------------------------------------|
| Default: **WEIMIN** | = 0.001 | for [IBRION](IBRION.md)≥0  |
|                     | = 0     | for [IBRION](IBRION.md)=−1 |

Description: WEIMIN specifies
the maximum weight for a band to be considered empty.

------------------------------------------------------------------------

The tags WEIMIN,
[EBREAK](EBREAK.md), and [DEPER](DEPER.md) allow
fine-tuning of the iterative matrix diagonalization and are best not
changed. They are optimized for a large variety of systems, and changing
one of the parameters usually decreases performance or can even screw up
the iterative matrix diagonalization totally. In general, these tags
control when the optimization of a single band is stopped within the
iterative matrix diagonalization schemes:

Within all implemented iterative schemes a distinction between empty and
occupied bands is made to speed up calculations. Unoccupied bands are
optimized only twice, whereas occupied bands are optimized up to four
times till another break criterion is met. Eigenvalue/eigenvector pairs
for which the partial occupancies are smaller than
WEIMIN are treated as
unoccupied states (and are thus only optimized twice).

## Related tags and articles\[<a href="/wiki/index.php?title=WEIMIN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[EBREAK](EBREAK.md), [DEPER](DEPER.md),
[IBRION](IBRION.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-WEIMIN-_incategory-Examples)



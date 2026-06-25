<!-- Source: https://vasp.at/wiki/index.php/NBANDSGW | revid: 18031 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBANDSGW


NBANDSGW = \[integer\]  
Default: **NBANDSGW** = twice the number of occupied states 

Description: The flag determines how many QP energies are calculated and
updated in GW type calculations.

------------------------------------------------------------------------

This value usually needs to be increased somewhat for partially or fully
self-consistent calculations. Very accurate results are only obtained
when NBANDSGW approaches
[NBANDS](NBANDS.md), although this dramatically increases
the computational requirements.

## Related tags and articles\[<a href="/wiki/index.php?title=NBANDSGW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NBANDS](NBANDS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NBANDSGW-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/SYMPREC | revid: 27002 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SYMPREC


SYMPREC = \[real\]  
Default: **SYMPREC** = $10^{-5}$ 

Description: SYMPREC
determines to which accuracy the positions in the
[POSCAR](../input-files/POSCAR.md) file must be specified (as of
VASP.4.4.4).

------------------------------------------------------------------------

SYMPREC determines how
accurately the positions in the [POSCAR](../input-files/POSCAR.md) file
must be specified. The default,
SYMPREC=10<sup>-5</sup>, is
usually large enough, even if the [POSCAR](../input-files/POSCAR.md) file
has been generated with single precision accuracy. Increasing
SYMPREC means that the
positions in the [POSCAR](../input-files/POSCAR.md) file can be specified
with less accuracy (increasing fuzziness). Please also have a look at
[this section](../input-files/POSCAR.md).

## Related tags and articles\[<a href="/wiki/index.php?title=SYMPREC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ISYM](ISYM.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SYMPREC-_incategory-Examples)



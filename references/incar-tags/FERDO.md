<!-- Source: https://vasp.at/wiki/index.php/FERDO | revid: 28538 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FERDO


FERDO = \[real array\] 

Description: FERDO sets the
occupancies of the states in the down-spin channel for
[ISMEAR](ISMEAR.md)=-2 and [ISPIN](ISPIN.md)=2.

------------------------------------------------------------------------

To set the occupancies, specify

     FERDO = f(1) f(2) f(3) ... f(NBANDS×Nk)

The occupancies must be specified for all bands and k points. The
band-index runs fastest. The occupancies must be between 0 and 1.
FERDO has the same format as
[FERWE](FERWE.md), please consider the notes on that page
when setting FERDO.

## Related tags and articles\[<a href="/wiki/index.php?title=FERDO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[FERWE](FERWE.md), [ISMEAR](ISMEAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-FERDO-_incategory-Examples)



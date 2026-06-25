<!-- Source: https://vasp.at/wiki/index.php/QMAXFOCKAE | revid: 27006 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# QMAXFOCKAE


QMAXFOCKAE = \[real array\] 

Description: Controls at which wave vectors the local augmentation
charges are fitted to obtain an accurate charge augmentation on the
plane-wave grid.

------------------------------------------------------------------------

We do not recommend setting these tags manually, except after careful
inspection of the VASP code (fast_aug.F). The default values are 6.0
Å<sup>-1</sup> if <a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a>=1 (corresponding to 140 eV), and 5.0
and 10 Å<sup>-1</sup> (corresponding to 95 eV and 380 eV) for
<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a>=2.

## Related tags and articles\[<a
href="/wiki/index.php?title=QMAXFOCKAE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a>,
<a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a>,
[LFOCKAEDFT](LFOCKAEDFT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-QMAXFOCKAE-_incategory-Examples)



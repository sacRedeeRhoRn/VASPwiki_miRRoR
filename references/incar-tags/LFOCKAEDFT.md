<!-- Source: https://vasp.at/wiki/index.php/LFOCKAEDFT | revid: 18007 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LFOCKAEDFT


LFOCKAEDFT = \[logical\]  
Default: **LFOCKAEDFT** = .FALSE. 

Description: LFOCKAEDFT forces
VASP to use the same charge augmentation for the Hartree and DFT
exchange correlation part as is used in the Fock exchange and the many
body beyond DFT methods, such as RPA, MP2 etc.

------------------------------------------------------------------------

This flag should be set only in exceptional cases. The Hartree as well
as the DFT part are usually calculated very accurately using the
one-centre PAW spheres. Restoring the all-electron charge accurately on
the plane wave grid adds potentially noise, but should not change the
results (relative energies, forces etc.). The flag, however, needs to be
set for optimized potential methods, which are supported by VASP but not
documented yet.

## Related tags and articles\[<a
href="/wiki/index.php?title=LFOCKAEDFT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a>,
<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a>,
[QMAXFOCKAE](QMAXFOCKAE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LFOCKAEDFT-_incategory-Examples)

------------------------------------------------------------------------



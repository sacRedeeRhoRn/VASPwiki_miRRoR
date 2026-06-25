<!-- Source: https://vasp.at/wiki/index.php/LWRITE_UNK | revid: 18096 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWRITE_UNK


LWRITE_UNK = .TRUE. \|
.FALSE.  
Default: **LWRITE_UNK** = .FALSE. 

Description: LWRITE_UNK
decides whether the cell-periodic part of the relevant Bloch functions
is written.

------------------------------------------------------------------------

For LWRITE_UNK=True, VASP
writes the cell-periodic part of the Kohn–Sham orbitals in spin channel
s at k point p to the file **wannier90.UNKp.s**. This file can be used
to plot Wannier orbitals with WANNIER90.

For details on the execution of `wannier_setup` in VASP, see the
description of the [LWANNIER90](LWANNIER90.md) tag. For
information on the **wannier90.win** file and the execution of
WANNIER90, we refer to the
<a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>.

## Related tags and articles\[<a
href="/wiki/index.php?title=LWRITE_UNK&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LWANNIER90](LWANNIER90.md),
[LWRITE_MMN_AMN](LWRITE_MMN_AMN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWANNIER90_RUN-_incategory-Examples)

------------------------------------------------------------------------



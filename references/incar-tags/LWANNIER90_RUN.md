<!-- Source: https://vasp.at/wiki/index.php/LWANNIER90_RUN | revid: 35704 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWANNIER90_RUN


LWANNIER90_RUN = .TRUE. \|
.FALSE.  
Default: **LWANNIER90_RUN** = .FALSE. 

Description: LWANNIER90_RUN
executes `wannier_setup` (see
[LWANNIER90](LWANNIER90.md)=.TRUE.) and subsequently
runs <a href="http://www.wannier.org" class="external text"
rel="nofollow">WANNIER90</a> in library mode (`wannier_run`).

------------------------------------------------------------------------

For details on the execution of `wannier_setup` in VASP, see the
description of the [LWANNIER90](LWANNIER90.md)-tag. For
information on the many tags one may set in the <a
href="/wiki/index.php?title=Wannier90.win&amp;action=edit&amp;redlink=1"
class="new"
title="Wannier90.win (page does not exist)">wannier90.win</a> file to
control the execution of WANNIER90 (be it standalone or in library mode)
we refer to the <a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>.

**Mind**: when running WANNIER90 in library mode, the <a
href="/wiki/index.php?title=Wannier90.mmn&amp;action=edit&amp;redlink=1"
class="new"
title="Wannier90.mmn (page does not exist)">wannier90.mmn</a> and <a
href="/wiki/index.php?title=Wannier90.amn&amp;action=edit&amp;redlink=1"
class="new"
title="Wannier90.amn (page does not exist)">wannier90.amn</a> files are
not written. The information these files normally contain is passed on
to `wannier_run` internally. If you want these files to be written
anyway, for instance to be able to run WANNIER90 standalone later on,
one should add

    LWRITE_MMN_AMN=.TRUE.

to the [INCAR](../input-files/INCAR.md) file.

## Related tags and articles\[<a
href="/wiki/index.php?title=LWANNIER90_RUN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LWANNIER90](LWANNIER90.md),
[LWRITE_MMN_AMN](LWRITE_MMN_AMN.md),
[LWRITE_UNK](LWRITE_UNK.md),
[NUM_WANN](NUM_WANN.md),
[LWRITE_SPN](LWRITE_SPN.md),
[WANNIER90_WIN](WANNIER90_WIN.md),
[LWRITE_WANPROJ](LWRITE_WANPROJ.md),
[WANPROJ](../input-files/WANPROJ.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWANNIER90_RUN-_incategory-Examples)

------------------------------------------------------------------------



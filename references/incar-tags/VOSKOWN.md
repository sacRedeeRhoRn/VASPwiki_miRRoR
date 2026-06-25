<!-- Source: https://vasp.at/wiki/index.php/VOSKOWN | revid: 17005 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VOSKOWN


VOSKOWN = 0 \| 1  
Default: **VOSKOWN** = 0 

Description: Determines whether Vosko-Wilk-Nusair interpolation is used
or not.

------------------------------------------------------------------------

This flag is not relevant for most "modern" gradient corrected
functionals, such as PBE or PBEsol.

For the LDA and some "older" gradient corrected functionals such as
PW91, VASP interpolates the correlation energy from the
non-spinpolarized to the fully spinpolarized case in the same way as the
exchange energy (Barth-Hedin spin
interpolation<sup>[\[1\]](#cite_note-barth:jpc:1972-1)</sup>.
If VOSKOWN is set to 1, the
interpolation formula according to Vosko, Wilk and
Nusair<sup>[\[2\]](#cite_note-vosko1980-2)</sup>
is used (this interpolation is based on the RPA correlation energy of
partially spin polarized systems). The Vosko, Wilk and Nusair
interpolation usually enhances the magnetic moments and the magnetic
energies. Because the Vosko-Wilk-Nusair interpolation is the
interpolation usually applied in the context of gradient corrected
functionals, it is desirable to use this interpolation whenever the PW91
functional is applied. Setting this tag is not required for most modern
functions, such as the PBE or PBEsol functional, since these functional
strictly follow the original publications and disregard the setting of
this flag entirely (this implicitly implies that the correlation energy
is interpolated according to Vosko, Wilk and Nusair).

## References\[<a href="/wiki/index.php?title=VOSKOWN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-barth:jpc:1972_1-0)
    <a href="https://doi.org/10.1088/0022-3719/5/13/012"
    class="external text" rel="nofollow">U. V. Barth and L. Hedin, J. Phys.
    C <strong>5</strong>, 1629 (1972).</a>
2.  [↑](#cite_ref-vosko1980_2-0)
    <a href="https://doi.org/10.1139/p80-159" class="external text"
    rel="nofollow">S. H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys.
    <strong>58</strong>, 1200 (1980).</a>


[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VOSKOWN-_incategory-Examples)

------------------------------------------------------------------------



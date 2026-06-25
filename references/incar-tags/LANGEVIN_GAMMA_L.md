<!-- Source: https://vasp.at/wiki/index.php/LANGEVIN_GAMMA_L | revid: 36572 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LANGEVIN_GAMMA_L


LANGEVIN_GAMMA_L = \[Real\]  
Default: **LANGEVIN_GAMMA_L** = 0 

Description: LANGEVIN_GAMMA_L
specifies the friction coefficient (in ps<sup>-1</sup>) for lattice
degrees-of-freedom in case of Parrinello-Rahman dynamics (in case VASP
was compiled with <a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">-Dtbdyn</a>).

------------------------------------------------------------------------

When running *NpT* simulations with a [Langevin
thermostat](MDALGO.md)<sup>[\[1\]](#cite_note-allen:book:1991-1)</sup>
([MDALGO](MDALGO.md)=3), using the method of [Parrinello and
Rahman](MDALGO.md)<sup>[\[2\]](#cite_note-parrinello:prl:1980-2)[\[3\]](#cite_note-parrinello:jap:1981-3)</sup>,
the friction coefficient for lattice degrees-of-freedom have to be
specified (in ps<sup>-1</sup>) by means of the
LANGEVIN_GAMMA_L-tag. A
fictitious mass for the lattice degrees-of-freedom has to be assigned
using the [PMASS](PMASS.md) tag.

The friction coefficients γ for the atomic degrees-of-freedom are
specified using the
[LANGEVIN_GAMMA](LANGEVIN_GAMMA.md)-tag.

## Related tags and articles\[<a
href="/wiki/index.php?title=LANGEVIN_GAMMA_L&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LANGEVIN_GAMMA](LANGEVIN_GAMMA.md),
[PMASS](PMASS.md), [MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LANGEVIN_GAMMA_L-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LANGEVIN_GAMMA_L&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------


1.  [↑](#cite_ref-allen:book:1991_1-0)
    <a
    href="https://books.google.co.jp/books?id=WFExDwAAQBAJ&amp;lpg=PP1&amp;hl=ja&amp;pg=PP1#v=onepage&amp;q&amp;f=false"
    class="external text" rel="nofollow">M. P. Allen and D. J. Tildesley,
    <em>Computer simulation of liquids</em> (Oxford university press: New
    York, 1991).</a>
2.  [↑](#cite_ref-parrinello:prl:1980_2-0)
    <a href="https://doi.org/10.1103/PhysRevLett.45.1196"
    class="external text" rel="nofollow">M. Parrinello and A. Rahman, Phys.
    Rev. Lett. <strong>45</strong>, 1196 (1980).</a>
3.  [↑](#cite_ref-parrinello:jap:1981_3-0)
    <a href="https://doi.org/10.1063/1.328693" class="external text"
    rel="nofollow">M. Parrinello and A. Rahman, J. Appl. Phys.
    <strong>52</strong>, 7182 (1981).</a>



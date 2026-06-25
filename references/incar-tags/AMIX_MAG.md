<!-- Source: https://vasp.at/wiki/index.php/AMIX_MAG | revid: 27042 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AMIX_MAG


AMIX_MAG = \[real\]  
Default: **AMIX_MAG** = 1.6 

Description: Linear mixing parameter for the magnetization density.

------------------------------------------------------------------------

The default mixing parameters for spinpolarized calculations are:

[IMIX](IMIX.md)=4, [AMIX](AMIX.md)=0.4,
[AMIN](AMIN.md)=min(0.1,[AMIX](AMIX.md),AMIX_MAG),
[BMIX](BMIX.md)=1.0,
AMIX_MAG=1.6, and
[BMIX_MAG](BMIX_MAG.md)=1.0.

These settings are consistent with an (initial) spin enhancement factor
of 4, which is usually a reasonable approximation.

There are only a few other parameter combinations that can be tried if
convergence turns out to be very slow. In particular, for slabs,
magnetic systems, and insulating systems (e.g. molecules and clusters),
an initial "linear mixing" can result in faster convergence than the
Kerker model
function.<sup>[\[1\]](#cite_note-kerker:prb:1981-1)</sup>
One can therefore try to use the following setting

    AMIX     = 0.2
    BMIX     = 0.0001 ! almost zero, but 0 will crash some versions
    AMIX_MAG = 0.8
    BMIX_MAG = 0.0001 ! almost zero, but 0 will crash some versions

|  |
|----|
| **Mind:** For spin-polarized calculations the defaults for the mixing parameters [AMIX](AMIX.md) and [BMIX](BMIX.md) are different than for the non-spin-polarized case. |

## Related tags and articles\[<a href="/wiki/index.php?title=AMIX_MAG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [AMIX](AMIX.md),
[BMIX](BMIX.md), [BMIX_MAG](BMIX_MAG.md),
[AMIN](AMIN.md), [MIXPRE](MIXPRE.md),
[WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AMIX_MAG-_incategory-Examples)


1.  [↑](#cite_ref-kerker:prb:1981_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.23.3082" class="external text"
    rel="nofollow">G. P. Kerker, <em>Efficient iteration scheme for
    self-consistent pseudopotential calculations</em>, Phys. Rev. B
    <strong>23</strong>, 3082 (1981).</a>



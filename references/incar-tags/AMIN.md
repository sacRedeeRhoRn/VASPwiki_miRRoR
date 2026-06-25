<!-- Source: https://vasp.at/wiki/index.php/AMIN | revid: 27037 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AMIN


AMIN = \[real\]  
Default: **AMIN** =
min(0.1,[AMIX](AMIX.md),[AMIX_MAG](AMIX_MAG.md)) 

Description: AMIN specifies
the minimal mixing parameter in Kerker's initial
approximation<sup>[\[1\]](#cite_note-kerker:prb:1981-1)</sup>
to the charge-dielectric function used in the
Broyden<sup>[\[2\]](#cite_note-bluegel:phd:1988-2)[\[3\]](#cite_note-johnson:prb:1988-3)</sup>/Pulay<sup>[\[4\]](#cite_note-pulay:cpl:1980-4)</sup>
mixing scheme ([IMIX](IMIX.md)=4,
[INIMIX](INIMIX.md)=1).

------------------------------------------------------------------------

Kerker's initial
approximation<sup>[\[1\]](#cite_note-kerker:prb:1981-1)</sup>
for the charge-dielectric function is given by

$\max\left(\frac{AG^2}{G^2+B^2},A_{\rm min}\right),$

where $A$=[AMIX](AMIX.md), $B$=[BMIX](BMIX.md), and
$A_{\rm min}$=AMIN.

## Related tags and articles\[<a href="/wiki/index.php?title=AMIN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [AMIX](AMIX.md),
[BMIX](BMIX.md), [AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [MIXPRE](MIXPRE.md),
[WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AMIN-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=AMIN&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-kerker:prb:1981_1-0)</sup>
    <sup>[b](#cite_ref-kerker:prb:1981_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.23.3082" class="external text"
    rel="nofollow">G. P. Kerker, <em>Efficient iteration scheme for
    self-consistent pseudopotential calculations</em>, Phys. Rev. B
    <strong>23</strong>, 3082 (1981).</a>
2.  [↑](#cite_ref-bluegel:phd:1988_2-0)
    <a href="http://hdl.handle.net/2128/18476" class="external text"
    rel="nofollow">S. Blügel, PhD Thesis, RWTH Aachen (1988).</a>
3.  [↑](#cite_ref-johnson:prb:1988_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.38.12807"
    class="external text" rel="nofollow">D. D. Johnson, Phys. Rev. B
    <strong>38</strong>, 12807 (1988)</a>
4.  [↑](#cite_ref-pulay:cpl:1980_4-0)
    <a href="https://doi.org/10.1016/0009-2614(80)80396-4"
    class="external text" rel="nofollow">P. Pulay, Chem. Phys. Lett.
    <strong>73</strong>, 393 (1980).</a>



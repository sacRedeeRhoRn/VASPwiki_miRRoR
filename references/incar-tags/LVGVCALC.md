<!-- Source: https://vasp.at/wiki/index.php/LVGVCALC | revid: 29604 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LVGVCALC


LVGVCALC = .TRUE. \| .FALSE.  
Default: **LVGVCALC** = .TRUE. 

Description: LVGVCALC switches
on calculation of the *vGv* expression for the orbital magnetic
susceptibility.

LVGVCALC is available as of
VASP.6.4.0.

------------------------------------------------------------------------

When performing a chemical shift calculation the standard *pGv*
susceptibility is calculated and used in the calculation of the CSA
tensor
<sup>[\[1\]](#cite_note-yates:prb:2007-1)</sup>.
When LVGVCALC is true, the
magnetic susceptibility is also calculated with the *vGv* approximation.
[LVGVAPPL](LVGVAPPL.md) determines whether the *vGv* or
*pGv* result is applied in the calculation of the
$\mathbf{G=0}$ contribution to the CSA tensor.

The *vGv* expression for the orbital susceptibility was introduced by
d'Avezac *et al.*
<sup>[\[2\]](#cite_note-avezac:prb:2007-2)</sup>.
In VASP its ultra-soft generalization is used
<sup>[\[3\]](#cite_note-dewijs:havenith:jcp:2021-3)</sup>.

## Related tags and articles\[<a href="/wiki/index.php?title=LVGVCALC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md),
[LVGVAPPL](LVGVAPPL.md)

## References\[<a href="/wiki/index.php?title=LVGVCALC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-yates:prb:2007_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.76.024401"
    class="external text" rel="nofollow">J. R. Yates, C. J. Pickard, and F.
    Mauri, <em>Calculation of NMR chemical shifts for extended systems using
    ultrasoft pseudopotentials</em>, Phys. Rev. B <strong>76</strong>,
    024401 (2007).</a>
2.  [↑](#cite_ref-avezac:prb:2007_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.76.165122"
    class="external text" rel="nofollow">M. d'Avezac, N. Marzari, and F.
    Mauri, <em>Spin and orbital magnetic response in metals: Susceptibility
    and NMR shifts</em>, Phys. Rev. B <strong>76</strong>, 165122
    (2007).</a>
3.  [↑](#cite_ref-dewijs:havenith:jcp:2021_3-0)
    <a href="https://doi.org/10.1063/5.0069637" class="external text"
    rel="nofollow">G.A. de Wijs, G. Kresse, R. W. A. Havenith, and M.
    Marsman, <em>Spin and orbital magnetic response in metals:
    Susceptibility and NMR shifts</em>, J. Chem. Phys. <strong>155</strong>,
    234101 (2021).</a>



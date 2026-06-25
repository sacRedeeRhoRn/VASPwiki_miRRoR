<!-- Source: https://vasp.at/wiki/index.php/LRHFCALC | revid: 34131 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LRHFCALC


LRHFCALC = .TRUE. \| .FALSE.  
Default: **LRHFCALC** = .FALSE. 

Description: Switch on the decomposition of the exchange for the hybrid
functionals using full Hartree-Fock exchange at long range.

------------------------------------------------------------------------

If LRHFCALC=.TRUE. the
exchange functional is decomposed into short-range LDA, PBE or PBEsol
([GGA](GGA.md)=CA, PE, PS, respectively) and long-range
Hartree-Fock:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{c}}^{\mathrm{SL}}$

The mixing $a_{\mathrm{LR}}$ and screening $\mu$ are
controlled by the [AEXX](AEXX.md) and
[HFSCREEN](HFSCREEN.md) tags, respectively. The RSHXLDA or
RSHXPBE
functionals[^iikura:jcp:2001-1][^gerber:cpl:2005-2][^gerber:jcp:2007-3]
are examples of such functionals and their settings are shown on the
[page listing the hybrid
functionals](../methods/List_of_hybrid_functionals.md).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>If <span class="mw-selflink selflink">LRHFCALC</span>=.TRUE., then
<a href="/wiki/LHFCALC" title="LHFCALC">LHFCALC</a>=.TRUE. is
automatically set.</li>
<li>If <span class="mw-selflink selflink">LRHFCALC</span>=.TRUE., then
<a href="/wiki/AEXX" title="AEXX">AEXX</a>=1 is automatically set, but
<a href="/wiki/AEXX" title="AEXX">AEXX</a> can be set to another
value.</li>
</ul></td>
</tr>
</tbody>
</table>

|  |
|----|
| **Important:** When [AEXX](AEXX.md)=1 (the default for LRHFCALC=.TRUE.), the correlation $E_{\mathrm{c}}^{\mathrm{SL}}$ is not included. However, it can be included by setting [ALDAC](ALDAC.md)=1.0 and [AGGAC](AGGAC.md)=1.0. |

## Related tags and articles\[<a href="/wiki/index.php?title=LRHFCALC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LHFCALC](LHFCALC.md),
[HFSCREEN](HFSCREEN.md), [AEXX](AEXX.md),
[LMODELHF](LMODELHF.md),
[LTHOMAS](LTHOMAS.md), [list of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LRHFCALC-_incategory-Examples)

------------------------------------------------------------------------

[^iikura:jcp:2001-1]: [H. Iikura, T. Tsuneda, T. Yanai, and K. Hirao, *A long-range correction scheme for generalized-gradient-approximation exchange functionals*, J. Chem. Phys. **115**, 3540 (2001).](http://doi.org/10.1063/1.1383587)
[^gerber:cpl:2005-2]: [I. C. Gerber and J. G. Ángyán, *Hybrid functional with separated range*, Chem. Phys. Lett. **415**, 100 (2005).](http://doi.org/10.1016/j.cplett.2005.08.060)
[^gerber:jcp:2007-3]: [I. C. Gerber, J. G. Ángyán, M. Marsman, and G. Kresse, *Range separated hybrid density functional with long-range Hartree-Fock exchange applied to solids*, J. Chem. Phys. **127**, 054101 (2007).](http://doi.org/10.1063/1.2759209)

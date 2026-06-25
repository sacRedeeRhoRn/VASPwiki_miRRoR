<!-- Source: https://vasp.at/wiki/index.php/AEXX | revid: 33504 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AEXX


AEXX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **AEXX** | = 0.25 | if [LHFCALC](LHFCALC.md)=.TRUE. .AND. [LRHFCALC](LRHFCALC.md)=.FALSE. |
|  | = 1 | if [LRHFCALC](LRHFCALC.md)=.TRUE. |
|  | = 0 | if [LHFCALC](LHFCALC.md)=.FALSE. |

Description: AEXX specifies
the fraction of exact exchange in a Hartree-Fock-type/hybrid-functional
calculation.

------------------------------------------------------------------------

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>For versions of VASP prior to 6.4.0, <a href="/wiki/ALDAX"
title="ALDAX">ALDAX</a> was constrained to be equal to 1.0-<span
class="mw-selflink selflink">AEXX</span>. This constraint is lifted
since VASP.6.4.0.</li>
<li>For <span class="mw-selflink selflink">AEXX</span>=1.0, VASP
switches off correlation by default (<a href="/wiki/ALDAC"
title="ALDAC">ALDAC</a>=0.0, <a href="/wiki/AGGAC"
title="AGGAC">AGGAC</a>=0.0, and <a href="/wiki/AMGGAC"
title="AMGGAC">AMGGAC</a>=0.0) and thus runs a full Hartree-Fock
calculation.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=AEXX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[BEXX](BEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAX](AMGGAX.md),
[AMGGAC](AMGGAC.md), [LHFCALC](LHFCALC.md),
[HFSCREEN](HFSCREEN.md),
[LMODELHF](LMODELHF.md),
[LTHOMAS](LTHOMAS.md),
[LRHFCALC](LRHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AEXX-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=AEXX&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

  

------------------------------------------------------------------------



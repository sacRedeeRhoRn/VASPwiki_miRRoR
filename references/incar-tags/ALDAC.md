<!-- Source: https://vasp.at/wiki/index.php/ALDAC | revid: 23561 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ALDAC


ALDAC = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ALDAC** | = 1.0 | if [LHFCALC](LHFCALC.md)$=$.FALSE. or [AEXX](AEXX.md)$\neq$1.0 |
|  | = 0.0 | if [LHFCALC](LHFCALC.md)$=$.TRUE. and [AEXX](AEXX.md)$=$1.0 |

Description: ALDAC is a
parameter that multiplies the LDA correlation functional or the LDA part
of the GGA correlation functional.

------------------------------------------------------------------------

ALDAC can be used as the
fraction of LDA correlation in a Hartree-Fock/DFT hybrid functional.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li><span class="mw-selflink selflink">ALDAC</span> is implemented for
all functionals listed at <a href="/wiki/GGA" title="GGA">GGA</a> except
AM05.</li>
<li><span class="mw-selflink selflink">ALDAC</span> is implemented for
the functionals from Libxc (see <a href="/wiki/LIBXC1"
title="LIBXC1">LIBXC1</a> for details).</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=ALDAC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ALDAC-_incategory-Examples)

------------------------------------------------------------------------



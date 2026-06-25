<!-- Source: https://vasp.at/wiki/index.php/AMGGAX | revid: 25513 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AMGGAX


AMGGAX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **AMGGAX** | = 1.0-[AEXX](AEXX.md) | if [LHFCALC](LHFCALC.md)=.TRUE. |
|  | = 1.0 | if [LHFCALC](LHFCALC.md)=.FALSE. |

Description: AMGGAX is a
parameter that multiplies the meta-GGA exchange functional (available as
of VASP.6.4.0).

------------------------------------------------------------------------

AMGGAX can be used as the
fraction of meta-GGA exchange in a Hartree-Fock/DFT hybrid functional
(possible since VASP.6.4.0).

|  |
|----|
| **Important:** AMGGAX can be used only if [LHFCALC](LHFCALC.md)=.TRUE. |

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>Note the difference with respect to <a href="/wiki/AGGAX"
title="AGGAX">AGGAX</a>: <span
class="mw-selflink selflink">AMGGAX</span> multiplies the whole meta-GGA
exchange functional, while <a href="/wiki/AGGAX" title="AGGAX">AGGAX</a>
multiplies only the gradient-correction term of a GGA exchange
functional.</li>
<li><span class="mw-selflink selflink">AMGGAX</span> is implemented for
the functionals from Libxc (see <a href="/wiki/LIBXC1"
title="LIBXC1">LIBXC1</a> for details).</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=AMGGAX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AMGGAX-_incategory-Examples)

------------------------------------------------------------------------



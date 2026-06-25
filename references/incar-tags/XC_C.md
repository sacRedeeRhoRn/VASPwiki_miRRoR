<!-- Source: https://vasp.at/wiki/index.php/XC_C | revid: 34353 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# XC_C


XC_C = \[real array\]  
Default: **XC_C** = 1.0\*NXC 

Description: Multiplication factors for the components of the functional
given by the [XC](XC.md) tag.

------------------------------------------------------------------------

XC_C sets the factors that
multiply each component of the functional specified with the
[XC](XC.md) tag. The number of values specified with
XC_C has to be equal to the
number of functional components set with [XC](XC.md) (NXC).
Examples of how to use XC_C
are provided at [XC](XC.md).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li><span class="mw-selflink selflink">XC_C</span> is available since
VASP.6.4.3.</li>
<li>The <span class="mw-selflink selflink">XC_C</span> tag can be used
together with the <a href="/wiki/ALDAX" title="ALDAX">ALDAX</a>, <a
href="/wiki/ALDAC" title="ALDAC">ALDAC</a>, <a href="/wiki/AGGAX"
title="AGGAX">AGGAX</a>, <a href="/wiki/AGGAC" title="AGGAC">AGGAC</a>,
<a href="/wiki/AMGGAX" title="AMGGAX">AMGGAX</a>, and <a
href="/wiki/AMGGAC" title="AMGGAC">AMGGAC</a> tags that can be used when
<a href="/wiki/LHFCALC" title="LHFCALC">LHFCALC</a>=.TRUE.. Such
examples are provided at <a href="/wiki/XC" title="XC">XC</a>.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=XC_C&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[XC](XC.md), [XCm_Pn](XCm_Pn.md),
[GGA](GGA.md), [METAGGA](METAGGA.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-XC_C-_incategory-Examples)

------------------------------------------------------------------------



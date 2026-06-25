<!-- Source: https://vasp.at/wiki/index.php/SDFTD3_XC | revid: 34411 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SDFTD3_XC


SDFTD3_XC = \[string\]  
Default: **SDFTD3_XC** = The functional set by the
[GGA](GGA.md), [METAGGA](METAGGA.md) or
[XC](XC.md) tag. 

Description: SDFTD3_XC sets
the exchange-correlation functional which determines the van der Waals
parameters used in the DFT-D3 method implemented in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package.

------------------------------------------------------------------------

SDFTD3_XC allows to choose the
exchange-correlation functional that determines which set of van der
Waals parameters is used in the DFT-D3 method implemented in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package
([IVDW](IVDW.md)=15).

The possible choices (e.g.,
SDFTD3_XC=pbe, hse06, ...)
depend on the damping function selected with the
[SDFTD3_DAMPING](SDFTD3_DAMPING.md) tag and are
listed in the file param.f90 of the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) source code.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>The <span class="mw-selflink selflink">SDFTD3_XC</span> tag is
available from VASP.6.6.0 onwards.</li>
<li>The <span class="mw-selflink selflink">SDFTD3_XC</span> tag can be
used only for the simple DFT-D3 package (<a href="/wiki/IVDW"
title="IVDW">IVDW</a>=15).</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=SDFTD3_XC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md),
[SDFTD3_DAMPING](SDFTD3_DAMPING.md),
[GGA](GGA.md), [METAGGA](METAGGA.md),
[XC](XC.md), [DFTD4_XC](DFTD4_XC.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SDFTD3_XC-_incategory-Examples)

------------------------------------------------------------------------



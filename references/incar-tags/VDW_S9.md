<!-- Source: https://vasp.at/wiki/index.php/VDW_S9 | revid: 34383 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VDW_S9


VDW_S9 = \[real\] 

|  |  |  |
|----|----|----|
| Default: **VDW_S9** | = 1 | if [IVDW](IVDW.md)=13 (DFT-D4 package) |
|  | = 0 | if [IVDW](IVDW.md)=15 (simple DFT-D3 package) |
|  | = 0 | if [IVDW](IVDW.md)=11 or 12 (**cannot be changed**) |

Description: VDW_S9 sets the
contribution of the three-body term to the dispersion energy.

------------------------------------------------------------------------

VDW_S9 allows to set the
coefficient $s_{9}$ that
multiplies the three-body (Axilrod–Teller–Muto) term in the DFT-D3 and
DFT-D4 methods implemented in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md)
([IVDW](IVDW.md)=15) and [DFT-D4](../methods/DFT-D4.md)
([IVDW](IVDW.md)=13) external packages, respectively.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>The <span class="mw-selflink selflink">VDW_S9</span> tag is
available from VASP.6.6.0 onwards.</li>
<li><span class="smj-container" style="opacity:.5">$s_{9}=0$</span> for <a href="/wiki/IVDW"
title="IVDW">IVDW</a>=11 and 12 (VASP implementation of <a
href="/wiki/DFT-D3" title="DFT-D3">DFT-D3</a>) and cannot be changed
with <span class="mw-selflink selflink">VDW_S9</span>.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=VDW_S9&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md), [VDW_S6](VDW_S6.md),
[VDW_S8](VDW_S8.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md),
[DFT-D4](../methods/DFT-D4.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VDW_S9-_incategory-Examples)

------------------------------------------------------------------------



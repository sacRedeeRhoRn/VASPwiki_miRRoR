<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/ISURFACE | revid: 34868 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/ISURFACE


KERNEL_TRUNCATION/ISURFACE = 1
\| 2 \| 3 

Description: Specifies the non-periodic dimension when performing
calculations with the Coulomb-kernel-truncation method for
<a href="/wiki/2D_materials" class="mw-redirect" title="2D materials">2D
materials</a>.

------------------------------------------------------------------------

When performing Coulomb-kernel truncation
([`KERNEL_TRUNCATION/LTRUNCATE`](KERNEL_TRUNCATION__LTRUNCATE.md)` = T`)
with
[`KERNEL_TRUNCATION/IDIMENSIONALITY`](KERNEL_TRUNCATION__IDIMENSIONALITY.md)` = 2`,
KERNEL_TRUNCATION/ISURFACE
specifies which direction is non-periodic. If the surface normal points
in the direction of the x-axis set
`KERNEL_TRUNCATION/ISURFACE`` = 1`,
if it is along the y-axis set
`KERNEL_TRUNCATION/ISURFACE`` = 2`,
and along the z-axis set
`KERNEL_TRUNCATION/ISURFACE`` = 3`.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>IF <a href="/wiki/KERNEL_TRUNCATION/LTRUNCATE"
title="KERNEL TRUNCATION/LTRUNCATE"><code class="vasp-dark-link-panel"
style="padding: 2px">KERNEL_TRUNCATION/LTRUNCATE</code></a><code
class="vasp-dark-link-panel" style="padding: 2px"> = F</code>, all other
KERNEL_TRUNCATION tags including <span
class="mw-selflink selflink">KERNEL_TRUNCATION/ISURFACE</span> are
ignored.</li>
<li>Available as of VASP.6.5.0.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/ISURFACE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/LCOARSEN](KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/IDIMENSIONALITY](KERNEL_TRUNCATION__IDIMENSIONALITY.md),
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md),
[KERNEL_TRUNCATION/FACTOR](KERNEL_TRUNCATION__FACTOR.md)



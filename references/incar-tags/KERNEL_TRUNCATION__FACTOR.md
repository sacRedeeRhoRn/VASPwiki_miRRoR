<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/FACTOR | revid: 35976 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/FACTOR


KERNEL_TRUNCATION/FACTOR =
real 

|  |  |  |
|----|----|----|
| Default: **KERNEL_TRUNCATION/FACTOR** | = \$\sqrt{3}\$ | if [`KERNEL_TRUNCATION/IDIMENSIONALITY`](KERNEL_TRUNCATION__IDIMENSIONALITY.md)` = 0` |
|  | = 1 | if [`KERNEL_TRUNCATION/IDIMENSIONALITY`](KERNEL_TRUNCATION__IDIMENSIONALITY.md)` = 2` |

**Description:** Determines the spatial extent of the truncated Coulomb
interaction relative to the computational cell dimension along the
truncation direction.

------------------------------------------------------------------------

KERNEL_TRUNCATION/FACTOR
defines the cutoff distance of the Coulomb-kernel-truncation boundary.
It is expressed as a fraction of the simulation-cell length along the
truncated axis (e.g., the surface normal for 2D systems
[KERNEL_TRUNCATION/ISURFACE](KERNEL_TRUNCATION__ISURFACE.md)).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>If<a href="/wiki/KERNEL_TRUNCATION/LTRUNCATE"
title="KERNEL TRUNCATION/LTRUNCATE"><code class="vasp-dark-link-panel"
style="padding: 2px">KERNEL_TRUNCATION/LTRUNCATE</code></a><code
class="vasp-dark-link-panel" style="padding: 2px"> = F</code>, <span
class="mw-selflink selflink">KERNEL_TRUNCATION/FACTOR</span> is
ignored.</li>
<li>Available as of VASP.6.5.0.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/FACTOR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/IDIMENSIONALITY](KERNEL_TRUNCATION__IDIMENSIONALITY.md),
[KERNEL_TRUNCATION/LCOARSEN](KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md),
[KERNEL_TRUNCATION/ISURFACE](KERNEL_TRUNCATION__ISURFACE.md)



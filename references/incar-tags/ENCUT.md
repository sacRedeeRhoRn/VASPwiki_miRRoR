<!-- Source: https://vasp.at/wiki/index.php/ENCUT | revid: 26956 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENCUT


ENCUT = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ENCUT** | = largest <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> in the [POTCAR](../input-files/POTCAR.md) file |  |

Description: ENCUT specifies
the energy cutoff for the plane-wave basis set in eV.

------------------------------------------------------------------------

All plane waves with a kinetic energy smaller than
$E_{\mathrm{cut}}$ are included in the basis set, i.e.,

$|
\mathbf{G} + \mathbf{k} | < G_{\mathrm{cut}}$ with
$E_{\mathrm{cut}} = \frac{\hbar^2}{2m} G^2_{\mathrm{cut}}$

With this energy cutoff, the number of plane waves included in the basis
set depends on the **k**-point, leading to a superior behavior. For
instance, for energy-volume calculations the total number of plane waves
changes fairly smoothly according to the volume, while the criterion
$|
\mathbf{G} | < G_{\mathrm{cut}}$ (i.e. same number
of plane waves for all **k**-points) would lead to a very rough
energy-volume curve and, generally, to a slower energy convergence with
respect to the basis set size.

The [POTCAR](../input-files/POTCAR.md) files contain a default
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> (and
[ENMIN](ENMIN.md)). Therefore, it is, in principle, not
necessary to specify ENCUT in
the [INCAR](../input-files/INCAR.md) file. For calculations with more than
one species, the maximum cutoff
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> (or
[ENMIN](ENMIN.md)) value is used for the calculation (see
[PREC](PREC.md)).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span
style="color: var(--vpurple);">Important:</span></strong>
<ul>
<li>The convergence of the quantity of interest with respect to the
energy cutoff <span class="mw-selflink selflink">ENCUT</span> should
always be checked.</li>
<li>We strongly recommend specifying the energy cutoff <span
class="mw-selflink selflink">ENCUT</span> always manually in the <a
href="/wiki/INCAR" title="INCAR">INCAR</a> file to ensure the same
accuracy between calculations. Otherwise, the default <span
class="mw-selflink selflink">ENCUT</span> may differ among the different
calculations (e.g., for the calculation of the cohesive energy), with
the consequence that the total energies, for instance, can not be
compared.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=ENCUT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>,
[ENMIN](ENMIN.md), [ENINI](ENINI.md),
[ENAUG](ENAUG.md), [PREC](PREC.md),
[NGX](NGX.md), [NGY](NGY.md), [NGZ](NGZ.md),
[NGXF](NGXF.md), [NGYF](NGYF.md),
[NGZF](NGZF.md), [POTCAR](../input-files/POTCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ENCUT-_incategory-Examples)



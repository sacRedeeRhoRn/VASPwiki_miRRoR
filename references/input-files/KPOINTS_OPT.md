<!-- Source: https://vasp.at/wiki/index.php/KPOINTS_OPT | revid: 25762 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINTS_OPT


KPOINTS_OPT is an optional
input file to perform an additional one-shot calculation after
self-consistency is reached. The format is the same as for the
[KPOINTS](KPOINTS.md) file. VASP first performs a
self-consistent calculation using the **k** points specified in the
[KPOINTS](KPOINTS.md) file and then performs an additional
one-shot calculation to obtain the Kohn–Sham orbitals and eigenenergies
at the **k** points specified in the
KPOINTS_OPT file.

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
<li>The <a href="/wiki/KPOINTS" title="KPOINTS">KPOINTS</a> file must
contain a uniform <strong>k</strong> mesh, when the <span
class="mw-selflink selflink">KPOINTS_OPT</span> file should be used
afterward.</li>
<li>In the case of a functional using the long-range Hartree-Fock
exchange (e.g., unscreened hybrid functionals), the default method for
treating the Coulomb singularity (<a href="/wiki/HFRCUT"
title="HFRCUT">HFRCUT</a>=0) is not adapted to do so for states at
k-points that have not been included in the calculation of the Fock
potential. Instead, <a href="/wiki/HFRCUT" title="HFRCUT">HFRCUT</a>=-1
should be used.</li>
</ul></td>
</tr>
</tbody>
</table>

KPOINTS_OPT is read
automatically when present. To avoid this, set
[LKPOINTS_OPT](../incar-tags/LKPOINTS_OPT.md)`=.FALSE.` in the
[INCAR](INCAR.md) file. VASP writes the
[PROCAR_OPT](../output-files/PROCAR_OPT.md) file when
[LORBIT](../incar-tags/LORBIT.md)\>10 and corresponding fields in the
[vaspout.h5](../output-files/Vaspout.h5.md) file indicated by the
keyword *kpoints_opt*.

|  |
|----|
| **Mind:** Available as of VASP 6.3.0. |

## Related tags and sections\[<a
href="/wiki/index.php?title=KPOINTS_OPT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[LKPOINTS_OPT](../incar-tags/LKPOINTS_OPT.md),
[KPOINTS](KPOINTS.md),
[KSPACING](../incar-tags/KSPACING.md),
[PROCAR_OPT](../output-files/PROCAR_OPT.md),
[KPOINTS_OPT_NKBATCH](../incar-tags/KPOINTS_OPT_NKBATCH.md)



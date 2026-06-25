<!-- Source: https://vasp.at/wiki/index.php/NBANDS_WAVE | revid: 24555 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBANDS_WAVE


NBANDS_WAVE = \[integer\] 

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Default: <strong>NBANDS_WAVE</strong>
<p><strong></strong></p></td>
<td>= <a href="/wiki/NBANDSGW" title="NBANDSGW">NBANDSGW</a></td>
<td>for <a href="/wiki/LALL_IN_ONE"
title="LALL IN ONE">LALL_IN_ONE</a>=.TRUE. and <a href="/wiki/NBANDS"
title="NBANDS">NBANDS</a>&lt;1</td>
</tr>
<tr>
<td></td>
<td>= <a href="/wiki/NBANDS" title="NBANDS">NBANDS</a></td>
<td>for <a href="/wiki/LALL_IN_ONE"
title="LALL IN ONE">LALL_IN_ONE</a>=.TRUE. and <a href="/wiki/NBANDS"
title="NBANDS">NBANDS</a>&gt;0</td>
</tr>
<tr>
<td></td>
<td>= <a href="/wiki/NBANDSEXACT"
title="NBANDSEXACT">NBANDSEXACT</a></td>
<td>for <a href="/wiki/LALL_IN_ONE"
title="LALL IN ONE">LALL_IN_ONE</a>=.FALSE. and <a href="/wiki/NBANDS"
title="NBANDS">NBANDS</a>&lt;1</td>
</tr>
<tr>
<td></td>
<td>= <a href="/wiki/NBANDS" title="NBANDS">NBANDS</a></td>
<td>for <a href="/wiki/LALL_IN_ONE"
title="LALL IN ONE">LALL_IN_ONE</a>=.FALSE. and <a href="/wiki/NBANDS"
title="NBANDS">NBANDS</a>&gt;0</td>
</tr>
</tbody>
</table>

Description: NBANDS_WAVE
specifies the number of bands written to
[WAVECAR](../input-files/WAVECAR.md) in the all-in-one mode of
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>
calculations, i.e.,
[ALGO](ALGO.md)=[ACFDT\[R\]](/wiki/ACFDT/RPA_calculations "ACFDT/RPA calculations"),
[\[EV\]GW0\[R\]](/wiki/Practical_guide_to_GW_calculations "Practical guide to GW calculations"),
[GWR](../methods/Practical_guide_to_GW_calculations.md).

|  |
|----|
| **Mind:** available as of VASP.6.4.0 |

------------------------------------------------------------------------

In the all-in-one mode, VASP automatically performs the necessary DFT
steps prior to the many-body perturbation theory (MBPT) calculation,
i.e. a DFT calculation with [NBANDS](NBANDS.md), followed by
an exact diagonalization of the Kohn-Sham Hamiltonian with
[NBANDSEXACT](NBANDSEXACT.md) bands. Note,
[NBANDSEXACT](NBANDSEXACT.md) is set by default to the
maximum number of plane-waves given by the chosen energy cutoff for the
orbitals [ENCUT](ENCUT.md). In the all-in-one mode, the
actual GW/RPA calculation is also performed with
[NBANDSEXACT](NBANDSEXACT.md) bands. If
NBANDS_WAVE is not set, all
orbitals are written to [WAVECAR](../input-files/WAVECAR.md), which
potentially becomes huge in file size.

|  |
|----|
| **Tip:** The NBANDS_WAVE tag can be used to limit the number of bands written to [WAVECAR](../input-files/WAVECAR.md) if [LALL_IN_ONE](LALL_IN_ONE.md)=.TRUE. |

The all-in-one mode is automatically enabled for
[ALGO](ALGO.md)=\[EV\]GW\[0\]R, RPA\[R\],ACFDT\[R\] if
[NBANDS](NBANDS.md) is not set.

## Related tags and articles\[<a
href="/wiki/index.php?title=NBANDS_WAVE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ALGO](ALGO.md), [NBANDS](NBANDS.md)
[NBANDSEXACT](NBANDSEXACT.md)
[IALL_IN_ONE](IALL_IN_ONE.md)
[LALL_IN_ONE](LALL_IN_ONE.md)

------------------------------------------------------------------------



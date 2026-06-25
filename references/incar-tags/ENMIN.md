<!-- Source: https://vasp.at/wiki/index.php/ENMIN | revid: 25193 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENMIN


ENMIN = \[real\]  
Default: **ENMIN** = value read from [POTCAR](../input-files/POTCAR.md) 

Description: ENMIN describes
the minimum viable
<a href="/wiki/Energy_cut_off_and_FFT_mesh" class="mw-redirect"
title="Energy cut off and FFT mesh">plane-wave energy cutoff</a> in eV
for the pseudopotential it is read from.

------------------------------------------------------------------------

For a multi-element [POTCAR](../input-files/POTCAR.md) file, the maximum
ENMIN determines the
absolutely lowest cutoff energy for the plane-wave basis that should be
used. If the deprecated [PREC](PREC.md) setting *Low* is used,
this value is used by default. With all recommended
[PREC](PREC.md) setting VASP will use the largest
*recommended* cutoff energy
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> found
in the POTCAR file instead. In all cases, the value can be overwritten
by setting [ENCUT](ENCUT.md) in the
[INCAR](../input-files/INCAR.md) file.

## Related tags and articles\[<a href="/wiki/index.php?title=ENMIN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[POTCAR](../input-files/POTCAR.md),
<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a>

------------------------------------------------------------------------



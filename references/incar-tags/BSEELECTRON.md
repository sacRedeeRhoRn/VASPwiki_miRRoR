<!-- Source: https://vasp.at/wiki/index.php/BSEELECTRON | revid: 24373 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BSEELECTRON


BSEELECTRON = \[real array\] 

Description: BSEELECTRON sets
the coordinates of the fixed electron of the exciton wavefunction

------------------------------------------------------------------------

If BSEELECTRON is set in a BSE
calculation, VASP computes exciton wavefunction for the first
[NBSEEIG](NBSEEIG.md) states. The coordinates are provided
in direct (fractional) coordinates.

When fixing the position of the particle, ensure that it is not fixed
exactly at the center of an atom or coincides with a node of the
wavefunction. To avoid that, shift the fixed coordinate slightly away
from the center of the atom. Furthermore, the wavefunction of the fixed
particle is taken at the nearest $\mathbf{G}$-vector, whose exact position is written in the
[OUTCAR](../output-files/OUTCAR.md) file

    hole position is fixed at:

or

    electron position is fixed at:

## Related tags and sections\[<a
href="/wiki/index.php?title=BSEELECTRON&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[BSEHOLE](BSEHOLE.md), [NBSEEIG](NBSEEIG.md),
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>, [Plotting exciton
wavefunction](../theory/Plotting_exciton_wavefunction.md)

------------------------------------------------------------------------



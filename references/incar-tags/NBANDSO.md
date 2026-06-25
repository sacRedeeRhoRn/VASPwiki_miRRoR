<!-- Source: https://vasp.at/wiki/index.php/NBANDSO | revid: 17869 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBANDSO


NBANDSO = \[integer\] 

|                      |                               |     |
|----------------------|-------------------------------|-----|
| Default: **NBANDSO** | = number of occupied orbitals |     |

Description: NBANDSO
determines how many occupied orbitals are included in the
Casida/<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a> or time propagation
([ALGO](ALGO.md)=TIMEEV.

------------------------------------------------------------------------

For the time-propagation algorithm increasing
NBANDSO only modestly
increases the compute time. For BSE and Casida-type calculations, the
compute time grows with the third power of the number of included
occupied and unoccupied bands

$(N_{\mathrm{occ}} N_{\mathrm{virtual}} N_{\mathrm{k}})^{3}$

and the memory requirements increase quadratically

$(N_{\mathrm{occ}}N_{\mathrm{virtual}} N_{\mathrm{k}})^{2}$

Please be aware that symmetry is not exploited in the BSE code, hence
memory requirements can be excessive. To allow for calculations on large
systems, the BSE code distributes the BSE matrix among all available
cores and uses ScaLAPACK for the diagonalization.

VASP always uses the orbitals closest to the Fermi-level, and
NBANDSO
($N_{\mathrm{occ}}$) and
[NBANDSV](NBANDSV.md) ($N_{\mathrm{virtual}}$) determines how many occupied and unoccupied orbitals
are included. The defaults are fairly "conservative" and equal the total
number of electrons/2 (this usually implies that all occupied states are
included). For highly accurate results,
[NBANDSV](NBANDSV.md) often needs to be increased, whereas
for large systems one is often forced to reduce both values to much
smaller numbers. Sometimes qualitative results for bandlike Wannier-Mott
excitons can be obtained even with a single conduction and valence band.

## Related tags and articles\[<a href="/wiki/index.php?title=NBANDSO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NBANDSV](NBANDSV.md),
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>,
<a href="/wiki/Timepropagation" class="mw-redirect"
title="Timepropagation">Timepropagation</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NBANDSO-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/PHON_SIGMA | revid: 24232 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PHON_SIGMA


PHON_SIGMA = \[real\] 

|                         |             |     |
|-------------------------|-------------|-----|
| Default: **PHON_SIGMA** | = 0.0005 eV |     |

Description: Set the width of the Gaussian function in eV to compute the
phonon density of states.

------------------------------------------------------------------------

The density of states is computed between $\[\omega_{\text{min}}-5\sigma,\omega_{\text{max}}+5\sigma\]$ with $\omega_{\text{min}}$ and $\omega_{\text{max}}$ the lowest and highest phonon frequency and
$\sigma$ the broadening
PHON_SIGMA. The number of
energy points in this interval is set by
[PHON_NEDOS](PHON_NEDOS.md).

|  |
|----|
| **Mind:** Only available as of VASP 6.4.0. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PHON_SIGMA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QPOINTS](../input-files/QPOINTS.md),
[PHON_NWRITE](PHON_NWRITE.md),
[LPHON_POLAR](LPHON_POLAR.md),
[PHON_DIELECTRIC](PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](PHON_G_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPHON_DISPERSION-_incategory-Examples)



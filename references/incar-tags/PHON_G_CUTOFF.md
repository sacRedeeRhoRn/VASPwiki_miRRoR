<!-- Source: https://vasp.at/wiki/index.php/PHON_G_CUTOFF | revid: 22585 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PHON_G_CUTOFF


PHON_G_CUTOFF = \[real\] 

|                            |       |     |
|----------------------------|-------|-----|
| Default: **PHON_G_CUTOFF** | = 8.0 |     |

Description: PHON_G_CUTOFF
sets the cutoff radius in reciprocal space used to determine the number
of $\mathbf{G}$ vectors involved in the Ewald sum in polar
phonon calculations.

------------------------------------------------------------------------

The Ewald sum that accounts for the long-range electrostatic
interactions in phonon calculations runs over all G-vectors inside a
cutoff sphere. The radius of this sphere is given by
PHON_G_CUTOFF as a multiple of
the longest reciprocal lattice vector of the primitive cell (as detected
by VASP). Specifying the cutoff this way (as opposed to an absolute
length or energy) ensures a default value that is relatively
system-independent.

The default value of
PHON_G_CUTOFF is a safe choice
in most cases. Lowering
PHON_G_CUTOFF can result in
faster phonon calculations. However, ensure that the phonon spectrum is
properly converged. If you run into convergence problems, try raising
the value until the phonon dispersion converges.

For more information on polar phonon calculations, see
[LPHON_POLAR](LPHON_POLAR.md).

|  |
|----|
| **Mind:** Only available as of VASP 6.3.2. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PHON_G_CUTOFF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QPOINTS](../input-files/QPOINTS.md),
[LPHON_DISPERSION](LPHON_DISPERSION.md),
[PHON_NWRITE](PHON_NWRITE.md),
[LPHON_POLAR](LPHON_POLAR.md),
[PHON_DIELECTRIC](PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PHON_G_CUTOFF-_incategory-Examples)



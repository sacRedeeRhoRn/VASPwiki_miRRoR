<!-- Source: https://vasp.at/wiki/index.php/PHON_DIELECTRIC | revid: 22583 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PHON_DIELECTRIC


PHON_DIELECTRIC = \[3x3
real\] 

|                              |        |     |
|------------------------------|--------|-----|
| Default: **PHON_DIELECTRIC** | = None |     |

Description: PHON_DIELECTRIC
sets the static dielectric tensor to be used for the dipole-dipole
corrections in the computation of the phonon dispersion. This is only
used when [LPHON_POLAR](LPHON_POLAR.md)=.TRUE.

------------------------------------------------------------------------

If the material is non-metallic and polar (i.e. two or more atoms in the
unit cell carry nonzero Born effective charge tensors), a special
treatment of the long-range dipole-dipole interaction is required to
obtain a smooth phonon dispersion. This is activated by setting
[LPHON_POLAR](LPHON_POLAR.md)=.TRUE. and supplying the
static dielectric tensor
(PHON_DIELECTRIC) and the
Born-effective charges
([PHON_BORN_CHARGES](PHON_BORN_CHARGES.md)) which
can be obtained in a separate VASP calculation using the
[LEPSILON](LEPSILON.md) or
[LCALCEPS](LCALCEPS.md) tag. The dipole-dipole part of the
interatomic force-constants is evaluated using an Ewald summation with
the number of $\mathbf{G}$
vectors determined by the cutoff length
([PHON_G_CUTOFF](PHON_G_CUTOFF.md)).

|  |
|----|
| **Mind:** Only available as of VASP 6.3.2. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PHON_DIELECTRIC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QPOINTS](../input-files/QPOINTS.md),
[LPHON_DISPERSION](LPHON_DISPERSION.md),
[PHON_NWRITE](PHON_NWRITE.md),
[LPHON_POLAR](LPHON_POLAR.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](PHON_G_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PHON_DIELECTRIC-_incategory-Examples)



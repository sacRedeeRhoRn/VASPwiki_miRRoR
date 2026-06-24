<!-- Source: https://vasp.at/wiki/index.php/LPHON_POLAR | revid: 27678 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LPHON_POLAR
LPHON_POLAR = .TRUE. \| .FALSE.  
Default: **LPHON_POLAR** = .FALSE. 

Description: LPHON_POLAR includes dipole-dipole corrections in the
computation of the phonon dispersion. For this mode,
[PHON_DIELECTRIC](PHON_DIELECTRIC.md) and
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md) must
also be set.

------------------------------------------------------------------------

If the material is non-metallic and polar (i.e. two or more atoms in the
unit cell carry nonzero Born effective charge tensors), a special
treatment of the long-range dipole-dipole interaction is required to
obtain a smooth phonon dispersion. This is activated by setting
LPHON_POLAR=.TRUE. and supplying the static dielectric tensor
([PHON_DIELECTRIC](PHON_DIELECTRIC.md)) and the
Born-effective charges
([PHON_BORN_CHARGES](PHON_BORN_CHARGES.md)) which
can be obtained in a separate VASP calculation using the
[LEPSILON](LEPSILON.md) or
[LCALCEPS](LCALCEPS.md) tag. The dipole-dipole part of the
interatomic force-constants is evaluated using an Ewald summation with
the number of $\mathbf{G}$ vectors
determined by the cutoff length
([PHON_G_CUTOFF](PHON_G_CUTOFF.md)).

In the case of metals, the dielectric function is infinite, for nonpolar
semiconductors the Born effective charges are zero which in both cases
means that the [long-range interatomic
force-constants](../theory/Phonons-_Theory.md)
are zero and this dipole-dipole correction does not need to be applied.

|                                            |
|--------------------------------------------|
| **Mind:** Only available as of VASP 6.3.2. |

## Related tags and articles
[QPOINTS](../input-files/QPOINTS.md),
[LPHON_DISPERSION](LPHON_DISPERSION.md),
[PHON_NWRITE](PHON_NWRITE.md),
[PHON_DIELECTRIC](PHON_DIELECTRIC.md),
[PHON_BORN_CHARGES](PHON_BORN_CHARGES.md),
[PHON_G_CUTOFF](PHON_G_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPHON_POLAR-_incategory-Examples)

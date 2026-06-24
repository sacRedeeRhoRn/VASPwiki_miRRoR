<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/IDIMENSIONALITY | revid: 34863 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/IDIMENSIONALITY
KERNEL_TRUNCATION/IDIMENSIONALITY = 0 \| 2 \| 3  
Default: **KERNEL_TRUNCATION/IDIMENSIONALITY** = 3 

Description: Specifies the boundary condition used to compute the
hartree and ionic potential.

------------------------------------------------------------------------

If
[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md)
= T, KERNEL_TRUNCATION/IDIMENSIONALITY determines the boundary condition
that is used to compute the local potential. Setting
KERNEL_TRUNCATION/IDIMENSIONALITY to either 0 or 2 uses the 0D and 2D
truncated kernel
respectively.^([\[1\]](#cite_note-vijay:prb:2025-1)[\[2\]](#cite_note-rozzi:prb:2006-2)[\[3\]](#cite_note-sohier:prb:2017-3))
These kernels create 0D (i.e. no periodic interactions, as is the case
of molecules) and 2D (i.e. periodic interactions only in two dimensions,
as in the case for surfaces).

[TABLE]

## Contents

- [1 KERNEL_TRUNCATION/IDIMENSIONALITY =
  0](#KERNEL_TRUNCATION/IDIMENSIONALITY_=_0)
- [2 KERNEL_TRUNCATION/IDIMENSIONALITY =
  2](#KERNEL_TRUNCATION/IDIMENSIONALITY_=_2)
- [3 KERNEL_TRUNCATION/IDIMENSIONALITY = 3
  (default)](#KERNEL_TRUNCATION/IDIMENSIONALITY_=_3_(default))
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

## KERNEL_TRUNCATION/IDIMENSIONALITY = 0
Consider using the option when computing energies and forces of atoms
and molecules. Recommended [INCAR](../input-files/INCAR.md) tags to be used
with option are

     KERNEL_TRUNCATION/LTRUNCATE = T
     KERNEL_TRUNCATION/IDIMENSIONALITY = 0
     KERNEL_TRUNCATION/LCOARSEN = T

## KERNEL_TRUNCATION/IDIMENSIONALITY = 2
Use this option when computing the energies and forces of 2D and
quasi-2D systems, such as 2D materials and surfaces. We suggest setting
the following [INCAR](../input-files/INCAR.md) tags for a surface that is
oriented along the z-axis

     KERNEL_TRUNCATION/LTRUNCATE = T
     KERNEL_TRUNCATION/IDIMENSIONALITY = 2
     KERNEL_TRUNCATION/LCOARSEN = T
     KERNEL_TRUNCATION/ISURFACE = 3

## KERNEL_TRUNCATION/IDIMENSIONALITY = 3 (default)
The system is periodic in all dimensions, i.e. there is no influence of
the Coulomb-kernel truncation on the resulting energies and forces.

## Related tags and articles
[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/LCOARSEN](KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/ISURFACE](KERNEL_TRUNCATION__ISURFACE.md),
[KERNEL_TRUNCATION/FACTOR](KERNEL_TRUNCATION__FACTOR.md),
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md)

## References
1.  [↑](#cite_ref-vijay:prb:2025_1-0) [S. Vijay, M. Schlipf, H.
    Miranda, F. Karsai, M. Kaltak, M. Marsman, and G. Kresse, *Efficient
    periodic density functional theory calculations of charged molecules
    and surfaces using Coulomb kernel truncation*, Phys. Rev. B **112**,
    045409 (2025).](https://doi.org/10.1103/cd6s-cdkf)
2.  [↑](#cite_ref-rozzi:prb:2006_2-0) [C. A. Rozzi, D. Varsano, A.
    Marini, E. K. Gross, A. J. Rubio, Phys. Rev. B **73**, 20511
    (2006).](https://doi.org/10.1103/PhysRevB.73.205119)
3.  [↑](#cite_ref-sohier:prb:2017_3-0) [T. Sohier, M. Calandra, and F.
    Mauri, Phys. Rev. B 96, 75448
    (2017).](https://doi.org/10.1103/PhysRevB.96.075448)

<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/IDIMENSIONALITY | revid: 34863 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/IDIMENSIONALITY


KERNEL_TRUNCATION/IDIMENSIONALITY =
0 \| 2 \| 3  
Default: **KERNEL_TRUNCATION/IDIMENSIONALITY** = 3 

Description: Specifies the boundary condition used to compute the
hartree and ionic potential.

------------------------------------------------------------------------

If
[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md)
= T,
KERNEL_TRUNCATION/IDIMENSIONALITY
determines the boundary condition that is used to compute the local
potential. Setting
KERNEL_TRUNCATION/IDIMENSIONALITY
to either 0 or 2 uses the 0D and 2D truncated kernel
respectively.[^vijay:prb:2025-1][^rozzi:prb:2006-2][^sohier:prb:2017-3]
These kernels create 0D (i.e. no periodic interactions, as is the case
of molecules) and 2D (i.e. periodic interactions only in two dimensions,
as in the case for surfaces).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>If <a href="/wiki/KERNEL_TRUNCATION/LTRUNCATE"
title="KERNEL TRUNCATION/LTRUNCATE">KERNEL_TRUNCATION/LTRUNCATE</a> is
switched off, all other KERNEL_TRUNCATION tags including <span
class="mw-selflink selflink">KERNEL_TRUNCATION/IDIMENSIONALITY</span>
will be ignored.</li>
<li>Available as of VASP.6.5.0.</li>
</ul></td>
</tr>
</tbody>
</table>


## Contents


- [1
  KERNEL_TRUNCATION/IDIMENSIONALITY =
  0](#KERNEL_TRUNCATION/IDIMENSIONALITY_=_0)
- [2
  KERNEL_TRUNCATION/IDIMENSIONALITY =
  2](#KERNEL_TRUNCATION/IDIMENSIONALITY_=_2)
- [3
  KERNEL_TRUNCATION/IDIMENSIONALITY = 3
  (default)](#KERNEL_TRUNCATION/IDIMENSIONALITY_=_3_(default))
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


## KERNEL_TRUNCATION/IDIMENSIONALITY = 0\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/IDIMENSIONALITY&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: KERNEL_TRUNCATION/IDIMENSIONALITY = 0">edit</a> \| (./index.php.md)\]

Consider using the option when computing energies and forces of atoms
and molecules. Recommended [INCAR](../input-files/INCAR.md) tags to be used
with option are

     KERNEL_TRUNCATION/LTRUNCATE = T
     KERNEL_TRUNCATION/IDIMENSIONALITY = 0
     KERNEL_TRUNCATION/LCOARSEN = T

## KERNEL_TRUNCATION/IDIMENSIONALITY = 2\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/IDIMENSIONALITY&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: KERNEL_TRUNCATION/IDIMENSIONALITY = 2">edit</a> \| (./index.php.md)\]

Use this option when computing the energies and forces of 2D and
quasi-2D systems, such as 2D materials and surfaces. We suggest setting
the following [INCAR](../input-files/INCAR.md) tags for a surface that is
oriented along the z-axis

     KERNEL_TRUNCATION/LTRUNCATE = T
     KERNEL_TRUNCATION/IDIMENSIONALITY = 2
     KERNEL_TRUNCATION/LCOARSEN = T
     KERNEL_TRUNCATION/ISURFACE = 3

## KERNEL_TRUNCATION/IDIMENSIONALITY = 3 (default)\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/IDIMENSIONALITY&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: KERNEL_TRUNCATION/IDIMENSIONALITY = 3 (default)">edit</a> \| (./index.php.md)")\]

The system is periodic in all dimensions, i.e. there is no influence of
the Coulomb-kernel truncation on the resulting energies and forces.

## Related tags and articles\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/IDIMENSIONALITY&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/LCOARSEN](KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/ISURFACE](KERNEL_TRUNCATION__ISURFACE.md),
[KERNEL_TRUNCATION/FACTOR](KERNEL_TRUNCATION__FACTOR.md),
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md)

## References\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/IDIMENSIONALITY&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^vijay:prb:2025-1]: [S. Vijay, M. Schlipf, H. Miranda, F. Karsai, M. Kaltak, M. Marsman, and G. Kresse, *Efficient periodic density functional theory calculations of charged molecules and surfaces using Coulomb kernel truncation*, Phys. Rev. B **112**, 045409 (2025).](https://doi.org/10.1103/cd6s-cdkf)
[^rozzi:prb:2006-2]: [C. A. Rozzi, D. Varsano, A. Marini, E. K. Gross, A. J. Rubio, Phys. Rev. B **73**, 20511 (2006).](https://doi.org/10.1103/PhysRevB.73.205119)
[^sohier:prb:2017-3]: [T. Sohier, M. Calandra, and F. Mauri, Phys. Rev. B 96, 75448 (2017).](https://doi.org/10.1103/PhysRevB.96.075448)

<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/LTRUNCATE | revid: 35076 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/LTRUNCATE


KERNEL_TRUNCATION/LTRUNCATE =
.True. \| .False.  
Default: **KERNEL_TRUNCATION/LTRUNCATE** = .False. 

Description: Truncates the Coulomb kernel to remove [electrostatic
interactions](../categories/Category-Electrostatics.md)
along non-periodic dimensions.

------------------------------------------------------------------------

Setting
KERNEL_TRUNCATION/LTRUNCATE =
T switches on the Coulomb-kernel-truncation
method[^vijay:prb:2025-1][^rozzi:prb:2006-2][^sohier:prb:2017-3].
It effectively removes interactions with periodic replicas in
non-periodic directions. In other words, the interactions are removed
along the surface normal for
<a href="/wiki/2D_materials" class="mw-redirect" title="2D materials">2D
materials</a>, and along all directions for 0D systems, i.e. for
isolated atoms and molecules.

In the simplest implementation of the Coulomb-kernel-truncation method
([`KERNEL_TRUNCATION/LCOARSEN`](KERNEL_TRUNCATION__LCOARSEN.md)` = F`),
the computational cell provided in the [POSCAR](../input-files/POSCAR.md)
file is internally padded by an additional vacuum (see
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md)).
This implies increasing the [FFT-grid
sizes](../tutorials/Energy_cutoff_and_FFT_meshes.md)
by a certain factor and thus leads to a significant increase in
computational cost.

|  |
|----|
| **Tip:** Use the [`KERNEL_TRUNCATION/LCOARSEN`](KERNEL_TRUNCATION__LCOARSEN.md)` = T` to avoid the increased [FFT-grid sizes](../tutorials/Energy_cutoff_and_FFT_meshes.md). |

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li><span
class="mw-selflink selflink">KERNEL_TRUNCATION/LTRUNCATE</span> acts as
a "super-tag", i.e. unless this tag is switched on further options in
KERNEL_TRUNCATION will be ignored.</li>
<li>This tag is only available as of VASP.6.5.0.</li>
</ul></td>
</tr>
</tbody>
</table>

Detailed information about the setting are documented on respective
related tags.

|  |
|----|
| **Warning:** When padding is used, the vaccum is added on the edges of the cell, therefore it is very important there are no atoms on the cell boundary in the non-periodic direction. We recommend centering the motif in the simulation box. If you encounter problems using Coulomb truncation with padding, try the same calculations without padding (see examples bellow). |

## Example\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/LTRUNCATE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Example">edit</a> \| (./index.php.md)\]

    KERNEL_TRUNCATION {
         LTRUNCATE       = T
         IDIMENSIONALITY = 2
         ISURFACE        = 3
         LCOARSEN        = F
    }

In this case, we pad the cell along the surface normal direction. The
Coulomb interaction is truncated beyond the boundaries of the cell along
this direction.

    KERNEL_TRUNCATION {
         LTRUNCATE       = T
         IDIMENSIONALITY = 2
         ISURFACE        = 3
         IPAD            = 1
         FACTOR          = 0.5
    }

This setup corresponds to truncating the Coulomb interaction along the
surface normal direction (say, along z) for a
<a href="/wiki/2D_material" class="mw-redirect" title="2D material">2D
material</a>, using no vacuum padding and a truncation length of z/2. In
this case, half of the simulation box is effectively unused and will
produce a potential that is not desired. However, the algorithm is much
simpler. We recommend this configuration for debugging purposes.

## Related tags and articles\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/LTRUNCATE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[KERNEL_TRUNCATION/LCOARSEN](KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/IDIMENSIONALITY](KERNEL_TRUNCATION__IDIMENSIONALITY.md),
[KERNEL_TRUNCATION/ISURFACE](KERNEL_TRUNCATION__ISURFACE.md),
[KERNEL_TRUNCATION/FACTOR](KERNEL_TRUNCATION__FACTOR.md),
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md)

## References\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/LTRUNCATE&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^vijay:prb:2025-1]: [S. Vijay, M. Schlipf, H. Miranda, F. Karsai, M. Kaltak, M. Marsman, and G. Kresse, *Efficient periodic density functional theory calculations of charged molecules and surfaces using Coulomb kernel truncation*, Phys. Rev. B **112**, 045409 (2025).](https://doi.org/10.1103/cd6s-cdkf)
[^rozzi:prb:2006-2]: [C. A. Rozzi, D. Varsano, A. Marini, E. K. Gross, A. J. Rubio, Phys. Rev. B **73**, 20511 (2006).](https://doi.org/10.1103/PhysRevB.73.205119)
[^sohier:prb:2017-3]: [T. Sohier, M. Calandra, and F. Mauri, Phys. Rev. B 96, 75448 (2017).](https://doi.org/10.1103/PhysRevB.96.075448)

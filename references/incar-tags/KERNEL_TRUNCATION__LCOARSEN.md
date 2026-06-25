<!-- Source: https://vasp.at/wiki/index.php/KERNEL_TRUNCATION/LCOARSEN | revid: 34858 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KERNEL_TRUNCATION/LCOARSEN


KERNEL_TRUNCATION/LCOARSEN =
.True. \| .False.  
Default: **KERNEL_TRUNCATION/LCOARSEN** = .False. 

Description: Coarsen the charge density before padding to speed up the
computation of the local potential in the Coulomb-kernel-truncation
method.

------------------------------------------------------------------------

The Coulomb-kernel-truncation method
([KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md))
modifies the electrostatic potential to remove spurious interactions
between periodic images in systems with reduced dimensionality (e.g.
molecules or surfaces).
`KERNEL_TRUNCATION/LCOARSEN`` = T`
avoids significantly increasing [FFT-grid
sizes](../tutorials/Energy_cutoff_and_FFT_meshes.md)
by using a *coarsen-before-padding* approach:

- The full electrostatic potential is first computed under standard 3D
  periodic boundary conditions.
- A coarse representation of the charge density on a reduced
  [FFT-grid](../tutorials/Energy_cutoff_and_FFT_meshes.md)
  which is constructed by retaining only the long-wavelength (low-\|G\|)
  components responsible for long-range interactions.
- The truncated Coulomb kernel is applied only to this coarse density
  using a padded grid (see
  [KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md)).
- The final potential is obtained by subtracting the long-range periodic
  contribution and replacing it with the correctly truncated one.

This procedure exploits the fact that
<a href="/wiki/Electrostatics" class="mw-redirect"
title="Electrostatics">long-range electrostatics</a> depends only on
low-frequency components of the charge density, allowing the expensive
padded FFTs to be performed on a much smaller grid with minimal loss of
accuracy.

|  |
|----|
| **Mind:** If [`KERNEL_TRUNCATION/LTRUNCATE`](KERNEL_TRUNCATION__LTRUNCATE.md)` = F`, all other KERNEL_TRUNCATION tags including KERNEL_TRUNCATION/LCOARSEN are ignored. |

## Related tags and articles\[<a
href="/wiki/index.php?title=KERNEL_TRUNCATION/LCOARSEN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[KERNEL_TRUNCATION/LTRUNCATE](KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/IDIMENSIONALITY](KERNEL_TRUNCATION__IDIMENSIONALITY.md),
[KERNEL_TRUNCATION/ISURFACE](KERNEL_TRUNCATION__ISURFACE.md),
[KERNEL_TRUNCATION/IPAD](KERNEL_TRUNCATION__IPAD.md),
[KERNEL_TRUNCATION/FACTOR](KERNEL_TRUNCATION__FACTOR.md)



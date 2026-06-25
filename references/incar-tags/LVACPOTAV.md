<!-- Source: https://vasp.at/wiki/index.php/LVACPOTAV | revid: 24020 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LVACPOTAV


LVACPOTAV = .True. \|
.False.  
Default: **LVACPOTAV** = .False. 

Description: Switch on determining the vacuum potential by averaging the
local potential over a field-free region.

------------------------------------------------------------------------

LVACPOTAV switches on the
computation of the vacuum potential, i.e., the average of the local
potential in the vacuum region. It computes the average potential by
searching regions that are field-free
([VACPOTFLAT](VACPOTFLAT.md)), and the 2D-averaged
charge density is nearly zero. The averaging is done in the direction of
[IDIPOL](IDIPOL.md) and is reported as the vacuum potential
in the [OUTCAR](../output-files/OUTCAR.md).

|  |
|----|
| **Tip:** As LVACPOTAV performs a post-processing step, you may use it together with [ALGO](ALGO.md) = None by restarting a converged calculation. |

The vacuum potential is one of the quantities needed to [compute the
work
function](../tutorials/Computing_the_work_function.md).
It can be extracted from the [OUTCAR](../output-files/OUTCAR.md) by the
following bash command

     grep upper OUTCAR

Note that two vacuum potentials will be produced, one corresponding to
the upper termination of the slab and one corresponding to the lower.
Depending on the system, one might be more interesting than the other.

|  |
|----|
| **Tip:** For determining the work function, we suggest using LVACPOTAV along with the [LVHAR](LVHAR.md) tag such that only the sum of the Hartree and ionic potentials are used in the calculation of the vacuum potential. This choice is because the exchange-correlation potential might be noisy in the vacuum region but should, in principle, be zero. |

|  |
|----|
| **Mind:** LVACPOTAV is available only for versions after 6.4.3. |

Before VASP 6.4.3, the default algorithm reports the 2D-averaged
potential four grid points from the the minimum 2D-averaged charge
density in the direction of [IDIPOL](IDIPOL.md), i.e., no
averaging is performed along the surface normal of the 2D-averaged
potential.


## Contents


- [1 Use in
  conjunction with the dipole
  correction](#use-in-conjunction-with-the-dipole-correction)
- [2
  Warnings](#warnings)
  - [2.1 Vacuum
    region is likely too
    small](#vacuum-region-is-likely-too-small)
  - [2.2 The
    minimum charge density in your cell may be too
    large](#the-minimum-charge-density-in-your-cell-may-be-too-large)
- [3 Related tags
  and articles](#related-tags-and-articles)


### Use in conjunction with the dipole correction\[<a
href="/wiki/index.php?title=LVACPOTAV&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Use in conjunction with the dipole correction">edit</a> \| (./index.php.md)\]

A typical use case for
LVACPOTAV is together with the
dipole correction (including tags [LDIPOL](LDIPOL.md) and
[IDIPOL](IDIPOL.md)). Switching on the dipole correction is
crucial for determining the vacuum potential; without it, there will be
no field-free region for dipolar systems.

|  |
|----|
| **Mind:** Note that LVACPOTAV is currently implemented for [IDIPOL](IDIPOL.md) between 1 and 3. |

### Warnings\[<a
href="/wiki/index.php?title=LVACPOTAV&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Warnings">edit</a> \| (./index.php.md)\]

In case LVACPOTAV is not able
to generate an accurate work function, the following warnings may be
found in the [OUTCAR](../output-files/OUTCAR.md) file.

#### Vacuum region is likely too small\[<a
href="/wiki/index.php?title=LVACPOTAV&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Vacuum region is likely too small">edit</a> \| (./index.php.md)\]

    |     Did not find any points to average over, which means that no vacuum     |
    |     field-free region was found. Please increase the size of  your cell     |
    |     in the dimension of the dipole correction to obtain accurate            |
    |     workfunction values.                                                    |

A possible solution to this problem is to increase the size of the
vacuum dimension in your cell.

#### The minimum charge density in your cell may be too large\[<a
href="/wiki/index.php?title=LVACPOTAV&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: The minimum charge density in your cell may be too large">edit</a> \| (./index.php.md)\]

    |     The minimum charge density times volume of the cell along the axis      |
    |     of the dipole correction is larger 1E-1, which could mean that your     |
    |     workfunction is not accurate as there is no field free region in        |
    |     your cell. Please consider either increasing the size of your cell      |
    |     along the dipole correction (vacuum dimension) or perhaps               |
    |     increasing the precision of your calculation.                           |

Possible solutions include:

- Making sure you have a large enough vacuum dimension.
- Increasing the precision of your calculation by changing
  [EDIFF](EDIFF.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=LVACPOTAV&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[DIPOL](DIPOL.md), [LDIPOL](LDIPOL.md),
[IDIPOL](IDIPOL.md),
[VACPOTFLAT](VACPOTFLAT.md),
[WRT_POTENTIAL](WRT_POTENTIAL.md),
[LVTOT](LVTOT.md), [LVHAR](LVHAR.md)

[Computing the work
function](../tutorials/Computing_the_work_function.md)



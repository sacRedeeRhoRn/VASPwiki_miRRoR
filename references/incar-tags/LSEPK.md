<!-- Source: https://vasp.at/wiki/index.php/LSEPK | revid: 32854 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSEPK


LSEPK = \[logical\]  
Default: **LSEPK** = .FALSE. 

Description: Specifies whether the
<a href="/wiki/Band-decomposed_charge_densities" class="mw-redirect"
title="Band-decomposed charge densities">partial charge density</a> is
summed up for all selected **k** points or separated and printed out in
different files.

|  |
|----|
| **Mind:** If the **k** points are separated, each **k** point weight is set to 1. To get the correct results in this case it is necessary to turn off symmetry ([ISYM](ISYM.md) = -1) for the initial ground state calculation and the post-processing partial charge calculation in most cases. However, the correct weight of each **k** point is determined from the [KPOINTS](../input-files/KPOINTS.md) file if all contributions are summed up. |

------------------------------------------------------------------------

If [LPARD](LPARD.md) = .TRUE. the partial charge density is
calculated for a subset of bands and **k** points depending on the
setting of the tags [IBAND](IBAND.md),
[KPUSE](KPUSE.md), [NBMOD](NBMOD.md), and
[EINT](EINT.md). If
LSEPK is set to .TRUE.,
separate PARCHG.ALLB.nk or PARCHG.nb.nk files are created, dependent on
the [LSEPB](LSEPB.md) tag. If
LSEPK = .FALSE., the output is
written to [PARCHG](../output-files/PARCHG.md) or PARCHG.nb.ALLK, again
depending on [LSEPB](LSEPB.md).

Here are four examples to illustrate the interplay of
[LSEPB](LSEPB.md) and
LSEPK. in all cases, the
following settings apply, selecting three specific bands and two **k**
points [`IBAND`](IBAND.md)` = 9 10 11`,
[`NBMOD`](NBMOD.md)` = 3`, and
[`KPUSE`](KPUSE.md)` = 1 34`:

- [`LSEPB`](LSEPB.md)` = .FALSE.`,
  `LSEPK`` = .FALSE.`

|                                                                    |
|--------------------------------------------------------------------|
| **output files:** PARCHG |

- [`LSEPB`](LSEPB.md)` = .TRUE.`,
  `LSEPK`` = .FALSE.`

|  |
|----|
| **output files:** PARCHG.0009.ALLK, PARCHG.0010.ALLK, PARCHG.0011.ALLK |

- [`LSEPB`](LSEPB.md)` = .FALSE.`,
  `LSEPK`` = .TRUE.`

|  |
|----|
| **output files:** PARCHG.ALLB.0001, PARCHG.ALLB.0034 |

- [`LSEPB`](LSEPB.md)` = .TRUE.`,
  `LSEPK`` = .TRUE.`

|  |
|----|
| **output files:** PARCHG.0009.0001, PARCHG.0009.0034, PARCHG.0010.0001, PARCHG.0010.0034, PARCHG.0011.0001, PARCHG.0011.0034 |

|  |
|----|
| **Mind:** If VASP 6.5.0 or later is used, the code is compiled with [HDF5 support](../misc/Makefile.include.md) "Makefile.include"), and [LPARDH5](LPARDH5.md) = .TRUE., all output will be redirected to the [vaspout.h5](../output-files/Vaspout.h5.md) file, where it can be analyzed with <a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a>. |

## Related tags and articles\[<a href="/wiki/index.php?title=LSEPK&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LPARD](LPARD.md), [IBAND](IBAND.md),
[EINT](EINT.md), [NBMOD](NBMOD.md),
[KPUSE](KPUSE.md), [LSEPB](LSEPB.md),
[LPARDH5](LPARDH5.md), [PARCHG](../output-files/PARCHG.md),
[vaspout.h5](../output-files/Vaspout.h5.md),
<a href="/wiki/Band-decomposed_charge_densities" class="mw-redirect"
title="Band-decomposed charge densities">Band-decomposed charge
densities</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSEPB-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/LPARD | revid: 27579 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LPARD


LPARD = \[logical\]  
Default: **LPARD** = .FALSE. 

Description: Determines whether partial (band and/or
**k**-point-decomposed) charge densities are evaluated.

------------------------------------------------------------------------

An LPARD run is a
postprocessing step that requires a pre-converged calculation. It writes
the partial density, or multiple partial charge densities, to one
[PARCHG](../output-files/PARCHG.md) file or several PARCHG.\*.\* files,
depending on the setting of [LSEPB](LSEPB.md) and
[LSEPK](LSEPK.md). If [LPARDH5](LPARDH5.md) =
.TRUE., the output is redirected from [PARCHG](../output-files/PARCHG.md) to
[vaspout.h5](../output-files/Vaspout.h5.md).

|  |
|----|
| **Warning:** The orbitals read from the [WAVECAR](../input-files/WAVECAR.md) file must be converged in a prior VASP run. |

|  |
|----|
| **Warning:** LPARD is not supported for noncollinear calculations ([LNONCOLLINEAR](LNONCOLLINEAR.md)=true). |

There are various ways to divide the partial charge density. You can
pick the contributing bands either by index (refer to
[NBMOD](NBMOD.md) and [IBAND](IBAND.md)) or by
energy range (refer to [EINT](EINT.md)), and select
contributing **k** points through [KPUSE](KPUSE.md).

|  |
|----|
| **Mind:** If only the LPARD tag is set, without any other tags to specify the separation of charge, then the [NBMOD](NBMOD.md) tag defaults to -1. The valence charge density (without the augmentation charges) is then written to the [CHGCAR](../input-files/CHGCAR.md) file, and no other partial charge output is generated. |

## Related tags and articles\[<a href="/wiki/index.php?title=LPARD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBAND](IBAND.md), [EINT](EINT.md),
[NBMOD](NBMOD.md), [KPUSE](KPUSE.md),
[LSEPB](LSEPB.md), [LSEPK](LSEPK.md),
[LPARDH5](LPARDH5.md), [PARCHG](../output-files/PARCHG.md),
[vaspout.h5](../output-files/Vaspout.h5.md),
<a href="/wiki/Band-decomposed_charge_densities" class="mw-redirect"
title="Band-decomposed charge densities">Band-decomposed charge
densities</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPARD-_incategory-Examples)

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/K_MULTIPLY | revid: 35907 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# K_MULTIPLY


K_MULTIPLY = \[integer
array\] 

|  |  |  |
|----|----|----|
| Default: **K_MULTIPLY** | = -1 -1 -1 | if not set in [INCAR](../input-files/INCAR.md) |

Description: K_MULTIPLY sets
the per-direction k-point grid multiplier for downsampling from a denser
[WAVECAR](../input-files/WAVECAR.md)

------------------------------------------------------------------------

K_MULTIPLY specifies the ratio
between the denser k-point grid stored in the
[WAVECAR](../input-files/WAVECAR.md) (or
[vaspwave.h5](../output-files/Vaspwave.h5.md)) and the coarser grid of
the current calculation, for each of the three reciprocal-lattice
directions independently.

When K_MULTIPLY is set,
[LDOWNSAMPLE](LDOWNSAMPLE.md) is automatically set to
[`LDOWNSAMPLE`](LDOWNSAMPLE.md)` = .TRUE.`.

By default, [LDOWNSAMPLE](LDOWNSAMPLE.md) triggers an
automatic search that tries the *same* multiplier in all three
directions. This works for isotropic grids but fails for anisotropic
ones, e.g., when the [WAVECAR](../input-files/WAVECAR.md) contains a
24×24×1 grid and the current calculation uses a 2×2×1 grid (requiring
multipliers 12, 12, 1). In such cases,
K_MULTIPLY must be set
explicitly.

|  |
|----|
| **Tip:** For isotropic grids the automatic search is fast and K_MULTIPLY is not required. Use K_MULTIPLY when the grid ratio differs between directions. |

|  |
|----|
| **Mind:** Available as of VASP 6.6.1 |


## Contents


- [1
  Usage](#usage)
  - [1.1 Single
    value](#single-value)
  - [1.2 Three
    values (anisotropic)](#three-values-anisotropic))
- [2 Related tags
  and articles](#related-tags-and-articles)
- [3
  References](#references)


## Usage\[<a
href="/wiki/index.php?title=K_MULTIPLY&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

### Single value\[<a
href="/wiki/index.php?title=K_MULTIPLY&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Single value">edit</a> \| (./index.php.md)\]

    K_MULTIPLY = 2

The value is replicated to all three directions, equivalent to
`K_MULTIPLY = 2 2 2`.

### Three values (anisotropic)\[<a
href="/wiki/index.php?title=K_MULTIPLY&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Three values (anisotropic)">edit</a> \| (./index.php.md)")\]

    K_MULTIPLY = 12 12 1

Each value specifies the multiplier for the first, second, and third
reciprocal-lattice direction, respectively. This is required when the
dense-to-coarse grid ratio is not the same in every direction.

|  |
|----|
| **Warning:** All values must be positive integers. Providing any number of values other than 1 or 3 will cause an error. |

## Related tags and articles\[<a
href="/wiki/index.php?title=K_MULTIPLY&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LDOWNSAMPLE](LDOWNSAMPLE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-K_MULTIPLY-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=K_MULTIPLY&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]



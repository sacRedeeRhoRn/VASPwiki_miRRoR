<!-- Source: https://vasp.at/wiki/index.php/FMP_DIRECTION | revid: 27503 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FMP_DIRECTION


FMP_DIRECTION = 1 \| 2 \| 3  
Default: **FMP_DIRECTION** = 3 

Description: Index of the lattice vector $\mathbf{a}_i$ along which the temperature gradient is created in the
([Müller-Plathe
method](../tutorials/Müller-Plathe_method.md)).

------------------------------------------------------------------------

FMP_DIRECTION defines the
index of the lattice vector $\mathbf{a}_i$ along which the gradient $\partial T/\partial
\mathbf{a}_i$ is created during the reverse
nonequilibrium molecular-dynamics run using the [Müller-Plathe
method](../tutorials/Müller-Plathe_method.md).

|  |
|----|
| **Mind:** This tag will only be available from VASP 6.4.4 |

## Related tags and articles\[<a
href="/wiki/index.php?title=FMP_DIRECTION&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Müller-Plathe
method](../tutorials/Müller-Plathe_method.md),
[FMP_ACTIVE](FMP_ACTIVE.md),
[FMP_SNUMBER](FMP_SNUMBER.md),
[FMP_SWAPNUM](FMP_SWAPNUM.md),
[FMP_PERIOD](FMP_PERIOD.md)



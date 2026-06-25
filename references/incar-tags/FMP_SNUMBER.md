<!-- Source: https://vasp.at/wiki/index.php/FMP_SNUMBER | revid: 27498 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FMP_SNUMBER


FMP_SNUMBER = integer  
Default: **FMP_SNUMBER** = 10 

Description: Number of slabs perpendicular to the temperature gradient
in the [Müller-Plathe
method](../tutorials/Müller-Plathe_method.md).

------------------------------------------------------------------------

FMP_SNUMBER defines the number
of slabs perpendicular to the lattice vector $\mathbf{a}_i$ along which the gradient $\partial T/\partial
\mathbf{a}_i$ is created during the reverse
nonequilibrium molecular dynamics run using the [Müller-Plathe
method](../tutorials/Müller-Plathe_method.md).

|  |
|----|
| **Mind:** This tag will only be available from VASP 6.4.4 |

## Related tags and articles\[<a
href="/wiki/index.php?title=FMP_SNUMBER&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Müller-Plathe
method](../tutorials/Müller-Plathe_method.md),
[FMP_ACTIVE](FMP_ACTIVE.md),
[FMP_DIRECTION](FMP_DIRECTION.md),
[FMP_SWAPNUM](FMP_SWAPNUM.md),
[FMP_PERIOD](FMP_PERIOD.md)



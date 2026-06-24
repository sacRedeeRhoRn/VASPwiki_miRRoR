<!-- Source: https://vasp.at/wiki/index.php/GGA_COMPAT | revid: 31519 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GGA_COMPAT
GGA_COMPAT = .TRUE. \| .FALSE.  
Default: **GGA_COMPAT** = .TRUE. 

Description: If set to GGA_COMPAT = .*FALSE*., this tag restores the
full lattice symmetry for gradient-corrected functionals.

------------------------------------------------------------------------

[GGA](GGA.md) and [METAGGA](METAGGA.md)
functionals might break the symmetry of the Bravais lattice slightly for
cells that are not primitive cubic cells. The origin of this problem is
subtle and relates to the fact that the gradient field breaks the
lattice symmetry for noncubic lattices. This can be fixed by setting

    GGA_COMPAT = .FALSE.

to apply a spherical cutoff to the gradient field. In other words, the
gradient field, as well as the charge density are set to zero for all
reciprocal lattice vectors $\mathbf{G}$
that exceed a certain cutoff length $\mathbf{G}_{cut}$ before calculating the exchange-correlation
energy and potential. The cutoff $\mathbf{G}_{cut}$ is determined automatically so that the
cutoff sphere is fully inscribed in the parallelepiped defined by the
FFT grid in reciprocal space.

|  |
|----|
| **Mind:** For compatibility reasons with older versions of VASP, the default is GGA_COMPAT=*.TRUE.* However, setting the tag usually changes the energy only in the sub-meV energy range (0.1 meV), and for most results the setting of GGA_COMPAT is insignificant. The most important exception is for the calculation of magnetic anisotropy, for which we strongly recommend GGA_COMPAT=.*FALSE*. |

## Related tags and articles
[GGA](GGA.md), [METAGGA](METAGGA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-GGA_COMPAT-_incategory-Examples)

------------------------------------------------------------------------

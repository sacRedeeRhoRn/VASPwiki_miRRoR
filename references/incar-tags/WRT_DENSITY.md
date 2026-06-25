<!-- Source: https://vasp.at/wiki/index.php/WRT_DENSITY | revid: 34637 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WRT_DENSITY


WRT_DENSITY = string  
Default: **WRT_DENSITY** = None  Description: Select which densities
associated to the local potential are written as a post-processing step.

------------------------------------------------------------------------

WRT_DENSITY can select one or
multiple densities on the real-space grid in the unit cell to be
written, e.g.,

     WRT_POTENTIAL = gradient

or

     WRT_POTENTIAL = density gradient laplacian

It writes the augmented total (core + valence) pseudo densities (charge
and magnetization, their gradient, and their laplacian) that enter the
<a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">XC functional</a> on the plane-wave grid to
[vaspout.h5](../output-files/Vaspout.h5.md) in VASP units. That is
$\AA^{-3}$ for charge and $\mu_B$ for
the magnetization. Correspondingly, $\AA^{-4}$ for
the gradient, etc.

With
[`LWRT_AUGMENTED_DENSITY`](LWRT_AUGMENTED_DENSITY.md)` = F`
the densities can be written without augmentation (compensation
charge=0). Mind that the augmented densities are still used during
<a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> to evaluate
the <a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">XC functional</a> (unlike for the
[MGGA](METAGGA.md) specific tag
[LNOAUGXC](LNOAUGXC.md)).

The output is written to [vaspout.h5](../output-files/Vaspout.h5.md) and
can be accessed by HDF5 command-line tools (h5ls, h5dump).

     h5ls -r vaspout.h5

The above shows the table of contents of
[vaspout.h5](../output-files/Vaspout.h5.md). Depending on the keywords
specified with WRT_DENSITY and
the system it yields

     /results/gradient        Group
     /results/gradient/grid   Dataset {3}
     /results/gradient/structure Group
     /results/gradient/structure/position Group
     /results/gradient/structure/position/direct_coordinates Dataset {SCALAR}
     /results/gradient/structure/position/ion_sha256 Dataset {1}
     /results/gradient/structure/position/ion_types Dataset {1}
     /results/gradient/structure/position/lattice_vectors Dataset {3, 3}
     /results/gradient/structure/position/number_ion_types Dataset {1}
     /results/gradient/structure/position/position_ions Dataset {1, 3}
     /results/gradient/structure/position/scale Dataset {SCALAR}
     /results/gradient/structure/position/system Dataset {SCALAR}
     /results/gradient/values Dataset {12, 20, 20, 20}

The grid density can be increased by choosing a higher value for
[ENCUT](ENCUT.md) or explicitly by [NGXF](NGXF.md),
[NGYF](NGYF.md), [NGZF](NGZF.md).

The first dimension of the datasets in /results/charge_density is 1 for
nonmagnetic calculation, 2 for spin-polarized calculation, and 4 for
noncollinear calculations. For the datasets in /results/gradient the
first dimension is multiplied by three to account for the three
Cartesian directions. The components for the magnetic calculations
correspond to the spinor representation with the scalar part in the
first component and the magnetic part in the second
([ISPIN](ISPIN.md)=2) or $m_1$,
$m_2$ and $m_3$ in the
2nd, 3rd and 4th component
([LNONCOLLINEAR](LNONCOLLINEAR.md)=T) in the basis of
Pauli matrices $\\\sigma_1$,
$\sigma_2$, $\mathbf{\sigma}_3\\$ given by [SAXIS](SAXIS.md).

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

## Related tags and articles\[<a
href="/wiki/index.php?title=WRT_DENSITY&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[WRT_POTENTIAL](WRT_POTENTIAL.md),
[ENCUT](ENCUT.md), [NGXF](NGXF.md),
[NGYF](NGYF.md), [NGZF](NGZF.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-WRT_DENSITY-_incategory-HowTo)



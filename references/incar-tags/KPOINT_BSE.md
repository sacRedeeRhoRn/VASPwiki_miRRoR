<!-- Source: https://vasp.at/wiki/index.php/KPOINT_BSE | revid: 36381 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINT_BSE
KPOINT_BSE = \[integer\] (optionally
\[integer\],\[integer\],\[integer\]) 

Description: KPOINT_BSE specifies the k-point index at which VASP
calculates the dielectric matrix.

------------------------------------------------------------------------

In the simplest form, one can specify

     KPOINT_BSE = index_of_k-point

Select the desired k point from the list of k points in the
[OUTCAR](../output-files/OUTCAR.md) file. Additionally, a shift by an
arbitrary reciprocal lattice vector can be supplied by specifying three
additional integer numbers:

     KPOINT_BSE = index_of_k-point  n1 n2 n3

This allows calculating the dielectric function at a k point outside of
the first Brillouin zone corresponding to

$\mathbf{k} + n_{1} \mathbf{b}_{1}+ n_{2}
\mathbf{b}_{2} + n_{3} \mathbf{b}_{3}$

where $\mathbf{b}_{i}$ are the
reciprocal-lattice vectors of the unit cell.

|  |
|----|
| **Warning:** We strongly recommend using [ANTIRES](ANTIRES.md)=2 for the finite wavevector calculations. The Tamm-Dancoff approximation can lead to unphysical results for the dielectric function at a finite wavevector. |

## Related tags and articles
[BSE calculations](../redirects/BSE_calculations.md),

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-KPOINT_BSE-_incategory-HowTo)

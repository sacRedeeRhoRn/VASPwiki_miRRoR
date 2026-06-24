<!-- Source: https://vasp.at/wiki/index.php/URijkl | revid: 36307 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# URijkl
|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

The URijkl file stores the effectively screened off-center Coulomb
integrals

$U_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf
r}\int {\rm d}{\bf r}' w_{i}^{\*\sigma}({\bf r}) w_{j}^{\sigma}({\bf
r}) U({\bf r},{\bf r}',\omega) w_{k}^{\*\sigma'}({\bf r}'+{\bf R})
w_{l}^{\sigma'}({\bf r}'+{\bf R})$

evaluated at zero frequency ($\omega=0$)
for all lattice vectors **R** commensurate with the selected k-point
grid (see [off-center
interactions](../theory/Constrained–random-phase–approximation_formalism.md)).
The URijkl file contains one block per lattice vector. Each block header
gives the lattice vector index and its fractional coordinates. The
columns I, J, K, L are the Wannier function indices; RE and IM are the
real and imaginary parts. The format is as follows:

     # U_ijkl = [ij,R|kl,0] 
     #  I   J   K   L          RE(V_IJKL)          IM(V_IJKL)
     # R:    1  0.000000  0.000000  0.000000
        1   1   1   1        4.3457689208        0.0000000000
        2   1   1   1        0.0000021313        0.0000001349
      ... 
     # R:    2  0.000000  0.000000  1.000000
        1   1   1   1        1.2535567886        0.0000000000
        2   1   1   1        0.0324545667       -0.0000455665
      ...

The Coulomb integrals are computed and written as a post-processing step
using [`ALGO`](../incar-tags/ALGO.md)` = 2e4wa`. The process differs for the
two types of integrals:

- [VRijkl](VRijkl.md) (bare off-center Coulomb integrals):
  Always written when requested.
- URijkl: Only written if all
  [WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) files matching
  the selected k-point grid are present in the working directory.

The basis set for these calculations can be specified using
[LOCALIZED_BASIS](../theory/LOCALIZED_BASIS.md) tag.

Evaluating Coulomb integrals can be computationally intensive,
especially when dealing with a large number of basis functions.

|  |
|----|
| **Tip:** To improve performance, use a coarser sub-grid of the original **k**-point grid by enabling [`LDOWNSAMPLE`](../incar-tags/LDOWNSAMPLE.md)` = T`. |

## Related tags and articles
[Constrained–random-phase–approximation
formalism](../theory/Constrained–random-phase–approximation_formalism.md)

Files: [VIJKL](VIJKL.md), [UIJKL](UIJKL.md),
[VRijkl](VRijkl.md)

Tags: [LTWO_CENTRE](../incar-tags/LTWO_CENTRE.md),
[LOCALIZED_BASIS](../theory/LOCALIZED_BASIS.md),
[ALGO](../incar-tags/ALGO.md)

<!-- Source: https://vasp.at/wiki/index.php/VRijkl | revid: 36306 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VRijkl
|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

The VRijkl file is written for [`ALGO`](../incar-tags/ALGO.md)` = 2e4wa` and
stores all bare off-center Coulomb integrals commensurate with the
selected k-point grid (see [off-center
interactions](../theory/Constrained–random-phase–approximation_formalism.md)):

$V_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf
r}\int {\rm d}{\bf r}' \frac{ w_{i}^{\*\sigma}({\bf r})
w_{j}^{\sigma}({\bf r}) w_{k}^{\*\sigma'}({\bf r}'+{\bf R})
w_{l}^{\sigma'}({\bf r}'+{\bf R})}{|{\bf r}-{\bf r}'|}$

The file contains one block per lattice vector **R**. Each block header
gives the lattice vector index and its fractional coordinates. The
columns I, J, K, L are the Wannier function indices; RE and IM are the
real and imaginary parts. The format is as follows:

     # V_ijkl = [ij,R|kl,0] 
     #  I   J   K   L          RE(V_IJKL)          IM(V_IJKL)
     # R:    1  0.000000  0.000000  0.000000
        1   1   1   1       14.4576272582        0.0000000000
        2   1   1   1        0.0000010313        0.0000031049
      ... 
     # R:    2  0.000000  0.000000  1.000000
        1   1   1   1        4.6546536926        0.0000000000
        2   1   1   1        0.0617934919       -0.0000371600
      ...

A proper [WAVECAR](../input-files/WAVECAR.md) file must be present in the
working directory. The basis can be specified using
[LOCALIZED_BASIS](../theory/LOCALIZED_BASIS.md) tag.

Evaluation of Coulomb integrals can be computationally demanding if the
number of basis functions becomes large.

|  |
|----|
| **Tip:** To improve performance, use a coarser sub-grid of the original **k**-point grid by enabling [`LDOWNSAMPLE`](../incar-tags/LDOWNSAMPLE.md)` = T`. |

## Related tags and articles
[Constrained–random-phase–approximation
formalism](../theory/Constrained–random-phase–approximation_formalism.md)

Files: [VIJKL](VIJKL.md), [UIJKL](UIJKL.md),
[URijkl](URijkl.md)

Tags: [LTWO_CENTRE](../incar-tags/LTWO_CENTRE.md),
[LOCALIZED_BASIS](../theory/LOCALIZED_BASIS.md),
[ALGO](../incar-tags/ALGO.md)

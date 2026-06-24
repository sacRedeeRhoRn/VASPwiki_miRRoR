<!-- Source: https://vasp.at/wiki/index.php/LANCZOSTHR | revid: 31823 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LANCZOSTHR
|  |
|----|
| **Deprecated:** This feature is deprecated and will be removed in a future release. Please use [BSEPREC](BSEPREC.md) instead. |

LANCZOSTHR = \[real\]  
Default: **LANCZOSTHR** = $10^{-3}$ 

Description: LANCZOSTHR is used by the BSE Lanczos algorithm to stop the
iterative procedure, once the dielectric function has reached numerical
convergence.

------------------------------------------------------------------------

The difference between the dielectric function at two consecutive
iterations, $i$ and
$i+1$, is computed as root-mean-square
over the frequency grid

$\mathrm{RMS}\[\epsilon\] =
\sqrt{\sum_{j=1}^N\frac{1}{N}\left\[\epsilon_{i}(\omega_j)-\epsilon_{i+1}(\omega_j)\right\]^2}$

and once $\mathrm{RMS}\[\epsilon\]<=$LANCZOSTHR the iterative algorithm stops.

## Related tag and articles
[BSE](../redirects/BSE.md), [BSE
calculations](../redirects/BSE_calculations.md),
[Bethe-Salpeter
equations](../redirects/Bethe-Salpeter_equations.md)

------------------------------------------------------------------------

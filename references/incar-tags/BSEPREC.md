<!-- Source: https://vasp.at/wiki/index.php/BSEPREC | revid: 31968 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BSEPREC
BSEPREC = Low \| Medium \| High \| Accurate  
Default: **BSEPREC** = Medium 

Description: Determines the precision of the [time-evolution
algorithm](../theory/Category-Bethe-Salpeter_equations.md),
where it controls the timestep and the number of steps, and the
precision of the [Lanczos
algorithms](../theory/Category-Bethe-Salpeter_equations.md),
where it sets the convergence threshold for the dielectric function.

------------------------------------------------------------------------

## Time-evolution algorithm
The timestep in the time-evolution calculation is inversely proportional
to the maximum transition energy [OMEGAMAX](OMEGAMAX.md)
and the number of steps is inversely proportional to the broadening
[CSHIFT](CSHIFT.md). Depending on the BSEPREC stable these
parameters are scaled depending on the precision tag BSEPREC.

|  |  |  |
|:--:|:--:|:--:|
| BSEPREC | [OMEGAMAX](OMEGAMAX.md) | [CSHIFT](CSHIFT.md) |
| Accurate (a) | $\times 4$ | $\times 1/10$ |
| High (h) | $\times 3$ | $\times 1/7.5$ |
| Medium (m) | $\times 2.5$ | $\times1/6.25$ |
| Low (l) | $\times 2$ | $\times1/5$ |

For example, the number of steps $N_{\rm steps}$ for BSEPREC = Low can be found via $N_{\rm steps}=\frac{{\rm OMEGAMAX}\times 2}{{\rm CSHIFT}/5}$

## Lanczos algorithm
|  |
|----|
| **Mind:** Replaces [LANCZOSTHR](LANCZOSTHR.md) as of version 6.5.1 |

The Lanczos algorithm stops once the imaginary part of the dielectric
function computed in two consecutive iterations differs bellow a certain
threshold for the root-mean-square, i.e. once after
$n$ iterations the value of

$\mathrm{RMS}\[\epsilon_n\] =
\sqrt{\frac{1}{N_\omega}\sum_{i=1}^{N_\omega}\left(\Im\[\epsilon_n(\omega_i)\]-\Im\[\epsilon_{n-1}(\omega_i)\]\right)^2}$

is below a certain value defined by **BSEPREC**.

|              |                                                              |
|:------------:|:------------------------------------------------------------:|
|   BSEPREC    | $\mathrm{RMS}\[\epsilon_n\]$ |
| Accurate (a) |          $10^{-5}$           |
|   High (h)   |          $10^{-4}$           |
|  Medium (m)  |          $10^{-3}$           |
|   Low (l)    |          $10^{-2}$           |

To prevent the algorithm from being too slow, the number of frequencies
during the convergence loop is set to $N_\omega$ = INT(SQRT(NOMEGA)), where [NOMEGA](NOMEGA.md) is
set in the [INCAR](../input-files/INCAR.md).

## Related tag and articles
[IBSE](IBSE.md), [NBANDSV](NBANDSV.md),
[NBANDSO](NBANDSO.md), [CSHIFT](CSHIFT.md),
[OMEGAMAX](OMEGAMAX.md)

[BSE calculations](../redirects/BSE_calculations.md)

[Time-dependent density-functional theory
calculations](../methods/Time-dependent_density-functional_theory_calculations.md)

[Bethe-Salpeter
equations](../redirects/Bethe-Salpeter_equations.md)

------------------------------------------------------------------------

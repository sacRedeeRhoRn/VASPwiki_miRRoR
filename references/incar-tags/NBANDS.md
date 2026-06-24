<!-- Source: https://vasp.at/wiki/index.php/NBANDS | revid: 31110 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBANDS
NBANDS = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **NBANDS** | = $\max \left( \frac{1}{2}\operatorname{nint} \left(N_{\mathrm{elect}} + 2\right) + \max\left(\frac{1}{2}N_{\mathrm{ions}}, 3\right), \operatorname{int}\left(\frac{3}{5} N_{\mathrm{elect}}\right) \right)$ |  |

$N_{\mathrm{elect}}$ is
[NELECT](NELECT.md) and $N_{\mathrm{ions}}$ is the number of ions (`NIONS` in
[OUTCAR](../output-files/OUTCAR.md)).

Description: NBANDS specifies the total number of KS or QP orbitals in
the calculation.

------------------------------------------------------------------------

  
The right choice of NBANDS strongly depends on the type of the performed
calculation and the system. As a minimum, VASP requires all occupied
states + one empty band, otherwise, a warning is given.

## Contents

- [1 Electronic minimization](#Electronic_minimization)
- [2 Many-body perturbation theory
  calculations](#Many-body_perturbation_theory_calculations)
- [3 Parallelization](#Parallelization)
- [4 Spin-polarized calculation](#Spin-polarized_calculation)
- [5 Noncollinear calculation](#Noncollinear_calculation)
- [6 Related tags and article](#Related_tags_and_article)

#### Electronic minimization
In the electronic minimization calculations, empty states do not
contribute to the total energy, however, empty states are required to
achieve a better convergence. In iterative matrix-diagonalization
algorithms (see [ALGO](ALGO.md)) eigenvectors close to the top
of the calculated number of states converge much slower than the lowest
eigenstates, thus it is important to choose a sufficiently large NBANDS.
Therefore, we recommend using the default settings for NBANDS, i.e.,
*NELECT/2 + NIONS/2*, which is a safe choice in most cases. In some
cases, it is also possible to decrease it to *NELECT/2+NIONS/4*,
however, in some transition metals with open *f* shells a much larger
number of empty bands might be required (up to *NELECT/2+2\*NIONS*). To
check this parameter perform several calculations for a fixed potential
([ICHARG](ICHARG.md)=12) with an increasing number of bands
(e.g. starting from *NELECT/2 + NIONS/2*). An accuracy of
$10^{-6}$ should be obtained in 10-15
iterations.

|  |
|----|
| **Tip:** Note that the [RMM-DIIS](../theory/RMM-DIIS.md) scheme ([ALGO](ALGO.md)=Fast) is more sensitive to the number of bands than the default Davidson algorithm ([ALGO](ALGO.md)=Normal) and can require more bands for fast convergence. |

#### Many-body perturbation theory calculations
In the Many-Body Perturbation Theory calculations
([*GW*](../methods/Practical_guide_to_GW_calculations.md),[RPA](../methods/RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md),
and [BSE](../redirects/BSE_calculations.md)), a large number of
empty orbitals is usually required, which can be much higher than the
number of occupied states. The convergence of the calculations with a
large number of empty states can be very slow. In such cases, we
recommend performing an exact diagonalization
([ALGO](ALGO.md)=Exact) of the Hamiltonian with empty bands
starting from a converged charge density.

#### Parallelization
When executed on multiple CPUs, VASP automatically increases the number
of bands, so that NBANDS is divisible by the number of CPU cores. If
[NCORE](NCORE.md) \> 1, NBANDS is increased until it is
divisible by the number of cores in a group
([NCORE](NCORE.md)). If [KPAR](KPAR.md) \> 1,
NBANDS is increased until it is divisible by the number of cores in a
group.

#### Spin-polarized calculation
In the case of spin-polarized calculations, the default value for NBANDS
is increased to account for the initial magnetic moments.

#### Noncollinear calculation
In noncollinear calculations, the default NBANDS value is doubled to
account for the spinors components.

## Related tags and article
[NCORE](NCORE.md), NBANDS,
[NBANDSGW](NBANDSGW.md),
[NBANDSV](NBANDSV.md), [NBANDSO](NBANDSO.md),
[NPAR](NPAR.md),[KPAR](KPAR.md)

------------------------------------------------------------------------

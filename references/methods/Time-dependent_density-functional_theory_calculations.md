<!-- Source: https://vasp.at/wiki/index.php/Time-dependent_density-functional_theory_calculations | revid: 37289 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Time-dependent density-functional theory calculations


VASP offers a powerful module for performing time-dependent
density-functional theory (TDDFT) or time-dependent Hartree-Fock (TDHF)
calculations by solving the Casida equation . This approach can be used
for obtaining the frequency-dependent dielectric function with the
excitonic effects and can be based on the ground-state electronic
structure in the DFT, hybrid-functional or even *GW* approximations. You
can watch a lecture covering
<a href="https://youtu.be/arTPHW28qNM" class="external text"
rel="nofollow">TDDFT theory and calculations</a> on our YouTube channel.


## Contents


- [1 From TDDFT (or
  TDHF) to Casida's
  equation](#From_TDDFT_(or_TDHF)_to_Casida's_equation)
- [2 Solving Casida
  equation](#solving-casida-equation)
- [3 Time-dependent
  Hartree-Fock](#time-dependent-hartree-fock)
- [4 Time-dependent
  DFT calculation](#time-dependent-dft-calculation)
- [5 Calculations
  beyond Tamm-Dancoff
  approximation](#calculations-beyond-tamm-dancoff-approximation)
- [6 Calculations
  at finite wavevectors](#calculations-at-finite-wavevectors)
- [7
  References](#references)


## From TDDFT (or TDHF) to Casida's equation\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: From TDDFT (or TDHF) to Casida&#39;s equation">edit</a> \| (./index.php.md) to Casida's equation")\]

In time-dependent density functional theory the electrons follow a
time-dependent Schrödinger equation

$\mathrm i \frac{\partial}{\partial t}\left|\phi_i\[n(t)\]\rangle\right.
= \left\[-\frac{\nabla^2}{2} + V_{\mathrm H}\[n(t)\] +
V_{\mathrm{xc}}\[n(t)\] +
V_\mathrm{ext}(t)\right\]\left|\phi_i\[n(t)\]\rangle\right.,$

where all quantities are now dependent on a time-evolving density,
$n(t)$. The external potential
$V_\mathrm{ext}(t)$ now is explicitly dependent on
time, and which is used to perturb the system away from the ground
state. For time-dependent Hartree-Fock (TDHF) one would only need to
replace the exchange correlation potential, $V_\mathrm{xc}$, with the Fock exchange term,
$V_\mathrm{x}$.

From linear-response theory it is possible to evaluate the change in the
ground-state density due to the external potential,

$\chi(\mathbf 1,2) = \frac{\delta n(1)}{\delta V_\mathrm{ext}(2)},$

or due to the total Kohn-Sham potential

$\chi_0(\mathbf 1,2) = \frac{\delta n(1)}{\delta V_\mathrm{Ks}(2)}.$

Both quantities are related via a Dyson equation. It is possible to show
that

$\frac{\delta V_\mathrm{KS}(1)}{\delta V_\mathrm{ext}(2)} =
\delta(1,2) + \frac{\delta(t_1-t_2)}{|\mathbf r_1 - \mathbf r_2|} +
f_\mathrm{xc}(1,2),$

with $f_\mathrm{xc}(1,2) =
\frac{\delta V_\mathrm{xc}(1)}{\delta n(2)}$ being the
exchange-correlation kernel. This quantity is dependent on the choice
taken to the exchange-correlation energy functional. The application of
a chain rule to $\chi(1,2)$
leads to a Dyson equation

$\chi(1,2) = \chi_0(1,2) +
\chi_0(1,3)\left\[\frac{\delta(t_3-t_4)}{|\mathbf r_3 - \mathbf
r_4|} + f_\mathrm{xc}(3,4)\right\]\chi(4,2).$

While relatively simple, it is easier to solve this equation working
within the frequency domain and in a basis set that considers
transitions from valence to conduction states at the same k-point. The
latter choice comes from the fact that, when dealing with optical
measurements (e.g. absorption), we deal with neutral excitations and the
momentum of the absorbed photons is practically zero. Once all of this
is taken into account, the equation for $\chi(1,2)$ is
recast as an eigenvalue problem

$\left( \begin{matrix} A & B \\ -B^\* & -A^\* \end{matrix} \right) \left(
\begin{matrix} X \\ Y \end{matrix} \right) = \omega \left(
\begin{matrix} X \\ Y \end{matrix} \right),$

which is also known as the Casida equation. The A and B matrices are
given by

$A_{vc}^{v'c'} =
(\varepsilon_v-\varepsilon_c)\delta_{vv'}\delta_{cc'} + \langle
cv'|\frac{1}{|\mathbf r_1-\mathbf r_2|}|vc'\rangle - \langle
cv'|f_\mathrm{xc}(1,2)|c'v\rangle,$

while the B matrix is computed via

$B_{vc}^{v'c'} = \langle vv'|\frac{1}{|\mathbf r_1-\mathbf
r_2|}|cc'\rangle - \langle vv'|f_\mathrm{xc}(1,2)|c'c\rangle.$

The A matrix describes the resonant (excitations) and anti-resonant
(de-excitation) transitions, while the B matrix deals with the coupling
between both. Due to the presence of this coupling, Casida's matrix is
non-Hermitian.

This formalism is very similar to the [Bethe-Salpeter
equation](../theory/Bethe-Salpeter_equation.md), only
now instead of the exchange-correlation self-energy,
$\Sigma_\mathrm{xc}$, and the screened interaction,
$W$, it deals with the exchange-correlation potential,
$V_\mathrm{xc}$, and with the exchange-correlation
kernen, $f_\mathrm{xc}$.

Contrary to the [time-propagation
algorithm](../tutorials/Time-evolution_algorithm.md),
here VASP requires the computation and storage in memory of the A and B
matrices. So, while more robust this algorithm also requires more memory
during its execution. But, it has the added advantage that it can
compute not only the dielectric function, but also the eigenvalues and
eigenvectors of the Casida matrix, which can provide important
information on the nature of the electron-hole pairs that are involved
in the absorption process.

## Solving Casida equation\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory_calculations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Solving Casida equation">edit</a> \| (./index.php.md)\]

The algorithm for solving the Casida equation can be selected by setting
[ALGO](../incar-tags/ALGO.md) = TDHF. This approach is very similar to BSE
but differs in the way the screening of the Coulomb potential is
approximated. The TDHF approach uses the exchange-correlation kernel
$f_{\rm xc}$, whereas BSE requires the
$W(\omega \to 0)$ from a preceding *GW* calculation.
Thus, in order to perform a TDHF calculation, one only needs to provide
the ground-state orbitals ([WAVECAR](../input-files/WAVECAR.md)) and the
derivatives of the orbitals with respect to $k$
([WAVEDER](../input-files/WAVEDER.md)).

|  |
|----|
| **Mind:** Unlike BSE, TDHF calculations do **not** require $W(\omega \to 0)$, i.e., [Wxxxx.tmp](../input-files/Wxxxx.tmp.md) |

In summary, both TDHF and BSE approaches require a preceding
ground-state calculation, however, the TDHF does not need the preceding
*GW* and can be performed with the DFT or hybrid-functional orbitals and
energies.

## Time-dependent Hartree-Fock\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory_calculations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Time-dependent Hartree-Fock">edit</a> \| (./index.php.md)\]

The TDHF calculations can be performed in two steps:

1.  ground-state calculation
2.  optical absorption calculation

For example, an optical absorption calculation of bulk Si can be
performed using a dielectric-dependent hybrid-functional described in
Refs.[^chen2018nonempirical-1][^cui2018doubly-2][^liu2019assessing-3].

    SYSTEM    = Si
    ISMEAR    = 0 
    SIGMA     = 0.05
    NBANDS    = 16      ! or any larger desired value
    ALGO      = D       ! Damped algorithm often required for HF type calculations, ALGO = Normal might work as well
    LHFCALC   = .TRUE. 
    LMODELHF  = .TRUE. 
    AEXX      = 0.083
    HFSCREEN  = 1.22
    LOPTICS   = .TRUE.  ! can also be done in an additional intermediate step

In the second step, the dielectric function is evaluated by solving the
Casida equation

    SYSTEM    = Si
    ISMEAR    = 0 
    SIGMA     = 0.05
    NBANDS    = 16     
    ALGO      = TDHF
    IBSE      = 2
    NBANDSO   = 4       ! number of occupied bands
    NBANDSV   = 8       ! number of unoccupied bands
    LHARTREE  = .TRUE.
    LADDER    = .TRUE.
    LFXC      = .TRUE.
    LMODELHF  = .TRUE. 
    AEXX      = 0.083
    HFSCREEN  = 1.22

THDF calculations can be performed for non-spin-polarized,
spin-polarized, and noncollinear cases, as well as the case with
spin-orbit coupling. There is, however, one caveat. The local
exchange-correlation kernel is approximated by the density-density part
only. This makes predictions for spin-polarized systems less accurate
than for non-spin-polarized systems.

## Time-dependent DFT calculation\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory_calculations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Time-dependent DFT calculation">edit</a> \| (./index.php.md)\]

The TDDFT calculation using the PBE exchange-correlation kernel can be
performed by disabling the ladder diagrams
[LADDER](../incar-tags/LADDER.md) = .FALSE., i.e., only the PBE
exchange-correlation kernel is present in the Hamiltonian.

    SYSTEM    = Si
    ISMEAR    = 0 
    SIGMA     = 0.05
    NBANDS    = 16     
    ALGO      = TDHF
    IBSE      = 2
    NBANDSO   = 4       ! determines how many occupied bands are used
    NBANDSV   = 8       ! determines how many unoccupied (virtual) bands are used
    LFXC      = .TRUE.
    LHARTREE  = .TRUE.
    LADDER    = .FALSE.

|  |
|----|
| **Mind:** In TDDFT calculation, where the ladder diagrams are not included ([LADDER](../incar-tags/LADDER.md)=.FALSE.) or the fraction of exact exchange in the kernel is zero ([AEXX](../incar-tags/AEXX.md)=0), the resulting dielectric function lacks the excitonic effects. |

VASP tries to use sensible defaults, but it is highly recommended to
check the [OUTCAR](../output-files/OUTCAR.md) file and make sure that the
right bands are included. The tag [OMEGAMAX](../incar-tags/OMEGAMAX.md)
specifies the maximum excitation energy of included electron-hole pairs
and the pairs with the one-electron energy difference beyond this limit
are not included in the Hamiltonian.

The calculated frequency-dependent dielectric function, transition
energies and oscillator strength values are stored in the
[vasprun.xml](../output-files/Vasprun.xml.md) file.

## Calculations beyond Tamm-Dancoff approximation\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory_calculations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Calculations beyond Tamm-Dancoff approximation">edit</a> \| (./index.php.md)\]

Calculations beyond Tamm-Dancoff approximation can be performed in the
same manner as in the <a
href="/wiki/BSE_calculations#Calculations_beyond_Tamm-Dancoff_approximation"
class="mw-redirect" title="BSE calculations">BSE</a>.

## Calculations at finite wavevectors\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory_calculations&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculations at finite wavevectors">edit</a> \| (./index.php.md)\]

Calculations at finite wavevectors can be performed in the same manner
as in the
<a href="/wiki/BSE_calculations#Calculations_at_finite_wavevectors"
class="mw-redirect" title="BSE calculations">BSE</a>.

## References\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory_calculations&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^chen2018nonempirical-1]: [W. Chen, G. Miceli, G.M. Rignanese, and A. Pasquarello, *Nonempirical dielectric-dependent hybrid functional with range separation for semiconductors and insulators*, Phys. Rev. Mater. **2**, 073803 (2018).](https://doi.org/10.1103/PhysRevMaterials.2.073803)
[^cui2018doubly-2]: [Z.H. Cui, Y.C. Wang, M.Y. Zhang, X. Xu, and H. Jiang, *Doubly Screened Hybrid Functional: An Accurate First-Principles Approach for Both Narrow- and Wide-Gap Semiconductors* J. Phys. Chem. Lett., **9**, 2338-2345 (2018).](https://doi.org/10.1021/acs.jpclett.8b00919)
[^liu2019assessing-3]: [P. Liu, C. Franchini, M. Marsman, and G. Kresse, *Assessing model-dielectric-dependent hybrid functionals on the antiferromagnetic transition-metal monoxides MnO, FeO, CoO, and NiO*, J. Phys.: Condens. Matter **32**, 015502 (2020).](https://doi.org/10.1088/1361-648x/ab4150)

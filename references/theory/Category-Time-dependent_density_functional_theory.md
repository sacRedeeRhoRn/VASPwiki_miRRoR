<!-- Source: https://vasp.at/wiki/index.php/Category:Time-dependent_density_functional_theory | revid: 37182 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Time-dependent density functional theory


**Time-dependent density-functional theory** (TDDFT) extends
[density-functional
theory](../categories/Category-Exchange-correlation_functionals.md)
to time-varying external potentials, enabling the computation of neutral
electronic excitations and frequency-dependent response functions. The
accuracy of TDDFT strongly depends on the choice of the
exchange-correlation kernel $f_\mathrm{xc}$ ([LFXC](../incar-tags/LFXC.md),
[LADDER](../incar-tags/LADDER.md)) and if the nonlocal limit of
$f_\mathrm{xc}$ is properly treated, excitonic effects
can be captured with good
accuracy[^tal:prr:2020-1].
VASP provides multiple implementations of TDDFT, each with its own
advantages and disadvantages, so that the best algorithm can be selected
based on the problem at hand. The detailed theoretical background is
given on the [theory
page](../methods/Time-dependent_density-functional_theory.md).

- Lecture on
  <a href="https://youtu.be/arTPHW28qNM" class="external text"
  rel="nofollow">TDDFT theory and calculations</a>.


## Contents


- [1 Casida TDDFT
  (ALGO = TDHF)](#Casida_TDDFT_(ALGO_=_TDHF))
  - [1.1 Exact
    diagonalization (IBSE =
    2)](#Exact_diagonalization_(IBSE_=_2))
  - [1.2
    Time-evolution algorithm (IBSE =
    1)](#Time-evolution_algorithm_(IBSE_=_1))
  - [1.3 Lanczos
    algorithm (IBSE = 3)](#Lanczos_algorithm_(IBSE_=_3))
  - [1.4 Scaling
    with the system size](#scaling-with-the-system-size)
- [2 Time-evolution
  or real-time TDDFT (ALGO =
  TIMEEV)](#Time-evolution_or_real-time_TDDFT_(ALGO_=_TIMEEV))
  - [2.1 Scaling
    with the system size](#scaling-with-the-system-size-2)
- [3 Dyson-equation
  TDDFT (ALGO = CHI)](#Dyson-equation_TDDFT_(ALGO_=_CHI))
  - [3.1 Scaling
    with the system size](#scaling-with-the-system-size-2)
- [4 Additional
  resources](#additional-resources)
  - [4.1
    Tutorials](#tutorials)
  - [4.2 How
    to](#how-to)
- [5
  References](#references)


## Casida TDDFT ([`ALGO`](../incar-tags/ALGO.md)` = TDHF`)\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Casida TDDFT (ALGO = TDHF)">edit</a> \| (./index.php.md)")\]

The Casida formulation of TDDFT recasts the linear-response problem as a
non-Hermitian eigenvalue problem

$\left(\begin{array}{cc} \mathbf{A} & \mathbf{B} \\ \mathbf{B}^\* &
\mathbf{A}^\* \end{array}\right)\left(\begin{array}{l}
\mathbf{X}_\lambda \\ \mathbf{Y}_\lambda
\end{array}\right)=\omega_\lambda\left(\begin{array}{cc} \mathbf{1} &
\mathbf{0} \\ \mathbf{0} & -\mathbf{1}
\end{array}\right)\left(\begin{array}{l} \mathbf{X}_\lambda \\
\mathbf{Y}_\lambda \end{array}\right),$

with the same mathematical structure as the [Bethe-Salpeter
equation](Bethe-Salpeter_equation.md)
(BSE). The eigenvalues $\omega_\lambda$ are the excitation energies, and the eigenvectors
$\mathbf{X}_\lambda, \mathbf{Y}_\lambda$ determine the
oscillator strengths and the dielectric function.

VASP provides three algorithms for solving the Casida equation, selected
via [IBSE](../incar-tags/IBSE.md):

### Exact diagonalization ([`IBSE`](../incar-tags/IBSE.md)` = 2`)\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Exact diagonalization (IBSE = 2)">edit</a> \| (./index.php.md)")\]

The Hamiltonian is diagonalized exactly. The excitation energies and
oscillator strengths are obtained directly from the eigenvalues and
eigenvectors, which makes this approach particularly useful for
analyzing individual excitons. The macroscopic dielectric function is
obtained from the spectral representation:

$\varepsilon_M(\omega) = 1 - \frac{4\pi}{\Omega} \sum_\lambda
\left|\sum_{cv\mathbf k} \mu_{cv\mathbf k} X_\lambda^{cv\mathbf
k}\right|^2 \left\[\frac{1}{\omega - \omega_\lambda + \mathrm i\eta} -
\frac{1}{\omega + \omega_\lambda + \mathrm i\eta}\right\],$

where $\mu_{cv\mathbf{k}}^j=\frac{\langle
c\mathbf{k}|v_j|v\mathbf{k}\rangle}{\varepsilon_c(\mathbf{k})-\varepsilon_v(\mathbf{k})}$ is the dipole matrix element,
$X_\lambda^{cv\mathbf k}$ are the eigenvector
components, and $\omega_\lambda$ are the excitation energies.

### Time-evolution algorithm ([`IBSE`](../incar-tags/IBSE.md)` = 1`)\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Time-evolution algorithm (IBSE = 1)">edit</a> \| (./index.php.md)")\]

This algorithm is based on the same time-evolution approach described in
the [real-time TDDFT
section](#Time-evolution_or_real-time_TDDFT_(ALGO=TIMEEV)), but applied
within the Casida framework. The key difference is that the Hamiltonian
in transition space is built once and never updated during the
propagation. Only the time-dependent dipole vector
$|\mu_{cv\mathbf k}(t)\rangle$ is propagated forward
in time using the fixed Hamiltonian.

The dielectric function is found via a Fourier
transform[^sander:jcp:2017-2]:

$\varepsilon_M(\omega)=1-\frac{4\pi}{\Omega}\int_0^{\infty} \mathrm{d} t
\sum_{c,v,\mathbf{k}}\left(\langle\mu_{cv\mathbf{k}}|
\xi_{cv\mathbf{k}}(t)\rangle + \mathrm{c.c.}\right) e^{-\mathrm
i(\omega-\mathrm i \eta) t},$

where $\mu_{cv\mathbf k}$ are the dipole moments and $|\xi_{cv\mathbf k}(t)\rangle$ is the time-evolved dipole vector. The solution is
strictly equivalent to that of the exact diagonalization for the
dielectric function.

### Lanczos algorithm ([`IBSE`](../incar-tags/IBSE.md)` = 3`)\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Lanczos algorithm (IBSE = 3)">edit</a> \| (./index.php.md)")\]

The dielectric function is expressed as a continued fraction

$\varepsilon_M(\omega) = 1 -
\frac{4\pi}{\Omega}\cfrac{|u_0|^2}{(\omega - a_1 + \mathrm i\eta) -
\cfrac{b_1^2}{(\omega -a_2 + \mathrm i\eta) - \cfrac{b_2^2}{...}}},$

where $|u_0\rangle$
is an initial guess vector computed from the dipole moments. The
$a$ and $b$
coefficients are evaluated iteratively, with the algorithm stopping once
the difference between $\varepsilon(\omega)$ from two consecutive iterations is below a threshold
selected by [BSEPREC](../incar-tags/BSEPREC.md).

### Scaling with the system size\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Scaling with the system size">edit</a> \| (./index.php.md)\]

Building the Hamiltonian scales as $N^4$–$N^5$ with the
system size. Solving the equation scales as $N^6$ for
exact diagonalization ([`IBSE`](../incar-tags/IBSE.md)` = 2`) and
$N^4$ for the time-evolution
([`IBSE`](../incar-tags/IBSE.md)` = 1`) and Lanczos
([`IBSE`](../incar-tags/IBSE.md)` = 3`) algorithms.

## Time-evolution or real-time TDDFT ([`ALGO`](../incar-tags/ALGO.md)` = TIMEEV`)\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Time-evolution or real-time TDDFT (ALGO = TIMEEV)">edit</a> \| (./index.php.md)")\]

An alternative to solving the Casida equation is to compute the
frequency-dependent response via real-time propagation of the Kohn-Sham
orbitals
[^sander:jcp:2017-2].
The starting point is the time-dependent Kohn-Sham equation,

$\mathrm i \frac{\partial}{\partial t}\left|\phi_{v\mathbf
k}\[n(t)\]\right\rangle = \left\[-\frac{\nabla^2}{2} + V_{\mathrm
H}\[n(t)\] + V_{\mathrm{xc}}\[n(t)\] +
V_\mathrm{ext}(t)\right\]\left|\phi_{v\mathbf
k}\[n(t)\]\right\rangle,$

where all potentials are functionals of the time-evolving density
$n(\mathbf r, t)$. A delta-like perturbation is applied
to the ground-state system, and the time-dependent coefficients are
propagated forward in time. The dielectric function is then obtained
from the Fourier transform of the time-dependent dipole moments:

$\varepsilon_M(\omega) = 1 - \frac{4\pi e^2}{\Omega} \int_0^\infty
\mathrm d t \sum_{cv\mathbf k} \left(\langle\mu_{cv\mathbf
k}|c_{cv\mathbf k}(t)\rangle + \mathrm{c.c.}\right) e^{-\mathrm
i(\omega - \mathrm i\eta)t},$

where $\mu_{cv\mathbf{k}}$ is the dipole matrix element and
$c_{cv\mathbf k}(t)$ are the time-dependent expansion
coefficients. This approach avoids building and storing the full
Hamiltonian in transition space. The detailed theory and propagation
algorithm are described on the [theory
page](../methods/Time-dependent_density-functional_theory.md).

### Scaling with the system size\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Scaling with the system size">edit</a> \| (./index.php.md)\]

The compute time per time step scales as $N^3$ with the
system size. When nonlocal exchange is included
([LADDER](../incar-tags/LADDER.md)=.TRUE.), an additional
$N_{\mathbf{k}}^2 \times N_v^2 \times N_G$ contribution
arises from evaluating the exchange integrals at each time step.

## Dyson-equation TDDFT ([`ALGO`](../incar-tags/ALGO.md)` = CHI`)\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Dyson-equation TDDFT (ALGO = CHI)">edit</a> \| (./index.php.md)")\]

Instead of recasting the problem as an eigenvalue equation, TDDFT can
also be solved by directly evaluating the two-point Dyson equation for
the density-density response function $\chi$. The
macroscopic dielectric function is then obtained from

$\varepsilon_M(\omega) = 1 - v(\mathbf{G}=0) \\
\chi_{\mathbf{G}=0,\mathbf{G}'=0}(\mathbf{q},\omega),$

where $v(\mathbf{G})$ is the Coulomb kernel and $\chi_{\mathbf{G},\mathbf{G}'}(\mathbf{q},\omega)$ is
the interacting response function in reciprocal space. This approach
gives access to the full matrix $\chi_{\mathbf{G},\mathbf{G}'}(\mathbf{q},\omega)$ and
is used, for instance, to compute the screened Coulomb interaction
$W$ needed in *GW* calculations. However, the Dyson
equation must be inverted at every frequency point, which makes it
expensive for computing spectra with fine resolution. The only nonlocal
exchange-correlation kernel currently supported is the nanoquanta kernel
([LFXC](../incar-tags/LFXC.md)).

### Scaling with the system size\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Scaling with the system size">edit</a> \| (./index.php.md)\]

The compute time scales as $N^4$ with the
system size. The Dyson equation must be inverted at every frequency
point ([NOMEGA](../incar-tags/NOMEGA.md)), so the total cost grows
linearly with the number of frequency points.

## Additional resources\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Tutorials\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial calculating optical absorption of C diamond using
  <a href="https://www.vasp.at/tutorials/latest/bse/part1/#BSE-e03"
  class="external text" rel="nofollow">TDDDH</a>.
- Tutorial on the
  <a href="https://www.vasp.at/tutorials/latest/bse/part3/#BSE-e09"
  class="external text" rel="nofollow">efficient Brillouin zone
  sampling</a> using TDDDH and
  <a href="https://www.vasp.at/tutorials/latest/bse/part3/#BSE-e10"
  class="external text" rel="nofollow">exciton analysis</a> using TDDDH.

### How to\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

- Practical guide for solving the Casida equation via diagonalization:
  <a href="/wiki/TDDFT_calculations" class="mw-redirect"
  title="TDDFT calculations">TDDFT calculations</a>.
- Practical guide for real-time TDDFT calculations: [Time-evolution
  algorithm](../tutorials/Time-evolution_algorithm.md).

## References\[<a
href="/wiki/index.php?title=Category:Time-dependent_density_functional_theory&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^tal:prr:2020-1]: [A. Tal, P. Liu, G. Kresse, A. Pasquarello, *Accurate optical spectra through time-dependent density functional theory based on screening-dependent hybrid functionals*, Phys. Rev. Research *2*, 032019 (2020)](http://doi.org/10.1103/PhysRevResearch.2.032019)
[^sander:jcp:2017-2]: [T. Sander, G. Kresse, *Macroscopic dielectric function within time-dependent density functional theory—Real time evolution versus the Casida approach* , J. Chem. Phys. *146*, 064110 (2017)](http://doi.org/10.1063/1.4975193)

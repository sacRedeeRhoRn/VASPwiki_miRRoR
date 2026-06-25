<!-- Source: https://vasp.at/wiki/index.php/Time-evolution_algorithm | revid: 35077 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Time-evolution algorithm


The <a href="/wiki/Dielectric_properties" class="mw-redirect"
title="Dielectric properties">macroscopic dielectric function</a>,
$\epsilon_{ij}(\omega)$, measures how a given
dielectric medium reacts when subject to an external electric field.
From $\epsilon_{ij}(\omega)$ it is possible to extract several optical properties
such as absorption, optical conductivity, and reflectance. However, it
is important that the interacting electrons and holes are taken into
account. This makes the evaluation of the macroscopic dielectric
function more involved, since it goes beyond the single-particle level,
working at the two-particle level via either the
<a href="/wiki/Bethe-Salpeter_equations" class="mw-redirect"
title="Bethe-Salpeter equations">Bethe-Salpeter equation</a> (BSE) or
time-dependent density-functional theory (TDDFT).

For both frameworks, BSE and TDDFT, users can select two different
strategies to compute $\epsilon_{ij}(\omega)$. The first is based on the eigendecomposition of the
electron-hole hamiltonian, $H^\mathrm{exc}$<sup>[\[1\]](#cite_note-sander:prb:15-1)</sup>.
It allows for the evaluation of $\epsilon_{ij}(\omega)$ by initially obtaining the eigenvalues and
eigenvectors of $H^\mathrm{exc}$ and then using both to evaluate
$\epsilon_{ij}(\omega)$. This strategy is based on the
<a href="/wiki/Bethe-Salpeter_equations" class="mw-redirect"
title="Bethe-Salpeter equations">Bethe-Salpeter equation</a> or the
[Casida
equation](../methods/Time-dependent_density-functional_theory_calculations.md).
The second strategy transforms the mathematical expression of
$\epsilon_{ij}(\omega)$ into a time-dependent
integral<sup>[\[2\]](#cite_note-sander:jcp:2017-2)</sup>.
By propagating the dipolar moments in time and then applying a Fourier
transform, VASP can compute $\epsilon_{ij}(\omega)$.

The advantage of the later method in relation to the former is related
to their cost. The time-dependent integral has a cost of the order
$O(N^2)$, while the eigendecomposition has a cost of the
order $O(N^3)$,
where $N$ is the
rank of $H^\mathrm{exc}$. This means that for very large numbers of bands or
k-points, the time-dependent formalism is cheaper than the
eigendecomposition method.

Below is a brief description of the time-dependent method, from its
theoretical support to how calculations should be performed, with the
relevant approximations needed in the two-particle Hamiltonian.

|  |
|----|
| **Warning:** In VASP \< 6.6.0 the dielectric function is not calculated correctly with [ALGO](../incar-tags/ALGO.md)=TIMEEV if [ISYM](../incar-tags/ISYM.md)\>0. |


## Contents


- [1 The TDDFT
  Schrödinger equation](#the-tddft-schrödinger-equation)
- [2 The
  macroscopic-dielectric function as a time-dependent
  integral](#the-macroscopic-dielectric-function-as-a-time-dependent-integral)
- [3 Perturbing all
  transitions with a delta-like
  potential](#perturbing-all-transitions-with-a-delta-like-potential)
- [4 The many-body
  terms in the
  hamiltonian](#the-many-body-terms-in-the-hamiltonian)
  - [4.1
    Independent-particle
    approximation](#independent-particle-approximation)
  - [4.2 Hartree
    exchange potential](#hartree-exchange-potential)
  - [4.3 Screened
    two-particle interaction](#screened-two-particle-interaction)
    - [4.3.1
      Exchange-correlation effects from
      time-dependent density functional
      theory](#exchange-correlation-effects-from-time-dependent-density-functional-theory)
    - [4.3.2 Ladder
      diagrams from many-body perturbation
      theory](#ladder-diagrams-from-many-body-perturbation-theory)
- [5 Step-by-step
  instructions on bulk Si](#step-by-step-instructions-on-bulk-si)
  - [5.1 Step 1:
    ground state with extra empty
    states](#step-1-ground-state-with-extra-empty-states)
  - [5.2 Step 2:
    time-evolution run](#step-2-time-evolution-run)
    - [5.2.1
      Setting up the
      bands](#setting-up-the-bands)
    - [5.2.2
      Setting up the
      time-step](#setting-up-the-time-step)
    - [5.2.3
      Choosing the direction of
      perturbation](#choosing-the-direction-of-perturbation)
  - [5.3 Analysing
    the results](#analysing-the-results)
- [6 Comparison to
  other methods](#comparison-to-other-methods)
  - [6.1
    Bethe-Salpeter
    equation](#bethe-salpeter-equation)
  - [6.2 Casida
    equation](#casida-equation)
- [7 Related tags
  and articles](#related-tags-and-articles)
- [8
  References](#references)


## The TDDFT Schrödinger equation\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: The TDDFT Schrödinger equation">edit</a> \| (./index.php.md)\]

Much like in density-functional theory, there is an equivalent
time-dependent equivalent called time-dependent density functional
theory where each electron follows a time-dependent equation

$\mathrm i \frac{\partial}{\partial t}\left|\phi_i\[n(t)\]\rangle\right.
= \left\[-\frac{\nabla^2}{2} + V_{\mathrm H}\[n(t)\] +
V_{\mathrm{xc}}\[n(t)\] +
V_\mathrm{ext}\[n(t)\]\right\]\left|\phi_i\[n(t)\]\rangle\right.,$

but now all quantities are functionally dependent on a time-evolving
density, $n(t)$.
Through the use of linear-response formalism this equation can be
brought into a matrix equation. However, this involves the computation
and storage of large matrices. To circumvent this issue it is possible
to evolve the starting ground state under a perturbative potential that
probes all possible excitations (see more below).

Taking the following ansatz for the time-dependent wave-function,

$\left|\phi_i(t)\right\rangle=\left\\\left|\phi_i^0\right\rangle+\lambda\sum_{a
\in \mathrm{unocc} .} c_{a i}(t)\left|\phi_a^0\right\rangle\right\\
e^{-i \varepsilon_i t},$

one can compute the changes in an initial, occupied state
$|\phi_i^0\rangle$ as time-dependent contributions from
unoccupied states. In this way the original problem is recast as the
propagation in time of the coefficients $c_{a i}(t)$,
with the starting point being $\left|\phi_i(0)\right\rangle
= \left|\phi_i^0)\right\rangle$.

In essence, the time-dependent algorithm implemented in VASP works as
follows:

1.  Setup states at time step $t_n$
2.  Update time-dependent hamiltonian $H\[\left|\phi_i(t)\right\rangle\]$
3.  Calculate the change in time-dependent coefficients
    $\delta c_{a
    i}\left(t_n\right) = \left\langle\phi_a^0\right|
    H\left\\\phi_i\left(t_n\right)\right\\\left|\phi_i\left(t_n\right)\right\rangle$
4.  Compute the coefficients at the next time-step
    $c_{a
    i}\left(t_{n+1}\right)=c_{a i}\left(t_{n-1}\right)+2 i \Delta t
    \delta c_{a i}\left(t_n\right)$,

where $\Delta t$ is
the time step chosen for the propagation. Updating the hamiltonian with
the new states is an essential step, as it is now a functional of the
time-dependent density.

The remaining step is to prove that the computation of the dielectric
function can be recast as a time-dependent problem. This is shown in the
next section.

## The macroscopic-dielectric function as a time-dependent integral\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: The macroscopic-dielectric function as a time-dependent integral">edit</a> \| (./index.php.md)\]

The starting point is that one can re-write $\epsilon_{ij}(\omega)$ as a time-dependent
integral<sup>[\[3\]](#cite_note-schmidt:prb:2003-3)</sup>.
It starts from its expression, given by

$\epsilon^M(\omega)=1+\frac{4 \pi}{\Omega_0} \sum_\lambda\left|\sum_{c
v \mathbf{k}} \mu_{c v \mathbf{k}} A_{c v
\mathbf{k}}^\lambda\right|^2\left\[\frac{1}{\omega+E_\lambda+\mathrm{i}
\eta}-\frac{1}{\omega-E_\lambda+\mathrm{i} \eta}\right\]$,

where $\mu_{v c
\mathbf{k}}^j=\frac{\left\langle c \mathbf{k}\left|v_j\right| v
\mathbf{k}\right\rangle}{\varepsilon_c(\mathbf{k})-\varepsilon_v(\mathbf{k})}$ is the dipolar moment associated to the the conduction
$c$, valence band $v$, and
k-point $k$.
$\lambda$ is the index of the eigenstate of
$H^\mathrm{exc}$, with $A^\lambda$
and $E_\lambda$
being the associated eigenvector and eigenvalue.

This definition of $\epsilon_{ij}(\omega)$ can be brought into operational form

$\epsilon^M(\omega)=1+\frac{4
\pi}{\Omega_0}\left\langle\mu\left|\left\[\frac{1}{\omega+\mathrm{i}
\eta+\hat{H}^{\mathrm{exc}}}-\frac{1}{\omega+\mathrm{i}
\eta-\hat{H}^{\mathrm{exc}}}\right\]\right| \mu\right\rangle$

by using the spectral decomposition $\left\[\hat{H}^{\mathrm{exc}}-\omega\right\]^{-1}=\sum_\lambda
\frac{\left|A_\lambda\right\rangle\left\langle
A_\lambda\right|}{E_\lambda-\omega}$. The new
expression of $\epsilon(\omega)$ is related to a time-dependent integral, using the
fact that

$\frac{1}{\omega+\mathrm{i}
\eta-\hat{H}^{\mathrm{exc}}}|\mu\rangle=-\mathrm{i} \int_0^{\infty}
e^{-\mathrm{i}\left(\omega-\hat{H}^{\mathrm{exc}}+\mathrm{i} \eta\right)
t}|\mu\rangle=-\mathrm{i} \int_0^{\infty}
e^{-\mathrm{i}(\omega+\mathrm{i} \eta) t} e^{\mathrm{i}
\hat{H}^{\mathrm{exc}}t}|\mu\rangle$,

and recognizing that $e^{\mathrm{i}
\hat{H}^{\mathrm{exc}}t}|\mu\rangle = |\xi(t)\rangle$
is the exponential form of a time-dependent equation operator. These
considerations allow for the expression of $\epsilon_{ij}(\omega)$ to be written as

$\epsilon_{ij}(\omega)=\delta_{ij}-\frac{4\pi
e^2}{\Omega}\int_0^{\infty} \mathrm{d} t
\sum_{c,v,\mathbf{k}}\left(\langle\mu^j_{cv\mathbf{k}}|
\xi^i_{cv\mathbf{k}}(t)\rangle+ \mathrm{c.c.}\right) e^{-\mathrm
i(\omega-\mathrm i \eta) t}$.

The fundamental aspect behind this transformation is that the new,
time-dependent vector $\left.\mid
\xi^j(t)\right\rangle$ follows the equation

$\mathrm i \frac{\mathrm d}{\mathrm d
t}\left|\xi^j(t)\right\rangle=\hat{H}^\mathrm{exc}(t)\left|\xi^j(t)\right\rangle,$

with the initial vector given by $\left|\xi^j(0)\right\rangle=\left|\mu^j\right\rangle$.

To compute the dielectric function with this method, VASP evaluates and
stores at each time step the projections of $\left.\mid
\xi^j(t)\right\rangle$ over $\left.\mid \mu^i\right\rangle$, $c^{ij}_{cv\mathbf k}(t) =
\langle \mu^i_{cv\mathbf k}|\xi^i_{cv\mathbf k}(t)\rangle$. It is the fact that all these operations are of the
matrix-vector type that makes this method having a cost of the order of
$O(N^2)$.

## Perturbing all transitions with a delta-like potential\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Perturbing all transitions with a delta-like potential">edit</a> \| (./index.php.md)\]

In order to probe all possible $v\to c$
transitions, a time-dependent term is added to the
hamiltonian<sup>[\[2\]](#cite_note-sander:jcp:2017-2)</sup>

$V_\mathrm{ext}(\mathbf r, t) = \lambda \mathbf r\cdot \mathbf
D\delta(t),$

where $\lambda$ is
the perturbation strength parameter and $\mathbf D$ is
the electric displacement field. The narrow (in time) potential allows
all bands in the occupied and unoccupied manifolds to be included in the
transition space. The constant displacement field replicates the long
wavelength limit (i.e. $\mathbf q \to 0$).

## The many-body terms in the hamiltonian\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: The many-body terms in the hamiltonian">edit</a> \| (./index.php.md)\]

Approximations to the interaction between electrons and holes are
controlled in the [INCAR](../input-files/INCAR.md) by the tags
[LHARTREE](../incar-tags/LHARTREE.md), [LADDER](../incar-tags/LADDER.md),
and [LFXC](../incar-tags/LFXC.md), which can be set to either .TRUE. or
.FALSE.. Below we provide an explanation of what interaction term each
tag controls.

|  |
|----|
| **Mind:** The default setup for VASP is LHARTREE and LADDER set to .FALSE., while LFXC is set to .TRUE.. This means that if no tags are set in the INCAR the time-propagation run will using the TDDFT kernel. |

### Independent-particle approximation\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Independent-particle approximation">edit</a> \| (./index.php.md)\]

In this approximation all interaction terms in the hamiltonian are
turned off by setting [LHARTREE](../incar-tags/LHARTREE.md),
[LADDER](../incar-tags/LADDER.md), and [LFXC](../incar-tags/LFXC.md) to
.FALSE. in the [INCAR](../input-files/INCAR.md) file. This means that the
computed spectrum will be equal the one obtained during a ground-state
calculation with [LOPTICS](../incar-tags/LOPTICS.md)=.TRUE.. This
calculation is useful to test if everything is in order with the input
files and the workflow is properly setup.

### Hartree exchange potential\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Hartree exchange potential">edit</a> \| (./index.php.md)\]

With the tag [LHARTREE](../incar-tags/LHARTREE.md)=.TRUE. the
interaction terms in the hamiltonian will include the unscreened Coulomb
exchange. These terms are also known as the bubble diagrams from
many-body perturbation theory (MBPT). With both
[LFXC](../incar-tags/LFXC.md) and [LADDER](../incar-tags/LADDER.md) set to
.FALSE., this will be equivalent to running random-phase approximation
(RPA) calculation.

Note that at the end, the dielectric function reported in the output
files is the macroscopic dielectric function, where no contributions
from local fields (i.e. terms with finite $\mathbf G$)
are included.

The missing interaction between electrons and holes from either
[LFXC](../incar-tags/LFXC.md) or [LADDER](../incar-tags/LADDER.md) has as
consequence that bound excitons cannot be properly described, which is a
known problem of RPA. However, it can still be used to compute the
electron energy-loss function, <a
href="/wiki/Dielectric_properties#Electron_energy_loss_spectroscopy_(EELS)"
class="mw-redirect" title="Dielectric properties">EELS</a>.

### Screened two-particle interaction\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Screened two-particle interaction">edit</a> \| (./index.php.md)\]

#### Exchange-correlation effects from time-dependent density functional theory\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Exchange-correlation effects from time-dependent density functional theory">edit</a> \| (./index.php.md)\]

Setting [LFXC](../incar-tags/LFXC.md)=.TRUE. includes the local
exchange-correlation kernel, $f_\mathrm{xc}$ in the time-propagation

$f_{\mathrm{xc}}^{\text {loc }}\left(\mathbf{r},
\mathbf{r}^{\prime}\right)=\frac{\delta^2\left\\E_{\mathrm{c}}^{\mathrm{DFT}}+\left(1-c_{\mathrm{x}}\right)
E_{\mathrm{x}}^{\mathrm{DFT}}\right\}{\delta \rho(\mathbf{r}) \delta
\rho\left(\mathbf{r}^{\prime}\right)},$

where $c_X$ controls
the fraction of the exchange energy functional that is included in the
kernel (see [AEXX](../incar-tags/AEXX.md)). This lets users perform
time-dependent calculations using hybrid functionals.

These kernels often lack the long-range component (which goes as
$-1/q^2$, where $q$ is the
momentum difference between the electron and the hole). When using them
in periodic or extended systems it is very likely that they will fail to
properly reproduce the binding energies of electron-hole pairs.

#### Ladder diagrams from many-body perturbation theory\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Ladder diagrams from many-body perturbation theory">edit</a> \| (./index.php.md)\]

By setting [LADDER](../incar-tags/LADDER.md)=.TRUE. the interaction
hamiltonian will include the screened exchange interaction potential,
$W(\mathbf r,\mathbf r';\omega)$. This treats the
electron-hole interaction by including the ladder diagrams from
MBPT<sup>[\[1\]](#cite_note-sander:prb:15-1)</sup>.
This term also has the correct long-range behaviour, meaning that it can
properly describe bound electron-hole pairs in solids and large
molecules.

At the present, the screened interaction has to be computed from a
[model dielectric
function](../misc/Improving_the_dielectric_function.md),
given by

${\varepsilon}_{\mathbf{G},\mathbf{G}}^{-1}(\mathbf{q})=1-(1-{{\varepsilon}_{\infty}^{-1}})\text{exp}\left(-\frac{|\mathbf{q+G}|^2}{4{\lambda}^2}\right)$.

Both [LHFCALC](../incar-tags/LHFCALC.md) and
[LMODELHF](../incar-tags/LMODELHF.md) must be set to .TRUE.. Also, VASP
must be provided both with [HFSCREEN](../incar-tags/HFSCREEN.md)
($\lambda$) and [AEXX](../incar-tags/AEXX.md)
(${\varepsilon}_{\infty}^{-1}$) to control the range
separation parameters in the model dielectric function.

## Step-by-step instructions on bulk Si\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions on bulk Si">edit</a> \| (./index.php.md)\]

### Step 1: ground state with extra empty states\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: ground state with extra empty states">edit</a> \| (./index.php.md)\]

The starting point is a ground-state calculation which includes extra
empty states, whose number is controlled in the
[INCAR](../input-files/INCAR.md) file with the tag
[NBANDS](../incar-tags/NBANDS.md). In the following example
[INCAR](../input-files/INCAR.md) file

    SYSTEM = Si
    NBANDS = 12
    ISMEAR = 0 ; SIGMA = 0.05
    ALGO = N
    LOPTICS = .TRUE.
    KPAR = 4

8 empty bands are chosen (silicon has 4 occupied bands in the
pseudo-potential file, thus making a total of 12 bands for
[NBANDS](../incar-tags/NBANDS.md)). However, with
[ALGO](../incar-tags/ALGO.md)=N, VASP will employ an iterative
diagonalization algorithm, meaning that the last conduction states will
not be converged with the same accuracy level as the occupied states. It
is possible to avoid this by setting [ALGO](../incar-tags/ALGO.md)=Exact, or
by increasing the number of bands to make sure that the states which
will be used in the time-propagation step are converged with the same
level of accuracy.

Finally, with [LOPTICS](../incar-tags/LOPTICS.md)=.TRUE., VASP will
compute the dipole momentum for each possible
$v\to c$ transition (recall the definition of the dipole
momentum vector). These are written in the file
[WAVEDER](../input-files/WAVEDER.md), which will be used in the next step.

|  |
|----|
| **Mind:** This calculation was performed on bulk Si (primitive cell), with a gamma-centred, 4x4x4 k-point grid, using the PBE standard pseudopotential. |

### Step 2: time-evolution run\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: time-evolution run">edit</a> \| (./index.php.md)\]

Once the ground state with extra empty states is computed, the resulting
[WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files are ready to use in a
time-propagation calculation. The following will be used as an example
[INCAR](../input-files/INCAR.md) file:

    SYSTEM = Si
    ALGO = TIMEEV
    !Information about the bands
    NBANDS = 12
    NBANDSO = 4
    NBANDSV = 8
    !Smearing parameters
    ISMEAR = 0 ; SIGMA = 0.05
    !Direction of propagation
    IEPSILON = 1 
    !Parallelization options
    KPAR = 4
    !Time-propagation parameters
    NELM = 2000
    CSHIFT = 0.1
    OMEGAMAX = 20
    !Particle interactions
    LHARTREE = .TRUE.
    LADDER = .TRUE.
    LFXC = .FALSE.
    LHFCALC = .TRUE.
    LMODELHF = .TRUE.
    AEXX = 0.088
    HFSCREEN = 1.26

Here [ALGO](../incar-tags/ALGO.md) is set to TIMEEV, meaning that VASP will
now perform a time-propagation calculation.

#### Setting up the bands\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Setting up the bands">edit</a> \| (./index.php.md)\]

With [NBANDS](../incar-tags/NBANDS.md)=12 informs VASP that there are 12
states in total in the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md). This must be consistent with Step 1!
The number of occupied and unoccupied states that are used in the
propagation is controlled by the [NBANDSO](../incar-tags/NBANDSO.md) and
[NBANDSV](../incar-tags/NBANDSV.md) tags, respectively. To choose which
bands to use it is advisable to understand the type of property that is
going to be studied. For instance, in the case of optical absorption,
materials are probed within a few hundreds of milli-electronvolt of the
band gap. In this case it means that only states that lie close to the
band extrema are important for the time-propagation.

In this example VASP will use [NBANDSO](../incar-tags/NBANDSO.md)=4
occupied and [NBANDSV](../incar-tags/NBANDSV.md)=8 unoccupied states
during the time propagation. There is no need to use the total number of
bands set up by [NBANDS](../incar-tags/NBANDS.md), but still
[NBANDSO](../incar-tags/NBANDSO.md)+[NBANDSV](../incar-tags/NBANDSV.md)
cannot be larger than [NBANDS](../incar-tags/NBANDS.md).

#### Setting up the time-step\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Setting up the time-step">edit</a> \| (./index.php.md)\]

VASP is now integrating a time-dependent differential equation so the
time-step used to propagate the dipole moments can be specified in the
[INCAR](../input-files/INCAR.md). By default, VASP will use 20000 steps,
however a different number can be set with the tag
[NELM](../incar-tags/NELM.md). Nevertheless, [NELM](../incar-tags/NELM.md) must
be larger than 100, otherwise VASP will revert to the default value.

The time-step, $\Delta t$,
and maximum propagation time, $T_\mathrm{max}$, are not dependent on the size of the interacting
hamiltonian matrix. However they are dependent on the system in case and
the input tag [CSHIFT](../incar-tags/CSHIFT.md) and
[OMEGAMAX](../incar-tags/OMEGAMAX.md). This comes from the Fourier
transform used to integrate the time-dependent dipole moments, which
leads to $T_\mathrm{max} \approx
1/\mathrm{CSHIFT}$ and $\Delta t \approx
1/\mathrm{OMEGAMAX}$.

The tag [CSHIFT](../incar-tags/CSHIFT.md) also controls the width used in
the plotting of the dielectric function, since

$\frac{1}{\omega - E_\lambda + \mathrm i \eta} = \frac{1}{\omega -
E_\lambda} - \mathrm i\pi \delta(\omega - E_\lambda)$

and the $\delta$-function is approximated as
$\delta(\omega - E_\lambda) = \lim_{\eta\to
0^+}\frac{1}{\pi}\frac{\eta}{(\omega - E_\lambda)^2+\eta^2}$, with
[CSHIFT](../incar-tags/CSHIFT.md)=$\eta$.

Setting [CSHIFT](../incar-tags/CSHIFT.md) = 0.1 ~ 0.01 is often a good
choice, as lower values will lead to unnecessarily long propagation
times and spectra with very narrow peaks.
[OMEGAMAX](../incar-tags/OMEGAMAX.md) is automatically from the maximum
energy difference between occupied and unoccupied states, but can be
lowered to decrease the number of pairs used in the basis set and the
size of the interacting hamiltonian.

#### Choosing the direction of perturbation\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Choosing the direction of perturbation">edit</a> \| (./index.php.md)\]

The dipole momentum vector $\mu^i$ is
direction dependent. The direction of propagation is chosen in the
[INCAR](../input-files/INCAR.md) with the tag
[IEPSILON](../incar-tags/IEPSILON.md), which can take values of 1, 2, or
3 (corresponding to x, y, and z direction, respectively), and 4
(corresponding to all directions).

While choosing a single direction of propagation decreases the computing
time, it is important to pay attention to the symmetries of the material
in study. For example, in the case of bulk silicon, since the material
has cubic symmetry propagating along one direction (x, or y, or z) is
enough. However, for a material like monolayer hexagonal boron nitride,
the crystal symmetries destroy the equivalency between the x and y
directions. For this system propagation should happen along both x and
y, and then the dielectric function should be the average of both
calculations.

### Analysing the results\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Analysing the results">edit</a> \| (./index.php.md)\]

Once the calculation is finished, the dielectric function can be plotted
by executing the following script


     #!/bin/sh
     awk 'BEGIN{i=0} /<dielectricfunction comment="time-propagation">/,\
                    /<\/dielectricfunction>/ \
                     {if ($1=="<r>") {a[i]=$2 ; b[i]=($3+$4+$5)/3 ; c[i]=$4 ; d[i]=$5 ; i=i+1}} \
         END{for (j=0;j<i/2;j++) print a[j],b[j],b[j+i/2]}' vasprun.xml > optics.dat


which can be copied to a file (e.g. extract_optics.sh) in the same
directory where the calculation was performed and then ran with

    $ sh extract_optics.sh

This creates a file called optics.dat with three data columns. The first
column is the energy of excitation, in eV. The second and third columns
correspond to the imaginary and real parts of
$\frac{1}{3}\[\epsilon_{xx}(\omega)+\epsilon_{yy}(\omega)+\epsilon_{zz}(\omega)\]$. For the example shown here, the obtained
$\mathrm{Im}\[\epsilon\]$ should be similar to the
following image.

<a href="/wiki/File:TIMEEV_bulk_Si_dielectric_function.png"
class="mw-file-description"
title="Imaginary part of the dielectric function"><img
src="https://vasp.at/wiki/images/thumb/3/3a/TIMEEV_bulk_Si_dielectric_function.png/600px-TIMEEV_bulk_Si_dielectric_function.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/3/3a/TIMEEV_bulk_Si_dielectric_function.png/900px-TIMEEV_bulk_Si_dielectric_function.png 1.5x, /wiki/images/thumb/3/3a/TIMEEV_bulk_Si_dielectric_function.png/1200px-TIMEEV_bulk_Si_dielectric_function.png 2x"
width="600" height="400"
alt="Imaginary part of the dielectric function" /></a>

Alternatively, if VASP was compiled with hdf5 support, the results can
also be plotted with py4vasp


     import py4vasp
     #replace path_to_calculation below with the path to the directory where the corresponding vaspout.h5 is located
     calc=py4vasp.Calculation.from_path("path_to_calculation")

     calc.dielectric_function.plot("TIMEEV")


which will create the following figure with both the real and imaginary
part of $\epsilon(\omega)$.

<a href="/wiki/File:TIMEEV_bulk_Si_dielectric_function_py4vasp.png"
class="mw-file-description"
title="Imaginary part of the dielectric function"><img
src="https://vasp.at/wiki/images/thumb/6/61/TIMEEV_bulk_Si_dielectric_function_py4vasp.png/600px-TIMEEV_bulk_Si_dielectric_function_py4vasp.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/6/61/TIMEEV_bulk_Si_dielectric_function_py4vasp.png 1.5x"
width="600" height="455"
alt="Imaginary part of the dielectric function" /></a>

  

|  |
|----|
| **Mind:** It should be stated that this is just an example, not a converged calculation! Several numerical parameters should be checked for convergence (e.g. number of k-points, number of empty states, etc). |

## Comparison to other methods\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Comparison to other methods">edit</a> \| (./index.php.md)\]

VASP offers two other methods with which you can compute the macroscopic
dielectric function. These are based on eigendecomposition of the two
particle hamiltonian, $H^\mathrm{exc}$. While more expensive than time-evolution, both these
methods are able to compute eigenvalues and eigenstates of
$H^\mathrm{exc}$, thus providing direct access to the
excitation energies of a system.

### Bethe-Salpeter equation\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: Bethe-Salpeter equation">edit</a> \| (./index.php.md)\]

Here the full
<a href="/wiki/Bethe-Salpeter_equations" class="mw-redirect"
title="Bethe-Salpeter equations">Bethe-Salpeter equation</a> is employed
by setting [ALGO](../incar-tags/ALGO.md)=BSE. The interaction hamiltonian is
built using the dielectric function from RPA, and has the right
behaviour in the long range regime. This means that it can accurately
describe bound excitons in solids and large molecules. However, it is
more costly than time-evolution, scaling with
$N_\mathrm{rank}^3$.

### Casida equation\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: Casida equation">edit</a> \| (./index.php.md)\]

Similar to the Bethe-Salpeter equation, the [Casida
equation](../methods/Time-dependent_density-functional_theory_calculations.md)
employs an eigensolver method to compute the dielectric function. This
is chosen in the [INCAR](../input-files/INCAR.md) with
[ALGO](../incar-tags/ALGO.md)=TDHF. The key difference is that the Casida
method does not require a preceding GW run to compute the RPA screening
and can be performed with either DFT or hybrid-functional orbitals and
energies.

## Related tags and articles\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NBANDSO](../incar-tags/NBANDSO.md), [NBANDSV](../incar-tags/NBANDSV.md),
[IEPSILON](../incar-tags/IEPSILON.md), [NELM](../incar-tags/NELM.md),
[LHARTREE](../incar-tags/LHARTREE.md), [LADDER](../incar-tags/LADDER.md),
[LFXC](../incar-tags/LFXC.md), [LHFCALC](../incar-tags/LHFCALC.md),
[LMODELHF](../incar-tags/LMODELHF.md), [AEXX](../incar-tags/AEXX.md),
[HFSCREEN](../incar-tags/HFSCREEN.md)

[Time-dependent density-functional theory
calculations](../methods/Time-dependent_density-functional_theory_calculations.md)

[Bethe-Salpeter-equations
calculations](Bethe-Salpeter-equations_calculations.md)

## References\[<a
href="/wiki/index.php?title=Time-evolution_algorithm&amp;veaction=edit&amp;section=21"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-sander:prb:15_1-0)</sup>
    <sup>[b](#cite_ref-sander:prb:15_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.92.045209"
    class="external text" rel="nofollow">T. Sander, E. Maggio, and G.
    Kresse, <em>Beyond the Tamm-Dancoff approximation for extended systems
    using exact diagonalization</em>, Phys. Rev. B <strong>92</strong>,
    045209 (2015).</a>
2.  ↑
    <sup>[a](#cite_ref-sander:jcp:2017_2-0)</sup>
    <sup>[b](#cite_ref-sander:jcp:2017_2-1)</sup>
    <a href="http://doi.org/10.1063/1.4975193" class="external text"
    rel="nofollow">T. Sander, G. Kresse, <em>Macroscopic dielectric function
    within time-dependent density functional theory—Real time evolution
    versus the Casida approach</em> , J. Chem. Phys. <em>146</em>, 064110
    (2017)</a>
3.  [↑](#cite_ref-schmidt:prb:2003_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.67.08530"
    class="external text" rel="nofollow">W. G. Schmidt, S. Glutsch, P. H.
    Hahn, and F. Bechstedt, <em>Efficient O(N2) method to solve the
    Bethe-Salpeter equation</em>, Phys. Rev. B <strong>67</strong>, 085307
    (2003)</a>



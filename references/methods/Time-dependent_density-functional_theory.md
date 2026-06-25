<!-- Source: https://vasp.at/wiki/index.php/Time-dependent_density-functional_theory | revid: 37288 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Time-dependent density-functional theory


Time-dependent density-functional theory (TDDFT) is an extension of
density-functional theory (DFT) to systems with time-varying external
potentials, enabling the computation of excited-state properties and
response
functions<sup>[\[1\]](#cite_note-onida:revmodphys:2002-1)</sup>.
TDDFT calculations can be based on ground-state electronic structures
obtained from DFT,
<a href="/wiki/Hybrid_functionals" class="mw-redirect"
title="Hybrid functionals">hybrid functionals</a>, or even *GW*
approximations.

The theoretical foundation of TDDFT is the Runge-Gross
theorem<sup>[\[2\]](#cite_note-runge:gross:1984-2)</sup>,
which is the time-dependent analog of the Hohenberg-Kohn theorem of
density-functional theory. It states that the time-dependent density
$n(\mathbf r, t)$ is uniquely determined by the
time-dependent external potential $v_\mathrm{ext}(\mathbf r, t)$. As a consequence, all physical observables are
functionals of the density, and the interacting many-electron problem
can be mapped onto an auxiliary system of non-interacting electrons
reproducing the same density (the time-dependent Kohn-Sham system).


## Contents


- [1
  Linear-response
  formalism](#linear-response-formalism)
  - [1.1
    Approximation
    hierarchy](#approximation-hierarchy)
- [2 Casida
  equation formalism for
  TDDFT](#casida-equation-formalism-for-tddft)
  - [2.1
    Tamm-Dancoff
    approximation](#tamm-dancoff-approximation)
  - [2.2 Connection
    to the dielectric
    function](#connection-to-the-dielectric-function)
- [3 Time-evolution
  or real-time TDDFT](#time-evolution-or-real-time-tddft)
  - [3.1
    Propagation of the time-dependent
    coefficients](#propagation-of-the-time-dependent-coefficients)
  - [3.2 Connection
    to the dielectric
    function](#connection-to-the-dielectric-function-1)
- [4 Dyson equation
  (Linear response)
  TDDFT](#Dyson_equation_(Linear_response)_TDDFT)
- [5 Approximations
  for the exchange-correlation
  kernel](#approximations-for-the-exchange-correlation-kernel)
  - [5.1 Adiabatic
    approximation](#adiabatic-approximation)
  - [5.2 Local
    exchange-correlation
    kernel](#local-exchange-correlation-kernel)
  - [5.3
    Exchange-correlation kernel from exact
    exchange](#exchange-correlation-kernel-from-exact-exchange)
  - [5.4 Nanoquanta
    kernel](#nanoquanta-kernel)
- [6 TDDFT compared
  to BSE](#tddft-compared-to-bse)
  - [6.1 Casida
    TDDFT and BSE](#casida-tddft-and-bse)
- [7 Related tags
  and articles](#related-tags-and-articles)
- [8
  References](#references)


## Linear-response formalism\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Linear-response formalism">edit</a> \| (./index.php.md)\]

In the linear-response regime, the external potential is split into a
static part and a small time-dependent perturbation,
$v_\mathrm{ext}(\mathbf r, t) = v(\mathbf r) + \delta v(\mathbf r, t)$. The induced density variation
$\delta n$ is then related to the perturbation through
the density-density response function $\chi$,

$\delta n(1) = \int \mathrm d 2 \\ \chi(1,2) \\ \delta v(2),$

where $1 \equiv (\mathbf{r}_1, t_1)$ and $2 \equiv (\mathbf{r}_2, t_2)$ denote space-time coordinates. Equivalently,
$\chi$ is the functional derivative
$\chi(1,2) = \delta n(1)/\delta v_\mathrm{ext}(2)$.
Within the Kohn-Sham scheme, the density response of the interacting
system equals that of an auxiliary non-interacting system responding to
an effective perturbation $\delta v_\mathrm{KS} = \delta
v + \delta v_\mathrm{H} + \delta v_\mathrm{xc}$,
which defines the independent-particle response

$\chi_0(1,2) = \frac{\delta n(1)}{\delta v_\mathrm{KS}(2)}.$

Applying the chain rule to $\chi(1,2)$
and using

$\frac{\delta v_\mathrm{KS}(1)}{\delta v_\mathrm{ext}(2)} =
\delta(1,2) + v(1,2) + f_\mathrm{xc}(1,2),$

with the exchange-correlation kernel $f_\mathrm{xc}(1,2) = \delta
v_\mathrm{xc}(1)/\delta n(2)$ and the bare Coulomb
interaction $v(1,2) =
\delta(t_1-t_2)/|\mathbf r_1 - \mathbf r_2|$, yields
the Dyson equation

$\chi(1,2) = \chi_0(1,2) + \chi_0(1,3)\left\[v(3,4) +
f_\mathrm{xc}(3,4)\right\]\chi(4,2).$

### Approximation hierarchy\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Approximation hierarchy">edit</a> \| (./index.php.md)\]

The response function formalism above can be systematically simplified
by neglecting different interaction terms in the Dyson equation for
$\chi$:

- **Independent-particle approximation (IPA)**
  ([LHARTREE](../incar-tags/LHARTREE.md)=.FALSE. and
  [LFXC](../incar-tags/LFXC.md)=.FALSE.): If both the Coulomb interaction
  $v$ and the exchange-correlation kernel
  $f_\mathrm{xc}$ are neglected, the full response
  function reduces to the independent-particle response,

$\chi(1,2) = \chi_0(1,2).$

In this limit, optical spectra are computed from non-interacting
Kohn-Sham transitions without any electron-hole interaction or
local-field effects.

- **Random-phase approximation (RPA)**
  ([LHARTREE](../incar-tags/LHARTREE.md)=.TRUE. and
  [LFXC](../incar-tags/LFXC.md)=.FALSE.): If $f_\mathrm{xc}$ is neglected but the Coulomb kernel is retained, the
  Dyson equation becomes

$\chi(1,2) = \chi_0(1,2) + \chi_0(1,3)\\v(3,4)\\\chi(4,2).$

This approximation includes the long-range Coulomb interaction, but
omits exchange-correlation contributions beyond those already present in
the Kohn-Sham eigenvalues used to construct $\chi_0$. RPA
captures plasmons and local-field effects, but typically fails to
describe bound excitons in semiconductors and insulators.

- **Full TDDFT** ([LHARTREE](../incar-tags/LHARTREE.md)=.TRUE. and
  [LFXC](../incar-tags/LFXC.md)=.TRUE.; additionally
  [LADDER](../incar-tags/LADDER.md)=.TRUE. if a hybrid functional is
  used): Retaining both the Coulomb interaction and an
  exchange-correlation kernel $f_\mathrm{xc}$ yields the complete TDDFT response,

$\chi(1,2) = \chi_0(1,2) + \chi_0(1,3)\left\[v(3,4) +
f_\mathrm{xc}(3,4)\right\]\chi(4,2).$

The choice of $f_\mathrm{xc}$ determines whether bound excitons and other many-body
effects are accurately captured.

## Casida equation formalism for TDDFT\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Casida equation formalism for TDDFT">edit</a> \| (./index.php.md)\]

The Casida approach ([ALGO](../incar-tags/ALGO.md)=TDHF) solves for the
excitation spectrum by diagonalizing the excitonic Hamiltonian in the
transition space. It is often useful to rewrite the Dyson equation for
$\chi$ in terms of a four-point response function
$L(1,2,3,4)$, which describes the response of the system
to a two-particle perturbation. The four-point function is related to
the two-point density response $\chi$ by

$\chi(1,2) = \int \mathrm d 3 \\ \mathrm d 4 \\ L(1,3,2,4) \\ v(3,4),$

where $v(3,4)$ is
the bare Coulomb interaction. The four-point response function satisfies
a Dyson-like equation

$L(1,2,3,4) = L_0(1,2,3,4) + L_0(1,2,5,6) \left\[v(5,6) +
f_\mathrm{xc}(5,6)\right\] L(5,6,3,4),$

where $L_0$ is the
independent-particle four-point response. This four-point formulation is
particularly useful when comparing Casida TDDFT with the [Bethe-Salpeter
equation](../theory/Bethe-Salpeter_equation.md), as
both can be expressed in terms of analogous four-point functions.

Working within the frequency domain and using a basis set that considers
transitions from valence to conduction states at the same **k** point
(transition basis) makes it possible to recast the equation for
$\chi(1,2)$ into an eigenvalue
problem<sup>[\[3\]](#cite_note-casida:1995-3)</sup>

$\left(\begin{array}{cc} \mathbf{A} & \mathbf{B} \\ \mathbf{B}^\* &
\mathbf{A}^\* \end{array}\right)\left(\begin{array}{l}
\mathbf{X}_\lambda \\ \mathbf{Y}_\lambda
\end{array}\right)=\omega_\lambda\left(\begin{array}{cc} \mathbf{1} &
\mathbf{0} \\ \mathbf{0} & -\mathbf{1}
\end{array}\right)\left(\begin{array}{l} \mathbf{X}_\lambda \\
\mathbf{Y}_\lambda \end{array}\right),$

which is also known as the Casida equation. The
$A$ and $B$ matrices
are given by

$A_{vc}^{v'c'} =
(\varepsilon_v-\varepsilon_c)\delta_{vv'}\delta_{cc'} + \langle
cv'|v|vc'\rangle - \langle cv'|f_\mathrm{xc}|c'v\rangle,$

$B_{vc}^{v'c'} = \langle vv'|v|cc'\rangle - \langle
vv'|f_\mathrm{xc}|c'c\rangle.$

Here, $v$ and
$c$ denote valence and conduction states, respectively,
$\varepsilon_v$ and $\varepsilon_c$ are the corresponding eigenvalues, and the
two-electron integrals $\langle
\cdot|\cdot|\cdot\rangle$ involve the bare Coulomb
interaction or the exchange-correlation kernel as indicated. The
$A$ matrix describes the resonant (excitation) and
anti-resonant (de-excitation) transitions, while the
$B$ matrix describes the coupling between them. Due to
this coupling, the Casida matrix is non-Hermitian.

### Tamm-Dancoff approximation\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Tamm-Dancoff approximation">edit</a> \| (./index.php.md)\]

The non-Hermitian structure of the Casida equation arises from the
coupling between resonant and anti-resonant transitions through the
off-diagonal block $B$. A common
simplification is the Tamm-Dancoff approximation (TDA), in which the
coupling block is set to zero, $B = 0$. The
eigenvalue problem then reduces to the Hermitian form

$A
\\ X_\lambda = \omega_\lambda \\ X_\lambda.$

The TDA significantly reduces the computational cost and guarantees
real, positive excitation energies, but it neglects the mixing between
excitations and de-excitations. For optical absorption spectra of solids
it is usually a good approximation, but for calculations at finite
momentum **q** the full equation must be solved.

### Connection to the dielectric function\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Connection to the dielectric function">edit</a> \| (./index.php.md)\]

The macroscopic dielectric function is obtained by using the eigenvalues
$\omega_\lambda$ and eigenvectors
$\mathbf{X}_\lambda$ of the Casida equation in the
spectral representation

$\varepsilon_M(\omega) = 1 + \frac{4\pi}{\Omega} \sum_\lambda
\left|\sum_{cv\mathbf k} \mu_{cv\mathbf k} X_\lambda^{cv\mathbf
k}\right|^2 \left\[\frac{1}{\omega + \omega_\lambda + \mathrm i\eta} -
\frac{1}{\omega - \omega_\lambda + \mathrm i\eta}\right\],$

where $\mu_{cv\mathbf{k}}^j=\frac{\langle
c\mathbf{k}|v_j|v\mathbf{k}\rangle}{\varepsilon_c(\mathbf{k})-\varepsilon_v(\mathbf{k})}$ is the dipole matrix element associated with the
transition from valence state $v$ to
conduction state $c$ at
**k**-point $\mathbf k$,
$v_j$ is the velocity operator along direction
$j$, and $\omega_\lambda$ are the excitation energies. The eigenvalues give the
peak positions and the eigenvectors determine the oscillator strengths
(peak intensities) in the optical absorption spectrum
$\mathrm{Im}\\\varepsilon_M(\omega)$.

## Time-evolution or real-time TDDFT\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Time-evolution or real-time TDDFT">edit</a> \| (./index.php.md)\]

An alternative to solving the Casida equation is to compute the
frequency-dependent response via real-time propagation of the Kohn-Sham
orbitals
([ALGO](../incar-tags/ALGO.md)=TIMEEV)<sup>[\[4\]](#cite_note-sander:jcp:2017-4)</sup>.
The starting point is the time-dependent Kohn-Sham equation,

$\mathrm i \frac{\partial}{\partial t}\left|\phi_{v\mathbf
k}\[n(t)\]\right\rangle = \left\[-\frac{\nabla^2}{2} + V_{\mathrm
H}\[n(t)\] + V_{\mathrm{xc}}\[n(t)\] +
V_\mathrm{ext}(t)\right\]\left|\phi_{v\mathbf
k}\[n(t)\]\right\rangle,$

where all potentials are functionals of the time-evolving density
$n(\mathbf r, t)$.

Instead of constructing and diagonalizing the full Hamiltonian in
transition space as done in Casida formalism, the time-evolution method
applies a delta-like perturbation

$V_\mathrm{ext}(\mathbf r, t) = \lambda \\ \mathbf r\cdot \mathbf D \\
\delta(t)$

to the ground-state system, where $\lambda$ is a
small perturbation parameter and $\mathbf D$ is
the electric displacement field.

### Propagation of the time-dependent coefficients\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Propagation of the time-dependent coefficients">edit</a> \| (./index.php.md)\]

The time-dependent wavefunctions are expanded as

$\left|\phi_{v\mathbf k}(t)\right\rangle=\left\\\left|\phi_{v\mathbf
k}^0\right\rangle+\lambda\sum_{c \in \mathrm{unocc} .} c_{cv\mathbf
k}(t)\left|\phi_{c\mathbf k}^0\right\rangle\right\\ e^{-\mathrm i
\varepsilon_{v\mathbf{k}} t},$

so that changes in an initial occupied state $|\phi_{v\mathbf k}^0\rangle$ are captured by time-dependent contributions from
unoccupied states $|\phi_{c\mathbf k}^0\rangle$. The time-dependent coefficients
$c_{cv\mathbf k}(t)$ are propagated forward in time
starting from $c_{cv\mathbf k}(0)=0$ by repeatedly updating the time-dependent Hamiltonian
$H\[\phi_{v\mathbf k}(t)\]$.

In essence, the time-evolution algorithm works as follows:

1.  Set up states at time step $t_n$:
    $\left|\phi_{v\mathbf
    k}(t_n)\right\rangle=\left\\\left|\phi_{v\mathbf
    k}^0\right\rangle+\lambda\sum_{c \in \mathrm{unocc.}} c_{cv\mathbf
    k}(t_n)\left|\phi_{c\mathbf k}^0\right\rangle\right\\ e^{-\mathrm
    i \varepsilon_{v\mathbf{k}} t_n}.$
2.  Update the time-dependent Hamiltonian $H\[\phi_{v\mathbf
    k}(t_n)\]$.
3.  Calculate the change in the time-dependent coefficients:
    $\delta c_{cv\mathbf
    k}(t_n) = \left\langle\phi_{c\mathbf k}^0\right|
    H\[\phi_{v\mathbf k}(t_n)\] \left|\phi_{v\mathbf
    k}(t_n)\right\rangle.$
4.  Compute the coefficients at the next time step:
    $c_{cv\mathbf k}(t_{n+1})
    = c_{cv\mathbf k}(t_{n-1}) + 2\mathrm i \\ \Delta t \\ \delta
    c_{cv\mathbf k}(t_n).$

Here, $\Delta t$ is
the time step chosen for the propagation. Updating the Hamiltonian with
the new states is essential, as it is a functional of the time-dependent
density.

The same approximation hierarchy described in the [Approximation
hierarchy](#approximation-hierarchy) section applies to the
time-evolution approach. The tags [LHARTREE](../incar-tags/LHARTREE.md),
[LFXC](../incar-tags/LFXC.md), and [LADDER](../incar-tags/LADDER.md) control
which interaction terms are included in the time-dependent Hamiltonian:
[LHARTREE](../incar-tags/LHARTREE.md) controls the Coulomb (Hartree)
energy, [LFXC](../incar-tags/LFXC.md) controls the local
exchange-correlation kernel, and [LADDER](../incar-tags/LADDER.md)
controls the nonlocal exchange contribution from hybrid functionals. At
each time step, the corresponding energy terms in the Hamiltonian are
updated based on the time-evolving density.

### Connection to the dielectric function\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Connection to the dielectric function">edit</a> \| (./index.php.md)\]

The dielectric function is obtained by propagating the time-dependent
coefficients $c_{cv\mathbf k}(t)$ and accumulating their overlap with the dipole vector
$|\mu\rangle$ at each time step, followed by a Fourier
transform<sup>[\[4\]](#cite_note-sander:jcp:2017-4)</sup>:

$\varepsilon_{ij}(\omega) = \delta_{ij} - \frac{4\pi e^2}{\Omega}
\int_0^\infty \mathrm d t \sum_{cv\mathbf k}
\left(\langle\mu^j_{cv\mathbf k}|c^i_{cv\mathbf k}(t)\rangle +
\mathrm{c.c.}\right) e^{-\mathrm i(\omega - \mathrm i\eta)t}.$

Here, $\mu_{cv\mathbf{k}}^j$ is the dipole matrix element defined in the
[connection to the dielectric
function](#connection-to-the-dielectric-function) above.

## Dyson equation (Linear response) TDDFT\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Dyson equation (Linear response) TDDFT">edit</a> \| (./index.php.md) TDDFT")\]

Another approach to TDDFT ([ALGO](../incar-tags/ALGO.md)=CHI) is to solve
the two-point Dyson equation directly and find the density-density
response function $\chi$. This
approach allows one to calculate the full $\chi_{\mathbf q}(\mathbf
G,\mathbf G',\omega)$ and is used for finding the
Coulomb interaction screened via the RPA dielectric function, *W*.
However, it requires inverting the Dyson equation at every frequency,
which becomes too costly for calculating spectra with good resolution.
Since this approach does not invoke the Tamm-Dancoff approximation, the
RPA dielectric function obtained this way is equivalent to the Casida
RPA dielectric function.

## Approximations for the exchange-correlation kernel\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Approximations for the exchange-correlation kernel">edit</a> \| (./index.php.md)\]

The exchange-correlation kernel $f_\mathrm{xc}$ is a key quantity in TDDFT that approximates the
interaction between electrons and holes. The choice of kernel depends on
the exchange-correlation functional used in the ground-state
calculation.

### Adiabatic approximation\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Adiabatic approximation">edit</a> \| (./index.php.md)\]

In its exact form, the exchange-correlation kernel
$f_\mathrm{xc}(\mathbf r, \mathbf r', t-t')$ is
nonlocal in time, meaning that $v_\mathrm{xc}$ at time $t$ depends on
the density at all earlier times $t' < t$.
This memory dependence is intractable in practice. The adiabatic
approximation replaces the time-nonlocal kernel by the instantaneous
functional derivative of a ground-state exchange-correlation functional,

$f_\mathrm{xc}(\mathbf r, \mathbf r', t-t') = \delta(t-t') \frac{\delta
v_\mathrm{xc}\[n\](\mathbf r)}{\delta n(\mathbf r')},$

evaluated at the ground-state density $n_0$. The
kernel is therefore frequency-independent in this approximation.
Combining the adiabatic approximation with the local-density
approximation gives the adiabatic LDA (ALDA), with GGA gives AGGA, and
so on. All TDDFT kernels discussed below are adiabatic.

### Local exchange-correlation kernel\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Local exchange-correlation kernel">edit</a> \| (./index.php.md)\]

The local exchange-correlation kernel, $f_\mathrm{xc}$, in TDDFT calculations is given by

$f_{\mathrm{xc}}^{\text {loc }}\left(\mathbf{r},
\mathbf{r}^{\prime}\right)=\frac{\delta^2
E_{\mathrm{xc}}^{\mathrm{DFT}}}{\delta n(\mathbf{r}) \delta
n\left(\mathbf{r}^{\prime}\right)},$

where $E_{\mathrm{xc}}^{\mathrm{DFT}}$ is the local or
semilocal exchange-correlation functional (e.g., LDA or PBE).

These local kernels lack the long-range component (which goes as
$-1/q^2$). In periodic or extended systems, they fail to
properly reproduce the binding energies of electron-hole pairs.

The ALDA and APBE kernels work well for metallic systems and for optical
properties where excitonic effects are not important (such as plasmon
frequencies). However, they fail to describe bound excitons in
semiconductors and insulators, where the long-range electron-hole
interaction is crucial for determining excitation energies and binding
energies.

### Exchange-correlation kernel from exact exchange\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Exchange-correlation kernel from exact exchange">edit</a> \| (./index.php.md)\]

When hybrid functionals or Hartree-Fock exchange are used in TDDFT, the
exchange-correlation kernel includes a contribution from exact exchange.
This nonlocal exchange contribution naturally provides the
$-1/q^2$ long-range behavior in the kernel, which is
essential for capturing excitonic effects. The exact-exchange
contribution to $f_\mathrm{xc}$ takes the form

$f_{\mathrm{x}}^{\text{exact}}(\mathbf{r}, \mathbf{r'}) = \frac{\delta^2
E_{\mathrm{x}}^{\text{exact}}}{\delta^2 n(\mathbf{r},\mathbf{r'})},$

where $E_{\mathrm{x}}^{\text{exact}}$ is the exact-exchange energy.

Alternatively, the screened exchange interaction potential
$W(\mathbf r,\mathbf r';\omega)$ from
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>
can be used. This treats the electron-hole interaction by including the
ladder diagrams from many-body perturbation
theory<sup>[\[5\]](#cite_note-sander:prb:15-5)</sup>,
providing an alternative route to the correct long-range physics.

### Nanoquanta kernel\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Nanoquanta kernel">edit</a> \| (./index.php.md)\]

The **nanoquanta** kernel is an exchange-correlation kernel derived from
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>
that maps the [Bethe-Salpeter
equation](../theory/Bethe-Salpeter_equation.md) (BSE)
onto a TDDFT-like
equation<sup>[\[6\]](#cite_note-sottile:prl:2003-6)</sup>.
Rather than being a simple analytical form, it is constructed by
requiring that the TDDFT response function reproduces the BSE response
function. This leads to a kernel of the form

$f_{\mathrm{xc}}^{NQ}(1,2)=\int \mathrm d 3456 \\ \chi_0^{-1}(1,3) \\
G(3,4) \\ G(5,3) \\ W(4,5) \\ G(4,6) \\ G(6,5) \\ \chi_0^{-1}(6,2),$

where $\chi_0$ is
the independent-particle response function, $G$ is the
single-particle Green's function, and $W$ is the
screened Coulomb interaction from
<a href="/wiki/GW" class="mw-redirect" title="GW"><em>GW</em></a>
theory. The four Green's functions $G$ contract
the two-point density indices on the outside with the four-point
structure of $W$ inside,
effectively mapping the four-point BSE kernel onto a two-point TDDFT
kernel. Because $W$ contains
the proper $-1/q^2$
long-range behavior, the resulting nanoquanta kernel inherits this
feature and is therefore capable of describing bound excitons in
semiconductors and insulators.

By construction, the nanoquanta kernel yields optical spectra of
comparable accuracy to BSE calculations, including bound excitons and
continuum excitonic enhancement. However, computing it is as expensive
as a BSE calculation and does not provide a computational advantage over
BSE itself.

See the [LFXC](../incar-tags/LFXC.md) tag page for details on how the
$f_\mathrm{xc}$ kernels are implemented in VASP and
what approximations are made.

## TDDFT compared to BSE\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: TDDFT compared to BSE">edit</a> \| (./index.php.md)\]

### Casida TDDFT and BSE\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Casida TDDFT and BSE">edit</a> \| (./index.php.md)\]

The Casida formulation of TDDFT and the [Bethe-Salpeter
equation](../theory/Bethe-Salpeter_equation.md) (BSE)
share essentially the same mathematical structure: both are
non-Hermitian eigenvalue problems of the form

$\left(\begin{array}{cc} \mathbf{A} & \mathbf{B} \\ \mathbf{B}^\* &
\mathbf{A}^\* \end{array}\right)\left(\begin{array}{l}
\mathbf{X}_\lambda \\ \mathbf{Y}_\lambda
\end{array}\right)=\omega_\lambda\left(\begin{array}{cc} \mathbf{1} &
\mathbf{0} \\ \mathbf{0} & -\mathbf{1}
\end{array}\right)\left(\begin{array}{l} \mathbf{X}_\lambda \\
\mathbf{Y}_\lambda \end{array}\right),$

where the matrix elements of $A$ and
$B$ are built from valence-to-conduction transitions and
contain a Hartree (Coulomb) contribution together with a term that goes
beyond the random-phase approximation (RPA). The Coulomb part is
identical in both methods and the difference lies entirely in how the
beyond-RPA contribution is described:

- In TDDFT, the beyond-RPA term is the exchange-correlation kernel
  $f_\mathrm{xc}$.
- In BSE, the beyond-RPA term is the screened Coulomb interaction
  $W$.

When $f_\mathrm{xc}$ includes a fraction of exact exchange (as in
<a href="/wiki/Hybrid_functionals" class="mw-redirect"
title="Hybrid functionals">hybrid</a> or range-separated hybrid
functionals), both formalisms involve integrals of the same form and the
remaining difference is how that interaction is screened:

- In BSE, the bare Coulomb interaction $v$ is
  screened by the inverse dielectric tensor, $W = \varepsilon^{-1} v$, so that the screening is determined by the actual
  electronic response of the system and is in general nonlocal.
- In Casida TDDFT with hybrid functionals, the screening is replaced by
  a constant prefactor $c_\mathrm{x}$, the fraction of exact exchange (e.g., 0.25 for
  PBE0). For range-separated hybrids, this prefactor becomes a simple
  function of $|\mathbf q + \mathbf G|$ that mimics a screened interaction.

In this sense, hybrid-functional TDDFT can be viewed as a BSE-like
calculation in which the screening is approximated by a model function
or a constant. This makes TDDFT considerably cheaper than BSE, because
it avoids the need for a preceding *GW* or screening calculation, but at
the cost of using an approximate, diagonal screening model.

## Related tags and articles\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

Tags

[ALGO](../incar-tags/ALGO.md), [LHARTREE](../incar-tags/LHARTREE.md),
[LFXC](../incar-tags/LFXC.md), [LADDER](../incar-tags/LADDER.md)

How-to

[Time-dependent density-functional theory
calculations](Time-dependent_density-functional_theory_calculations.md),
[Plotting exciton
wavefunction](../theory/Plotting_exciton_wavefunction.md)

Theory

[Bethe-Salpeter
equation](../theory/Bethe-Salpeter_equation.md),
<a href="/wiki/Dielectric_properties" class="mw-redirect"
title="Dielectric properties">Dielectric properties</a>

## References\[<a
href="/wiki/index.php?title=Time-dependent_density-functional_theory&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-onida:revmodphys:2002_1-0)
    <a href="https://link.aps.org/doi/10.1103/RevModPhys.74.601"
    class="external text" rel="nofollow">G. Onida, L. Reining, and A. Rubio,
    <em>Electronic excitations: density-functional versus many-body
    Green's-function approaches</em>, Rev. Mod. Phys. <strong>74</strong>, 2
    (2002).</a>
2.  [↑](#cite_ref-runge:gross:1984_2-0)
    <a href="https://doi.org/10.1103/PhysRevLett.52.997"
    class="external text" rel="nofollow">E. Runge and E. K. U. Gross,
    <em>Density-Functional Theory for Time-Dependent Systems</em>, Phys.
    Rev. Lett. <strong>52</strong>, 997 (1984).</a>
3.  [↑](#cite_ref-casida:1995_3-0)
    <a href="https://doi.org/10.1142/9789812830586_0005"
    class="external text" rel="nofollow">M. E. Casida, in <em>Recent
    Advances in Density Functional Methods, Part I</em>, edited by D. P.
    Chong (World Scientific, Singapore, 1995), p. 155.</a>
4.  ↑
    <sup>[a](#cite_ref-sander:jcp:2017_4-0)</sup>
    <sup>[b](#cite_ref-sander:jcp:2017_4-1)</sup>
    <a href="http://doi.org/10.1063/1.4975193" class="external text"
    rel="nofollow">T. Sander, G. Kresse, <em>Macroscopic dielectric function
    within time-dependent density functional theory—Real time evolution
    versus the Casida approach</em> , J. Chem. Phys. <em>146</em>, 064110
    (2017)</a>
5.  [↑](#cite_ref-sander:prb:15_5-0)
    <a href="https://doi.org/10.1103/PhysRevB.92.045209"
    class="external text" rel="nofollow">T. Sander, E. Maggio, and G.
    Kresse, <em>Beyond the Tamm-Dancoff approximation for extended systems
    using exact diagonalization</em>, Phys. Rev. B <strong>92</strong>,
    045209 (2015).</a>
6.  [↑](#cite_ref-sottile:prl:2003_6-0)
    <a href="https://doi.org/10.1103/PhysRevLett.91.056402"
    class="external text" rel="nofollow">F. Sottile, V. Olevano, and L.
    Reining, <em>Parameter-Free Calculation of Response Functions in
    Time-Dependent Density-Functional Theory</em>, Phys. Rev. Lett.
    <strong>91</strong>, 056402 (2003).</a>



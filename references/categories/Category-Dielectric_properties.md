<!-- Source: https://vasp.at/wiki/index.php/Category:Dielectric_properties | revid: 35520 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Dielectric properties



## Contents


- [1 Dielectric
  function](#dielectric-function)
  - [1.1 Static
    response](#static-response)
    - [1.1.1
      LEPSILON: density-functional-perturbation
      theory
      (DFPT)](#lepsilon-density-functional-perturbation-theory-dfpt))
    - [1.1.2
      LCALCEPS: finite differences
      approach](#lcalceps-finite-differences-approach)
  - [1.2 Dynamical
    response: Green-Kubo and many-body perturbation
    theory](#dynamical-response-green-kubo-and-many-body-perturbation-theory)
    - [1.2.1
      LOPTICS: Green-Kubo
      formula](#loptics-green-kubo-formula)
    - [1.2.2 ALGO =
      TDHF: Casida equation](#ALGO_=_TDHF:_Casida_equation)
    - [1.2.3 ALGO =
      TIMEEV: delta-pulse electric
      field](#ALGO_=_TIMEEV:_delta-pulse_electric_field)
    - [1.2.4 ALGO =
      CHI: polarizability within RPA
      approximation](#ALGO_=_CHI:_polarizability_within_RPA_approximation)
    - [1.2.5 ALGO =
      BSE: macroscopic dielectric function including
      excitons](#ALGO_=_BSE:_macroscopic_dielectric_function_including_excitons)
- [2 Level of
  approximation](#level-of-approximation)
  - [2.1
    Microscopic and macroscopic
    quantities](#microscopic-and-macroscopic-quantities)
  - [2.2 Finite
    momentum dielectric
    function](#finite-momentum-dielectric-function)
  - [2.3 Local
    fields in the Hamiltonian](#local-fields-in-the-hamiltonian)
  - [2.4
    Ion-clamped vs relaxed-ion/dressed dielectric
    function](#ion-clamped-vs-relaxed-iondressed-dielectric-function)
  - [2.5
    Density-density versus current-current
    response
    functions](#density-density-versus-current-current-response-functions)
- [3 Other
  dielectric properties](#other-dielectric-properties)
  - [3.1 Electron
    energy loss spectroscopy
    (EELS)](#electron-energy-loss-spectroscopy-eels))
  - [3.2 Optical
    conductivity](#optical-conductivity)
  - [3.3 Optical
    absorption](#optical-absorption)
  - [3.4 X-ray
    absorption](#x-ray-absorption)
  - [3.5
    Reflectance](#reflectance)
  - [3.6
    Magneto-optical Kerr effect
    (MOKE)](#magneto-optical-kerr-effect-moke))
- [4 Electric
  response combined with perturbations of the ionic degrees of
  freedom](#electric-response-combined-with-perturbations-of-the-ionic-degrees-of-freedom)
  - [4.1
    Low-frequency corrections from atomic
    displacements](#low-frequency-corrections-from-atomic-displacements)
    - [4.1.1 Polar
      materials](#polar-materials)
  - [4.2
    Corrections from
    strain](#corrections-from-strain)
- [5 Additional
  resources](#additional-resources)
  - [5.1
    Lectures](#lectures)
  - [5.2
    Tutorials](#tutorials)
- [6
  References](#references)


## Dielectric function\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Dielectric function">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Exciton.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/a/aa/Exciton.png/400px-Exciton.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/a/aa/Exciton.png/600px-Exciton.png 1.5x, /wiki/images/a/aa/Exciton.png 2x"
width="400" height="175" /></a>
<figcaption>When light excites an electron from the valence to the
conduction band, the created hole can bind with the electron to form an
exciton.</figcaption>
</figure>

When an external electric field $\mathbf E$
acts on a medium, both the electronic and ionic charges will react to
the perturbing field. For dielectric materials, in a very simplistic
approach, one can thinkthat the bound charges will create dipoles inside
the medium leading to an induced polarization,
$\mathbf P$. The combined effects of both fields are
expressed in the electric displacement field $\mathbf D$,
given by

$\mathbf D = \mathbf E + 4\pi\mathbf P$.

If the external field is not strong enough to significantly change the
properties of the dielectric medium, one can treat the induced
polarization within the so-called linear response regime. Here, the
information on how the dielectric reacts on the external field is given
by the **dielectric function**:

$\epsilon_{\alpha\beta} = \delta_{\alpha\beta} + 4\pi\frac{\partial
P_i}{\partial E_j}$,

which (assuming that the system has time-reversal symmetry) leads to

$D_\alpha(\omega) = \epsilon_{\alpha\beta}(\omega)E_\beta(\omega)$.

Depending on the nature of the external field, there are different
approaches for the calculation of $\epsilon$. If
$\mathbf E$ is static, then one can rely on perturbative
methods based on finite differences or [density functional perturbation
theory](../theory/Electric_field_response_from_density-functional-perturbation_theory.md)
(DFPT). However, if the perturbation is a time-dependent
$\mathbf E$-field, (e.g., in measurements of the optical
absorption, reflectance, magneto-optical Kerr effect (MOKE), etc.), the
response will depend on the frequency of the external field. For these
cases, one must employ methods based on time-dependent linear response,
(e.g., Green-Kubo) or many-body perturbation theory.

Below we present an overview of all possible cases where VASP employs
either one of such methods for the calculation of
$\epsilon$.

### Static response\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Static response">edit</a> \| (./index.php.md)\]

#### [LEPSILON](../incar-tags/LEPSILON.md): density-functional-perturbation theory (DFPT)\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: LEPSILON: density-functional-perturbation theory (DFPT)">edit</a> \| (./index.php.md)")\]

By setting [LEPSILON](../incar-tags/LEPSILON.md)=.True., VASP uses
[DFPT](../theory/Electric_field_response_from_density-functional-perturbation_theory.md)
to compute the static ion-clamped dielectric matrix with or without
local field effects ([LRPA](../incar-tags/LRPA.md)). Derivatives are
evaluated using Sternheimer equations, avoiding the explicit computation
of derivatives of the periodic part of the wave function. This method
does not require the inclusion of empty states via
[NBANDS](../incar-tags/NBANDS.md).

At the end of the calculation, both the values of
$\epsilon$ including ([LRPA](../incar-tags/LRPA.md)=.True.)
or excluding ([LRPA](../incar-tags/LRPA.md)=.False.) local-field effects are
printed in the [OUTCAR](../output-files/OUTCAR.md) file. Perform a
consistency check by comparing the values excluding local-field effects
and static limit of $\epsilon$
obtained with [LOPTICS](../incar-tags/LOPTICS.md)=.True., i.e.,
$\lim_{\omega\to0}\epsilon(\omega)$.

#### [LCALCEPS](../incar-tags/LCALCEPS.md): finite differences approach\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: LCALCEPS: finite differences approach">edit</a> \| (./index.php.md)\]

With [LCALCEPS](../incar-tags/LCALCEPS.md)=.True., the dielectric tensor
is computed from the derivative of the polarization, using

$\epsilon^\infty_{ij}=\delta_{ij}+
\frac{4\pi}{\epsilon_0}\frac{\partial P_i}{\partial \mathcal{E}_j}
\qquad {i,j=x,y,z}.$

However, here the derivative is evaluated explicitly by employing finite
differences. The direction and intensity of the perturbing electric
field have to be specified in the [INCAR](../input-files/INCAR.md) file
using the [EFIELD_PEAD](../incar-tags/EFIELD_PEAD.md) tag. As with
DFPT, at the end of the calculation, VASP will write the dielectric
tensor in the [OUTCAR](../output-files/OUTCAR.md) file. Control over the
inclusion of local-field effects is done with the variable
[LRPA](../incar-tags/LRPA.md).

### Dynamical response: Green-Kubo and many-body perturbation theory\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Dynamical response: Green-Kubo and many-body perturbation theory">edit</a> \| (./index.php.md)\]

#### [LOPTICS](../incar-tags/LOPTICS.md): Green-Kubo formula\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: LOPTICS: Green-Kubo formula">edit</a> \| (./index.php.md)\]

[LOPTICS](../incar-tags/LOPTICS.md) allows for the evaluation of the
frequency-dependent dielectric function once the ground state is
computed. It uses the explicit expression to evaluate the imaginary part
of $\epsilon$:

$\epsilon^{(2)}_{\alpha \beta}\left(\omega\right) = \frac{4\pi^2
e^2}{\Omega} \mathrm{lim}_{q \rightarrow 0} \frac{1}{q^2}
\sum_{c,v,\mathbf{k}} 2 w_\mathbf{k} \delta( \epsilon_{c\mathbf{k}} -
\epsilon_{v\mathbf{k}} - \omega) \times \langle
u_{c\mathbf{k}+\mathbf{e}_\alpha q} | u_{v\mathbf{k}} \rangle
\langle u_{v\mathbf{k}} | u_{c\mathbf{k}+\mathbf{e}_\beta q}
\rangle,$

while the real part is evaluated using the Kramers-Kroing relation. At
this level, there are no effects coming from local fields.

This method requires two steps: First, obtain the electronic ground
state. Secondly, increase the value of [NBANDS](../incar-tags/NBANDS.md)
in the [INCAR](../input-files/INCAR.md) file to include unoccupied states.
Always check for convergence w.r.t. the number of unoccupied states.

Furthermore, the [INCAR](../input-files/INCAR.md) should also include values
for [CSHIFT](../incar-tags/CSHIFT.md) (the broadening applied to the
Lorentzian function which replaces the $\delta$-function), and [NEDOS](../incar-tags/NEDOS.md) (the
frequency grid for $\omega$).

#### [ALGO](../incar-tags/ALGO.md) = TDHF: Casida equation\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: ALGO = TDHF: Casida equation">edit</a> \| (./index.php.md)\]

This option performs a [time-dependent
Hartree-Fock](../tutorials/Bethe-Salpeter-equations_calculations.md)
or [time-dependent density-functional-theory
(TDDFT)](../tutorials/Bethe-Salpeter-equations_calculations.md)
calculation. It follows the Casida equation and uses a Fourier transform
of the time-evolving dipoles to compute $\epsilon$.

The number of [NBANDS](../incar-tags/NBANDS.md) controls how many bands
are present in the time evolution. This can be fewer empty states
compared to [LOPTICS](../incar-tags/LOPTICS.md).

The choice of time-dependent kernel is controlled by
[AEXX](../incar-tags/AEXX.md), [HFSCREEN](../incar-tags/HFSCREEN.md), and
[LFXC](../incar-tags/LFXC.md) tags. For calculations using hybrid
functionals, [AEXX](../incar-tags/AEXX.md) controls the fraction of exact
exchange used in the exchange-correlation potential, while
[HFSCREEN](../incar-tags/HFSCREEN.md) specifies the range-separation
parameter. For a pure TDDFT calculation, [LFXC](../incar-tags/LFXC.md) uses
the local exchange-correlation kernel in the time-evolution equations.

#### [ALGO](../incar-tags/ALGO.md) = TIMEEV: delta-pulse electric field\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: ALGO = TIMEEV: delta-pulse electric field">edit</a> \| (./index.php.md)\]

Uses a delta-pulse electric field to probe all transitions and calculate
the dielectric function by following the
<a href="/wiki/Time_Evolution" class="mw-redirect"
title="Time Evolution">evolution in time of the dipole momenta</a>. This
algorithm is able to fully reproduce the absorption spectra from
standard <a href="/wiki/Bethe-Salpeter_equations" class="mw-redirect"
title="Bethe-Salpeter equations">Bethe-Salpeter calculations</a> by
setting the correct time-dependent kernel with
[LHARTREE](../incar-tags/LHARTREE.md)=.True. and
[LFXC](../incar-tags/LFXC.md)=.True.

The time step is controlled automatically by the
[CSHIFT](../incar-tags/CSHIFT.md) and [PREC](../incar-tags/PREC.md). This
means that the smaller the value of [CSHIFT](../incar-tags/CSHIFT.md) and
the more accurate the level of precision chosen by the user, the higher
the number of time steps that VASP will perform, and the higher the cost
of the calculation.

The number of valence and conduction bands involved in the time
propagation is set by the [NBANDSO](../incar-tags/NBANDSO.md) and
[NBANDSV](../incar-tags/NBANDSV.md) tags, respectively. Choose a small
number of bands near the band gap to reproduce optical measurements.

Finally, the maximum energy used in both the Fourier transform and in
calculating the frequency-dependent dielectric function is set by
[OMEGAMAX](../incar-tags/OMEGAMAX.md), and the sampling of the frequency
grid is controlled by [NEDOS](../incar-tags/NEDOS.md).

#### [ALGO](../incar-tags/ALGO.md) = CHI: polarizability within RPA approximation\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: ALGO = CHI: polarizability within RPA approximation">edit</a> \| (./index.php.md)\]

Here, the frequency dielectric function is computed within the
Random-Phase approximation. VASP will compute the polarizability
$\chi$ by setting [ALGO](../incar-tags/ALGO.md)=Chi in the
[INCAR](../input-files/INCAR.md) file and then use

$\epsilon^{-1}_{\mathbf G\mathbf G'}(\mathbf q,\omega) =
\delta_{\mathbf G\mathbf G'} + v(\mathbf q+\mathbf G)\chi_{\mathbf
G\mathbf G'}(\mathbf q,\omega)$

to compute the dielectric function. Here, $v$ is the
bare Coulomb potential describing electron-electron interaction. This
requires increasing [NBANDS](../incar-tags/NBANDS.md) to include
unoccupied states as generally the case for [GW
calculations](../methods/GW_and_dielectric_matrix.md).

Two methods for computing the polarizability are available: For
[LSPECTRAL](../incar-tags/LSPECTRAL.md)=.True., VASP will avoid direct
computation of $\chi$ and use
a fast matrix-vector product. However, this can introduce spurious peaks
at low frequencies for some values of [CSHIFT](../incar-tags/CSHIFT.md)
and [NOMEGA](../incar-tags/NOMEGA.md). The second method computes
$\chi$ directly and is activated by setting
[LSPECTRAL](../incar-tags/LSPECTRAL.md)=.False.. However, it is much
slower than the former method.

#### [ALGO](../incar-tags/ALGO.md) = BSE: macroscopic dielectric function including excitons\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: ALGO = BSE: macroscopic dielectric function including excitons">edit</a> \| (./index.php.md)\]

Setting [ALGO](../incar-tags/ALGO.md)=BSE computes the macroscopic
dielectric function $\epsilon_M$
by solving the
<a href="/wiki/Bethe-Salpeter_equations" class="mw-redirect"
title="Bethe-Salpeter equations">Bethe-Salpeter equations</a>. The
electron-hole pairs are treated as a new quasi-particle called exciton,
and the dielectric function is built using the eigenvectors
($X_{\lambda}^{cv\mathbf k}$) and eigenvalues
($\omega_\lambda$):

$\epsilon_M(\mathbf{q},\omega)= 1+v(\mathbf q)\sum_{\lambda\lambda'}
\sum_{c,v,\mathbf k}\sum_{c',v',\mathbf k'}\langle
c\mathbf{k}|e^{i\mathbf{qr}}|v\mathbf{k}\rangle
X_\lambda^{cv\mathbf{k}} \langle
c'\mathbf{k'}|e^{-i\mathbf{qr}}|v'\mathbf{k'}\rangle
X_{\lambda'}^{c'v'\mathbf{k}',\*}\times S^{-1}_{\lambda,\lambda'}
\left(\frac{1}{\omega_\lambda - \omega - i\delta} +
\frac{1}{\omega_\lambda+\omega + i\delta}\right)~.$

Here, $S_{\lambda\lambda'}$ is the overlap between exciton states of indices
$\lambda$ and $\lambda'$ (in
general, the BSE Hamiltonian is not hermitian, so eigenstates associated
to different eigenvalues are not necessarily orthogonal).

The number of occupied and unoccupied states that are included in the
BSE Hamiltonian is controlled by the [NBANDSO](../incar-tags/NBANDSO.md)
and [NBANDSV](../incar-tags/NBANDSV.md), respectively. Normally only a
few bands above and below the band gap are required to converge the
optical spectrum, and the memory requirements increase quickly with the
number of bands. Thus, be careful in setting up these two tags.

Regarding the comparison with optical experiments, (e.g., absorption,
MOKE, reflectance), $q$ is the
photon momentum. Often, the $\mathbf q \to 0$ limit is considered. Furthermore, the coupling between
the resonant and anti-resonant terms can be switched off, in what is
called the <a
href="/wiki/Bethe-Salpeter_equations#Theory#Tamm-Dancoff_approximation"
class="mw-redirect" title="Bethe-Salpeter equations">Tamm-Dancoff
approximation</a>. This approximation can be activated with the variable
[ANTIRES](../incar-tags/ANTIRES.md) set to 0. Setting this variable to 1
or 2 will include the coupling, but increase the computational cost.

## Level of approximation\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Level of approximation">edit</a> \| (./index.php.md)\]

### Microscopic and macroscopic quantities\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Microscopic and macroscopic quantities">edit</a> \| (./index.php.md)\]

It is important to distinguish between macroscopic quantities, measured
over several repetitions of the unit cell, and microscopic quantities,
which include fields that change rapidly in all regions of the unit
cell.

When measuring a property experimentally, it is the macroscopic version
that will be represented in the experimental data. On the other hand,
computationally, the microscopic quantities are more accessible. In
other words, in order to compare experimental and computational results,
the microscopic quantities, e.g., the dielectric function, must be
averaged over several repetitions of the unit cell. It is possible to
show that the macroscopic dielectric function,
$\epsilon_M(\mathbf q,\omega)$ is related to the
microscopic one via

$\epsilon_M(\mathbf q,\omega) = \frac{1}{\epsilon_{\mathbf G = 0,
\mathbf G'=0}^{-1}(\mathbf q,\omega)}$

where $\epsilon_{\mathbf G = 0,
\mathbf G'=0}^{-1}(\mathbf q,\omega)$ is the inverse
dielectric function at $\mathbf G = \mathbf G'=0$.

Note that this does not mean that $\epsilon_M(\mathbf q,\omega) =
\epsilon_{\mathbf G = 0, \mathbf G'=0}(\mathbf q,\omega)$! The full matrix $\epsilon_{\mathbf G, \mathbf
G'}(\mathbf q,\omega)$ has to be inverted and it is the
component at $\mathbf G = \mathbf G'=0$ that is used to calculate $\epsilon_M(\mathbf q,\omega)$.

### Finite momentum dielectric function\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Finite momentum dielectric function">edit</a> \| (./index.php.md)\]

In the optical limit, the momentum of the incoming photon,
$\mathbf q$, is almost zero, since the wavelength of the
electric field is several times larger than the dimensions of the unit
cell. Since the Coulomb potential diverges at very small momenta, the
optical limit of the dielectric function must be obtained by taking with
the limit of $\mathbf q\to 0$ instead of setting $\mathbf q\to 0$. For instance, in the case of the independent particle
approximation of full BSE, one yields

$\lim_{\mathbf q\to0}\frac{\langle c\mathbf k + \mathbf q|e^{\mathrm
i\mathbf q\cdot\mathbf r}|v\mathbf k\rangle}{q} \approx \lim_{\mathbf
q\to0}\frac{\langle c\mathbf k+\mathbf q|1 + \mathrm i\mathbf
q\cdot\mathbf r|v\mathbf k\rangle}{q} = \hat{\mathbf{q}}\cdot \langle
c\mathbf k+\mathbf q|\mathbf r|v\mathbf k\rangle.$

VASP can also analyze the effects of finite momentum excitons. This is
important, e.g., in the case of the optical absorption of bulk hexagonal
BN. To calculate the absorption spectrum at finite momentum, set
[KPOINT_BSE](../incar-tags/KPOINT_BSE.md) to the index of the desired
**q** point.

### Local fields in the Hamiltonian\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Local fields in the Hamiltonian">edit</a> \| (./index.php.md)\]

Local fields, i.e., terms with finite $\mathbf G$,
can be turned on or off in the Coulomb potential when evaluating the
polarizability. VASP will distinguish the results in the
[OUTCAR](../output-files/OUTCAR.md) file with:

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects) 

    BORN EFFECTIVE CHARGES (including local field effects) 

    PIEZOELECTRIC TENSOR (including local field effects) 

and

    MACROSCOPIC STATIC DIELECTRIC TENSOR (excluding local field effects) 

    BORN EFFECTIVE CHARGES (excluding local field effects) 

    PIEZOELECTRIC TENSOR (excluding local field effects)

for both cases.

Another approximation can also be taken, where the contributions from
the exchange-correlation kernel are neglected when evaluating the
polarizability. This is equivalent to the so-called random-phase
approximation (RPA) and can be activated by setting
[LRPA](../incar-tags/LRPA.md)=.True. in the [INCAR](../input-files/INCAR.md).

### Ion-clamped vs relaxed-ion/dressed dielectric function\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Ion-clamped vs relaxed-ion/dressed dielectric function">edit</a> \| (./index.php.md)\]

The dielectric function computed either in the static or dynamical
response regimes does not consider the effects coming from changes of
the ionic positions due to the incoming electric field. This can be
corrected by computing the relaxed-ion (or dressed) dielectric function
$\bar\epsilon$[^wu:prb:2005-1]

$\bar\epsilon_{\alpha\beta} = \epsilon_{\alpha\beta} +
\Omega_0^{-1}Z_{m\alpha}(\Phi^{-1})_{mn}Z_{n\beta},$

where $\Omega_0$ is
the volume of the unit cell, $Z_{n\alpha}$
is the Born effective charge, and $\Phi_{mn}$
is the force constants matrix.

### Density-density versus current-current response functions\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Density-density versus current-current response functions">edit</a> \| (./index.php.md)\]

The inclusion of an electromagnetic field in the Hamiltonian is subject
to a gauge choice. For instance, a classical electric field can be
described by either a scalar potential $\phi$ or a
longitudinal vector potential $\mathbf A$ in
the incomplete Weyl gauge ($\phi$ = 0).
The former means that the perturbing potential couples to the electronic
density, while the second, implies a vector potential couples to a
current. The fundamental consequence is that one can define two
different response functions: a density-density response function for
the first, $\chi_{\rho\rho}$; and a current-current response function,
$\chi_{jj}$. This circumstance is a common source of
error when comparing experimental and computational optical properties
of periodic systems, as discussed by Sangalli et
al.[^sangalli:prb:2017-2].

Infact, perturbations associated with longitudinal fields will be
described by the density-density polarisability function
$\chi_{\rho\rho}$, (e.g., laser fields taken in the
classical limit), while transverse fields will be described by the
current-current polarizability $\chi_{jj}$,
which is in fact a 3x3 tensor, (e.g., required to obtain the MOKE).
Fundamentally, the time-dependent density is associated only with the
longitudinal part of the current via the continuity equation. This also
links both response functions via

$q^2 \chi_{jj}(\mathbf q,\omega) = \omega^2\chi_{\rho\rho}(\mathbf q,
\omega).$

It guarantees that the dielectric functions obtained from either
approach match at finite momentum and frequency:
$\epsilon\[\chi_{\rho\rho}\]= \epsilon\[\chi_{jj}\]$.

The current-current dielectric function is exact at both
$\mathbf q \to 0$ and at $\mathbf q = 0$. Especially for metals, it will reproduce the proper
behavior of the Drude tail at $\omega=0$.
However, $\chi_{jj}$
is more prone to numerical instabilities.

## Other dielectric properties\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Other dielectric properties">edit</a> \| (./index.php.md)\]

### Electron energy loss spectroscopy (EELS)\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: Electron energy loss spectroscopy (EELS)">edit</a> \| (./index.php.md)")\]

In
[EELS](../tutorials/Electron-energy-loss_spectrum.md)
experiments a narrow beam of electrons with a well defined energy is
shot at the sample. These electrons then lose energy to the sample by
exciting plasmons, electron-hole pairs, or other higher-order
quasiparticles. The loss function can then be expressed as

$\mathrm{EELS} = -\mathrm{Im}\left\[\epsilon^{-1}(\omega)\right\].$

### Optical conductivity\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: Optical conductivity">edit</a> \| (./index.php.md)\]

From Maxwell's equations and the microscopic form of Ohm's law it is
possible to arrive at the following relation between the tensorial
dielectric function and the optical conductivity
$\sigma(\omega)$

$\sigma_{\alpha\beta}(\omega) = \mathrm
i\frac{\omega}{4\pi}\left\[\delta_{\alpha\beta} -
\epsilon_{\alpha\beta}(\omega)\right\].$

### Optical absorption\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: Optical absorption">edit</a> \| (./index.php.md)\]

For an electromagnetic wave traveling through a medium, one can express
the electric field as $\mathbf E(\mathbf r, t) =
\mathbf E_0e^{-\mathrm i(\omega t - \mathbf q \cdot \mathbf r)}$, and the effects of the medium in the wave propagation
are contained inside the dispersion relation $\omega = \omega(\mathbf q)$. Using Maxwell's equations, one can arrive at

$q^2 = \frac{\omega^2}{c^2}\epsilon(\omega).$

If the magnetic permeability of the material is assumed to be equal to
that of vacuum, the equation above implies that the refractive index can
be written as $n = \sqrt{\epsilon(\omega)} =
\tilde{n} + \mathrm i k$. Since
$n$ is complex, the exponential factor in
$\mathbf E(\mathbf r, t)$ will have a dampening factor,
$e^{-\frac{\omega}{c}k\hat q\cdot \mathbf r}$, which
accounts for the absorption of electromagnetic energy by the medium.
With this relation one can define the absorption coefficient,
$\alpha(\omega)$ as

$\alpha(\omega) = \frac{2\omega}{c}k(\omega).$

### X-ray absorption\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=21"
class="mw-editsection-visualeditor"
title="Edit section: X-ray absorption">edit</a> \| (./index.php.md)\]

<a href="/wiki/XAS" class="mw-redirect" title="XAS">Core-state
excitations</a> can be modeled using two main approaches:

- [the supercell core-hole
  method](../tutorials/Supercell_core-hole_calculations.md)
- [the Bethe–Salpeter
  equation](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md).

In both cases, the interaction between the excited electron and the core
hole can be included. In the supercell core-hole approach, the core-hole
is introduced explicitly by removing an electron and then relaxing the
charge density in the presence of the core hole. The dielectric function
is then found within the independent-particle approximation via

$\varepsilon_{\alpha \alpha}^{(2)}(\omega)= \frac{4 \pi^2 e^2
\hbar^2}{\Omega \omega^2 m_e^2} \sum_{\text{core}, c, \mathbf{k}} 2
w_{\mathbf{k}} |\left\langle\psi_{c \mathbf{k}}\right| i
\nabla_\alpha-\mathbf{k}_\alpha\left|\psi_{\text{core}}\right\rangle|^2\delta\left(\varepsilon_{c
\mathbf{k}}-\varepsilon_{\text{core}}-\omega\right).$

In the BSE approach, core-state excitations are included explicitly in
the response-function calculation. As a result, the electron-core-hole
interaction enters the dielectric function through the eigenvectors of
the two-particle Hamiltonian $A^\lambda$:

$\varepsilon_{\alpha \alpha}^{(2)}(\omega)= \frac{4 \pi^2 e^2
\hbar^2}{\Omega \omega^2 m_e^2}
\sum_\lambda\left|\sum_{\text{core},c, \mathbf{k}} 2A_{\text{core},
c \mathbf{k}}^\lambda \left\langle\psi_{c \mathbf{k}}\right| i
\nabla_\alpha-\mathbf{k}_\alpha\left|\psi_{\text{core}}\right\rangle
\right|^2 \delta\left(\varepsilon^\lambda-\omega\right).$

### Reflectance\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=22"
class="mw-editsection-visualeditor"
title="Edit section: Reflectance">edit</a> \| (./index.php.md)\]

From the previous subsection, one can also define the reflectivity
coefficient at normal incidence as

$R
= \frac{(1-\tilde n)^2 + k^2}{(1+\tilde n)^2 + k^2}.$

This equation can be generalized for any angle of incidence
$\theta$, resulting in the general form of Fresnel
equations.

### Magneto-optical Kerr effect (MOKE)\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=23"
class="mw-editsection-visualeditor"
title="Edit section: Magneto-optical Kerr effect (MOKE)">edit</a> \| (./index.php.md)")\]

The incoming electromagnetic wave interacts with the finite magnetic
moment of the material. Usually, the interaction is with the
magnetization of the medium, but there are also antiferromagnetic
systems that can observe a finite MOKE. Generally, the reflected wave
will gain an extra complex phase with respect to the incident
$\mathbf E$-field. For a surface or two-dimensional
material, (e.g., hexagonal BN, MoS$_2$), this
phase can be computed using the off-diagonal components of the
current-current dielectric tensor:

$\theta_\mathrm K(\omega) =
-\mathrm{Re}\left\[\frac{\epsilon_{xy}(\omega)}{(\epsilon_{xx}(\omega)-1)\sqrt{\epsilon_{xx}(\omega)}}\right\].$

## Electric response combined with perturbations of the ionic degrees of freedom\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=24"
class="mw-editsection-visualeditor"
title="Edit section: Electric response combined with perturbations of the ionic degrees of freedom">edit</a> \| (./index.php.md)\]

### Low-frequency corrections from atomic displacements\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=25"
class="mw-editsection-visualeditor"
title="Edit section: Low-frequency corrections from atomic displacements">edit</a> \| (./index.php.md)\]

The corrections from ionic motion to the low frequency regime can be
added to $\epsilon_{\alpha\beta}^\infty$
following[^gonze:prb:1997-3]

$\epsilon_{\alpha\beta}(\omega) = \epsilon_{\alpha\beta}^\infty +
\frac{4\pi
e^2}{\Omega_0}\sum_\nu\frac{S_{\alpha\beta,\nu}}{\omega_\nu^2 -
(\omega+\mathrm i\eta)^2},$

where $\omega_\nu$
is the phonon frequency of mode $\nu$, and
$S_{\alpha\beta,\nu}$ is the mode-oscillator strength,
defined by

$S_{\alpha\beta,\nu} =
\left(\sum_{I,\delta}Z^\*_{I\alpha\delta}\varepsilon^\*_{I\delta,\nu}(\mathbf{q
=
0})\right)\left(\sum_{J,\delta'}Z^\*_{J\beta\delta'}\varepsilon_{J\delta',\nu}(\mathbf{q
= 0})\right).$

Here $Z^\*_{J\beta\delta'}$ are the Born effective charges and
$\varepsilon_{J\delta',\nu}(\mathbf{q = 0})$ are the
eigendisplacements associated with the vibration mode
$\nu$ for atom $J$ along
direction $\delta'$.
More information on the theory and methods behind the computation of
phonon frequencies and eigendisplacements can be found in the
[phonons](../theory/Phonons-_Theory.md) dedicated page.

Inclusion of the low-frequency corrections can be activated in the
[INCAR](../input-files/INCAR.md) file with either
[IBRION](../incar-tags/IBRION.md) = 5,6 (finite differences) or 7,8
(DFPT), and by setting to .True. the variables
[LEPSILON](../incar-tags/LEPSILON.md) or
[LCALCEPS](../incar-tags/LCALCEPS.md).

#### Polar materials\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=26"
class="mw-editsection-visualeditor"
title="Edit section: Polar materials">edit</a> \| (./index.php.md)\]

For polar materials it is important to recall that there is a
discontinuity near $\Gamma$, i.e.
$\omega^2_\nu(\mathbf{q\to 0}) \neq \omega^2_\nu(\mathbf{q= 0})$, and in fact, for a given unitary directional vector
$\mathbf q$, it can be shown that the
Lyddane-Sachs-Teller relationship
holds[^gonze:prb:1997-3]

$\prod_\nu\frac{\omega^2_\nu(\mathbf{q \to
0})-\omega^2}{\omega^2_\nu(\mathbf{q= 0}) - \omega^2} =
\frac{\sum_{\alpha\beta}q_\alpha\epsilon_{\alpha\beta}(\omega)q_\beta}{\sum_{\alpha\beta}q_\alpha\epsilon_{\alpha\beta}^\infty
q_\beta},$

meaning that the splitting in frequencies between the LO and TO modes at
zero momentum carries over the evaluation of the dielectric function.

In order to obtain smooth phonon dispersions and to properly account for
the LO-TO splitting in the evaluation of the optical limit of the
dielectric function, users should read the dedicated page on [LO-TO
splitting](../theory/Phonons-_Theory.md) "Phonons: Theory"),
where it is explained how to set the variables
[LPHON_POLAR](../incar-tags/LPHON_POLAR.md),
[PHON_DIELECTRIC](../incar-tags/PHON_DIELECTRIC.md), and
[PHON_BORN_CHARGES](../incar-tags/PHON_BORN_CHARGES.md) in the
[INCAR](../input-files/INCAR.md) file.

### Corrections from strain\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=27"
class="mw-editsection-visualeditor"
title="Edit section: Corrections from strain">edit</a> \| (./index.php.md)\]

The dielectric tensor can also be included in the evaluation of the
elastic tensor, $C_{jk}$,
(see [theory of static linear
response](../theory/Static_linear_response-_theory.md)
for more information on derived quantities from the static linear
response). While this quantity is normally evaluated at fixed
$\mathbf E$-field, in cases where a thin film is placed
between layers of insulating materials, it is more convenient to
evaluate the elastic tensor for fixed displacement field
$\mathbf D$, since the boundary conditions fix the
components of this vector in the direction normal to the surface.

If $C^E_{jk}$ is the elastic tensor defined at fixed
$\mathbf E$-field and $C^D_{jk}$
the elastic tensor defined at fixed $\mathbf D$-field, then they are related by

$C^D_{jk} = C^E_{jk} + e_{\alpha
j}(\epsilon)^{-1}_{\alpha\beta}e_{\beta k},$

where $e_{\alpha j}$ is the ion-relaxed piezoelectric tensor.

## Additional resources\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=28"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Lectures\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=29"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on
  <a href="https://youtu.be/3YKJZHmcGhY" class="external text"
  rel="nofollow">dielectric properties from first principles</a>.
- Lecture on the
  <a href="https://youtu.be/6F_WNIh6V7I" class="external text"
  rel="nofollow">optical bandgap</a>.

### Tutorials\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=30"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorials for
  <a href="https://www.vasp.at/tutorials/latest/response/part1"
  class="external text" rel="nofollow">linear response</a>.
- Tutorials for <a href="https://www.vasp.at/tutorials/latest/gw/part1"
  class="external text" rel="nofollow">GW approximation</a>.
- Tutorials for <a href="https://www.vasp.at/tutorials/latest/bse/"
  class="external text" rel="nofollow">Bethe-Salpeter equation (BSE)</a>.

## References\[<a
href="/wiki/index.php?title=Category:Dielectric_properties&amp;veaction=edit&amp;section=31"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^wu:prb:2005-1]: [X. Wu, D. Vanderbilt, and D. R. Hamann, Phys. Rev. B **72**, 035105 (2005).](https://doi.org/10.1103/PhysRevB.72.035105)
[^sangalli:prb:2017-2]: [Davide Sangalli, J. A. Berger, Claudio Attaccalite, Myrta Grüning, and Pina Romaniello, *Optical properties of periodic systems within the current-current response framework: Pitfalls and remedies* , Phys. Rev. B **95**, 155203 (2017)](https://doi.org/10.1103/PhysRevB.95.155203)
[^gonze:prb:1997-3]: [X. Gonze and C. Lee, *Dynamical matrices, Born effective charges, dielectric permittivity tensors, and interatomic force constants from density-functional perturbation theory*, Phys. Rev. B **55**, 10355 (1997).](http://doi.org/10.1103/PhysRevB.55.10355)

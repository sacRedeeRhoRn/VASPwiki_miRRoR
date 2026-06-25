<!-- Source: https://vasp.at/wiki/index.php/Electronic_transport_coefficients | revid: 34116 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Electronic transport coefficients


The theoretical framework is based on the [linearized Boltzmann
transport equation
(BTE)](Electron-phonon_interactions_theory.md)
within the relaxation time approximation (RTA). We employ the
frozen-band approximation, which assumes that the electronic potential
and eigenvalues computed for the undoped system remain unchanged when
electrons are added or removed. The goal of this page is to explain how
to compute the electronic lifetimes, scattering rates, and transport
coefficients such as the electrical conductivity, Seebeck coefficient,
and the electronic thermal conductivity. If you would like to plot the
scattering lifetimes or the electron-phonon matrix elements, see the <a
href="https://www.vasp.at/tutorials/latest/electron-phonon/part4/#electron-phonon-e12"
class="external text" rel="nofollow">end of Exercise 12</a> and <a
href="https://www.vasp.at/tutorials/latest/electron-phonon/part3/#electron-phonon-e08"
class="external text" rel="nofollow">Exercise 9</a> of the
electron-phonon tutorials, respectively.


## Contents


- [1
  Electron–phonon coupling matrix
  elements](#electronphonon-coupling-matrix-elements)
- [2 Scattering
  rates and lifetimes](#scattering-rates-and-lifetimes)
- [3 Transport
  distribution function](#transport-distribution-function)
- [4 Onsager
  coefficients](#onsager-coefficients)
- [5 Transport
  coefficients](#transport-coefficients)
- [6 Electron and
  hole mobilities in
  semiconductors](#electron-and-hole-mobilities-in-semiconductors)
- [7 Approximations
  and methods](#approximations-and-methods)
- [8 Related tags
  and articles](#related-tags-and-articles)


## Electron–phonon coupling matrix elements\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Electron–phonon coupling matrix elements">edit</a> \| (./index.php.md)\]

The starting point is the set of Kohn–Sham eigenstates obtained from
density functional theory (DFT). For a given Bloch state,

$H_{\mathbf{k}} |\psi_{n\mathbf{k}}\rangle = \epsilon_{n\mathbf{k}}
S_{\mathbf{k}} |\psi_{n\mathbf{k}}\rangle,$

where $n$ is the
band index, $\mathbf{k}$
is a crystal momentum, and $S_{\mathbf{k}}$ is the overlap matrix. The scattering with phonons is
described by the electron–phonon coupling matrix elements

$g_{n\mathbf{k},n'\mathbf{k}'}^{\nu\mathbf{q}} = \langle
\psi_{n\mathbf{k}} | \partial_{\nu\mathbf{q}} V |
\psi_{n'\mathbf{k}'} \rangle,$

where $\partial_{\nu\mathbf{q}} V$ is the perturbation of the crystal potential due to a
phonon of branch index $\nu$ and
wavevector $\mathbf{q}$.
These matrix elements determine the scattering probability between
states $(n,\mathbf{k})$ and $(n',\mathbf{k}')$.

## Scattering rates and lifetimes\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Scattering rates and lifetimes">edit</a> \| (./index.php.md)\]

Within Fermi’s golden rule, the inverse lifetime (scattering rate) of an
electron in state $(n,\mathbf{k})$ is

$\frac{1}{\tau_{n\mathbf{k}}} = \frac{2\pi}{\hbar}
\sum_{n'\nu\mathbf{k}'} w_{n\mathbf{k},n'\mathbf{k}'} \\
|g^{\nu\mathbf{q}}_{n\mathbf{k},n'\mathbf{k}'}|^2 \left\[
(n_{\nu\mathbf{q}} + 1 - f_{n'\mathbf{k}'}) \\
\delta(\varepsilon_{n\mathbf{k}} - \varepsilon_{n'\mathbf{k}'} -
\hbar\omega_{\nu\mathbf{q}}) + (n_{\nu\mathbf{q}} +
f_{n'\mathbf{k}'}) \\ \delta(\varepsilon_{n\mathbf{k}} -
\varepsilon_{n'\mathbf{k}'} + \hbar\omega_{\nu\mathbf{q}}) \right\]$

where:

- $f_{n\mathbf{k}}$ is the Fermi–Dirac occupation,
- $n_{\nu\mathbf{q}}$ is the Bose–Einstein phonon
  occupation,
- $\omega_{\nu\mathbf{q}}$ is the phonon frequency.
- $w_{n\mathbf{k},n'\mathbf{k}'}$ weight determined by
  the
  [ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md)

The two terms correspond to phonon emission and absorption,
respectively.

## Transport distribution function\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Transport distribution function">edit</a> \| (./index.php.md)\]

The energy-resolved transport distribution function is

$\mathcal{T}(\epsilon) = \frac{e^2}{N_\mathbf{k}\Omega}
\sum_{n\mathbf{k}} \tau_{n\mathbf{k}} \\ \mathbf{v}_{n\mathbf{k}}
\otimes \mathbf{v}_{n\mathbf{k}} \\
\delta(\epsilon_{n\mathbf{k}}-\epsilon),$

where $\Omega$ is
the unit-cell volume, $\mathbf{v}_{n\mathbf{k}}$ are the carrier velocities,
$\tau_{n\mathbf{k}}$ are the lifetimes, and
$N_\mathbf{k}$ the number of
$\mathbf{k}$-points.

## Onsager coefficients\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Onsager coefficients">edit</a> \| (./index.php.md)\]

The Onsager coefficients relate generalized forces (electric field and
temperature gradient) to generalized fluxes (electronic and heat
currents). In compact matrix form:

$\begin{pmatrix} \mathbf{J}_e \\ \mathbf{J}_q \end{pmatrix} =
\begin{pmatrix} L_{11} & L_{12} \\ L_{21} & L_{22} \end{pmatrix}
\begin{pmatrix} \mathbf{\mathcal{E}} \\ -\nabla T / T \end{pmatrix},$

where

- $\mathbf{J}_e$ = electrical current density,
- $\mathbf{J}_q$ = heat current density carried by the
  electrons,
- $\mathbf{\mathcal{E}} = E + \frac{\nabla\mu}{e}$
  electrochemical potential with $\mu$ the
  [chemical
  potential](Chemical_potential_in_electron-phonon_interactions.md)
- $T$ = temperature.

They are defined as

$L_{ij} = \int d\epsilon \\ \mathcal{T}(\epsilon) \\
(\epsilon-\mu)^{i+j-2} \left( -\frac{\partial f^0}{\partial \epsilon}
\right),$

where $\mathcal{T}(\epsilon)$ is the transport distribution function,
$\mu$ the [chemical
potential](Chemical_potential_in_electron-phonon_interactions.md),
and $f^0$ the
Fermi–Dirac distribution.

|  |
|----|
| **Important:** The [chemical potential](Chemical_potential_in_electron-phonon_interactions.md) is written as $\mu$. The mobility is $\mu_e$ or $\mu_h$, and should not be mistaken for it. |

In practice, this integral can be evaluated in one of two ways
determined by
[ELPH_TRANSPORT_DRIVER](../incar-tags/ELPH_TRANSPORT_DRIVER.md)

Linear energy grids and Simpson rule

The integrand is computed on a linear energy grid, and the Simpson rule
is used for integration. The discretized Onsager coefficient is
evaluated as

$L_{ij} \\\approx\\ \sum_{k=1}^{N} w_k \\ \mathcal{T}(\epsilon_k)\\
(\epsilon_k - \mu)^{\\i+j-2}\\ \left( -\frac{\partial f^0}{\partial
\epsilon} \right).$

with $\epsilon_k =
\epsilon_\text{min}+(k-1)\Delta \epsilon,\\\\ k=1,\dots,N$ and $\Delta \epsilon =
\tfrac{\epsilon_\text{max}-\epsilon_\text{min}}{N-1}$
and $\epsilon_\text{min}$=[ELPH_TRANSPORT_EMIN](../incar-tags/ELPH_TRANSPORT_EMIN.md)
and $\epsilon_\text{max}$=[ELPH_TRANSPORT_EMAX](../incar-tags/ELPH_TRANSPORT_EMAX.md)
or alternatively both $\epsilon_\text{min}$ and $\epsilon_\text{max}$ are set by
[ELPH_TRANSPORT_DFERMI_TOL](../incar-tags/ELPH_TRANSPORT_DFERMI_TOL.md)
and $w_k$ the
weights due to the Simpson integration rule.

Gauss–Legendre quadrature

A change of variables is introduced to avoid explicitly sampling the
sharp derivative of the Fermi–Dirac function. Define

$x
= 1-2f(\epsilon-\mu,T)$

so that $\epsilon = \mu+ k_B T
\ln\frac{1+x}{1-x}$. With this substitution, the
derivative of the Fermi–Dirac distribution is absorbed into the
Jacobian, and the Onsager coefficients take the form

$L_{ij} \\\approx\\ \tfrac{1}{2} \sum_{k=1}^N w_k \\ \left( \frac{k_B
T}{-e} \ln \frac{1+x_k}{1-x_k} \right)^{i+j-2} \mathcal{T}\\\left(\mu+
k_B T \ln\frac{1+x_k}{1-x_k}\right),$

with $w_k$ and
$x_k$ the weights and abscissae of the Gauss-Legendre
quadrature rule.

The Gauss–Legendre approach has the advantage that the integration grid
adapts naturally to the width of the Fermi window, making it numerically
efficient without having define manually the energy window through
[ELPH_TRANSPORT_DFERMI_TOL](../incar-tags/ELPH_TRANSPORT_DFERMI_TOL.md)
or
[ELPH_TRANSPORT_EMIN](../incar-tags/ELPH_TRANSPORT_EMIN.md)
and
[ELPH_TRANSPORT_EMAX](../incar-tags/ELPH_TRANSPORT_EMAX.md).
Instead, only the number of points $N$ in the sum
above needs to be defined through
[TRANSPORT_NEDOS](../incar-tags/TRANSPORT_NEDOS.md).

## Transport coefficients\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Transport coefficients">edit</a> \| (./index.php.md)\]

|  |  |  |
|----|----|----|
| Quantity | Formula | Physical meaning |
| Electrical conductivity $\sigma$ | $\sigma = L_{11}$ | Charge current response to an electric field |
| Seebeck coefficient $S$ | $S = \tfrac{1}{T} L_{11}^{-1} L_{12}$ | Voltage generated per temperature gradient |
| Peltier coefficient $\Pi$ | $\Pi = T S = L_{11}^{-1} L_{12}$ | Heat carried per unit charge current |
| Electronic thermal conductivity $\kappa_e$ | $\kappa_e = \tfrac{1}{T} ( L_{22} - L_{21} L_{11}^{-1} L_{12} )$ | Heat current carried by electrons in response to a thermal gradient |

The lattice thermal conductivity $\kappa_l$,
i.e., the heat current carried by the lattice in response to a thermal
gradient, can be computed using the [Müller-Plathe
method](../tutorials/Müller-Plathe_method.md) or with
an external package such as
<a href="https://phonopy.github.io/phono3py/" class="external text"
rel="nofollow">phono3py</a>.

## Electron and hole mobilities in semiconductors\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Electron and hole mobilities in semiconductors">edit</a> \| (./index.php.md)\]

In semiconductors, the electrical conductivity can be separated into
contributions from conduction-band electrons and valence-band holes.
This is only meaningful in materials with a finite band gap, where
carriers can be clearly identified as either electrons in the conduction
band (CB) or holes in the valence band (VB).

|  |
|----|
| **Important:** Be careful not to mistake the [chemical potential](Chemical_potential_in_electron-phonon_interactions.md) $\mu$ for the mobility $\mu_e$ or $\mu_h$. |

|  |  |  |
|----|----|----|
| Quantity | Definition | Carrier density |
| Electron mobility $\mu_e$ | $\mu_e = \tfrac{\sigma_{n \in \text{CB}}}{n_e}$ | $n_e = \frac{1}{\Omega N_\mathbf{k}}\sum_{\mathbf{k}n \in \text{CB}} f(\varepsilon_{\mathbf{k}n}, T, \mu)$ |
| Hole mobility $\mu_h$ | $\mu_h = \tfrac{\sigma_{n \in \text{VB}}}{n_h}$ | $n_h = \frac{1}{\Omega N_\mathbf{k}}\sum_{\mathbf{k}n \in \text{VB}} \big\[1 - f(\varepsilon_{\mathbf{k}n}, T, \mu)\big\]$ |

Here:

- $\sigma_{n \in \text{CB}}$ and
  $\sigma_{n \in \text{VB}}$ denote the conductivity
  restricted to states in the conduction and valence bands,
  respectively.
- $f_{n\mathbf{k}}$ is the Fermi–Dirac distribution.
- $\Omega$ is the volume of the unit cell.
- $N_\mathbf{k}$ is the total number of k-points.
- $\mu$ is the [chemical
  potential](Chemical_potential_in_electron-phonon_interactions.md)
  at the given temperature.

## Approximations and methods\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Approximations and methods">edit</a> \| (./index.php.md)\]

- Tetrahedron method: used for Brillouin-zone integration, avoiding the
  need for ad-hoc smearing parameters.
- Plane-wave Bloch states: ensure systematic convergence and avoid
  interpolation errors.
- Selection algorithms: restrict scattering processes to those allowed
  by energy conservation (delta functions), minimizing the number of
  matrix elements to compute.

## Related tags and articles\[<a
href="/wiki/index.php?title=Electronic_transport_coefficients&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Band-structure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)
- [Transport coefficients including electron-phonon
  scattering](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Chemical potential in electron-phonon
  interactions](Chemical_potential_in_electron-phonon_interactions.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
- [Electron-phonon interactions from Monte-Carlo
  sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md)
- [ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md)
- [ELPH_TRANSPORT_DRIVER](../incar-tags/ELPH_TRANSPORT_DRIVER.md)



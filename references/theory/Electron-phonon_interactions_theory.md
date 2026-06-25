<!-- Source: https://vasp.at/wiki/index.php/Electron-phonon_interactions_theory | revid: 35880 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Electron-phonon interactions theory


This theory section outlines the most important equations and their
physical meaning in the context of electron-phonon calculations using
VASP. It covers the theory of electron-phonon interactions in the two
approaches implemented:

- Electron-phonon interactions from perturbation theory
- Electron-phonon interactions from statistical sampling

For each section, additional theory pages are linked, along with
corresponding how-to's


## Contents


- [1
  Electron-phonon interactions from perturbation
  theory](#Electron-phonon_interactions_from_perturbation_theory)
  - [1.1 Electron
    self-energy](#Electron_self-energy)
    - [1.1.1
      Band-structure
      renormalization](#Band-structure_renormalization)
    - [1.1.2
      Transport
      coefficients](#Transport_coefficients)
- [2
  Electron-phonon interactions from statistical
  sampling](#Electron-phonon_interactions_from_statistical_sampling)
  - [2.1 Full Monte
    Carlo sampling](#Full_Monte_Carlo_sampling)
  - [2.2 ZG
    configuration (one-shot
    method)](#ZG_configuration_(one-shot_method))
- [3
  References](#References)


## Electron-phonon interactions from perturbation theory\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Electron-phonon interactions from perturbation theory">edit</a> \| (./index.php.md)\]

One can obtain these quantities rigorously from many-body perturbation
theory and then apply approximations to make the calculations feasible
at the DFT level. For a comprehensive theoretical description of
electron-phonon interactions using many-body perturbation theory, we
recommend to read Ref.
<sup>[\[1\]](#cite_note-giustino:rmp:2017-1)</sup>
or other contemporary literature.

### Electron self-energy\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Electron self-energy">edit</a> \| (./index.php.md)\]

The interaction between electrons and lattice vibrations (phonons) leads
to a modification of the electronic energies, described by the electron
<a href="https://en.wikipedia.org/wiki/Self-energy"
class="external text" rel="nofollow">self-energy</a>,
$\Sigma_{n\mathbf{k}}(E, T)$, for the band
$n$ and wavevector $\mathbf{k}$
at energy $E$ and
temperature $T$ (often,
the energy dependence is written as a frequency dependence,
$\hbar \omega$). This complex quantity has a real part,
$\text{Re}\[\Sigma_{n\mathbf{k}}(E, T)\]$, which
represents the shift or "renormalization" of the electron's energy. The
imaginary part, $\text{Im}\[\Sigma_{n\mathbf{k}}(E, T)\]$, describes
the finite lifetime of the electronic state due to scattering with
phonons.

Using second-order perturbation theory, the electron self-energy can be
separated into two contributions: the
[Fan-Migdal](../incar-tags/ELPH_SELFEN_FAN.md) (FM) and
[Debye-Waller](../incar-tags/ELPH_SELFEN_DW.md) (DW) terms:

$\Sigma_{n\mathbf{k}}(E, T) = \Sigma^{\text{FM}}_{n\mathbf{k}}(E, T) +
\Sigma^{\text{DW}}_{n\mathbf{k}}(E, T).$

In practice, we often use the on-the-mass-shell approximation, where the
self-energy is evaluated at the Kohn-Sham (KS) eigenvalue,
$E
= \varepsilon_{n\mathbf{k}}$. Let us highlight the FM
contribution, which involves the electron-phonon matrix elements
$g_{mn\mathbf{k}, \nu \mathbf{q}}$:

$\Sigma^{\text{FM}}_{n\mathbf{k}}(T) = \frac{1}{N_q}
\sum_{m\nu\mathbf{q}} |g_{mn\mathbf{k}, \nu \mathbf{q}}|^2 \left\[
\frac{n_{\nu\mathbf{q}}(T) + 1 -
f_{m\mathbf{k}+\mathbf{q}}(T)}{\varepsilon_{n\mathbf{k}} -
\varepsilon_{m\mathbf{k}+\mathbf{q}} - \omega_{\nu\mathbf{q}} +
i\delta} + \frac{n_{\nu\mathbf{q}}(T) +
f_{m\mathbf{k}+\mathbf{q}}(T)}{\varepsilon_{n\mathbf{k}} -
\varepsilon_{m\mathbf{k}+\mathbf{q}} + \omega_{\nu\mathbf{q}} +
i\delta} \right\],$

where $n_{\nu\mathbf{q}}(T)$ is the Bose-Einstein occupation of phonon mode
$(\nu, \mathbf{q})$ with index
$\nu$ and phonon wavevector $\mathbf{q}$,
$\omega_{\nu\mathbf{q}}$ is the phonon frequency,
$N_q$ is the number of $\mathbf{q}$-points, and $f_{m\mathbf{k}+\mathbf{q}}(T)$ is the Fermi-Dirac occupation of the electronic state
with band $m$ and
wavevector $\mathbf{k}+\mathbf{q}$. The infinitesimal imaginary shift
$i
\delta$ in the denominator ensures the correct pole
structure of the self-energy. In practice, $\delta$ is
often finite and used as a smearing or convergence parameter.

The DW contribution is a purely real shift and can be calculated using
the phonon frequencies and eigenvectors, as well as the second
derivatives of the KS potential with respect to atomic displacements:

$\Sigma^{\text{DW}}_{n\mathbf{k}}(T) = \frac{1}{N_q}
\sum_{\nu\mathbf{q}} g^{2,\text{DW}}_{n \mathbf{k}, \nu\mathbf{q}}
(2n_{\nu\mathbf{q}}(T) + 1),$

where $g^{2,\text{DW}}_{n
\mathbf{k}, \nu\mathbf{q}}$ represents the second-order
change in the KS potential due to phonon mode
$(\nu, \mathbf{q})$. To evaluate this term in practice,
we employ the rigid-ion approximation, which simplifies the calculation
by assuming that the potential changes rigidly with atomic
displacements<sup>[\[1\]](#cite_note-giustino:rmp:2017-1)</sup>.
This approximation is implemented in VASP. It means that we do not need
to compute the second derivatives of the KS potential explicitly, but
can instead use the first derivatives (i.e., the electron-phonon matrix
elements) to estimate the DW term.

The combination of $\Sigma^{\text{FM}}_{n\mathbf{k}}(T) +
\Sigma^{\text{DW}}_{n\mathbf{k}}(T)$ at this level of
approximation is often called the Allen-Heine-Cardona (AHC)
theory<sup>[\[2\]](#cite_note-allen:jpcss:1976-2)[\[3\]](#cite_note-allen:prb:1981-3)</sup>.
To be precise, the expressions we showed here are have come to be know
as nonadiabatic AHC theory, owing to the fact that the phonon frequency
$\omega_{\nu \mathbf{q}}$ appears in the denominator of
the FM self-energy. Physically, this means that energy can be exchanged
between the electrons and phonons. In contrast, there is also an
adiabatic formula where the phonon frequency is neglected in the
denominator, which assumes that the electrons respond instantaneously to
the slower lattice vibrations:

$\Sigma^{\text{FM, ad}}_{n\mathbf{k}}(T) = \frac{1}{N_q}
\sum_{m\nu\mathbf{q}} |g_{mn\mathbf{k}, \nu \mathbf{q}}|^2 \frac{2
n_{\nu\mathbf{q}}(T) + 1}{\varepsilon_{n\mathbf{k}} -
\varepsilon_{m\mathbf{k}+\mathbf{q}} + i\delta}.$

The adiabatic approximation is sometimes used for calculating
band-structure renormalizations in semiconductors and insulators, where
the phonon frequencies are typically much smaller than the electronic
energy differences. However, the adiabatic approximation breaks down in
polar materials due to the long-range Fröhlich interaction, which can
lead to divergences in the self-energy.

To compute both the FM and DW contributions, we need the electron-phonon
matrix elements. In the context of KS DFT, the matrix elements can be
defined using the KS orbitals, $\psi_{n\mathbf{k}}$, and the perturbation of the KS potential,
$V_{\text{KS}}$, due to phonon displacements:

$g_{mn\mathbf{k}, \nu \mathbf{q}} = \left\langle
\psi_{m\mathbf{k}+\mathbf{q}} \left| \partial_{\nu \mathbf{q}}
V_{\text{KS}} \right| \psi_{n\mathbf{k}} \right\rangle,$

We usually call the object $\partial_{\nu \mathbf{q}}
V_{\text{KS}}$ the electron-phonon potential. The
phonon displacement operator $\partial_{\nu \mathbf{q}}$ can be expressed as a superposition of atomic
displacements:

$\partial_{\nu \mathbf{q}} = \sum_{l\kappa\alpha} \sqrt{\frac{\hbar}{2
m_\kappa \omega_{\nu\mathbf{q}}}} e_{\kappa\alpha,\nu \mathbf{q}}
\mathrm{e}^{\mathrm{i} \mathbf{q}\cdot\mathbf{R}_l}
\frac{\partial}{\partial u_{l\kappa\alpha}},$

where $\kappa$ and
$\alpha$ index the atoms in the unit cell and Cartesian
directions, respectively, $m_\kappa$ is
the mass of atom $\kappa$,
$e_{\kappa\alpha,\nu \mathbf{q}}$ is the phonon
eigenvector component, and $u_{l\kappa\alpha}$ is the displacement of atom
$\kappa$ in cell $\mathbf{R}_l$.

There is a set of instructions on how to [compute the electron-phonon
potential](../tutorials/Electron-phonon_potential_from_supercells.md).

#### Band-structure renormalization\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Band-structure renormalization">edit</a> \| (./index.php.md)\]

As mentioned above, the electron-phonon interactions lead to a
renormalization of the electronic band structure. The renormalized
electronic energies, $E_{n\mathbf{k}}(T)$, can be obtained by adding the real part of the
self-energy to the KS eigenvalues:

$E_{n\mathbf{k}}(T) = \varepsilon_{n\mathbf{k}} +
\text{Re}\[\Sigma_{n\mathbf{k}}(T)\],$

where $\varepsilon_{n\mathbf{k}}$ are the Kohn-Sham eigenvalues.

Of particular interest is the renormalization of the bandgap in
semiconductors and insulators, which refers to the change in the energy
difference between the conduction band minimum (CBM) and the valence
band maximum (VBM) due to these electron-phonon interactions. In this
case, we evaluate $\Sigma_{n\mathbf{k}}(T)$ at the KS eigenvalues that correspond to the CBM and
VBM to get the bandgap renormalization. The renormalization varies with
temperature as phonon populations change. However, it also occurs at 0 K
due to zero-point atomic motion where it is referred to as zero-point
renormalization (ZPR).

For the computation of the band-structure renormalization, it is
important to include both the FM and DW contributions to the
self-energy. Neglecting the DW term can lead to significant errors in
the predicted bandgap renormalization, as the DW term often partially
cancels the FM
contribution<sup>[\[1\]](#cite_note-giustino:rmp:2017-1)</sup>.

For information on how to compute the band-structure renormalization
using VASP, please refer to [this how-to
page](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
of the manual.

#### Transport coefficients\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Transport coefficients">edit</a> \| (./index.php.md)\]

The [transport
coefficients](Electronic_transport_coefficients.md)
describe how efficiently charge, heat, or another quantity is carried
through the material. The electronic transport coefficients are derived
via the linearized Boltzmann equation within the relaxation time
approximation (RTA)
<sup>[\[1\]](#cite_note-giustino:rmp:2017-1)</sup>:

$\frac{\partial f^0_{n \mathbf{k}}}{\partial \varepsilon_{n
\mathbf{k}}} \mathbf{v}_{n \mathbf{k}} \cdot (-e)\textbf{E} = -
\sum_\nu \int \frac{d \mathbf{q}}{\Omega_{BZ}} \Gamma_{mn
\nu}(\mathbf{k}, \mathbf{q}) \times \[(f_{n \mathbf{k}} - f^0_{n
\mathbf{k}}) - (f_{n \mathbf{k} + \mathbf{q}} - f^0_{n \mathbf{k} +
\mathbf{q}})\]$,

where $f^0_{n \mathbf{k} +
\mathbf{q}}$ is the electron occupation at band
$n$ at k-point $\mathbf{k}$
and q-point $\mathbf{k}$,
$\varepsilon_{n \mathbf{k}}$ is the electron band
energy, $\textbf{v}_{n \mathbf{k}}$ is the carrier velocity, $\textbf{E}$
is the electric field, $\Omega_{BZ}$
is the cell volume, and $\Gamma_{mn \nu}(\mathbf{k},
\mathbf{q})$ is a kernel describing the interaction
between the electrons and phonons.

We employ the frozen-band approximation, which assumes that the
electronic potential and eigenvalues computed for the undoped system
remain unchanged when electrons are added or removed.

The current $J$ can then
be iteratively solved and the Onsager coefficients derived. From the
Onsager coefficients, the electrical conductivity
$\sigma$, the Seebeck coefficient
$S$, Peltier coefficient $\Pi$, and
electronic thermal conductivity $\kappa_e$ can
be calculated. The electronic transport coefficients are described in
more detail in [this theory
page](Electronic_transport_coefficients.md).

Details about calculating the electronic transport coefficients can be
found in [this
how-to](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

## Electron-phonon interactions from statistical sampling\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Electron-phonon interactions from statistical sampling">edit</a> \| (./index.php.md)\]

In contrast to the perturbative approach outlined above, this section
shows how to describe electron-phonon interactions from a statistical
point of view. To begin with, the probability distribution of finding an
atom within the coordinates $\kappa+d\kappa$ (where $\kappa$
denotes the Cartesian coordinates as well as the atom number) at
temperature $T$ in the
harmonic approximation is given by the following
expression<sup>[\[4\]](#cite_note-bloch:zfp:1932-4)[\[5\]](#cite_note-landau:ctp:1959-5)</sup>

$dW_{\nu}(\kappa,T)=\frac{1}{2\pi \langle u^{2}_{\nu \kappa}\rangle}
e^{-\kappa^{2}/(2 \langle u^{2}_{\nu \kappa}\rangle)} d\kappa,$

where the mean-square displacement of the harmonic oscillator is given
as

$\langle u^{2}_{\nu \kappa}\rangle = \frac{\hbar}{2 M_{\kappa}
\omega_{\nu}} \coth{\frac{\hbar \omega_{\nu}}{2 k_{B}T}}.$

Here $M_{\kappa}$,
$\nu$ and $\omega_{\nu}$ denote the mass, phonon eigenmode and phonon
eigenfrequency, respectively. The equation for
$dW$ is valid at any temperature and the high
(Maxwell-Boltzmann distribution) and low temperature limits are easily
regained. In order to obtain an observable $O(T)$ at a
given temperature $T$, the
average of the observable sampled at different coordinate sets
$x_{T}^{\textrm{MC},i}$ with sample size
$n$ is taken

$\langle O(T)\rangle = \frac{1}{n} \sum\limits_{i=1}^{n}
O(x_{T}^{\textrm{MC,i}}).$

### Full Monte Carlo sampling\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Full Monte Carlo sampling">edit</a> \| (./index.php.md)\]

Each set $i$ is
obtained from the equilibrium atomic positions
$x_{\textrm{eq}}$ as

$x_{T}^{\textrm{MC,i}} = x_{\textrm{eq}} + \Delta \tau^{\textrm{MC,i}}$

with the displacement

$\Delta \tau^{\textrm{MC,i}} = \sqrt{\frac{1}{M_{\kappa}}}
\sum\limits_{\nu}^{3(N-1)} \varepsilon_{\kappa,\nu} \mathcal{N}.$

Here $\varepsilon_{\kappa,\nu}$ denotes the unit vector of eigenmode
$\nu$ on atom $\kappa$. The
magnitude of the displacement in each Cartesian direction is obtained
from the normal-distributed random variable $\mathcal{N}$
with a probability distribution according to $dW$.

### ZG configuration (one-shot method)\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: ZG configuration (one-shot method)">edit</a> \| (./index.php.md)")\]

Motivated by the empirical observation that for increasing super-cell
sizes the number of required structures in the MC method can be
decreased, M. Zacharias and F.
Giustino<sup>[\[6\]](#cite_note-zacharias:prb:2016-6)</sup>
proposed a one-shot method where only a single set of displacements is
used

$\Delta \tau^{\textrm{OS}} = \sqrt{\frac{1}{M_{\kappa}}}
\sum\limits_{\nu}^{3(N-1)} (-1)^{\nu-1} \varepsilon_{\kappa,\nu}
\sigma_{\nu,T},$

where the summation over the eigenmodes runs in an ascending order with
respect to the values of the eigenfrequencies, and the magnitude of each
displacement is given by

$\sigma_{\nu,T} = \sqrt{(2 n_{\nu,T}+1) \frac{\hbar}{2 \omega_{\nu}}}.$

Here $n_{\nu,T}=\[\mathrm{exp}(\hbar \omega_{\nu} /k_{B}T)-1\]^{-1}$ denotes the Bose-Einstein occupation number. In this
way, the sum for the observable $\langle O(T)\rangle$ is reduced to a single calculation. In Ref.
<sup>[\[6\]](#cite_note-zacharias:prb:2016-6)</sup>
it was shown that for super-cell sizes $N\rightarrow \infty$ the structural configuration obtained using the ZG
configuration should lead to equivalent results as fully converged MC
calculations. In practice, it was shown that already relatively small
supercell sizes are sufficient to achieve good accuracy, but the
convergence with respect to the cell size can vary between different
materials. In Ref.
<sup>[\[7\]](#cite_note-karsai:njp:2018-7)</sup>
we have also used a slightly modified approach, in which the signs of
the displacements are chosen randomly instead of
$\pm 1$. This was only necessary when calculating
volume-dependent ZPR, since the modes sometimes change the order as the
volume changes. Using alternating signs for the displacement then causes
small discontinuities in the ZPR volume curve of the order of 5 meV for
carbon diamond. By averaging over many random phases, this problem can
be eliminated. Nevertheless 5 meV difference between the ZG
configuration and full MC is considered as accurate enough in most
calculations.

For information on how to compute the band-structure renormalization
using VASP, please refer to [this how-to
page](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md)
of the manual.

## References\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_theory&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-giustino:rmp:2017_1-0)</sup>
    <sup>[b](#cite_ref-giustino:rmp:2017_1-1)</sup>
    <sup>[c](#cite_ref-giustino:rmp:2017_1-2)</sup>
    <sup>[d](#cite_ref-giustino:rmp:2017_1-3)</sup>
    <a href="https://doi.org/10.1103/RevModPhys.89.015003"
    class="external text" rel="nofollow">F. Giustino, <em>Electron-phonon
    interactions from first principles</em>, Rev. Mod. Phys.
    <strong>89</strong>, 015003 (2017).</a>
2.  [↑](#cite_ref-allen:jpcss:1976_2-0)
    <a href="https://doi.org/10.1088/0022-3719/9/12/013"
    class="external text" rel="nofollow">P. B. Allen and V. Heine,
    <em>Theory of the temperature dependence of electronic band
    structures</em>, J. Phys. C: Solid State Phys. <strong>9</strong>, 2305
    (1976).</a>
3.  [↑](#cite_ref-allen:prb:1981_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.23.1495" class="external text"
    rel="nofollow">P. B. Allen and M. Cardona, <em>Theory of the temperature
    dependence of the direct gap of germanium</em>, Phys. Rev. B
    <strong>23</strong>, 1495 (1981).</a>
4.  [↑](#cite_ref-bloch:zfp:1932_4-0)
    <a href="https://doi.org/10.1007/BF01337791" class="external text"
    rel="nofollow">F. Bloch, Zeitschrift fuer Physik. <strong>74</strong>,
    295 (1932).</a>
5.  [↑](#cite_ref-landau:ctp:1959_5-0)
    <a href="https://doi.org/10.1016/C2009-0-24487-4" class="external text"
    rel="nofollow">L. D. Landau and E. M. Lifshitz, Course of Theoretical
    Physics: Statistical Physics vol 5, (London: Pergamon), (1959).</a>
6.  ↑
    <sup>[a](#cite_ref-zacharias:prb:2016_6-0)</sup>
    <sup>[b](#cite_ref-zacharias:prb:2016_6-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.94.075125"
    class="external text" rel="nofollow">M. Zacharias and F. Giustino, Phys.
    Rev. B <strong>94</strong>, 075125 (2016).</a>
7.  [↑](#cite_ref-karsai:njp:2018_7-0)
    <a href="https://doi.org/10.1088/1367-2630/aaf53f" class="external text"
    rel="nofollow">F. Karsai, M. Engel, E. Flage-Larssen, and G. Kresse, New
    J. of Phys. <strong>20</strong>, 123008 (2018).</a>


------------------------------------------------------------------------



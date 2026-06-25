<!-- Source: https://vasp.at/wiki/index.php/Projector-augmented-wave_formalism | revid: 32084 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Projector-augmented-wave formalism



## Contents


- [1 Basics of the
  PAW formalism](#Basics_of_the_PAW_formalism)
- [2 Charge and
  overlap densities](#Charge_and_overlap_densities)
- [3 The
  compensation or augmentation
  density](#The_compensation_or_augmentation_density)
- [4
  References](#References)


## Basics of the PAW formalism\[<a
href="/wiki/index.php?title=Projector-augmented-wave_formalism&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Basics of the PAW formalism">edit</a> \| (./index.php.md)\]

The PAW formalism is a generalization of ideas of both
Vanderbilt-type<sup>[\[1\]](#cite_note-vander:90-1)</sup>
ultrasoft-pseudopotentials<sup>[\[2\]](#cite_note-kresshaf:94-2)</sup>
(USPP) and the linearized
augmented-plane-wave<sup>[\[3\]](#cite_note-andersen:75-3)</sup>
(LAPW) method. The method was first proposed and implemented by
Blöchl<sup>[\[4\]](#cite_note-bloechl:94-4)</sup>.
The formal relationship between Vanderbilt-type ultrasoft
pseudopotentials and the PAW method has been derived by Kresse and
Joubert<sup>[\[5\]](#cite_note-kressjoub:99-5)</sup>,
and the generalization of the PAW method to noncollinear magnetism has
been discussed by Hobbs, Kresse and
Hafner<sup>[\[6\]](#cite_note-hobbs:00-6)</sup>.
We briefly summarize the basics of the PAW method below (following Refs.
<sup>[\[4\]](#cite_note-bloechl:94-4)</sup>
and
<sup>[\[5\]](#cite_note-kressjoub:99-5)</sup>).

In the PAW method the one electron wavefunctions
$\psi_{n\mathbf{k}}$, in the following simply called
orbitals, are derived from the pseudo orbitals
$\widetilde{\psi}_{n\mathbf{k}}$ by means of a linear
transformation:

$|\psi_{n\mathbf{k}} \rangle = |\widetilde{\psi}_{n\mathbf{k}}
\rangle + \sum_{i}(|\phi_{i} \rangle - |\widetilde{\phi}_{i}
\rangle) \langle \widetilde{p}_{i} |\widetilde{\psi}_{n\mathbf{k}}
\rangle.$

The pseudo orbitals $\widetilde{\psi}_{n\mathbf{k}}$, where
$nk$ is the band index and k-point index, are the
variational quantities and expanded in plane waves (see below). In the
interstitial region between the PAW spheres, the orbitals
$\widetilde{\psi}_{n\mathbf{k}}$ are identical to the
exact orbitals ${\psi}_{n\mathbf{k}}$. Inside the spheres, the pseudo-orbitals are however
only a computational tool and an inaccurate approximation to the true
orbitals, since even the norm of the all-electron wave function is not
reproduced. The last equation is required to map the auxiliary
quantities $\widetilde{\psi}_{n\mathbf{k}}$ onto the corresponding
exact orbitals. The PAW method implemented in VASP exploits the frozen
core (FC) approximation, which is not an inherent characteristic of the
PAW method, but has been made in all implementations so far. In the
present case, the core electrons are also kept frozen in the
configuration for which the PAW dataset was generated.

The index $\alpha$ is a
shorthand for the atomic site $\mathbf{R}_\alpha$, the angular momentum quantum numbers
$l_\alpha,m_\alpha$ and an additional index
$\varepsilon_\alpha$ referring to the reference energy.
The pseudo orbitals are expanded in the reciprocal space using plane
waves

$\langle \mathbf{r} | \widetilde{\psi}_{n\mathbf{k}} \rangle =
\frac{1}{\Omega^{1/2}} \sum_{\mathbf{G}} C_{n\mathbf{kG}}
e^{i(\mathbf{G}+\mathbf{k})\cdot \mathbf{r}} = e^{i\mathbf{k}\cdot
\mathbf{r}}\tilde u_{n\mathbf k}(\mathbf r),$

where $\Omega$ is
the volume of the Wigner-Seitz cell and $\tilde u_{n\mathbf k}(\mathbf
r)$ is the cell periodic part of the pseudo orbital.
The all-electron (AE) partial waves $\phi_{\alpha}$ are solutions of the radial Schrödinger equation for a
non-spinpolarized reference atom at a specific energy
$\varepsilon_\alpha$ and for a specific angular
momentum $l_\alpha$:

$\langle \mathbf{r}|\phi_{\alpha}\rangle =
\frac{1}{|\mathbf{r}-\mathbf{R}_\alpha|}
u_{\alpha}(|\mathbf{r}-\mathbf{R}_\alpha|)Y_{\alpha}(\widehat{\mathbf{r}-\mathbf{R}_\alpha})
= \frac{1}{|\mathbf{r}-\mathbf{R}_\alpha|}
u_{l_\alpha\varepsilon_\alpha}(|\mathbf{r}-\mathbf{R}_\alpha|)\\
Y_{l_\alpha m_\alpha}(\widehat{\mathbf{r}-\mathbf{R}_\alpha}).$

The notation $\widehat{\mathbf{r}-\mathbf{R}_\alpha}$ is used to
clarify that the spherical harmonics $Y$ depends on
the orientation but not on the length of the vector
$\mathbf{r}-\mathbf{R}_\alpha$. Note that the radial
component of the partial wave $u_{\alpha}$
is independent of $m_\alpha$,
since the partial waves are calculated for a spherical atom. Also, do
not confuse the radial functions, $u_{\alpha}(|\mathbf r|)$, with the functions of the cell-periodic part,
$\tilde u_{n\mathbf k}(\mathbf r)$. Furthermore, the
spherical harmonics depend on the angular quantum numbers only and not
on the reference energy. The pseudo partial waves
$\widetilde{\phi}_{\alpha}$ are equivalent to the AE
partial waves outside a core radius $r_{c}$ and
match continuously onto $\phi_{\alpha}$ inside the core radius:

$\langle \mathbf{r}|\widetilde{\phi}_{\alpha}\rangle =
\frac{1}{|\mathbf{r}-\mathbf{R}_\alpha|}
\widetilde{u}_{\alpha}(|\mathbf{r}-\mathbf{R}_\alpha|)
Y_{\alpha}(\widehat{\mathbf{r}-\mathbf{R}_\alpha}) =
\frac{1}{|\mathbf{r}-\mathbf{R}_\alpha|}
\widetilde{u}_{l_\alpha\varepsilon_\alpha}(|\mathbf{r}-\mathbf{R}_\alpha|)\\
Y_{l_\alpha m_\alpha}(\widehat{\mathbf{r}-\mathbf{R}_\alpha}).$

The core radius $r_{c}$ is
usually chosen approximately around half the nearest neighbor distance.
The projector functions $\widetilde{p}_{\alpha}$ are dual to the partial waves:

$\langle \widetilde{p}_{i} | \widetilde{\phi}_{j} \rangle =
\delta_{ij}.$

## Charge and overlap densities\[<a
href="/wiki/index.php?title=Projector-augmented-wave_formalism&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Charge and overlap densities">edit</a> \| (./index.php.md)\]

Starting from the completeness relations it is possible to show that, in
the PAW method, the total charge density (or more precisely the overlap
density) related to two orbitals $\psi_{n\mathbf{k}}$ and $\psi_{m\mathbf{k}}$

$n(\mathbf{r}) =
\psi^{\ast}_{n\mathbf{k}}(\mathbf{r})\\\psi_{m\mathbf{k}}(\mathbf{r})$

can be rewritten as (for details we refer to Ref.
<sup>[\[4\]](#cite_note-bloechl:94-4)</sup>):

$n(\mathbf{r}) = \widetilde{n} (\mathbf{r}) -
\widetilde{n}^{1}(\mathbf{r})+ n^{1}(\mathbf{r}).$

Here, the constituent charge densities are defined as:

$\widetilde{n}(\mathbf{r}) = \langle \widetilde{\psi}_{n\mathbf{k}}|
\mathbf{r}\rangle\langle \mathbf{r} | \widetilde{\psi}_{m\mathbf{k}}
\rangle$

$\widetilde{n}^{1}(\mathbf{r}) = \sum_{\alpha, \beta}
\widetilde{\phi}^\ast_\alpha(\mathbf{r}) \widetilde{\phi}_\beta
(\mathbf{r})
\langle\widetilde{\psi}_{n\mathbf{k}}|\widetilde{p}_\alpha\rangle
\langle\widetilde{p}_\beta| \widetilde{\psi}_{m\mathbf{k}}\rangle$

$n^{1}(\mathbf{r}) = \sum_{\alpha, \beta} \phi^\ast_\alpha(\mathbf{r})
\phi_\beta (\mathbf{r})
\langle\widetilde{\psi}_{n\mathbf{k}}|\widetilde{p}_\alpha\rangle
\langle\widetilde{p}_\beta| \widetilde{\psi}_{m\mathbf{k}}\rangle.$

The quantities with a superscript 1 are one-center quantities and are
usually only evaluated on radial grids. Furthermore, one can usually
drop the complex conjugation for the partial waves, since they are
real-valued. The indices $\alpha$ and
$\beta$ are restricted to those pairs that correspond to
one atom $\mathbf{R}_\alpha=\mathbf{R}_\beta$. For a complete
set of projectors the one-centre pseudo charge density
$\widetilde{n}^{1}$ is exactly identical to
$\widetilde{n}$ within the augmentation spheres.
Furthermore, it is often necessary to define $\rho_{\alpha\beta}$, the occupancies of each augmentation channel
$(\alpha,\beta)$ inside each PAW sphere. These are
calculated from the pseudo orbitals applying the projector functions and
summing over all bands

$\rho_{\alpha\beta} = \sum_{n\mathbf{k}} f_{n\mathbf{k}} \langle
\widetilde{\psi}_{n\mathbf{k}} | \widetilde{p}_{\alpha} \rangle
\langle \widetilde{p}_{\beta} | \widetilde{\psi}_{n\mathbf{k}}
\rangle,$

where the occupancy $f_{n\mathbf{k}}$ is one for occupied orbitals and zero for unoccupied
one electron orbitals.

## The compensation or augmentation density\[<a
href="/wiki/index.php?title=Projector-augmented-wave_formalism&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: The compensation or augmentation density">edit</a> \| (./index.php.md)\]

The PAW method would yield exact overlap densities on the plane wave
grid if the density were calculated as

$n(\mathbf{r})= \langle \widetilde{\psi}_{n\mathbf{k}}|
\mathbf{r}\rangle\langle \mathbf{r} | \widetilde{\psi}_{m\mathbf{k}}
\rangle + \sum_{\alpha, \beta} ( \phi^\ast_\alpha(\mathbf{r})
\phi_\beta (\mathbf{r}) - \widetilde{\phi}^\ast_\alpha(\mathbf{r})
\widetilde{\phi}_\beta (\mathbf{r}) )
\langle\widetilde{\psi}_{n\mathbf{k}}|\widetilde{p}_\alpha\rangle
\langle\widetilde{p}_\beta| \widetilde{\psi}_{m\mathbf{k}}\rangle$

In practice, the second term changes far too rapidly in real space to be
represented on a plane wave grid. Since even the norm of the
pseudo-orbitals does not agree with the norm of the all-electron
orbitals, it does not suffice to calculate Hartree or exchange energies
from the pseudo densities only.

Hence, in order to treat the long-range electrostatic interactions in
the Hartree and exchange term an additional quantity, the compensation
density $\widehat{n}$,
is introduced. Its purpose is to approximate

$Q_{\alpha,\beta}({\mathbf r}) = \phi^\ast_\alpha(\mathbf{r})
\phi_\beta (\mathbf{r}) - \widetilde{\phi}^\ast_\alpha(\mathbf{r})
\widetilde{\phi}_\beta (\mathbf{r}).$

This compensation density (sometimes also referred to as augmentation
density) is chosen such that the sum of the pseudo charge density and
the compensation density $\widetilde{n}^{1} +
\widehat{n}$ has exactly the same moments as the exact
density $n^{1}$ within
each augmentation sphere centered at the position
$\mathbf{R}_\alpha$. This requires that

$\int_{\Omega_{r}}\[n^{1}(\mathbf{r}) -\widetilde{n}^{1}(\mathbf{r}) -
\widehat{n}(\mathbf{r})\]|\mathbf{r}-\mathbf{R}_\alpha|^{L}
Y_{LM}^{\ast}(\widehat{\mathbf{r}-\mathbf{R}_\alpha})\\d\mathbf{r} = 0
\quad \forall \quad \mathbf{R}_\alpha, L, M.$

This implies that the electrostatic potential originating from
$n^{1}$ is identical to that of
$\widetilde{n}^{1}+\widehat{n}$ outside the augmentation
sphere. Details on the construction of the compensation charge density
in the VASP program have been published
elsewhere<sup>[\[5\]](#cite_note-kressjoub:99-5)</sup>.
The compensation charge density is written in the form of a one-center
multipole expansion

$\widehat{n}(\mathbf{r}) = \sum_{\alpha,\beta,LM}
\widehat{Q}_{\alpha,\beta}^{LM}(\mathbf{r})\\ \langle
\widetilde{\psi}_{n\mathbf{k}} | \widetilde{p}_{\alpha} \rangle
\langle \widetilde{p}_{\beta} | \widetilde{\psi}_{m\mathbf{k}}
\rangle,$

where the functions $\widehat{Q}_{\alpha\beta}^{LM}(\mathbf{r})$ are given
by

$\widehat{Q}_{\alpha \beta}^{LM}(\mathbf{r}) = q_{\alpha
\beta}^{LM}\\g_{L}(|\mathbf{r}-\mathbf{R}_i|)
Y_{LM}(\widehat{\mathbf{r}-\mathbf{R}_\alpha}).$

The moment $L$ of the
function $g_L(r)$ is
equal to 1. The quantity $q_{\alpha\beta}^{LM}$ is defined in Eq. (25) of Ref.
<sup>[\[5\]](#cite_note-kressjoub:99-5)</sup>.

## References\[<a
href="/wiki/index.php?title=Projector-augmented-wave_formalism&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-vander:90_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.41.7892" class="external text"
    rel="nofollow">D. Vanderbilt, Phys. Rev. B 41, 7892 (1990).</a>
2.  [↑](#cite_ref-kresshaf:94_2-0)
    <a
    href="http://iopscience.iop.org/article/10.1088/0953-8984/6/40/015/pdf"
    class="external text" rel="nofollow">G. Kresse, and J. Hafner, J. Phys.:
    Condens. Matter 6, 8245 (1994).</a> 
3.  [↑](#cite_ref-andersen:75_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.12.3060" class="external text"
    rel="nofollow">O.K. Andersen, Phys. Rev. B 12, 3060 (1975).</a>
    
4.  ↑
    <sup>[a](#cite_ref-bloechl:94_4-0)</sup>
    <sup>[b](#cite_ref-bloechl:94_4-1)</sup>
    <sup>[c](#cite_ref-bloechl:94_4-2)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.50.17953"
    class="external text" rel="nofollow">P.E. Blöchl, Phys. Rev. B 50, 17953
    (1994).</a> 
5.  ↑
    <sup>[a](#cite_ref-kressjoub:99_5-0)</sup>
    <sup>[b](#cite_ref-kressjoub:99_5-1)</sup>
    <sup>[c](#cite_ref-kressjoub:99_5-2)</sup>
    <sup>[d](#cite_ref-kressjoub:99_5-3)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.59.1758" class="external text"
    rel="nofollow">G. Kresse, and D. Joubert, Phys. Rev. B 59, 1758
    (1999).</a> 
6.  [↑](#cite_ref-hobbs:00_6-0)
    <a href="https://doi.org/10.1103/PhysRevB.62.11556"
    class="external text" rel="nofollow">D. Hobbs, G. Kresse, and J. Hafner,
    Phys. Rev. B. 62 (2000).</a> 


------------------------------------------------------------------------



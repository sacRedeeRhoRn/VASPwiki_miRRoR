<!-- Source: https://vasp.at/wiki/index.php/Charged_systems_with_density_functional_theory | revid: 34439 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Charged systems with density functional theory


On this page, we describe technical issues with computing the energies
of charged systems with periodic density functional theory (DFT)
calculations. We first introduce the problem of divergence of the
electrostatic energy in DFT calculations and illustrate how this
divergence is removed for charge neutral computations. We then discuss
why this divergence is present for charged systems. Finally, we present
methods which have been implemented in VASP that allow for calculations
of charged bulk, surface and molecular systems.


## Contents


- [1 Treating
  divergence in charge neutral
  calculations](#Treating_divergence_in_charge_neutral_calculations)
- [2 Divergences in
  charged calculations](#Divergences_in_charged_calculations)
- [3 Treating
  charged systems in
  practice](#Treating_charged_systems_in_practice)
- [4 Related tags
  and articles](#Related_tags_and_articles)
- [5
  References](#References)


## Treating divergence in charge neutral calculations\[<a
href="/wiki/index.php?title=Charged_systems_with_density_functional_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Treating divergence in charge neutral calculations">edit</a> \| (./index.php.md)\]

VASP utilizes efficient fast Fourier transforms (FFT) to compute the
electrostatic potential from the charge density using the Poisson
equation,

$V(\mathbf{r}) = 4\pi \int \frac{\rho(\mathbf{r}^\prime)}{\left |
\mathbf{r} - \mathbf{r}^\prime \right|} d\mathbf{r}^\prime,$

where $\mathbf{r}$
and $\mathbf{r}^\prime$ are all points in real space. Fourier transforming the
Poisson equation to reciprocal space,

$V(\mathbf{G}) = \frac{4\pi}{\mathrm{G}^2} \rho(\mathbf{G}),$

where $\mathbf{G}$
is the reciprocal lattice vector and $\mathrm{G}$
is its norm.

An obvious issue with computing $V(\mathbf{G})$ is that it diverges for $\mathrm{G}\to 0$. This divergence is handled in charge neutral DFT
calculations by cancelling out individual divergences for the total
electrostatic
energy,<sup>[\[1\]](#cite_note-ihm:jpcss:1979-1)</sup>
which is the sum of electron-electron, ion-electron and ion-ion energies

$E_{\mathrm{electrostatic}} = E_{\mathrm{electron-electron}} +
E_{\mathrm{ion-electron}} + E_{\mathrm{ion-ion}}.$

Individually, these terms have the following functional forms,

$E_{\mathrm{electron-electron}} = \frac{1}{2} \sum_{\mathrm{G}}
\rho_{\mathrm{electron}}(\mathbf{G})
V_{\mathrm{electron}}(\mathbf{G}),$

where $\rho_{\mathrm{electron}}$ and $V_{\mathrm{electron}}$ are the electronic charge density and potential
respectively.

$E_{\mathrm{ion-electron}} = -\sum_{\mathrm{G}}
\rho_{\mathrm{ion}}(\mathbf{G}) V_{\mathrm{electron}}(\mathbf{G}),$

where $\rho_{\mathrm{ion}}$ is the ion charge density. VASP does not explicitly
compute $E_{\mathrm{ion-electron}}$, but the potential of the ion is reflected through the
eigenvalues. The ion-ion interactions are treated by Ewald summation
$E_{\mathrm{ion-ion}} = E_{\mathrm{long-range}} +
E_{\mathrm{short-range}} + E_{\mathrm{self}} +
E_{\mathrm{homogeneous}},$

where $E_{\mathrm{long-range}}$ is the only component which sums over the
$\mathrm{G}$ vectors and has the form,

$E_{\mathrm{ion-ion}} = \frac{1}{2} \sum_{\mathrm{G}}
\rho_{\mathrm{ion}}(\mathbf{G}) V_{\mathrm{ion}}(\mathbf{G}).$

The summed $\mathrm{G}=0$
terms of $E_{\mathrm{electron-electron}}$,
$E_{\mathrm{ion-electron}}$ and
$E_{\mathrm{ion-ion}}$ are given by,

$E_{\mathrm{electrostatic}}(\mathbf{G}=0) =
\frac{1}{2}\rho_{\mathrm{electron}}(\mathbf{G}=0)
V_{\mathrm{electron}}(\mathbf{G}=0) -
\rho_{\mathrm{ion}}(\mathbf{G}=0)
V_{\mathrm{electron}}(\mathbf{G}=0) +
\frac{1}{2}\rho_{\mathrm{ion}}(\mathbf{G}=0)
V_{\mathrm{ion}}(\mathbf{G}=0),$

which, can be expressed through the reciprocal space Poisson equation
as, $E_{\mathrm{electrostatic}}(\mathbf{G}=0) = \frac{4\pi}{\mathrm{G}^2}
\left \[\frac{1}{2}\rho_{\mathrm{electron}}(\mathbf{G}=0)^2 -
\rho_{\mathrm{ion}}(\mathbf{G}=0)^2 +
\frac{1}{2}\rho_{\mathrm{ion}}(\mathbf{G}=0)^2 \right\].$

Under the condition that $\rho_{\mathrm{electron}}(\mathbf{G}=0)=\rho_{\mathrm{ion}}(\mathbf{G}=0)$, the individual divergences would cancel out and the
total energy is convergent. Since the $\mathrm{G}=0$
term of a Fourier transformed quantity is its average, the above
condition is satisfied when the average electron and ion charge density
are the same, i.e. the system is charge neutral.

## Divergences in charged calculations\[<a
href="/wiki/index.php?title=Charged_systems_with_density_functional_theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Divergences in charged calculations">edit</a> \| (./index.php.md)\]

The total energy does not converge when $\rho_{\mathrm{electron}}(\mathbf{G}=0) \neq
\rho_{\mathrm{ion}}(\mathbf{G}=0)$, i.e., when the
system is not charge neutral. Alternatively, we can think of this
divergence as coming a compensating uniformly smeared out charge
density, $\delta \rho$
with energy $E_{\mathrm{compensating}}$

$E_{\mathrm{compensating}} = \frac{4\pi}{\mathrm{G}^2} \left \[ \delta
\rho^2 \right\]$

which cancels out the divergent terms in $E_{\mathrm{electrostatic}}(\mathbf{G}=0)$.

The consequences of adding a uniform compensating charge is system
specific. For highly screened systems, the potential coming from a
moderate compensating charge presents an acceptable amount of error.
Conversely, systems containing vacuum (such as 2D materials, surfaces
and molecules) have little screening and hence are more susceptible to
artifacts caused by this compensating charge.

## Treating charged systems in practice\[<a
href="/wiki/index.php?title=Charged_systems_with_density_functional_theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Treating charged systems in practice">edit</a> \| (./index.php.md)\]

We
implement<sup>[\[2\]](#cite_note-vijay:prb:2025-2)</sup>
two separate methods to deal with charged systems. These methods are
specific to the dimensionality of the system that is being computed.

Bulk charged systems in orthorhombic cells can be treated by applying
analytical monopole-monolpole corrections (see
[LMONO](../incar-tags/LMONO.md) for further practical details).

Surfaces and other two dimensional materials are treated with Coulomb
kernel truncation methods. These methods replace the Coulomb kernel
$v(\mathbf{G})$, i.e., the $\frac{4\pi}{\mathrm{G}^2}$ in $V(\mathbf{G})$ with a 2D
kernel<sup>[\[3\]](#cite_note-rozzi:prb:2006-3)</sup>
($v_{\text{2D}}(\mathbf{G})$) that removes electrostatic
interactions between non-periodic replicas along the surface
normal,<sup>[\[4\]](#cite_note-sohier:prb:2017-4)</sup>

$v_{\text{2D}}(\mathbf{G}) = \begin{cases} 4\pi / \mathrm{G}^2 \left\[
1 - e^{-\mathrm{G}_{\parallel}R} \left ( \cos(\mathrm{G}_\perp
R_\mathrm{c}) - \mathrm{G}_\perp / \mathrm{G}_{\parallel}
\sin(\mathrm{G}_{\perp}R_\mathrm{c}) \right ) \right\] \quad &
\mathrm{G} \neq 0 \\ 4\pi / \mathrm{G}_\perp^2\left\[ 1 -
\cos(\mathrm{G}_\perp R_\mathrm{c}) - \mathrm{G}_{\perp}R_\mathrm{c}
\sin(\mathrm{G}_\perp R_\mathrm{c}) \right\] \quad &
\mathrm{G}_{\parallel} = 0 \\ -2\pi R_\mathrm{c}^2 \quad &
\mathrm{G}=0 \end{cases}$

where $\mathrm{G}_{\parallel}$ is the norm of the $\mathbf{G}$
vector parallel to the surface and $\mathrm{G}_{\perp}$ is the $\mathbf{G}$
vector along the surface normal. A similar change can be made to the
Coulomb kernel to treat charged molecules (so-called 0D systems with
$v_{\text{0D}}(\mathbf{G}$)) to remove interactions
with periodic replicas in all directions,

$v_{\text{0D}}(\mathbf{G}) = \begin{cases} 4\pi/\mathrm{G}^2 \left( 1 -
\cos\left(\mathrm{G}R_\mathrm{c}\right) \right) & \quad \mathrm{G}\neq
0 \\ 2\pi R_\mathrm{c}^2 & \quad \mathrm{G} = 0 \end{cases}$

See
[KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md)
(available as of VASP.6.5.0) for further details on applying these
Coulomb truncation methods in practice.

## Related tags and articles\[<a
href="/wiki/index.php?title=Charged_systems_with_density_functional_theory&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NELECT](../incar-tags/NELECT.md),
[KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md),
[KERNEL_TRUNCATION/LCOARSEN](../incar-tags/KERNEL_TRUNCATION__LCOARSEN.md),
[KERNEL_TRUNCATION/IDIMENSIONALITY](../incar-tags/KERNEL_TRUNCATION__IDIMENSIONALITY.md),
[KERNEL_TRUNCATION/ISURFACE](../incar-tags/KERNEL_TRUNCATION__ISURFACE.md),
[LMONO](../incar-tags/LMONO.md)

## References\[<a
href="/wiki/index.php?title=Charged_systems_with_density_functional_theory&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-ihm:jpcss:1979_1-0)
    <a href="https://doi.org/10.1088/0022-3719/12/21/009"
    class="external text" rel="nofollow">J. Ihm, A. Zunger, M. L. Cohen,
    Journal of Physics C: Solid State Physics <strong>12</strong>, 4409
    (1979).</a>
2.  [↑](#cite_ref-vijay:prb:2025_2-0)
    <a href="https://doi.org/10.1103/cd6s-cdkf" class="external text"
    rel="nofollow">S. Vijay, M. Schlipf, H. Miranda, F. Karsai, M. Kaltak,
    M. Marsman, and G. Kresse, <em>Efficient periodic density functional
    theory calculations of charged molecules and surfaces using Coulomb
    kernel truncation</em>, Phys. Rev. B <strong>112</strong>, 045409
    (2025).</a>
3.  [↑](#cite_ref-rozzi:prb:2006_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.73.205119"
    class="external text" rel="nofollow">C. A. Rozzi, D. Varsano, A. Marini,
    E. K. Gross, A. J. Rubio, Phys. Rev. B <strong>73</strong>, 20511
    (2006).</a>
4.  [↑](#cite_ref-sohier:prb:2017_4-0)
    <a href="https://doi.org/10.1103/PhysRevB.96.075448"
    class="external text" rel="nofollow">T. Sohier, M. Calandra, and F.
    Mauri, Phys. Rev. B 96, 75448 (2017).</a>



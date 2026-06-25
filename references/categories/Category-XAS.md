<!-- Source: https://vasp.at/wiki/index.php/Category:XAS | revid: 34596 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:XAS


X-ray absorption spectroscopy (XAS) is a powerful method for
investigating the chemical properties of materials. The absorption of
the X-ray photons involves excitations of the core electrons into
conduction bands. The main challenge for an accurate description of such
excitations is the interactions between a positive charge left in place
of the excited core electron, i.e., **core hole**, and the excited
electron, which can form a bound state called **exciton**. There are two
main approaches to *ab initio* modeling of XAS. The first one is based
on DFT and is commonly known as the supercell core-hole (SCH) method.
The second approach is based on the
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>
and requires solving the
<a href="/wiki/Bethe-Salpeter_equations" class="mw-redirect"
title="Bethe-Salpeter equations">Bethe-Salpeter equation (BSE)</a>. In
VASP both approaches rely on the frozen core (FC) approximation, where
the core electrons are kept frozen in the configuration for which the
[PAW](../methods/Projector-augmented-wave_formalism.md)
potential was generated. Although, a shortcoming of the
[PAW](../methods/Projector-augmented-wave_formalism.md)
approach implemented in VASP, this approach nevertheless has been shown
to hold very well for deep core states mostly due to the weak coupling
between the core state and the valence states.


## Contents


- [1 Theoretical
  background](#theoretical-background)
  - [1.1
    Nomenclature](#nomenclature)
  - [1.2 Supercell
    core-hole (SCH)](#supercell-core-hole-sch))
  - [1.3
    Bethe-Salpeter
    equation](#bethe-salpeter-equation)
  - [1.4 Comparing
    BSE and SCH](#comparing-bse-and-sch)
- [2
  Tutorials](#tutorials)
- [3
  References](#references)


## Theoretical background\[<a
href="/wiki/index.php?title=Category:XAS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theoretical background">edit</a> \| (./index.php.md)\]

### Nomenclature\[<a
href="/wiki/index.php?title=Category:XAS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Nomenclature">edit</a> \| (./index.php.md)\]

The X-ray absorption spectra are divided into two regions. The part of
the spectrum starting from the absorption threshold and up to around 50
eV above the edge is called the X-ray absorption near-edge structure
(XANES) or near-edge X-ray absorption fine structure (NEXAFS), which is
the range VASP is designed to reproduce accurately. The part of the
spectrum beyond this range is called the extended X-ray absorption fine
structure (EXAFS), there the spectrum is dominated by the
multiple-scattering effects and can be very challenging to converge with
the number of empty states in VASP.

The edges of the absorption spectra are named by the corresponding core
state, i.e., *K*-edge for the excitations from the state with
$n=1$, *L*-edge for $n=2$, and
*M*-edge for $n=3$. The
spin-orbit interaction causes the splitting of the core states. For
example, the *2p* core states due to the spin-orbit coupling are
splitting into *2p*(*j=1/2*) and *2p*(*j=3/2*) states which show in XAS
as the *L2*- and *L3*-edges, correspondingly.

|  |
|----|
| **Mind:** Currently the spin-orbit coupling is only supported in the valence and conduction states but not in the core states. Hence, the splitting of an absorption edge with the orbital quantum number L\>0 is not captured. For example, the splitting to *L2* and *L3*-edges is not captured in the calculations and instead, a single *L*-edge is shown. |

### Supercell core-hole (SCH)\[<a
href="/wiki/index.php?title=Category:XAS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Supercell core-hole (SCH)">edit</a> \| (./index.php.md)")\]

The SCH
approach<sup>[\[1\]](#cite_note-karsai:prb:2018-1)[\[2\]](#cite_note-unzog:prb:2022-2)</sup>
is explained in detail on the following [theory
page](../theory/Supercell_core-hole_theory.md).
When the core hole is explicitly introduced in one of the atoms, i.e., a
core electron is removed, it is necessary to eliminate the effective
interaction of the core hole with its image across the periodic
boundary. That requires using a large supercell so that this interaction
is negligible.

After the self-consistent electronic minimization is converged in the
presence of the core hole, the dielectric function is calculated using
Fermi's golden rule

$\varepsilon_{\alpha \alpha}^{(2)}(\omega)= \frac{4 \pi^2 e^2
\hbar^2}{\Omega \omega^2 m_e^2} \sum_{\text{core}, c, \mathbf{k}} 2
w_{\mathbf{k}} |\left\langle\psi_{c \mathbf{k}}\right| i
\nabla_\alpha-\mathbf{k}_\alpha\left|\psi_{\text{core}}\right\rangle|^2\delta\left(\varepsilon_{c
\mathbf{k}}-\varepsilon_{\text{core}}-\omega\right)$

In the **initial state** approximation, the electronic minimization in
the presence of the core hole is not carried out, thus the electron-hole
interaction is completely neglected.

- Learn [how to calculate the XAS via a supercell core-hole
  calculation](../tutorials/Supercell_core-hole_calculations.md)

### Bethe-Salpeter equation\[<a
href="/wiki/index.php?title=Category:XAS&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Bethe-Salpeter equation">edit</a> \| (./index.php.md)\]

Within the BSE
approach<sup>[\[2\]](#cite_note-unzog:prb:2022-2)</sup>,
the interaction between the core hole and the excited electron is
explicitly included in the polarizability as explained in the [theory
page](../theory/Bethe-Salpeter_equation.md). The BSE
is solved in the transition space as an eigenvalue problem, whose
eigenvalues $\varepsilon^\lambda$ are the transitions including the excitonic effects
and the eigenvectors $A^\lambda$
are the excitonic states in the transition space. The BSE dielectric
function is found via

$\varepsilon_{\alpha \alpha}^{(2)}(\omega)= \frac{4 \pi^2 e^2
\hbar^2}{\Omega \omega^2 m_e^2}
\sum_\lambda\left|\sum_{\text{core},c, \mathbf{k}} 2A_{\text{core},
c \mathbf{k}}^\lambda \left\langle\psi_{c \mathbf{k}}\right| i
\nabla_\alpha-\mathbf{k}_\alpha\left|\psi_{\text{core}}\right\rangle
\right|^2 \delta\left(\varepsilon^\lambda-\omega\right)$

The BSE calculation based on the [$GW$
calculation](/wiki/Practical_guide_to_GW_calculations "Practical guide to GW calculations")
quasiparticles is considered to be the state of the art for XAS and is
overall more reliable and accurate than the SCH methods.

- Learn [how to calculate the XAS via
  BSE.](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md)

### Comparing BSE and SCH\[<a
href="/wiki/index.php?title=Category:XAS&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Comparing BSE and SCH">edit</a> \| (./index.php.md)\]

The scaling of the BSE+GW approach is $N^4-N^5$ with
the system size, which makes it very expensive computationally for large
cells. The SCH approach on the other hand scales as
$N^3$ with the system size which makes it much cheaper
for complex systems with large cells. Nevertheless, the BSE+GW approach
can be less computationally expensive for small cells and provides a
better insight into the physics of the excitons. Furthermore, some
results indicate that the valence state excitations have to be included
in the XAS calculations as well to reproduce the experimental results,
which is only possible within the BSE formalism
<sup>[\[3\]](#cite_note-tang:pnas:2022-3)</sup>.
SCH has been shown to provide overall an accurate approximation for the
deep core excitations
<sup>[\[1\]](#cite_note-karsai:prb:2018-1)</sup>,
but it can be less accurate for some systems, where the BSE+GW
calculations are required to accurately reproduce the experimental
spectra
<sup>[\[2\]](#cite_note-unzog:prb:2022-2)[\[4\]](#cite_note-liang:prl:2017-4)</sup>.

|  |
|----|
| **Mind:** By default the Lorentzian broadening is applied in the XAS BSE dielectric function. In SCH the default broadening function is Gaussian. |

## Tutorials\[<a
href="/wiki/index.php?title=Category:XAS&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for <a href="https://vasp.at/tutorials/latest/xas/part1"
  class="external text" rel="nofollow">SCH XAS calculations</a>.
- Tutorial for <a href="https://vasp.at/tutorials/latest/xas/part2"
  class="external text" rel="nofollow">BSE XAS calculations</a>.

## References\[<a
href="/wiki/index.php?title=Category:XAS&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-karsai:prb:2018_1-0)</sup>
    <sup>[b](#cite_ref-karsai:prb:2018_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.98.235205"
    class="external text" rel="nofollow">F. Karsai, M. Humer, E.
    Flage-Larsen, P. Blaha, and G. Kresse, Phys. Rev. B <strong>98</strong>,
    235205 (2018).</a>
2.  ↑
    <sup>[a](#cite_ref-unzog:prb:2022_2-0)</sup>
    <sup>[b](#cite_ref-unzog:prb:2022_2-1)</sup>
    <sup>[c](#cite_ref-unzog:prb:2022_2-2)</sup>
    <a href="http://doi.org/10.1103/PhysRevB.106.155133"
    class="external text" rel="nofollow">M. Unzog, A. Tal, G. Kresse,
    <em>X-ray absorption using the projector augmented-wave method and the
    Bethe-Salpeter equation</em>, Phys. Rev. B <strong>106</strong>, 155133
    (2022).</a>
3.  [↑](#cite_ref-tang:pnas:2022_3-0)
    <a href="https://doi.org/10.1073/pnas.2201258119" class="external text"
    rel="nofollow">F. Tang, Z. Li, C. Zhang, and X. Wu, <em>Many-body
    effects in the X-ray absorption spectra of liquid water</em>, Proc.
    Natl. Acad. Sci. USA <strong>119</strong>, 1 (2022).</a>
4.  [↑](#cite_ref-liang:prl:2017_4-0)
    <a href="http://dx.doi.org/10.1103/PhysRevLett.118.096402"
    class="external text" rel="nofollow">Y. Liang, J. Vinson, S. Pemmaraju,
    W. S. Drisdell, E. L. Shirley, and D. Prendergast, <em>Accurate X-Ray
    Spectral Predictions: An Advanced Self-Consistent-Field Approach
    Inspired by Many-Body Perturbation Theory</em>, Phys. Rev. Lett.
    <strong>118</strong>, 096402 (2017)</a>



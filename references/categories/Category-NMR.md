<!-- Source: https://vasp.at/wiki/index.php/Category:NMR | revid: 35930 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:NMR


**Nuclear magnetic resonance** (NMR) spectroscopy is a highly sensitive
technique for probing the atomic-scale structure of molecules, liquids,
and solids. However, directly extracting structural information from NMR
spectra is often challenging. Consequently, *ab-initio* quantum
mechanical simulations, such as those performed using VASP, play a
crucial role in accurately linking NMR spectra to atomic-scale
structural properties.

This page presents an overview of nuclear-electron interactions that can
be computed and are relevant to interpret NMR spectra.


## Contents


- [1 Chemical
  shielding](#chemical-shielding)
  - [1.1
    Nuclear-independent chemical
    shielding](#nuclear-independent-chemical-shielding)
- [2 Magnetic
  susceptibility](#magnetic-susceptibility)
- [3 Quadrupolar
  nuclei - electric field
  gradient](#quadrupolar-nuclei---electric-field-gradient)
- [4 Hyperfine
  coupling](#hyperfine-coupling)
- [5 Additional
  resources](#additional-resources)
  - [5.1
    Lectures](#lectures)
  - [5.2
    Tutorials](#tutorials)
- [6
  References](#references)


## Chemical shielding\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Chemical shielding">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Chemical_shielding.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/5/52/Chemical_shielding.png/200px-Chemical_shielding.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/5/52/Chemical_shielding.png/300px-Chemical_shielding.png 1.5x, /wiki/images/thumb/5/52/Chemical_shielding.png/400px-Chemical_shielding.png 2x"
width="200" height="194" /></a>
<figcaption>The external magnetic field
<strong>B</strong><em><sub>ext</sub></em> (purple) induces currents in
the electrons in atoms. These NMR response currents (black arrows) in
turn induce an opposing magnetic field
<strong>B</strong><em><sub>in</sub></em> (red), reducing the magnetic
field at the position of the nucleus, effectively shielding the nucleus
from <strong>B</strong><em><sub>ext</sub></em>.</figcaption>
</figure>

The effective B-field felt by a nucleus with finite nuclear spin is
related to the applied B field via the chemical shielding tensor. The
applied B-field induces a para- and diamagnetic NMR response current in
the electrons and screens the nucleus with an induced B-field that
follows from the Biot-Savart law, c.f. figure. The chemical shift is the
difference in chemical shielding σ relative to a reference
σ<sub>ref</sub>.

$\delta_{ij} = \sigma_{ij}^{\mathrm{ref}} - \sigma_{ij}.$

VASP can efficiently compute electronic properties in bulk systems
thanks to the
<a href="/wiki/Projector-augmented_wave" class="mw-redirect"
title="Projector-augmented wave">projector-augmented wave</a> (PAW)
method which takes advantage of
<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a> and a [frozen core
approximation](Category-Pseudopotentials.md).
However, the <a href="/wiki/PAW_formalism" class="mw-redirect"
title="PAW formalism">standard PAW transformation</a> does not fully
account for how the gauge field $A$ interacts
with the reconstructed wavefunctions in the augmentation regions (near
atomic cores). Thus, NMR calculations
([`LCHIMAG`](../incar-tags/LCHIMAG.md)` = True`) are based on an extended
version of the
<a href="/wiki/PAW_method" class="mw-redirect" title="PAW method">PAW
method</a>, the gauge-invariant PAW (GIPAW)
method<sup>[\[1\]](#cite_note-pickard:prb:2001-1)[\[2\]](#cite_note-yates:prb:2007-2)</sup>
that properly ensures the gauge invariance. The NMR currents
([WRT_NMRCUR](../incar-tags/WRT_NMRCUR.md)) are computed using linear
response theory.

- Learn [how to calculate the chemical
  shielding](../tutorials/Calculating_the_chemical_shieldings.md).


### Nuclear-independent chemical shielding\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Nuclear-independent chemical shielding">edit</a> \| (./index.php.md)\]

Nuclear-independent chemical shielding (NICS) is a computational method
used to quantify aromaticity in molecules by calculating the magnetic
shielding at a virtual point (not at a nucleus) in space, typically at
the center of a ring or above it
<sup>[\[3\]](#cite_note-schleyer:1996-3)[\[4\]](#cite_note-chen:schleyer:2005-4)</sup>.
See [NUCIND](../incar-tags/NUCIND.md) for more information.

## Magnetic susceptibility\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Magnetic susceptibility">edit</a> \| (./index.php.md)\]

The macroscopic magnetic susceptibility $\chi$ is
defined by
<sup>[\[5\]](#cite_note-mauri:louie:1996-5)</sup>

$\textbf{B}_{\textrm{in}}^{(1)}(\textbf{G}=0) = \frac{8 \pi}{3} \chi
\textbf{B}_{ext},$

where $\textbf{B}_{ext}$ is the external magnetic field and
$\textbf{B}_{\textrm{in}}^{(1)}$ is the induced
magnetic field. This must be taken into account for the chemical
shielding as a G=0 contribution.

It is calculated within linear response theory
([`LCHIMAG`](../incar-tags/LCHIMAG.md)` = True`), where a key variable
*Q<sub>ij</sub>* is approximated in two ways. The so-called *pGv*
approximation is used by default
<sup>[\[2\]](#cite_note-yates:prb:2007-2)</sup>,
where *p* is momentum, *v* is velocity, and *G* is a Green's function.
An alternative approach, the *vGv* approximation is available to
calculate the susceptibility
<sup>[\[6\]](#cite_note-avezac:prb:2007-6)</sup>.
See [LVGVCALC](../incar-tags/LVGVCALC.md) and
[LVGVAPPL](../incar-tags/LVGVAPPL.md) to control the approximation.

- Learn [how to perform a magnetic susceptibility
  calculation.](../tutorials/Calculating_the_magnetic_susceptibility.md)


## Quadrupolar nuclei - electric field gradient\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Quadrupolar nuclei - electric field gradient">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Quadrupolar_efg.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/73/Quadrupolar_efg.png/250px-Quadrupolar_efg.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/73/Quadrupolar_efg.png/375px-Quadrupolar_efg.png 1.5x, /wiki/images/thumb/7/73/Quadrupolar_efg.png/500px-Quadrupolar_efg.png 2x"
width="250" height="162" /></a>
<figcaption>The quadrupolar electric field of a nitrogen nucleus
coupling to electric field gradient <em>V</em> in MAPbI3 (methyl
ammonium lead (III) iodide)</figcaption>
</figure>

Nuclei with **I** \> ± ½ have a non-zero electric field gradient (EFG)
and an electronic quadrupolar moment. The electric quadrupolar moment
couples with the EFG and so the chemical environment of the nucleus may
be probed using nuclear quadrupole resonance (NQR)
<sup>[\[7\]](#cite_note-nqr:web-7)</sup>
(sometimes called zero-field NMR spectroscopy). The EFG is the second
derivative of the potential $V$:

$V_{ij} = \frac{\partial^2 V}{\partial x_i \partial x_j}$,

which is a sum of three parts along the Cartesian *i*,*j* axes:

$V_{i,j} = \tilde{V}_{i,j} -\tilde{V}_{i,j}^1 + V_{i,j}^1$

where $\tilde{V}_{i,j}$ is the plane-wave part of the AE potential,
$\tilde{V}_{i,j}^1$ is the one-center expansion of the
pseudopotential method, and $V_{i,j}^1$
is the one-center expansion of the AE potential.

In VASP, the EFG is calculated using the [LEFG](../incar-tags/LEFG.md) tag.
The commonly reported nuclear quadrupolar coupling constant
*C<sub>q</sub>* is then printed using isotope-specific quadrupole moment
defined using [QUAD_EFG](../incar-tags/QUAD_EFG.md)
<sup>[\[8\]](#cite_note-petrilli:prb:1998-8)</sup>.

- Learn [how to perform an electric field gradient
  calculation](../tutorials/Calculating_the_electric_field_gradient.md).


## Hyperfine coupling\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Hyperfine coupling">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Hyperfine_coupling.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/7b/Hyperfine_coupling.png/250px-Hyperfine_coupling.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/7b/Hyperfine_coupling.png/375px-Hyperfine_coupling.png 1.5x, /wiki/images/thumb/7/7b/Hyperfine_coupling.png/500px-Hyperfine_coupling.png 2x"
width="250" height="143" /></a>
<figcaption>Hyperfine coupling between the nuclear spin and the
electronic spin of the unpaired electron at a nitrogen-vacancy (NV)
center in diamond.</figcaption>
</figure>

The hyperfine tensor $A^I$
describes the interaction between a nuclear spin
$S^I$ and the electronic spin distribution
$S^e$. In most cases associated with a paramagnetic
defect state measureable by electron paramagnetic resonance (EPR)
<sup>[\[9\]](#cite_note-weil:bolton:2007-9)</sup>:

$E=\sum_{ij} S^e_i A^I_{ij} S^I_j.$

The hyperfine tensor is split into two terms, isotropic (or Fermi
contact) $A^I_{iso}$
and anisotropic (or dipolar contributions) $A^I_{ani}$:

$A^I_{i,j} = (A^I_{iso})_{i,j} + (A^I_{ani})_{i,j}.$

$A^I_{iso}$ is calculated based on the
spin-density<sup>[\[10\]](#cite_note-szasz:prb:2013-10)</sup>
and $A^I_{ani}$
is calculated based on the dipolar-dipolar contribution terms
$W_{i,j}(\textbf{R})$. The hyperfine tensor calculation
itself is defined using
[`LHYPERFINE`](../incar-tags/LHYPERFINE.md)` = True`. Both the Fermi
contact and dipolar contribution terms are related to the nuclear
gyromagnetic moment γ, which are controlled by setting
[NGYROMAG](../incar-tags/NGYROMAG.md).

- Learn <a href="/wiki/Calculating_the_hyperfine_coupling_constant"
  class="mw-redirect"
  title="Calculating the hyperfine coupling constant">how to perform a
  hyperfine coupling calculation.</a>


## Additional resources\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Lectures\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on
  <a href="https://youtu.be/CyALJ8Qb1yk" class="external text"
  rel="nofollow">PAW, GIPAW, and NMR theory</a>.
- Lecture on
  <a href="https://youtu.be/Jw8oFzh9Z3k" class="external text"
  rel="nofollow">NMR theory and calculations</a>.

### Tutorials\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for <a href="https://www.vasp.at/tutorials/latest/nmr/part1"
  class="external text" rel="nofollow">chemical shielding calculations</a>.
- Tutorial for <a href="https://www.vasp.at/tutorials/latest/nmr/part2"
  class="external text" rel="nofollow">coupling constants and two-center
  correction calculations</a>.
- Tutorial for <a href="https://www.vasp.at/tutorials/latest/nmr/part3"
  class="external text" rel="nofollow">NICS and current calculations</a>.

## References\[<a
href="/wiki/index.php?title=Category:NMR&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-pickard:prb:2001_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.63.245101"
    class="external text" rel="nofollow">C. J. Pickard and F. Mauri,
    <em>All-electron magnetic response with pseudopotentials: NMR chemical
    shifts</em>, Phys. Rev. B <strong>63</strong>, 245101 (2001).</a>
2.  ↑
    <sup>[a](#cite_ref-yates:prb:2007_2-0)</sup>
    <sup>[b](#cite_ref-yates:prb:2007_2-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.76.024401"
    class="external text" rel="nofollow">J. R. Yates, C. J. Pickard, and F.
    Mauri, <em>Calculation of NMR chemical shifts for extended systems using
    ultrasoft pseudopotentials</em>, Phys. Rev. B <strong>76</strong>,
    024401 (2007).</a>
3.  [↑](#cite_ref-schleyer:1996_3-0)
    <a href="https://doi.org/10.1021/ja960582d" class="external text"
    rel="nofollow">P. von Ragué Schleyer, C. Maerker, A. Dransfeld, H. Jiao,
    and N. J. R. van Eikema Hommes, <em>Nucleus-Independent Chemical
    Shifts:  A Simple and Efficient Aromaticity Probe</em>, J. Am. Chem.
    Soc. <strong>118</strong>, 6317 (1996).</a>
4.  [↑](#cite_ref-chen:schleyer:2005_4-0)
    <a href="https://doi.org/10.1021/cr030088+" class="external text"
    rel="nofollow">Z. Chen, C. S. Wannere, C. Corminboeuf, R. Puchta, and P.
    von Ragué Schleyer, <em>Nucleus-Independent Chemical Shifts (NICS) as an
    Aromaticity Criterion</em>, Chem. Rev. 10, <strong>105</strong>,
    3842–3888 (2005).</a>
5.  [↑](#cite_ref-mauri:louie:1996_5-0)
    <a href="https://doi.org/10.1103/PhysRevLett.76.4246"
    class="external text" rel="nofollow">F. Mauri and S. G. Louie,
    <em>Magnetic Susceptibility of Insulators from First Principles</em>,
    Phys. Rev. Lett. <strong>76</strong>, 4246 (1996).</a>
6.  [↑](#cite_ref-avezac:prb:2007_6-0)
    <a href="https://doi.org/10.1103/PhysRevB.76.165122"
    class="external text" rel="nofollow">M. d'Avezac, N. Marzari, and F.
    Mauri, <em>Spin and orbital magnetic response in metals: Susceptibility
    and NMR shifts</em>, Phys. Rev. B <strong>76</strong>, 165122
    (2007).</a>
7.  [↑](#cite_ref-nqr:web_7-0)
    <a href="https://en.wikipedia.org/wiki/Nuclear_quadrupole_resonance"
    class="external text" rel="nofollow">Nuclear quadrupole resonance,
    www.wikipedia.org (2025)</a>
8.  [↑](#cite_ref-petrilli:prb:1998_8-0)
    <a href="https://doi.org/10.1103/PhysRevB.57.14690"
    class="external text" rel="nofollow">H. M. Petrilli, P. E. Blöchl, P.
    Blaha, and K. Schwarz, <em>Electric-field-gradient calculations using
    the projector augmented wave method</em>, Phys. Rev. B
    <strong>57</strong>, 14690 (1998).</a>
9.  [↑](#cite_ref-weil:bolton:2007_9-0)
    <a href="https://doi.org/10.1002/0470084987" class="external text"
    rel="nofollow">J. Weil and J. Bolton, <em>Electron Paramagnetic
    Resonance: Elementary Theory and Practical Applications</em>,
    (2007).</a>
10. [↑](#cite_ref-szasz:prb:2013_10-0)
    <a href="https://doi.org/10.1103/PhysRevB.88.075202"
    class="external text" rel="nofollow">K. Szasz, T. Hornos, M. Marsman,
    and A. Gali, <em>Hyperfine coupling of point defects in semiconductors
    by hybrid density functional calculations: The role of core spin
    polarization</em>, Phys. Rev. B, <strong>88</strong>, 075202 (2013).</a>



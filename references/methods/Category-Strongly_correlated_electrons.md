<!-- Source: https://vasp.at/wiki/index.php/Category:Strongly_correlated_electrons | revid: 37173 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Strongly correlated electrons


<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Ni_d_s_bands.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/48/Ni_d_s_bands.png/200px-Ni_d_s_bands.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/48/Ni_d_s_bands.png/300px-Ni_d_s_bands.png 1.5x, /wiki/images/thumb/4/48/Ni_d_s_bands.png/400px-Ni_d_s_bands.png 2x"
width="200" height="184" /></a>
<figcaption>Band structure of a typical strongly correlated system -
Ni</figcaption>
</figure>

**Strongly correlated materials** are systems in which electron-electron
interactions play a dominant role and cannot be adequately described by
independent-particle approximations such as standard DFT
<sup>[\[1\]](#cite_note-martin:book:2016-1)</sup>.
These systems typically include elements with partially filled
$d$ and $f$ electron
orbitals which are localized. Correlation effects lead to phenomena such
as metal-insulator transitions, magnetism, and unconventional
superconductivity. To model such systems, several extensions of DFT have
been developed. Below, you find methods relevant in the context of
strongly correlated electrons. Many rely on estimating the on-site
Coulomb interaction U.


## Contents


- [1 Estimating the
  on-site Coulomb interaction
  U](#Estimating_the_on-site_Coulomb_interaction_U)
- [2
  DFT+U](#DFT+U)
- [3 Dynamical
  mean-field theory (DMFT)](#Dynamical_mean-field_theory_(DMFT))
- [4 Other
  methods](#Other_methods)
  - [4.1 Hybrid
    functionals](#Hybrid_functionals)
  - [4.2 Hybrid
    functionals + U](#Hybrid_functionals_+_U)
  - [4.3
    Quasi-particle GW
    (QPGW)](#Quasi-particle_GW_(QPGW))
- [5 Additional
  resources](#Additional_resources)
  - [5.1
    Books](#Books)
- [6
  References](#References)


## Estimating the on-site Coulomb interaction U\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Estimating the on-site Coulomb interaction U">edit</a> \| (./index.php.md)\]

<a href="/wiki/DFT%2BU" class="mw-redirect" title="DFT+U">DFT+U</a> and
[DFT+DMFT
calculations](../tutorials/DFT+DMFT_calculations.md)
rely on the on-site Coulomb interaction U as an input parameter. There
are some strategies to obtain a value for U:

- Estimate U based on available experimental results. This approach is
  not fully ab initio, yet it can be the most pragmatic strategy. Here
  one treats the effective on-site interaction
  $U$ as an adjustable parameter, tuning it to reproduce
  selected experimental observables such as the band gap, magnetic
  moments, or lattice parameters. For instance, one may perform [volume
  relaxations](Volume_relaxation.md) at different
  U values to obtain volume as a function of U, \$v(U)\$. Knowing the
  experimental value for the volume, a linear fit of \$v(U)\$ can give
  an estimate for a suitable U value. This approach relies on the fact
  that the expansion or localization of the strongly correlated d or f
  electron orbitals drives the ions to relax at a certain distance. One
  then use the fixed U value to obtain other quantities like band gap,
  optical properties. Another approach can be to fit the optical gap to
  ensure the band-structure properties resemble the experiment, which is
  crucial for, e.g., binding energies or excited states calculations.

<!-- -->

- Linear-response calculation of $U$
  ([`LDAUTYPE`](../incar-tags/LDAUTYPE.md)` = 3`). Within this approach
  the effective interaction $U$ can be
  determined via the linear response approach
  <sup>[\[2\]](#cite_note-cococcioni:2005-2)</sup>

$U=\chi^{-1}-\chi_0^{-1} \approx\left(\frac{\partial
N_I^{\mathrm{SCF}}}{\partial V_I}\right)^{-1}-\left(\frac{\partial
N_I^{\mathrm{NSCF}}}{\partial V_I}\right)^{-1}.$

The shortcoming of this method is that the effective interaction
accounts for the response due to all electrons including the target
states (localized $d$ or
$f$ orbitals), thus leading to double counting in the
derived effective potential U.

- Workflow for <a href="https://vasp.at/wiki/Calculate_U_for_LSDA%2BU"
  class="external text" rel="nofollow">NiO Calculate U for LSDA+U
  calculations</a>.

<!-- -->

- [Constrained random phase approximation
  (cRPA)](../theory/Constrained–random-phase–approximation_formalism.md)
  is a first-principles method to estimate U. cRPA allows to separate
  the screening originating from the target states from the rest of the
  system and to determine the effective interaction
  $U$ that is free of double counting.

The response function without the contribution of the target states or
constrained polarizability $\chi_c$ is
calculated by explicitly removing the response in the target space
$\chi_d$ from the total response function:

$\chi_c(\omega) = \chi(\omega) - \chi_d(\omega)$.

[VASP provides several approaches for calculating
$\chi_d$](/wiki/Constrained%E2%80%93random-phase%E2%80%93approximation_formalism#Effective_Coulomb_kernel_in_constrained_random-phase_approximation "Constrained–random-phase–approximation formalism")

- Lecture on the
  <a href="https://youtu.be/z5sqTVLxZKA" class="external text"
  rel="nofollow">constrained random-phase approximation</a> (cRPA).
- Workflow for [CRPA of SrVO3](../misc/CRPA_of_SrVO3.md).

## DFT+U\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: DFT+U">edit</a> \| (./index.php.md)\]

[DFT+U](Category-DFT+U.md) is the simplest and the
most computationally efficient approach to treat strong correlations
within electronic structure calculations. Within this approach, standard
DFT is augmented with an on-site [Hubbard interaction term
$U$](/wiki/LDAU "LDAU") that explicitly penalizes
fractional occupation of localized orbitals. The Hubbard interaction is
typically applied to $d$ or
$f$ states.

|  |
|----|
| **Mind:** It is not currently possible to apply $U$ to both $d$ and $f$ states of the same atom |

The total energy within DFT+U can be written as

$E=E_{DFT}+\sum_I\left\[\frac{U^I}{2} \sum_{m, \sigma \neq m^{\prime},
\sigma^{\prime}} n_m^{I \sigma} n_{m^{\prime}}^{I
\sigma^{\prime}}-\frac{U^I}{2} n^I\left(n^I-1\right)\right\],$

where the first term is the standard DFT energy, the second term is the
Hubbard on-site interaction and the third term accounts for the double
counting. The on-site interaction is described by
$U^I$ and $n_m^{I\sigma}$ are occupation numbers that are defined as projections
of occupied Kohn-Sham orbitals on the states of a localized basis set.

- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/bulk/part3/#bulk-e09"
  class="external text" rel="nofollow">NiO DFT+U calculations</a>.
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part1/#mag-e03"
  class="external text" rel="nofollow">antiferromagnetic NiO</a>.
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part1/#mag-e04"
  class="external text" rel="nofollow">LSDA+U structure relaxation of
  NiO</a>.
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part2/#mag-e05"
  class="external text" rel="nofollow">Heisenberg model for NiO using
  DFT+U</a>.
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part2/#mag-e07"
  class="external text" rel="nofollow">magnetic anisotropy in FeO</a>.

## Dynamical mean-field theory (DMFT)\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Dynamical mean-field theory (DMFT)">edit</a> \| (./index.php.md)")\]

In [DFT+DMFT
calculations](../tutorials/DFT+DMFT_calculations.md),
DMFT<sup>[\[3\]](#cite_note-kotliar:rmp:2006-3)</sup>
augments the DFT calculation with an additional local correlated
subproblem — typically a specific $d$- or
$f$-shell. The key idea is to map the full lattice problem
onto a quantum impurity model: a single correlated site embedded in a
self-consistently determined effective bath representing the rest of the
lattice. DMFT can be discussed using the [Green's function
formalism](GW_approximation_of_Hedin's_equations.md)
also used in the context of
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>.
The main quantity is the electronic self-energy. Within DMFT it is
defined as the sum of all one-particle irreducible diagrams. The central
approximation is that the self-energy is frequency-dependent but
momentum-independent, i.e., purely local. [DFT+DMFT
calculations](../tutorials/DFT+DMFT_calculations.md)
capture many-body effects beyond the reach of DFT+U, such as
quasiparticle mass renormalization, Hubbard bands, and the Mott
metal–insulator transition. The interaction parameter entering DMFT can
be determined as discussed in [estimating the on-site Coulomb
interaction U](#Estimating_the_on-site_Coulomb_interaction_U).

- Workflow for [NiO DFT+DMFT
  calculations](../tutorials/DFT+DMFT_calculations.md).

## Other methods\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Other methods">edit</a> \| (./index.php.md)\]

There are other methods that, while not specifically designed for
strongly correlated systems, have nonetheless been demonstrated to
improve their description and electronic structure.

### Hybrid functionals\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Hybrid functionals">edit</a> \| (./index.php.md)\]

By incorporating a fraction of exact exchange, [hybrid
functionals](Category-Hybrid_functionals.md)
partially mitigate the self-interaction error inherent to standard DFT.
This reduction of the self-interaction error has been shown to yield an
improved description of strongly correlated systems
<sup>[\[4\]](#cite_note-Silva2007-4)[\[5\]](#cite_note-liu2019assessing-5)</sup>.

### Hybrid functionals + U\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Hybrid functionals + U">edit</a> \| (./index.php.md)\]

A well-known limitation of hybrid functionals is their uniform treatment
of all electronic states, which can result in markedly different levels
of accuracy for states with varying degrees of localization. The
inclusion of the Hubbard on-site interaction term within the hybrid
functional framework ([hybrid +
U](../categories/Category-Exchange-correlation_functionals.md) "Category:Exchange-correlation functionals"))
has been shown to address inaccuracies arising from the overscreening of
localized states
<sup>[\[6\]](#cite_note-Ivady2014-6)</sup>.

### Quasi-particle GW (QPGW)\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Quasi-particle GW (QPGW)">edit</a> \| (./index.php.md)")\]

The [GW](../theory/Category-GW.md) approximation in its simplest,
non-self-consistent form (i.e., the one-shot approach) exhibits a strong
dependence on the choice of starting point, and thus inherits the
limitations of the underlying DFT description of localized states. In
contrast, self-consistent GW schemes such as QPGW, which are independent
of the starting electronic structure, have been shown to provide an
accurate description of correlated electrons
<sup>[\[7\]](#cite_note-Cunningham2023-7)[\[8\]](#cite_note-shishkin:prl:2007-8)</sup>.

## Additional resources\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Books\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Books">edit</a> \| (./index.php.md)\]

- *Interacting Electrons - Theory and Computational Approaches* by
  Richard Martin, Lucia Reining, and David Ceperley - a book about
  strong correlation
  <sup>[\[1\]](#cite_note-martin:book:2016-1)</sup>.
- *Dynamical Mean-Field Theory for Strongly Correlated Materials* by
  Volodymyr Turkowski - a book about DMFT
  <sup>[\[9\]](#cite_note-turkowski:book:2021-9)</sup>.

## References\[<a
href="/wiki/index.php?title=Category:Strongly_correlated_electrons&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-martin:book:2016_1-0)</sup>
    <sup>[b](#cite_ref-martin:book:2016_1-1)</sup>
    <a href="https://doi.org/10.1017/CBO9781139050807" class="external text"
    rel="nofollow">R. Martin, L. Reining, D. Ceperley, <em>Interacting
    Electrons: Theory and Computational Approaches</em>, Cambridge
    University Press (2016).</a>
2.  [↑](#cite_ref-cococcioni:2005_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.71.035105"
    class="external text" rel="nofollow">M. Cococcioni and S. de Gironcoli,
    Phys. Rev. B <strong>71</strong>, 035105 (2005).</a>
3.  [↑](#cite_ref-kotliar:rmp:2006_3-0)
    <a href="https://link.aps.org/doi/10.1103/RevModPhys.78.865"
    class="external text" rel="nofollow">G. Kotliar, S. Y. Savrasov, K.
    Haule, V. S. Oudovenko, O. Parcollet, and C. A. Marianetti,
    <em>Electronic structure calculations with dynamical mean-field
    theory</em>, Rev. Mod. Phys. <strong>78</strong>, 865 (2006)</a>
4.  [↑](#cite_ref-Silva2007_4-0)
    <a href="http://dx.doi.org/10.1103/PhysRevB.75.045121"
    class="external text" rel="nofollow">Juarez L. F. Da Silva, M. Verónica
    Ganduglia-Pirovano, Joachim Sauer, Veronika Bayer, Phys. Rev. B
    <strong>75</strong>, 045121 (2007).</a>
5.  [↑](#cite_ref-liu2019assessing_5-0)
    <a href="https://doi.org/10.1088/1361-648x/ab4150" class="external text"
    rel="nofollow">P. Liu, C. Franchini, M. Marsman, and G. Kresse,
    <em>Assessing model-dielectric-dependent hybrid functionals on the
    antiferromagnetic transition-metal monoxides MnO, FeO, CoO, and
    NiO</em>, J. Phys.: Condens. Matter <strong>32</strong>, 015502
    (2020).</a>
6.  [↑](#cite_ref-Ivady2014_6-0)
    <a href="http://dx.doi.org/10.1103/PhysRevB.90.035146"
    class="external text" rel="nofollow">Viktor Ivády, Rickard Armiento,
    Krisztián Szász, Erik Janzén, Adam Gali, Phys. Rev. B
    <strong>90</strong>, 035146 (2014).</a>
7.  [↑](#cite_ref-Cunningham2023_7-0)
    <a href="http://dx.doi.org/10.1103/PhysRevB.108.165104"
    class="external text" rel="nofollow">Brian Cunningham, Myrta Grüning,
    Dimitar Pashov, Phys. Rev. B <strong>108</strong>, 165104 (2023).</a>
8.  [↑](#cite_ref-shishkin:prl:2007_8-0)
    <a href="https://doi.org/10.1103/PhysRevLett.99.246403"
    class="external text" rel="nofollow">M. Shishkin, M. Marsman, and G.
    Kresse, Phys. Rev. Lett. <strong>99</strong>, 246403 (2007).</a>
9.  [↑](#cite_ref-turkowski:book:2021_9-0)
    <a href="https://doi.org/10.1007/978-3-030-64904-3"
    class="external text" rel="nofollow">V. Turkowski, <em>Dynamical
    Mean-Field Theory for Strongly Correlated Materials</em>, Springer Cham
    (2021).</a>



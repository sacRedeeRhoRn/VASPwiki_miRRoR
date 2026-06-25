<!-- Source: https://vasp.at/wiki/index.php/Category:Transition_States | revid: 22452 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Transition States


<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Transition_state_pathway.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/8/88/Transition_state_pathway.png/400px-Transition_state_pathway.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/8/88/Transition_state_pathway.png/600px-Transition_state_pathway.png 1.5x, /wiki/images/thumb/8/88/Transition_state_pathway.png/800px-Transition_state_pathway.png 2x"
width="400" height="343" /></a>
<figcaption>Reaction profile for the substitution reaction of
chloromethane by chloride. This is a symmetric reaction, where the
products and reactants are identical. The maximum of the reaction
profile is the transition state (TS). The arrows indicate the direction
of motion, showing the attack of the chloromethane by one chloride and
then the ejection by the new chloride.</figcaption>
</figure>

A **transition state** (TS) in chemistry refers to a high-energy,
short-lived configuration that occurs during a chemical reaction as
reactants transform into
products[^tst:web-1].
At this point, the reaction's progress is maximized. In other words, the
transition state is a metastable structure that corresponds to a saddle
point on the high-dimensional potential energy surface
(PES)[^hratchian:schlegel:2005-2].

Identifying the transition state is essential for understanding reaction
mechanisms, energy barriers, and rates of reaction. The energy barrier
is calculated from the energy difference between the reactant R and TS
(for the forward reaction) or the product P and TS (for the reverse
reaction). It is important to remember that the TS can be reached from
either R or P; whichever is more favored depends only on the respective
reaction barrier. A single unstable vibrational mode (an imaginary
frequency) connects R and P. For comparison to experimental values,
additional thermodynamic corrections can be made to the simple energetic
barrier, including the zero-point vibrational energy, the population of
the vibrational states, and entropy to enable better comparison to the
experiment[^mcquarrie:2000-3].
It is also possible to model solid-solid phase transitions in a similar
manner[^henkelman:jcp:2012-4].

There are many thorough review articles and books on transition state
theory
(TST)[^truhlar:jpc:1996-5][^roussel:2023-6]
and its subsequent development variational TST
(VTST)[^truhlar:csr:2017-7]
which we refer to for the interested reader. There are various methods
available to pinpoint transition states in VASP.


## Contents


- [1 Static
  methods](#static-methods)
  - [1.1 Improved
    dimer method](#improved-dimer-method)
  - [1.2 Nudged
    elastic bands](#nudged-elastic-bands)
  - [1.3 Intrinsic
    reaction coordinate](#intrinsic-reaction-coordinate)
- [2 Dynamic
  methods](#dynamic-methods)
- [3 Additional
  resources](#additional-resources)
  - [3.1
    Books](#books)
  - [3.2 How
    to](#how-to)
  - [3.3
    Tutorials](#tutorials)
  - [3.4
    Lectures](#lectures)
- [4
  References](#references)


## Static methods\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Static methods">edit</a> \| (./index.php.md)\]

There are three static methods implemented in VASP for finding
transition states (TS) using the static, or harmonic, approach: the
improved dimer method (IDM), nudged elastic band (NEB), and following
the intrinsic reaction coordinate (IRC). IDM takes a guess structure for
the TS and then relaxes it along a trial unstable vibrational mode to a
first-order saddle point, i.e. the TS. NEB takes the reactant and
product structures and interpolates structures between the two to model
the reaction pathway. IRC starts at the TS and follows the TS' unstable
vibrational mode to reactant and product.

### Improved dimer method\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Improved dimer method">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Idm_single_image.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/0/0e/Idm_single_image.png/250px-Idm_single_image.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/0e/Idm_single_image.png/375px-Idm_single_image.png 1.5x, /wiki/images/thumb/0/0e/Idm_single_image.png/500px-Idm_single_image.png 2x"
width="250" height="205" /></a>
<figcaption>A dimer consisting of two points on the potential energy
surface (PES) is rotated to find the lowest curvature. The structure is
updated and then a new dimer is defined. The IDM converges towards the
desired saddle point, i.e. the TS.</figcaption>
</figure>

The dimer
method[^henkelman:jpc:1999-8]
is a technique for determining activated transitions without knowledge
of the final state. Beginning with a trial transition state (TS)
structure, a relaxed TS is obtained. In VASP, the improved dimer method
(IDM) by Heyden et al. is implemented. The modification reduces the
number of gradient calculations per cycle, improving algorithm
performance. A detailed presentation of the method can be found in their
paper[^heyden:jpc:2005-9].
The main tag is [IBRION](../incar-tags/IBRION.md)=44.

Follow the how-to in order to learn [how to perform an IDM
calculation](https://vasp.at/wiki/index.php/Improved_dimer_method).


### Nudged elastic bands\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Nudged elastic bands">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:NEB.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/e/e1/NEB.png/300px-NEB.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/e/e1/NEB.png/450px-NEB.png 1.5x, /wiki/images/thumb/e/e1/NEB.png/600px-NEB.png 2x"
width="300" height="207" /></a>
<figcaption>The potential energy surface (PES) is described by a series
of images (blue) connected by springs (green arrows). The initial
(reactant) and final (product) states are shown in black and remain
fixed. The TS is the maximum of the PES (red).</figcaption>
</figure>

The nudged elastic band (NEB)
method[^mills:surf-sci:1995-10][^jonsson:book:1998-11]
involves the creation of an initial path connecting the system's initial
and final states, utilizing a set of intermediate configurations
([IMAGES](../incar-tags/IMAGES.md)). Hence, as a prerequisite, the initial
and final state (e.g., reactant and product) must be known. The *images*
are interconnected by springs ([SPRING](../incar-tags/SPRING.md)), forming
a flexible *band*. Through iterative adjustments (*nudging*), the
positions of the images along the band are modified, minimizing energy
until a minimum energy pathway, referred to as the *nudged elastic
band*, is attained.

Learn [how to perform an NEB
calculation](../tutorials/Nudged_elastic_bands.md).


### Intrinsic reaction coordinate\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Intrinsic reaction coordinate">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:IRC.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/45/IRC.png/500px-IRC.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/45/IRC.png/750px-IRC.png 1.5x, /wiki/images/thumb/4/45/IRC.png/1000px-IRC.png 2x"
width="500" height="201" /></a>
<figcaption>The potential energy surface (PES) is shown as a contour
plot. The IRC begins at TS and follows the associated imaginary
frequency $u_{\xi}$ forward
to the product P (red) or backward to the reactant R (blue). The energy
$U(\chi)$ is plotted against the complex coordinate $\chi$ to illustrate the energy change as the PES is
explored.</figcaption>
</figure>

Following the intrinsic reaction coordinate (IRC) implies following the
steepest descent path from the transition state to reactants and
products. The IRC method employs a classical trajectory integration
method with fixed velocity, i.e., the damped-velocity Verlet algorithm,
incorporating an adaptive time step such that the dynamic reaction
pathway resembles the IRC. Hence, as a prerequisite, the transition
state must be known. The main tag is [IBRION](../incar-tags/IBRION.md)=40.

Learn <a href="/wiki/IRC_calculations" class="mw-redirect"
title="IRC calculations">how to perform an IRC calculation</a>.


## Dynamic methods\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Dynamic methods">edit</a> \| (./index.php.md)\]

An alternative to the static approach for modeling the TS, is to use a
dynamic (or anharmonic) approach, that is to use molecular dynamics
(MD). The static approach models a single structure for the reactant R,
TS, and product P. An MD simulation treats each of these states as an
ensemble, a combination of many possible structures.

It is difficult to use MD to find uncommon states or rare events, such
as the TS. An MD simulation is for a short period of time, typically
only femto or picoseconds, while seconds would be required to encounter
a TS. However, using [constrained
MD](../theory/Constrained_molecular_dynamics.md),
e.g. a [blue moon
simulation](../theory/Blue_moon_ensemble.md)[^gesvandtnerova:rucco:bucko:2021-12],
a path-based coordinate ([IRCCAR](../input-files/IRCCAR.md)), or
[metadynamics](../theory/Metadynamics.md) (cf. [metadynamics for
transition state
MLFFs](../methods/Using_metadynamics_to_train_a_machine-learned_force_field.md))[^klein:2006-13][^tiwary:parrinello:2006-14],
finding even rare events like the TS becomes feasible.

More detail for each of these methods, as well as other advanced MD
approaches can be found on the [advanced
MD](Category-Advanced_molecular-dynamics_sampling.md)
category page.

## Additional resources\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Books\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Books">edit</a> \| (./index.php.md)\]

- *Investigating chemical reactions with VASP - A practical guide* by
  Tomáš Bučko - a book guiding modeling chemical reactions in VASP
  [^bucko:book:2025-15].

### How to\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

- Training an [MLFF for transition states using
  metadynamics](../methods/Using_metadynamics_to_train_a_machine-learned_force_field.md).

### Tutorials\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/transition_states/part1"
  class="external text" rel="nofollow">NEB, IDM, elbow plot, and IRC
  calculations</a>.
- Tutorial for modeling reaction pathways and calculating free energies
  of reaction using
  <a href="https://www.vasp.at/tutorials/latest/transition_states/part2"
  class="external text" rel="nofollow">static methods</a>.
- Tutorial for modeling reaction pathways and calculating free energies
  of reaction using
  <a href="https://www.vasp.at/tutorials/latest/transition_states/part3"
  class="external text" rel="nofollow">dynamic methods</a>.
- Tutorial for <a href="https://www.vasp.at/tutorials/latest/md/part3"
  class="external text" rel="nofollow">dynamic methods for
  chloromethane-chloride inversion</a>.

### Lectures\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on modeling chemical reactions (and transition states) using
  <a href="https://youtu.be/mLK7CtDmw0A" class="external text"
  rel="nofollow">static approaches</a>.
- Lecture on modeling chemical reactions (and transition states) using
  <a href="https://youtu.be/Rk0S-yvxFUo" class="external text"
  rel="nofollow">dynamic approaches</a>.
- Lecture on modeling chemical reactions (and transition states) using
  <a href="https://youtu.be/bzzHpTBwxbA" class="external text"
  rel="nofollow">machine-learned force fields</a>.

## References\[<a
href="/wiki/index.php?title=Category:Transition_states&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^tst:web-1]: [Transition state theory, www.wikipedia.org (2024)](https://en.wikipedia.org/wiki/Transition_state_theory)
[^hratchian:schlegel:2005-2]: [H. Hratchian, H. Schlegel, Theory and Application of Computational Chemistry, Chapter 10 - Finding minima, transition states, and following reaction pathways on ab initio potential energy surfaces (2005), p. 195-249](https://www.sciencedirect.com/science/article/abs/pii/B9780444517197500536)
[^mcquarrie:2000-3]: [D. McQuarrie, *Statistical Mechanics*, (2000).](https://uscibooks.aip.org/books/statistical-mechanics/)
[^henkelman:jcp:2012-4]: [D. Sheppard, P. Xiao, W. Chemelweski, D. Johnson, G. Henkelman, *A generalized solid-state nudged elastic band method*, J. Chem. Phys. **136**, 074103 (2012).](https://doi.org/10.1063/1.3684549)
[^truhlar:jpc:1996-5]: [D. Truhlar, B. Garrett, and S. Klippenstein, *Current Status of Transition-State Theory*, J. Phys. Chem. **100**, 12771 (1996).](https://doi.org/10.1039/C7CS00602K)
[^roussel:2023-6]: [M. Roussel, *Foundations of Chemical Kinetics, Chapter 7 - Transition-state theory*, (2023), p. 195-249.](https://doi.org/10.1088/978-0-7503-5321-2)
[^truhlar:csr:2017-7]: [J. Bao and D. Truhlar, *Variational transition state theory: theoretical framework and recent developments*, Chem. Soc. Rev. **46**, 7548 (2017).](https://doi.org/10.1039/C7CS00602K)
[^henkelman:jpc:1999-8]: [G. Henkelman and H. Jónsson, *A dimer method for finding saddle points on high dimensional potential surfaces using only first derivatives*, J. Chem. Phys. **111**, 7010–7022 (1999).](https://doi.org/10.1063/1.480097)
[^heyden:jpc:2005-9]: [A. Heyden, A. T. Bell, and F. J. Keil, *Efficient methods for finding transition states in chemical reactions: Comparison of improved dimer method and partitioned rational function optimization method*, J. Chem. Phys. **123**, 224101 (2005).](https://doi.org/10.1063/1.2104507)
[^mills:surf-sci:1995-10]: [G. Mills, H. Jonsson and G. K. Schenter, *Reversible work transition state theory: application to dissociative adsorption of hydrogen*, Surf. Sci., **324**, 305 (1995).](http://doi.org/10.1016/0039-6028(94)00731-4)
[^jonsson:book:1998-11]: [H. Jonsson, G. Mills and K. W. Jacobsen, *Nudged Elastic Band Method for Finding Minimum Energy Paths of Transitions*, in *Classical and Quantum Dynamics in Condensed Phase Simulations*, ed. B. J. Berne, G. Ciccotti and D. F. Coker (World Scientific, 1998).](https://doi.org/10.1142/9789812839664_0016)
[^gesvandtnerova:rucco:bucko:2021-12]: [M. Gešvandtnerová, D. Rocca, T. Bučko, *Methanol carbonylation over acid mordenite: Insights from ab initio molecular dynamics and machine learning thermodynamic perturbation theory*, J. Catal. **396**, 166 (2021).](https://doi.org/10.1016/j.jcat.2021.02.011)
[^klein:2006-13]: [B. Ensing, M. De Vivo, Z. Liu, P. Moore, M. Klein, *Metadynamics as a Tool for Exploring Free Energy Landscapes of Chemical Reactions*, Acc. Chem. Res. **39**, 73 (2006)](https://doi.org/10.1021/ar040198i)
[^tiwary:parrinello:2006-14]: [P. Tiwary, M. Parrinello, *From Metadynamics to Dynamics*, Phys. Rev. Lett. **111**, 230602 (2013).](https://doi.org/10.1103/PhysRevLett.111.230602)
[^bucko:book:2025-15]: [T. Bučko, *Investigating chemical reactions with VASP - A practical guide*, Comenius University Bratislava (2025), p.50-51.](https://stella.uniba.sk/texty/PRIF_TB_investigating_chemical_reactions_vasp.pdf)

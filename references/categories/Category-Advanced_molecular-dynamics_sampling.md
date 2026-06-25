<!-- Source: https://vasp.at/wiki/index.php/Category:Advanced_molecular-dynamics_sampling | revid: 37176 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Advanced molecular-dynamics sampling


In a
[molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
(MD) calculation, we are often interested in rare events or specific
transitions. **Advanced molecular-dynamics sampling** helps to capture
these during an MD run within a feasible simulation time. There are
several different available methods:

- <a href="#Thermodynamic_integration"
  class="mw-selflink-fragment">Thermodynamic integration</a>
- <a href="#Constrained_molecular_dynamics"
  class="mw-selflink-fragment">Constrained molecular dynamics</a>
- <a href="#Biased_molecular_dynamics" class="mw-selflink-fragment">Biased
  molecular dynamics</a>
- <a href="#Metadynamics" class="mw-selflink-fragment">Metadynamics</a>
- <a href="#Blue_moon_ensemble" class="mw-selflink-fragment">Blue moon
  ensemble</a>
- <a href="#Slow-growth_approach" class="mw-selflink-fragment">Slow-growth
  approach</a>
- <a href="#Interface_pinning" class="mw-selflink-fragment">Interface
  pinning</a>


## Contents


- [1 Thermodynamic
  integration](#Thermodynamic_integration)
- [2 Constrained
  molecular dynamics](#Constrained_molecular_dynamics)
- [3 Biased
  molecular dynamics](#Biased_molecular_dynamics)
- [4
  Metadynamics](#Metadynamics)
- [5 Blue moon
  ensemble](#Blue_moon_ensemble)
- [6 Slow-growth
  approach](#Slow-growth_approach)
- [7 Interface
  pinning](#Interface_pinning)
- [8 Additional
  resources](#Additional_resources)
  - [8.1
    Books](#Books)
  - [8.2
    Tutorials](#Tutorials)
  - [8.3
    Lectures](#Lectures)
- [9
  References](#References)


## Thermodynamic integration\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Thermodynamic integration">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Thermodynamic_integration.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/0/0b/Thermodynamic_integration.png/250px-Thermodynamic_integration.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/0b/Thermodynamic_integration.png/375px-Thermodynamic_integration.png 1.5x, /wiki/images/thumb/0/0b/Thermodynamic_integration.png/500px-Thermodynamic_integration.png 2x"
width="250" height="234" /></a>
<figcaption>Thermodynamic integration allows integration from a
non-interacting system (λ = 0) to an interacting system (λ = 1). E.g.,
between a harmonic and an anharmonic system.</figcaption>
</figure>

In the [thermodynamic
integration](../theory/Thermodynamic_integration.md)
method,<sup>[\[1\]](#cite_note-dorner:PRL:2018-1)[\[2\]](#cite_note-kirkwood:jcp:1935-2)</sup>
the energy differences of a fully interacting and non-interacting system
are calculated. This is achieved by making the potential energy depend
on a coupling parameter and defining the free energy as a smooth
integral over the potential energy along this coupling parameter. As the
reference state for a non-interacting system, usually an [ideal
gas](../incar-tags/SCALEE.md) or a [harmonic
solid](../incar-tags/TILAMBDA.md) is chosen.

[Thermodynamic
integration](../theory/Thermodynamic_integration.md)
is usually used to compute free energy differences between [different
phases](../incar-tags/VCAIMAGES.md).

- [Thermodynamic
  integration](../theory/Thermodynamic_integration.md)
- [Thermodynamic integration
  calculations](../tutorials/Thermodynamic_integration_calculations.md)


## Constrained molecular dynamics\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Constrained molecular dynamics">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Constrained_MD.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/b/b8/Constrained_MD.png/250px-Constrained_MD.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/b/b8/Constrained_MD.png/375px-Constrained_MD.png 1.5x, /wiki/images/thumb/b/b8/Constrained_MD.png/500px-Constrained_MD.png 2x"
width="250" height="146" /></a>
<figcaption>Selected geometric parameters in this hydrogen cyanide
isomerization to hydrogen isocyanide reaction are constrained to model
the transition state. R<sub>1</sub> is the C-H bond, R<sub>2</sub> is
the C-N bond, and R<sub>3</sub> is the N-H bond.</figcaption>
</figure>

In [constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)
selected geometric parameters are constrained during the calculations
using the [ICONST](../input-files/ICONST.md) file. This is achieved by
extending the Lagrangian with a term incorporating the desired
constraints ([SHAKE
algorithm](../theory/Constrained_molecular_dynamics.md)<sup>[\[3\]](#cite_note-ryckaertt:jcp:1977-3)</sup>)
directly. This method can be used on its own to support molecular
dynamics calculations but some of the methods on this page also
incorporate constraints via the same methodology.

- [Constrained molecular
  dynamics](../theory/Constrained_molecular_dynamics.md).
- [Constrained molecular dynamics
  calculations](../tutorials/Constrained_molecular_dynamics_calculations.md).


## Biased molecular dynamics\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Biased molecular dynamics">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Umbrella_sampling.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/9/92/Umbrella_sampling.png/250px-Umbrella_sampling.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/9/92/Umbrella_sampling.png/375px-Umbrella_sampling.png 1.5x, /wiki/images/thumb/9/92/Umbrella_sampling.png/500px-Umbrella_sampling.png 2x"
width="250" height="236" /></a>
<figcaption>In biased MD, a biased potential can be used to pin the
system to given configuration (i.e., uncommon configurations), e.g., in
umbrella sampling.</figcaption>
</figure>

[Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md)
refers to methods introducing a biased potential
<sup>[\[4\]](#cite_note-frenkel:ap-book:2002-4)</sup>.
In one of this method's most popular representatives, the umbrella
sampling or umbrella integration, the biased potential is used to pin
the system to given configurations. This way the sampling of a system is
greatly enhanced and thermodynamic methods with proper statistics become
accessible. Although some of the methods on this page also use biased
potentials they have differences in the usage of the potential and hence
belong in their categories.

[Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md)
are often used to calculate free energies or free energy differences.

- [Biased molecular
  dynamics](../theory/Biased_molecular_dynamics.md).
- [Biased molecular dynamics
  calculations](../tutorials/Biased_molecular_dynamics_calculations.md).


## Metadynamics\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Metadynamics">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Metadynamics.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/78/Metadynamics.png/250px-Metadynamics.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/78/Metadynamics.png/375px-Metadynamics.png 1.5x, /wiki/images/thumb/7/78/Metadynamics.png/500px-Metadynamics.png 2x"
width="250" height="235" /></a>
<figcaption>In metadynamics, a biased potential (coloured lines) is
applied along selected collective variables (x), cf. potential V, to
gradually fill free-energy minima and allows the system to cross
barriers and explore the potential energy surface, including other
minima.</figcaption>
</figure>

In
[metadynamics](../theory/Metadynamics.md),<sup>[\[5\]](#cite_note-laio:pnas:02-5)[\[6\]](#cite_note-iannuzzi:prl:03-6)</sup>
a [biased potential](../input-files/PENALTYPOT.md) that acts on a few
selected geometric parameters (collective variables) is added to the
Hamiltonian of a system. The biased potential is constantly built up
during a molecular dynamics run by adding [Gaussian
hills](../incar-tags/HILLS_H.md) at selected time increments. This way
even deep potential minima can be filled and overcome.

This method is good for exploring new phases of a given system.

- [Metadynamics](../theory/Metadynamics.md).
- [Metadynamics
  calculations](../tutorials/Metadynamics_calculations.md).
- [Using metadynamics to train a machine-learned force
  field](../methods/Using_metadynamics_to_train_a_machine-learned_force_field.md)


## Blue moon ensemble\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Blue moon ensemble">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Blue_moon.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/f1/Blue_moon.png/250px-Blue_moon.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/f1/Blue_moon.png/375px-Blue_moon.png 1.5x, /wiki/images/thumb/f/f1/Blue_moon.png/500px-Blue_moon.png 2x"
width="250" height="240" /></a>
<figcaption>In the Blue moon ensemble method, the free energy profile
along a chosen reaction coordiante (x) can be calculated by calculating
the unbiased free-energy derivative.</figcaption>
</figure>

The [blue moon ensemble](../theory/Blue_moon_ensemble.md)
method<sup>[\[7\]](#cite_note-carter:kapral:1989-7)</sup>
is designed to calculate the free energy profile along the path of
selected reaction coordinates. It also employs constraining of the atoms
during molecular dynamics ([SHAKE
algorithm](../theory/Constrained_molecular_dynamics.md)<sup>[\[3\]](#cite_note-ryckaertt:jcp:1977-3)</sup>).
The term "[blue moon](../incar-tags/LBLUEOUT.md)" refers to rare events
such as the "moon turning blue".

The method is often used to calculate free energy differences for
systems where the profile is characterized by a few barriers that are
high enough that they would not be crossed within regular thermostatted
molecular dynamics.

- [Blue moon ensemble](../theory/Blue_moon_ensemble.md).
- [Blue moon ensemble
  calculations](../tutorials/Blue_moon_ensemble_calculations.md).


## Slow-growth approach\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Slow-growth approach">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Slow_growth_md.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/0/0a/Slow_growth_md.png/250px-Slow_growth_md.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/0a/Slow_growth_md.png/375px-Slow_growth_md.png 1.5x, /wiki/images/thumb/0/0a/Slow_growth_md.png/500px-Slow_growth_md.png 2x"
width="250" height="235" /></a>
<figcaption>In the slow-growth approach, a reaction pathway can be
followed linearly on a reaction coordinate (x) from the reactant state
(λ = 0) to the target state (λ = 1).</figcaption>
</figure>

In the [slow-growth
approach](../theory/Slow-growth_approach.md),<sup>[\[8\]](#cite_note-woo:ziegler:1997-8)</sup>
the free energy profile is scanned along a reaction coordinate. The
scanning is done by linearly changing the reaction coordinate from that
of the reactant state to that of a transition or product state via
[constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)
([SHAKE
algorithm](../theory/Constrained_molecular_dynamics.md)<sup>[\[3\]](#cite_note-ryckaertt:jcp:1977-3)</sup>).

Like in the [blue moon
ensemble](../theory/Blue_moon_ensemble.md), this method is
also designed to calculate free energy differences for systems where the
profile is characterized by a few barriers that are high enough that
they would not be crossed within regular thermostatted molecular
dynamics.

- [Slow-growth
  approach](../theory/Slow-growth_approach.md).
- [Slow-growth approach
  calculations](../tutorials/Slow-growth_approach_calculations.md).


## Interface pinning\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Interface pinning">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Water_ice_interface.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/0/0a/Water_ice_interface.png/250px-Water_ice_interface.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/0a/Water_ice_interface.png/375px-Water_ice_interface.png 1.5x, /wiki/images/thumb/0/0a/Water_ice_interface.png/500px-Water_ice_interface.png 2x"
width="250" height="216" /></a>
<figcaption>Interface pinning is used to model two different phases on
the same system in the same cell, e.g., the water-ice
interface.</figcaption>
</figure>

In [interface
pinning](../theory/Interface_pinning.md),<sup>[\[9\]](#cite_note-pedersen:prb:13-9)</sup>
two different phases of the same system are simulated in a single
simulation box. The goal of this method is to look for the right
conditions where both phases would coexist, which corresponds to a phase
transition point. Above a transition point, the whole system would
quickly turn into one phase and below the point into the other phase.
With this, the transition point could be searched via bi-sectioning, but
this would involve a huge effort. To accelerate the search for a phase
transition point the order parameters are used to control the
composition of the box and the force that would drive the system towards
equilibrium is used to estimate the phase transition point.

[Interface pinning](../theory/Interface_pinning.md) is
usually used to determine melting points (solid-liquid interface).

- [Interface pinning](../theory/Interface_pinning.md).
- [Interface pinning
  calculations](../tutorials/Interface_pinning_calculations.md).


## Additional resources\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Books\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Books">edit</a> \| (./index.php.md)\]

- *Statistical Mechanics: Theory and Molecular Simulation* by M.
  Tuckerman
  <sup>[\[10\]](#cite_note-tuckerman:book:2023-10)</sup>.
- *Understanding Molecular Simulation - From Algorithms to Applications*
  by D. Frenkel and B. Smit
  <sup>[\[11\]](#cite_note-frenkel:smit:2023-11)</sup>.

### Tutorials\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for chloromethane-chloride inversion
  <a href="https://www.vasp.at/tutorials/latest/md/part3/#MD-e08"
  class="external text" rel="nofollow">using the slow-growth approach,
  blue-moon ensemble, and constrained MD</a>.
- Tutorial for a chemical reaction in a zeolite
  <a href="https://www.vasp.at/tutorials/latest/transition_states/part3"
  class="external text" rel="nofollow">using the slow-growth approach,
  blue-moon ensemble, and constrained MD</a>.

### Lectures\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on
  <a href="https://youtu.be/HVeamQOmM-s" class="external text"
  rel="nofollow">advanced methods of MD</a>.
- Lecture on
  <a href="https://youtu.be/Rk0S-yvxFUo" class="external text"
  rel="nofollow">advanced methods of MD applied to a chemical reaction</a>.

## References\[<a
href="/wiki/index.php?title=Category:Advanced_molecular-dynamics_sampling&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-dorner:PRL:2018_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.121.195701"
    class="external text" rel="nofollow">F. Dorner, Z. Sukurma, C. Dellago,
    and G. Kresse, Phys. Rev. Lett. <strong>121</strong>, 195701 (2018).</a>
2.  [↑](#cite_ref-kirkwood:jcp:1935_2-0)
    <a href="https://doi.org/10.1063/1.1749657" class="external text"
    rel="nofollow">J. Kirkwood, <em>Statistical Mechanics of Fluid
    Mixtures</em>, J. Chem. Phys. <strong>3</strong>, 300–313 (1935).</a>
3.  ↑
    <sup>[a](#cite_ref-ryckaertt:jcp:1977_3-0)</sup>
    <sup>[b](#cite_ref-ryckaertt:jcp:1977_3-1)</sup>
    <sup>[c](#cite_ref-ryckaertt:jcp:1977_3-2)</sup>
    <a href="http://dx.doi.org/10.1016/0021-9991(77)90098-5"
    class="external text" rel="nofollow">J. P. Ryckaert, G. Ciccotti, and H.
    J. C. Berendsen, J. Comp. Phys. <strong>23</strong>, 327 (1977).</a>
4.  [↑](#cite_ref-frenkel:ap-book:2002_4-0)
    <a href="http://doi.org/10.1016/0021-9991(77)90121-8"
    class="external text" rel="nofollow">D. Frenkel and B. Smit,
    <em>Understanding molecular simulations: from algorithms to
    applications</em>, Academic Press: San Diego, 2002.</a>
5.  [↑](#cite_ref-laio:pnas:02_5-0)
    <a href="https://doi.org/10.1073/pnas.202427399" class="external text"
    rel="nofollow">R. A. Laio and M. Parrinello, Proc. Natl. Acad, Sci. USA
    <strong>99</strong>, 12562 (2002).</a>
6.  [↑](#cite_ref-iannuzzi:prl:03_6-0)
    <a href="https://doi.org/10.1103/PhysRevLett.90.238302"
    class="external text" rel="nofollow">M. Iannuzzi, A. Laio, and M.
    Parrinello, Phys. Rev. Lett. <strong>90</strong>, 238302 (2003).</a>
7.  [↑](#cite_ref-carter:kapral:1989_7-0)
    <a href="https://doi.org/10.1016/S0009-2614(89)87314-2"
    class="external text" rel="nofollow">E. Carter, G. Ciccotti, J. Hynes,
    R. Kapral, Chem. Phys. Lett., <strong>156</strong>, 472 (1989).</a>
8.  [↑](#cite_ref-woo:ziegler:1997_8-0)
    <a href="https://doi.org/10.1021/jp9717296" class="external text"
    rel="nofollow">T. Woo, P. Margl, P. Blöchl, T. Ziegler. J. Phys. Chem.,
    <strong>101</strong>, 40 (1997)</a>
9.  [↑](#cite_ref-pedersen:prb:13_9-0)
    <a href="https://doi.org/10.1103/PhysRevB.88.094101"
    class="external text" rel="nofollow">U. R. Pedersen, F. Hummel, G.
    Kresse, G. Kahl, and C. Dellago, Phys. Rev. B <strong>88</strong>,
    094101 (2013).</a>
10. [↑](#cite_ref-tuckerman:book:2023_10-0)
    <a href="https://doi.org/10.1093/oso/9780198825562.001.0001"
    class="external text" rel="nofollow">M. Tuckerman, <em>Statistical
    Mechanics: Theory and Molecular Simulation (2nd edn)</em>, Oxford
    University Press (2023).</a>
11. [↑](#cite_ref-frenkel:smit:2023_11-0)
    <a href="https://doi.org/10.1016/B978-0-12-267351-1.X5000-7"
    class="external text" rel="nofollow">D. Frenkel, B. Smit,
    <em>Understanding Molecular Simulation - From Algorithms to Applications
    (2nd edn)</em>, Elsevier Science (2023).</a>



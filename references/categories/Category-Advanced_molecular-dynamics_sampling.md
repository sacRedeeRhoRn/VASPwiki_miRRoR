<!-- Source: https://vasp.at/wiki/index.php/Category:Advanced_molecular-dynamics_sampling | revid: 37176 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Advanced molecular-dynamics sampling
In a
[molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
(MD) calculation, we are often interested in rare events or specific
transitions. **Advanced molecular-dynamics sampling** helps to capture
these during an MD run within a feasible simulation time. There are
several different available methods:

- [Thermodynamic integration](#Thermodynamic_integration)
- [Constrained molecular dynamics](#Constrained_molecular_dynamics)
- [Biased molecular dynamics](#Biased_molecular_dynamics)
- [Metadynamics](#Metadynamics)
- [Blue moon ensemble](#Blue_moon_ensemble)
- [Slow-growth approach](#Slow-growth_approach)
- [Interface pinning](#Interface_pinning)

## Contents

- [1 Thermodynamic integration](#Thermodynamic_integration)
- [2 Constrained molecular dynamics](#Constrained_molecular_dynamics)
- [3 Biased molecular dynamics](#Biased_molecular_dynamics)
- [4 Metadynamics](#Metadynamics)
- [5 Blue moon ensemble](#Blue_moon_ensemble)
- [6 Slow-growth approach](#Slow-growth_approach)
- [7 Interface pinning](#Interface_pinning)
- [8 Additional resources](#Additional_resources)
  - [8.1 Books](#Books)
  - [8.2 Tutorials](#Tutorials)
  - [8.3 Lectures](#Lectures)
- [9 References](#References)

## Thermodynamic integration
[![](https://vasp.at/wiki/images/thumb/0/0b/Thermodynamic_integration.png/250px-Thermodynamic_integration.png)](https://vasp.at/wiki/File:Thermodynamic_integration.png)

Thermodynamic integration allows integration from a non-interacting
system (λ = 0) to an interacting system (λ = 1). E.g., between a
harmonic and an anharmonic system.

In the [thermodynamic
integration](../theory/Thermodynamic_integration.md)
method,^([\[1\]](#cite_note-dorner:PRL:2018-1)[\[2\]](#cite_note-kirkwood:jcp:1935-2))
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

## Constrained molecular dynamics
[![](https://vasp.at/wiki/images/thumb/b/b8/Constrained_MD.png/250px-Constrained_MD.png)](https://vasp.at/wiki/File:Constrained_MD.png)

Selected geometric parameters in this hydrogen cyanide isomerization to
hydrogen isocyanide reaction are constrained to model the transition
state. R₁ is the C-H bond, R₂ is the C-N bond, and R₃ is the N-H bond.

In [constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)
selected geometric parameters are constrained during the calculations
using the [ICONST](../input-files/ICONST.md) file. This is achieved by
extending the Lagrangian with a term incorporating the desired
constraints ([SHAKE
algorithm](../theory/Constrained_molecular_dynamics.md)^([\[3\]](#cite_note-ryckaertt:jcp:1977-3)))
directly. This method can be used on its own to support molecular
dynamics calculations but some of the methods on this page also
incorporate constraints via the same methodology.

- [Constrained molecular
  dynamics](../theory/Constrained_molecular_dynamics.md).
- [Constrained molecular dynamics
  calculations](../tutorials/Constrained_molecular_dynamics_calculations.md).

## Biased molecular dynamics
[![](https://vasp.at/wiki/images/thumb/9/92/Umbrella_sampling.png/250px-Umbrella_sampling.png)](https://vasp.at/wiki/File:Umbrella_sampling.png)

In biased MD, a biased potential can be used to pin the system to given
configuration (i.e., uncommon configurations), e.g., in umbrella
sampling.

[Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md)
refers to methods introducing a biased potential
^([\[4\]](#cite_note-frenkel:ap-book:2002-4)). In one of this method's
most popular representatives, the umbrella sampling or umbrella
integration, the biased potential is used to pin the system to given
configurations. This way the sampling of a system is greatly enhanced
and thermodynamic methods with proper statistics become accessible.
Although some of the methods on this page also use biased potentials
they have differences in the usage of the potential and hence belong in
their categories.

[Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md)
are often used to calculate free energies or free energy differences.

- [Biased molecular
  dynamics](../theory/Biased_molecular_dynamics.md).
- [Biased molecular dynamics
  calculations](../tutorials/Biased_molecular_dynamics_calculations.md).

## Metadynamics
[![](https://vasp.at/wiki/images/thumb/7/78/Metadynamics.png/250px-Metadynamics.png)](https://vasp.at/wiki/File:Metadynamics.png)

In metadynamics, a biased potential (coloured lines) is applied along
selected collective variables (x), cf. potential V, to gradually fill
free-energy minima and allows the system to cross barriers and explore
the potential energy surface, including other minima.

In
[metadynamics](../theory/Metadynamics.md),^([\[5\]](#cite_note-laio:pnas:02-5)[\[6\]](#cite_note-iannuzzi:prl:03-6))
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

## Blue moon ensemble
[![](https://vasp.at/wiki/images/thumb/f/f1/Blue_moon.png/250px-Blue_moon.png)](https://vasp.at/wiki/File:Blue_moon.png)

In the Blue moon ensemble method, the free energy profile along a chosen
reaction coordiante (x) can be calculated by calculating the unbiased
free-energy derivative.

The [blue moon ensemble](../theory/Blue_moon_ensemble.md)
method^([\[7\]](#cite_note-carter:kapral:1989-7)) is designed to
calculate the free energy profile along the path of selected reaction
coordinates. It also employs constraining of the atoms during molecular
dynamics ([SHAKE
algorithm](../theory/Constrained_molecular_dynamics.md)^([\[3\]](#cite_note-ryckaertt:jcp:1977-3))).
The term "[blue moon](../incar-tags/LBLUEOUT.md)" refers to rare events
such as the "moon turning blue".

The method is often used to calculate free energy differences for
systems where the profile is characterized by a few barriers that are
high enough that they would not be crossed within regular thermostatted
molecular dynamics.

- [Blue moon ensemble](../theory/Blue_moon_ensemble.md).
- [Blue moon ensemble
  calculations](../tutorials/Blue_moon_ensemble_calculations.md).

## Slow-growth approach
[![](https://vasp.at/wiki/images/thumb/0/0a/Slow_growth_md.png/250px-Slow_growth_md.png)](https://vasp.at/wiki/File:Slow_growth_md.png)

In the slow-growth approach, a reaction pathway can be followed linearly
on a reaction coordinate (x) from the reactant state (λ = 0) to the
target state (λ = 1).

In the [slow-growth
approach](../theory/Slow-growth_approach.md),^([\[8\]](#cite_note-woo:ziegler:1997-8))
the free energy profile is scanned along a reaction coordinate. The
scanning is done by linearly changing the reaction coordinate from that
of the reactant state to that of a transition or product state via
[constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)
([SHAKE
algorithm](../theory/Constrained_molecular_dynamics.md)^([\[3\]](#cite_note-ryckaertt:jcp:1977-3))).

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

## Interface pinning
[![](https://vasp.at/wiki/images/thumb/0/0a/Water_ice_interface.png/250px-Water_ice_interface.png)](https://vasp.at/wiki/File:Water_ice_interface.png)

Interface pinning is used to model two different phases on the same
system in the same cell, e.g., the water-ice interface.

In [interface
pinning](../theory/Interface_pinning.md),^([\[9\]](#cite_note-pedersen:prb:13-9))
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

## Additional resources
### Books
- *Statistical Mechanics: Theory and Molecular Simulation* by M.
  Tuckerman ^([\[10\]](#cite_note-tuckerman:book:2023-10)).
- *Understanding Molecular Simulation - From Algorithms to Applications*
  by D. Frenkel and B. Smit
  ^([\[11\]](#cite_note-frenkel:smit:2023-11)).

### Tutorials
- Tutorial for chloromethane-chloride inversion [using the slow-growth
  approach, blue-moon ensemble, and constrained
  MD](https://www.vasp.at/tutorials/latest/md/part3/#MD-e08).
- Tutorial for a chemical reaction in a zeolite [using the slow-growth
  approach, blue-moon ensemble, and constrained
  MD](https://www.vasp.at/tutorials/latest/transition_states/part3).

### Lectures
- Lecture on [advanced methods of MD](https://youtu.be/HVeamQOmM-s).
- Lecture on [advanced methods of MD applied to a chemical
  reaction](https://youtu.be/Rk0S-yvxFUo).

## References
1.  [↑](#cite_ref-dorner:PRL:2018_1-0) [F. Dorner, Z. Sukurma, C.
    Dellago, and G. Kresse, Phys. Rev. Lett. **121**, 195701
    (2018).](https://doi.org/10.1103/PhysRevLett.121.195701)
2.  [↑](#cite_ref-kirkwood:jcp:1935_2-0) [J. Kirkwood, *Statistical
    Mechanics of Fluid Mixtures*, J. Chem. Phys. **3**, 300–313
    (1935).](https://doi.org/10.1063/1.1749657)
3.  ↑ ^([a](#cite_ref-ryckaertt:jcp:1977_3-0))
    ^([b](#cite_ref-ryckaertt:jcp:1977_3-1))
    ^([c](#cite_ref-ryckaertt:jcp:1977_3-2)) [J. P. Ryckaert, G.
    Ciccotti, and H. J. C. Berendsen, J. Comp. Phys. **23**, 327
    (1977).](http://dx.doi.org/10.1016/0021-9991(77)90098-5)
4.  [↑](#cite_ref-frenkel:ap-book:2002_4-0) [D. Frenkel and B. Smit,
    *Understanding molecular simulations: from algorithms to
    applications*, Academic Press: San Diego,
    2002.](http://doi.org/10.1016/0021-9991(77)90121-8)
5.  [↑](#cite_ref-laio:pnas:02_5-0) [R. A. Laio and M. Parrinello, Proc.
    Natl. Acad, Sci. USA **99**, 12562
    (2002).](https://doi.org/10.1073/pnas.202427399)
6.  [↑](#cite_ref-iannuzzi:prl:03_6-0) [M. Iannuzzi, A. Laio, and M.
    Parrinello, Phys. Rev. Lett. **90**, 238302
    (2003).](https://doi.org/10.1103/PhysRevLett.90.238302)
7.  [↑](#cite_ref-carter:kapral:1989_7-0) [E. Carter, G. Ciccotti, J.
    Hynes, R. Kapral, Chem. Phys. Lett., **156**, 472
    (1989).](https://doi.org/10.1016/S0009-2614(89)87314-2)
8.  [↑](#cite_ref-woo:ziegler:1997_8-0) [T. Woo, P. Margl, P. Blöchl, T.
    Ziegler. J. Phys. Chem., **101**, 40
    (1997)](https://doi.org/10.1021/jp9717296)
9.  [↑](#cite_ref-pedersen:prb:13_9-0) [U. R. Pedersen, F. Hummel, G.
    Kresse, G. Kahl, and C. Dellago, Phys. Rev. B **88**, 094101
    (2013).](https://doi.org/10.1103/PhysRevB.88.094101)
10. [↑](#cite_ref-tuckerman:book:2023_10-0) [M. Tuckerman, *Statistical
    Mechanics: Theory and Molecular Simulation (2nd edn)*, Oxford
    University Press
    (2023).](https://doi.org/10.1093/oso/9780198825562.001.0001)
11. [↑](#cite_ref-frenkel:smit:2023_11-0) [D. Frenkel, B. Smit,
    *Understanding Molecular Simulation - From Algorithms to
    Applications (2nd edn)*, Elsevier Science
    (2023).](https://doi.org/10.1016/B978-0-12-267351-1.X5000-7)

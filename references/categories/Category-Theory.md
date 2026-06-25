<!-- Source: https://vasp.at/wiki/index.php/Category:Theory | revid: 35500 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Theory


The **Vienna ab-initio simulation package** (VASP) is a computer program
for atomic scale materials modeling from first principles. A so-called
ab-initio simulation generally entails

- choosing the elements and a structure of the material,
- <a href="/wiki/Electronic_minimization" class="mw-redirect"
  title="Electronic minimization">treating the electrons fully quantum
  mechanically</a> and
- optionally updating the ionic positions

<!-- -->

- to <a href="/wiki/Ionic_minimization" class="mw-redirect"
  title="Ionic minimization">minimize the forces</a> and obtain a stable
  structure, or
- by means of Newton's equation of motion to perform
  <a href="/wiki/MD" class="mw-redirect" title="MD">molecular dynamics
  simulations</a>.

VASP computes an approximate solution to the many-body Schrödinger
equation to obtain the
<a href="/wiki/Electronic_ground-state_properties" class="mw-redirect"
title="Electronic ground-state properties">electronic ground state</a>.
This can either be done within density-functional theory (DFT) by
solving the Kohn-Sham (KS) equations, or within the Hartree-Fock (HF)
approximation by solving the Roothaan equations.
<a href="/wiki/Hybrid_functionals" class="mw-redirect"
title="Hybrid functionals">Hybrid functionals</a> that mix the
Hartree-Fock approach with density-functional theory are also
implemented. Furthermore, Green’s functions methods based on
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>
are available in VASP. For instance, the [GW
method](../theory/Category-GW.md), random-phase approximation,
2nd-order Møller-Plesset, [Bethe-Salpeter
equations](../theory/Category-Bethe-Salpeter_equations.md),
and more to grant access to
<a href="/wiki/Optical_properties" class="mw-redirect"
title="Optical properties">optical properties</a>.

In VASP, central quantities, like the one-electron orbitals, the
electronic charge density, and the local potential are expressed in
plane-wave basis using the [projector-augmented-wave (PAW)
method](../methods/Projector-augmented-wave_formalism.md).
This entails using PAW
<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a> to efficiently treat the
relevant valence electrons while appropriately capturing the nodal
features near the nuclei. To [determine the
orbitals](Category-Electronic_minimization.md)
for the electronic ground state, VASP makes use of efficient iterative
matrix [diagonalization techniques](../incar-tags/ALGO.md). These are
coupled with highly efficient Broyden and Pulay
[density-mixing](Category-Density_mixing.md)
schemes to speed up the self-consistency cycle.

The ionic degrees of freedom can be updated by various algorithms
([IBRION](../incar-tags/IBRION.md)) based on
<a href="/wiki/Forces" class="mw-redirect" title="Forces">forces</a>
that are either obtained directly from the electronic state or from
ab-intio quality force fields that were trained by machine learning.
VASP is particularly strong in describing crystal structures due to the
periodic boundary conditions it exploits. Naturally, these systems
feature quantized vibrations in the form of
<a href="/wiki/Phonons" class="mw-redirect" title="Phonons">phonons</a>
whose influence on the electronic ground state is taken into account by
including <a href="/wiki/Electron-phonon_coupling" class="mw-redirect"
title="Electron-phonon coupling">electron-phonon coupling</a>.

In this category, we collect theory pages from all the different areas
VASP offers functionalities. These can also be reached from the
corresponding category. For instance, the article on the
[Blocked-Davidson
algorithm](../theory/Blocked-Davidson_algorithm.md)
is also linked from the
<a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> page.

For an <a href="https://youtu.be/Fv3F4LHGPuc" class="external text"
rel="nofollow">introduction to ab-initio simulations in VASP</a>, check
out the lecture available on our YouTube channel.



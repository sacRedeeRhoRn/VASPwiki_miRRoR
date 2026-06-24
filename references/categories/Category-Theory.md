<!-- Source: https://vasp.at/wiki/index.php/Category:Theory | revid: 35500 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Theory
The **Vienna ab-initio simulation package** (VASP) is a computer program
for atomic scale materials modeling from first principles. A so-called
ab-initio simulation generally entails

- choosing the elements and a structure of the material,
- [treating the electrons fully quantum
  mechanically](../redirects/Electronic_minimization.md)
  and
- optionally updating the ionic positions

&nbsp;

- to [minimize the
  forces](../redirects/Ionic_minimization.md) and obtain a
  stable structure, or
- by means of Newton's equation of motion to perform [molecular dynamics
  simulations](../redirects/MD.md).

VASP computes an approximate solution to the many-body Schrödinger
equation to obtain the [electronic ground
state](../redirects/Electronic_ground-state_properties.md).
This can either be done within density-functional theory (DFT) by
solving the Kohn-Sham (KS) equations, or within the Hartree-Fock (HF)
approximation by solving the Roothaan equations. [Hybrid
functionals](../redirects/Hybrid_functionals.md) that mix the
Hartree-Fock approach with density-functional theory are also
implemented. Furthermore, Green’s functions methods based on [many-body
perturbation
theory](../redirects/Many-body_perturbation_theory.md)
are available in VASP. For instance, the [GW
method](../theory/Category-GW.md), random-phase approximation,
2nd-order Møller-Plesset, [Bethe-Salpeter
equations](../theory/Category-Bethe-Salpeter_equations.md),
and more to grant access to [optical
properties](../redirects/Optical_properties.md).

In VASP, central quantities, like the one-electron orbitals, the
electronic charge density, and the local potential are expressed in
plane-wave basis using the [projector-augmented-wave (PAW)
method](../methods/Projector-augmented-wave_formalism.md).
This entails using PAW
[pseudopotentials](../redirects/Pseudopotentials.md) to
efficiently treat the relevant valence electrons while appropriately
capturing the nodal features near the nuclei. To [determine the
orbitals](Category-Electronic_minimization.md)
for the electronic ground state, VASP makes use of efficient iterative
matrix [diagonalization techniques](../incar-tags/ALGO.md). These are
coupled with highly efficient Broyden and Pulay
[density-mixing](Category-Density_mixing.md)
schemes to speed up the self-consistency cycle.

The ionic degrees of freedom can be updated by various algorithms
([IBRION](../incar-tags/IBRION.md)) based on
[forces](../redirects/Forces.md) that are either obtained directly from
the electronic state or from ab-intio quality force fields that were
trained by machine learning. VASP is particularly strong in describing
crystal structures due to the periodic boundary conditions it exploits.
Naturally, these systems feature quantized vibrations in the form of
[phonons](../redirects/Phonons.md) whose influence on the electronic
ground state is taken into account by including [electron-phonon
coupling](../redirects/Electron-phonon_coupling.md).

In this category, we collect theory pages from all the different areas
VASP offers functionalities. These can also be reached from the
corresponding category. For instance, the article on the
[Blocked-Davidson
algorithm](../theory/Blocked-Davidson_algorithm.md)
is also linked from the [electronic
minimization](../redirects/Electronic_minimization.md)
page.

For an [introduction to ab-initio simulations in
VASP](https://youtu.be/Fv3F4LHGPuc), check out the lecture available on
our YouTube channel.

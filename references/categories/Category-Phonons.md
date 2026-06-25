<!-- Source: https://vasp.at/wiki/index.php/Category:Phonons | revid: 35514 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Phonons


Phonons are the collective excitation of nuclei in an extended periodic
system.

Here we will present a short summary with the complete derivation
presented on the [theory page](../theory/Phonons-_Theory.md).
There is also a [article relating several basic
concepts](../theory/Static_linear_response-_theory.md)
like the forces, stresses, Taylor expansion, Born effective charges,
etc. Let us start by making the Taylor expansion of the total energy
$E$ in terms of the ionic displacement
$u_{I\alpha} = R_{I\alpha} - R^0_{I\alpha}$ around
the equilibrium positions of the nuclei $R^0_{I\alpha}$

$E(\\\mathbf{R}\\)= E(\\\mathbf{R}^0\\)+ \sum_{I\alpha} -F_{I\alpha}
(\\\mathbf{R}^0\\) u_{I\alpha}+ \sum_{I\alpha J\beta} \Phi_{I\alpha
J\beta} (\\\mathbf{R}^0\\) u_{I\alpha} u_{J\beta} +
\mathcal{O}(\mathbf{R}^3)$

with $F_{I\alpha}$
being the atomic forces and $\Phi_{I\alpha J\beta}$ the interatomic force constants (IFC).

If the structure is in equilibrium (i.e. the forces are zero) then we
can find the normal modes of vibration of the system by solving the
eigenvalue problem

$\sum_{J\beta} \frac{1}{\sqrt{M_I M_J}} \Phi_{I\alpha J\beta}
e^{i\mathbf{q} \cdot (\mathbf{R}_J-\mathbf{R}_I)} (\mathbf{q})
\varepsilon_{J\beta,\nu}(\mathbf{q}) = \omega_\nu(\mathbf{q})^2
\varepsilon_{I\alpha,\nu}(\mathbf{q})$

where the normal modes $\varepsilon_{I\alpha,\nu}(\mathbf{q})$ and
corresponding frequencies $\omega_\nu(\mathbf{q})^2$ are the phonons in the adiabatic harmonic
approximation.

The computation of the IFCs using the supercell approach can be done
using
[finite-differences](../tutorials/Phonons_from_finite_differences.md)
or [density functional perturbation
theory](../tutorials/Phonons_from_density-functional-perturbation_theory.md).

It is possible to [obtain the phonon dispersion at different **q**
points](../tutorials/Computing_the_phonon_dispersion_and_DOS.md)
by computing the IFCs on a sufficiently large supercell and Fourier
interpolating the dynamical matrices in the unit cell.


## Contents


- [1
  Electron-phonon
  interaction](#electron-phonon-interaction)
- [2 Additional
  resources](#additional-resources)
  - [2.1 How
    to](#how-to)
  - [2.2
    Tutorials](#tutorials)
  - [2.3
    Lectures](#lectures)


## Electron-phonon interaction\[<a
href="/wiki/index.php?title=Category:Phonons&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Electron-phonon interaction">edit</a> \| (./index.php.md)\]

The movement of the nuclei leads to changes in the electronic degrees of
freedom with this coupling between the electronic and phononic systems
commonly referred to as [electron-phonon
interactions](../theory/Electron-phonon_interactions_theory.md).
These interactions can be captured by [perturbative
methods](Category-Electron-phonon_interactions.md)
or [Monte-Carlo
sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md)
to populate a supercell with phonons and monitor how the electronic
band-structure changes.

## Additional resources\[<a
href="/wiki/index.php?title=Category:Phonons&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### How to\[<a
href="/wiki/index.php?title=Category:Phonons&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

- [Phonons from finite
  differences](../tutorials/Phonons_from_finite_differences.md)
- [Phonons from density-functional-perturbation
  theory](../tutorials/Phonons_from_density-functional-perturbation_theory.md)
- [Computing the phonon dispersion and
  DOS](../tutorials/Computing_the_phonon_dispersion_and_DOS.md)
- [Electron-phonon interactions from Monte-Carlo
  sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md)

### Tutorials\[<a
href="/wiki/index.php?title=Category:Phonons&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/phonon/part1"
  class="external text" rel="nofollow">lattice parameter and phonon
  dispersion</a> in graphene.
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/phonon/part2"
  class="external text" rel="nofollow">lattice parameter, phonon
  dispersion and DOS, and long-range dipole-dipole interaction
  calculations</a> for MgO.

### Lectures\[<a
href="/wiki/index.php?title=Category:Phonons&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on
  <a href="https://youtu.be/VhYEdKOlIws" class="external text"
  rel="nofollow">phonons</a>.



<!-- Source: https://vasp.at/wiki/index.php/Category:Electronic_minimization | revid: 35361 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Electronic minimization


By **electronic minimization** we denote the process of determining the
electronic ground state. This is an integral part of the vast majority
of VASP calculations. The **electronic minimization** in VASP is highly
optimized, and different settings warrant the use of different
algorithms or procedures. For instance, very elongated cells are prone
to [charge sloshing](../theory/Charge_sloshing.md), which
hampers convergence and can be avoided by clever settings in the
[density
mixer](Category-Density_mixing.md).To learn
the basics of electronic minimization in practice, visit the following
how-to pages:

- [Setting up an electronic
  minimization](../tutorials/Setting_up_an_electronic_minimization.md)
- [Troubleshooting electronic
  convergence](../tutorials/Troubleshooting_electronic_convergence.md)
- <a href="https://youtu.be/WlYykovzyiA" class="external text"
  rel="nofollow">Lecture on electronic optimization</a>

## Theoretical background\[<a
href="/wiki/index.php?title=Category:Electronic_minimization&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theoretical background">edit</a> \| (./index.php.md)\]

Within the context of Hohenberg-Kohn-Sham density functional theory, the
ground state is that state of the system that minimizes the Kohn-Sham
free energy:

 

$F
= \sum_n f_n \epsilon_n -E_{\rm H}\left\[ \rho \right\] + E_{\rm xc}
\left\[ \rho \right\] -\int V_{\rm xc}({\bf r})\rho({\bf r})d{\bf r} -
\sum_n \sigma S \left( \frac{\epsilon_n - \mu}{\sigma} \right)$

where the electronic density is given by:

$\rho({\bf r})= \sum_n f_{n} |\psi_{n}({\bf r})|^2$

and the Kohn-Sham orbitals and eigenenergies,
$\\\psi_n, \epsilon_n \\$ are solutions to the Kohn-Sham
equations:

$H
\left\[ \rho \right\] | \psi_n \rangle = \epsilon_n S | \psi_n \rangle$

under the constraint that the orbitals are *S*-orthonormal:

$\langle \psi_m | S | \psi_n \rangle = \delta_{mn}$

The various algorithms for **electronic minimization** VASP offers can
be roughly divided into two categories:

- Iterative matrix diagonalization + density mixing, also known as the
  [self-consistency
  cycle](../theory/Self-consistency_cycle.md) (SCC).
- [Direct optimization of the
  orbitals](../theory/Direct_optimization_of_the_orbitals.md).

Selecting a particular method of **electronic minimization** is done by
means of the [ALGO](../incar-tags/ALGO.md) (or [IALGO](../incar-tags/IALGO.md))
tag.

## Self-consistency cycle\[<a
href="/wiki/index.php?title=Category:Electronic_minimization&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Self-consistency cycle">edit</a> \| (./index.php.md)\]

1.  The SCC starts with an initial guess for the electronic density of
    the system. In particular, VASP uses the approximation of
    overlapping atomic charge densities. This density defines the
    initial Hamiltonian.
2.  By means of iterative matrix-diagonalization techniques, one obtains
    the [NBANDS](../incar-tags/NBANDS.md) lowest lying eigenstates of the
    Hamiltonian. The iterative matrix-diagonalization algorithms
    implemented in VASP are the [blocked-Davidson
    algorithm](../theory/Blocked-Davidson_algorithm.md)
    and the [residual-minimization method with direct inversion in the
    iterative subspace (RMM-DIIS)](../theory/RMM-DIIS.md). By
    default, VASP uses the blocked-Davidson algorithm
    ([`ALGO`](../incar-tags/ALGO.md)` = Normal`).
3.  After the eigenstates and eigenvalues have been determined with
    sufficient accuracy, they are used to compute the total energy of
    the system and to construct a new electronic density.
4.  In principle, this new density could be taken to define a new
    Hamiltonian. However, in order to obtain a stable algorithm, this
    new density is not used as is but is mixed with the old density. By
    default, VASP uses a Broyden mixer. The resulting density then
    defines the new Hamiltonian for the next round of iterative matrix
    diagonalization (step 2).

Steps 2–4 are repeated until the change in the total energy from one
cycle to the next drops below a specific threshold set by
[EDIFF](../incar-tags/EDIFF.md).

Note that when starting from scratch
([`ISTART`](../incar-tags/ISTART.md)` = 0`), the SCC procedure of VASP
always begins with several ([NELMDL](../incar-tags/NELMDL.md)) cycles
where the density is kept fixed at the initial approximation, i.e.,
overlapping atomic charge densities. This ensures that the orbitals that
are initialized with random numbers have converged to something sensible
before they are used to construct a new charge density.

For a more detailed description of the SCC, see [self-consistency
cycle](../theory/Self-consistency_cycle.md).

## Direct optimization\[<a
href="/wiki/index.php?title=Category:Electronic_minimization&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Direct optimization">edit</a> \| (./index.php.md)\]

Similar to the SCC procedure described above, when starting from scratch
([`ISTART`](../incar-tags/ISTART.md)` = 0`), the direct optimization
procedures in VASP always begin with several
([NELMDL](../incar-tags/NELMDL.md)) self-consistency cycles where the
density is kept fixed at the initial approximation (overlapping atomic
charge densities). This ensures that the orbitals that are initialized
with random numbers have converged to a reasonable starting point for
the subsequent direct optimization.

The direct optimization of the orbitals uses the gradient of the total
energy with respect to the orbitals to move towards the ground state of
the system: the orbitals are changed such that the total energy is
lowered, using, e.g., the conjugate-gradient approximation, or damped
molecular dynamics.

After every change of the orbitals, the total energy and electronic
density are recomputed. By default, the electronic density is
constructed directly from the orbitals at each step along the way,
without any density mixing. Optionally, though, density mixing may be
used to stabilize these optimization procedures when [charge
sloshing](../theory/Charge_sloshing.md) occurs.

As for the SCC described above, the direct optimization of the orbitals
stops when the change of the total energy drops below
[EDIFF](../incar-tags/EDIFF.md).

For more details on the direct optimization algorithms, see [direct
optimization of the
orbitals](../theory/Direct_optimization_of_the_orbitals.md).



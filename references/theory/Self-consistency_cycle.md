<!-- Source: https://vasp.at/wiki/index.php/Self-consistency_cycle | revid: 22835 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Self-consistency cycle


<figure typeof="mw:File/Thumb">
<a href="/wiki/File:SCC.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/a/a0/SCC.png/350px-SCC.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/a/a0/SCC.png/525px-SCC.png 1.5x, /wiki/images/thumb/a/a0/SCC.png/700px-SCC.png 2x"
width="350" height="573" /></a>
<figcaption>Fig. 1: the self-consistency cycle</figcaption>
</figure>

The term **self-consistency cycle** (SCC) denotes a category of
algorithms that determine the electronic ground state by a combination
of iterative matrix diagonalization and
<a href="/wiki/Density_mixing" class="mw-redirect"
title="Density mixing">density mixing</a>.

Figure 1. shows a procedural flowchart of the self-consistency cycle:

1.  When starting from scratch, the SCC starts with an initial guess for
    the electronic density of the system under consideration: VASP uses
    the approximation of overlapping atomic charge densities. The
    orbitals are initialized with random numbers. Alternatively, the SCC
    may (re-)start from the orbitals and/or electronic density obtained
    in a previous calculation.
2.  The density defines the Hamiltonian.
3.  By means of iterative matrix diagonalization techniques, one obtains
    the [NBANDS](../incar-tags/NBANDS.md) lowest lying eigenstates of the
    Hamiltonian. The iterative matrix diagonalization algorithms
    implemented in VASP are the [blocked-Davidson
    algorithm](Blocked-Davidson_algorithm.md)
    and the [residual-minimization method with direct inversion in the
    iterative subspace (RMM-DIIS)](RMM-DIIS.md). Per
    default VASP uses the [blocked-Davidson
    algorithm](Blocked-Davidson_algorithm.md)
    ([ALGO](../incar-tags/ALGO.md) = Normal). This step is often referred to
    as *iterative optimization/refinement of the orbitals*.
4.  After the eigenstates and eigenvalues of the Hamiltonian, i.e.,
    orbitals and one-electron energies, have been determined with
    sufficient accuracy, the corresponding partial occupancies of the
    orbitals are calculated.
5.  From the one-electron energies and partial occupancies, the free
    energy of the system is computed.
6.  From the orbitals and partial occupancies, a new electronic density
    is constructed.
7.  In principle, the new density could be directly used to define a new
    Hamiltonian. In most cases, however, this does not lead to a stable
    algorithm (on account of, e.g., charge sloshing). Instead, the new
    density is not used directly but is mixed with the old density. By
    default VASP uses a Broyden mixer ([IMIX](../incar-tags/IMIX.md)). The
    resulting density then defines the new Hamiltonian for the next
    round of iterative matrix diagonalization.

Steps 2-7 are repeated until the change in the free energy from one
cycle to the next drops below a specific threshold
([EDIFF](../incar-tags/EDIFF.md)).

Note that when starting from scratch ([ISTART](../incar-tags/ISTART.md) =
0), the self-consistency cycle procedure of VASP always begins with
several ([NELMDL](../incar-tags/NELMDL.md)) cycles where the density is
kept fixed at the initial approximation (overlapping atomic charge
densities). This ensures that the wavefunctions that are initialized
with random numbers have converged to something sensible before they are
used to construct a new charge density.

Especially in case of the [RMM-DIIS](RMM-DIIS.md) the
initial set of orbitals plays a critical role. Therefore, either the
number of non-selfconsistent cycles is chosen to be large
([NELMDL](../incar-tags/NELMDL.md) = 12, for [ALGO](../incar-tags/ALGO.md) =
VeryFast), or the non-selfconsistent cycles are done with the
[blocked-Davidson
algorithm](Blocked-Davidson_algorithm.md)
before switching over to the use of the
[RMM-DIIS](RMM-DIIS.md) ([ALGO](../incar-tags/ALGO.md) =
Fast).

Furthermore, note that per default ([LDIAG](../incar-tags/LDIAG.md)=.TRUE.)
the iterative refinement of the orbitals is preceded
([RMM-DIIS](RMM-DIIS.md)) or followed
([blocked-Davidson](Blocked-Davidson_algorithm.md))
by a diagonalization of the subspace spanned by the current orbitals. In
case of the [RMM-DIIS](RMM-DIIS.md), the optimization step
is additionally followed by an orthogonalization of the refined
orbitals.

With respect to the aforementioned it should be emphasized that, in
principle, the [RMM-DIIS](RMM-DIIS.md) method should also
converge without any explicit subspace diagonalization and/or
re-orthonormalization. However, in our experience their inclusion speeds
up the convergence of the
self-consistency cycle so
substantially that it shortens the time-to-solution of most
calculations, even though these operations scale as
$O(N^3)$.

For (a lot) more details on the self-consistency cycle and associated
algorithms in VASP, we recommend the seminal papers by Kresse and
Furthmüller.<sup>[\[1\]](#cite_note-kresse:cms:1996-1)[\[2\]](#cite_note-kresse:prb:96-2)</sup>

## References\[<a
href="/wiki/index.php?title=Self-consistency_cycle&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-kresse:cms:1996_1-0)
    <a href="https://doi.org/10.1016/0927-0256(96)00008-0"
    class="external text" rel="nofollow">G. Kresse and J. Furthmüller, Comp.
    Mater. Sci. <strong>6</strong>, 15 (1996)</a>
2.  [↑](#cite_ref-kresse:prb:96_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.54.11169"
    class="external text" rel="nofollow">G. Kresse and J. Furthmüller, Phys.
    Rev. B <strong>54</strong>, 11169 (1996).</a>


------------------------------------------------------------------------



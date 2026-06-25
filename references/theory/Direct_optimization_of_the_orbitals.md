<!-- Source: https://vasp.at/wiki/index.php/Direct_optimization_of_the_orbitals | revid: 25721 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Direct optimization of the orbitals


With "direct optimization of the orbitals" we denote a category of
electronic minimization algorithms that use the gradient of the free
energy with respect to the orbitals to move towards the ground state of
the system: the orbitals are changed such that the total energy is
lowered, using, *e.g.* the conjugate gradient approximation, or damped
molecular dynamics.

In direct optimization methods, the orthogonality constraints are
directly incorporated into the functional that is optimized, through
Lagrange multipliers. So in fact, instead of minimizing the
<a href="/wiki/Electronic_minimization#KohnShamFreeEnergy"
class="mw-redirect" title="Electronic minimization">Kohn-Sham free
energy functional</a> *F*, one minimizes the following Langrangian:

$\bar{F} = F - \sum_{mn} \gamma_{mn} \left( \langle \psi_m |S| \psi_n
\rangle - \delta_{mn} \right) - \mu \left( \sum_n f_n - N_{\rm el}
\right)$

The gradient of this Langrangian with respect to an orbital
$\psi_n$, is given by:

$|
g_n \rangle = f_n \Big(1-\sum^N_{m=1} \hat{S} \vert \psi_m \rangle
\langle \psi_m \vert\Big) \hat{H} \vert \psi_n \rangle + \sum^N_{m=1}
\frac{1}{2} {\bf H}_{nm} (f_n - f_m) \hat{S} \vert \psi_m \rangle$

where $\\ f_i | i=1,..,N \\$ are the partial occupancies, and

${\bf H}_{nm}=\langle \psi_m \vert \hat{H} \vert \psi_n \rangle$

is the Hamiltonian expressed within the subspace spanned by the current
orbitals $\\ \psi_i | i=1,..,N \\$.<sup>[\[1\]](#cite_note-kresse:cms:1996-1)</sup>

The structure of the gradient may be understood as follows: the first
part on the right-hand side describes the change of the free energy with
respect to changes in the orbitals that are outside (orthogonal) the
subspace spanned by the current set of orbitals, whereas the second part
describes the changes of the free energy due to a unitary transformation
between the orbitals within this subspace.

To derive a search direction, *i.e.*, actual change in the orbitals from
the gradient these aforementioned parts are treated separately. The
search direction related to the out-of-subspace part of the gradient is:

$\vert p_n \rangle = f_n K \Big(1-\sum^N_{m=1} \hat{S} \vert \psi_m
\rangle \langle \psi_m \vert\Big) \hat{H} \vert \psi_n \rangle$

where $K$ is a
[preconditioning](Preconditioning.md) function.

The search direction associated with the subspace rotational part of the
gradient may be constructed using Loewdin perturbation theory:

$U_{nm} = \delta_{nm} - \Delta \frac{H_{nm}}{H_{mm}-H_{nn}}$

where $\Delta$
denotes the
stepsize.<sup>[\[2\]](#cite_note-gillan:jpc:89-2)</sup>
Note that taking a step along this search direction amounts to a
rotation of the orbitals (*rotation* on account of
$U$ being unitary):

$\vert \psi_n \rangle = \sum^N_{m=1} U_{nm} \vert \psi_m \rangle$

Per default, however, VASP constructs a search direction for the
subspace rotational part of the gradient in the manner proposed by
Freysoldt *et
al.*<sup>[\[3\]](#cite_note-freysoldt:prb:2009-3)</sup>

Changes in the partial occupancies are computed in accordance with the
aforementioned work as well.

When the three contributions to the "search direction"
(*out-of-subspace*, *subspace rotational*, and *change in the partial
occupancies*) have been determined, they are used to update the orbitals
and partial occupancies, either by steepest descent, by means of the
conjugate-gradient approximation, or using a damped molecular dynamics
scheme.

After every change of the orbitals and partial occupancies, the total
energy and electronic density are recomputed. Per default, the
electronic density is constructed directly from the orbitals and partial
occupancies at each step along the way, without any density mixing.
Optionally, though, density mixing may be used to stabilise these
optimisation procedures when charge sloshing occurs.

The direct optimization of the orbitals stops when the change of the
total energy drops below [EDIFF](../incar-tags/EDIFF.md).

Note that, when starting from scratch ([ISTART](../incar-tags/ISTART.md) =
0), the direct optimization procedures in VASP always begin with several
([NELMDL](../incar-tags/NELMDL.md)) [self-consistency
cycles](Self-consistency_cycle.md) where the
density is kept fixed at the initial approximation (overlapping atomic
charge densities), using the blocked-Davidson algorithm to optimize the
orbitals. This ensures that the orbitals, that are initialised with
random numbers, have converged to reasonable starting point for the
subsequent direct optimization.

## References\[<a
href="/wiki/index.php?title=Direct_optimization_of_the_orbitals&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-kresse:cms:1996_1-0)
    <a href="https://doi.org/10.1016/0927-0256(96)00008-0"
    class="external text" rel="nofollow">G. Kresse and J. Furthmüller, Comp.
    Mater. Sci. <strong>6</strong>, 15 (1996)</a>
2.  [↑](#cite_ref-gillan:jpc:89_2-0)
    <a href="https://doi.org/10.1088/0953-8984/1/4/005"
    class="external text" rel="nofollow">M. J. Gillan, J. Phys.: Condens.
    Matter <strong>1</strong>, 689 (1989).</a>
3.  [↑](#cite_ref-freysoldt:prb:2009_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.79.241103"
    class="external text" rel="nofollow">C. Freysoldt, S. Beck, and J.
    Neugebauer, <em>Direct minimization technique for metals in density
    functional theory</em>, Phys. Rev. B <strong>79</strong>, 241103R
    (2009).</a>


------------------------------------------------------------------------



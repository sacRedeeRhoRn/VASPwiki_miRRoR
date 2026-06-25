<!-- Source: https://vasp.at/wiki/index.php/RMM-DIIS | revid: 22842 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# RMM-DIIS


The implementation of the Residual Minimization Method with Direct
Inversion in the Iterative Subspace (RMM-DIIS) in
VASP[^kresse:cms:1996-1][^kresse:prb:96-2]
is based on the original work of
Pulay:[^pulay:cpl:1980-3]

- The procedure starts with the evaluation of the preconditioned
  residual vector for some selected orbital $\psi^0_m$:

$K
\vert R^0_m \rangle = K \vert R(\psi^0_m) \rangle$

where $K$ is the
[preconditioning](Preconditioning.md) function, and
the residual is computed as:

$\vert R(\psi) \rangle = (H-\epsilon_{\rm app}) \vert \psi \rangle$

with

$\epsilon_{\rm app} = \frac{\langle \psi \vert H \vert \psi
\rangle}{\langle \psi \vert S \vert \psi \rangle}$

- Then a Jacobi-like trial step is taken in the direction of the vector:

$\vert \psi^1_m \rangle = \vert \psi^0_m \rangle + \lambda K \vert R^0_m
\rangle$

and a new residual vector is determined:

$\vert R^1_m \rangle = \vert R(\psi^1_m) \rangle$

- Next a linear combination of the initial orbital
  $\psi^0_m$ and the trial orbital
  $\psi^1_m$

$\vert \bar{\psi}^M \rangle = \sum^M_{i=0} \alpha_i \vert \psi^i_m
\rangle, \\\\ M=1$

is sought, such that the norm of the residual vector is minimized.
Assuming linearity in the residual vector:

$\vert \bar{R}^M \rangle = \vert R(\bar{\psi}^M) \rangle = \sum^M_{i=0}
\alpha_i \vert R^i_m \rangle$

this requires the minimization of:

$\frac{\sum_{ij} \alpha_i^\* \alpha_j \langle R^i_m \vert R^j_m
\rangle}{\sum_{ij}\alpha_i^\* \alpha_j \langle \psi^i_m \vert S \vert
\psi^j_m \rangle}$

with respect to ${\\\alpha_i | i=0,..,M\}$.

This step is usually called *direct inversion of the iterative subspace*
(DIIS).

- The next trial step ($M=2$)
  starts from $\bar{\psi}^1$, along the direction $K \bar{R}^1$. In each iteration $M$ is
  increased by 1, and a new trial orbital:

$\vert \psi^M_m \rangle = \vert \bar{\psi}^{M-1} \rangle + \lambda K
\vert \bar{R}^{M-1} \rangle$

and its corresponding residual vector $R(\psi^M_m)$
are added to the iterative subspace, that is subsequently inverted to
yield $\bar{\psi}^M$.

The algorithm keeps iterating until the norm of the residual
$\bar{R}^M$ has dropped below a certain threshold, or
the maximum number of iterations per orbital has been reached
([NRMM](../incar-tags/NRMM.md)).

- Replace $\psi^0_m$
  by $\bar{\psi}^M$ and move on to start work on the next orbital,
  *e.g.* $\psi^0_{m+1}$.

The size of the trial step $\lambda$ is a
critical value for the stability of the algorithm. We have found that a
reasonable choice for the trial step can be obtained from the
minimization of the Rayleigh quotient along the search direction in *the
first step*, this optimal $\lambda$ is
then used for a particular orbital until the algorithm moves on to the
next
orbital.[^kresse:cms:1996-1][^kresse:prb:96-2]

As mentioned before, the optimization of an orbital is stopped when
either the maximum number of iterations per orbital
([NRMM](../incar-tags/NRMM.md)), or a certain convergence threshold has been
reached. The latter may be fine-tuned by means of the
[EBREAK](../incar-tags/EBREAK.md), [DEPER](../incar-tags/DEPER.md), and
[WEIMIN](../incar-tags/WEIMIN.md) tags. Note: we do not recommend you to
do so! Rather rely on the defaults instead.

The RMM-DIIS algorithm works
on a "per-orbital" basis and as such it trivially parallelizes over
orbitals, which is the default
<a href="/wiki/Parallelization" class="mw-redirect"
title="Parallelization">parallelization strategy of VASP</a>. However,
to cast some of the operations involved into the form of *matrix-matrix
multiplications* and leverage the performance of BLAS3 library calls,
the RMM-DIIS implementation in
VASP works on [NSIM](../incar-tags/NSIM.md) orbitals simultaneously.

Note that, in the [self-consistency
cycle](Self-consistency_cycle.md) of VASP,
subspace rotation and RMM-DIIS
refinement of the orbitals alternate. Furthermore, VASP
re-orthonormalizes the orbitals after the
RMM-DIIS refinement step. It
should be emphasized that, in principle, the
RMM-DIIS method should also
converge without any explicit subspace diagonalization and/or
re-orthonormalization. However, in our experience their inclusion speeds
up convergence so substantially that it shortens the time-to-solution of
most calculations, even though these operations scale as
$O(N^3)$.[^kresse:cms:1996-1][^kresse:prb:96-2]

A drawback of the RMM-DIIS
method is that it always converges toward the eigenstates which are
closest to the initial trial orbitals. This leads, in principle, to
serious problems because there is no guarantee of convergence to the
correct ground state at all: if the initial set of orbitals does not
‘‘span’’ the ground state it might happen that in the final solution
some eigenstates are ‘‘missing’’. To avoid this, the initialization of
the orbitals must be done with great care. Therefore, either the number
of non-selfconsistent cycles at the start of [self-consistency
cycle](Self-consistency_cycle.md) is chosen
to be large ([NELMDL](../incar-tags/NELMDL.md) = 12, for
[ALGO](../incar-tags/ALGO.md) = VeryFast), or the non-selfconsistent cycles
are done with the [blocked-Davidson
algorithm](Blocked-Davidson_algorithm.md)
before switching over to the use of the
RMM-DIIS
([ALGO](../incar-tags/ALGO.md) = Fast).

The RMM-DIIS is approximately
a factor of 1.5-2 faster than the [blocked-Davidson
algorithm](Blocked-Davidson_algorithm.md),
but less robust.

## References\[<a href="/wiki/index.php?title=RMM-DIIS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^kresse:cms:1996-1]: [G. Kresse and J. Furthmüller, Comp. Mater. Sci. **6**, 15 (1996)](https://doi.org/10.1016/0927-0256(96)00008-0)
[^kresse:prb:96-2]: [G. Kresse and J. Furthmüller, Phys. Rev. B **54**, 11169 (1996).](https://doi.org/10.1103/PhysRevB.54.11169)
[^pulay:cpl:1980-3]: [P. Pulay, Chem. Phys. Lett. **73**, 393 (1980).](https://doi.org/10.1016/0009-2614(80)80396-4)

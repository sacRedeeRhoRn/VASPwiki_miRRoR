<!-- Source: https://vasp.at/wiki/index.php/Blocked-Davidson_algorithm | revid: 22849 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Blocked-Davidson algorithm


The workflow of the blocked-Davidson iterative matrix diagonalization
scheme implemented in VASP is as
follows:<sup>[\[1\]](#cite_note-kresse:cms:1996-1)[\[2\]](#cite_note-kresse:prb:96-2)</sup>

- Take a subset (block) of $n_1$
  orbitals out of the total set of [NBANDS](../incar-tags/NBANDS.md)
  orbitals:

$\\
\psi_n| n=1,..,N_{\rm bands}\\\Rightarrow \\ \psi^1_k| k=1,..,n_1\\$.

- Extend the subspace spanned by $\\\psi^1\\$
  by adding the preconditioned residual vectors of
  $\\\psi^1\\$:

$\left \\ \psi^1_k \\ / \\ g^1_k = \left (1- \sum_{n=1}^{N_{\rm bands}}
| \psi_n \rangle \langle\psi_n | {\bf S} \right) {\bf K} \left ({\bf
H} - \epsilon_{\rm app} {\bf S} \right ) \psi^1_k \\ | \\ k=1,..,n_1
\right \\.$

- Rayleigh-Ritz optimization ("subspace rotation") within the
  $2n_1$-dimensional space spanned by
  $\\\psi^1/g^1\\$, to determine the
  $n_1$ lowest eigenvectors:

${\rm diag}\\\psi^1/g^1\\ \Rightarrow \\ \psi^2_k| k=1,..,n_1\\$

- Extend the subspace with the residuals of $\\\psi^2\\$:

$\left \\ \psi^2_k \\/ \\ g^1_k \\ / \\ g^2_k = \left (1-
\sum_{n=1}^{N_{\rm bands}} | \psi_n \rangle \langle\psi_n | {\bf S}
\right ) {\bf K} \left ({\bf H} - \epsilon_{\rm app} {\bf S} \right)
\psi^2_k \\ | \\ k=1,..,n_1 \right \\.$

- Rayleigh-Ritz optimization ("subspace rotation") within the
  $3n_1$-dimensional space spanned by
  $\\\psi^1/g^1/g^2\\$:

${\rm diag}\\\psi^1/g^1/g^2\\ \Rightarrow \\ \psi^3_k| k=1,..,n_1\\$

- If need be the subspace may be extended by repetition of this cycle of
  adding residual vectors and Rayleigh-Ritz optimization of the
  resulting subspace:

${\rm diag}\\\psi^1/g^1/g^2/../g^{d-1}\\\Rightarrow \\ \psi^d_k|
k=1,..,n_1\\$

Per default VASP will not iterate deeper than
$d=4$, though it may break off even sooner when certain
criteria that measure the convergence of the orbitals have been met.

- When the iteration is finished, store the optimized block of orbitals
  back into the set:

$\\
\psi^d_k| k=1,..,n_1\\ \Rightarrow \\ \psi_k| k=1,..,N_{\rm bands}\\$.

- Move on to the next block $\\ \psi^1_k| k=n_1+1,..,2
  n_1\\$.
- When [LDIAG](../incar-tags/LDIAG.md)=.TRUE. (default), a Rayleigh-Ritz
  optimization in the complete subspace $\\ \psi_k| k=1,..,N_{\rm
  bands}\\$ is performed after all orbitals have been
  optimized.

  
The blocksize $n_1$ used in
the blocked-Davidson algorithm can be set by means of the
[NSIM](../incar-tags/NSIM.md) tag. In principle $n_1= 2\times$
[NSIM](../incar-tags/NSIM.md), but for technical reasons it needs to be
dividable by an integer *N*:

$n_1 = {\rm int}\left(\frac{2\*{\rm NSIM} + N - 1}{N}\right) N$

where $N$ is the
"number of band groups per k-point group":

$N
= \frac{{\rm \\\\ of\\ MPI\\ ranks}}{{\rm IMAGES}\*{\rm KPAR}\*{\rm
NCORE}}$

(see <a href="/wiki/Parallelization#Basic_parallelization"
class="mw-redirect" title="Parallelization">the section on
parallelization basics</a>).

As mentioned before, the optimization of a block of orbitals is stopped
when either the maximum iteration depth ([NRMM](../incar-tags/NRMM.md)), or
a certain convergence threshold has been reached. The latter may be
fine-tuned by means of the [EBREAK](../incar-tags/EBREAK.md),
[DEPER](../incar-tags/DEPER.md), and [WEIMIN](../incar-tags/WEIMIN.md) tags.
Note: we do not recommend you to do so! Rather rely on the defaults
instead.

The blocked-Davidson algorithm is approximately a factor of 1.5-2 slower
than the [RMM-DIIS](RMM-DIIS.md), but more robust.

## References\[<a
href="/wiki/index.php?title=Blocked-Davidson_algorithm&amp;veaction=edit&amp;section=1"
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



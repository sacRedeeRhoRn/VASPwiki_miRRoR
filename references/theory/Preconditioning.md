<!-- Source: https://vasp.at/wiki/index.php/Preconditioning | revid: 31528 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Preconditioning


The idea is to find a matrix that multiplied with the residual vector
gives the exact error in the wavefunction. Formally this matrix (the
Greens function) can be written down and is given by

$\frac{1}{{\bf H} - \epsilon_n},$

where $\epsilon_n$
is the exact eigenvalue for the band in interest. Actually the
evaluation of this matrix is not possible, recognizing that the kinetic
energy dominates the Hamiltonian for large $\mathbf{G}$-vectors (i.e. $H_{\mathbf{G},\mathbf{G'}}
\to \delta_{\mathbf{G},\mathbf{G'}} \frac{\hbar^2}{2m} \mathbf{G}^2$), it is a good idea to approximate the matrix by a
diagonal function which converges to $\frac{2m}{\hbar^2
\mathbf{G}^2}$ for large $\mathbf{G}$
vectors, and possess a constant value for small
$\mathbf{G}$ vectors. We actually use the
preconditioning function proposed by Teter et.
al<sup>[\[1\]](#cite_note-teter:prb:1989-1)</sup>

$\langle \mathbf{G} | {\bf K} | \mathbf{G'}\rangle =
\delta_{\mathbf{G} \mathbf{G'}} \frac{ 27 + 18 x+12 x^2 + 8x^3} {27 +
18x + 12x^2+8x^3 +16x^4} \quad \mbox{and} \quad x = \frac{\hbar^2}{2m}
\frac{G^2} {1.5 E^{\rm kin}( \mathbf{R}) },$

with $E^{\rm kin}(\mathbf{R})$ being the kinetic energy of the residual vector. The
preconditioned residual vector is then simply

$|
p_n \rangle = {\bf K} | R_n \rangle.$

## References\[<a
href="/wiki/index.php?title=Preconditioning&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-teter:prb:1989_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.40.12255"
    class="external text" rel="nofollow">M. P. Teter, M. C. Payne, and D. C.
    Allan, Phys. Rev. B <strong>40</strong>, 12255 (1989).</a>


------------------------------------------------------------------------



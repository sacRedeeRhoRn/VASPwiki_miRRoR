<!-- Source: https://vasp.at/wiki/index.php/Conjugate_gradient_optimization | revid: 15102 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Conjugate gradient optimization


Instead of the previous iteration scheme, which is just some kind of
Quasi-Newton scheme, it also possible to optimize the expectation value
of the Hamiltonian using a successive number of conjugate gradient
steps. The first step is equal to the steepest descent step in section
<a
href="/wiki/index.php?title=Single_band_steepest_descent_scheme&amp;action=edit&amp;redlink=1"
class="new"
title="Single band steepest descent scheme (page does not exist)">Single
band steepest descent scheme</a>. In all following steps the
preconditioned gradient $g^N_{n}$ is
conjugated to the previous search direction. The resulting conjugate
gradient algorithm is almost as efficient as the algorithm given in <a
href="/wiki/index.php?title=Efficient_single_band_eigenvalue-minimization&amp;action=edit&amp;redlink=1"
class="new"
title="Efficient single band eigenvalue-minimization (page does not exist)">Efficient
single band eigenvalue-minimization</a>. For further reading see
<sup>[\[1\]](#cite_note-teter:prb:1989-1)[\[2\]](#cite_note-bylander:prb:1990-2)[\[3\]](#cite_note-press:book:1986-3)</sup>.

## References\[<a
href="/wiki/index.php?title=Conjugate_gradient_optimization&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-teter:prb:1989_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.40.12255"
    class="external text" rel="nofollow">M. P. Teter, M. C. Payne, and D. C.
    Allan, Phys. Rev. B <strong>40</strong>, 12255 (1989).</a>
2.  [↑](#cite_ref-bylander:prb:1990_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.42.1394" class="external text"
    rel="nofollow">D. M. Bylander, L. Kleinman, and S. Lee, Phys Rev. B
    <strong>42</strong>, 1394 (1990).</a>
3.  [↑](#cite_ref-press:book:1986_3-0)
    <a href="https://archive.org/details/numericalrecipes00pres"
    class="external text" rel="nofollow">W. H. Press, B. P. Flannery, S. A.
    Teukolsky, and W. T. Vetterling, em Numerical Recipes (Cambridge
    University Press, New York, 1986).</a>


------------------------------------------------------------------------



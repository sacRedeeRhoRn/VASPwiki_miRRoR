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
[^teter:prb:1989-1][^bylander:prb:1990-2][^press:book:1986-3].

## References\[<a
href="/wiki/index.php?title=Conjugate_gradient_optimization&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^teter:prb:1989-1]: [M. P. Teter, M. C. Payne, and D. C. Allan, Phys. Rev. B **40**, 12255 (1989).](https://doi.org/10.1103/PhysRevB.40.12255)
[^bylander:prb:1990-2]: [D. M. Bylander, L. Kleinman, and S. Lee, Phys Rev. B **42**, 1394 (1990).](https://doi.org/10.1103/PhysRevB.42.1394)
[^press:book:1986-3]: [W. H. Press, B. P. Flannery, S. A. Teukolsky, and W. T. Vetterling, em Numerical Recipes (Cambridge University Press, New York, 1986).](https://archive.org/details/numericalrecipes00pres)

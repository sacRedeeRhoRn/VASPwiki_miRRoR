<!-- Source: https://vasp.at/wiki/index.php/Conjugate_gradient_optimization | revid: 15102 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Conjugate gradient optimization
Instead of the previous iteration scheme, which is just some kind of
Quasi-Newton scheme, it also possible to optimize the expectation value
of the Hamiltonian using a successive number of conjugate gradient
steps. The first step is equal to the steepest descent step in section
[Single band steepest descent
scheme](https://vasp.at/wiki/index.php/index.php)").
In all following steps the preconditioned gradient
$g^N_{n}$ is conjugated to the previous
search direction. The resulting conjugate gradient algorithm is almost
as efficient as the algorithm given in [Efficient single band
eigenvalue-minimization](https://vasp.at/wiki/index.php/index.php)").
For further reading see
^([\[1\]](#cite_note-teter:prb:1989-1)[\[2\]](#cite_note-bylander:prb:1990-2)[\[3\]](#cite_note-press:book:1986-3)).

## References
1.  [↑](#cite_ref-teter:prb:1989_1-0) [M. P. Teter, M. C. Payne,
    and D. C. Allan, Phys. Rev. B **40**, 12255
    (1989).](https://doi.org/10.1103/PhysRevB.40.12255)
2.  [↑](#cite_ref-bylander:prb:1990_2-0) [D. M. Bylander, L. Kleinman,
    and S. Lee, Phys Rev. B **42**, 1394
    (1990).](https://doi.org/10.1103/PhysRevB.42.1394)
3.  [↑](#cite_ref-press:book:1986_3-0) [W. H. Press, B. P.
    Flannery, S. A. Teukolsky, and W. T. Vetterling, em Numerical
    Recipes (Cambridge University Press, New York,
    1986).](https://archive.org/details/numericalrecipes00pres)

------------------------------------------------------------------------

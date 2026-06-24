<!-- Source: https://vasp.at/wiki/index.php/ODDONLY | revid: 21680 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ODDONLY
ODDONLY = .TRUE. \| .FALSE.  
Default: **ODDONLY** = .FALSE. 

Description: ODDONLY=.TRUE. selects a subset of **k**-points for the
representation of the Fock exchange potential, with *C*₁=*C*₂=*C*₃=1,
and *n*₁+*n*₂+*n*₃ odd.

------------------------------------------------------------------------

One may restrict the sum over **q** in the [Fock exchange
potential](../methods/Hybrid_functionals-_formalism.md)
(or one of its short range counterparts) to a subset, {**q**_(**k**)},
of the full (*N*₁×*N*₂×*N*₃) **k**-point set, {**k**}, for which the
following holds

$\mathbf{q_k} = \mathbf{b}_1 \frac{n_1
C_1}{N_1} + \mathbf{b}_2 \frac{n_2 C_2}{N_2} + \mathbf{b}_3 \frac{n_3
C_3}{N_3},\quad(n_i=0,..,N_i-1)$

where **b**_(1,2,3) are the reciprocal lattice vectors of the primitive
cell, and *C*_(i) is the integer grid reduction factor along reciprocal
lattice direction **b**_(i).

ODDONLY=.TRUE. selects a subset of **k**-points with *C*₁=*C*₂=*C*₃=1,
and *n*₁+*n*₂+*n*₃ odd. It reduces the computational work load for HF
type calculations by a factor two, but is only sensible for high
symmetry cases (such as sc, fcc or bcc cells).

  

|  |
|----|
| **Warning:** [there are circumstances under which **NKRED** and **NKREDX**,**Y**,**Z** should not be used!](../methods/Downsampling_of_the_Hartree-Fock_operator.md) |

## Related tags and articles
[NKRED](NKRED.md), [NKREDX](NKREDX.md),
[NKREDY](NKREDY.md), [NKREDZ](NKREDZ.md),
[EVENONLY](EVENONLY.md),
[downsampling](../methods/Downsampling_of_the_Hartree-Fock_operator.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ODDONLY-_incategory-Examples)

------------------------------------------------------------------------

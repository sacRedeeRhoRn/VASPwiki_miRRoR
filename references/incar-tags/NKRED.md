<!-- Source: https://vasp.at/wiki/index.php/NKRED | revid: 21675 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NKRED
NKRED = \[integer\]  
Default: **NKRED** = 1 

Description: NKRED specifies an uniform reduction factor for the
**q**-point grid representation of the exact exchange potential and the
correlation part in GW calculations.

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
lattice direction **b**_(i). This leads to a reduction in the
computational workload by a factor:

$\frac{1}{C_1 C_2 C_3}$

In case one sets NKRED, the grid reduction factors will be uniformly set
to *C*₁=*C*₂=*C*₃=NKRED. If one wants to specify separate grid reduction
factors for *C*₁, *C*₂, and *C*₃ one should use
*C*₁=[NKREDX](NKREDX.md),
*C*₂=[NKREDY](NKREDY.md), and
*C*₃=[NKREDZ](NKREDZ.md), respectively.

This flag also applies to GW and RPA calculations with a similar
speedup. In GW and RPA type calculations, analogously to hybrid
functional calculations the outermost loop over the momentum transfer
**q** is reduced to a subgrid specified by the NKRED parameters.

  

|  |
|----|
| **Warning:** [there are circumstances under which **NKRED** and **NKREDX**,**Y**,**Z** should not be used!](../methods/Downsampling_of_the_Hartree-Fock_operator.md) |

## Related tags and articles
[NKREDX](NKREDX.md), [NKREDY](NKREDY.md),
[NKREDZ](NKREDZ.md), [EVENONLY](EVENONLY.md),
[ODDONLY](ODDONLY.md),
[downsampling](../methods/Downsampling_of_the_Hartree-Fock_operator.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NKRED-_incategory-Examples)

------------------------------------------------------------------------

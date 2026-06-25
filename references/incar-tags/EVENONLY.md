<!-- Source: https://vasp.at/wiki/index.php/EVENONLY | revid: 21679 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EVENONLY


EVENONLY = .TRUE. \| .FALSE.  
Default: **EVENONLY** = .FALSE. 

Description: EVENONLY=.TRUE.
selects a subset of **k**-points for the representation of the Fock
exchange potential, with
*C*<sub>1</sub>=*C*<sub>2</sub>=*C*<sub>3</sub>=1, and
*n*<sub>1</sub>+*n*<sub>2</sub>+*n*<sub>3</sub> even.

------------------------------------------------------------------------

One may restrict the sum over **q** in the [Fock exchange
potential](../methods/Hybrid_functionals-_formalism.md)
(or one of its short range counterparts) to a subset,
{**q**<sub>**k**</sub>}, of the full
(*N*<sub>1</sub>×*N*<sub>2</sub>×*N*<sub>3</sub>) **k**-point set,
{**k**}, for which the following holds

$\mathbf{q_k} = \mathbf{b}_1 \frac{n_1 C_1}{N_1} + \mathbf{b}_2
\frac{n_2 C_2}{N_2} + \mathbf{b}_3 \frac{n_3
C_3}{N_3},\quad(n_i=0,..,N_i-1)$

where **b**<sub>1,2,3</sub> are the reciprocal lattice vectors of the
primitive cell, and *C*<sub>i</sub> is the integer grid reduction factor
along reciprocal lattice direction **b**<sub>i</sub>.

EVENONLY=.TRUE. selects a
subset of **k**-points with
*C*<sub>1</sub>=*C*<sub>2</sub>=*C*<sub>3</sub>=1, and
*n*<sub>1</sub>+*n*<sub>2</sub>+*n*<sub>3</sub> even. It reduces the
computational work load for HF type calculations by a factor two, but is
only sensible for high symmetry cases (such as sc, fcc or bcc cells).

  

|  |
|----|
| **Warning:** [there are circumstances under which **NKRED** and **NKREDX**,**Y**,**Z** should not be used!](../methods/Downsampling_of_the_Hartree-Fock_operator.md) |

## Related tags and articles\[<a href="/wiki/index.php?title=EVENONLY&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NKRED](NKRED.md), [NKREDX](NKREDX.md),
[NKREDY](NKREDY.md), [NKREDZ](NKREDZ.md),
[ODDONLY](ODDONLY.md),
[downsampling](../methods/Downsampling_of_the_Hartree-Fock_operator.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EVENONLY-_incategory-Examples)

------------------------------------------------------------------------



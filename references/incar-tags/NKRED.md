<!-- Source: https://vasp.at/wiki/index.php/NKRED | revid: 21675 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NKRED


NKRED = \[integer\]  
Default: **NKRED** = 1 

Description: NKRED specifies
an uniform reduction factor for the **q**-point grid representation of
the exact exchange potential and the correlation part in GW
calculations.

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
along reciprocal lattice direction **b**<sub>i</sub>. This leads to a
reduction in the computational workload by a factor:

$\frac{1}{C_1 C_2 C_3}$

In case one sets NKRED, the
grid reduction factors will be uniformly set to
*C*<sub>1</sub>=*C*<sub>2</sub>=*C*<sub>3</sub>=NKRED.
If one wants to specify separate grid reduction factors for
*C*<sub>1</sub>, *C*<sub>2</sub>, and *C*<sub>3</sub> one should use
*C*<sub>1</sub>=[NKREDX](NKREDX.md),
*C*<sub>2</sub>=[NKREDY](NKREDY.md), and
*C*<sub>3</sub>=[NKREDZ](NKREDZ.md), respectively.

This flag also applies to GW and RPA calculations with a similar
speedup. In GW and RPA type calculations, analogously to hybrid
functional calculations the outermost loop over the momentum transfer
**q** is reduced to a subgrid specified by the
NKRED parameters.

  

|  |
|----|
| **Warning:** [there are circumstances under which **NKRED** and **NKREDX**,**Y**,**Z** should not be used!](../methods/Downsampling_of_the_Hartree-Fock_operator.md) |

## Related tags and articles\[<a href="/wiki/index.php?title=NKRED&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NKREDX](NKREDX.md), [NKREDY](NKREDY.md),
[NKREDZ](NKREDZ.md), [EVENONLY](EVENONLY.md),
[ODDONLY](ODDONLY.md),
[downsampling](../methods/Downsampling_of_the_Hartree-Fock_operator.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NKRED-_incategory-Examples)

------------------------------------------------------------------------



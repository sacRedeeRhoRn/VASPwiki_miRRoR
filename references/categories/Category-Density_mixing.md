<!-- Source: https://vasp.at/wiki/index.php/Category:Density_mixing | revid: 25724 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Density mixing
**Density mixing** refers to the way of updating, e.g., the charge
density with each iteration step in a self-consistent calculation within
density-functional theory (DFT). In the case of magnetism and metaGGAs,
VASP can also consider the spin-magnetization density and kinetic-energy
density. Selecting the optimal procedure enhances the convergence of the
[electronic
minimization](Category-Electronic_minimization.md)
and avoids [charge sloshing](../theory/Charge_sloshing.md).
In many cases, VASP automatically selects suitable values, and it is
unnecessary to [set the tags related to density mixing
manually](#Improve_the_convergence).

## Contents

- [1 Theory](#Theory)
- [2 How to](#How_to)
  - [2.1 Improve the convergence](#Improve_the_convergence)
  - [2.2 Magnetic calculations](#Magnetic_calculations)
  - [2.3 MetaGGAs](#MetaGGAs)
- [3 References](#References)

## Theory
In each iteration of a DFT calculation, we start from a given charge
density $\rho_{in}$ and obtain the
corresponding Kohn-Sham (KS) Hamiltonian and its eigenstates, i.e., KS
orbitals. From the occupied KS orbitals, we can compute a new charge
density $\rho_{out}$. Thus,
conceptionally VASP solves a multidimensional fixed-point problem. To
solve this problem, VASP uses nonlinear solvers that work with the input
vector $\rho_{in}$ and the residual
$R = \rho_{out} - \rho_{in}$. The
optimal solution is obtained within the subspace spanned by the input
vectors. The most efficient density-mixing schemes are the
Broyden^([\[1\]](#cite_note-broyden:mc:1965-1)) and the
Pulay^([\[2\]](#cite_note-pulay:cpl:1980-2)) mixing
([IMIX](../incar-tags/IMIX.md)=4). In the
Broyden^([\[1\]](#cite_note-broyden:mc:1965-1)) mixing, an approximate
of the Jacobian matrix is iteratively improved to find the optimal
solution. In the Pulay^([\[2\]](#cite_note-pulay:cpl:1980-2)) mixing,
the input vectors are combined assuming linearity to minimize the
residual.

The implementation in VASP is based on the work of
Johnson^([\[3\]](#cite_note-johnson:prb:1988-3)). Kresse and
Furthmüller^([\[4\]](#cite_note-kresse:cms:1996-4)) extended on it and
demonstrated that the Broyden and Pulay schemes transform into each
other for certain choices of weights for the previous iterations. They
also introduced an efficient metric putting additional weight on the
long-range components of the density (small $\mathbf G$ vectors), resulting in a more robust convergence.
Furthermore, VASP uses a Kerker
preconditioning^([\[5\]](#cite_note-kerker:prb:1981-5)) to improve the
choice of the input density for the next iteration.

## How to
### Improve the convergence
For most simple DFT calculations, the default choice of the convergence
parameters is well suited to converge the calculation. As a first step,
we suggest visualizing your structure or examining the output for
warnings to check for very close atoms. That can happen during a
structure relaxation if VASP performs a large ionic step. If the
structure is correct, we recommend increasing the number of steps
[NELM](../incar-tags/NELM.md) and only if that doesn't work starting to
tweak the parameters [AMIX](../incar-tags/AMIX.md) or
[BMIX](../incar-tags/BMIX.md); preferably the latter.

### Magnetic calculations
For magnetic materials, the charge density and the spin-magnetization
density need to converge.

Hence, if you have problems to converge to a desired magnetic solution,
try to calculate first the non-magnetic groundstate, and continue from
the generated [WAVECAR](../input-files/WAVECAR.md) and
[CHGCAR](../input-files/CHGCAR.md) file. For the continuation job, you need
to set

    ISPIN = 2
    ICHARG = 1 

in the [INCAR](../input-files/INCAR.md) file.

### MetaGGAs
For the density mixing schemes to work reliably, the charge density
mixer must know all quantities that affect the total energy during the
self-consistency cycle. For a standard DFT functional, this is solely
the charge density. In the case of meta-GGAs, however, the total energy
depends on the kinetic-energy density.

In many cases, the density-mixing scheme works well enough without
passing the kinetic-energy density through the mixer, which is why
[LMIXTAU](../incar-tags/LMIXTAU.md)=.FALSE., per default. However, when
the self-consistency cycle fails to converge for one of the algorithms
exploiting density mixing, e.g., [IALGO](../incar-tags/IALGO.md)=38 or 48,
one may set [LMIXTAU](../incar-tags/LMIXTAU.md)=.TRUE. to have VASP pass
the kinetic-energy density through the mixer as well. It sometimes helps
to cure convergence problems in the self-consistency cycle.

## References
1.  ↑ ^([a](#cite_ref-broyden:mc:1965_1-0))
    ^([b](#cite_ref-broyden:mc:1965_1-1)) [C. G. Broyden, Math. Comput.
    **19**, 577
    (1965)](https://doi.org/10.1090/S0025-5718-1965-0198670-6)
2.  ↑ ^([a](#cite_ref-pulay:cpl:1980_2-0))
    ^([b](#cite_ref-pulay:cpl:1980_2-1)) [P. Pulay, Chem. Phys. Lett.
    **73**, 393 (1980).](https://doi.org/10.1016/0009-2614(80)80396-4)
3.  [↑](#cite_ref-johnson:prb:1988_3-0) [D. D. Johnson, Phys. Rev. B
    **38**, 12807 (1988)](https://doi.org/10.1103/PhysRevB.38.12807)
4.  [↑](#cite_ref-kresse:cms:1996_4-0) [G. Kresse and J. Furthmüller,
    Comp. Mater. Sci. **6**, 15
    (1996)](https://doi.org/10.1016/0927-0256(96)00008-0)
5.  [↑](#cite_ref-kerker:prb:1981_5-0) [G. P. Kerker, *Efficient
    iteration scheme for self-consistent pseudopotential calculations*,
    Phys. Rev. B **23**, 3082
    (1981).](https://doi.org/10.1103/PhysRevB.23.3082)

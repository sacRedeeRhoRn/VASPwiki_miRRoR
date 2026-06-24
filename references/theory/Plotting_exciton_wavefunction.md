<!-- Source: https://vasp.at/wiki/index.php/Plotting_exciton_wavefunction | revid: 35845 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Plotting exciton wavefunction
[![](https://vasp.at/wiki/images/thumb/6/60/HBN_exciton.png/400px-HBN_exciton.png)](https://vasp.at/wiki/File:HBN_exciton.png)

Charge density of the first bright exciton in hBN.

Plotting the wavefunction or charge density corresponding to an exciton
can be instrumental in analyzing the excitonic state's symmetry,
position, and localization.

The exciton wavefunction is written as a function of coordinates of two
particles (one hole and one electron) $\psi_\lambda(\mathbf{r}_e,\mathbf{r}_h)=\sum_{vc} A_{vc}^\lambda
\phi_v^\*(\mathbf{r}_h)\phi_c(\mathbf{r}_e)$
^([\[1\]](#cite_note-gatti:prb:2013-1)). In order to visualize such a
function in 3D space, we need to "fix" one of the coordinates: the
position of the electron $\psi_\lambda(r_e,\mathbf{r}_h)$ or the position of the hole
$\psi_\lambda(\mathbf{r}_e,r_h)$.

## Contents

- [1 How to fix the position of the
  particle](#How_to_fix_the_position_of_the_particle)
- [2 How to plot the exciton
  wavefunction](#How_to_plot_the_exciton_wavefunction)
- [3 Degeneracy](#Degeneracy)
- [4 Related tags and sections](#Related_tags_and_sections)
- [5 References](#References)

### How to fix the position of the particle
The position of the fixed particle is provided in direct (fractional)
coordinates by the tags [BSEHOLE](../incar-tags/BSEHOLE.md) or
[BSEELECTRON](../incar-tags/BSEELECTRON.md) for a hole or an
electron, respectively. The tag [NBSEEIG](../incar-tags/NBSEEIG.md) sets
the number of exciton wavefunctions that need to be computed.

When fixing the position of the particle, ensure that it is not fixed
exactly at the center of an atom or coincides with a node of the
wavefunction. To avoid that, shift the fixed coordinate slightly away
from the center of the atom. Furthermore, the wavefunction of the fixed
particle is taken at the nearest $\mathbf{G}$-vector, whose exact position is written in the
[OUTCAR](../output-files/OUTCAR.md) file

    hole position is fixed at:

or

    electron position is fixed at:

### How to plot the exciton wavefunction
VASP computes the charge density of a particular excitonic state, i.e.,
$\rho_\lambda(\mathbf{r})=|\psi_\lambda(r_e,\mathbf{r}_h)|^2$ or $\rho_\lambda(\mathbf{r})=|\psi_\lambda(\mathbf{r}_e,r_h)|^2$, and writes the resulting charge density into
[CHG](../output-files/CHG.md).XX files, which can be visualized using standard
tools like VESTA, ASE, etc. Here, XX stands for the index
$\lambda$ of the state. VASP computes
the charge density by transforming the unit cell with k-points into a
supercell. Thus, the exciton charge density is written for a supercell
of dimensions ${\rm NKX}\times{\rm NKX}\times{\rm
NKX}$. The size of the supercell is written in the
[OUTCAR](../output-files/OUTCAR.md) file

    FFT grid for supercell:

|  |
|----|
| **Mind:** The size of [CHG](../output-files/CHG.md).XX files can get very large. Estimate the [CHG](../output-files/CHG.md).XX file size as follows $(\mathrm{NGX\*NKX})\times(\mathrm{NGX\*NKX})\times(\mathrm{NGX\*NKX})\*12$ bytes. Here, NG{X,Y,Z} is the number of grid points and NK{X,Y,Z} is the number of k-points along the axis. |

|  |
|----|
| **Mind:** The exciton charge density only accounts for the plane-wave part of the wavefunction, and the augmentation terms are neglected. |

|  |
|----|
| **Warning:** In VASP 6.4.3 the exciton wavefunction is not correctly calculated in `vasp_std` and `vasp_ncl` if the hole or electron is not fixed at the coordinate (0,0,0). This issue was resolved in VASP 6.5.0 |

### Degeneracy
The calculated excitonic states can be degenerate, i.e., multiple
eigenvectors have the same energy. For the correct analysis, the
degenerate states should be added together.

|  |
|----|
| **Mind:** Calculation of the exciton wavefunction is only supported with [`IBSE`](../incar-tags/IBSE.md)` = 2` (or [`IBSE`](../incar-tags/IBSE.md)` = 0`), and [`ANTIRES`](../incar-tags/ANTIRES.md)` = 0`. |

## Related tags and sections
[CHG](../output-files/CHG.md), [NBSEEIG](../incar-tags/NBSEEIG.md),
[BSEHOLE](../incar-tags/BSEHOLE.md),
[BSEELECTRON](../incar-tags/BSEELECTRON.md),
[BSE](../tutorials/Bethe-Salpeter-equations_calculations.md)

## References
1.  [↑](#cite_ref-gatti:prb:2013_1-0) [Matteo Gatti and Francesco
    Sottile, Phys. Rev. B **88**, 155113
    (2013).](http://dx.doi.org/10.1103/PhysRevB.88.155113)

<!-- Source: https://vasp.at/wiki/index.php/LSORBIT | revid: 27887 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSORBIT


LSORBIT = .TRUE. \| .FALSE.  
Default: **LSORBIT** = .FALSE. 

Description: Switch on spin-orbit coupling.

------------------------------------------------------------------------

LSORBIT = True switches on
spin-orbit coupling
(SOC)<sup>[\[1\]](#cite_note-Steiner:2016-1)</sup>
and automatically sets
[LNONCOLLINEAR](LNONCOLLINEAR.md) = True. It requires
using `vasp_ncl`. SOC couples the spin degrees of freedom with the
lattice degrees of freedom. We recommend carefully checking the symmetry
and convergence of your results when using SOC; see below.

LSORBIT only works for PAW
potentials and is not supported by ultrasoft pseudopotentials. It is
supported as of VASP.4.5.


## Contents


- [1 Assumptions
  and output](#Assumptions_and_output)
- [2 Symmetry and
  convergence](#Symmetry_and_convergence)
- [3 Related tags
  and articles](#Related_tags_and_articles)
- [4
  References](#References)


## Assumptions and output\[<a href="/wiki/index.php?title=LSORBIT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Assumptions and output">edit</a> \| (./index.php.md)\]

- Switching on spin-orbit coupling (SOC) adds an additional term
  $H^{\alpha\beta}_{soc}\propto\mathbf{\sigma}\cdot\mathbf{L}$ to the Hamiltonian that couples the Pauli-spin
  operator $\mathbf{\sigma}$ with the angular momentum operator
  $\mathbf{L}$.<sup>[\[1\]](#cite_note-Steiner:2016-1)</sup>
  As a relativistic correction, SOC acts predominantly in the immediate
  vicinity of the nuclei. Therefore, it is assumed that contributions of
  $H_{soc}$ outside the PAW spheres are negligible.
  Hence, VASP calculates the matrix elements of
  $H_{soc}$ only for the all-electron one-center
  contributions

$E_{soc}^{ij} = \delta_{{\bf R}_i{\bf R}_j}\delta_{l_il_j} \sum_{n
\bf k} w_{\bf k} f_{n\bf k} \sum_{\alpha\beta} \langle
\tilde{\psi}^\alpha_{n\bf k} |\tilde{p}_i \rangle \langle \phi_i |
H^{\alpha\beta}_{soc} | \phi_j \rangle \langle \tilde{p}_j |
\tilde{\psi}^\beta_{n\bf k} \rangle$

where $\phi_i({\bf r}) = R_i(|{\bf
r}-{\bf R}_i|) Y_{l_im_i}(\theta,\varphi)$ are the
partial waves of an atom centered at ${\bf R}_i$,
$\tilde{\psi}^\alpha_{n\bf k}$ is the spinor-component
$\alpha=\uparrow,\downarrow$ of the pseudo-orbital with
band-index *n* and Bloch vector **k**, and $f_{n\bf k}$
and $w_{\bf k}$
are the Fermi- and **k**-point weights,
respectively.<sup>[\[1\]](#cite_note-Steiner:2016-1)</sup>

- It is possible to write the partial magnetization by setting
  [LORBIT](LORBIT.md), i.e., the site- and orbital-resolved
  expectation value of the Pauli-spin operator
  $\mathbf{\sigma}$. And the partial orbital angular
  momentum by setting [LORBMOM](LORBMOM.md), i.e., the
  site- and orbital-resolved expectation value of the orbital angular
  momentum operator $\mathbf{L}$.

|  |
|----|
| **Mind:** The orbital angular momentum (vector-like quantity) is written to the [OUTCAR](../output-files/OUTCAR.md) file in Cartesian coordinates, while the magnetic moments (spinor-like quantity) are read and written in the basis specified by [SAXIS](SAXIS.md) (spinor space). |

The default orientation of spinor space is $\sigma_1=\hat x$, $\sigma_2 =\hat y$, $\sigma_3 = \hat z$. Hence, the bases agree by default, and no
transformation is required.

- After a successful calculation including SOC, VASP writes the
  following results to the [OUTCAR](../output-files/OUTCAR.md) file:

<!-- -->

    Spin-Orbit-Coupling matrix elements

    Ion:    1  E_soc:     -0.0984080
    l=   1
        0.0000000    -0.0134381    -0.0134381
       -0.0134381     0.0000000    -0.0134381
       -0.0134381    -0.0134381     0.0000000
    l=   2
        0.0000000    -0.0005072     0.0000000    -0.0005072    -0.0024560
       -0.0005072     0.0000000    -0.0018420    -0.0005072    -0.0006140
        0.0000000    -0.0018420     0.0000000    -0.0018420     0.0000000
       -0.0005072    -0.0005072    -0.0018420     0.0000000    -0.0006140
       -0.0024560    -0.0006140     0.0000000    -0.0006140     0.0000000
    l=   3
        0.0000000    -0.0000000     0.0000000     0.0000000     0.0000000    -0.0000000    -0.0000000
       -0.0000000     0.0000000    -0.0000000     0.0000000    -0.0000000    -0.0000000    -0.0000000
        0.0000000    -0.0000000     0.0000000    -0.0000000    -0.0000000    -0.0000000     0.0000000
        0.0000000     0.0000000    -0.0000000     0.0000000    -0.0000000     0.0000000     0.0000000
        0.0000000    -0.0000000    -0.0000000    -0.0000000     0.0000000    -0.0000000     0.0000000
       -0.0000000    -0.0000000    -0.0000000     0.0000000    -0.0000000     0.0000000    -0.0000000
       -0.0000000    -0.0000000     0.0000000     0.0000000     0.0000000    -0.0000000     0.0000000

Here, `1 E_soc` represents the accumulated energy contribution
$E_{soc}=\sum_{ij} E_{soc}^{ij}$ inside the
augmentation sphere that is centered at ${\bf R}_1$
(position of ion 1), while the following entries correspond to the
matrix elements $E_{soc}^{ij}$ for the angular momentum $l$. Rows and
columns correspond to $m$ and
$m'$ of the real spherical harmonics
$Y_{lm}$(see [Angular
functions](../misc/Angular_functions.md) for naming and
ordering conventions).

## Symmetry and convergence\[<a href="/wiki/index.php?title=LSORBIT&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Symmetry and convergence">edit</a> \| (./index.php.md)\]

In any spin-polarized ([ISPIN](ISPIN.md)=2) or noncollinear
([LNONCOLLINEAR](LNONCOLLINEAR.md)=T) calculation,
even without SOC, the total energy depends on the relative orientation
of magnetic moments. For instance, two magnetic sites may couple
ferromagnetically or antiferromagnetically. On the other hand, the total
energy is independent of the orientation of the magnetic moments with
respect to the lattice without SOC. For instance, in-plane and
out-of-plane moments on a surface would yield the same energy in the
absence of SOC.

Switching on SOC couples the spin degrees of freedom that live in spinor
space and the lattice degrees of freedom that live in real space, see
[SAXIS](SAXIS.md). Therefore, the in-plane and out-of-plane
magnetic moments on a surface would yield different energies, when
including SOC. Similarly, the ferromagnetically or antiferromagnetically
ordered magnetic moments may additionally align with, e.g., the third
lattice vector by setting
LSORBIT = True.

Generally, be extremely diligent when using SOC: The energy differences
can be of the order of few $\mu$eV/atom,
k-point convergence is tedious and slow, and the required compute time
might be huge, even for small cells.

|  |
|----|
| **Warning:** When SOC is included, we recommend testing whether switching off symmetry ([ISYM](ISYM.md)=-1) changes the results. |

Often, the k-point set changes from one to the other spin orientation,
thus worsening the transferability of the results. Note that the
[WAVECAR](../input-files/WAVECAR.md) file cannot be reread properly if the
number of k-points changes. Hence, restart the calculation without
symmetry from a converged charge density by setting
[ICHARG](ICHARG.md)=1! Also, consider the setting of
[LMAXMIX](LMAXMIX.md).

We recommend setting [GGA_COMPAT](GGA_COMPAT.md) = False
for noncollinear calculations since this improves the numerical
precision of GGA calculations.

Please check the sections on
[LNONCOLLINEAR](LNONCOLLINEAR.md),
[SAXIS](SAXIS.md), [LMAXMIX](LMAXMIX.md), and
[GGA_COMPAT](GGA_COMPAT.md).

## Related tags and articles\[<a href="/wiki/index.php?title=LSORBIT&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LNONCOLLINEAR](LNONCOLLINEAR.md),
[MAGMOM](MAGMOM.md), [SAXIS](SAXIS.md),
[LORBMOM](LORBMOM.md), [LORBIT](LORBIT.md),
[LMAXMIX](LMAXMIX.md),
[GGA_COMPAT](GGA_COMPAT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSORBIT-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LSORBIT&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-Steiner:2016_1-0)</sup>
    <sup>[b](#cite_ref-Steiner:2016_1-1)</sup>
    <sup>[c](#cite_ref-Steiner:2016_1-2)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.93.224425"
    class="external text" rel="nofollow">S. Steiner, S. Khmelevskyi, M.
    Marsman, and G. Kresse, Phys. Rev. B <strong>93</strong>, 224425
    (2016).</a>


------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/Category:Crystal_momentum | revid: 35407 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Crystal momentum


A crystal is characterized by the fact that it obeys translational
<a href="/wiki/Symmetry" class="mw-redirect"
title="Symmetry">symmetry</a>. The concept of **crystal momentum** is
crucial in order to take into account interactions that go beyond the
primitive unit cell during a simulation. It arises as a direct
consequence of translational invariance and allows one to work with a
finite unit cell while capturing the physics of the infinite periodic
solid.

## Theoretical background\[<a
href="/wiki/index.php?title=Category:Crystal_momentum&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theoretical background">edit</a> \| (./index.php.md)\]

Formally, translational invariance can be written as a translation
operator that commutes with the Hamiltonian:

$\[T_{\mathbf R},H\]=0$

For the [KS
orbitals](../methods/Projector-augmented-wave_formalism.md)
this implies that each translation can only add a phase factor:

$T_\mathbf{R} \psi_{n\mathbf{k}}(\mathbf{r}) =
\text{e}^{\text{i}\mathbf{k}\cdot\mathbf{R}}\psi_{n\mathbf{k}}(\mathbf{r}),$

where $n$ is the
band index. Performing two consecutive translations should yield the sum
of the individual translations:

$T_{\mathbf{R}_1}T_{\mathbf{R}_2} \psi_{n\mathbf
k}(\mathbf{r})=T_{\mathbf{R}_1+\mathbf{R}_2}\psi_{n\mathbf
k}(\mathbf{r}).$

For a system with translational invariance, we obtain a periodic
potential and, hence, it is most convenient to use periodic boundary
conditions.

By virtue of the *Bloch theorem*, we can separate each KS orbital into

$\psi_{n\mathbf{k}}(\mathbf{r})=u_{n\mathbf{k}}(\mathbf{r})\text{e}^{\text{i}\mathbf{k}\cdot\mathbf{r}}$

a cell-periodic part $u$ and a
phase factor $\phi =
\mathbf{k}\cdot\mathbf{r}$. The phase
$\phi$ is called Bloch factor and
$\mathbf{k}$ is the **crystal momentum** which lives in
reciprocal space. Note that $u_{n\mathbf{k}}$ depends on $\mathbf{k}$.

The reciprocal space is spanned by reciprocal lattice vectors
$\mathbf{b}_i$:

$\mathbf{b}_1 = \frac{2\pi}{\Omega} \mathbf{a}_2 \times \mathbf{a}_3,
\quad \mathbf{b}_2 = \frac{2\pi}{\Omega} \mathbf{a}_3 \times
\mathbf{a}_1, \quad \mathbf{b}_3 = \frac{2\pi}{\Omega} \mathbf{a}_1
\times \mathbf{a}_2$

These are defined in terms of the real-space lattice vectors
$\mathbf{a}_i$ ([POSCAR](../input-files/POSCAR.md)), where
$\Omega = \mathbf{a}_1 \cdot \mathbf{a}_2 \times \mathbf{a}_3$ is the volume of the unit cell. Note that a short
real-space direction yields a long direction in reciprocal space:

$\mathbf{a}_i\cdot \mathbf{b}_j = 2\pi \delta_{ij}$

Based on the reciprocal lattice vectors $\mathbf{b}_i$, we can identify a *primitive cell in reciprocal
space*; this is the so-called first Brillouin zone (first BZ). The
connection between real space and reciprocal space is a Fourier
transformation, so the integral over all of real space (as is frequently
required to compute properties) can be expressed as an integral over the
first BZ:

$\int_{-\infty}^{\infty} \text{d}^3 r\\ f(\mathbf{r})
=\frac{1}{\Omega_{BZ}}\int_{\text{1st BZ}} \text{d}^3 k\\
\tilde{f}(\mathbf{k})$

In principle one has to include an infinite number of
$\mathbf{k}$ points to converge this integral. In
practice, the integral is approximated by a sum on a finite regular
$\mathbf{k}$ mesh. Beyond a certain
$\mathbf{k}$-point density the result converges because
crystal momentum vectors that are close together are almost identical:

$\int_{-\infty}^{\infty} \text{d}^3 r\\ f(\mathbf{r}) \approx
\sum_{\mathbf k \in \text{1st BZ}} \tilde{f}(\mathbf{k})\\ \Delta^3k$

The first BZ itself has a certain symmetry, so some
$\mathbf{k}$ points on the regular mesh are equivalent.
VASP automatically reduces the mesh to the irreducible
$\mathbf{k}$ points and applies appropriate weights
$w_\mathbf{k}$:

$\int_{-\infty}^{\infty} \text{d}^3 r\\ f(\mathbf{r}) \approx
\sum_{\mathbf{k} \in \text{irred. BZ}} w_\mathbf{k}\\
\tilde{f}(\mathbf{k})$

To see which <a href="/wiki/Symmetry" class="mw-redirect"
title="Symmetry">symmetry</a> VASP identified and which irreducible
$\mathbf{k}$ points are used, look at the
[OUTCAR](../output-files/OUTCAR.md) and [IBZKPT](../output-files/IBZKPT.md)
files.

For an introduction to crystal momentum and PAW formalism, see . For a
detailed discussion of $\mathbf{k}$-point sampling, see .

## k-point mesh setup\[<a
href="/wiki/index.php?title=Category:Crystal_momentum&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: k-point mesh setup">edit</a> \| (./index.php.md)\]

The $\mathbf{k}$-point mesh for the [SCF
calculation](../tutorials/Setting_up_an_electronic_minimization.md)
can be specified either via the [KPOINTS](../input-files/KPOINTS.md) file
or via the [KSPACING](../incar-tags/KSPACING.md) and
[KGAMMA](../incar-tags/KGAMMA.md) tags in the [INCAR](../input-files/INCAR.md)
file. To compute band structures or densities of states on a finer mesh
non-self-consistently, use the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) driver controlled by
[KSPACING_OPT](../incar-tags/KSPACING_OPT.md) or a
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file. Reading of the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file can be disabled with
[LKPOINTS_OPT](../incar-tags/LKPOINTS_OPT.md).

## References\[<a
href="/wiki/index.php?title=Category:Crystal_momentum&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]



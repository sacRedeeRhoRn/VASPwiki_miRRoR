<!-- Source: https://vasp.at/wiki/index.php/PROOUT | revid: 29862 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PROOUT
This file is written if [LORBIT](../incar-tags/LORBIT.md)=5 and the
[RWIGS](../incar-tags/RWIGS.md) tag is set in the
[INCAR](../input-files/INCAR.md) file. It contains the projection of the
Kohn-Sham orbitals $|\psi_{n\mathbf{k}}\rangle$ onto a localized orbitals basis $|\beta^\alpha_{lm}\rangle$ which can be written as

$P^\alpha_{lmn\mathbf{k}} \equiv \langle
\beta_{lm}^{\alpha}|S|\psi_{n\mathbf{k}}\rangle =
\underbrace{\langle
\beta_{lm}^{\alpha}|\psi_{n\mathbf{k}}\rangle}_{P^{\text{SOFT},\alpha}_{lmn\mathbf{k}}} +
\underbrace{\sum_{ij} \langle \beta^\alpha_{lm}|\tilde{p}_i\rangle
Q_{ij} \langle \tilde{p}_j |
\psi_{n\mathbf{k}}\rangle}_{P^{\text{AUG},\alpha}_{lmn\mathbf{k}}}.$

Here, the two terms on the right-hand side are called soft and
augmentation part, respectively, and $S$
is the overlap matrix,

$S = 1+\sum_{ij} |\tilde{p}_i\rangle Q_{ij}
\langle \tilde{p}_j|.$

The radial and the angular part of $\beta^\alpha_{lm}(\mathbf{r})$ are described by a linear
combination of spherical bessel functions $\phi_n(r)$ and by spherical harmonics $Y^\alpha_{lm}(\hat{\mathbf{r}})$, respectively:

$\beta^\alpha_{lm}(\mathbf{r}) =
Y^\alpha_{lm}(\hat{\mathbf{r}})\sum_n \phi_n(r).$

The spherical bessel functions $\phi_n(r)$ are parametrized to be non-zero within a radius determined by
[RWIGS](../incar-tags/RWIGS.md). In addition, it so happens that
$|\tilde{p}_i\rangle$ has a similar
form as $|\beta^\alpha_{lm}\rangle$
which simplifies the computations above.

The PROOUT file contains similar information as the
[PROCAR](PROCAR.md) file but the following differences
exist:

- The PROOUT file writes the real and imaginary parts of
  $P^{\text{SOFT},\alpha}_{lmn\mathbf{k}}$, and the real part of the augmentation part
  $P^{\text{AUG},\alpha}_{lmn\mathbf{k}}$.
- The [PROCAR](PROCAR.md) file contains the information of
  the squared projection, $P^\alpha_{lmn\mathbf{k}} (P^\alpha_{lmn\mathbf{k}})^{\*}$,
  whereas the PROOUT file contains $P^\alpha_{lmn\mathbf{k}}$.
- The arrangement of the output is very different in both files.

This information makes it possible to construct, e.g., partial DOS
projected onto bonding and anti-bonding molecular orbitals and the
so-called crystal-orbital-overlap-population (COOP) function. Depending
on the application, users might find it more practical to use the
information contained in the [PROJCAR](../incar-tags/PROJCAR.md) and
[LOCPROJ](../incar-tags/LOCPROJ.md) files. These are controlled by the
[LOCPROJ](../incar-tags/LOCPROJ.md) tag.

For spin-polarized calculations with [ISPIN](../incar-tags/ISPIN.md)=2 and
noncollinear calculations with
[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=.TRUE.,
**PROOUT.1** and **PROOUT.2** are written, referring to the Kohn-Sham
orbitals' two spin components.

## Format
- line 1: PROOUT
- line 2: Number of kpoints, bands and ions
- line 3: Twice the number of types followed by the number of ions for
  each type
- line 4: The Fermi weights for each k point (inner loop) and band
  (outer loop)
- line 5 $-$ ...: Real and imaginary
  part of $P^{\text{SOFT},\alpha}_{lmn\mathbf{k}}$ for every $lm$-quantum
  number (inner loop), band, ion per type, k point and ion type (outer
  loop).
- below : augmentation part
- last line: real part of $P^{\text{AUG},\alpha}_{lmn\mathbf{k}}$ for every
  $lm$-quantum number (inner loop), ion
  per type, ion type, band and k point (outer loop).

|  |
|----|
| **Warning:** For VASP version \<= 6.2.1, PROOUT is not correctly written when [LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md) = True. |

## Related Tags and Sections
[LORBIT](../incar-tags/LORBIT.md), [LOCPROJ](../incar-tags/LOCPROJ.md),
[PROJCAR](../incar-tags/PROJCAR.md), [PROCAR](PROCAR.md)

------------------------------------------------------------------------

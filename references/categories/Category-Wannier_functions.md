<!-- Source: https://vasp.at/wiki/index.php/Category:Wannier_functions | revid: 29312 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Wannier functions
Wannier functions $|w_{m\mathbf{R}}\rangle$ are constructed by a linear combination of Bloch states
$|\psi_{n\mathbf{k}}\rangle$, i.e.,
the computed Kohn-Sham (KS) orbitals, as follows:

$|w_{m\mathbf{R}}\rangle = \sum_{n\mathbf{k}}
e^{-i\mathbf{k}\cdot\mathbf{R}} U_{mn\mathbf{k}}
|\psi_{n\mathbf{k}}\rangle.$

Here, $U_{mn\mathbf{k}}$ is a unitary
matrix which can be generated using different approaches discussed
below, $m$ is an index enumerating
Wannier functions with position $\mathbf{R}$, $n$ is the band index, and
$\mathbf{k}$ is the Bloch vector.
Generally, one starts with an initial guess for $U_{mn\mathbf{k}}$ that is built from $A_{mn\mathbf{k}}$. The latter can be built from projections
onto some localized-orbital basis.

- Comprehensive instructions on [how to construct Wannier
  orbitals](../tutorials/Constructing_Wannier_orbitals.md).

## Contents

- [1 One-shot singular-value decomposition
  (SVD)](#One-shot_singular-value_decomposition_(SVD))
- [2 Selected columns of the density matrix
  (SCDM)](#Selected_columns_of_the_density_matrix_(SCDM))
- [3 Maximally localized Wannier functions using
  Wannier90](#Maximally_localized_Wannier_functions_using_Wannier90)
- [4 References](#References)

## One-shot singular-value decomposition (SVD)
In one-shot SVD, $A_{mn\mathbf{k}}$ is
computed by projecting the KS orbitals onto localized orbitals basis
$\phi_{m\mathbf{k}}$ that is specified
by the [LOCPROJ](../incar-tags/LOCPROJ.md) tag:

$A_{mn\mathbf{k}} = \langle \psi_{n\mathbf{k}}
| S |\phi_{m\mathbf{k}}\rangle,$

where

$\phi_{i\mathbf{k}}(\mathbf{r}) =
e^{\mathrm{i}\mathbf{k}\cdot\mathbf{r}} Y_{lm}(\hat{r})R_n(r).$

Note that $i$ encodes the quantum
numbers $n$, $l$, and $m$. Thus, in
$A_{mn\mathbf{k}}$,
$m$ is not the magnetic quantum number.

Then, VASP performs one-shot SVD for each k point

$A_{mn\mathbf{k}} = \[D \Sigma
V^\*\]_{mn\mathbf{k}}$

to obtain the unitary matrix

$U_{mn\mathbf{k}} = \[DV^\*\]_{mn\mathbf{k}}.$

## Selected columns of the density matrix (SCDM)
The SCDM method ^([\[1\]](#cite_note-damle:mms:2018-1)) is switched on
using [LSCDM](../incar-tags/LSCDM.md). It has the advantage that the
specification of a local basis in terms of atomic quantum numbers is
omitted.

## Maximally localized Wannier functions using Wannier90
The interface of VASP with the Wannier90
code^([\[2\]](#cite_note-mostofi:cpc:2014-2)[\[3\]](#cite_note-pizzi:jpcm:2020-3))
is mainly controlled by [LWANNIER90](../incar-tags/LWANNIER90.md) and
[LWANNIER90_RUN](../incar-tags/LWANNIER90_RUN.md). First, the
initial guess for $A_{mn\mathbf{k}}$
can be created by providing the *projections block* in the
**wannier90.win** file (also see
[WANNIER90_WIN](../incar-tags/WANNIER90_WIN.md)) and setting
[LWANNIER90](../incar-tags/LWANNIER90.md)=True.

In order to obtain maximally localized Wannier functions,
$U_{mn\mathbf{k}}$ is constructed in a
second step. For this, $A_{mn\mathbf{k}}$ could be created using any projection method in the first
step, i.e., single-shot SVD method ([LOCPROJ](../incar-tags/LOCPROJ.md)),
SCDM method ([LSCDM](../incar-tags/LSCDM.md)), or Wannier90
([LWANNIER90](../incar-tags/LWANNIER90.md)). Then, Wannier90 can be
executed directly or through VASP with the
[LWANNIER90_RUN](../incar-tags/LWANNIER90_RUN.md) tag.

## References
1.  [↑](#cite_ref-damle:mms:2018_1-0) [A. Damle and L. Lin, Multiscale
    Model. Simul., **16(3)**, 1392–1410
    (2018).](https://doi.org/10.1137/17M1129696)
2.  [↑](#cite_ref-mostofi:cpc:2014_2-0) [A. A. Mostofi, J. R. Yates, G.
    Pizzi, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, *An
    Updated Version of Wannier90: A Tool for Obtaining
    Maximally-Localised Wannier Functions*, Computer Physics
    Communications **185**, 2309
    (2014).](https://doi.org/10.1016/j.cpc.2014.05.003)
3.  [↑](#cite_ref-pizzi:jpcm:2020_3-0) [G. Pizzi et al., *Wannier90 as a
    community code: new features and applications*, J. Phys.: Condens.
    Matter **32**, 165902
    (2020).](https://doi.org/10.1088/1361-648X/ab51ff)

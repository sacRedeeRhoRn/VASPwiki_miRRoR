<!-- Source: https://vasp.at/wiki/index.php/Thermodynamic_integration | revid: 37271 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Thermodynamic integration
There are three implementations of thermodynamic integration (TI). The
settings for these calculations are described in [thermodynamic
integration
calculations](../tutorials/Thermodynamic_integration_calculations.md).
A detailed description of thermodynamic integration is given in
reference ^([\[1\]](#cite_note-dorner:PRL:2018-1)). An important
historic paper is Kirkwood 1936
^([\[2\]](#cite_note-kirkwood:jcp:1935-2)).

## Contents

- [1 Basic theory](#Basic_theory)
- [2 Thermodynamic integration with harmonic
  reference](#Thermodynamic_integration_with_harmonic_reference)
- [3 Thermodynamic integration using internal
  coordinates](#Thermodynamic_integration_using_internal_coordinates)
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

## Basic theory
The free energy of a fully interacting system can be written as the sum
of the free energy a non-interacting reference system and the difference
in the free energy of the fully interacting system and the
non-interacting system ^([\[1\]](#cite_note-dorner:PRL:2018-1))

$A_{1} = A_{0} + \Delta A_{0\rightarrow 1}$.

Using thermodynamic integration the free energy difference between the
two systems is written as

$\Delta A_{0\rightarrow 1} = \int\limits_{0}^{1}
d\lambda \langle U_{1}(\lambda) - U_{0}(\lambda) \rangle_{\lambda}$.

Here $U_{1}(\lambda)$ and
$U_{0}(\lambda)$ describe the potential
energies of a fully-interacting and a non-interacting reference system,
respectively. The coupling strength of the systems is controlled via the
coupling parameter $\lambda$. It is
neccessary that the connection of the two systems via the coupling
constant is reversible. The notation $\langle
\ldots \rangle_{\lambda}$ denotes an ensemble average of a
system driven by the following classical Hamiltonian

$H_{\lambda}= \lambda H_{1} + (1-\lambda) H_{0}$.

There are many options that can be taken for the non-interacting and
interacting systems. In Dorner et al., TI was first performed from a
harmonic system (the ideal gas) to the full *ab initio* Hamiltonian
(e.g., PBE) to include the anharmonic contributions
^([\[1\]](#cite_note-dorner:PRL:2018-1)); a second TI was then performed
to increase the *k*-mesh density and change the density functional
(e.g., SCAN, HSE06). We will now describe the theory when going from a
harmonic to anharmonic system, as this requires some special details.

## Thermodynamic integration with harmonic reference
The Helmholtz free energy ($A$) of a
fully interacting system (1) can be expressed in terms of that of system
harmonic in Cartesian coordinates (0,$\mathbf{x}$) as follows

$A_{1} = A_{0,\mathbf{x}} + \Delta
A_{0,\mathbf{x}\rightarrow 1}$

where $\Delta A_{0,\mathbf{x}\rightarrow 1}$ is anharmonic free energy. The latter term can be determined
by means of thermodynamic integration (TI)
^([\[2\]](#cite_note-kirkwood:jcp:1935-2))

$\Delta A_{0,\mathbf{x}\rightarrow 1} = \int_0^1
d\lambda \langle V_1 -V_{0,\mathbf{x}} \rangle_\lambda$

with $V_i$ being the potential energy of
system $i$, $\lambda$ is a coupling constant and $\langle\cdots\rangle_\lambda$ is the NVT ensemble average of
the system driven by the Hamiltonian

$\mathcal{H}_\lambda = \lambda \mathcal{H}_1 +
(1-\lambda)\mathcal{H}_{0,\mathbf{x}}$

Free energy of harmonic reference system within the quasi-classical
theory writes

$A_{0,\mathbf{x}} =
A_\mathrm{el}(\mathbf{x}_0) - k_\mathrm{B} T \sum_{i =
1}^{N_\mathrm{vib}} \ln \frac{k_\mathrm{B} T}{\hbar \omega_i}$

with the electronic free energy $A_\mathrm{el}(\mathbf{x}_0)$ for the configuration
corresponding to the potential energy minimum with the atomic position
vector $\mathbf{x}_0$, the number of
vibrational degrees of freedom $N_\mathrm{vib}$, and the angular frequency $\omega_i$ of vibrational mode $i$
obtained using the Hesse matrix $\underline{\mathbf{H}}^\mathbf{x}$. Finally, the harmonic
potential energy is expressed as

$V_{0,\mathbf{x}}(\mathbf{x}) =
V_{0,\mathbf{x}}(\mathbf{x}_0) + \frac{1}{2} (\mathbf{x} -
\mathbf{x}_0)^T \underline{\mathbf{H}}^\mathbf{x} (\mathbf{x} -
\mathbf{x}_0)$

Thus, a conventional TI calculation consists of the following steps:

1.  determine $\mathbf{x}_0$ and
    $V_{0,\mathbf{x}}(\mathbf{x}_0)$
    in structural relaxation
2.  compute $\omega_i$ in vibrational
    analysis
3.  use the data obtained in the point 2 to determine
    $\underline{\mathbf{H}}^\mathbf{x}$
    that defines the harmonic forcefield
4.  perform NVT MD simulations for several values of
    $\lambda \in \langle0,1\rangle$ and
    determine $\langle V_1 -V_{0,\mathbf{x}}
    \rangle$
5.  integrate $\langle V_1 -V_{0,\mathbf{x}}
    \rangle$ over the $\lambda$ grid and compute $\Delta
    A_{0,\mathbf{x}\rightarrow 1}$

Unfortunately, there are several problems linked with such a
straightforward approach. First, the systems with rotational and/or
translational degrees of freedom cannot be treated in a straightforward
manner because $V_{0,\mathbf{x}}(\mathbf{x})$ is not invariant under rotations and translations.
Conventional TI is thus unsuitable for simulations of gas-phase
molecules or adsorbate-substrate systems. and this problem also imposes
restrictions on the choice of thermostat used in NVT simulation
(Langevin thermostat, for instance, does not conserve the position of
the center of mass and is therefore unsuitable for use in conventional
TI). Furthermore, if the Hesse matrix of the harmonic system has one or
more eigenvalues that nearly vanish, the simulations with
$\lambda \rightarrow$ 0 are likely to
generate unphysical configurations, causing serious convergence issues.

## Thermodynamic integration using internal coordinates
The problems of TI using a harmonic reference have been addressed in a
series of works by Amsler et al
^([\[3\]](#cite_note-bucko:studt:jctc:2021-3)[\[4\]](#cite_note-bucko:studt:jctc:2023-4)).
First, the method was formulated in terms of rotationally and
translationally invariant internal coordinates $\mathbf{q}=\mathbf{q}(\mathbf{x})$, whereby the free energy of
the interacting system is repartitioned as follows:

$A_1 = A_{0,\mathbf{x}} + \Delta A_{0,\mathbf{x}
\rightarrow 0,\mathbf{q}} + \Delta A_{0,\mathbf{q} \rightarrow 1}$

where $\Delta A_{0,\mathbf{x} \rightarrow
0,\mathbf{q}}$ is the free energy change due to transformation
from the system harmonic in $\mathbf{x}$
into the system harmonic in $\mathbf{q}$
and $\Delta A_{0,\mathbf{q} \rightarrow 1}$ is that for the transformation of the latter into a fully
interacting system. The force field for the system harmonic in
$\mathbf{q}$ is defined as:

$V_{0,\mathbf{q}}(\mathbf{q}) =
V_{0,\mathbf{q}}(\mathbf{q}_0) + \frac{1}{2} (\mathbf{q} -
\mathbf{q}_0)^T \mathbf{\underline{H}^q} (\mathbf{q} - \mathbf{q}_0)$

where $\mathbf{q}_0=\mathbf{q}(\mathbf{x}_0)$ and the Hesse matrix $\mathbf{\underline{H}}^\mathbf{q}$ defined for a potential
energy minimum is related to $\mathbf{\underline{H}}^\mathbf{x}$ via $\mathbf{\underline{H}}^\mathbf{x} = \mathbf{\underline{B}}^T
\mathbf{\underline{H}}^\mathbf{q} \mathbf{\underline{B}}$ with
$\mathbf{\underline{B}}_{i,j} = \frac{\partial
q_i}{\partial x_j}$ being the Wilson matrix. Note that the
calculation of the term $\Delta A_{0,\mathbf{x}
\rightarrow 0,\mathbf{q}}$ is inexpensive as it corresponds to
a force field to force field transformation. Furthermore, this term
vanishes in the case of phase volume conserving coordinates, such as
interatomic distances.

## Related tags and articles
[VCAIMAGES](../incar-tags/VCAIMAGES.md),
[NCORE_IN_IMAGE1](../incar-tags/NCORE_IN_IMAGE1.md),
[IMAGE_1](../incar-tags/IMAGE_1.md), [SCALEE](../incar-tags/SCALEE.md),
[DYNMATFULL](../input-files/DYNMATFULL.md),
[PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md),
[TILAMBDA](../incar-tags/TILAMBDA.md),
[HESSEMAT](../incar-tags/HESSEMAT.md), [ICONST](../input-files/ICONST.md),
[REPORT](../output-files/REPORT.md)

[Thermodynamic integration
calculations](../tutorials/Thermodynamic_integration_calculations.md)

## References
1.  ↑ ^([a](#cite_ref-dorner:PRL:2018_1-0))
    ^([b](#cite_ref-dorner:PRL:2018_1-1))
    ^([c](#cite_ref-dorner:PRL:2018_1-2)) [F. Dorner, Z. Sukurma, C.
    Dellago, and G. Kresse, Phys. Rev. Lett. **121**, 195701
    (2018).](https://doi.org/10.1103/PhysRevLett.121.195701)
2.  ↑ ^([a](#cite_ref-kirkwood:jcp:1935_2-0))
    ^([b](#cite_ref-kirkwood:jcp:1935_2-1)) [J. Kirkwood, *Statistical
    Mechanics of Fluid Mixtures*, J. Chem. Phys. **3**, 300–313
    (1935).](https://doi.org/10.1063/1.1749657)
3.  [↑](#cite_ref-bucko:studt:jctc:2021_3-0) [J. Amsler, P. N.
    Plessow, F. Studt, T. Bucko, *Anharmonic Correction to Adsorption
    Free Energy from DFT-Based MD Using Thermodynamic Integration*, J.
    Chem. Theory Comput. **17**, 1155-1169
    (2021).](https://doi.org/10.1021/acs.jctc.0c01022)
4.  [↑](#cite_ref-bucko:studt:jctc:2023_4-0) [J. Amsler, P. N.
    Plessow, F. Studt, T. Bucko, *Anharmonic Correction to Free Energy
    Barriers from DFT-Based Molecular Dynamics Using Constrained
    Thermodynamic Integration*, J. Chem. Theory Comput. **19**,
    2455-2468 (2023).](https://doi.org/10.1021/acs.jctc.3c00169)

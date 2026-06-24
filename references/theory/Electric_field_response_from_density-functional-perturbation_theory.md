<!-- Source: https://vasp.at/wiki/index.php/Electric_field_response_from_density-functional-perturbation_theory | revid: 33373 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Electric field response from density-functional-perturbation theory
**Density-functional-perturbation theory (DFPT)** provides a way to
compute the behaviour of a material under an external perturbation (e.g.
ionic displacement, strain, electric fields) within the limits of
linear-response theory. For the case of an external electric field VASP
can employ DFPT for the computation of the static dielectric tensor, the
Born effective charges, and the piezoelectric tensor.

## Contents

- [1 Introduction](#Introduction)
- [2 Sternheimer equations](#Sternheimer_equations)
- [3 Computation of physical
  quantities](#Computation_of_physical_quantities)
  - [3.1 Ionic contributions](#Ionic_contributions)
    - [3.1.1 Piezoelectric tensor](#Piezoelectric_tensor)
    - [3.1.2 Dielectric tensor](#Dielectric_tensor)
- [4 Related tags and sections](#Related_tags_and_sections)
- [5 References](#References)

## Introduction
Under the presence of a small, finite external electric field,
$\mathcal{E_\alpha}$, the changes in
the total energy of the system due to $\mathcal{E_\alpha}$ can be computed from the polarization at
first order, and at second order in $\mathcal{E_\alpha}$ from the dielectric susceptibility,
Born-effective charges, and piezoelectric tensor.

All quantities can be computed via finite-differences methods (see for
instance [perturbation expansion after
discretization](../incar-tags/LPEAD.md) or the [modern theory of
polarisation](Berry_phases_and_finite_electric_fields.md)),
but they can also be computed employing DFPT. The essential quantities
are the wave functions at finite electric field, which can be
approximated as

$|\psi^{\mathcal{E}_\alpha}_\lambda\rangle =
|\psi\rangle + \lambda |\partial_{\mathcal{E}_\alpha}\psi\rangle,$

with $\lambda$ being the vanishing
strength of the field, and the static dielectric tensor

$\varepsilon^{\infty}(\hat{\mathbf q},0)= 1 -
\frac{8 \pi e^2}{\Omega} \lim _{\mathbf{q} \rightarrow
0}\frac{1}{\mathbf q^2} \sum_{c, v, \mathbf{k}} 2 w_{\mathbf{k}}
\left|\langle u_{c \mathbf{k+q}}|u_{v \mathbf{k}}\rangle\right|^2,$

which requires the periodic part of the wave function to be computed at
different momenta. However, in the limit of very small **q**, this can
be expanded as

$u_{n \mathbf{k}+\mathbf{q}}=u_{n
\mathbf{k}}+\mathbf{q} \cdot \nabla_{\mathbf{k}} u_{n
\mathbf{k}}+O\left(\mathbf{q}^2\right).$

So, both the derivative with respect to the crystal momentum **k** and
the finite electric field $\mathcal{E_\alpha}$ are required. Fortunately both can be obtained from a system
of coupled equations called the Sternheimer equations.

## Sternheimer equations
The starting point is density-functional theory (DFT), where one has to
solve the Kohn-Sham (KS) equations

$H(\mathbf{k}) | \psi_{n\mathbf{k}} \rangle=
e_{n\mathbf{k}}S(\mathbf{k}) | \psi_{n\mathbf{k}} \rangle,$

where $H(\mathbf{k})$ is the DFT
Hamiltonian, $S(\mathbf{k})$ is the
overlap operator and, $| \psi_{n\mathbf{k}}
\rangle$ and $e_{n\mathbf{k}}$ are the KS eigenpairs.

As it was mentioned before, to compute the response with respect to an
external electric field $\mathcal{E_\alpha}$ one requires the derivative of the orbitals with respect to
$\mathbf{k}$ and $\mathcal{E_\alpha}$. For the former we have
that^([\[1\]](#cite_note-gajdos:prb:2006-1))

$\left\[ H(\mathbf{k}) -
e_{n\mathbf{k}}S(\mathbf{k}) \right\]
|\partial_\mathbf{k}\tilde{u}_{n\mathbf{k}}\rangle =
-\partial_\mathbf{k} \left\[ H(\mathbf{k}) -
e_{n\mathbf{k}}S(\mathbf{k})\right\] |\tilde{u}_{n\mathbf{k}}\rangle$

while the latter is given by

$\left\[ H(\mathbf{k}) -
e_{n\mathbf{k}}S(\mathbf{k}) \right\]
|\partial_\mathcal{E_\alpha}\tilde{u}_{n\mathbf{k}} \rangle =
-\Delta H_{\text{SCF}}(\mathbf{k}) |\tilde{u}_{n\mathbf{k}}\rangle
-\mathbf{\hat{q}_\alpha}\cdot |\vec{\beta}_{n\mathbf{k}}\rangle.$

Here $\Delta H_{\text{SCF}}(\mathbf{k})
|\tilde{u}_{n\mathbf{k}}\rangle$ is the change in the
microscopic cell periodic part of the Hamiltonian that comes from the
change in wave functions (self-consistent field effects). These are
computed at first order only, thus ensuring that local field effects are
included directly in the evaluation of the dielectric response.

The derivative with respect to $\mathbf{k}$ in the second equation enters via the polarization vector,
$\vec\beta_{n\mathbf k}$, which in the
[PAW
formalism](../methods/Projector-augmented-wave_formalism.md)
is given by

$|\vec{\beta}_{n\mathbf{k}}\rangle= \left(
1+\sum_{ij} |\tilde{p}_{i\mathbf{k}}\rangle Q_{ij}
\langle\tilde{p}_{j\mathbf{k}}| \right) |\partial_\mathbf{k}
\tilde{u}_{n\mathbf{k}}\rangle+ i\left( \sum_{ij}
|\tilde{p}_{i\mathbf{k}}\rangle Q_{ij}
(\mathbf{r}-\mathbf{R}_i)-\vec{\tau}_{ij}
\langle\tilde{p}_{j\mathbf{k}}|
\right)|\tilde{u}_{n\mathbf{k}}\rangle,$

where $Q_{ij}$ and
$\vec\tau_{ij}$ are the norm and the
dipole moments of the one-center charge densities, each respectively
expressed as

$Q_{ij} = \int_{\Omega_\text{PAW}} \left\[
\phi_i(\mathbf{r}) \phi_j(\mathbf{r}) - \tilde{\phi}_i(\mathbf{r})
\tilde{\phi}_j(\mathbf{r}) \right\] d^3 \mathbf{r}$

and

$\vec{\tau}_{ij} = \int_{\Omega_\text{PAW}}
(\mathbf{r}-\mathbf{R}_i) \left\[ \phi_i(\mathbf{r})
\phi_j(\mathbf{r}) - \tilde{\phi}_i(\mathbf{r})
\tilde{\phi}_j(\mathbf{r}) \right\] d^3 \mathbf{r}.$

For norm-conserving pseudopotentials the expression for
$|\vec{\beta}_{n\mathbf{k}}\rangle$ is
reduced to

$|\vec{\beta}_{n\mathbf{k}}\rangle=|\partial_\mathbf{k}
\tilde{u}_{n\mathbf{k}}\rangle.$

To employ the Sternheimer formalism you should set
[LEPSILON](../incar-tags/LEPSILON.md) = TRUE  in the
[INCAR](../input-files/INCAR.md) file. However, if you want to use the
instead of that of the [perturbation expansion after
discretisation](../incar-tags/LPEAD.md) formalism and finite differences of
an electric field you should use
[`LCALCEPS`](../incar-tags/LCALCEPS.md)` = .TRUE.`.

## Computation of physical quantities
After obtaining the derivatives of the Kohn-Sham orbitals with respect
to the electric field $|\partial_\mathcal{E_\alpha}\tilde{u}_{n\mathbf{k}} \rangle$, the dielectric tensor can then be computed using

$\epsilon^\infty(\hat{\mathbf{q}},0) =
1-\frac{8\pi e^2}{\Omega} \sum_{v\mathbf{k}} 2 w_\mathbf{k} \langle
\mathbf{\hat{q}}\vec{\beta}_{n\mathbf{k}} |
\partial_{\mathcal{E}_\alpha} \tilde{u}_{n\mathbf{k}} \rangle.$

Note that the sum runs over occupied states only! Meaning that very few
empty states are required in this calculation. The macroscopic
dielectric tensor is reported in the [OUTCAR](../output-files/OUTCAR.md) in
the field

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in DFT) 

By computing the the [forces](../methods/Category-Forces.md)
on each atom, $a$, for a given set of
perturbed KS orbitals it is also possible to obtain the Born effective
charges using

$Z^a_{ij}=\frac{\Omega}{e}\frac{\partial
P_i}{\partial u^a_j} =\frac{1}{e}\frac{\partial F^a_j}{\partial
\mathcal{E}_i} \approx\frac{1}{e}\frac{ \left(
\mathbf{F}\[\\\psi^{\mathcal{E}_i}_{\lambda/2}\\\]-
\mathbf{F}\[\\\psi^{\mathcal{E}_i}_{-\lambda/2}\\\]
\right)^a_j}{\lambda}.$

These are also reported in the [OUTCAR](../output-files/OUTCAR.md), after

    BORN EFFECTIVE CHARGES (in e, cummulative output) 

Finally, the ion-clamped piezoelectric tensor $\overline{e}_{ij}$ can be computed from the strain tensor,
$\mathbf{\sigma}\[\psi_{n\mathbf{k}}\]$, using

$\overline{e}_{ij} =-\frac{\partial
\sigma_j}{\partial \mathcal{E}_i} \approx -\frac{ \left(
\sigma\[\\\psi^{\mathcal{E}_i}_{\lambda/2}\\\]-
\sigma\[\\\psi^{\mathcal{E}_i}_{-\lambda/2}\\\] \right)_j }{\lambda},$

which can be found in

    PIEZOELECTRIC TENSOR for field in x, y, z (e Angst) 

### Ionic contributions
#### Piezoelectric tensor
The ionic contributions to the piezoelectric tensor can be computed by
setting [IBRION](../incar-tags/IBRION.md)=6, 8, and
[LEPSILON](../incar-tags/LEPSILON.md)=.TRUE. or
[LCALCEPS](../incar-tags/LCALCEPS.md) = TRUE  in the
[INCAR](../input-files/INCAR.md). This will correct the piezoelectric tensor
using

$e_{\alpha j} = \overline{e}_{\alpha j} +
\Omega_0^{-1}Z_{m\alpha}(\Phi)^{-1}_{mn}\Xi_{nj},$

where $\Phi_{mn}$ and
$\Xi_{nj}$ are the force constants and
force response to the internal strain tensors, respectively. The second
term on the right-hand side will be written to the
[OUTCAR](../output-files/OUTCAR.md) in

    PIEZOELECTRIC TENSOR IONIC CONTR  for field in x, y, z (C/m^2)

while the contributions from the ion-clamped tensor are written in

    PIEZOELECTRIC TENSOR (including local field effects) (e Angst)

#### Dielectric tensor
Setting the same tags in the [INCAR](../input-files/INCAR.md) as for the
corrected piezoelectric tensor, it is possible to compute the ionic
contributions to the dielectric tensor. These are given by

$\chi_{\alpha\beta} =
\overline{\chi_{\alpha\beta}} +
\Omega_0^{-1}Z_{m\alpha}(\Phi)^{-1}_{mn}Z_{n\beta}.$

The ionic contributions (second term on the right-hand side) are written
in the [OUTCAR](../output-files/OUTCAR.md) to

    MACROSCOPIC STATIC DIELECTRIC TENSOR IONIC CONTRIBUTION

while the ion-clamped tensor is written to

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects)

## Related tags and sections
[LEPSILON](../incar-tags/LEPSILON.md), [LRPA](../incar-tags/LRPA.md),
[LPEAD](../incar-tags/LPEAD.md), [Born effective
charges](../tutorials/Born_effective_charges.md)

## References
1.  [↑](#cite_ref-gajdos:prb:2006_1-0) [M. Gajdoš, K. Hummer, G.
    Kresse, J. Furthmüller, and F. Bechstedt, Phys. Rev. B **73**,
    045112 (2006).](https://doi.org/10.1103/PhysRevB.73.045112)

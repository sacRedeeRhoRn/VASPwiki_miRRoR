<!-- Source: https://vasp.at/wiki/index.php/Category:Forces | revid: 37124 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Forces


**Forces** on particles describe the interactions that cause particles,
such as atoms and molecules, to move and behave in specific ways. In
materials, forces result from electromagnetic interactions, which can be
computed by means of the [Hellmann-Feynman
theorem](../theory/Hellmann-Feynman_forces.md) within
density-functional theory (DFT), the [random-phase approximation
(RPA)](ACFDT__RPA_calculations.md) or by the
use of [machine-learned force fields
(MLFF)](Machine_learning_force_field-_Theory.md),
also refered to as machine-learned potentials. Understanding forces
between atoms is crucial in many aspects of material science, for
example:

- predicting the atomic structure of solids and molecules ([structure
  optimization](../tutorials/Structure_optimization.md))
- chemical reactions, catalysis, etc.
  (<a href="/wiki/Transition_states" class="mw-redirect"
  title="Transition states">transition states</a>)
- thermodynamic processes
  (<a href="/wiki/MD" class="mw-redirect" title="MD">molecular dynamics</a>)

For a classical particle, Newton's second law of motion states that the
change of motion of an object is proportional to the force acting on the
object and oriented in the same direction as the force vector
\$\mathbf{F}(t)\$. Therefore, the force is defined as the change of
particle momentum with time

$\mathbf{F}(t) = m\frac{d\mathbf{v}(t)}{d t} = m\mathbf{a}(t),$

where $\mathbf{a}(t)$ is the acceleration of the particle. Here, the
velocity is defined as the change of position with time \$\mathbf{v}(t)
= \frac{d\mathbf{r}(t)}{dt}\$, $\mathbf{r}(t)$ is the position of the particle, and the momentum
$\mathbf{p}(t)$ of the particle is the velocity times
the particle mass $m$:
$\mathbf{p}(t) = m\mathbf{v}(t).$

|  |
|----|
| **Mind:** With this equation of motion, the knowledge of some starting conditions $\mathbf{r}(0)$ and $\mathbf{v}(0)$ and an algorithm to compute the forces $\mathbf{F}$ the trajectory $\mathbf{r}(t)$ of a particle can be predicted for all times. |

Moreover, one can directly relate the force and the negative gradient of
the potential energy. The gradient of the potential energy can be
computed from the Lagrangian of the particle system of interest. The
Lagrangian for an N particle system is

$L=
\sum_{i=1}^{N}m_{i}\mathbf{v}^{2}_{i} - V(\\\mathbf{r}_{i}\\),$

where $V(\\\mathbf{r}_{i}\\)$ is the potential energy of the system. Using
Lagrange's equation of the second kind$\frac{d}{dt}\frac{\partial
L}{\partial \mathbf{v}_{i}}=\frac{\partial L}{\partial \mathbf{r}_{i}}$ yields the relation

$\mathbf{F}_{i} = -\frac{\partial V(\\\mathbf{r}_{i}\\)}{\partial
\mathbf{r}_{i}} = -\nabla V(\\\mathbf{r}_{i}\\).$

|  |
|----|
| **Mind:** To obtain forces and particle trajectories, the negative gradient of the potential energy has to be computed. |


## Contents


- [1 DFT
  forces](#dft-forces)
- [2 RPA
  forces](#rpa-forces)
- [3
  Machine-learned
  forces](#machine-learned-forces)
- [4 Applying
  external forces](#applying-external-forces)
- [5 Related
  concepts](#related-concepts)
  - [5.1 Stress and
    pressure](#stress-and-pressure)
  - [5.2
    Force-constant matrix and
    phonons](#force-constant-matrix-and-phonons)
- [6
  References](#references)


## DFT forces\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: DFT forces">edit</a> \| (./index.php.md)\]

One way to compute the potential energy's negative gradient is through
DFT. In DFT there is no classical potential energy function
$V(\\\mathbf{r}_{i}\\)$ but a Hamiltonian
$\mathcal{H}$ depending on the ionic positions
$\mathbf{R}_{i}$ and the electronic positions
$\mathbf{r}_{i}$. The total energy is given by

$E_{tot} = -\frac{1}{2}\int \sum_{i}\psi_{i}^{\*}({\bf
r})\nabla^{2}\psi_{i}({\bf r}) d{\bf r} - \int
\sum_{A}\frac{Z_{A}}{\left\vert{\bf r}-{\bf R}_{A}\right\vert}n({\bf
r})d{\bf r} + \int \int \frac{1}{2}\frac{n({\bf r})n({\bf
r'})}{\left\vert{\bf r}-{\bf r'}\right\vert} d{\bf r'}d{\bf r}+ E_{\rm
xc} + \frac{1}{2}\sum_{A\ne B}\frac{Z_{A}Z_{B}}{\left\vert{\bf
R}_{A}-{\bf R}_{B}\right\vert},$

where $n(\mathbf{r})$ denotes the electronic ground-state density and
$\psi_{i}$ are the Kohn-Sham orbitals.
$E_{\rm xc}$ is the exchange-correlation energy. To
obtain the force acting on ion A, the Hellmann-Feynman theorem has to be
used.

$\mathbf{F}_{A}=-\nabla_{A}
E_{tot}=\nabla_{A}\sum_{A}\int\frac{Z_{A}}{\left\vert{\bf r}-{\bf
R}_{A}\right\vert}n({\bf r})d^{3}r -\nabla_{A}\frac{1}{2}\sum_{A\ne
B}\frac{Z_{A}Z_{B}}{\left\vert{\bf R}_{A}-{\bf R}_{B}\right\vert},$

where $\nabla_{A}$
denotes the gradient with respect to ionic position
$\mathbf{R}_{A}$. The DFT forces will depend on the
chosen [exchange-correlation
functional](../categories/Category-Exchange-correlation_functionals.md)
via the electronic ground-state density $n({\bf r})$.
Therefore, the choice of the proper exchange-correlation functional for
the system of interest is crucial for obtaining proper forces and,
hence, the correct material properties.

## RPA forces\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: RPA forces">edit</a> \| (./index.php.md)\]

The [RPA](ACFDT__RPA_calculations.md) can be
used to yield estimates for the [exchange-correlation
energy](../categories/Category-Exchange-correlation_functionals.md)
as well as forces ([LRPAFORCE](../incar-tags/LRPAFORCE.md)) within
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>.[^ramberger:prl:118-1]
Note that the RPA is a correction to the underlying functional.
Therefore, the choice of the proper [exchange-correlation
functional](../categories/Category-Exchange-correlation_functionals.md)
is still crucial in the RPA approach for obtaining forces.

|  |
|----|
| **Tip:** It is recommended to use the Perdew-Burke-Ernzerhof (PBE) XC potential, i.e., [XC](../incar-tags/XC.md) = PE . |

The RPA forces are computed by the following equation

$\mathbf{F}_{A}=-Tr\[\rho^{(1)}\nabla_{A}V^{KS}-\gamma^{(1)}\nabla_{A}S\]$

The operators $\rho^{1}$ and
$\gamma^{1}$ are associated with the functional
derivatives $\delta E/\delta V^{KS}$ and $\delta E/\delta S$ respectively. S defines the overlap operator between
the Kohn-Sham orbitals of the used DFT approximation. The first term of
the force equation can be associated with the exchange energy and the
second term of the equation can be associated with the correlation part.

|  |
|----|
| **Mind:** It is recommended to use the <a
href="/wiki/Available_PAW_potentials#Recommended_potentials_for_GW/RPA_calculations"
class="mw-redirect" title="Available PAW potentials">GW POTCAR-files</a>. |

- [ACFDT/RPA
  calculations](ACFDT__RPA_calculations.md)

## Machine-learned forces\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Machine-learned forces">edit</a> \| (./index.php.md)\]

A speedy but less accurate approach for obtaining forces is through a
<a href="/wiki/MLFF" class="mw-redirect" title="MLFF">machine-learned
force field (MLFF)</a>. In this approach, a machine-learning model is
first trained on either the DFT or RPA forces, whereby also energies and
stresses are considered. In the case of the RPA, the stress tensor is
not computed. The machine-learning approach will be an approximation to
the underlying method against which it was fitted.

The MLFF approach is based on decomposing the total DFT energy into
local atomic contributions $E_{B}(\\\mathbf{R}_{C}\\)$ depending on all atomic positions in the system.
Therefore, the force acting on ion A is computed by

$\mathbf{F}_{A} =
-\nabla_{A}\sum_{B=1}^{N}E_{B}(\\\mathbf{R}_{C}\\)=-\sum_{B}^{N}w_{B}\frac{dK_{B}(\\\mathbf{R}_{C}\\)}{d\mathbf{R}_{A}},$

where $K(\mathbf{R}_{C})$ is the kernel matrix which can be found on the
[machine learning theory
page](Machine_learning_force_field-_Theory.md).
The kernel matrix as the local energies depends on the positions of all
atoms $\\\mathbf{R}_{C}\\$ in the actual atomic configuration.

- [Machine learning
  Basics](Machine_learning_force_field_calculations-_Basics.md)
- [Machine learning best
  practice](Best_practices_for_machine-learned_force_fields.md)

It is possible to **apply external machine-learned models** during a
VASP run using the Python-[plugins](../tutorials/Plugins.md) feature.
Please consult [our dedicated How-To page on
uMLFFs](Running_universal_machine-learned_force_fields.md)
for examples on how to directly supply a machine-learned potential or
any other model expressed in terms of an
<a href="https://wiki.fysik.dtu.dk/ase/development/calculators.html"
class="external text" rel="nofollow">ASE Calculator</a>.

## Applying external forces\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Applying external forces">edit</a> \| (./index.php.md)\]

There are multiple ways to run simulations with effective forces acting
on the ions. This includes
<a href="/wiki/Selective_dynamics" class="mw-redirect"
title="Selective dynamics">selective dynamics</a> defined in the
[POSCAR](../input-files/POSCAR.md) file, the
[LATTICE_CONSTRAINTS](../incar-tags/LATTICE_CONSTRAINTS.md)
tag and the [ICONST](../input-files/ICONST.md) file. To apply static
driving forces in a closer sense, the [EFOR](../incar-tags/EFOR.md) tag
offers direct control. Additionally it is possible to apply dynamically
changing forces and stress using the
Python-[plugins](../tutorials/Plugins.md) feature. In particular, the
[PLUGINS/FORCE_AND_STRESS](../incar-tags/PLUGINS__FORCE_AND_STRESS.md)
tag in combination with an appropriate Python script yields direct
control at each ionic step.

|  |
|----|
| **Tip:** Depending on the method, an overall **drift** may be removed from the forces. See [\#DFT forces](#dft-forces) For instance, for [structure optimization](../tutorials/Structure_optimization.md) and for the [Nosé-Hoover thermostat](../tutorials/Nosé-Hoover_thermostat.md) drifts are removed, but not for the stochastic [Langevin thermostat](../tutorials/Langevin_thermostat.md). |

## Related concepts\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related concepts">edit</a> \| (./index.php.md)\]

### Stress and pressure\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Stress and pressure">edit</a> \| (./index.php.md)\]

The stress tensor (see [ISIF](../incar-tags/ISIF.md)) provides valuable
information about how forces are distributed throughout a material, both
in magnitude and direction. It includes normal stresses, which act
perpendicular to a given plane, and shear stresses, which act parallel
to the plane. Together, these components allow predicting how materials
will behave under various conditions, such as tension, compression, or
shear. The stress tensor can be computed from a viral theorem, including
pair forces, or with a finite difference approach deforming the
simulation box.

Pressure, often denoted as P, is a scalar component of the stress
tensor. It represents the normal force per unit area acting on a surface
within the material. In the stress tensor, pressure is related to the
diagonal components $\sigma_{xx}$, $\sigma_{yy}$, and $\sigma_{zz}$:

$P
= \frac{1}{3}(\sigma_{xx} + \sigma_{yy} + \sigma_{zz}).$

In other words, the pressure is the average of the normal components of
the stress tensor in the three spatial directions. In electronic
structure calculations, finite basis sets are used to express the
electron density. Due to this finiteness of the basis set, errors on the
stress tensor and the pressure are introduced. The error in the pressure
is referred to as [Pulay stress](../tutorials/Pulay_stress.md) and
can be corrected with the tag [PSTRESS](../incar-tags/PSTRESS.md) or by
increasing [ENCUT](../incar-tags/ENCUT.md).

Related how-to pages:

- [Volume relaxation](Volume_relaxation.md)
- [NpT ensemble](../misc/NpT_ensemble.md)

### Force-constant matrix and phonons\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Force-constant matrix and phonons">edit</a> \| (./index.php.md)\]

The forces are defined as the negative gradient of the potential energy.
The **force-constant matrix** is defined by

$\Phi_{I\alpha J\beta} (\\\mathbf{R}^0\\) = \left. \frac{\partial
E(\\\mathbf{R}\\)}{\partial R_{I\alpha} \partial R_{J\beta}}
\right|_{\mathbf{R} =\mathbf{R^0}} = - \left. \frac{\partial
F_{I\alpha}(\\\mathbf{R}\\)}{\partial R_{J\beta}}
\right|_{\mathbf{R} =\mathbf{R^0}}$

and is, therefore, the gradient of the force. The force-constant matrix
is a fundamental concept in solid-state physics and materials science,
especially in the context of understanding the vibrational properties of
crystals, i.e.,
<a href="/wiki/Phonons" class="mw-redirect" title="Phonons">phonons</a>.
It is a generalization of the spring constant \$k\$ inside
(\$\mathbf{F}=k\mathbf{x}\$) for the case of 3D crystals. This matrix is
used to describe the relationships between atomic displacements and the
resulting forces that occur in a crystal. By Fourier transforming the
force-constant matrix, the [dynamical
matrix](../theory/Phonons-_Theory.md) is obtained.

By computing the eigenvalues of the dynamical matrix on various
reciprocal lattice points, the [phonon-dispersion
relation](../tutorials/Computing_the_phonon_dispersion_and_DOS.md)
can be obtained. Understanding
<a href="/wiki/Phonons" class="mw-redirect" title="Phonons">phonons</a>
is essential as they influence materials' properties directly, such as
lattice thermal conductivity and mechanical properties, as well as
indirectly via
<a href="/wiki/Electron-phonon_coupling" class="mw-redirect"
title="Electron-phonon coupling">electron-phonon coupling</a> that
provides access to [transport
properties](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
such as electrical conductivity, mobility, and electronic thermal
conductivity.

- [Phonons from finite
  differences](../tutorials/Phonons_from_finite_differences.md)
- [Phonons from density-functional-perturbation
  theory](../tutorials/Phonons_from_density-functional-perturbation_theory.md)
- [Computing the phonon dispersion and
  DOS](../tutorials/Computing_the_phonon_dispersion_and_DOS.md)

## References\[<a
href="/wiki/index.php?title=Category:Forces&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^ramberger:prl:118-1]: [B. Ramberger, T. Schäfer and G. Kresse, Phys. Rev. Lett **118**, 106403 (2017).](https://doi.org/10.1103/PhysRevLett.118.106403)

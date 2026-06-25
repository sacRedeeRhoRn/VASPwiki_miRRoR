<!-- Source: https://vasp.at/wiki/index.php/Thermodynamic_integration_calculations | revid: 36205 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Thermodynamic integration calculations


[Thermodynamic
integration](../theory/Thermodynamic_integration.md)
(TI) is an approach where two different calculations (e.g., different
k-point meshes, machine learning force fields vs. ab-initio) are run in
parallel with linear combination of the forces and stresses. This allows
controlled integration between the two, from a *reference* system to an
*interacting* system. The free energy of a fully interacting system can
be written as the sum of the free energy of a non-interacting reference
system and the difference in the free energy of the fully interacting
system and the non-interacting system

$F_{1} = F_{0} + \Delta F_{0\rightarrow 1}$.

Using thermodynamic integration the free energy difference between the
two systems is written as

$\Delta F_{0\rightarrow 1} = \int\limits_{0}^{1} d\lambda \langle
U_{1}(\lambda) - U_{0}(\lambda) \rangle_{\lambda}$.

Here $U_{1}(\lambda)$ and $U_{0}(\lambda)$ describe the potential energies of a fully-interacting
and a non-interacting reference system, respectively. The coupling
strength of the systems is controlled via the coupling parameter
$\lambda$. It is neccessary that the connection of the
two systems via the coupling constant is reversible. The notation
$\langle \ldots \rangle_{\lambda}$ denotes an ensemble
average of a system driven by the following classical Hamiltonian

$H_{\lambda}= \lambda H_{1} + (1-\lambda) H_{0}$.

VASP supports three approaches to [thermodynamic
integration](../theory/Thermodynamic_integration.md)
(TI):

- TI between any two states using
  [VCAIMAGES](../incar-tags/VCAIMAGES.md)<sup>[\[1\]](#cite_note-dorner:PRL:2018-1)</sup>.
- TI with a harmonic solid or ideal gas as a reference state using
  [SCALEE](../incar-tags/SCALEE.md)<sup>[\[1\]](#cite_note-dorner:PRL:2018-1)</sup>.
- TI with a harmonic solid as a reference state using
  [TILAMBDA](../incar-tags/TILAMBDA.md).

Details on choosing the ensemble size and how to perform the integration
are described in the main text and especially the supplementary
information of reference
<sup>[\[1\]](#cite_note-dorner:PRL:2018-1)</sup>.
**Caution:** the tag *ISPECIAL*=0 used in that reference is not valid
anymore, instead the tag
[PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md)=-1 is used.


## Contents


- [1 TI using
  VCAIMAGES](#ti-using-vcaimages)
- [2 TI using
  SCALEE](#ti-using-scalee)
  - [2.1 Available
    options for reference
    system](#available-options-for-reference-system)
- [3 TI using
  TILAMBDA](#ti-using-tilambda)
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


## TI using VCAIMAGES\[<a
href="/wiki/index.php?title=Thermodynamic_integration_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: TI using VCAIMAGES">edit</a> \| (./index.php.md)\]

**Main tags:**

- [VCAIMAGES](../incar-tags/VCAIMAGES.md)
- [NCORE_IN_IMAGE1](../incar-tags/NCORE_IN_IMAGE1.md).

**Directory structure:**

- A parent directory with two subdirectories: *01* and *02* (these
  represent two images).
- Subdirectories must contain identical [POSCAR](../input-files/POSCAR.md)
  files.
- Other files (e.g., [KPOINTS](../input-files/KPOINTS.md),
  [POTCAR](../input-files/POTCAR.md), etc.) can differ, enabling TI between
  distinct calculation setups (e.g., different k-point meshes, different
  potentials, machine learning force fields vs. ab-initio, etc.).
- The subdirectories should not contain [INCAR](../input-files/INCAR.md)
  files. Only the parent directory contains an
  [INCAR](../input-files/INCAR.md) file.
- To enable thermodynamic integration
  [VCAIMAGES](../incar-tags/VCAIMAGES.md) and
  [NCORE_IN_IMAGE1](../incar-tags/NCORE_IN_IMAGE1.md) need to be
  set.
- Parameters controlling atomic motion (e.g.,
  [IBRION](../incar-tags/IBRION.md), [ISIF](../incar-tags/ISIF.md),
  [POTIM](../incar-tags/POTIM.md), [MDALGO](../incar-tags/MDALGO.md) etc.)
  must be identical in both images and are set in the common region of
  the [INCAR](../input-files/INCAR.md) file.
- Force calculation parameters (e.g., ML vs. DFT, different functionals
  etc.) may differ and can be set for each image via
  [IMAGES](../incar-tags/IMAGES.md) blocks (i.e.,
  [IMAGE_1](../incar-tags/IMAGE_1.md),
  <a href="/wiki/IMAGE_2" class="mw-redirect" title="IMAGE 2">IMAGE_2</a>)
  in the [INCAR](../input-files/INCAR.md) file.

**How it works:**

- Similar to nudged elastic band calculations, multiple calculations are
  run (subdirectories *01* and *02*).
- The [VCAIMAGES](../incar-tags/VCAIMAGES.md) tag linearly combines the
  forces and stresses:
  - Weight for *01*: [VCAIMAGES](../incar-tags/VCAIMAGES.md)
  - Weight for *02*: 1 - [VCAIMAGES](../incar-tags/VCAIMAGES.md)
  - Thus, [VCAIMAGES](../incar-tags/VCAIMAGES.md) must be between 0 and
    1.
- [NCORE_IN_IMAGE1](../incar-tags/NCORE_IN_IMAGE1.md) sets the
  number of cores used for *01*; remaining cores are used for *02*.

**Example [INCAR](../input-files/INCAR.md):**

     # Thermodynamic integration
     VCAIMAGES = 0.75
     NCORE_IN_IMAGE1 = 8

     # Parameters for motion of atoms
     IBRION = 0
     ISYM   = 0
     POTIM  = 2.0
     TEBEG = 298.15
     TEEND = 298.15
     MDALGO = 3
     ISIF   = 3
     SMASS = 0
     NSW = 20

     # First image DFT
     IMAGE_1 {
     ENCUT = 400.0
     ISMEAR = 0
     EDIFF  = 1E-5
     }

     # Second image MLFF
     IMAGE_2 {
     ML_LMLFF = .TRUE.
     ML_MODE = run
     }

The following [INCAR](../input-files/INCAR.md) tags are forbidden inside an
[IMAGES](../incar-tags/IMAGES.md) block, as they must be the same for both
images:

    IBRION
    ISIF
    KBLOCK
    MDALGO
    ML_ESTBLOCK
    ML_IERR
    ML_OUTBLOCK
    NBLOCK
    NCORE_IN_IMAGE1
    NSW
    POTIM
    TEBEG
    TEEND

## TI using SCALEE\[<a
href="/wiki/index.php?title=Thermodynamic_integration_calculations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: TI using SCALEE">edit</a> \| (./index.php.md)\]

**Main tags:**

- [SCALEE](../incar-tags/SCALEE.md): Sets the coupling parameter
  $\lambda$ and determines the Hamiltonian used in the
  calculation.

**Directory structure:**

- Thermodynamic integration (TI) with [SCALEE](../incar-tags/SCALEE.md) is
  performed in a single directory.
- Optionally, the calculation can read the file
  [DYNMATFULL](../input-files/DYNMATFULL.md) if present (see details
  below).

**How it works:**

- The main control tag is [SCALEE](../incar-tags/SCALEE.md), which sets
  the coupling parameter $\lambda$
  and determines the Hamiltonian used in the calculation.

### Available options for reference system\[<a
href="/wiki/index.php?title=Thermodynamic_integration_calculations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Available options for reference system">edit</a> \| (./index.php.md)\]

**Ideal gas:** By default the thermodynamic integration is carried out
from the ideal gas to the fully interacting case (in the case when no
[DYNMATFULL](../input-files/DYNMATFULL.md) is present in the
calculation folder). Usually the Stirling approximation is used for the
free energy of the ideal gas written as

$F
= -\frac{1}{\beta} \mathrm{ln} \left\[ \frac{V^{N}}{\Alpha^{3N} N!}
\right\]$

where $V$ is the
volume of the system, $N$ is the
number of particles in the system and $\Alpha$ is
the de Broglie wavelength. The Stirling approximation applies in
principle only in the limes of infinitely many particles. In reference
<sup>[\[1\]](#cite_note-dorner:PRL:2018-1)</sup>
the exact ideal gas equation was used since it helped to speed up the
convergence of the final free energy of liquid Si with respect to the
system size.

**Harmonic solid:** If the file
[DYNMATFULL](../input-files/DYNMATFULL.md) exists in the calculation
directory and [SCALEE](../incar-tags/SCALEE.md)$\ne$1, the
second order Hessian matrix is added to the force and thermodynamic
integration from a harmonic model to a fully interacting system is
carried out. The [DYNMATFULL](../input-files/DYNMATFULL.md) file stores
the eigenmodes and eigenvalues from diagonalizing the dynamic matrix.
This file is written by a previous calculation using the
[INCAR](../input-files/INCAR.md) tags [IBRION](../incar-tags/IBRION.md)=6 and
[PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md)=-1. This calculation
runs in a single folder. It optionally reads in a
[DYNMATFULL](../input-files/DYNMATFULL.md) file in the calculation
directory (for more details see below). The tag
[SCALEE](../incar-tags/SCALEE.md) sets the coupling parameter
$\lambda$ and hence controls the Hamiltonian of the
calculation. By default [SCALEE](../incar-tags/SCALEE.md)=1 and the
scaling of the energies and forces via the coupling constant is
internally skipped in the code. To enable the scaling
[`SCALEE`](../incar-tags/SCALEE.md)` < 1` has to be specified.

## TI using TILAMBDA\[<a
href="/wiki/index.php?title=Thermodynamic_integration_calculations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: TI using TILAMBDA">edit</a> \| (./index.php.md)\]

**Main tags:**

- [TILAMBDA](../incar-tags/TILAMBDA.md): Sets the value for the coupling
  parameter $\lambda$.

**Directory structure:**

- Thermodynamic integration (TI) with
  [TILAMBDA](../incar-tags/TILAMBDA.md) is performed in a single
  directory.
- Internal coordinates for the TI calculation are defined in the
  [ICONST](../input-files/ICONST.md) file, with the status set to 3.
- The Hessian matrix in Cartesian coordinates,
  $\mathbf{\underline{H}}^\mathbf{x}$, must be provided
  in the [HESSEMAT](../incar-tags/HESSEMAT.md) file. The calculation
  automatically transforms this matrix to internal coordinates,
  $\mathbf{\underline{H}}^\mathbf{q}$.

**How it works:**

- The potential energies for both systems (system 1 and system 0) are
  computed in the internal coordinate representation,
  $\mathbf{q}$.
- These values are used to evaluate the integrand
  $\langle V_1 - V_{0,\mathbf{q}} \rangle$ in the TI
  expression $\Delta F_{0,\mathbf{q}
  \rightarrow 1}$.
- The TI calculations are performed in the [NVT
  ensemble](../misc/NVT_ensemble.md) using any available
  [thermostat](../categories/Category-Thermostats.md).

**Output:**

- The required energies are written in the
  [REPORT](../output-files/REPORT.md) file. Look for lines beginning with
  the string `e_ti>`.

## Related tags and articles\[<a
href="/wiki/index.php?title=Thermodynamic_integration_calculations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VCAIMAGES](../incar-tags/VCAIMAGES.md),
[NCORE_IN_IMAGE1](../incar-tags/NCORE_IN_IMAGE1.md),
<a href="/wiki/IMAGE_N" class="mw-redirect" title="IMAGE N">IMAGE_N</a>,
[SCALEE](../incar-tags/SCALEE.md),
[DYNMATFULL](../input-files/DYNMATFULL.md),
[PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md),
[TILAMBDA](../incar-tags/TILAMBDA.md),
[HESSEMAT](../incar-tags/HESSEMAT.md), [ICONST](../input-files/ICONST.md),
[REPORT](../output-files/REPORT.md)

[Thermodynamic
integration](../theory/Thermodynamic_integration.md)

## References\[<a
href="/wiki/index.php?title=Thermodynamic_integration_calculations&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-dorner:PRL:2018_1-0)</sup>
    <sup>[b](#cite_ref-dorner:PRL:2018_1-1)</sup>
    <sup>[c](#cite_ref-dorner:PRL:2018_1-2)</sup>
    <sup>[d](#cite_ref-dorner:PRL:2018_1-3)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.121.195701"
    class="external text" rel="nofollow">F. Dorner, Z. Sukurma, C. Dellago,
    and G. Kresse, Phys. Rev. Lett. <strong>121</strong>, 195701 (2018).</a>



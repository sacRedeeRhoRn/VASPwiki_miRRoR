<!-- Source: https://vasp.at/wiki/index.php/Category:Linear_response | revid: 35521 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Linear response
Apart from ground-state properties, VASP can compute how a system reacts
to external perturbations. Currently, we can consider three types of
perturbations:

1.  external electric field
2.  atomic displacements
3.  homogeneous strains

If we restrict ourselves to the first order of the perturbation then we
are in the linear regime and thus we talk about linear response. A
central quantity in linear response is the [dielectric
function](Category-Dielectric_properties.md)
which relates an external electric field with the internal electric
displacement. The response to atomic displacements includes
[phonons](Category-Phonons.md) and
[electron-phonon
interactions](Category-Electron-phonon_interactions.md).
The response to homogeneous strains is used to compute the elastic
tensor and piezoelectric tensor when combined with a response to an
external electric field.

## Contents

- [1 Polarization, berry phases, and finite electric
  fields](#Polarization,_berry_phases,_and_finite_electric_fields)
- [2 Static response](#Static_response)
  - [2.1 Dielectric tensor](#Dielectric_tensor)
  - [2.2 Born effective charges](#Born_effective_charges)
  - [2.3 Piezolectric tensor](#Piezolectric_tensor)
  - [2.4 Elastic tensor](#Elastic_tensor)
  - [2.5 Internal strain tensor](#Internal_strain_tensor)
- [3 Dynamic response](#Dynamic_response)
- [4 X-ray absorption spectroscopy
  (XAS)](#X-ray_absorption_spectroscopy_(XAS))
- [5 Nuclear magnetic resonance
  (NMR)](#Nuclear_magnetic_resonance_(NMR))
- [6 Additional resources](#Additional_resources)
  - [6.1 How to](#How_to)
  - [6.2 Lectures](#Lectures)
  - [6.3 Tutorials](#Tutorials)

## Polarization, berry phases, and finite electric fields
The polarization in a periodic system can be computed using the [berry
phase formulation of the
polarization](../theory/Berry_phases_and_finite_electric_fields.md)
(often referred to as the modern theory of polarization). With a method
to compute the polarization, we can apply a [finite electric
field](../theory/Berry_phases_and_finite_electric_fields.md)
to the system. Strictly speaking, polarization, as well as the
application of a finite electric field, are ground-state properties,
however, because they can be used to compute the static dielectric
tensor, born effective charges, and piezoelectric tensors which are
response properties, we refer to this approach here.

## Static response
We consider separately static and dynamic responses for perturbations
that are constant or change over time. The different static responses
can be understood as [derivatives of the total energy with respect to
the different external
perturbations](../theory/Static_linear_response-_theory.md).

### Dielectric tensor
The static dielectric tensor can be computed by finite differences
[LCALCEPS](../incar-tags/LCALCEPS.md) of the polarization with respect
to a finite external electric field or by using density functional
perturbation theory [LEPSILON](../incar-tags/LEPSILON.md). Both
[LEPSILON](../incar-tags/LEPSILON.md) or
[LCALCEPS](../incar-tags/LCALCEPS.md) yield the same converged results
for the dielectric tensor, however, the former can only be used for
local or semi-local exchange-correlation functionals and applies to both
semiconductors and metals while the second can be used for
[METAGGA](../incar-tags/METAGGA.md) or
[hybrid](../methods/Category-Hybrid_functionals.md)
but [only for systems with a gap](../incar-tags/EFIELD_PEAD.md).

### Born effective charges
There are two approaches to compute Born effective charges implemented
in VASP: one is done by applying [finite electric
fields](../theory/Berry_phases_and_finite_electric_fields.md)
along the three cartesian directions and computing the forces on the
atoms which are activated using [LCALCEPS](../incar-tags/LCALCEPS.md) or
by computing the derivating of the wavefunction with respect to an
electric field using [density functional perturbation
theory](../theory/Electric_field_response_from_density-functional-perturbation_theory.md)
(DFPT) using [LEPSILON](../incar-tags/LEPSILON.md).

### Piezolectric tensor
The piezoelectric tensor can be computed by finite differences with
respect to a [finite electric
field](../theory/Berry_phases_and_finite_electric_fields.md)
using [LCALCEPS](../incar-tags/LCALCEPS.md) or by using DFPT with
[LEPSILON](../incar-tags/LEPSILON.md) in combination with
[`IBRION`](../incar-tags/IBRION.md)` = 5,6 or 7,8`.

### Elastic tensor
The elastic tensor is computed using strain finite differences using
[`IBRION`](../incar-tags/IBRION.md)` = 5,6` in combination with
[`ISIF`](../incar-tags/ISIF.md)` = 3`. It is not possible to compute it
using [`IBRION`](../incar-tags/IBRION.md)` = 7,8` because the strain
perturbation is not implemented in DFPT.

### Internal strain tensor
The internal strain tensor can be computed using finite differences
using [`IBRION`](../incar-tags/IBRION.md)` = 5,6` or DFPT using
[`IBRION`](../incar-tags/IBRION.md)` = 7,8`.

## Dynamic response
There are [different
approaches](Category-Dielectric_properties.md)
and levels of theory implemented in VASP to compute the
frequency-dependent dielectric tensor. The simplest of these is done
using the Green-kubo formula and is activated using
[LOPTICS](../incar-tags/LOPTICS.md). This however neglects local-field
effects which means that it only reproduces calculations from DFPT or
finite differences of a [finite
electric](../theory/Berry_phases_and_finite_electric_fields.md)
field when [`LRPA`](../incar-tags/LRPA.md)` = .TRUE.` when the frequency is
zero (static limit). To include local field effects one should use
[`ALGO`](../incar-tags/ALGO.md)` = CHI`. Additionally one can include
electron-hole interaction when computing the dielectric function using
the Bethe-Salpeter equation in the many-body perturbation theory
framework using [`ALGO`](../incar-tags/ALGO.md)` = BSE`.

## X-ray absorption spectroscopy (XAS)
Another case of interest is the absorption of electromagnetic radiation
by core electrons as measured experimentally in [X-ray absorption
spectroscopy (XAS)](Category-XAS.md). The absorption
spectra can be found from the imaginary part of the frequency-dependent
dielectric function. Two methods for calculating XAS are available in
VASP: the supercell core-hole (SCH) method and the Bethe-Salpeter
equation (BSE). Both methods are capable of including the excitonic
effects in the spectra. In SCH these effects are included at the DFT
level, while the BSE approach relies on the many-body perturbation
theory. A comparison of the two approaches is given in the [XAS category
page](Category-XAS.md).

## Nuclear magnetic resonance (NMR)
[Nuclear magnetic resonance](Category-NMR.md) is a
widely used spectroscopy technique used to probe the structure and
chemical composition of molecules and solids. VASP can compute [chemical
shifts](../incar-tags/LCHIMAG.md) which is the ratio between the external
and induced magnetic field compared to a reference compound, [hyperfine
tensors](../incar-tags/LHYPERFINE.md) and [electric field
gradients](Category-NMR.md).

## Additional resources
### How to
- [XAS from the supercell core-hole
  method](../redirects/SCH_calculations.md)
- [XAS from the Bethe-Salpeter
  equation](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md)

### Lectures
- Lecture on [dielectric properties from first
  principles](https://youtu.be/3YKJZHmcGhY).
- Lecture on nuclear magnetic resonance (NMR)
  [theory](https://youtu.be/CyALJ8Qb1yk) and
  [application](https://youtu.be/Jw8oFzh9Z3k).
- Lecture on [phonons](https://youtu.be/VhYEdKOlIws).
- Lecture on [linear response](https://youtu.be/0BRrAY6RrgU).

### Tutorials
- Tutorial for [static and frequency-dependent response
  calculations](https://www.vasp.at/tutorials/latest/response/part1).
- Tutorial for [SCH XAS
  calculations](https://www.vasp.at/tutorials/latest/xas/part1).
- Tutorial for [BSE XAS
  calculations](https://www.vasp.at/tutorials/latest/xas/part2).
- Tutorial for [chemical shielding
  calculations](https://www.vasp.at/tutorials/latest/nmr/part1).
- Tutorial for [coupling constants and two-center correction
  calculations](https://www.vasp.at/tutorials/latest/nmr/part2).
- Tutorial for [NICS and current
  calculations](https://www.vasp.at/tutorials/latest/nmr/part3).
- Tutorial for [phonon
  calculations](https://www.vasp.at/tutorials/latest/phonon/).

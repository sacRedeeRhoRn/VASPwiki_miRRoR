<!-- Source: https://vasp.at/wiki/index.php/Category:Many-body_perturbation_theory | revid: 35531 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Many-body perturbation theory


Treating the electron-electron interaction within **many-body
perturbation theory** includes screening and renormalization effects
beyond density-functional theory (DFT). It is based on the
Green's-function formalism and can be derived and visualized in terms of
a diagrammatic expansion of the electron interacting with other
electrons. Instead of describing electrons by means of Kohn-Sham (KS)
orbitals, the renormalized (or dressed) propagators yield quasiparticle
orbitals. Another area that can be discussed in the language of
many-body perturbation theory is
<a href="/wiki/Electron-phonon_coupling" class="mw-redirect"
title="Electron-phonon coupling">electron-phonon coupling</a>, which
treats the interaction between electronic and ionic degrees of freedom.


## Contents


- [1 Available
  methods](#available-methods)
  - [1.1
    Random-phase approximation
    (RPA)](#random-phase-approximation-rpa))
  - [1.2
    Constrained random-phase approximation
    (cRPA)](#constrained-random-phase-approximation-crpa))
  - [1.3 GW
    method](#gw-method)
  - [1.4
    Bethe-Salpeter equations
    (BSE)](#bethe-salpeter-equations-bse))
    - [1.4.1 X-ray
      absorption spectra](#x-ray-absorption-spectra)
  - [1.5
    Second-order Møller-Plesset perturbation
    theory
    (MP2)](#second-order-møller-plesset-perturbation-theory-mp2))
- [2
  References](#references)


## Available methods\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Available methods">edit</a> \| (./index.php.md)\]

### Random-phase approximation (RPA)\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Random-phase approximation (RPA)">edit</a> \| (./index.php.md)")\]

GW and RPA are post-DFT methods used to solve the many-body problem
approximately.

RPA stands for the random-phase approximation and is often used as a
synonym for the adiabatic connection fluctuation-dissipation theorem
(ACFDT). RPA/ACFDT provides access to the correlation energy of a system
and can be understood in terms of Feynman diagrams as an infinite sum of
all bubble diagrams, where excitonic effects (interactions between
electrons and holes) are neglected. The RPA/ACFDT is used as a
post-processing tool to determine a more accurate ground-state energy.

- [RPA/ACFDT: Correlation energy in the Random Phase
  Approximation](../methods/RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md)
  — theory
- [ACFDT/RPA
  calculations](../methods/ACFDT__RPA_calculations.md) —
  practical guide
- Lecture on
  <a href="https://youtu.be/0hV5bTpY89M" class="external text"
  rel="nofollow">RPA</a>.

### Constrained random-phase approximation (cRPA)\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Constrained random-phase approximation (cRPA)">edit</a> \| (./index.php.md)")\]

The constrained random-phase approximation (cRPA) is a method that
allows calculating the effective interaction parameter
$U$, $J$ and
$J'$ for model Hamiltonians. The main idea is to neglect
the screening effects of specific target states in the screened Coulomb
interaction $W$ of the
$GW$ method. Usually, the target space is low-dimensional
(up to 5 states) and therefore allows for the application of a
higher-level theory, such as dynamical-mean-field theory (DMFT).

- [Formalism used for the cRPA
  method](../theory/Constrained–random-phase–approximation_formalism.md)

### GW method\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: GW method">edit</a> \| (./index.php.md)\]

The GW approximation goes hand in hand with the RPA since the very same
diagrammatic contributions are taken into account in the screened
Coulomb interaction of a system often denoted as W. However, in contrast
to the RPA/ACFDT, the GW method provides access to the spectral
properties of the system by means of determining the energies of the
quasiparticles using a screened exchange-like contribution to the
self-energy. The GW approximation is currently one of the most accurate
many-body methods to calculate bandgaps.

- <a href="/wiki/The_GW_approximation_of_Hedin%27s_equations"
  class="mw-redirect"
  title="The GW approximation of Hedin&#39;s equations">The GW
  approximation of Hedin's equations</a> — theory
- [Practical guide to GW
  calculations](../methods/Practical_guide_to_GW_calculations.md)
  — practical guide
- [GW and dielectric
  matrix](../methods/GW_and_dielectric_matrix.md)
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/gw/" class="external text"
  rel="nofollow">GW calculations</a>
- Lecture on
  <a href="https://youtu.be/zGPqDxsD80o" class="external text"
  rel="nofollow">GW</a>
- Lecture on the
  <a href="https://youtu.be/6F_WNIh6V7I" class="external text"
  rel="nofollow">optical bandgap</a>, including using many-body
  perturbation theory (GW and RPA)

### Bethe-Salpeter equations (BSE)\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Bethe-Salpeter equations (BSE)">edit</a> \| (./index.php.md)")\]

VASP offers a powerful module for solving time-dependent DFT (TD-DFT)
and time-dependent Hartree-Fock equations (TDHF) (the Casida equation)
or the Bethe-Salpeter (BSE)
equation[^albrecht:prl:98-1][^rohlfing:prl:98-2].
These approaches are used for obtaining the frequency-dependent
dielectric function with excitonic effects and can be based on the
ground-state electronic structure in the DFT, hybrid-functional, or
[GW](../methods/Practical_guide_to_GW_calculations.md)
approximations. VASP also offers the TDHF and BSE calculations beyond
the Tamm-Dancoff approximation
(TDA)[^sander:prb:15-3].

- [Bethe-Salpeter
  equations](../theory/Category-Bethe-Salpeter_equations.md)
  — all tags and articles
- <a href="/wiki/BSE_calculations" class="mw-redirect"
  title="BSE calculations">BSE calculations</a> — practical guide
- Tutorial for <a href="https://www.vasp.at/tutorials/latest/bse/"
  class="external text" rel="nofollow">BSE calculations</a>
- Lecture on
  <a href="https://youtu.be/arTPHW28qNM" class="external text"
  rel="nofollow">BSE</a>

#### X-ray absorption spectra\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: X-ray absorption spectra">edit</a> \| (./index.php.md)\]

The BSE/TDHF algorithm can also be used to model the X-ray absorption
spectra (XAS), i.e., excitations from the core states into conduction
bands. Detailed documentation of this method can be found in the [XAS
category page](Category-XAS.md).

- Tutorials for <a href="https://www.vasp.at/tutorials/latest/xas/"
  class="external text" rel="nofollow">XAS calculations</a>

### Second-order Møller-Plesset perturbation theory (MP2)\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Second-order Møller-Plesset perturbation theory (MP2)">edit</a> \| (./index.php.md)")\]

There are three implementations available:

- **MP2**
  [^paier:2009-4]:
  this implementation is recommended for very small unit cells, very few
  k-points and very low plane-wave cutoffs. The system size scaling of
  this algorithm is N⁵.
- **LTMP2**[^schaefer:2017-5]:
  for all larger systems this Laplace-transformed MP2 (LTMP2)
  implementation is recommended. Larger cutoffs and denser k-point
  meshes can be used. It possesses a lower system size scaling (N⁴) and
  a more efficient k-point sampling.
- **stochastic
  LTMP2**[^schaefer:2018-6]:
  even faster calculations at the price of statistical noise can be
  achieved with the stochastic MP2 algorithm. It is an optimal choice
  for very large systems where only relative errors per valence electron
  are relevant. Keeping the absolute error fixed, the algorithm exhibits
  a cubic scaling with the system size, N³, whereas for a fixed relative
  error, a linear scaling, N¹, can be achieved. Note that there is no
  k-point sampling and no spin polarization implemented for this
  algorithm.

<!-- -->

- [MP2 ground state calculation -
  Tutorial](../tutorials/MP2_ground_state_calculation_-_Tutorial.md)

## References\[<a
href="/wiki/index.php?title=Category:Many-body_perturbation_theory&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^albrecht:prl:98-1]: [S. Albrecht, L. Reining, R. Del Sole, and G. Onida, Phys. Rev. Lett. **80**, 4510-4513 (1998).](https://doi.org/10.1103/PhysRevLett.80.4510)
[^rohlfing:prl:98-2]: [M. Rohlfing and S. G. Louie, Phys. Rev. Lett. **81**, 2312-2315 (1998).](https://doi.org/10.1103/PhysRevLett.81.2312)
[^sander:prb:15-3]: [T. Sander, E. Maggio, and G. Kresse, *Beyond the Tamm-Dancoff approximation for extended systems using exact diagonalization*, Phys. Rev. B **92**, 045209 (2015).](https://doi.org/10.1103/PhysRevB.92.045209)
[^paier:2009-4]: [M. Marsman, A. Grüneis, J. Paier, G. Kresse, J. Chem. Phys. **130**, 184103 (2009).](https://doi.org/10.1063/1.3126249)
[^schaefer:2017-5]: [T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys. **146**, 104101 (2017).](https://doi.org/10.1063/1.4976937)
[^schaefer:2018-6]: [T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys. **148**, 064103 (2018).](https://doi.org/10.1063/1.5016100)

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
many-body perturbation theory is [electron-phonon
coupling](../redirects/Electron-phonon_coupling.md),
which treats the interaction between electronic and ionic degrees of
freedom.

## Contents

- [1 Available methods](#Available_methods)
  - [1.1 Random-phase approximation
    (RPA)](#Random-phase_approximation_(RPA))
  - [1.2 Constrained random-phase approximation
    (cRPA)](#Constrained_random-phase_approximation_(cRPA))
  - [1.3 GW method](#GW_method)
  - [1.4 Bethe-Salpeter equations
    (BSE)](#Bethe-Salpeter_equations_(BSE))
    - [1.4.1 X-ray absorption spectra](#X-ray_absorption_spectra)
  - [1.5 Second-order Møller-Plesset perturbation theory
    (MP2)](#Second-order_Møller-Plesset_perturbation_theory_(MP2))
- [2 References](#References)

## Available methods
### Random-phase approximation (RPA)
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
- Lecture on [RPA](https://youtu.be/0hV5bTpY89M).

### Constrained random-phase approximation (cRPA)
The constrained random-phase approximation (cRPA) is a method that
allows calculating the effective interaction parameter
$U$, $J$
and $J'$ for model Hamiltonians. The
main idea is to neglect the screening effects of specific target states
in the screened Coulomb interaction $W$
of the $GW$ method. Usually, the target
space is low-dimensional (up to 5 states) and therefore allows for the
application of a higher-level theory, such as dynamical-mean-field
theory (DMFT).

- [Formalism used for the cRPA
  method](../theory/Constrained–random-phase–approximation_formalism.md)

### GW method
The GW approximation goes hand in hand with the RPA since the very same
diagrammatic contributions are taken into account in the screened
Coulomb interaction of a system often denoted as W. However, in contrast
to the RPA/ACFDT, the GW method provides access to the spectral
properties of the system by means of determining the energies of the
quasiparticles using a screened exchange-like contribution to the
self-energy. The GW approximation is currently one of the most accurate
many-body methods to calculate bandgaps.

- [The GW approximation of Hedin's
  equations](../redirects/The_GW_approximation_of_Hedin's_equations.md)
  — theory
- [Practical guide to GW
  calculations](../methods/Practical_guide_to_GW_calculations.md)
  — practical guide
- [GW and dielectric
  matrix](../methods/GW_and_dielectric_matrix.md)
- Tutorial for [GW
  calculations](https://www.vasp.at/tutorials/latest/gw/)
- Lecture on [GW](https://youtu.be/zGPqDxsD80o)
- Lecture on the [optical bandgap](https://youtu.be/6F_WNIh6V7I),
  including using many-body perturbation theory (GW and RPA)

### Bethe-Salpeter equations (BSE)
VASP offers a powerful module for solving time-dependent DFT (TD-DFT)
and time-dependent Hartree-Fock equations (TDHF) (the Casida equation)
or the Bethe-Salpeter (BSE)
equation^([\[1\]](#cite_note-albrecht:prl:98-1)[\[2\]](#cite_note-rohlfing:prl:98-2)).
These approaches are used for obtaining the frequency-dependent
dielectric function with excitonic effects and can be based on the
ground-state electronic structure in the DFT, hybrid-functional, or
[GW](../methods/Practical_guide_to_GW_calculations.md)
approximations. VASP also offers the TDHF and BSE calculations beyond
the Tamm-Dancoff approximation
(TDA)^([\[3\]](#cite_note-sander:prb:15-3)).

- [Bethe-Salpeter
  equations](../theory/Category-Bethe-Salpeter_equations.md)
  — all tags and articles
- [BSE calculations](../redirects/BSE_calculations.md) —
  practical guide
- Tutorial for [BSE
  calculations](https://www.vasp.at/tutorials/latest/bse/)
- Lecture on [BSE](https://youtu.be/arTPHW28qNM)

#### X-ray absorption spectra
The BSE/TDHF algorithm can also be used to model the X-ray absorption
spectra (XAS), i.e., excitations from the core states into conduction
bands. Detailed documentation of this method can be found in the [XAS
category page](Category-XAS.md).

- Tutorials for [XAS
  calculations](https://www.vasp.at/tutorials/latest/xas/)

### Second-order Møller-Plesset perturbation theory (MP2)
There are three implementations available:

- **MP2** ^([\[4\]](#cite_note-paier:2009-4)): this implementation is
  recommended for very small unit cells, very few k-points and very low
  plane-wave cutoffs. The system size scaling of this algorithm is N⁵.
- **LTMP2**^([\[5\]](#cite_note-schaefer:2017-5)): for all larger
  systems this Laplace-transformed MP2 (LTMP2) implementation is
  recommended. Larger cutoffs and denser k-point meshes can be used. It
  possesses a lower system size scaling (N⁴) and a more efficient
  k-point sampling.
- **stochastic LTMP2**^([\[6\]](#cite_note-schaefer:2018-6)): even
  faster calculations at the price of statistical noise can be achieved
  with the stochastic MP2 algorithm. It is an optimal choice for very
  large systems where only relative errors per valence electron are
  relevant. Keeping the absolute error fixed, the algorithm exhibits a
  cubic scaling with the system size, N³, whereas for a fixed relative
  error, a linear scaling, N¹, can be achieved. Note that there is no
  k-point sampling and no spin polarization implemented for this
  algorithm.

&nbsp;

- [MP2 ground state calculation -
  Tutorial](../tutorials/MP2_ground_state_calculation_-_Tutorial.md)

## References
1.  [↑](#cite_ref-albrecht:prl:98_1-0) [S. Albrecht, L. Reining, R. Del
    Sole, and G. Onida, Phys. Rev. Lett. **80**, 4510-4513
    (1998).](https://doi.org/10.1103/PhysRevLett.80.4510)
2.  [↑](#cite_ref-rohlfing:prl:98_2-0) [M. Rohlfing and S. G. Louie,
    Phys. Rev. Lett. **81**, 2312-2315
    (1998).](https://doi.org/10.1103/PhysRevLett.81.2312)
3.  [↑](#cite_ref-sander:prb:15_3-0) [T. Sander, E. Maggio, and G.
    Kresse, *Beyond the Tamm-Dancoff approximation for extended systems
    using exact diagonalization*, Phys. Rev. B **92**, 045209
    (2015).](https://doi.org/10.1103/PhysRevB.92.045209)
4.  [↑](#cite_ref-paier:2009_4-0) [M. Marsman, A. Grüneis, J. Paier, G.
    Kresse, J. Chem. Phys. **130**, 184103
    (2009).](https://doi.org/10.1063/1.3126249)
5.  [↑](#cite_ref-schaefer:2017_5-0) [T. Schäfer, B. Ramberger, and G.
    Kresse, J. Chem. Phys. **146**, 104101
    (2017).](https://doi.org/10.1063/1.4976937)
6.  [↑](#cite_ref-schaefer:2018_6-0) [T. Schäfer, B. Ramberger, and G.
    Kresse, J. Chem. Phys. **148**, 064103
    (2018).](https://doi.org/10.1063/1.5016100)

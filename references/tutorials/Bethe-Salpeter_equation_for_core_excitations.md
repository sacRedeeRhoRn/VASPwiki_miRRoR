<!-- Source: https://vasp.at/wiki/index.php/Bethe-Salpeter_equation_for_core_excitations | revid: 33486 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bethe-Salpeter equation for core excitations
VASP offers two approaches for calculating the X-ray Absorption Spectra
(XAS). The [supercell core-hole (SCH)](../redirects/XAS_theory.md)
method and the Bethe-Salpeter equation (BSE). As discussed in detail on
the [theory
page](../theory/Bethe-Salpeter_equation.md), within
the BSE approach the electron-hole interaction or the excitonic effects
are explicitly included in the dielectric function. The screening of the
electron-hole interaction is described in the random phase approximation
(RPA) and the Green's functions are calculated in the [GW
approximation](../methods/GW_approximation_of_Hedin's_equations.md).
This BSE+GW approach represents the state of the art for XAS spectra
calculations in solids.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

## Contents

- [1 Solving Bethe-Salpeter equation](#Solving_Bethe-Salpeter_equation)
- [2 Recommendations and advice](#Recommendations_and_advice)
  - [2.1 BSE solvers](#BSE_solvers)
  - [2.2 Processing the results](#Processing_the_results)
  - [2.3 Core exciton wavefunction](#Core_exciton_wavefunction)
  - [2.4 Beyond Tamm-Dancoff
    approximation](#Beyond_Tamm-Dancoff_approximation)
  - [2.5 Model BSE and TDDFT](#Model_BSE_and_TDDFT)
- [3 Comparing to the SCH](#Comparing_to_the_SCH)
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

## Solving Bethe-Salpeter equation
The BSE calculations for core excitaions, similarly to BSE in the
optical region, require a preceding [$GW$
calculation](/wiki/Practical_guide_to_GW_calculations "Practical guide to GW calculations").
In addition to the standard VASP input files, the following files are
needed to perform a BSE calculation:

- [WAVECAR](../input-files/WAVECAR.md) the quasiparticle energies and
  orbitals produced in the preceding $GW$ calculation
- [Wxxxx.tmp](../input-files/Wxxxx.tmp.md) the RPA dielectric matrix
  from the preceding $GW$ calculation
- [WAVEDER](../input-files/WAVEDER.md)\* the orbital derivatives from the
  $GW$ step, only required if the
  valence states are included

The quasiparticle energies are only calculated for the valence and
conduction bands set by [NBANDSGW](../incar-tags/NBANDSGW.md), the
energies of the core states are taken from the potentials in the
[POTCAR](../input-files/POTCAR.md) file. Hence, the absolute values for the
core excitations are not accurate, but the overall shape and the
relative positions of the spectral feature can be captured with high
precision within BSE
^([\[1\]](#cite_note-unzog:prb:2022-1)[\[2\]](#cite_note-karsai:prb:2018-2)).

The BSE calculation workflow consists of the following steps:

1.  DFT calculation with a large number of empty states
2.  $GW$ calculation to obtain the
    quasiparticles and the RPA dielectric tensor
3.  BSE calculation

Below you will find an example of the [INCAR](../input-files/INCAR.md) file
required for an XAS calculation in BSE.

    NBANDS     = 64      ! same as in GW calculation
    ISMEAR     = 0       ! Gaussian smearing
    SIGMA      = 0.05    ! rather small to avoid fractional occupations
    ALGO       = BSE     ! BSE algorithm
    NBANDSO    = 0       ! zero valence states 
    NBANDSV    = 16      ! number of empty bands
    ICORELEVEL = 2       ! enables the core states calculation
    CLNT       = 1       ! species of the excited atom
    CLN        = 0       ! main quantum number of the excited core state
    CLL        = 0       ! orbital quantum number of the excited core state

|  |
|----|
| **Mind:** The core states in VASP remain frozen in the configuration for which the PAW potential was generated. |

The intensities of the core state excitations can be too small for a
correct representation with the four decimal places used in the standard
output, thus VASP provides a tag that can be used to scale the
dielectric function and the oscillator strengths by a factor
[CH_AMPLIFICATION](../incar-tags/CH_AMPLIFICATION.md). All atoms
of the selected type [CLNT](../incar-tags/CLNT.md) are excited in the BSE
calculation, therefore, it is recommended to treat the excited atom as a
separate species in the [POSCAR](../input-files/POSCAR.md) file. It is
possible to excite multiple atoms in BSE, but it increases the number of
core states, i.e., the size of the problem, and it should be done only
if the atoms are not equivalent in the atomic configuration. The valence
states are usually not included in the XAS calculations, i.e.,
[NBANDSO](../incar-tags/NBANDSO.md)=0. Nevertheless, the valence states
can be included in BSE via tag [NBANDSO](../incar-tags/NBANDSO.md).

## Recommendations and advice
General advice for running BSE calculations can be found in this
[article](Best_practices_for_Bethe-Salpeter_calculations.md).
Specific advice for using the BSE to calculate the XAS as given below.

### BSE solvers
The default option for solving BSE is the exact diagonalization
algorithm with [IBSE](../incar-tags/IBSE.md)=2, which is the most accurate
but also most time-consuming method. Approximate solvers can yield
accurate spectra at a fraction of the computational time. The most
efficient approach is the iterative Lanczos algorithm, which can be
selected with [IBSE](../incar-tags/IBSE.md)=3. The time-evolution algorithm
([IBSE](../incar-tags/IBSE.md)=1) can be used in the XAS calculations, but
it is less efficient for spectra with a wide energy range as in the case
of XANES. Both approximate solvers can only be used to obtain the
spectra, but cannot be used to calculated the BSE eigenvectors.

### Processing the results
The calculated dielectric function and the oscillator strength
information can be found in
[vasprun.xml](../output-files/Vasprun.xml.md) and
[vaspout.h5](../output-files/Vaspout.h5.md).

### Core exciton wavefunction
The excitons can be visualized in VASP as described in this
[article](../theory/Plotting_exciton_wavefunction.md).
In the case of XAS, the core state is strongly localized and only the
hole position can be fixed by providing the coordinate of the excited
atom via the [BSEHOLE](../incar-tags/BSEHOLE.md) tag.

### Beyond Tamm-Dancoff approximation
The default approximation for the BSE algorithm is the Tamm-Dancoff
approximation (TDA), i.e., [ANTIRES](../incar-tags/ANTIRES.md)=0, which
usually holds for XAS. Nevertheless, the full BSE equation without TDA
can be solved by setting [ANTIRES](../incar-tags/ANTIRES.md)=2.

### Model BSE and TDDFT
The dielectric function for the core states can be calculated with the
model BSE approach or the Casida TDDFT formalism by selecting the
algorithm [ALGO](../incar-tags/ALGO.md)=TDHF. However, these approximations
were found inaccurate for XANES ^([\[1\]](#cite_note-unzog:prb:2022-1)).

## Comparing to the SCH
The spectra from the SCH calculation in the initial state approximation
and the BSE calculation in the independent particle approximation (IP)
can be directly compared and should be identical. The initial state
approximation can be selected in SCH by setting
[ICORELEVEL](../incar-tags/ICORELEVEL.md)=1. The independent particle
approximation (IP) can be selected in BSE by disabling both the bare and
screened Coulomb interaction, i.e.,
[LADDER](../incar-tags/LADDER.md)=.FALSE. and
[LHARTREE](../incar-tags/LHARTREE.md)=.FALSE..

## Related tags and articles
[ALGO](../incar-tags/ALGO.md), [LADDER](../incar-tags/LADDER.md),
[LHARTREE](../incar-tags/LHARTREE.md),
[NBANDSV](../incar-tags/NBANDSV.md), [NBANDSO](../incar-tags/NBANDSO.md),
[OMEGAMAX](../incar-tags/OMEGAMAX.md),
[ANTIRES](../incar-tags/ANTIRES.md), [NBSEEIG](../incar-tags/NBSEEIG.md),
[BSEHOLE](../incar-tags/BSEHOLE.md), [CLNT](../incar-tags/CLNT.md),
[CLL](../incar-tags/CLL.md), [CLN](../incar-tags/CLN.md),
[ICORELEVEL](../incar-tags/ICORELEVEL.md),
[BSEFATBAND](../output-files/BSEFATBAND.md)

## References
1.  ↑ ^([a](#cite_ref-unzog:prb:2022_1-0))
    ^([b](#cite_ref-unzog:prb:2022_1-1)) [M. Unzog, A. Tal, G. Kresse,
    *X-ray absorption using the projector augmented-wave method and the
    Bethe-Salpeter equation*, Phys. Rev. B **106**, 155133
    (2022).](http://doi.org/10.1103/PhysRevB.106.155133)
2.  [↑](#cite_ref-karsai:prb:2018_2-0) [F. Karsai, M. Humer, E.
    Flage-Larsen, P. Blaha, and G. Kresse, Phys. Rev. B **98**, 235205
    (2018).](https://doi.org/10.1103/PhysRevB.98.235205)

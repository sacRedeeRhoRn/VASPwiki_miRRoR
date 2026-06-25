<!-- Source: https://vasp.at/wiki/index.php/Bandgap_renormalization_due_to_electron-phonon_coupling | revid: 33357 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bandgap renormalization due to electron-phonon coupling


The band-structure renormalization within the nonadiabatic Allen Heine
Cardona (AHC) theory is computed from the real part of the electron
self-energy evaluated at the Kohn-Sham (KS) eigenvalue. This calculation
is activated by default when
[`ELPH_RUN`](../incar-tags/ELPH_RUN.md)` = True` and
[`ELPH_DRIVER`](../incar-tags/ELPH_DRIVER.md)` = EL`. For the
particular case where we want to determine the bandgap, we can compute
the self-energy only for the states that form the gap (including all the
degenerate states). The selection of these states can be done
automatically by VASP using
[`ELPH_SELFEN_GAPS`](../incar-tags/ELPH_SELFEN_GAPS.md)` = True`.

For the theory on bandgap renormalization from perturbation theory, see
the many-body perturbation theory section of the [theory
page](../theory/Electron-phonon_interactions_theory.md).

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

|  |
|----|
| **Important:** This feature requires [HDF5 support](../categories/Category-HDF5_support.md). |

|  |
|----|
| **Warning:** There was a [known issue](../misc/Known_issues.md) for electron-phonon calculations using [`ISPIN`](../incar-tags/ISPIN.md)` = 2` for VASP 6.5.0 and 6.5.1 that was fixed in VASP 6.6.0. |

|  |
|----|
| **Tip:** The phonon-induced renormalization of the fundamental gap can alternatively be calculated from a [stochastic approach](Electron-phonon_interactions_from_Monte-Carlo_sampling.md). |


## Contents


- [1 Basic
  usage](#basic-usage)
- [2 Basis set
  convergence](#basis-set-convergence)
- [3 K-point
  sampling convergence and extrapolation to
  infinity](#k-point-sampling-convergence-and-extrapolation-to-infinity)
- [4 Special
  treatment of the dipole interaction for polar
  materials](#special-treatment-of-the-dipole-interaction-for-polar-materials)
- [5 Related tags
  and articles](#related-tags-and-articles)


## Basic usage\[<a
href="/wiki/index.php?title=Bandgap_renormalization_due_to_electron-phonon_coupling&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Basic usage">edit</a> \| (./index.php.md)\]

The first step of an electron-phonon calculation is the [computation of
the electron-phonon
potential](Electron-phonon_potential_from_supercells.md),
which corresponds to the derivatives of the KS potential with ionic
displacement. This calculation produces the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file, which is a required input for the subsequent calculation. The
electron-phonon matrix elements are computed using the KS states
obtained from a non-self-consistent-field calculation on a dense k-point
mesh. This k-point mesh is specified in the
[KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md) file, which has the
same format as the regular [KPOINTS](../input-files/KPOINTS.md) file. Note
that [NBANDS](../incar-tags/NBANDS.md) governs the number of bands used in
the self-consistent-field calculation, while
[ELPH_NBANDS](../incar-tags/ELPH_NBANDS.md) governs the number of
bands that will be used in the electron-phonon calculation and are
computed in the grid specified via
[KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md).

The computation of the electronic bandgap renormalization can be done
using the following [INCAR](../input-files/INCAR.md) file:

     PREC = Accurate
     ENCUT = 500
     EDIFF = 1e-8
     ISMEAR = 0; SIGMA = 0.01
     LREAL = .FALSE.
     LWAVE = .FALSE.
     LCHARG = .FALSE.
     
     #run electron-phonon calculation
     ELPH_RUN = .TRUE.
     ELPH_DRIVER = EL
     
     # use exact diagonalization and compute all the bands
     ELPH_NBANDS = -2
     KPOINTS_OPT_MODE = 2
     
     # compute gap renormalization
     ELPH_SELFEN_DELTA = 0.01
     ELPH_SELFEN_FAN = .TRUE.
     ELPH_SELFEN_DW = .TRUE.
     ELPH_SELFEN_GAPS = .TRUE.

  

|  |
|----|
| **Tip:** For your convenience, you can set [`ELPH_MODE`](../incar-tags/ELPH_MODE.md)` = renorm`, which automatically sets reasonable values for many of these electron-phonon tags to perform the band-gap renormalization. It is still possible to manually overwrite the chosen values. |

To get an accurate value while using the smallest possible amount of
computational resources, we recommend performing a basis set and k-point
sampling convergence study. This ensures that the result is precise,
provides an error estimate and reveals the computationally most
favorable settings.

The final output of the code is reported for each combination of
computational parameters using the concept of [electron-phonon
accumulators](../misc/Electron-phonon_accumulators.md).

## Basis set convergence\[<a
href="/wiki/index.php?title=Bandgap_renormalization_due_to_electron-phonon_coupling&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Basis set convergence">edit</a> \| (./index.php.md)\]

First, we will deal with convergence of the bandgap renormalization with
respect to the number of electronic states
([NBANDS](../incar-tags/NBANDS.md)) and plane-waves
([ENCUT](../incar-tags/ENCUT.md)). To avoid a more cumbersome
double-convergence with [ENCUT](../incar-tags/ENCUT.md) and
[ELPH_NBANDS](../incar-tags/ELPH_NBANDS.md) we recommend setting
[ELPH_NBANDS](../incar-tags/ELPH_NBANDS.md) to be equal to the
maximum number of plane-waves. This can be done automatically by setting
[`ELPH_NBANDS`](../incar-tags/ELPH_NBANDS.md)` = -2`.

The derivatives of the electron-phonon potential are contained in the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md) file
on a pre-selected grid ([NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md),
[NGZ](../incar-tags/NGZ.md)). This means that we should avoid running the
electron-phonon calculation with an [ENCUT](../incar-tags/ENCUT.md) that
would yield a set of [NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md) and
[NGZ](../incar-tags/NGZ.md) that is different from the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. We can, however, choose a smaller [ENCUT](../incar-tags/ENCUT.md) and
set [NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md) and
[NGZ](../incar-tags/NGZ.md) manually in the [INCAR](../input-files/INCAR.md) file
to be the same as the one in the
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
file. This allows running the calculation with different values of
[ENCUT](../incar-tags/ENCUT.md) and monitoring how that affects the final
value of the bandgap renormalization.

Let us consider an example calculation where the electron-phonon
potential was generated for Silicon with an
[`ENCUT`](../incar-tags/ENCUT.md)` = 500` which yields
[NGX](../incar-tags/NGX.md)=[NGY](../incar-tags/NGY.md)=[NGZ](../incar-tags/NGZ.md)=28
in the primitive cell. The values of [NGX](../incar-tags/NGX.md),
[NGY](../incar-tags/NGY.md) and [NGZ](../incar-tags/NGZ.md) chosen by VASP can be
monitored in the [OUTCAR](../output-files/OUTCAR.md) file. A convergence
study can be performed by running multiple calculations with
[ENCUT](../incar-tags/ENCUT.md)=200, then 300, then 400 and finally 500.
[`NGX`](../incar-tags/NGX.md)` = 28`, [`NGY`](../incar-tags/NGY.md)` = 28` and
[`NGZ`](../incar-tags/NGZ.md)` = 28` are set explicitly in the
[INCAR](../input-files/INCAR.md) file. You can verify that the calculations
with a lower cutoff run faster, highlighting the importance of
convergence tests for reaching a good compromise between accuracy and
computational time.

## K-point sampling convergence and extrapolation to infinity\[<a
href="/wiki/index.php?title=Bandgap_renormalization_due_to_electron-phonon_coupling&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: K-point sampling convergence and extrapolation to infinity">edit</a> \| (./index.php.md)\]

Apart from the convergence with respect to the basis set, one should
perform a convergence with respect to the k-point sampling. This step
implies running the calculation for increasingly dense k-point meshes
specified in the [KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md) file.
The convergence behavior with respect to k-points is mostly independent
of the convergence behavior with respect to the plane-wave basis.
Therefore, it is recommended to study both types of convergence
separately to save on time.

Furthermore, we recommend extrapolating the bandgap renormalization to
infinite k-point density. This is most easily accomplished by plotting
the value of the renormalization as a function of the inverse k-point
density. In addition to the k-point convergence, the broadening
parameter
[ELPH_SELFEN_DELTA](../incar-tags/ELPH_SELFEN_DELTA.md) should
be monitored as well. In principle, this parameter should be as small as
possible.

|  |
|----|
| **Warning:** Choosing [ELPH_SELFEN_DELTA](../incar-tags/ELPH_SELFEN_DELTA.md) too small might produce inaccurate results for numerical reasons. |

The usual approach is to extrapolate the result to zero broadening.

|  |
|----|
| **Tip:** Multiple values can be specified for [ELPH_SELFEN_DELTA](../incar-tags/ELPH_SELFEN_DELTA.md). VASP then computes the self-energy for each of these broadenings and reports the results in the [OUTCAR](../output-files/OUTCAR.md) and [vaspout.h5](../output-files/Vaspout.h5.md) files. For each value of the broadening, a new electron [self-energy accumulator](../misc/Electron-phonon_accumulators.md) is created with the corresponding settings and values reported in the [OUTCAR](../output-files/OUTCAR.md) file. This should help simplify the convergence study. |

## Special treatment of the dipole interaction for polar materials\[<a
href="/wiki/index.php?title=Bandgap_renormalization_due_to_electron-phonon_coupling&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Special treatment of the dipole interaction for polar materials">edit</a> \| (./index.php.md)\]

The convergence of the bandgap renormalization for polar materials (i.e.
materials with a gap and non-zero born-effective charges) is especially
challenging. This is because the electron-phonon potential diverges as
$q\rightarrow0$. This divergence is due to long-range
electrostatic interactions that are not screened by the electrons, as
would be the case for metals. In these cases, VASP can remove this
long-range component from the electron-phonon potential in the
supercell, Fourier interpolate it and add it back in the primitive cell.
The same [treatment is done for the interatomic force
constants](../theory/Phonons-_Theory.md) "Phonons: Theory").

To activate the long-range treatment, set the following
[INCAR](../input-files/INCAR.md) tags:

     ENCUTLR = 50
     ELPH_LR = 1
     IFC_LR = 1

  

|  |
|----|
| **Mind:** The long-range treatment is activated by default when the phelel_params.hdf5 file contains the dielectric tensor and born effective charges. |

|  |
|----|
| **Tip:** The value of [ENCUTLR](../incar-tags/ENCUTLR.md) should be the smallest possible for efficiency reasons, but large enough such that the final quantity does not depend on it. Avoid values of [ENCUTLR](../incar-tags/ENCUTLR.md) that are too large, otherwise, the results might become unphysical. |

## Related tags and articles\[<a
href="/wiki/index.php?title=Bandgap_renormalization_due_to_electron-phonon_coupling&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](Transport_coefficients_including_electron-phonon_scattering.md)
- [Electron-phonon potential from
  supercells](Electron-phonon_potential_from_supercells.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md)
- [Electron-phonon interactions from Monte-Carlo
  sampling](Electron-phonon_interactions_from_Monte-Carlo_sampling.md)



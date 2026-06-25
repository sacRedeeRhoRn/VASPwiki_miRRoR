<!-- Source: https://vasp.at/wiki/index.php/Changelog | revid: 35747 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Changelog



## Contents


- [1
  6.6.0](#660)
  - [1.1
    FEATURE](#feature)
  - [1.2
    IMPROVEMENT](#improvement)
  - [1.3
    BUGFIX](#bugfix)
- [2
  6.5.1](#651)
  - [2.1
    FEATURE](#feature-2)
  - [2.2
    IMPROVEMENT](#improvement-2)
  - [2.3
    BUGFIX](#bugfix-2)
- [3
  6.5.0](#650)
  - [3.1
    FEATURE](#feature-3)
  - [3.2
    IMPROVEMENT](#improvement-3)
  - [3.3
    BUGFIX](#bugfix-3)
- [4
  6.4.3](#643)
  - [4.1
    FEATURE](#feature-3)
  - [4.2
    IMPROVEMENT](#improvement-3)
  - [4.3
    BUGFIX](#bugfix-3)


## 6.6.0\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: 6.6.0">edit</a> \| (./index.php.md)\]


### FEATURE\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: FEATURE">edit</a> \| (./index.php.md)\]

- [X-ray absorption
  spectra](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md)
  (XAS) using the Bethe-Salpeter equation (BSE).
  - Calculate [exciton
    wavefunction](../theory/Plotting_exciton_wavefunction.md)
    for core excitations.
- [Constrained random-phase
  approximation](../theory/Constrained–random-phase–approximation_formalism.md)
  (cRPA).
  - [spectral cRPA](../incar-tags/LSCRPA.md).
  - [multi-centre Coulomb matrix
    elements](../theory/Constrained–random-phase–approximation_formalism.md).
- Checkpointing of finite-difference calculations
  ([CHECKPOINT_FD](../incar-tags/CHECKPOINT_FD.md) when
  [`IBRION`](../incar-tags/IBRION.md)` = 6`)
  - [Restarting phonon
    calculations](../tutorials/Restarting_finite_differences_calculations.md).
  - [Splitting phonon
    calculations](../tutorials/Restarting_finite_differences_calculations.md).
  - Restarting and splitting calculations of the [electron-phonon
    potential](../tutorials/Electron-phonon_potential_from_supercells.md)
    ([ELPH_POT_GENERATE](../incar-tags/ELPH_POT_GENERATE.md)).
- [Electron-phonon](../categories/Category-Electron-phonon_interactions.md)
  - Computing electron-phonon matrix elements using
    [meta-GGAs](../incar-tags/METAGGA.md). 
  - Use reciprocal space for contraction when computing electron-phonon
    matrix elements.
  - Computing the transport properties in CRTA using Wannier
    interpolation.
- [Nuclear magnetic resonance](../categories/Category-NMR.md) (NMR)
  - Spin-orbit coupling for NMR chemical shieldings
    ([`LSOSHIFT`](../incar-tags/LSOSHIFT.md)` = .TRUE.`).
  - ZORA scalar-relativistic chemical shieldings
    ([`LZORA`](../incar-tags/LZORA.md)` = .TRUE.`).
  - Updated chemical shieldings output in
    [OUTCAR](../output-files/OUTCAR.md) (cf.
    [`LNMRLEG`](../incar-tags/LNMRLEG.md)` = .TRUE.`).
  - Print current response ([WRT_NMRCUR](../incar-tags/WRT_NMRCUR.md))
    and the nucleus-independent chemical shielding
    ([NUCIND](../incar-tags/NUCIND.md)).
  - Output to Magres format.
- [Bethe-Salpeter
  equation](../theory/Category-Bethe-Salpeter_equations.md)
  (BSE)
  - Adds Gaussian smearing option for Lanczos algorithm
    ([`IBSE`](../incar-tags/IBSE.md)` = 3`).
- GPU
  - OpenMP offloading for Intel and AMD GPUs: DFT and hybrid functionals
    (beta).
- [Exchange-correlation
  functionals](../categories/Category-Exchange-correlation_functionals.md)
  - [Short-range EXX](../incar-tags/BEXX.md) within [dielectric-dependent
    range-separated hybrid functionals](../incar-tags/LMODELHF.md),
    enabling RS-DDH.
  - Link to [simple DFT-D3](../methods/Simple-DFT-D3.md)
    package.
  - Support for [`LOPTICS`](../incar-tags/LOPTICS.md)` = .TRUE.` and
    kinetic-energy-density-dependent
    [meta-GGAs](../incar-tags/METAGGA.md).
- [Machine-learning force
  fields](../categories/Category-Machine-learned_force_fields.md)
  - Improved interface for [thermodynamic
    integration](../tutorials/Thermodynamic_integration_calculations.md)
    (TI).
  - Thermodynamic integration for particle insertion using MLFF and
    empirical potentials (ML_LEMPPOT, ML_EMPPOT_RCUT, ML_SRPOT_B0,
    ML_SRPOT_N0, ML_SRPOT_S0,ML_MOPOT_NM, ML_MOPOT_DM, ML_MOPOT_RM,
    ML_MOPOT_RKM, ML_MOPOT_IJM).
  - Add "delta" mode ([`ML_MODE`](../incar-tags/ML_MODE.md)` = delta`):
    always adding the prediction from a given
    [ML_FF](../input-files/ML_FF.md) to the ab initio calculation results.
  - Experimental support for [GRACE force
    fields](../methods/Running_GRACE_force_fields_in_VASP.md)
    in prediction-only mode (requires
    [VASPml](Makefile.include.md) "Makefile.include"),
    Tensorflow and cppflow).
- [HDF5](../categories/Category-HDF5_support.md)
  - Write phonon frequencies and eigenvectors to
    [vaspout.h5](../output-files/Vaspout.h5.md).
  - HDF5 output for cRPA calculations and GW electron self-energy.
  - Write exciton wavefunction to
    [vaspout.h5](../output-files/Vaspout.h5.md).
- Output
  - Write the metaGGA potential μ
    ([`WRT_POTENTIAL`](../incar-tags/WRT_POTENTIAL.md)` = xcmu`).
  - Write the augmented total (core + valence) pseudo densities
    (`WRT_DENSITY = density gradient laplacian`).
  - Write the kinetic energy density ([LTAU](../incar-tags/LTAU.md) and
    [TAUCAR](../input-files/TAUCAR.md) file).

### IMPROVEMENT\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: IMPROVEMENT">edit</a> \| (./index.php.md)\]

- [Electron-phonon](../categories/Category-Electron-phonon_interactions.md)
  - List of carrier density ranges in electron-phonon transport
    calculations
    ([ELPH_SELFEN_CARRIER_DEN_RANGE](../incar-tags/ELPH_SELFEN_CARRIER_DEN_RANGE.md)).
  - Reduced memory consumption in electron-phonon calculations.
- [Machine-learning force
  fields](../categories/Category-Machine-learned_force_fields.md)
  - New output in [ML_LOGFILE](../output-files/ML_LOGFILE.md):
    type-dependent output for various reported errors, [species
    quantities for
    forces](../output-files/ML_LOGFILE.md),
    and normalized errors for energies, forces and stress
    ([NORME](../output-files/ML_LOGFILE.md) lines).
  - Reduced memory footprint for
    [`ML_MODE`](../incar-tags/ML_MODE.md)` = train` with
    [`ML_CALGO`](../incar-tags/ML_CALGO.md)` = 1`.
  - Reduced memory footprint at the cost of fitting performance with
    ML_SAVECMAT = .FALSE. (experimental).
  - Improve default settings: shared memory behavior
    ([ML_NCSHMEM](../incar-tags/ML_NCSHMEM.md)), [spilling
    factor](../methods/Machine_learning_force_field-_Theory.md)
    switched always switched on, the calculation will end if the
    spilling factor becomes critically large (\>0.9), and
    [`ML_OUTBLOCK`](../incar-tags/ML_OUTBLOCK.md)` = 10`.
- [Many-body perturbation
  theory](../categories/Category-Many-body_perturbation_theory.md)
  - Added support for [NKRED](../incar-tags/NKRED.md) in RPA and GW
    (quartic scaling).
  - Improved RPA forces and EXX-energies in low-scaling GW calculations
    ([LFOCKSTD](../incar-tags/LFOCKSTD.md)).
  - Increased number of frequency points for the low-scaling GW (i.e.,
    [`NOMEGA`](../incar-tags/NOMEGA.md)` > 24`).
  - Support for fast EXX mode in RPA and GW.
  - Double-counting corrections for [RPA forces when using
    DFT+U](Known_issues.md).
  - Reduced memory usage in BSE calculations
  - Improved support for single precision BSE with Lanczos algorithm.
- Change parameters in semilocal functionals
  ([XCm_Pn](../incar-tags/XCm_Pn.md)).
- Greatly improved stability of noncollinear GGA and metaGGA
  calculations.
- Allowed the Ewald-cutoff parameter to be changed.
- Implement [KSPACING](../incar-tags/KSPACING.md) for
  [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file using
  KSPACING_OPT.
- New CMake build system as an alternative to the traditional
  makefile.include's. See [Install VASP with
  CMake](Installing_VASP.6.X.X.md)
  for instructions.

### BUGFIX\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: BUGFIX">edit</a> \| (./index.php.md)\]

- MD driven by [VASPml](../methods/VASPml_library.md) (inside
  VASP or LAMMPS) crashed if the number of MPI tasks was larger than the
  number of atoms.
- The use of the [SCPC
  method](Self-Consistent_Potential_Correction.md)
  was broken for [`ALGO`](../incar-tags/ALGO.md)` = A`.
- The
  [PLUGINS/LOCAL_POTENTIAL](../incar-tags/PLUGINS__LOCAL_POTENTIAL.md)
  energy contribution was not correctly added to the total energy for
  [`ALGO`](../incar-tags/ALGO.md)` ≠ Normal`.
- The eigenvalues of the dynamical matrix written to vaspout.h5 had the
  wrong sign.
- The use of symmetry was broken in
  [`ALGO`](../incar-tags/ALGO.md)` = TIMEEV`.
- The "selfen_carrier_per_cell" and "selfen_carrier_den" variables were
  swapped in the [vaspout.h5](../output-files/Vaspout.h5.md) file in the
  "/results/electron_phonon/electrons/chemical_potential" group.
- For these [INCAR](../input-files/INCAR.md) tags,
  [ELPH_SELFEN_CARRIER_DEN](../incar-tags/ELPH_SELFEN_CARRIER_DEN.md),
  [ELPH_SELFEN_CARRIER_PER_CELL](../incar-tags/ELPH_SELFEN_CARRIER_PER_CELL.md),
  or [ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md) in the
  electron-phonon driver only the first element was written to
  vasprun.xml or [vaspout.h5](../output-files/Vaspout.h5.md) file. 
- [RPA
  forces](../methods/ACFDT__RPA_calculations.md)
  for spin-polarized systems were wrong.
- Tamm-Dancoff was not working correctly when VASP was built with ELPA.
- Closing [vaspin.h5](../input-files/Vaspin.h5.md) in INIT_MPI broke the
  restart from HDF5 capability.
- [NBANDS](../incar-tags/NBANDS.md) was reduced if the net magnetic moment
  is negative.
- Setting the tag
  [ELPH_SELFEN_ENERGY_WINDOW](../incar-tags/ELPH_SELFEN_ENERGY_WINDOW.md)
  was not updating the values of
  [ELPH_SELFEN_BAND_START](../incar-tags/ELPH_SELFEN_BAND_START.md)
  and
  [ELPH_SELFEN_BAND_STOP](../incar-tags/ELPH_SELFEN_BAND_STOP.md)
  for the computation of the electron-phonon matrix elements.
- Correctly account for external electric field when determining
  symmetry operations using [EFIELD](../incar-tags/EFIELD.md) and
  [`IDIPOL`](../incar-tags/IDIPOL.md)` = 1-3`.
- [PROCAR_OPT](../output-files/PROCAR_OPT.md) was broken for VASP 6.5.0
  and 6.5.1.
- For very dense k-meshes, a crash could occur in the subroutine TETIRR,
  cf. the forum post
  (<a href="https://www.vasp.at/forum/viewtopic.php?t=19800"
  class="external free"
  rel="nofollow">https://www.vasp.at/forum/viewtopic.php?t=19800</a>).
- The ionic CG algorithm ([`IBRION`](../incar-tags/IBRION.md)` = 2`) for
  the Brent algorithm determined the bracketing interval improperly.
- Fixed
  [`I_CONSTRAINED_M`](../incar-tags/I_CONSTRAINED_M.md)` = .TRUE.`
  calculations on GPU, which crashed or produced wrong results.
- Fixed computation of mobilities for linear grids
  ([`ELPH_TRANSPORT_DRIVER`](../incar-tags/ELPH_TRANSPORT_DRIVER.md)` = 1`),
  the Onsager coefficients from the electron and hole resolved transport
  function were not computed.
- Fixed incorrect handling of spin channels in electron–phonon matrix
  element calculations for [`ISPIN`](../incar-tags/ISPIN.md)` = 2`, and
  optimized potential interpolation to process each spin channel
  separately.
- The zero-field-splitting
  ([`LDMATRIX`](../incar-tags/LDMATRIX.md)` = .TRUE.`) led to randomly
  wrong results, especially with the GNU compiler.
- Fix integer overflows resulting in errors or NaNs appearing in long MD
  runs (combinations of large [NSW](../incar-tags/NSW.md),
  [ML_OUTBLOCK](../incar-tags/ML_OUTBLOCK.md),
  [NBLOCK](../incar-tags/NBLOCK.md), [KBLOCK](../incar-tags/KBLOCK.md)
  values).
- With zero conductivity, NaN appeared for other transport coefficients,
  now instead they are set to zero.
- Fixed wrong formatting of partial DOS in
  [DOSCAR](../output-files/DOSCAR.md) when f-states are present in
  noncollinear runs. Previously, f-state contributions were written in a
  new line instead of using the columns after the d-states.
- Running DFPT for electric fields
  [`LEPSILON`](../incar-tags/LEPSILON.md)` = .TRUE.` or ionic
  displacements [`IBRION`](../incar-tags/IBRION.md)` = 7-8` was
  inadvertently blocked for deorbitalized
  [metaGGAs](../incar-tags/METAGGA.md).
- Update ionic positions for [CONTCAR](../output-files/CONTCAR.md),
  [XDATCAR](../output-files/XDATCAR.md), and
  [CHGCAR](../input-files/CHGCAR.md) during interactive mode
  ([`IBRION`](../incar-tags/IBRION.md)` = 11`).
- Order of electron eigenvalues if
  [`LDIAG`](../incar-tags/LDIAG.md)` = .FALSE.` between ionic steps was not
  conserved ([FERDO](../incar-tags/FERDO.md)).
- The exchange and correlation components of the BEEF functional
  ([`GGA`](../incar-tags/GGA.md)` = BF`) were not multiplied by the
  parameters [AGGAX](../incar-tags/AGGAX.md) and
  [AGGAC](../incar-tags/AGGAC.md).
- During a geometry relaxation, the new atomic positions and cell
  parameters were not passed to libMBD, cf.
  <a href="https://www.vasp.at/forum/viewtopic.php?t=20071"
  class="external free"
  rel="nofollow">https://www.vasp.at/forum/viewtopic.php?t=20071</a>.
- Fixed deadlock in [VCAIMAGES](../incar-tags/VCAIMAGES.md) runs caused
  by inconsistent [STOPCAR](../incar-tags/STOPCAR.md)-check MPI_allreduce
  calls between MLFF and pure-DFT images.
- If there was an empty [PENALTYPOT](../input-files/PENALTYPOT.md) file
  or none, the [HILLSPOT](../incar-tags/HILLSPOT.md) was not written
  from scratch.
- [`MDALGO`](../incar-tags/MDALGO.md)` = 5` was not interacting with the
  [PENALTYPOT](../input-files/PENALTYPOT.md) or
  [HILLSPOT](../incar-tags/HILLSPOT.md) file.
- \`spin = up\` and \`spin = down\` in the corresponding
  \`wannier90.X.win\` input files were not specified for spin-polarized
  calculations.
- Fixed [`ML_MODE`](../incar-tags/ML_MODE.md)` = select` when atom types
  for training structures were switched around.
- The [spilling
  factor](../methods/Machine_learning_force_field-_Theory.md)
  was calculated incorrectly in the fast prediction mode if the order of
  atom species in the current structure differed from that of the force
  field.
- An issue in [VCAIMAGES](../incar-tags/VCAIMAGES.md) where MLFF
  calculations in any of the images failed unless a non-empty
  [ML_FF](../input-files/ML_FF.md) file was also present in the top
  directory.
- Sign error in the surface-normal component of the reciprocal-space
  Ewald force and NaN for large vacuum spacing for 2D truncation
  ([`KERNEL_TRUNCATION/IDIMENSIONALITY`](../incar-tags/KERNEL_TRUNCATION__IDIMENSIONALITY.md)` = 2`).
- Fix the output for the electron-phonon renormalization of the gaps for
  [`ISPIN`](../incar-tags/ISPIN.md)` = 2`.
- Deprecate
  [PLUGINS/MACHINE_LEARNING](../incar-tags/PLUGINS__MACHINE_LEARNING.md)
  due to inconsistency between units for VASP and ASE stresses - use
  [PLUGINS/FORCE_AND_STRESS](../incar-tags/PLUGINS__FORCE_AND_STRESS.md)
  instead.
- Neighbor list for [DFT-D3](../methods/DFT-D3.md) was determined for a
  fixed radius (50.2 Å, and 21.167 Å; two-body interaction cutoff, and
  coordination number cutoff), so
  [VDW_RADIUS](../incar-tags/VDW_RADIUS.md) and
  [VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md) did not work
  correctly for values larger than these.
- [`ELPH_DRIVER`](../incar-tags/ELPH_DRIVER.md)` = mels` with
  [`ISPIN`](../incar-tags/ISPIN.md)` = 2` produced incorrect output due to
  improper k-point counter handling in the spin-dependent accumulator.
- The [POSCAR](../input-files/POSCAR.md) scaling parameters were not
  correctly read in from [vaspin.h5](../input-files/Vaspin.h5.md).
- Fix potential MPI deadlock when running with
  [`KPAR`](../incar-tags/KPAR.md)` > 1` by synchronizing SCF break/abort
  decisions across all ranks to avoid divergent control flow due to
  small roundoff differences in energy terms (e.g., Hartree) between
  [KPAR](../incar-tags/KPAR.md) groups.

## 6.5.1\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: 6.5.1">edit</a> \| (./index.php.md)\]


### FEATURE\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: FEATURE">edit</a> \| (./index.php.md)\]

- Added output of the imaginary part of the dielectric function from XAS
  calculations to vaspout.h5 (HDF5), and of the dielectric function with
  respect to the Fermi level to OUTCAR.

<!-- -->

- For
  [`ELPH_POT_GENERATE`](../incar-tags/ELPH_POT_GENERATE.md)` = True`:
  - The FFT grid for the primitive cell is now determined automatically
    if not set via
    [ELPH_POT_FFT_MESH](../incar-tags/ELPH_POT_FFT_MESH.md).
  - VASP generates a [CONTCAR_ELPH](../output-files/CONTCAR_ELPH.md)
    file that can be used for the subsequent electron-phonon
    calculation.
  - The primitive-cell information is also written to
    [vaspout.h5](../output-files/Vaspout.h5.md).

### IMPROVEMENT\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: IMPROVEMENT">edit</a> \| (./index.php.md)\]

- The line search algorithm of the conjugate gradient optimizer
  ([`ALGO`](../incar-tags/ALGO.md)` = A`) has been extensively improved:
  - previously, when performing the line search, it moved incremental
    along the line. The new version, always starts from the origin for
    each step during the line search this vastly increases the
    consistency of the energies.
  - The line search is now done in a more way and all considered steps
    are stored into slots to avoid unnecessary redundancy. For
    acceptance of the final minimum in the line search, it is required
    that the neighbouring slots have been considered (that first
    principles energies are known).
  - The minimum is determined by fitting up to a 4th order polynomial to
    the data closest to the minimum, and determining the minimum of the
    polynomial.
  - If more than 5 data are available, a spline fit is performed through
    all points (this turns out to be more robust than a 5th order fit).
  - Last not least: the line search is usually performed using energy
    evaluations only, as this is faster than gradient calculations.
    However, if the new gradient is not sufficiently orthogonal to the
    search direction, one more correction is performed using all yet
    available data points (again using 4th order polynomial or spline)
  - The new and improved line search algorithm can be switched on by
    setting [`ISEARCH`](../incar-tags/ISEARCH.md)` = 1`. The legacy line
    search ([`ISEARCH`](../incar-tags/ISEARCH.md)` = 0`) is still the
    default.

<!-- -->

- Improvements for BSE:
  - The dielectric function is written as a scalar (not tensor) for
    finite q in [`IBSE`](../incar-tags/IBSE.md)` = 1, 2, 3`.
  - Hermiticity of the BSE matrix is now enforced for
    [`IBSE`](../incar-tags/IBSE.md)` = 3` to improve stability.

<!-- -->

- Improved the performance of the Ewald summation used in the truncated
  Coulomb kernel method for 2D materials by restricting the number of
  g-vectors that are used in the reciprocal space summation. This
  truncation of g-vectors is in keeping with the 3D summation, where
  every value less than $10^{-10}$
  is removed.

### BUGFIX\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: BUGFIX">edit</a> \| (./index.php.md)\]

- Fixed the handling of “very long full paths of files” with the Intel
  compiler (these were truncated at 255 characters). Now we allow for
  1023 characters and hope this will be enough …

<!-- -->

- For [`ISYM`](../incar-tags/ISYM.md)` = 3`, symmetry operation involving
  spinflips were incorrect under some special fringe circumstances. This
  bug may have affected hybrid functional calculations for
  anti-ferromagnetic systems where the spin-up and spin-dn density of
  states differ from each other at some k-points.

<!-- -->

- Fixed a bug that prevented building without scaLAPACK support.

<!-- -->

- Fixed inconsistent ML_FF input/output for non-scaLAPACK build.

<!-- -->

- The code crashed for [`LKPROJ`](../incar-tags/LKPROJ.md)` = True`. This
  [issue](Known_issues.md) is fixed.

<!-- -->

- SERTA is now correctly listed as "self-energy relaxation-time
  approximation" in [OUTCAR](../output-files/OUTCAR.md).

<!-- -->

- The `wannier90.UNK` files were not correctly written for non-collinear
  magnetic calculations. This
  [issue](Known_issues.md) is fixed.

<!-- -->

- If both [`ISPIN`](../incar-tags/ISPIN.md)` = 2` and
  [`LNONCOLLINEAR`](../incar-tags/LNONCOLLINEAR.md)` = True` (or
  [`LSORBIT`](../incar-tags/LSORBIT.md)` = True`) were set in the INCAR,
  the code would stop with an error message (something about the number
  of entries for [MAGMOM](../incar-tags/MAGMOM.md) being wrong). This
  [issue](Known_issues.md) is fixed:
  [`LNONCOLLINEAR`](../incar-tags/LNONCOLLINEAR.md)` = True` will
  now take precedence over [`ISPIN`](../incar-tags/ISPIN.md)` = 2` (and the
  latter will default back to [`ISPIN`](../incar-tags/ISPIN.md)` = 1`
  internally).

<!-- -->

- Fixed a problem with the final diagonalization in the occupied
  subspace before the computation of the forces: this bug sometimes
  caused errors in the forces when the wave functions were not tightly
  converged, for [`ALGO`](../incar-tags/ALGO.md)` = A or D`.

<!-- -->

- BSE crashed on GPUs with `-DCUSOLVERMP` and `-DCUBLASMP` when
  [OMEGAMAX](../incar-tags/OMEGAMAX.md) was set. This
  [issue](Known_issues.md) is fixed.

<!-- -->

- The computation of the dielectric function was not correctly
  implemented for finite-q in [`IBSE`](../incar-tags/IBSE.md)` = 1,3`.

<!-- -->

- BSE crashed for [`IBSE`](../incar-tags/IBSE.md)` = 3` with the gamma-only
  version. This has been fixed.

<!-- -->

- [BSEPREC](../incar-tags/BSEPREC.md) was overwritten for
  [`IBSE`](../incar-tags/IBSE.md)` = 3`. This has been fixed.

<!-- -->

- The feature to compute the transport function using
  [ELPH_TRANSPORT_NEDOS_PLOT](../incar-tags/ELPH_TRANSPORT_NEDOS_PLOT.md)
  was broken. This has been fixed.

<!-- -->

- Electron-phonon code crashed for
  [`ELPH_MODE`](../incar-tags/ELPH_MODE.md)` = renorm`. This
  [issue](Known_issues.md) is fixed.

<!-- -->

- VASP no longer crashes when running
  [`ELPH_POT_GENERATE`](../incar-tags/ELPH_POT_GENERATE.md)` = True`
  without specifying the FFT grid via
  [ELPH_POT_FFT_MESH](../incar-tags/ELPH_POT_FFT_MESH.md).

<!-- -->

- The
  [LATTICE_CONSTRAINTS](../incar-tags/LATTICE_CONSTRAINTS.md)
  were not applied correctly for [`ISIF`](../incar-tags/ISIF.md)` = 4, 5`.
  This [issue](Known_issues.md) has been
  fixed.

<!-- -->

- For [`ISIF`](../incar-tags/ISIF.md)` = 4, 5, 6`, the header of the
  [XDATCAR](../output-files/XDATCAR.md) file was written twice. This has
  been fixed.

<!-- -->

- The truncated Coulomb kernel method for 2D systems only worked
  correctly if the cell was twice as large as the thickness of the slab.
  This requirement was imposed by the 2D Ewald summation, where minimum
  image convention was used in the aperiodic dimension. This requirement
  has now been removed by setting the distance between two atoms to not
  follow if the minimum image convention if it is 2D boundary
  conditions. This
  [issue](Known_issues.md) is fixed.

<!-- -->

- There was a (small) memory leak in the use of HDF5. This
  [issue](Known_issues.md) has been
  fixed.

<!-- -->

- In case the HF exchange was activated via the
  [LTHOMAS](../incar-tags/LTHOMAS.md) tag, VASP wrongly kept
  [`IMIX`](../incar-tags/IMIX.md)` = 4`. Now
  [`IMIX`](../incar-tags/IMIX.md)` = 1` is used.

<!-- -->

- The OpenACC version crashed when compiled with python plugin support
  (`-DPLUGINS,`). This
  [issue](Known_issues.md) is fixed and
  the python plugins are now fully supported in the OpenACC version as
  well.

<!-- -->

- For [`IBRION`](../incar-tags/IBRION.md)` = 12` or
  [`PLUGINS/STRUCTURE`](../incar-tags/PLUGINS__STRUCTURE.md)` = True`
  (i.e. using the python structure plugin) the updated structures were
  not written to [XDATCAR](../output-files/XDATCAR.md). This
  [issue](Known_issues.md) has been
  fixed.

<!-- -->

- The combination of
  [`PLUGINS/STRUCTURE`](../incar-tags/PLUGINS__STRUCTURE.md)` = True`
  and [`ML_MODE`](../incar-tags/ML_MODE.md)` = run` caused the code to
  crash. This [issue](Known_issues.md) is
  fixed.

<!-- -->

- [`ML_MODE`](../incar-tags/ML_MODE.md)` = train` was broken when running
  on multiple nodes *and* using shared memory (`-Duse_shmem`). This
  [issue](Known_issues.md) is fixed.

<!-- -->

- Fixed broken ML_FF version check in VASPml; was unable to read ML_FFs
  from VASP 6.5.0 (earlier versions work).

<!-- -->

- <a href="/wiki/ML_IERR" class="mw-redirect" title="ML IERR">ML_IERR</a>
  was deprecated in favor of new tag name
  [ML_ESTBLOCK](../incar-tags/ML_ESTBLOCK.md). This fixes "grepping"
  for `ERR` in [ML_LOGFILE](../output-files/ML_LOGFILE.md) (old tag
  still works).

<!-- -->

- The output of the total energy to the [OUTCAR](../output-files/OUTCAR.md)
  was wrong when running [`ML_MODE`](../incar-tags/ML_MODE.md)` = train`
  with [`ALGO`](../incar-tags/ALGO.md)` = A`. This
  [issue](Known_issues.md) issue has been
  fixed.

<!-- -->

- Fixed an incorrectly sized spline grid that sometimes led to wrong
  force predictions by VASPml.

## 6.5.0\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: 6.5.0">edit</a> \| (./index.php.md)\]


### FEATURE\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: FEATURE">edit</a> \| (./index.php.md)\]

- [Electron-phonon
  coupling](../categories/Category-Electron-phonon_interactions.md):
  - Zero-point [renormalisation of band
    gaps](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md).
  - [Transport
    coefficients](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
    within the framework of the linearized Boltzmann transport equation.
- [Python plugins](../tutorials/Plugins.md): Introduces a Python package
  that links VASP to Python through a C++ interface. A selected number
  of interfaces allow users to modify interior working of VASP through
  Python scripting.
- [Solving the Bethe-Salpeter
  equation](../theory/Category-Bethe-Salpeter_equations.md):
  - [Lanczos
    diagonalization](../theory/Category-Bethe-Salpeter_equations.md)
    of the BSE matrix ([IBSE](../incar-tags/IBSE.md)=3).
  - [GPU
    support](../theory/Category-Bethe-Salpeter_equations.md)
    for time-evolution BSE ([IBSE](../incar-tags/IBSE.md)=1).
- Additional [exchange-correlation
  functionals](../categories/Category-Exchange-correlation_functionals.md):
  - (r)MS-B86bl, (r)MS-PBEl and (r)MS-RPBEl
    [MGGA](../incar-tags/METAGGA.md) functionals (provided by Nick
    Gerrits).
  - TASK and LAK [MGGA](../incar-tags/METAGGA.md) functionals (provided
    by Timo Lebeda).
  - Sources-free exchange-correlation B field
    ([LSFBXC](../incar-tags/LSFBXC.md)).
- [Coulomb kernel
  truncation](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md):
  open boundary conditions to compute the properties of dipolar and
  charged molecules, 2D materials, and surfaces.
- [Machine-learned force
  fields](../categories/Category-Machine-learned_force_fields.md):
  - Introducing the [spilling
    factor](../methods/Best_practices_for_machine-learned_force_fields.md)
    as an error estimate of the force field with
    <a href="/wiki/ML_IERR" class="mw-redirect" title="ML IERR">ML_IERR</a>,
    which can be easily combined with the fast execution mode.
- External forces with [EFOR](../incar-tags/EFOR.md).
- Spline interpolation of the electronic structure factor
  ([ESF_SPLINES](ESF_SPLINES.md)) for [k-point
  convergence
  acceleration](../methods/ACFDT__RPA_calculations.md)
  of RPA correlation energies.
- [Müller-Plathe method for thermal conductivity
  calculations](../tutorials/Müller-Plathe_method.md).

### IMPROVEMENT\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: IMPROVEMENT">edit</a> \| (./index.php.md)\]

- HDF5:
  - Write partial charges to the hdf5 output instead of
    [PARCHG](../output-files/PARCHG.md) files. This in turn enables the
    simulation of STM pictures with py4vasp.
  - Output that goes into [OSZICAR](../output-files/OSZICAR.md) is written
    into the [vaspout.h5](../output-files/Vaspout.h5.md) as well.
  - Dielectric function from time-evolution BSE is written to
    [vaspout.h5](../output-files/Vaspout.h5.md).
  - Possibility to force synchronization of the
    [vaspout.h5](../output-files/Vaspout.h5.md) file, and access
    [vaspout.h5](../output-files/Vaspout.h5.md) during the VASP runtime
    ([LSYNCH5](../incar-tags/LSYNCH5.md)).
- Improvements of the [VASP-TRIQS interface](../input-files/GAMMA.md): uses
  an [HDF5](../categories/Category-HDF5_support.md) file
  now (vaspgamma.h5).
- [ML_DESC_TYPE](../incar-tags/ML_DESC_TYPE.md)=1 is now also
  available for [ML_MODE](../incar-tags/ML_MODE.md)=*train*. This can
  significantly speed up training for systems with many elements.
- [ML_OUTBLOCK](../incar-tags/ML_OUTBLOCK.md) will be ignored when we
  are not running an MD with a [machine-learned force
  field](../categories/Category-Machine-learned_force_fields.md)
  in production mode.

### BUGFIX\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: BUGFIX">edit</a> \| (./index.php.md)\]

- The code failed to compile with gfortran with -DELPA.
- [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) did not work correctly
  anymore for [NCORE](../incar-tags/NCORE.md)/=1.
- Fixed an out-of-bounds access that broke the linear response NMR when
  using the NV compilers (confirmed for 24.1 and 24.3).
- The code on GPU was broken for some calculations that combine
  [LCALCEPS](../incar-tags/LCALCEPS.md) = .TRUE. with hybrid
  functionals.
- NKREDLF for GW+Gamma was not read correctly from
  [INCAR](../input-files/INCAR.md).
- [G0W0R](../methods/Practical_guide_to_GW_calculations.md)
  calculation crashed for certain combinations of ranks,
  [NBANDS](../incar-tags/NBANDS.md) and
  [NTAUPAR](../incar-tags/NTAUPAR.md).
- [CRPAR](../theory/Category-Constrained-random-phase_approximation.md)
  with many MPI ranks for small systems failed.
- fixed a memory leak in the deallocation of the reciprocal space
  projectors.
- The code did not detect when WFULLXXXX.tmp files were produced with a
  different [ENCUTGW](../incar-tags/ENCUTGW.md).
- Fix for possible integer overflows in [PEAD](../incar-tags/LPEAD.md)
  routines.
- Wrong projections in vasprun.xml with
  [KPOINTS_OPT](../input-files/KPOINTS_OPT.md).
- [ML_MODE](../incar-tags/ML_MODE.md)=refit was broken when not using
  scaLAPACK.
- Incorrect handling of noncollinear spin calculation in KDER_WAVE, in
  particular the spinor rotation part was not applied. This leads to
  incorrect results when using
  [LEPSILON](../incar-tags/LEPSILON.md)=.TRUE. for
  [LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=.TRUE. and
  [ISYM](../incar-tags/ISYM.md)\>0.
- Setting the [VDW_S6](../incar-tags/VDW_S6.md) tag had no effect in the
  case of the dDsC method ([IVDW](../incar-tags/IVDW.md)=4), while it
  should.
- Some of the ELPA calls were not using the correct communicators and
  matrix sizes.
- Fixed NaN Fock energy in [hybrid band structure
  calculations](../methods/Band-structure_calculation_using_hybrid_functionals.md).
- NaN lines in the [ML_LOGFILE](../output-files/ML_LOGFILE.md) for
  [ML_WTSIF](../incar-tags/ML_WTSIF.md)=0.00 are repaired.
- Fixed memory estimation for [ML_MODE](../incar-tags/ML_MODE.md)=train
  or select.
- Fixed a problem with the output of the positions to
  [CONTCAR](../output-files/CONTCAR.md) and
  [XDATCAR](../output-files/XDATCAR.md). During long MD runs the ions may
  move by multiple lattice vectors and at some point the write format of
  the positions would become unsuitable.
- For some systems, interpolation of phonon frequencies using
  [LPHON_DISPERSION](../incar-tags/LPHON_DISPERSION.md)=True
  would sometimes produce anisotropic results with respect to the
  q-vector. This is now fixed for most cases.
- [ALGO](../incar-tags/ALGO.md)=RPA with ESF splines was broken when large
  numbers of MPI ranks were used.
- [SCDM](../incar-tags/LSCDM.md) method now works correctly for
  [ISPIN](../incar-tags/ISPIN.md)=2.
- The gamma-only version of the calculation of zero-field-splitting
  (D-matrix) was broken for [NCORE](../incar-tags/NCORE.md) \> 1. This has
  been fixed.
- Fixed estimation of the cutoff criteria for the erfc function during
  one-shot Wannierization for [ISPIN](../incar-tags/ISPIN.md)=2. The
  behavior is now identical to the [ISPIN](../incar-tags/ISPIN.md)=1 case.
- Fixed [ISPIN](../incar-tags/ISPIN.md)=2 for Wannier electron-phonon
  calculations
- Prevent [LOPTICS](../incar-tags/LOPTICS.md) after GW if
  [LPEAD](../incar-tags/LPEAD.md) not set and notify user.
- The
  [LATTICE_CONSTRAINTS](../incar-tags/LATTICE_CONSTRAINTS.md)
  where not applied before checking the break criterion.
- Calculations with [KPOINTS_OPT](../input-files/KPOINTS_OPT.md)
  crashed when [LORBIT](../incar-tags/LORBIT.md)=10, 11 or 12.
- Calculations with [LMODELHF](../incar-tags/LMODELHF.md) crashed if no
  [WAVECAR](../input-files/WAVECAR.md) is present.
- Fixed a crash of noncollinear calculations when using
  [KPOINTS_OPT](../input-files/KPOINTS_OPT.md).

## 6.4.3\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: 6.4.3">edit</a> \| (./index.php.md)\]


#### FEATURE\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: FEATURE">edit</a> \| (./index.php.md)\]

- Increased flexibility in the choice of exchange-correlation
  functionals: added the tags [XC](../incar-tags/XC.md) and
  [XC_C](../incar-tags/XC_C.md) to specify linear combinations of
  exchange-correlation functionals.
- Additional MGGA functionals (v1-sregTM, v2-sregTM, v3-sregTM, and
  v2-sregTM-L) from Francisco, Cancio, and Trickey
  (<a href="https://doi.org/10.1063/5.0167868" class="external free"
  rel="nofollow">https://doi.org/10.1063/5.0167868</a>,
  <a href="https://doi.org/10.1063/5.0167873" class="external free"
  rel="nofollow">https://doi.org/10.1063/5.0167873</a>).
- Interface to the external code libMBD
  (<a href="https://libmbd.github.io" class="external free"
  rel="nofollow">https://libmbd.github.io</a>): many-body dispersion
  methods for van der Waals interactions. See
  [LIBMBD_METHOD](../incar-tags/LIBMBD_METHOD.md).
- Analyze the bandgap and write the results to
  [OUTCAR](../output-files/OUTCAR.md) and
  [vaspout.h5](../output-files/Vaspout.h5.md). The details of the output
  are controlled with the [BANDGAP](../incar-tags/BANDGAP.md) tag.
- [Compute and write out exciton wavefunctions in
  BSE](../theory/Plotting_exciton_wavefunction.md)
  (written to [CHG](../output-files/CHG.md)).
- Non-blocked Davidson minimizer ([ALGO](../incar-tags/ALGO.md) = Dav, or
  [IALGO](../incar-tags/IALGO.md) = 119).
- Select the minimum number of local reference configurations required
  to build an MLFF via the [ML_MB_MIN](../incar-tags/ML_MB_MIN.md) tag.
  A new log line "MSG" with a text message is written to
  [ML_LOGFILE](../output-files/ML_LOGFILE.md) if this threshold inhibits
  training.
- [CSVR thermostat](../theory/CSVR_thermostat.md) of Bussi et
  al.
- [WRT_POTENTIAL](../incar-tags/WRT_POTENTIAL.md) writes the
  potential (total, xc, hartree, and ion contributions) to
  [vaspout.h5](../output-files/Vaspout.h5.md). In case the dipole
  correction is switched on and
  [LVACPOTAV](../incar-tags/LVACPOTAV.md)=.TRUE., the workfunction
  (rather, the vacuum potentials on either side of the slab) will be
  automatically determined and written to both the
  [OUTCAR](../output-files/OUTCAR.md) as well as to the
  [vaspout.h5](../output-files/Vaspout.h5.md) file.
- [LWRITE_SPN](../incar-tags/LWRITE_SPN.md)=T writes the spin-matrix
  element to the .spn file for wannier90.

#### IMPROVEMENT\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: IMPROVEMENT">edit</a> \| (./index.php.md)\]

- Update
  [makefile.include.nec_aurora](Makefile.include.nec_aurora.md)
  template to work with the recent NEC compiler version (5.0.0+).
- Add workarounds for Intel oneAPI LLVM compilers (ifx), and
  [makefile.include](Makefile.include.md) files
  for these compilers.
- Print proper error message when using the gamma-only version in
  combination with [KPOINTS_OPT](../input-files/KPOINTS_OPT.md).
- [LSINGLES](../incar-tags/LSINGLES.md): “singles” contribution printed
  to [OUTCAR](../output-files/OUTCAR.md) for GWR algorithms, *i.e.*, Eq. 34
  of Klimes *et al.*, JCP 143, 102816 (2015)
  (<a href="https://doi.org/10.1063/1.4929346" class="external free"
  rel="nofollow">https://doi.org/10.1063/1.4929346</a>).
- [SAXIS](../incar-tags/SAXIS.md) = 0 0 0 behaves like
  [SAXIS](../incar-tags/SAXIS.md) = 0 0 1. This behavior is unchanged but
  we now print a warning.
- Speedup of tetrahedron method by parallelization over tetrahedra and
  excluding tetrahedra that do not contribute; this improvement will be
  most noticeable for dense energy grids or k-point meshes.
- Consistent treatment of [CSHIFT](../incar-tags/CSHIFT.md),
  [CSHIFT](../incar-tags/CSHIFT.md) set to 0.02, consistent break criteria
  for linear response to increase robustness.
- Improved structure output to HDF5 file.
- Support for cusolverMP (the distributed GPU eigensolver of NVIDIA).
- Change magnetization output for the noncollinear case so that the
  (x,y,z) magnetization densities are integrated at the atomic sites and
  printed to the [OUTCAR](../output-files/OUTCAR.md) file (if
  [LORBIT](../incar-tags/LORBIT.md)=11 is set) every 5 steps for all
  electronic minimization algorithms.
- In some cases, the "blow-up" step in the k-point generation leads to
  trouble in combination with [IBRION](../incar-tags/IBRION.md)=6 and
  [ISIF](../incar-tags/ISIF.md)=3. This is not solved per se, but the
  resulting error message has been improved to suggest adding the
  appropriate tag to skip this step
  (<a href="/wiki/index.php?title=KBLOWUP&amp;action=edit&amp;redlink=1"
  class="new" title="KBLOWUP (page does not exist)">KBLOWUP</a>=.FALSE.).
- Copy the atomic type designation from [POSCAR](../input-files/POSCAR.md)
  to [CONTCAR](../output-files/CONTCAR.md). In all other instances where
  the structure is written to file (e.g.
  [CHGCAR](../input-files/CHGCAR.md)) the atomic type information is
  replaced by the acronym from the periodic table.
- The [SCDM
  method](../categories/Category-Wannier_functions.md) "Category:Wannier functions")
  now consumes much less memory when executed on many cores.
- Write more information about DFT+D4 calculations
  ([IVDW](../incar-tags/IVDW.md)=13).
- For MD runs with a large number of atoms and few ionic steps, the
  current default chunking size might lead to an unnecessarily large
  [vaspout.h5](../output-files/Vaspout.h5.md) file. Here, we make sure
  the chunking size is never larger than the number of MD steps.
- The default value for the minimum number of local reference
  configurations ([ML_MB_MIN](../incar-tags/ML_MB_MIN.md)) is increased
  from 2 to 3. This should improve the robustness of initial MLFF
  guesses.
- Check maximum size of sysv shmem segments used in
  machine-learning-code paths.
- <a href="/wiki/BSE" class="mw-redirect" title="BSE">BSE algorithm</a>
  has been optimized and ported to GPU by means of OpenACC.
- Spectral function is recalculated after GW calculations for
  [LOPTICS](../incar-tags/LOPTICS.md)=.TRUE.
- Demote LATTCHK exception from error to warning.
- Increase the default [ML_CDOUB](../incar-tags/ML_CDOUB.md) value to
  100 for re-selection runs ([ML_MODE](../incar-tags/ML_MODE.md)=select).
  Because this makes critical steps very unlikely the number of
  force-field generations is decreased. Hence, the total runtime until
  re-selection is finished will also be reduced.

#### BUGFIX\[<a
href="/wiki/index.php?title=Changelog&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: BUGFIX">edit</a> \| (./index.php.md)\]

- Descriptor sparsification was not working in combination with the
  [ML_MODE](../incar-tags/ML_MODE.md) tag: the tag
  [ML_LSPARSDES](../incar-tags/ML_LSPARSDES.md) was automatically
  set to False.
- Reference energies in [INCAR](../input-files/INCAR.md) were ignored when
  continuing MLFF training runs and in re-selection runs
  ([ML_MODE](../incar-tags/ML_MODE.md)=select).
- MLFF: Verlet nearest-neighbor algorithm was not updating properly in
  some cases. This violated energy conservation in MD runs.
- [ML_OUTBLOCK](../incar-tags/ML_OUTBLOCK.md) now also controls the
  output frequency of [ML_EATOM](../output-files/ML_EATOM.md) and
  [ML_HEAT](../output-files/ML_HEAT.md). Unwanted output in
  [OUTCAR](../output-files/OUTCAR.md),
  [vasprun.xml](../output-files/Vasprun.xml.md) and
  [vaspout.h5](../output-files/Vaspout.h5.md) has been removed.
- Fixed problem with incorrect counting of atoms in slabs in FML + fixed
  NVE setting of CVS thermostat.
- When using [VCAIMAGES](../incar-tags/VCAIMAGES.md) in combination
  with the NPT ensemble ([ISIF](../incar-tags/ISIF.md)=3) the stress tensor
  was not averaged as the forces and energy when using this approach.
- Fix incorrect formatting in [REPORT](../output-files/REPORT.md) file
  (values of last column shifted to next line).

<!-- -->

- Restarting a calculation from
  [vaspwave.h5](../output-files/Vaspwave.h5.md) when the number of
  k-points changed, *e.g.* because symmetry was switched off
  ([ISYM](../incar-tags/ISYM.md)=-1), now behaves the same as restarting
  from [WAVECAR](../input-files/WAVECAR.md). Before it stopped with a bug
  message.
- Write [LOCPOT](../output-files/LOCPOT.md) to subfolders for calculations
  with [IMAGES](../incar-tags/IMAGES.md)/=0.
- In the non-collinear case, [LVTOT](../incar-tags/LVTOT.md)=.TRUE. now
  writes the potential in the "density, magnetization" representation,
  i.e., the scalar potential (v0), and magnetic field (Bx, By, Bz), to
  the [LOCPOT](../output-files/LOCPOT.md) file. Before the potential was
  written in the (upup, updown, downup, downdown) representation to real
  numbers, which is incomplete.
- Fixed a problem in the generation of partial charge densities
  ([PARCHG](../output-files/PARCHG.md)) with reading a single value from
  [EINT](../incar-tags/EINT.md) and setting the second one to the Fermi
  energy automatically. [IBAND](../incar-tags/IBAND.md) and
  [KPUSE](../incar-tags/KPUSE.md) can no longer contain bands or points
  that are larger than the total number of bands or k points.

<!-- -->

- Due to a bug the wavefunction prediction was not as effective as it
  could be.
- Use a tighter threshold for Laplace-transformed MP2 to avoid incorrect
  treatment of Coulomb potential.

<!-- -->

- NMR linear response did not work for [LREAL](../incar-tags/LREAL.md)=Auto
  or .TRUE. (with the GNU compiler).
- Calculations of NMR shielding tensors was broken for
  [ISPIN](../incar-tags/ISPIN.md)=2 and
  [LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=.TRUE.: setting
  [ISPIN](../incar-tags/ISPIN.md)=2 for a non-spinpolarized system did not
  yield the same result as with [ISPIN](../incar-tags/ISPIN.md)=1.

<!-- -->

- [SAXIS](../incar-tags/SAXIS.md): For sx=0 and sy\<0, alpha=-pi/2. It used
  to falsely assume alpha=pi/2.
- Rotation of the wavefunctions in PEAD calculations was incorrect for
  [LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=.TRUE.
- [LATTICE_CONSTRAINTS](../incar-tags/LATTICE_CONSTRAINTS.md)
  was not read when using [IBRION](../incar-tags/IBRION.md)=1 or 2:
  default values (T T T = no constraints) were used.

<!-- -->

- The SCDM method now works correctly for k-point meshes that do not
  include the Gamma point.
- CRPA calculations using wannier90 were broken when using legacy mode
  (i.e. wannier90.win file instead of
  [WANNIER90_WIN](../incar-tags/WANNIER90_WIN.md) tag).

<!-- -->

- The LDA and GGA components of the AM05 GGA functional were not
  multiplied by the parameters [ALDAX](../incar-tags/ALDAX.md),
  [ALDAC](../incar-tags/ALDAC.md), [AGGAX](../incar-tags/AGGAX.md) and
  [AGGAC](../incar-tags/AGGAC.md).
- If a new vdW kernel was generated because the existing one was
  incompatible with the selected functional, then the header of the new
  kernel was the one of the old incompatible kernel. Furthermore,
  writing the new vdW kernels was not restricted to a single MPI rank.



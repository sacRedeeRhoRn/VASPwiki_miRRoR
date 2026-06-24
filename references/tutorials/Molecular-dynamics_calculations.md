<!-- Source: https://vasp.at/wiki/index.php/Molecular-dynamics_calculations | revid: 37011 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Molecular-dynamics calculations
Molecular dynamics (MD) is used to study the movement of atoms over time
in a given thermodynamic ensemble. This makes MD useful whenever a
static ground-state calculation is insufficient, e.g., to study thermal
disorder, diffusion, structural fluctuations, phase stability, melting,
or how a system equilibrates under realistic conditions.

In an ab initio MD, the forces along the trajectory can be computed
directly from DFT, or they can be provided by a machine-learned force
field (MLFF) once a reliable model is available. In practice, MD in VASP
can therefore be used for both accurate short first-principles
trajectories and much longer simulations involving more atoms based on
native [MLFF
workflows](../methods/Machine_learning_force_field_calculations-_Basics.md)
or external models, such as
[GRACE](../methods/Running_GRACE_force_fields_in_VASP.md).
This page explains how to set up and validate standard MD calculations
in VASP, as well as how to avoid the most common numerical and physical
pitfalls. More advanced sampling methods are covered under "[advanced
molecular-dynamics
sampling](../redirects/Advanced_molecular-dynamics_sampling.md)".

## Contents

- [1 Step-by-step instructions](#Step-by-step_instructions)
  - [1.1 Step 1: Prepare a stable starting
    structure](#Step_1:_Prepare_a_stable_starting_structure)
  - [1.2 Step 2: Set the core MD tags](#Step_2:_Set_the_core_MD_tags)
  - [1.3 Step 3: Select the ensemble and cell
    dynamics](#Step_3:_Select_the_ensemble_and_cell_dynamics)
  - [1.4 Step 4: Choose how the forces are
    computed](#Step_4:_Choose_how_the_forces_are_computed)
  - [1.5 Step 5: Test the run before extending
    it](#Step_5:_Test_the_run_before_extending_it)
- [2 Recommendations and advice](#Recommendations_and_advice)
- [3 Related tags and articles](#Related_tags_and_articles)

## Step-by-step instructions
### Step 1: Prepare a stable starting structure
Generate a [POSCAR](../input-files/POSCAR.md) containing a large enough
cell. In practice, MD usually requires a substantial number of ions so
that the trajectory samples a meaningful distribution of local
environments. If the cell is too small, the statistics will be poor, and
the atoms, defects, or local distortions may interact too strongly with
their periodic images.

You may want to consider proceeding with a [structure
optimization](Structure_optimization.md). If
the initial structure is still strained or carries large residual
forces, the MD run will spend its initial steps removing artificial
stress rather than of sampling the desired physical motion. This often
results in to unstable trajectories, poor temperature control, and, in
MLFF training workflows, low-quality training data. Alternatively, you
can use a [CONTCAR](../output-files/CONTCAR.md) file from a previous MD run
as a starting point to continue the trajectory, because in that case it
already contains ionic velocities in addition to the structure.

If you plan to run ab initio MD, relax the structure with the same ab
initio setup that you will later use for the trajectory.The same
consistency is needed for MLFF-based MD: either relax with the same MLFF
that will drive the dynamics, or generate the reference structures with
the same ab initio settings used for training. Disable symmetry with
[`ISYM`](../incar-tags/ISYM.md)` = 0` for MD, since thermal motion generaly
breaks the symmetry of the relaxed structure.

[TABLE]

### Step 2: Set the core MD tags
Activate MD with [`IBRION`](../incar-tags/IBRION.md)` = 0`, then define
the trajectory length, timestep, temperature control, and cell
constraints.

The key MD tags are:

- **[NSW](../incar-tags/NSW.md)** sets the number of ionic steps and
  therefore the total simulation length.
- **[POTIM](../incar-tags/POTIM.md)** sets the time step in fs and must be
  supplied for MD runs. It must be small enough to resolve the fastest
  ionic motion.
- **[TEBEG](../incar-tags/TEBEG.md)** and **[TEEND](../incar-tags/TEEND.md)**
  define the initial and target temperatures for thermostat-based runs.
- **[MDALGO](../incar-tags/MDALGO.md)** selects the thermostat and
  integration scheme. More on that in the next step.
- **[ISIF](../incar-tags/ISIF.md)** determines whether the cell can change
  shape and volume or is fixed.

Choose [POTIM](../incar-tags/POTIM.md) conservatively. Systems containing
hydrogen bonds or stiff bonds usually require smaller timesteps than
heavy, weakly bound systems. Reduce [POTIM](../incar-tags/POTIM.md) and
retest if the total energy drifts strongly in
[NVE](../misc/NVE_ensemble.md), if the atoms show
unrealistically large displacements, or if the electronic
self-consistent field (SCF) cycle becomes erratic.

For long trajectories, also decide how often data should be written.
[NBLOCK](../incar-tags/NBLOCK.md) controls how often ionic configurations
are written to [XDATCAR](../output-files/XDATCAR.md) and how often
pair-correlation and DOS-related quantities are accumulated. In MLFF
prediction runs, use [ML_OUTBLOCK](../incar-tags/ML_OUTBLOCK.md) to
more broadly reduce screen and file output frequency.

|  |
|----|
| **Tip:** The atomic masses can be intentionally changed for MD, by setting the [POMASS](../incar-tags/POMASS.md) tag in the [INCAR](../input-files/INCAR.md). By default the masses are read from [POTCAR](../input-files/POTCAR.md). This can be useful for increasing POTIM for light atoms such as hydrogen, but it changes the physical dynamics and should be avoided when mass-dependent observables are the target. |

### Step 3: Select the ensemble and cell dynamics
Select an ensemble based on the physical conditions you want to sample.
Because VASP determines the ensemble by combining
[MDALGO](../incar-tags/MDALGO.md) and [ISIF](../incar-tags/ISIF.md), your
choice of [thermostat](../redirects/Thermostats.md) directly impacts
your available cell degrees of freedom. For instance, while the
[Langevin thermostat](Langevin_thermostat.md)
([`MDALGO`](../incar-tags/MDALGO.md)` = 3`) flexibly supports both
[NVT](../misc/NVT_ensemble.md) and
[NpT](../misc/NpT_ensemble.md) simulations, other algorithms
do not allow independent configuration of the cell.

- **[Canonical ensemble (NVT)](../misc/NVT_ensemble.md):** use
  this to run simulations at a fixed number of particles (N), fixed
  volume (V) and constant temperature (T). Several thermostats can be
  used here, including
  [Andersen](Andersen_thermostat.md)
  ([`MDALGO`](../incar-tags/MDALGO.md)` = 1`),
  [Nosé–Hoover](Nosé-Hoover_thermostat.md)
  ([`MDALGO`](../incar-tags/MDALGO.md)` = 2`),
  [Langevin](Langevin_thermostat.md)
  ([`MDALGO`](../incar-tags/MDALGO.md)` = 3`), [Nosé–Hoover
  chain](../misc/Nosé-Hoover_chain_thermostat.md)
  ([`MDALGO`](../incar-tags/MDALGO.md)` = 4`),
  [CSVR](../theory/CSVR_thermostat.md)
  ([`MDALGO`](../incar-tags/MDALGO.md)` = 5`), and multiple Andersen
  thermostats ([`MDALGO`](../incar-tags/MDALGO.md)` = 13`). Keep the cell
  fixed with [ISIF](../incar-tags/ISIF.md) \< 3;
  [`ISIF`](../incar-tags/ISIF.md)` = 2` is a common choice because it also
  reports the full stress tensor.
- **[Micro–canonical ensemble
  (NVE)](../misc/NVE_ensemble.md):** use this only after
  equilibration. This ensemble is very useful because the atoms will be
  propagated by the MLFF or DFT forces only. So there will be no
  artificial thermostat data added to the velocities. This ensemble
  might be helpful if there is interest in self correlation functions.
  For example [velocity auto-correlation
  functions](Sampling_phonon_spectra_from_molecular-dynamics_simulations.md)
  might be of interest because [phonon
  DOS](Computing_the_phonon_dispersion_and_DOS.md)
  can be obtained from these. It is treated as a special case where a
  thermostat is selected but effectively switched off. The simplest way
  to do this is with [`MDALGO`](../incar-tags/MDALGO.md)` = 1` and
  [`ANDERSEN_PROB`](../incar-tags/ANDERSEN_PROB.md)` = 0.0`.
  Another option is [`MDALGO`](../incar-tags/MDALGO.md)` = 2` with
  [`SMASS`](../incar-tags/SMASS.md)` = -3`, which disables the [Nosé–Hoover
  thermostat](Nosé-Hoover_thermostat.md)
  and yields [NVE](../misc/NVE_ensemble.md) dynamics. Keep the
  cell fixed with [ISIF](../incar-tags/ISIF.md) \< 3. Note here that the
  choice of the thermostat will determine the propagation scheme which
  is used for the NVE simulation.
- **[Isothermal–isobaric ensemble
  (NpT)](../misc/NpT_ensemble.md):** use this when pressure
  and volume fluctuations are part of the problem. This will be the case
  when for example phase transitions should be studied under which the
  simulation box will change. In VASP, this is implemented for [Langevin
  dynamics](Langevin_thermostat.md), i.e.,
  [`MDALGO`](../incar-tags/MDALGO.md)` = 3` together with
  [`ISIF`](../incar-tags/ISIF.md)` = 3`. The [Langevin
  thermostat](Langevin_thermostat.md) requires
  the following additional tags:
  [LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) for the ions
  and [LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) for
  the lattice. [PMASS](../incar-tags/PMASS.md) controls the fictitious
  lattice mass.
- **[Isoenthalpic–isobaric ensemble
  (NpH)](../misc/NpH_ensemble.md):** use this when you want
  constant pressure without a thermostat hitting at you system. This
  ensemble is interesting when studying for example crystallization
  processes. Crystallization converts potential energy into kinetic
  energy. An ([NpT](../misc/NpT_ensemble.md)) thermostat
  artificially drains this kinetic energy to keep temperature flat,
  killing the natural heating that regulates the real nucleation rate.
  Again, one has to use the Langevin route with
  [`MDALGO`](../incar-tags/MDALGO.md)` = 3` and
  [`ISIF`](../incar-tags/ISIF.md)` = 3`, but with
  [`LANGEVIN_GAMMA`](../incar-tags/LANGEVIN_GAMMA.md)` = 0` and
  [`LANGEVIN_GAMMA_L`](../incar-tags/LANGEVIN_GAMMA_L.md)` = 0`,
  which switches off both ionic and lattice thermostatting.

For most workflows, begin with [NVT](../misc/NVT_ensemble.md)
and then validate the timestep and force quality in
[NVE](../misc/NVE_ensemble.md). Only use
[NpT](../misc/NpT_ensemble.md) when the cell should fluctuate.
[NpT](../misc/NpT_ensemble.md) can lead to irreversible cell
deformations for liquids or systems with limited long-range order unless
lattice constraints are applied.

|  |  |  |  |  |  |  |
|----|:--:|:--:|:--:|:--:|:--:|:--:|
|  | [Thermostat](../categories/Category-Thermostats.md) |  |  |  |  |  |
| [Ensemble](../categories/Category-Ensembles.md) | [Andersen](Andersen_thermostat.md) | [Nosé-Hoover](Nosé-Hoover_thermostat.md) | [Langevin](Langevin_thermostat.md) | [Nosé-Hoover chain](../misc/Nosé-Hoover_chain_thermostat.md) | [CSVR](../theory/CSVR_thermostat.md) | [Multiple Andersen](../incar-tags/MDALGO.md) |
| [Microcanonical (NVE)](../misc/NVE_ensemble.md) | [MDALGO](../incar-tags/MDALGO.md)=1, [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)=0.0 |  |  |  |  |  |
| [Canonical (NVT)](../misc/NVT_ensemble.md) | [MDALGO](../incar-tags/MDALGO.md)=1 | [MDALGO](../incar-tags/MDALGO.md)=2 | [MDALGO](../incar-tags/MDALGO.md)=3 | [MDALGO](../incar-tags/MDALGO.md)=4 | [MDALGO](../incar-tags/MDALGO.md)=5 | [MDALGO](../incar-tags/MDALGO.md)=13 |
|  | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 |
| [Isobaric-isothermal (NpT)](../misc/NpT_ensemble.md) | not available | not available | [MDALGO](../incar-tags/MDALGO.md)=3 | not available | not available | not available |
|  |  |  | [ISIF](../incar-tags/ISIF.md)=3 |  |  |  |
| [Isoenthalpic-isobaric (NpH)](../misc/NpH_ensemble.md) | [MDALGO](../incar-tags/MDALGO.md)=3, [ISIF](../incar-tags/ISIF.md)=3, [LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md)=[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md)=0.0 |  |  |  |  |  |

A minimal fixed-cell [NVT](../misc/NVT_ensemble.md) starting
point is:

    IBRION = 0
    NSW    = 5000
    POTIM  = 1.0
    TEBEG  = 300
    TEEND  = 300
    MDALGO = 2
    SMASS  = 0
    ISIF   = 2
    ISYM   = 0

For variable-cell [NpT](../misc/NpT_ensemble.md) with Langevin
dynamics, start from:

    IBRION           = 0
    NSW              = 5000
    POTIM            = 1.0
    TEBEG            = 300
    TEEND            = 300
    MDALGO           = 3
    ISIF             = 3
    LANGEVIN_GAMMA   = 10.0 10.0 # For two species
    LANGEVIN_GAMMA_L = 10.0
    PMASS            = 1000
    ISYM             = 0

These are just starting points for MD control; add the converged
electronic and force-provider settings from the next step.

For the Langevin parameters, begin with moderate friction and only
adjust if a clear problem appears in the short test run. If
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) or
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) is too
small, temperature or pressure equilibration may be very slow. If they
are too large, the dynamics become overdamped, and time-dependent
observables become less meaningful. [PMASS](../incar-tags/PMASS.md)
controls how quickly the cell responds. Too small values can lead to
violent volume fluctuations, while too large values makes the cell
relaxation very sluggishly. For liquids or soft systems, closely monitor
the cell evolution and use the [ICONST](../input-files/ICONST.md) file to
constrain the lattice if the box begins to deform irreversibly.

### Step 4: Choose how the forces are computed
Select the method for force generation, as this choice dictates the
computational expense and determines whether the workflow incorporates
machine learning training.

- **Ab initio MD:** all forces are computed from DFT at every step. This
  is the standard setup and typically the best starting point for a new
  system.
- **Native VASP MLFF, on-the-fly:** enable
  [`ML_LMLFF`](../incar-tags/ML_LMLFF.md)` = .TRUE.` to activate
  machine-learned force fields. With
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = train`, VASP performs
  on-the-fly learning. MLFF predictions are used when the estimated
  error is low enough. Additional ab initio calculations are triggered
  when new reference data are needed. Therefore, this mode still
  requires a complete ab initio setup, including
  [INCAR](../input-files/INCAR.md), [KPOINTS](../input-files/KPOINTS.md), and
  [POTCAR](../input-files/POTCAR.md). For the full workflow, see: "[Machine
  learning force field calculations:
  Basics](../methods/Machine_learning_force_field_calculations-_Basics.md)".
- **Native VASP MLFF, prediction-only:** after training and refitting
  the force field, use [`ML_MODE`](../incar-tags/ML_MODE.md)` = run` to
  perform MD with MLFF predictions only. This mode does not generate new
  ab initio data, so it should only be used once the applicability of
  the force field has been verified.
- **GRACE in VASP:** GRACE is an external pretrained force field and is
  also a prediction-only method. Use
  [`ML_LMLFF`](../incar-tags/ML_LMLFF.md)` = .TRUE.`,
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = run`, and
  [`ML_TYPE`](../incar-tags/ML_TYPE.md)` = grace` with a compatible build
  and an available GRACE model.

In practice, the practical distinction is simple: ab initio MD computes
every step directly from DFT; on-the-fly MLFF combines MD with automatic
training; and both VASP-native
[`ML_MODE`](../incar-tags/ML_MODE.md)` = run` and GRACE are
prediction-only modes.

An ab initio MD run also requires electronic settings that maintain a
stable SCF cycle throughout the trajectory. A conservative starting
point is:

    PREC  = Accurate
    EDIFF = 1E-6
    ALGO  = Normal

Combine these with the converged [ENCUT](../incar-tags/ENCUT.md), smearing
choice, and **k**-point mesh from the preceding relaxation. For
on-the-fly MLFF runs, the same ab initio settings must be present
because VASP triggers reference electronic calculations whenever new
training data are needed.

|  |
|----|
| **Mind:** Keep the exchange-correlation functional, PAW datasets, cutoff, and **k**-point strategy consistent between relaxation, MLFF training, and MD. Changing these settings changes the underlying potential-energy surface, meaning the relaxed structure and forces are no longer fully compatible. |

To convert the previous MD input into an on-the-fly MLFF run, add:

    ML_LMLFF = .TRUE.
    ML_MODE  = train

For prediction-only MLFF, use:

    ML_LMLFF = .TRUE.
    ML_MODE  = run

For GRACE, add [`ML_TYPE`](../incar-tags/ML_TYPE.md)` = grace` to the
prediction-only setup.

|  |
|----|
| **Mind:** If the cell is allowed to change with [`ISIF`](../incar-tags/ISIF.md)` = 3`, monitor the cell shape and volume carefully. The PAW basis is fixed at the beginning of the calculation, so significant cell changes can lead to Pulay-stress errors and unreliable pressure readings. |

### Step 5: Test the run before extending it
Begin with a short trajectory and examine the temperature, forces,
stress, and electronic convergence before committing to a long run.
Ensure that the thermostat drives the system toward the intended
temperature, that no atom leaves the physically meaningful structure,
and that the SCF cycle remains stable along the trajectory.

In practice, check [OSZICAR](../output-files/OSZICAR.md) for the
temperature and total energy evolution, [OUTCAR](../output-files/OUTCAR.md)
for force maxima, stress, and SCF convergence behavior, and
[XDATCAR](../output-files/XDATCAR.md) or [CONTCAR](../output-files/CONTCAR.md)
for obviously unphysical atomic motion. Warning signs include repeated
electronic nonconvergence, large force spikes, a steady temperature
drift away from the target in [NVT](../misc/NVT_ensemble.md),
strong total energy drift in [NVE](../misc/NVE_ensemble.md),
and rapidly growing cell distortions in variable-cell runs. If any of
these occur, first reduce [POTIM](../incar-tags/POTIM.md). Then, tighten
the electronic settings. If needed, fall back to a simpler fixed-cell
[NVT](../misc/NVT_ensemble.md) test.

If the short test behaves sensibly, continue from
[CONTCAR](../output-files/CONTCAR.md) with the same physical and electronic
settings. To restart, copy [CONTCAR](../output-files/CONTCAR.md) to
[POSCAR](../input-files/POSCAR.md). If the
[CONTCAR](../output-files/CONTCAR.md) file was written by an MD run it may
also contain the ionic velocities. This allows the trajectory to
continue smoothly instead of starting with newly randomized velocities.
Use a short [NVE](../misc/NVE_ensemble.md) segment after
equilibration to assess whether the timestep and force convergence are
adequate.

|  |
|----|
| **Mind:** Equilibration and production serve different purposes. Use the initial part of the trajectory to allow the temperature, pressure, volume, and local structure to relax away from the initial configuration. Only after these quantities have fluctuated around a steady state should the trajectory be treated as production data for calculating averages, diffusion coefficients, performing structural analyses, and determining other observables. |

## Recommendations and advice
- Use a generous cutoff for variable-cell runs. With
  [`ISIF`](../incar-tags/ISIF.md)` = 3`, the PAW basis does not update
  during the run. Therefore, large cell distortions can increase
  Pulay-stress errors and degrade the pressure.
- For long trajectories, increase [NBLOCK](../incar-tags/NBLOCK.md) if
  [XDATCAR](../output-files/XDATCAR.md) and related MD output become
  unnecessarily large. For MLFF prediction-only runs, use
  [ML_OUTBLOCK](../incar-tags/ML_OUTBLOCK.md) for output throttling.
  It also sets a lower bound for [NBLOCK](../incar-tags/NBLOCK.md).
- Restart from [CONTCAR](../output-files/CONTCAR.md) and retain the
  velocities when continuing a trajectory.
- Do not interpret a very short trajectory as thermodynamic sampling.
  Equilibration and production are separate parts of an MD workflow.
- Most thermostat and barostat options selected through
  [MDALGO](../incar-tags/MDALGO.md) require a build compiled with
  `-Dtbdyn`.

Common pitfalls:

- Starting from an highly strained structure, which often causes large
  forces and unstable dynamics.
- Using a supercell that is too small or containing too few ions results
  in poor statistics and enhances finite-size artifacts from periodic
  images.
- Choosing a timestep that is too large for the fastest vibrational
  modes.
- Allowing poor electronic convergence, which directly corrupts the
  forces.
- Changing the cutoff, smearing, or the **k**-point mesh between related
  MD or MLFF runs.
- Using variable-cell dynamics without ensuring that the pressure and
  Pulay stress are under control.
- Treating thermostat-controlled trajectories as if they automatically
  provide reliable dynamical observables is also a mistake.
- Restarting from [CONTCAR](../output-files/CONTCAR.md) without confirming
  that velocities are present and physically consistent.
- Using MLFF or GRACE production runs outside the range of structures
  represented in the training data.

## Related tags and articles
Files: [POSCAR](../input-files/POSCAR.md), [INCAR](../input-files/INCAR.md),
[POTCAR](../input-files/POTCAR.md), [CONTCAR](../output-files/CONTCAR.md),
[OUTCAR](../output-files/OUTCAR.md), [OSZICAR](../output-files/OSZICAR.md),
[XDATCAR](../output-files/XDATCAR.md)

Tags: [IBRION](../incar-tags/IBRION.md), [NSW](../incar-tags/NSW.md),
[POTIM](../incar-tags/POTIM.md), [TEBEG](../incar-tags/TEBEG.md),
[TEEND](../incar-tags/TEEND.md), [MDALGO](../incar-tags/MDALGO.md),
[ISIF](../incar-tags/ISIF.md), [SMASS](../incar-tags/SMASS.md),
[ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md),
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md),
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md),
[PMASS](../incar-tags/PMASS.md), [NBLOCK](../incar-tags/NBLOCK.md),
[ML_OUTBLOCK](../incar-tags/ML_OUTBLOCK.md),
[ENCUT](../incar-tags/ENCUT.md), [EDIFF](../incar-tags/EDIFF.md),
[NELM](../incar-tags/NELM.md), [ALGO](../incar-tags/ALGO.md),
[PREC](../incar-tags/PREC.md), [ISYM](../incar-tags/ISYM.md),
[ML_LMLFF](../incar-tags/ML_LMLFF.md),
[ML_MODE](../incar-tags/ML_MODE.md), [ML_LIB](../incar-tags/ML_LIB.md),
[ML_TYPE](../incar-tags/ML_TYPE.md)

[Structure
optimization](Structure_optimization.md),
[Ensembles](../redirects/Ensembles.md), [NVT
ensemble](../misc/NVT_ensemble.md), [NVE
ensemble](../misc/NVE_ensemble.md), [NpT
ensemble](../misc/NpT_ensemble.md), [NpH
ensemble](../misc/NpH_ensemble.md),
[Thermostats](../redirects/Thermostats.md), [Andersen
thermostat](Andersen_thermostat.md),
[Nosé-Hoover
thermostat](Nosé-Hoover_thermostat.md),
[Langevin thermostat](Langevin_thermostat.md),
[Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md),
[CSVR thermostat](../theory/CSVR_thermostat.md),
[Machine-learned force
fields](../redirects/Machine-learned_force_fields.md)

[Advanced MD
methods](../categories/Category-Advanced_molecular-dynamics_sampling.md)
for free energies, biased sampling, monitored collective variables, and
transport properties: [Interface pinning
calculations](Interface_pinning_calculations.md),
[Constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md),
[Metadynamics](../theory/Metadynamics.md), [Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md),
[Slow-growth
approach](../theory/Slow-growth_approach.md),
[Monitoring geometric
parameters](../incar-tags/MDALGO.md),
[Thermodynamic
integration](../categories/Category-Thermodynamic_integration.md),
[Müller-Plathe
method](Müller-Plathe_method.md).

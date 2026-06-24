<!-- Source: https://vasp.at/wiki/index.php/IBRION | revid: 37190 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IBRION
IBRION = -1 \| 0 \| 1 \| 2 \| 3 \| 5 \| 6 \| 7 \| 8 \| 11 \| 12 \| 40 \|
44 

|                     |      |                                    |
|---------------------|------|------------------------------------|
| Default: **IBRION** | = -1 | for [NSW](NSW.md)=−1 or 0 |
|                     | = 0  | else                               |

Description: determines how the crystal structure changes during the
calculation:

- no update
  - `IBRION`` = -1` (Avoid setting `IBRION`` = -1` with
    [`NSW`](NSW.md)` > 0` to prevent recomputing the same
    structure [NSW](NSW.md) times).

&nbsp;

- [Molecular dynamics](#Molecular_dynamics)
  - `IBRION`` = 0`

&nbsp;

- [Structure optimization](#Structure_optimization)
  - `IBRION`` = 1` RMM-DIIS
  - `IBRION`` = 2` conjugate gradient
  - `IBRION`` = 3` damped molecular dynamics

&nbsp;

- [Computing phonon modes](#Computing_the_phonon_modes)
  - `IBRION`` = 5` finite differences without symmetry (deprecated; use
    6 instead)
  - `IBRION`` = 6` finite differences with symmetry
  - `IBRION`` = 7` perturbation theory without symmetry (deprecated; use
    8 instead)
  - `IBRION`` = 8` perturbation theory with symmetry

&nbsp;

- [Analyzing transition states](#Analyzing_transition_states)
  - `IBRION`` = 40` [intrinsic-reaction-coordinate
    calculations](../redirects/IRC_calculations.md)
  - `IBRION`` = 44` [improved dimer
    method](https://vasp.at/wiki/index.php/Improved_dimer_method)

&nbsp;

- [User-supplied interactive
  changes](#Interactively_supplied_positions_and_lattice_vectors)
  - `IBRION`` = 11` from standard input
  - `IBRION`` = 12` from Python plugin

------------------------------------------------------------------------

## Contents

- [1 Molecular dynamics](#Molecular_dynamics)
- [2 Structure optimization](#Structure_optimization)
- [3 Computing the phonon modes](#Computing_the_phonon_modes)
- [4 Analyzing transition states](#Analyzing_transition_states)
- [5 Interactively supplied positions and lattice
  vectors](#Interactively_supplied_positions_and_lattice_vectors)
- [6 Related tags and articles](#Related_tags_and_articles)

## Molecular dynamics
In [molecular-dynamics (MD)
simulations](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
the positions of the ions are updated using a classical equation of
motion for the ions. There are several algorithms for the [time
propagation in
MD](../theory/Time-propagation_algorithms_in_molecular_dynamics.md)
controlled by selecting [MDALGO](MDALGO.md) and the choice
of the [thermostats](../redirects/Thermostats.md). The MD run
performs [NSW](NSW.md) timesteps of length
[POTIM](POTIM.md).

Frequently, performing an [ab-initio
calculations](../redirects/Electronic_minimization.md)
in every step of an MD simulation is too expensive so that
[machine-learned force
fields](../categories/Category-Machine-learned_force_fields.md)
are needed.

|  |
|----|
| **Tip:** In order to limit the output of the MD simulation, control the verbosity by setting [NWRITE](NWRITE.md)=0,1, or reduce the frequency of output using [ML_OUTBLOCK](ML_OUTBLOCK.md), [NBLOCK](NBLOCK.md), or [KBLOCK](KBLOCK.md). |

## Structure optimization
VASP optimizes the structure based on the degrees of freedom selected
with the [ISIF](ISIF.md) tag and (if used) the selective
dynamics [POSCAR](../input-files/POSCAR.md) file. Generally, the larger the
number of degrees of freedom, the harder it is to find the optimal
solution. To find the solution, VASP provides multiple algorithms:

- RMM-DIIS (`IBRION`` = 1`) reduces the forces by linear combination of
  previous positions. It is the method of choice for larger systems
  (\>20 degrees of freedom) that are reasonably close to the
  ground-state structure.
- Conjugate gradient (`IBRION`` = 2`) finds the optimal step size along
  a search direction. It is a robust default choice but may need more
  iterations than RMM-DIIS.
- Damped molecular dynamics (`IBRION`` = 3`) runs a MD simulation with
  decreasing velocity of the ions. Use this for large systems far away
  from the minimum to get to a better starting point for the other
  algorithms.

Consult the [structure
optimization](../tutorials/Structure_optimization.md)
page for advise on how to choose the optimization algorithm.

## Computing the phonon modes
The second-order derivatives of the total energy $E$ with respect to ionic positions $R_{\alpha i}$ of ion $\alpha$
in the direction $i$, is computed using
a first-order derivative of the [forces](../redirects/Forces.md)
$F_{\beta j}$. Then, the dynamical
matrix $D_{\alpha i \beta j}$ is
constructed, diagonalized, and the phonon modes and frequencies of the
system are reported in the [OUTCAR](../output-files/OUTCAR.md) file and
[vaspout.h5](../output-files/Vaspout.h5.md). Also see [theory on
phonons](../theory/Phonons-_Theory.md).

|  |
|----|
| **Tip:** It may be necessary to set [`EDIFF`](EDIFF.md)` <= 1E-6` because the default ([`EDIFF`](EDIFF.md)` = 1E-4`) often results in unacceptably large errors. |

VASP implements two different methods to compute the phonon modes and
can use symmetry to reduce the number of computed displacements:

- `IBRION`` = 5` [finite
  differences](../tutorials/Phonons_from_finite_differences.md)
  **without** symmetry
- `IBRION`` = 6` [finite
  differences](../tutorials/Phonons_from_finite_differences.md)
  **with** symmetry
- `IBRION`` = 7` [density-functional-perturbation
  theory](../tutorials/Phonons_from_density-functional-perturbation_theory.md)
  **without** symmetry
- `IBRION`` = 8` [density-functional-perturbation
  theory](../tutorials/Phonons_from_density-functional-perturbation_theory.md)
  **with** symmetry

It is strongly recommended to use symmetry (6 or 8), as this can reduce
the computational effort by several orders of magnitude without
sacrifying accuracy. For finite differences, the elastic tensors and
internal strain tensors are computed for
[`ISIF`](ISIF.md)` >= 3`. Compute Born-effective charges,
piezoelectric constants, and the ionic contribution to the dielectric
tensor by specifying [`LEPSILON`](LEPSILON.md)` = .TRUE.`
([linear response theory](../redirects/Linear_response.md)) or
[`LCALCEPS`](LCALCEPS.md)` = .TRUE.` (finite external
field).

Also see [computing the phonon dispersion and
DOS](../tutorials/Computing_the_phonon_dispersion_and_DOS.md).

## Analyzing transition states
To study the kinetics of chemical reactions, one may want to construct
[transition states](../redirects/Transition_states.md) or
follow the reaction path. For the analysis of transition states the
following methods are available:

- Setting `IBRION`` = 40`, you can start from a transition state and
  monitor the energy along an intrinsic-reaction coordinate (IRC). The
  [IRC calculations](../redirects/IRC_calculations.md) section
  describes this method.
- With the [improved dimer
  method](https://vasp.at/wiki/index.php/Improved_dimer_method)
  (`IBRION`` = 44`), you can search for a the transition state starting
  from an arbitrary structure in the investigated phase space.
- The [nudged elastic
  bands](../tutorials/Nudged_elastic_bands.md) method finds
  an approximate reaction path based on the initial and final structure,
  i.e., reactant and product.

## Interactively supplied positions and lattice vectors
Occasionally, you may want to run VASP for related structures where the
overhead of restarting VASP is significant. In these scenarios, VASP
provides the following alternatives

- With `IBRION`` = 11`, you can provide new structures via the standard
  input, cf. the [INTERACTIVE](INTERACTIVE.md) tag. For
  [`ISIF`](ISIF.md)` >= 3`, a complete
  [POSCAR](../input-files/POSCAR.md) file is read, otherwise just the
  positions in fractional coordinates.

&nbsp;

- If you [linked VASP with
  Python](../misc/Makefile.include.md) "Makefile.include"),
  you can [write a Python plugin](../tutorials/Plugins.md) to modify the
  structure. Set `IBRION`` = 12` or
  [`PLUGINS/STRUCTURE`](PLUGINS__STRUCTURE.md)` = T`
  to activate it.

## Related tags and articles
Related tags: [NSW](NSW.md), [POTIM](POTIM.md),
[MDALGO](MDALGO.md), [SMASS](SMASS.md),
[NFREE](NFREE.md), [ISIF](ISIF.md),
[LEPSILON](LEPSILON.md),
[LCALCEPS](LCALCEPS.md)

Related files: [POSCAR](../input-files/POSCAR.md),
[CONTCAR](../output-files/CONTCAR.md), [XDATCAR](../output-files/XDATCAR.md),
[vaspout.h5](../output-files/Vaspout.h5.md)

Related topics and how-to pages: [Time-propagation algorithms in
molecular
dynamics](../theory/Time-propagation_algorithms_in_molecular_dynamics.md),
[Structure
optimization](../tutorials/Structure_optimization.md),
[Selective dynamics](../input-files/POSCAR.md),
[Computing the phonon dispersion and
DOS](../tutorials/Computing_the_phonon_dispersion_and_DOS.md),
[Transition states](../redirects/Transition_states.md), [IRC
calculations](../redirects/IRC_calculations.md), [Improved
Dimer Method](../misc/Improved_Dimer_Method.md),
[Writing a Python plugin](../tutorials/Plugins.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IBRION-_incategory-Examples)

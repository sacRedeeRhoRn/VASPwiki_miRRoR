<!-- Source: https://vasp.at/wiki/index.php/Machine_learning_force_field_calculations:_Basics | revid: 35184 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Machine learning force field calculations: Basics


The machine-learned force fields (MLFF) feature of VASP allows you to
generate, improve, modify and apply force fields based on machine
learning techniques for your system of interest. Although there are many
tunable parameters, i.e. MLFF-related [INCAR](../input-files/INCAR.md) tags,
the default values have been carefully selected to simplify the initial
creation of an MLFF. Hence, we hope that only minimal additional effort
is required to get started with this feature. Nevertheless, because
machine learning involves multiple steps, e.g., at a minimum separate
training and application stages, this page tries to explain the basic
tags controlling the corresponding modes of operation. If you are
already familiar with the basic usage of the MLFF feature, you may want
to have a closer look at the [best practices
page](Best_practices_for_machine-learned_force_fields.md)
which offers more in-depth advice for tuning MLFF settings. If you need
more information about the theory and algorithms please visit the [MLFF
theory
page](Machine_learning_force_field-_Theory.md).

## Step-by-step instructions\[<a
href="/wiki/index.php?title=Machine_learning_force_field_calculations:_Basics&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

On-the-fly training is based on molecular-dynamics (MD) simulations to
sample training structures. Piece by piece a data set is automatically
assembled and used to generate an MLFF whenever feasible. Conversely, at
each time step the current force field predicts energy, forces and the
corresponding Bayesian error estimations. Simply put, if the error is
above a certain threshold another ab-initio calculation is performed and
the reference energy and forces are added to the training data set. In
the opposite case, the ab-initio step is omitted and the system is
propagated via MLFF predictions. As the force field gets better along
the trajectory many ab-initio steps can be avoided and the MD simulation
is significantly accelerated. Ultimately, the on-the-fly training
results in an MLFF which is ready for production, i.e., running an MD
simulation in prediction-only mode.

|  |
|----|
| **Warning:** When compiling with shared memory MPI support (-Duse_shmem), it is utterly important to pin the MPI ranks to the physical cores of the node. For guidance on how to understand the hardware topology of your system and how to correctly set up rank pinning accordingly, refer to [here](../tutorials/Optimizing_the_parallelization.md). |

The following steps outline the path from start to production run:

**Step 1: Prepare a molecular dynamics run**

Prepare an
[ab-initio](../categories/Category-Calculation_setup.md)
[MD](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
run with your desired [POSCAR](../input-files/POSCAR.md) starting
configuration and an appropriate setup in [INCAR](../input-files/INCAR.md),
[KPOINTS](../input-files/KPOINTS.md) and [POTCAR](../input-files/POTCAR.md)
files.

**Step 2: Start on-the-fly training from scratch**

The MLFF method can be configured with a lot of [INCAR
tags](#Category:Machine-learned_force_fields) which are easily
recognized from their prefix `ML_`. In general, to enable any MLFF
feature the following [INCAR](../input-files/INCAR.md) tag needs to be set:

    ML_LMLFF = .TRUE.

If this tag is not set to `.TRUE.` other MLFF-related
[INCAR](../input-files/INCAR.md) tags are completely ignored and VASP will
perform regular ab-initio calculations. Furthermore, to start on-the-fly
training we additionally need to set the
[ML_MODE](../incar-tags/ML_MODE.md) "super"-tag:

    ML_MODE = train

When executed in this `train` mode VASP will automatically perform
ab-initio calculation whenever necessary and otherwise rely on the
predictions of the MLFF. The usual output files, e.g.,
[OUTCAR](../output-files/OUTCAR.md), [XDATCAR](../output-files/XDATCAR.md),
will be created along the MD trajectory. In addition, MLFF-related files
will be written to disk, the most important ones being:

- [ML_LOGFILE](../output-files/ML_LOGFILE.md) The log file for all
  MLFF-related details; training status, current errors and other
  important quantities can be extracted from here.
- [ML_ABN](../output-files/ML_ABN.md) This file contains the collected
  training structures and a list of selected local reference
  configurations.
- [ML_FFN](../output-files/ML_FFN.md) A binary file containing the current
  MLFF.

All three files are repeatedly updated during the MD simulation. After
[NSW](../incar-tags/NSW.md) time steps are carried out the
[ML_ABN](../output-files/ML_ABN.md) and [ML_FFN](../output-files/ML_FFN.md) file
contain the complete training data set and the final MLFF, respectively.
Training errors can be found in
[ML_LOGFILE](../output-files/ML_LOGFILE.md) by searching for lines
starting with `ERR`.

**Step 3 (optional): Continue on-the-fly training from existing training
database**

In principle, step 2 above may yield a force field ready for further
processing and application. However, most of the time additional
on-the-fly training iterations are necessary. For example, to extend the
training database with structures at higher temperatures or different
densities. Or, a force field is required to capture different atom type
compositions or phases, e.g., a liquid and multiple solid phases. This
can be achieved by on-the-fly continuation runs: at the beginning a
force field is generated from the previous training data and - if
applicable - used for predictions in the MD run. Like in step 2, the
force field is trained along the trajectory. However, it also retains
its applicability to the structures of the previous on-the-fly run.
Finally, the continuation training will result in an MLFF capable of
predicting structures of both runs. To continue on-the-fly training
first set up your new starting [POSCAR](../input-files/POSCAR.md)
structure, e.g., by copying from the [CONTCAR](../output-files/CONTCAR.md)
file. The new structure may share some atom types with the previous run
but this is not a requirement. It is also possible to continue training
with completely different atom types in the
[POSCAR](../input-files/POSCAR.md) file (remember to set up your
[POTCAR](../input-files/POTCAR.md) accordingly). The only other action
required is to copy the existing database to the
[ML_AB](../input-files/ML_AB.md) file:

    cp ML_ABN ML_AB

Leave [`ML_MODE`](../incar-tags/ML_MODE.md)` = train` unchanged and
restart VASP. The log file will contain a section describing the
existing data set and after initial generation of a force field the
regular on-the-fly procedure continues. In the end, the resulting
[ML_ABN](../output-files/ML_ABN.md) will contain the training structures
from both on-the-fly runs. Similarly, the
[ML_FFN](../output-files/ML_FFN.md) file is a combined force field. In the
presence of an [ML_AB](../input-files/ML_AB.md) file the `train` mode will
always perform a continuation run. If you would like to start from
scratch just remove the [ML_AB](../input-files/ML_AB.md) file from the
execution directory.

|  |
|----|
| **Tip:** Apply this strategy repeatedly in order to systematically improve your MLFF, e.g., first train on water only, then on sodium chloride and finally, train on the combination of both. |

**Step 4: Refit for fast prediction mode** (available as of VASP 6.4.0)

When on-the-fly training succeeded and the result matches your
expectations with respect to applicability and residual errors there is
one final step required before the force field should be applied in
prediction-only MD runs: refitting for fast prediction mode. Copy once
again the final data set to [ML_AB](../input-files/ML_AB.md):

    cp ML_ABN ML_AB

Also, set in the [INCAR](../input-files/INCAR.md) file:

    ML_MODE = refit

Running VASP will create a new [ML_FFN](../output-files/ML_FFN.md) which
finally can be used for production.

|  |
|----|
| **Important:** Although it is technically possible to continue directly with step 5 given a [ML_FFN](../output-files/ML_FFN.md) file from steps 2 or 3 it is strongly discouraged. Without the refitting step VASP cannot enable the fast prediction mode which comes with speedup factor of approximately 20 to 100. You can check the [ML_FFN](../output-files/ML_FFN.md) ASCII [header](../output-files/ML_FFN.md) to be sure whether the contained force field supports fast prediction. |

**Step 5: Applying the machine-learned force field in production runs**

The MLFF obtained from step 4 is now ready to be applied in the
prediction-only mode. First, copy the [ML_FFN](../output-files/ML_FFN.md)
file:

    cp ML_FFN ML_FF

In the [INCAR](../input-files/INCAR.md) file set

    ML_MODE = run

With this choice VASP will only use the predictions from the MLFF, no
ab-initio calculations are performed. The execution time per time step
will be orders of magnitude lower if compared with corresponding
ab-initio runs.

|  |
|----|
| **Tip:** The MLFF can be transferred to larger system sizes, i.e., you may duplicate your simulation box to benefit from improved statistics. Because the method scales linearly with the number of atoms you can easily estimate the impact on computational demand. |

|  |
|----|
| **Warning:** Please have a look at a [known issue](../misc/Known_issues.md) (from date 2023-05-17) if you intend to use triclinic geometries with small or large lattice angles. |

Usually, VASP machine-learned force field files
[ML_FFN](../output-files/ML_FFN.md) are backward compatible, i.e., files
generated by an older version of VASP can still be used with newer VASP
binaries (for details check [the ML_FFN file
header](../output-files/ML_FFN.md)).

## Advice\[<a
href="/wiki/index.php?title=Machine_learning_force_field_calculations:_Basics&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Advice">edit</a> \| (./index.php.md)\]

On-the-fly learning can be significantly more involved than, e.g., a
single-point electronic calculation, because it combines multiple
features of VASP. Each part requires a proper setup via the available
[INCAR](../input-files/INCAR.md) tags. A misconfiguration corresponding to
one part of the calculation may have severe effects on the quality of
the resulting MLFF. In the worst case, successful training may even be
impossible. To be more specific, on-the-fly learning requires control
over the following aspects:

- **Consistent convergence**

It is required that all ab-initio reference data collected via
on-the-fly training is consistent and well-converged with respect to the
[single-point electronic calculation
setup](../categories/Category-Electronic_minimization.md).
Mind different temperatures and densities targeted in MD runs. A MLFF
can only reproduce a single potential energy landscape!

- **Correct setup of [molecular dynamics
  simulations](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)**

Consider the choice of thermodynamic ensembles, thermostat and barostat
settings and an appropriate time step.

- **Proper setup of machine-learned force field parameters**

Mind system-dependent parameters like the cutoff radius or atomic
environment descriptor resolution.

- **Control over data set generation via on-the-fly learning**

Monitor and control how much ab-initio reference data is harvested via
automatic Bayesian threshold determination and sparsification.

- **Quality control**

Establish reasonable expectations regarding residual training errors.
Benchmark the quality of resulting force fields by comparison of
predictions with known quantities (from ab-initio).

|  |
|----|
| **Tip:** Begin by thoroughly familiarizing yourself with pure ab-initio calculations for your system before attempting to generate a MLFF from scratch. Once you are confident in controlling the convergence, proceed to run a brief MD simulation without machine learning assistance. Validate whether the results align with expected values regarding conservation principles and so forth. Only then, move forward with the machine learning aspects of the calculation. |

## Parallelization\[<a
href="/wiki/index.php?title=Machine_learning_force_field_calculations:_Basics&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Parallelization">edit</a> \| (./index.php.md)\]

At present, VASP provides only MPI-based parallelization for the MLFF
feature. Therefore, any operational mode relying exclusively on MLFF
code - such as predictive MD simulations
([ML_MODE](../incar-tags/ML_MODE.md) = `run`) and local reference
configuration selection ([ML_MODE](../incar-tags/ML_MODE.md) =
`select`) - cannot leverage alternative forms of parallelization like
[offloading to GPUs](../misc/GPU_ports_of_VASP.md) or [an
MPI/OpenMP hybrid
approach](../misc/Combining_MPI_and_OpenMP.md).
Conversely, a usual on-the-fly training involves both MLFF generation
and ab-initio computations. When the latter component predominates in
terms of computational demand, utilizing non-MPI parallelization remains
practical.



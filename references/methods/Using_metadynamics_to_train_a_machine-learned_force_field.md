<!-- Source: https://vasp.at/wiki/index.php/Using_metadynamics_to_train_a_machine-learned_force_field | revid: 36518 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Using metadynamics to train a machine-learned force field
It can be tricky to model transition states using [static
methods](https://vasp.at/wiki/index.php/Category:Transition_states)
methods. Sometimes, it is insufficient and more time-consuming [dynamic
methods](https://vasp.at/wiki/index.php/Category:Transition_states)
must be used. By using [advance MD
methods](../categories/Category-Advanced_molecular-dynamics_sampling.md)
in combination with [machine-learned force
fields](../categories/Category-Machine-learned_force_fields.md)
(MLFF), the cost can be significantly reduced.
[Metadynamics](../theory/Metadynamics.md) is one such method,
applying a biased potential on selected geometric parameters, to
describe rare events such as transition states. This tutorial is based
on [an older metadynamics
how-to](../misc/Nuclephile_Substitution_CH3Cl_-_mMD3.md).
The input files may be downloaded in a zip file at the end of this
tutorial.

## Contents

- [1 Input](#Input)
  - [1.1 POSCAR](#POSCAR)
  - [1.2 KPOINTS](#KPOINTS)
  - [1.3 ICONST](#ICONST)
  - [1.4 PENALTYPOT](#PENALTYPOT)
  - [1.5 INCAR.mlff](#INCAR.mlff)
  - [1.6 INCAR.refit](#INCAR.refit)
  - [1.7 INCAR.md](#INCAR.md)
  - [1.8 INCAR.interactive](#INCAR.interactive)
- [2 Step-by-step instructions](#Step-by-step_instructions)
  - [2.1 Step 0: Training the MLFF
    (optional)](#Step_0:_Training_the_MLFF_(optional))
  - [2.2 Step 1: Refitting the MLFF](#Step_1:_Refitting_the_MLFF)
  - [2.3 Step 2: Running the MD
    simulation](#Step_2:_Running_the_MD_simulation)
    - [2.3.1 MD analysis](#MD_analysis)
    - [2.3.2 Spilling factor](#Spilling_factor)
    - [2.3.3 Extracting new training
      structures](#Extracting_new_training_structures)
  - [2.4 Step 3: Retrain the MLFF](#Step_3:_Retrain_the_MLFF)
  - [2.5 Step 4: Refit the MLFF](#Step_4:_Refit_the_MLFF)
  - [2.6 Step 5: Repeat the MD
    simulation](#Step_5:_Repeat_the_MD_simulation)
    - [2.6.1 MD analysis](#MD_analysis_2)
    - [2.6.2 Spilling factor](#Spilling_factor_2)
    - [2.6.3 Plotting the biased
      potential](#Plotting_the_biased_potential)
- [3 Practical hints](#Practical_hints)
- [4 Download](#Download)
- [5 Related tags and articles](#Related_tags_and_articles)

## Input
### [POSCAR](../input-files/POSCAR.md)
       1.00000000000000
         9.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000    9.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    9.0000000000000000
       C    H    Cl
       1   3   2
    Direct
      0.1570348572197245  0.2904054711139102  0.1422643997559632
      0.1466469234176954  0.4066467848992589  0.1077433527138946
      0.0469134772399311  0.2399491465236156  0.1544210764126938
      0.2197893311177821  0.2820094213788985  0.2462070949679763
      0.9809163623144840  0.4723904404063168  0.3674924467383788
      0.2601754409903839  0.1874592103557934  0.9964911656110944

### [KPOINTS](../input-files/KPOINTS.md)
    Automatic
     0
    Gamma
     1  1  1
     0. 0. 0.

- For isolated atoms and molecules, interactions between periodic images
  are negligible (in sufficiently large cells), hence no Brillouin zone
  sampling is necessary.

### [ICONST](../input-files/ICONST.md)
    R 1 5 5
    R 1 6 5

- Two collective variables are used simultaneously to track the C-Cl
  distances.

### [PENALTYPOT](../input-files/PENALTYPOT.md)
       5.00000   1.00000   9.00000   0.50000
       5.00000   2.00000   9.00000   0.50000
       5.00000   3.00000   9.00000   0.50000
       5.00000   4.00000   9.00000   0.50000
       5.00000   5.00000   9.00000   0.50000
       1.00000   5.00000   9.00000   0.50000
       2.00000   5.00000   9.00000   0.50000
       3.00000   5.00000   9.00000   0.50000
       4.00000   5.00000   9.00000   0.50000

- To avoid the chlorine atom crossing between cells, a restrictive
  potential is used to hold it close to the molecule.

### [INCAR](../input-files/INCAR.md).mlff
    PREC=Normal
    EDIFF=1e-6
    LWAVE=.FALSE.
    LCHARG=.FALSE.
    NELECT=22
    NELMIN=4
    LREAL=.FALSE.
    ALGO=VeryFast
    ISMEAR=0
    SIGMA=0.05

    POMASS = 12.011 4.0 35.453 

    ############################# MD setting #####################################
    IBRION=0                                           # MD simulation
    NSW=100000                                         # number of steps
                                                          # reduce to NSW = 50000 or lower, if the MLFF is 
                                                          # too stable for subsequent steps
    POTIM=1                                            # integration step
    TEBEG=600                                          # simulation temperature
    MDALGO=1                                           # metaDynamics with Andersen thermostat
    ANDERSEN_PROB=0.05                                 # collision probability
    HILLS_BIN=50                                       # update the time-dependent bias
                                                                 # potential every 50 steps
    HILLS_H=0.0005                                     # height of the Gaussian
    HILLS_W=0.05                                       # width of the Gaussian
    ##############################################################################
    RANDOM_SEED = 311137787 0 0 

    # MLFF tags
    ML_LMLFF         = .TRUE.
    ML_MODE          =  TRAIN
    ISIF=2

### [INCAR](../input-files/INCAR.md).refit
    # MLFF tags
    ML_LMLFF         = .TRUE.
    ML_MODE          =  REFIT
    ISIF=2

### [INCAR](../input-files/INCAR.md).md
    POMASS = 12.011 4.0 35.453 

    ############################# MD setting #####################################
    IBRION=0                                           # MD simulation
    NSW=100000                                         # number of steps
    POTIM=1                                            # integration step
    TEBEG=600                                          # simulation temperature
    MDALGO=1                                           # metaDynamics with Andersen thermostat
    ANDERSEN_PROB=0.05                                 # collision probability
    HILLS_BIN=50                                       # update the time-dependent bias
                                                                 # potential every 50 steps
    HILLS_H=0.005                                      # height of the Gaussian
    HILLS_W=0.05                                       # width of the Gaussian
    ##############################################################################
    RANDOM_SEED = 311137787 0 0 

    # MLFF tags
    ML_LMLFF         = .TRUE.
    ML_MODE          =  RUN
    ISIF=2

    ML_ESTBLOCK = 20
    ML_OUTBLOCK = 20

### [INCAR](../input-files/INCAR.md).interactive
    PREC=Normal
    EDIFF=1e-6
    LWAVE=.FALSE.
    LCHARG=.FALSE.
    NELECT=22
    NELMIN=4
    LREAL=.FALSE.
    ALGO=VeryFast
    ISMEAR=0
    SIGMA=0.05

    POMASS = 12.011 4.0 35.453 

    ############################# MD setting #####################################
    IBRION=0                                           # MD simulation
    NSW=137                                            # number of steps
    POTIM=1                                            # integration step
    TEBEG=600                                          # simulation temperature
    MDALGO=1                                           # metaDynamics with Andersen thermostat
    ANDERSEN_PROB=0.05                                 # collision probability
    HILLS_BIN=50                                       # update the time-dependent bias
                                                                 # potential every 50 steps
    HILLS_H=0.0005                                     # height of the Gaussian
    HILLS_W=0.05                                       # width of the Gaussian
    ##############################################################################
    RANDOM_SEED = 311137787 0 0 

    # MLFF tags
    ML_LMLFF         = .TRUE.
    ML_MODE          = TRAIN
    ML_ICRITERIA     = 0
    ML_NMDINT        = 1
    ML_MCONF         = 2000

    ISIF             = 2
    INTERACTIVE      = .TRUE.

## Step-by-step instructions
### Step 0: Training the MLFF (optional)
**Required files:** [POSCAR](../input-files/POSCAR.md),
[POTCAR](../input-files/POTCAR.md), [INCAR](../input-files/INCAR.md).mlff,
[KPOINTS](../input-files/KPOINTS.md), [ICONST](../input-files/ICONST.md),
[PENALTYPOT](../input-files/PENALTYPOT.md),
[ML_AB](../input-files/ML_AB.md)

The first step is to generate the [machine-learned force
fields](../categories/Category-Machine-learned_force_fields.md)
(MLFFs). Run enough steps to have explored a large portion of the
configuration space of the reaction. This step will not sample many
points around the transition state, which you can account for later. Use
the `INCAR.mlff` file for this step. We have included an
[ML_AB](../input-files/ML_AB.md) file in the zip file below, so you can skip
this step.

|  |
|----|
| **Important:** Make sure that there is the [ICONST](../input-files/ICONST.md) and [PENALTYPOT](../input-files/PENALTYPOT.md) files or the MD run will not be metadynamics. |

    cd e00_training
    cp INCAR.mlff INCAR
    vasp_std

### Step 1: Refitting the MLFF
**Required files:** [POSCAR](../input-files/POSCAR.md),
[POTCAR](../input-files/POTCAR.md), [INCAR](../input-files/INCAR.md).refit,
[KPOINTS](../input-files/KPOINTS.md)

Copy the [ML_ABN](../output-files/ML_ABN.md) from step 0 to
[ML_AB](../input-files/ML_AB.md) (or from the zip file) and refit. Use the
`INCAR.refit` file for this.

    cd e01_refit
    cp INCAR.refit INCAR
    cp ../e00_training/ML_ABN ML_AB
    vasp_std

### Step 2: Running the MD simulation
**Required files:** [POSCAR](../input-files/POSCAR.md),
[POTCAR](../input-files/POTCAR.md), [INCAR](../input-files/INCAR.md).md,
[KPOINTS](../input-files/KPOINTS.md), [ICONST](../input-files/ICONST.md),
[PENALTYPOT](../input-files/PENALTYPOT.md)

First, link to the MLFF that you have just generated:
`ln -s ../e01_refit/ML_FFN ML_FF`. Then, run the molecular dynamics (MD)
simulation using `INCAR.md`. Make sure that the
[PENALTYPOT](../input-files/PENALTYPOT.md) file is present, as this is
vital for containing the molecule and modeling the reaction using
metadynamics. You will track the two C-Cl distances as collective
variables using the [ICONST](../input-files/ICONST.md) file.

    cd e02_MD
    cp INCAR.md INCAR
    ln -s ../e01_refit/ML_FFN ML_FF
    vasp_std

#### MD analysis
Once the metadynamics MD simulation is completed, plot the time
evolution of the collective variables (cf.
[ICONST](../input-files/ICONST.md)) using the `timeEv.sh` script and
`gnuplot`:

    bash ./timeEv.sh
    gnuplot -e "set terminal jpeg; set xlabel 'timestep'; set ylabel 'Collective variable (Ang)'; set style data lines; plot 'timeEvol1.dat', 'timeEvol2.dat'" > timeEvol.jpg

The obtained time evolution of the collective variables looks like the
following:

[![](https://vasp.at/wiki/images/thumb/7/70/ClCh3Cl_inversion_MLFF_MD.jpeg/600px-ClCh3Cl_inversion_MLFF_MD.jpeg)](https://vasp.at/wiki/File:ClCh3Cl_inversion_MLFF_MD.jpeg)

Two collective variables are monitored, the two C-Cl distances (purple
and green lines). After a few thousand steps (NB that we have used
[`ML_OUTBLOCK`](../incar-tags/ML_OUTBLOCK.md)` = 20` so there are 20
structures between each point), the two collective variables switch as
the transition state is crossed and the system inverts.

The Cl⁻ ion is initially far from the C atom. After a few thousand
steps, the chloromethane molecule inverts as the chloride attacks and
the opposing chlorine atom is expelled as a chloride. After a thousand
more steps, the MLFF breaks down, and a non-physical structure is formed
at which the MD simulation gets stuck.

|  |
|----|
| **Important:** If the simulation does not fail, repeat the calculation, try increasing the number of ionic steps ([NSW](../incar-tags/NSW.md)), until you run a simulation where the MLFF breaks down. Alternatively, decrease the number of [NSW](../incar-tags/NSW.md) used for training the MLFF in the first place. This will train an MLFF with fewer structures, i.e., a worse force field that will break down sooner. We only recommend this in this exercise so that you can learn how to fix an MLFF. |

#### Spilling factor
This is when the simulation leaves the configuration space of the MLFF
training set. You can see this by checking the [spilling
factor](../incar-tags/ML_ESTBLOCK.md) in the
[ML_LOGFILE](../output-files/ML_LOGFILE.md):

    grep SFF ML_LOGFILE

    # SFF ########################################################################################################
    # SFF This line shows the spilling factor,
    # SFF
    # SFF nstep ............ MD time step or input structure counter
    # SFF sfmax ............ Maximal spilling factor among atoms
    # SFF sfmin ............ Minimal spilling factor among atoms
    # SFF sfmean ........... Mean value of spilling factor
    # SFF sfvar ............ Variance of spilling factor
    # SFF threshold ........ Value of threshold criterion for learning
    # SFF ########################################################################################################
    # SFF               nstep            sfmax            sfmin           sfmean            sfvar        threshold
    # SFF                   2                3                4
    # SFF ########################################################################################################
    SFF                   100   9.29675803E-06   2.13512863E-07   2.26596576E-06   1.01225022E-11   2.00000000E-03
    SFF                   200   1.11874507E-06   4.26678995E-07   7.93844208E-07   5.02375989E-14   2.00000000E-03
    SFF                   300   1.69448509E-06   2.46957156E-07   9.74621854E-07   2.15210308E-13   2.00000000E-03
    ...
    SFF                 99960   9.99309893E-01   3.36556878E-03   3.40857829E-01   2.16239137E-01   2.00000000E-03
    SFF                 99980   9.99464421E-01   5.99966976E-03   3.44462977E-01   2.14118191E-01   2.00000000E-03
    SFF                100000   9.99581963E-01   5.29236322E-03   3.41837281E-01   2.15977938E-01   2.00000000E-03

We have set [`ML_OUTBLOCK`](../incar-tags/ML_OUTBLOCK.md)` = 20` so
that only every 20th structure is included. Notice how `sfmax` goes
to 1. This indicates that it is completely outside of the training set.
You can plot this to visualize what happens and compare to the plot
above. First, grep for the spilling factor `SFF` in the
[ML_LOGFILE](../output-files/ML_LOGFILE.md):

    grep '^SFF[[:space:]]*[0-9]' ML_LOGFILE | awk '{print $2 " " $3}' > sff.dat

Then plot `sff.dat` using Python:

    import py4vasp
    import numpy as np

    step, spilling_factor = np.loadtxt("./e02_MD/sff.dat", unpack=True)

    py4vasp.plot(step, spilling_factor, xlabel="MD step", ylabel="Spilling factor", label="Spilling factor")

[![](https://vasp.at/wiki/images/thumb/f/f6/Spilling_factor_plot.png/600px-Spilling_factor_plot.png)](https://vasp.at/wiki/File:Spilling_factor_plot.png)

The spilling factor plotted against the MD step. As it deviates from 0,
the structures are increasingly outside of the MLFF training set. The
MLFF then rapidly breaks down and the spilling factor increases to, then
remains at, 1.

#### Extracting new training structures
The structures after the spilling factor reaches 1 are not meaningful.
However, those shortly before are very useful. These are where the MLFF
begins to break down. You can extract these structures using the
`sff_grep.py` script:

    ./sff_grep.py ML_LOGFILE XDATCAR 5E-4 0.2

This will extract from [XDATCAR](../output-files/XDATCAR.md) all of the
structures in the configurations
[ML_LOGFILE](../output-files/ML_LOGFILE.md) that have a spilling factor
between `5E-4` and 0.2 and output them to a `POSCAR.interactive` file.
`POSCAR.interactive` can then be used in the next step to continue
training the MLFF.

|  |
|----|
| **Important:** `POSCAR.interactive` contains the position of the ions for each configuration in direct coordinates, which is used for interactive mode with [INTERACTIVE](../incar-tags/INTERACTIVE.md). The [POSCAR](../input-files/POSCAR.md) must still be included. |

### Step 3: Retrain the MLFF
**Required files:** [POSCAR](../input-files/POSCAR.md),
[POTCAR](../input-files/POTCAR.md),
[INCAR](../input-files/INCAR.md).interactive,
[KPOINTS](../input-files/KPOINTS.md), [ML_AB](../input-files/ML_AB.md)

Take the `POSCAR.interactive` that you have generated in the preceding
step, take the [ML_AB](../input-files/ML_AB.md) file that you have already
trained in step 0 (or refitted in step 1), along with the
[PENALTYPOT](../input-files/PENALTYPOT.md) from step 2, and the
`INCAR.interactive` file - making sure to update the
[NSW](../incar-tags/NSW.md) to the number of structures in
`POSCAR.interactive`. Then run a calculation with the same
[POSCAR](../input-files/POSCAR.md), [POTCAR](../input-files/POTCAR.md), and
[KPOINTS](../input-files/KPOINTS.md) files from step 1, ensuring to input
the `POSCAR.interactive` file into the VASP executable, enabled by
setting [`INTERACTIVE`](../incar-tags/INTERACTIVE.md)` = .TRUE.`,
e.g.:

    cd e03_interactive
    cp INCAR.interactive INCAR
    cp ../e00_training/ML_ABN ML_AB
    cp ../e00_training/HILLSPOT PENALTYPOT
    vasp_std < POSCAR.interactive

|  |
|----|
| **Important:** Ensure that you update [NSW](../incar-tags/NSW.md) in the [INCAR](../input-files/INCAR.md) to be equal to the number of configurations in your `POSCAR.interactive` file. |

### Step 4: Refit the MLFF
**Required files:** [POSCAR](../input-files/POSCAR.md),
[POTCAR](../input-files/POTCAR.md), [INCAR](../input-files/INCAR.md).refit,
[KPOINTS](../input-files/KPOINTS.md)

Refit the MLFF as before, copying the [ML_ABN](../output-files/ML_ABN.md) to
[ML_AB](../input-files/ML_AB.md) and refitting with `INCAR.refit`.

    cd e04_new_refit
    cp ../e03_interactive/ML_ABN ML_AB
    vasp_std

### Step 5: Repeat the MD simulation
**Required files:** [POSCAR](../input-files/POSCAR.md),
[POTCAR](../input-files/POTCAR.md), [INCAR](../input-files/INCAR.md).md,
[KPOINTS](../input-files/KPOINTS.md), [ICONST](../input-files/ICONST.md),
[PENALTYPOT](../input-files/PENALTYPOT.md) from old
[HILLSPOT](../incar-tags/HILLSPOT.md)

Copy your old biased potential ([HILLSPOT](../incar-tags/HILLSPOT.md)
file) from the initial MLFF training to the
[PENALTYPOT](../input-files/PENALTYPOT.md) in your new directory. This
saves you a lot of time by enabling you to begin from where the system
had already trained (alternatively, you can try using the potential from
the first MD run, being careful to remove the potentials added once the
spilling factor has reached 1, as these are non-physical). Then, run the
calculation as normal, increasing the number of ionic steps to 300000:

    cd e05_new_MD
    cp INCAR.md INCAR
    sed -i 's/NSW=100000/NSW=300000/g' INCAR
    cp ../e00_training/HILLSPOT PENALTYPOT
    ln -s ../e04_new_refit/ML_FFN ML_FF
    vasp_std

#### MD analysis
Once the calculation is finished, take a look at the time evolution of
the collective variables using `timeEv.sh` script and `gnuplot`:

    bash ./timeEv.sh
    gnuplot -e "set terminal jpeg; set xlabel 'timestep'; set ylabel 'Collective variable (Ang)'; set style data lines; plot 'timeEvol1.dat', 'timeEvol2.dat'" > timeEvol.jpg

The obtained time evolution of the collective variables looks like the
following:

[![](https://vasp.at/wiki/images/thumb/f/f9/Updated_inversions.jpeg/600px-Updated_inversions.jpeg)](https://vasp.at/wiki/File:Updated_inversions.jpeg)

Rather than getting stuck after a few thousand steps, this new MLFF is
much more stable and can keep on inverting back and forth over several
thousand steps.

Each time the green and purple lines switch, an inversion reaction has
occurred, and the transition state has been crossed. This is
signifciantly more stable than the previous iteration and indicates that
we are now more accurately modeling the transition state.

#### Spilling factor
You can confirm the stability of your MLFF by taking a look at the
spilling factor:

    grep '^SFF[[:space:]]*[0-9]' ML_LOGFILE | awk '{print $2 " " $3}' > sff.dat

Then plot `sff.dat` using Python:

    import py4vasp
    import numpy as np

    step, spilling_factor = np.loadtxt("./e05_new_MD/sff.dat", unpack=True)

    py4vasp.plot(step, spilling_factor, xlabel="MD step", ylabel="Spilling factor", label="Spilling factor")

[![](https://vasp.at/wiki/images/thumb/f/f2/Spilling_factor_plot_improved.png/600px-Spilling_factor_plot_improved.png)](https://vasp.at/wiki/File:Spilling_factor_plot_improved.png)

The spilling factor plotted against the MD step. The spilling factor
never deviates far from 0, indicating that the MD simulation is well
within the MLFF training set.

#### Plotting the biased potential
As a final step, you can visualize the biased potential that you have
generated. First, take the [HILLSPOT](../incar-tags/HILLSPOT.md) file
and, using the `gaussians.py` script, generate a file containing the sum
of the gaussians used for the biased potential
`gaussian_sum_output.txt`, removing the first 9 lines that contain the
initial biased potential:

    ./gaussians.py HILLSPOT 9

Then, plot the biased potential with the `contourplot.py` script:

    ./contourplot.py

This will generate the following interactive 3D plot (a 2D plot is also
created: `gaussian_sum_contour.png`):

[![](https://vasp.at/wiki/images/thumb/3/33/Gaussian_sum.png/600px-Gaussian_sum.png)](https://vasp.at/wiki/File:Gaussian_sum.png)

You can set a cutoff for the z-axis, e.g., 0.05, to get a better look at
the transition state region:

    ./contourplot.py 0.05

Taking a look at the biased potential from the initial MLFF training
(step 0), the first MD (step 2), and the final MD (step 5), you can see
how the configuration space has been explored:

[![](https://vasp.at/wiki/images/thumb/8/8b/Gaussian_sum_TS_compare.png/1000px-Gaussian_sum_TS_compare.png)](https://vasp.at/wiki/File:Gaussian_sum_TS_compare.png)

In the initial MLFF training, only the initial potential well is
well-explored, that on the lower right. This means that the other,
second, well (*yellow ellipse*) is not well-described by the MLFF.
Additionally, the transition state (*green circle*) is barely visited.
As a result, the MLFF breaks down fairly quickly, failing to describe
the transition state during one transition and getting stuck in a new
region outside of the trained space (cf. the spilling factor). The MLFF
finds that a non-physical structure (*white circle*) is the most stable.
Once we take the structures that have higher spilling factors (likely
those in the second potential and the transition state), the entire
simulation becomes much more stable and the transition state is better
described. Both wells become filled during the metadynamics run by the
biased potential.

As a final exercise, you could try repeating steps 3-5, taking the
structure from the second MD that have larger spilling factors, writing
them to `POSCAR.interactive`, and retraining the MLFF with these a
second time. Repeat this as many times as you would like to create an
ever more stable MLFF describing the transition state. After a certain
point, the wells will both be filled and the metadynamics run will be
completed; after this, the MLFF will become more unstable again.

## Practical hints
- Make sure to set the mass of hydrogen to above 1, e.g.,
  [`POMASS`](../incar-tags/POMASS.md)` = 12.011 4.0 35.453`, rather than
  [`POMASS`](../incar-tags/POMASS.md)` = 12.011 1.0 35.453`. This enables
  larger time steps for the MD simulation.
- We found that reducing the
  [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md) to 0.05 from 0.1
  improved stability (see [previous
  exercise](../misc/Nuclephile_Substitution_CH3Cl_-_mMD3.md)).
- It is crucial to reduce the hill height
  ([HILLS_H](../incar-tags/HILLS_H.md)) by an order of magnitude or more
  (e.g., 0.0005 instead of 0.005). This avoids being driven out of the
  reliably fitted energy surface. In a production run, it keeps the MLFF
  in the trained region for longer, stabilising the spilling factor.
- For long MLFF runs, it may be worth increasing
  [HILLS_BIN](../incar-tags/HILLS_BIN.md) to 100 to stay within the
  trained region for longer. This is only important for longer
  metadynamics simulations. You should also increase
  [`ML_ESTBLOCK`](../incar-tags/ML_ESTBLOCK.md)` = 100` and
  [`ML_OUTBLOCK`](../incar-tags/ML_OUTBLOCK.md)` = 100` in this case,
  so that the [OUTCAR](../output-files/OUTCAR.md) file does not become too
  big.
- Once you have a stable [ML_FF](../input-files/ML_FF.md), to improve the
  stability for longer MLFF runs, you should collect the positions for
  structures that are outside of the reliably fitted energy surface.
  These are those that have larger spilling factors. While continuing
  training (see [step
  4](../tutorials/Construction-MLFF+metadynamics.md)
  above), [`ML_NMDINT`](../incar-tags/ML_NMDINT.md)` = 1` should be
  used and the Bayesian threshold set to the final value from the
  previous training runs
  [`ML_ICRITERIA`](../incar-tags/ML_ICRITERIA.md)` = 0`.
- If you find that your molecule is rotating too much or moving between
  cells, make sure that you have the
  [PENALTYPOT](../input-files/PENALTYPOT.md) file present. This is to
  restrain the molecule in place, precisely to stop this movement.

## Download
[Metadynamics_with_mlff.zip](https://vasp.at/wiki/images/9/97/Metadynamics_with_mlff.zip "Metadynamics with mlff.zip")

## Related tags and articles
[Nucleophilic substitution of chloromethane by chloride using
metadynamics](../misc/Nuclephile_Substitution_CH3Cl_-_mMD3.md),
[INTERACTIVE](../incar-tags/INTERACTIVE.md)

------------------------------------------------------------------------

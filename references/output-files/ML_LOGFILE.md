<!-- Source: https://vasp.at/wiki/index.php/ML_LOGFILE | revid: 34741 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LOGFILE
Every VASP run with activated machine learning
([INCAR](../input-files/INCAR.md) contains
[ML_LMLFF](../incar-tags/ML_LMLFF.md) = .TRUE.) will generate a file
called ML_LOGFILE. In this log file a summary of settings and the
development of quantities related to machine learning are presented in a
compact, yet human-readable and post-processing friendly way. It
complements the usual ab initio log output in the
[OUTCAR](OUTCAR.md) and [OSZICAR](OSZICAR.md)
files for machine learning VASP runs.

## Contents

- [1 File layout](#File_layout)
  - [1.1 Memory consumption estimation](#Memory_consumption_estimation)
  - [1.2 Machine learning setup](#Machine_learning_setup)
  - [1.3 Existing ab initio data](#Existing_ab_initio_data)
  - [1.4 Main loop](#Main_loop)
    - [1.4.1 Header](#Header)
    - [1.4.2 Body](#Body)
  - [1.5 Timing information](#Timing_information)
- [2 Post-processing usage](#Post-processing_usage)
- [3 Collected data](#Collected_data)
  - [3.1 STDAB line](#STDAB_line)
    - [3.1.1 Energies](#Energies)
    - [3.1.2 Forces](#Forces)
    - [3.1.3 Stress](#Stress)
    - [3.1.4 Subset standard deviation](#Subset_standard_deviation)
  - [3.2 ERR line](#ERR_line)
    - [3.2.1 Energies](#Energies_2)
    - [3.2.2 Forces](#Forces_2)
    - [3.2.3 Stress](#Stress_2)
  - [3.3 NORME line](#NORME_line)
    - [3.3.1 Energies](#Energies_3)
    - [3.3.2 Forces](#Forces_3)
    - [3.3.3 Stress](#Stress_3)
  - [3.4 Per-species quantities for
    forces](#Per-species_quantities_for_forces)

## File layout
The machine learning log file is split into multiple sections, visually
separated like this:

    * SECTION TITLE ****************************************************************************************************************************

    ... content ...

    ********************************************************************************************************************************************

The actual composition of log sections may depend on the machine
learning mode of operation (see [ML_MODE](../incar-tags/ML_MODE.md)).
Usually, in the beginning there will be a couple of sections describing
the estimated memory consumption, machine learning settings and
preexisting data. Then follows the main loop, which is split into a
header and the actual loop body containing data describing the learning
progress ([`ML_MODE`](../incar-tags/ML_MODE.md)` = train`) or prediction
([`ML_MODE`](../incar-tags/ML_MODE.md)` = run`). Finally, there may be
sections about actual memory consumption and timing statistics. The
following chapters describe the contents of the log file sections in
more detail:

### Memory consumption estimation
This is usually the first section of the ML_LOGFILE and contains an
**estimation** of memory requirements based on VASP files read on
startup. In the simplest case
([`ML_MODE`](../incar-tags/ML_MODE.md)` = train`) it depends on the
settings in the [INCAR](../input-files/INCAR.md) and
[POSCAR](../input-files/POSCAR.md) file. For example, the expected memory
consumption may vary with the number of elements present in the
[POSCAR](../input-files/POSCAR.md) file. Various
[INCAR](../input-files/INCAR.md) tags also influence the memory demand, e.g.
[ML_MB](../incar-tags/ML_MB.md) or [ML_MRB2](../incar-tags/ML_MRB2.md). A
continuation or prediction run, i.e.,
[`ML_MODE`](../incar-tags/ML_MODE.md)` = train` with
[ML_AB](../input-files/ML_AB.md) present or
[`ML_MODE`](../incar-tags/ML_MODE.md)` = run`, may also take settings
from the files [ML_AB](../input-files/ML_AB.md) or
[ML_FF](../input-files/ML_FF.md) into account.

    * MEMORY INFORMATION ***********************************************************************************************************************

    Estimated memory consumption for ML force field generation (MB):

    Persistent allocations for force field        :    516.9
    |
    |-- CMAT for basis                            :     20.3
    |-- FMAT for basis                            :    458.5
    |-- DESC for basis                            :      2.6
    |-- DESC product matrix                       :      2.3

    Persistent allocations for ab initio data     :      8.1
    |
    |-- Ab initio data                            :      7.8
    |-- Ab initio data (new)                      :      0.3

    Temporary allocations for sparsification      :    460.9
    |
    |-- SVD matrices                              :    460.7

    Other temporary allocations                   :     15.5
    |
    |-- Descriptors                               :      4.7
    |-- Regression                                :      6.5
    |-- Prediction                                :      4.2

    Total memory consumption                      :   1001.4

    ********************************************************************************************************************************************

While the individual items in the above listing are of rather technical
nature the most important number is given in the last line:
`Total memory consumption` approximates the peak memory usage during
this VASP run. However, since not all memory is always allocated at the
same time the actual consumption may vary over time.

The following part summarizes which kind of parallelization each parts
employ:

|                      |           |               |
|:--------------------:|:---------:|:-------------:|
|                      | scaLAPACK | shared memory |
|    CMAT for basis    |     x     |       x       |
|    FMAT for basis    |     x     |               |
|    DESC for basis    |     x     |       x       |
| DESC product matrix  |     x     |               |
|    Ab initio data    |           |               |
| Ab initio data (new) |           |               |
|     SVD matrices     |     x     |               |
|     Descriptors      |           |               |
|      Regression      |     x     |               |
|      Prediction      |           |               |

The parts marked with an *x* for scaLAPACK contain block-cyclic
distributed arrays that usually scale almost perfectly with the number
of employed processors. The user will see that by increasing the number
of processors the amount of memory needed will significantly drop for
that part (we not that also `Descriptors` and `Prediction` will drop in
memory, but only slightly since only minor parts of these are
distributed). The parts marked with an *x* for shared memory show also a
significant decrease of memory usage if the code is compiled for shared
memory (precompiler option *use_shmem*). The risks of shared memory
usage are explained
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).

|  |
|----|
| **Mind:** This is only an estimate, the actual memory requirement may be even higher. Moreover, this is only the usage for the machine learning part of VASP which in a training run adds up to the memory of the ab initio part. |

### Machine learning setup
This section gives an overview of the most important
[INCAR](../input-files/INCAR.md) tags concerning machine learning settings.
The tags are grouped by topics and the tabular layout provides a short
description, the current value and a "state indicator" (see the actual
section header for an explanation).

    * MACHINE LEARNING SETTINGS ****************************************************************************************************************

    This section lists the available machine-learning related settings with a short description, their
    selected values and the INCAR tags. The column between the value and the INCAR tag may contain a
    "state indicator" highlighting the origin of the value. Here is a list of possible indicators:

     *     : (empty) Tag was not provided in the INCAR file, a default value was chosen automatically.
     * (I) : Value was provided in the INCAR file.
     * (i) : Value was provided in the INCAR file, deprecated tag.
     * (!) : A value found in the INCAR file was overwritten by the contents of the ML_FF file.
     * (?) : The value for this tag was never set (please report this to the VASP developers).

    Tag values with associated units are given here in Angstrom/eV, if not specified otherwise.

    Please refer to the VASP online manual for a detailed description of available INCAR tags.


    General settings
    --------------------------------------------------------------------------------------------------------------------------------------------
    Machine learning operation mode in strings (supertag)                                                 :         REFIT (I) ML_MODE       
    Machine learning operation mode                                                                       :             4     ML_ISTART     
    Precontraction of weights on Kernel for fast execution (ML_ISTART=2 only), but no error estimation    :             T     ML_LFAST      
    Controls the verbosity of the output at each MD step when machine learning is used                    :             1     ML_OUTPUT_MODE
    Sets the output frequency at various places for ML_ISTART=2                                           :             1     ML_OUTBLOCK

     
    Descriptor settings
    --------------------------------------------------------------------------------------------------------------------------------------------
    Radial descriptors:
    -------------------
    Cutoff radius of radial descriptors                                                                   :   5.00000E+00     ML_RCUT1
    Gaussian width for broadening the atomic distribution for radial descriptors                          :   5.00000E-01     ML_SION1
    Number of radial basis functions for atomic distribution for radial descriptors                       :             8     ML_MRB1

    Angular descriptors:
    --------------------
    Cutoff radius of angular descriptors                                                                  :   5.00000E+00     ML_RCUT2
    Gaussian width for broadening the atomic distribution for angular descriptors                         :   5.00000E-01     ML_SION2
    Number of radial basis functions for atomic distribution for angular descriptors                      :             8     ML_MRB2
    Maximum angular momentum quantum number of spherical harmonics used to expand atomic distributions    :             4     ML_LMAX2
    ...

### Existing ab initio data
This section will appear in continuation runs (e.g.
[`ML_MODE`](../incar-tags/ML_MODE.md)` = train` with existing
[ML_AB](../input-files/ML_AB.md)) and summarizes the ab initio data found in
the [ML_AB](../input-files/ML_AB.md) file.

    * AVAILABLE AB INITIO DATA *****************************************************************************************************************

    Number of stored (maximum) ab initio structures:       114 (     1500)
     * System   1 :       114 , name: "Si cubic diamond 2x2x2 super cell"
     * System   2 :         0 , name: "Si cubic diamond 2x2x2 super cell"
    Maximum number of atoms per element:
     * Element Si :        64

    ********************************************************************************************************************************************

### Main loop
The central part of the ML_LOGFILE is the main loop: depending on the
machine learning mode [ML_MODE](../incar-tags/ML_MODE.md) it contains
data collected over all the time steps (or other iterative schemes)
along the VASP run. The main loop layout is carefully designed to
minimize the file size while at the same being self-descriptive. To
achieve this, it is split into two parts: the description blocks in the
main loop header explain the available data and present its arrangement
in lines and columns. Then, the main loop body contains the actual data
(mostly raw numbers) in the previously defined layout. The separation of
data and its description avoids unnecessary repetition and simplifies
[post-processing](#Post-processing_usage).

#### Header
The main loop header consists of multiple blocks each introducing one of
the log lines appearing later in the loop body. In the example below the
log line `STATUS` is described: there will be 8 columns (counting also
the word `STATUS`) in the given order. The meaning of each column is
also briefly explained here. Next, the log line `STDAB` is outlined with
its 5 columns, and so on...

    * MAIN LOOP ********************************************************************************************************************************

    # STATUS ###############################################################
    # STATUS This line describes the overall status of each step.
    # STATUS 
    # STATUS nstep ..... MD time step or input structure counter
    # STATUS state ..... One-word description of step action
    # STATUS             - "accurate"  (1) : Errors are low, force field is used
    # STATUS             - "threshold" (2) : Errors exceeded threshold, structure is sampled from ab initio
    # STATUS             - "learning"  (3) : Stored configurations are used for training force field
    # STATUS             - "critical"  (4) : Errors are high, ab initio sampling and learning is enforced
    # STATUS             - "predict"   (5) : Force field is used in prediction mode only, no error checking
    # STATUS is ........ Integer representation of above one-word description (integer in parenthesis)
    # STATUS doabin .... Perform ab initio calculation (T/F)
    # STATUS iff ....... Force field available (T/F, False after startup hints to possible convergence problems)
    # STATUS nsample ... Number of steps since last reference structure collection (sample = T)
    # STATUS ngenff .... Number of steps since last force field generation (genff = T)
    # STATUS ###############################################################
    # STATUS            nstep     state is doabin    iff   nsample    ngenff
    # STATUS                2         3  4      5      6         7         8
    # STATUS ###############################################################

    # STDAB ####################################################################
    # STDAB This line contains the standard deviation of the collected ab initio reference data.
    # STDAB
    # STDAB nstep ........ MD time step or input structure counter
    # STDAB std_energy ... Standard deviation in energy (eV atom^-1)
    # STDAB std_force .... Standard deviation in forces (eV Angst^-1)
    # STDAB std_stress ... Standard deviation in stress (kB)
    # STDAB ####################################################################
    # STDAB             nstep       std_energy        std_force       std_stress
    # STDAB                 2                3                4                5
    # STDAB ####################################################################

    ...

|                                                                   |
|-------------------------------------------------------------------|
| **Tip:** The second column is **always** the current (time) step. |

#### Body
Right after the header the main loop body presents the time series of
collected information from the VASP run. The chunks of data belonging to
the same time step are fenced in dashed lines. The keywords, e.g.
`STDAB`, which were described in the header start each line. Usually the
`STATUS` line is located at the beginning of each time step chunk,
summarizing the actions which took place during this step. In the
example below the `STATUS` line indicates "learning", i.e. the machine
learning force field was retrained.

    ...
    --------------------------------------------------------------------------------
    STATUS                 82 learning   3      T      T         0        72
    LCONF                  82 Si      1222      1228
    SPRSC                  82       129       129 Si      1228      1224
    REGR                   82    1    1   1.27238822E+00   5.73175466E-02   7.83203623E-12 
    REGR                   82    1    2   1.28510216E+00   5.73084508E-02   7.75332075E-12 
    REGRF                  82    1    3   1.29486873E+00   5.73015362E-02   7.69391276E-12    2.23430718E+16   5.75166077E+09
    STDAB                  82   1.28851006E-01   1.02791005E+00   1.07081172E+01
    ERR                    82   1.21269596E-02   2.35740491E-01   4.40365370E+00
    CFE                    82   2.71935242E-01   2.20681769E-01   7.30391193E-01
    LASTE                  82   1.63070075E-02   2.66475855E-01   7.17595981E+00
    BEE                    82   4.72039040E-05   1.03291046E-01   3.02999592E-02   9.56824349E-02   6.23077315E-01   4.66683801E-01
    THRHIST                82    1   8.45535075E-02
    THRHIST                82    2   8.99995395E-02
    THRHIST                82    3   9.42765991E-02
    THRHIST                82    4   9.37027237E-02
    THRHIST                82    5   9.78682111E-02
    THRHIST                82    6   1.02991465E-01
    THRHIST                82    7   1.04972577E-01
    THRHIST                82    8   1.02574658E-01
    THRHIST                82    9   9.68150073E-02
    THRHIST                82   10   8.90700596E-02
    THRUPD                 82   9.54674570E-02   9.56824349E-02   6.60216623E-02   1.06906899E-02
    BEEF                   82   4.58511233E-05   9.95065359E-02   2.94732909E-02   9.56824349E-02   6.03276708E-01   4.51396163E-01
    --------------------------------------------------------------------------------
    ...

Note however, that the number and composition of lines in each time step
is not fixed and depends on the actual procedures which were carried
out. As an example, the much shorter block below only contains a
`STATUS` and `BEEF` line because the machine learning force field was
only used for prediction (indicated by "accurate"), so only the Bayesian
error estimate was computed (`BEEF` line):

    ...
    --------------------------------------------------------------------------------
    STATUS                 63 accurate   1      F      T         3        53
    BEEF                   63   4.67236540E-05   1.09788403E-01   2.90204790E-02   9.56824349E-02   6.29349214E-01   4.74949548E-01
    --------------------------------------------------------------------------------
    ...

### Timing information
This last section provides timings of different machine learning program
parts (ab initio code parts are not considered). There are separate
columns for system clock (wall time) and CPU time (summing all threads
of a process).

    * TIMING INFORMATION ***********************************************************************************************************************

    Program part                                         system clock (sec)       cpu time (sec)
    ---------------------------------------------------|--------------------|-------------------
    Setup (file I/O, parameters,...)                   |              0.242 |              0.240
    Descriptor and design matrix                       |             10.540 |             10.536
    Sparsification of configurations                   |              9.183 |              9.177
    Regression                                         |             14.778 |             14.770
    Prediction                                         |             32.461 |             32.450
    ---------------------------------------------------|--------------------|-------------------
    TOTAL                                              |             67.204 |             67.173

    ********************************************************************************************************************************************

## Post-processing usage
Although the main loop design looks complicated at first glance it
serves an important purpose: straightforward post-processing. The time
series of a specific quantity can be easily constructed from the
ML_LOGFILE, just by "searching" for the corresponding keyword. For
example, the evolution of the prediction errors is generated by
extracting all lines starting with the keyword `ERR`. In Linux, this can
be done via the command line tool *grep*:

    grep ERR ML_LOGFILE

An alternative to *grep* in Windows is the *Select-String* tool in the
Powershell:

    Select-String -CaseSensitive -Pattern "ERR" ML_LOGFILE | select-object -ExpandProperty Line

This will combine the contents of the main loop header and body to the
following result:

    # ERR ######################################################################
    # ERR This line contains the RMSEs of the predictions with respect to ab initio results for the training data.
    # ERR 
    # ERR nstep ......... MD time step or input structure counter
    # ERR rmse_energy ... RMSE of energies (eV atom^-1)
    # ERR rmse_force .... RMSE of forces (eV Angst^-1)
    # ERR rmse_stress ... RMSE of stress (kB)
    # ERR ######################################################################
    # ERR               nstep      rmse_energy       rmse_force      rmse_stress
    # ERR                   2                3                4                5
    # ERR ######################################################################
    ERR                     2   8.77652825E-05   1.00592308E-02   2.68800480E-02
    ERR                     3   3.01865279E-05   1.06283576E-02   5.81209819E-02
    ERR                     4   1.52820686E-04   1.31384993E-02   1.10439716E-01
    ERR                     5   1.62739008E-04   1.74252575E-02   1.40488725E-01
    ERR                     6   2.97462508E-04   2.32615279E-02   1.79092561E-01
    ERR                     7   2.10891509E-04   2.79123925E-02   1.94566420E-01
    ERR                     8   3.26150852E-04   3.15081244E-02   1.76637577E-01
    ERR                     9   7.03479132E-04   3.42249550E-02   1.66830771E-01
    ERR                    10   2.41808229E-04   3.54422133E-02   1.80246157E-01
    ERR                    11   2.46299647E-04   3.70102675E-02   2.01262013E-01
    ERR                    12   3.57654922E-04   3.93143970E-02   2.20533745E-01
    ERR                    14   1.95974374E-04   4.31813231E-02   2.44026531E-01
    ERR                    15   4.94080997E-04   4.73774930E-02   2.74308998E-01
    ERR                    16   9.62150633E-04   5.07005683E-02   3.17482301E-01
    ERR                    18   1.31336233E-03   5.39222716E-02   3.25526268E-01
    ERR                    21   1.07020831E-03   5.67663475E-02   3.04995023E-01
    ERR                    24   9.88977484E-04   6.37987961E-02   3.83686143E-01
    ERR                    26   9.63361971E-04   6.81972633E-02   4.92021943E-01
    ERR                    29   1.81730719E-03   7.47758864E-02   6.38563225E-01

The output can be redirected to a file or piped into other
post-processing tools. For example, the prediction error data can be
directly plotted in [gnuplot](http://www.gnuplot.info): first, redirect
the output to a file:

    grep ERR ML_LOGFILE > err.dat

Then, start gnuplot and type:

    p 'err.dat' u 2:4 w l

to show the force error along time steps.

## Collected data
In this section we present additional in-depth information about the
individual time series of data collected in the ML_LOGFILE. As mentioned
above, a short description is already provided directly in the file for
each column of each keyword, e.g.

    # ERR ######################################################################
    # ERR This line contains the RMSEs of the predictions with respect to ab initio results for the training data.
    # ...
    # ERR rmse_force .... RMSE of forces (eV Angst^-1)
    # ...
    # ERR ######################################################################
    # ERR               nstep      rmse_energy       rmse_force      rmse_stress
    # ERR                   2                3                4                5
    # ...

tells us that column 4 in the `ERR` time series corresponds to the root
mean square error of force predictions. However, this statement is not
precise enough because one may write down various definitions of the
force RMSE (e.g. with/without individual weighing of structures with
different numbers of atoms). Here, we collect this kind of background
information which cannot be integrated directly into the log file.

### `STDAB` line
This time series displays the standard deviations of energies, forces
and stress of the training data collected from ab initio simulations. It
gets updated whenever new a new force field is generated during
on-the-fly training (`STATUS` line indicates `learning` or `critical`).
The training data itself is written to the
[ML_ABN](ML_ABN.md) file. Assume that at a given time step
there are $M$ structures with ab initio
data (superscript $\mathsf{dft}$) in the
training data. Also, we define:

- Atomic reference energies per type $\tau$: $\quad e^{\mathsf{ref}}_\tau$
- Number of atoms in structure $i$ of
  type $\tau$: $\quad N_{i,\tau}$

#### Energies
Defining the sum of atomic reference energies in structure
$i$

$\quad E^{\mathsf{ref}}_{i} = \sum_{\tau}
N_{i,\tau} e^{\mathsf{ref}}_\tau$

we can write down the mean energy per atom

$\overline{e^{\mathsf{dft}}} = \frac{1}{M}
\sum_{i=1}^{M} \frac{E^{\mathsf{dft}}_{i} -
E^{\mathsf{ref}}_{i}}{N_i}$

and finally express the standard deviation of energies which is reported
in the `STDAB` line:

$\mathtt{STDAB}_E = \sigma_{E} =
\sqrt{\frac{1}{M} \sum_{i=1}^{M} \left(\frac{E^{\mathsf{dft}}_{i} -
E^{\mathsf{ref}}_{i}}{N_i} - \overline{e^{\mathsf{dft}}}\right)^2}$

#### Forces
Similarly, with the average reference force of component
$\alpha$

$\overline{F^{\mathsf{dft}}_{\alpha}} =
\frac{1}{M} \sum_{i=1}^{M} \frac{1}{N_i} \sum_{j=1}^{N_i}
F^{\mathsf{dft}}_{i,j,\alpha} \quad \mathrm{where} \quad \alpha \in
\\x,y,z\\$

we can define per-component force standard deviations

$\sigma_{F,\alpha} = \sqrt{\frac{1}{M}
\sum_{i=1}^{M} \frac{1}{N_i} \sum_{j=1}^{N_i}
\left(F^{\mathsf{dft}}_{i,j,\alpha} -
\overline{F^{\mathsf{dft}}_{\alpha}}\right)^2} \quad \mathrm{where}
\quad \alpha \in \\x,y,z\\$

and combine them via the root mean square to obtain the output in the
`STDAB` line:

$\mathtt{STDAB}_F = \sqrt{ \frac{1}{M}
\sum_{i=1}^{M} \frac{1}{3N_i} \sum_{j=1}^{N_i}
\sum_{\alpha\in\\x,y,z\} \left( F^{\mathsf{dft}}_{i,j,\alpha} -
\overline{F^{\mathsf{dft}}_{\alpha}}\right)^2 } = \sqrt{
\frac{\sigma_{F,x}^2 + \sigma_{F,y}^2 + \sigma_{F,z}^2}{3} }$

#### Stress
Just like for the forces we define all quantities for the six stress
components separately. First, the average stress

$\overline{S^{\mathsf{dft}}_{\alpha\beta}} =
\frac{1}{M} \sum_{i=1}^{M} S^{\mathsf{dft}}_{\alpha\beta} \quad
\mathrm{where} \quad \alpha\beta \in \\xx,yy,zz,xy,xz,yz\\$

and consequently the per-component standard deviation:

$\sigma_{S,\alpha\beta} = \sqrt{\frac{1}{M}
\sum_{i=1}^{M} \left(S^{\mathsf{dft}}_{\alpha\beta} -
\overline{S^{\mathsf{dft}}_{\alpha\beta}}\right)^2} \quad
\mathrm{where} \quad \alpha\beta \in \\xx,yy,zz,xy,xz,yz\\$

Finally, we obtain the combined (root mean square) stress standard
deviation in the `STDAB` line:

$\mathtt{STDAB}_S = \sqrt{\frac{1}{6M}
\sum_{i=1}^{M} \sum_{\alpha\beta}
\left(S^{\mathsf{dft}}_{\alpha\beta} -
\overline{S^{\mathsf{dft}}_{\alpha\beta}}\right)^2} = \sqrt{
\frac{\sigma_{S,xx}^2 + \sigma_{S,yy}^2 + \sigma_{S,zz}^2 +
\sigma_{S,xy}^2 + \sigma_{S,xz}^2 + \sigma_{S,yz}^2}{6} }$

#### Subset standard deviation
Calculation of mean values $\overline{e^{\mathsf{dft}}}$, $\overline{F^{\mathsf{dft}}_{\alpha}}$, $\overline{S^{\mathsf{dft}}_{\alpha\beta}}$ and respective
standard deviations $\sigma_{E}$,
$\sigma_{F,\alpha}$,
$\sigma_{S,\alpha\beta}$ are modified
for [`ML_IWEIGHT`](../incar-tags/ML_IWEIGHT.md)` = 3` to account for
potentially disconnected regions in the training data. For example,
consider a training data set which contains structures from ab initio MD
simulations of two different crystal structures (e.g. fcc and bcc). The
corresponding potential energies may then be clustered around two mean
values separated by an energy range not represented in the data set.
Computing $\sigma_{E}$ directly from
all energy data would then result in an overestimation of the desired
measure for the data spread. Consequently, also the normalized root mean
square error ($\mathtt{NORME}_E$) would
result in unreasonably low values. It seems natural to split the
calculation of the standard deviation along the clusters, compute
separate values for each subset and finally average the standard
deviations over both sets. In general, we adopt the following strategy
for computing standard deviations for heterogeneous data sets: First,
the training data is split into multiple subsets based on atom types,
number of atoms per type and system names. For details about data set
separation, see [ML_IWEIGHT](../incar-tags/ML_IWEIGHT.md) and
[ML_LUSE_NAMES](../incar-tags/ML_LUSE_NAMES.md). Let us assume we
now have $R$ subsets, where set
$r$ contains $M_r$ structures, i.e.,

$\sum_{r=1}^{R} M_r = M.$

Then, we can compute individual subset energy, force and stress means
$\overline{e^{\mathsf{dft}}_r}$,
$\overline{F^{\mathsf{dft}}_{\alpha,r}}$ and $\overline{S^{\mathsf{dft}}_{\alpha\beta,r}}$ by replacing

$\frac{1}{M} \sum_{i=1}^{M} \quad \rightarrow
\quad \frac{1}{M_r} \sum_{i \in \mathsf{set}_r}$

With these per-subset means and using the same replacement in the
formulae for standard deviations we obtain the per-subset standard
deviations $\sigma_{E,r}$,
$\sigma_{F,\alpha,r}$,
$\sigma_{S,\alpha\beta,r}$. Finally, we
take the root mean square (quadratic mean) to compute an overall
standard deviation for energies, forces and stress:

$\sigma_{E} = \sqrt{ \frac{1}{R} \sum_{r=1}^{R}
\sigma_{E,r}^2 }$

$\sigma_{F,\alpha} = \sqrt{ \frac{1}{R}
\sum_{r=1}^{R} \sigma_{F,\alpha,r}^2 }$

$\sigma_{S,\alpha\beta} = \sqrt{ \frac{1}{R}
\sum_{r=1}^{R} \sigma_{S,\alpha\beta,r}^2 }$

These are the standard deviations which enter the computation of `ERR`
and `NORME`.

### `ERR` line
The `ERR` lines list the root mean square error (RMSE) of energy, force
and stress predictions with respect to the reference data in the
training set. A side-by-side comparison of ab initio vs. predicted
values can be found in the [ML_REG](ML_REG.md) file. In the
following formulae we reuse definitions from the [`STDAB`](#STDAB_line)
section. Furthermore, the superscript $\mathsf{ml}$ is used to denote values predicted by the machine-learned
force field.

#### Energies
$\mathtt{ERR}_E = \sqrt{\frac{1}{M}
\sum_{i=1}^{M} \left(\frac{E^{\mathsf{dft}}_{i} -
E^{\mathsf{ml}}_{i}}{N_i}\right)^2}$

#### Forces
$\mathtt{ERR}_F = \sqrt{ \frac{1}{M}
\sum_{i=1}^{M} \frac{1}{3N_i} \sum_{j=1}^{N_i}
\sum_{\alpha\in\\x,y,z\} \left( F^{\mathsf{ml}}_{i,j,\alpha} -
F^{\mathsf{dft}}_{i,j,\alpha} \right)^2 }$

#### Stress
$\mathtt{ERR}_S = \sqrt{\frac{1}{6M}
\sum_{i=1}^{M} \sum_{\alpha\beta}
\left(S^{\mathsf{ml}}_{\alpha\beta} -
S^{\mathsf{dft}}_{\alpha\beta}\right)^2}$

  

### `NORME` line
|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

The log lines starting with the `NORME` keyword contain a normalized
version of the RMSEs given in the `ERR` line. The "normalizer" used here
is the standard deviation computed from the training data. This quantity
is sometimes abbreviated
NRMSE_($\sigma$) or RSR
(RMSE-observations standard deviation ratio). Values in the `NORME` line
are already multiplied with 100%, i.e., expressed in percent.

#### Energies
$\mathtt{NORME}_E = 100 \\ \cdot
\sqrt{\frac{1}{M} \sum_{i=1}^{M}
\frac{\left(\frac{E^{\mathsf{dft}}_{i} -
E^{\mathsf{ml}}_{i}}{N_i}\right)^2}{\sigma_E^2}} = 100 \\ \cdot
\frac{\mathtt{ERR}_E}{\mathtt{STDAB}_E}$

#### Forces
$\mathtt{NORME}_F = 100 \\ \cdot \sqrt{
\frac{1}{M} \sum_{i=1}^{M} \frac{1}{3N_i} \sum_{j=1}^{N_i}
\sum_{\alpha\in\\x,y,z\} \frac{\left( F^{\mathsf{ml}}_{i,j,\alpha} -
F^{\mathsf{dft}}_{i,j,\alpha} \right)^2}{\sigma_\mathtt{F,\alpha}^2}}$

#### Stress
$\mathtt{NORME}_S = 100 \\ \cdot
\sqrt{\frac{1}{6M} \sum_{i=1}^{M} \sum_{\alpha\beta}
\frac{\left(S^{\mathsf{ml}}_{\alpha\beta} -
S^{\mathsf{dft}}_{\alpha\beta}\right)^2}{\sigma_\mathtt{S,\alpha\beta}^2}}$

### Per-species quantities for forces
|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

Some global quantities (global with respect to the training data set)
given in the output lines of the ML_LOGFILE are also available as
per-atomic-species quantities, i.e., type-resolved results are provided
in additional log lines:

- `ERPS`: per-species RMSE of forces, corresponds to global force RMSE
  in `ERR`
- `NEPS`: per-species NRMSE_($\sigma$)
  of forces, corresponds to global force
  NRMSE_($\sigma$) in `NORME`
- `BEPS`,`BEFPS`: per-species Bayesian error estimate of forces,
  corresponds to global Bayesian error estimate of forces `BEE`,`BEEF`.
- `SPFPS`,`SPFFPS`: per-species spilling factor of forces, corresponds
  to global spilling factor of forces `SF`,`SFF`.

Per-species quantities are computed by replacing in the formulae of the
corresponding global quantities the sum over all atoms with a sum
restricted to atoms of the same type, i.e., if $\mathsf{A}_{i,\tau}$ denotes the set of atom indices of
structure $i$ with type
$\tau$:

$\frac{1}{N_i} \sum_{j=1}^{N_i} \quad \rightarrow
\quad \frac{1}{N_{i,\tau}} \sum_{j \in \mathsf{A}_{i,\tau}}.$

------------------------------------------------------------------------

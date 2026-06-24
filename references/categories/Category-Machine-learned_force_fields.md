<!-- Source: https://vasp.at/wiki/index.php/Category:Machine-learned_force_fields | revid: 36519 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Machine-learned force fields
**Machine-learned force fields** used in combination with ab-initio
[molecular
dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
(MD) allow capturing the underlying physics from first principles and
still reach long simulation times relatively cheaply. Generally, an
ab-initio MD step is computationally expensive due to the
[quantum-mechanical treatment of the
electrons](Category-Electronic_minimization.md),
e.g., within density-functional theory (DFT). In fully classical MD
calculations, **force fields** are used to evaluate the force acting on
each atom instead of DFT. These interatomic potentials are traditionally
based on experimental observation and empirical inclusion of known
forces, such as the van-der-Waals force, electrostatic charges, etc.
Therefore, the quality of the force field depends on how well
interactions in the specific system are known.

VASP offers **machine learning force fields on-the-fly** to overcome
these two issues. Namely, the high computational cost required for
ab-initio MD and the empirical knowledge necessary to construct a force
field the traditional way. To learn more about on-the-fly machine
learning read about the [theory of on-the-fly machine learning force
fields](../methods/Machine_learning_force_field-_Theory.md)
or about the [setup of a basic
calculation](../methods/Machine_learning_force_field_calculations-_Basics.md)!
Also, check out the description on [best practices on how to construct,
test, and retrain force
fields](../methods/Best_practices_for_machine-learned_force_fields.md),
as well as the [basic tutorial that provides hands-on experience for
silicon](https://www.vasp.at/tutorials/latest/md/part2) and this
tutorial: [Liquid Si - MLFF](../misc/Liquid_Si_-_MLFF.md).

## Contents

- [1 Theory](#Theory)
- [2 How to](#How_to)
  - [2.1 Input](#Input)
  - [2.2 Output](#Output)
  - [2.3 Hyperparameters](#Hyperparameters)
- [3 Additional resources](#Additional_resources)
  - [3.1 How to](#How_to_2)
  - [3.2 Tutorials](#Tutorials)
  - [3.3 Lectures](#Lectures)

## Theory
VASP uses a Bayesian-learning algorithm for on-the-fly machine learning.
The total energy and forces are predicted based on the machine-learned
force field at each time step of the MD simulation. If the Bayesian
error estimate exceeds a certain threshold an ab-initio calculation is
performed, where electrons are treated quantum mechanically.
Subsequently, previously untrained atomic environments are identified
and added to a set of so-called local reference configurations. This set
serves as a comparison database for future force field predictions. With
new information in the form of total energy and atomic forces obtained
from the triggered ab-initio calculation the machine-learned force field
is updated and the MD simulation continues. In this way the force field
is iteratively improved in the course of the MD simulation. Ideally, it
will reach such high prediction quality that no more ab-initio
calculations are required.

For details on the algorithm, check out the [theory article about
machine learning force
fields](../methods/Machine_learning_force_field-_Theory.md).

## How to
All related [INCAR tags](Category-INCAR_tag.md)
and [input/output files](Category-Files.md) begin
with the prefix *ML\_*. To learn about machine learning force fields,
visit:

- [Machine learning force field calculations:
  Basics](../methods/Machine_learning_force_field_calculations-_Basics.md).
- [Best practices for machine-learned force
  fields](../methods/Best_practices_for_machine-learned_force_fields.md)
  include how to construct, test, and retrain force fields.
- [Liquid Si - MLFF](../misc/Liquid_Si_-_MLFF.md).
- [Running machine-learned force fields in
  LAMMPS](../methods/Running_machine-learned_force_fields_in_LAMMPS.md)
- [Running GRACE force fields in
  VASP](../methods/Running_GRACE_force_fields_in_VASP.md)

### Input
Depending on whether the calculation is training, retraining, or
applying the force field (see [ML_MODE](../incar-tags/ML_MODE.md)), VASP
may require the following input files in addition to the usual [input
files](Category-Input_files.md)
([INCAR](../input-files/INCAR.md), [POSCAR](../input-files/POSCAR.md), etc.):

- [ML_AB](../input-files/ML_AB.md) Ab-initio training data.
- [ML_FF](../input-files/ML_FF.md) Force-field parameters.

### Output
The machine-learning–force-field method generates the following [output
files](https://vasp.at/wiki/index.php/Category:Output_files):

- [ML_LOGFILE](../output-files/ML_LOGFILE.md) Main output file.
- [ML_ABN](../output-files/ML_ABN.md) Generated ab-initio training data. It
  is used as [ML_AB](../input-files/ML_AB.md) file to restart a calculation.
- [ML_REG](../output-files/ML_REG.md) Summary of regression results.
- [ML_HIS](../output-files/ML_HIS.md) Summary of the histogram data.
- [ML_FFN](../output-files/ML_FFN.md) Force-field parameters. It is used as
  [ML_FF](../input-files/ML_FF.md) file to restart a calculation.
- [ML_EATOM](../output-files/ML_EATOM.md) Local atomic energies.
- [ML_HEAT](../output-files/ML_HEAT.md) Local heat flux.

### Hyperparameters
Hyperparameters are user-defined parameters of the MLFF model that will
not be optimized during training of the MLFF. For instance, cutoff radii
([ML_RCUT1](../incar-tags/ML_RCUT1.md),
[ML_RCUT2](../incar-tags/ML_RCUT2.md)), the normalization and weighting
of ab-initio training data ([ML_IWEIGHT](../incar-tags/ML_IWEIGHT.md),
[ML_WTOTEN](../incar-tags/ML_WTOTEN.md),
[ML_WTIFOR](../incar-tags/ML_WTIFOR.md),
[ML_WTSIF](../incar-tags/ML_WTSIF.md)) , threshold and the total number
of descriptors in the sparsification
([ML_EPS_LOW](../incar-tags/ML_EPS_LOW.md),
[ML_RDES_SPARSDES](../incar-tags/ML_RDES_SPARSDES.md)). We
recommend optimizing these in cross-validation by means of
systematically varying the parameters and refitting the force field
([ML_MODE](../incar-tags/ML_MODE.md)=refit). In principle, it is
necessary to do that for all hyperparameters available in VASP to obtain
the best MLFF model. In practice, usually the default values are a good
guess. The default parameters of VASP were optimized on a selected set
of bulk materials and on a molecular data base.

## Additional resources
### How to
- Training an [MLFF for transition states using
  metadynamics](../methods/Using_metadynamics_to_train_a_machine-learned_force_field.md).

### Tutorials
- Tutorial for [training a machine learning force field using
  MD](https://www.vasp.at/tutorials/latest/md/part2).
- Tutorial for [error analysis and hyperparameter
  optimization](https://www.vasp.at/tutorials/latest/mlff/part1).

### Lectures
- Lecture on the [basics of machine learning force
  fields](https://youtu.be/f1VXKVlVhg4)
- Lecture on [machine learning force
  fields](https://youtu.be/HgGwgtkwh7g)
- Lecture on [chemical reactions using
  MLFFs](https://youtu.be/bzzHpTBwxbA)

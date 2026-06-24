<!-- Source: https://vasp.at/wiki/index.php/OUTCAR | revid: 36630 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# OUTCAR
There are three main output files: OUTCAR in human-readable format,
[vasprun.xml](Vasprun.xml.md) in xml format, and
[vaspout.h5](Vaspout.h5.md) in HDF5 format. The OUTCAR
file gives detailed human-readable output of a VASP run with roughly the
following format:

- A summary of the used input parameters (e.g.,
  [INCAR](../input-files/INCAR.md) tags), the starting structure (cf.
  [POSCAR](../input-files/POSCAR.md)), the k-point mesh (cf.
  [KPOINTS](../input-files/KPOINTS.md)), and the pseudopotentials used
  (cf. [POTCAR](../input-files/POTCAR.md) and [choosing
  pseudopotentials](../tutorials/Choosing_pseudopotentials.md)).
- Information about the [electronic
  steps](../tutorials/Setting_up_an_electronic_minimization.md),
  KS-eigenvalues.
- Stress tensors.
- [Forces](../methods/Category-Forces.md) on the atoms.
- Local charges and [magnetic
  moments](../categories/Category-Magnetism.md).
- [Dielectric
  properties](../categories/Category-Dielectric_properties.md)
- The amount of output written onto the OUTCAR file can be chosen by
  modifying the [NWRITE](../incar-tags/NWRITE.md) tag in the
  [INCAR](../input-files/INCAR.md) file.

## Contents

- [1 INCAR tags](#INCAR_tags)
  - [1.1 Common tags](#Common_tags)
  - [1.2 Property tags](#Property_tags)
- [2 Related tags and articles](#Related_tags_and_articles)

## INCAR tags
### Common tags
The output to the OUTCAR file is determined by
[INCAR](../input-files/INCAR.md) tags. The output for these is documented on
their respective tag or how-to pages. Some of the most common tags are:

- the [IBRION](../incar-tags/IBRION.md) tag selects [structure
  optimization](../tutorials/Structure_optimization.md) -
  [`IBRION`](../incar-tags/IBRION.md)` = 1-3`, [molecular dynamics
  (MD)](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
  calculations - [`IBRION`](../incar-tags/IBRION.md)` = 0`, or
  [phonon](../categories/Category-Phonons.md) calculations -
  [`IBRION`](../incar-tags/IBRION.md)` = 5-6`.
- [ISIF](../incar-tags/ISIF.md) selects for degrees of ionic and structural
  freedom in structural optimization and MD.
- [ALGO](../incar-tags/ALGO.md) is used to define the electronic
  minimization algorithm that is used or to select the [many-body
  perturbation
  theory](../categories/Category-Many-body_perturbation_theory.md)
  (MBPT) algorithm, e.g., the [GW](../theory/Category-GW.md)
  approximation, the [random-phase
  approximation](../methods/RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md)
  (RPA), the [Bethe-Salpeter
  equation](../theory/Category-Bethe-Salpeter_equations.md)
  (BSE).

### Property tags
There are also many tags for specific properties, such as
[electron-phonon
interactions](../categories/Category-Electron-phonon_interactions.md)
(cf. the long list of `ELPH_` tags at the end of the category page),
[nuclear magnetic resonance](../categories/Category-NMR.md) (NMR) -
e.g., chemical shielding ([LCHIMAG](../incar-tags/LCHIMAG.md)), electric
field gradient EFG ([LEFG](../incar-tags/LEFG.md)), etc.

There are several other output files which we summarize below, along
with several common tags for

## Related tags and articles
- Output and input files: [INCAR](../input-files/INCAR.md),
  [POSCAR](../input-files/POSCAR.md), [KPOINTS](../input-files/KPOINTS.md),
  [POTCAR](../input-files/POTCAR.md), [OSZICAR](OSZICAR.md),
  [IBZKPT](IBZKPT.md), [CHGCAR](../input-files/CHGCAR.md),
  [WAVECAR](../input-files/WAVECAR.md),
  [vasprun.xml](Vasprun.xml.md),
  [vaspout.h5](Vaspout.h5.md).
- Controlling output verbosity: [NWRITE](../incar-tags/NWRITE.md).
- Output-controlling tags: [chemical
  shielding](../incar-tags/LCHIMAG.md), [electric field
  gradient](../incar-tags/LEFG.md), [hyperfine coupling
  constant](../incar-tags/LHYPERFINE.md), [dielectric
  function](../incar-tags/LOPTICS.md), [Born effective charges and
  dielectric tensor (DFPT)](../incar-tags/LEPSILON.md), [Born effective
  charges (finite-differences)](../incar-tags/LCALCEPS.md), [X-ray
  core-level binding energies](../incar-tags/ICORELEVEL.md),
  [optics](../incar-tags/ALGO.md), [density of states
  (DOS)](../incar-tags/LORBIT.md).

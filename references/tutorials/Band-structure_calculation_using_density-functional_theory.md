<!-- Source: https://vasp.at/wiki/index.php/Band-structure_calculation_using_density-functional_theory | revid: 35413 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Band-structure calculation using density-functional theory
The step-by-step instructions below cover calculating the [band
structure](../categories/Category-Band_structure.md)
within density-functional theory (DFT), including references to
practical examples.

Obtaining the band structure involves first solving the Hamiltonian to
get eigenvalues and eigenvectors, then plotting them as electronic
energy levels versus [crystal
momentum](../redirects/Crystal_momentum.md). The Kohn-Sham (KS)
Hamiltonian requires at least the density (charge and possibly
magnetization) and may contain higher derivatives depending on the
[exchange-correlation (XC)
functional](../categories/Category-Exchange-correlation_functionals.md).

|  |
|----|
| **Mind:** The approach presented on this page applies to [LDA](../incar-tags/GGA.md) (needs density), [GGA](../incar-tags/GGA.md) (needs density and gradient), and deorbitalized meta-GGA (needs density, gradient, and Laplacian) functionals. Additionally, it can be used for [meta-GGAs](../incar-tags/METAGGA.md) that need the kinetic energy density as of VASP 6.6.0. In contrast, another approach is required [for computing the band structure for hybrid functionals](../methods/Band-structure_calculation_using_hybrid_functionals.md) and [for computing the band structure for MGGAs before VASP 6.6.0](../methods/Band-structure_calculation_using_hybrid_functionals.md). |

## Contents

- [1 Step-by-step instructions](#Step-by-step_instructions)
  - [1.1 Option A: Single run](#Option_A:_Single_run)
    - [1.1.1 Step 1: Prepare SCF
      settings](#Step_1:_Prepare_SCF_settings)
    - [1.1.2 Step 2: High-symmetry path](#Step_2:_High-symmetry_path)
    - [1.1.3 Step 3: Run the calculation](#Step_3:_Run_the_calculation)
    - [1.1.4 Step 4: Plot the band
      structure](#Step_4:_Plot_the_band_structure)
  - [1.2 Option B: Split run](#Option_B:_Split_run)
    - [1.2.1 Step 1: Set up and perform a full SCF
      calculation](#Step_1:_Set_up_and_perform_a_full_SCF_calculation)
    - [1.2.2 Step 2 (optionally): Create a
      backup](#Step_2_(optionally):_Create_a_backup)
    - [1.2.3 Step 3: High-symmetry path](#Step_3:_High-symmetry_path)
    - [1.2.4 Step 4: Prepare a restart with fixed
      density](#Step_4:_Prepare_a_restart_with_fixed_density)
    - [1.2.5 Step 5: Run the NSCF
      calculation](#Step_5:_Run_the_NSCF_calculation)
    - [1.2.6 Step 6: Plot the band
      structure](#Step_6:_Plot_the_band_structure)
- [2 Choosing a high-symmetry path](#Choosing_a_high-symmetry_path)
- [3 Recommendations and advice](#Recommendations_and_advice)
- [4 Practical examples](#Practical_examples)
- [5 Related tags and articles](#Related_tags_and_articles)
- [6 References](#References)

## Step-by-step instructions
|  |
|----|
| **Tip:** [Option A: Single run](#Option_A:_Single_run) is convenient, because it does not require restarting the calculation. On the other hand, there is less control, e.g., over the used algorithm ([ALGO](../incar-tags/ALGO.md)), and depending on the number of **k** points on the regular mesh and the [parallelization](../redirects/Parallelization.md), it can be less performant than [Option B: Split run](#Option_B:_Split_run). |

### Option A: Single run
|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.3.0 |

#### Step 1: Prepare SCF settings
Follow [the steps to create input
files](Setting_up_an_electronic_minimization.md)
on the instructions for [setting up an electronic
minimization](Setting_up_an_electronic_minimization.md).
Typically, this involves defining the input settings using the
[INCAR](../input-files/INCAR.md), [POSCAR](../input-files/POSCAR.md),
[KPOINTS](../input-files/KPOINTS.md), and [POTCAR](../input-files/POTCAR.md)
files.

#### Step 2: High-symmetry path
[Choose a high-symmetry path](#Choosing_a_high-symmetry_path) and set it
in the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file. Both
[KPOINTS](../input-files/KPOINTS.md) and
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) define crystal momenta:
The [KPOINTS](../input-files/KPOINTS.md) file holds the regular **k** mesh
for the initial SCF computation, while the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file holds the
high-symmetry path usually in line mode along which the band structure
will be evaluated.

#### Step 3: Run the calculation
Start the VASP run, which will internally perform an SCF run to obtain
the converged KS orbitals and densities, and then perform the NSCF run
at fixed density to evaluate the eigenvalues along the high-symmetry
path. The progress is written to **stdout**. For more detailed
suggestions on [optimizing your
settings](Setting_up_an_electronic_minimization.md)
and [running the
calculation](Setting_up_an_electronic_minimization.md)
check the article on [setting up an electronic
minimization](Setting_up_an_electronic_minimization.md).

#### Step 4: Plot the band structure
[py4vasp](https://vasp.at/py4vasp/latest/calculation/band/#py4vasp.calculation._band.Band.to_graph)
provides utilities for plotting the band structure. Run the following in
a Python notebook in the directory of the calculation:

    import py4vasp
    calc = py4vasp.Calculation.from_path(".")
    ef = calc.dos.read()["fermi_energy"]
    calc.band.plot("kpoints_opt", fermi_energy=ef)

|  |
|----|
| **Tip:** Set the [EFERMI](../incar-tags/EFERMI.md) tag or pass the Fermi energy explicitly, because [py4vasp](https://vasp.at/py4vasp/latest/index.html) reads the Fermi energy from the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) density of states (`results/electron_dos_kpoints_opt/efermi`), which is computed from the line-mode **k** points and is therefore unreliable. |

### Option B: Split run
In a nutshell, the KS Hamiltonian within DFT can be expressed in terms
of the electronic charge and possibly the magnetization density. Both
are written to the [CHGCAR](../input-files/CHGCAR.md) file during an
initial self-consistent-field (SCF) run. From this converged
[CHGCAR](../input-files/CHGCAR.md) file, we can obtain the eigenvalues at
the desired [high-symmetry path](#Choosing_a_high-symmetry_path) via a
subsequent non-self-consistent-field (NSCF) run at fixed density.

#### Step 1: Set up and perform a full SCF calculation
Follow the steps described in [setting up an electronic
minimization](Setting_up_an_electronic_minimization.md).

|  |
|----|
| **Important:** Set [`LMAXMIX`](../incar-tags/LMAXMIX.md)` = 4` for d-electron systems and [`LMAXMIX`](../incar-tags/LMAXMIX.md)` = 6` for f-electron systems to adjust the maximum l-quantum number up to which the one-center PAW charge densities are written to the [CHGCAR](../input-files/CHGCAR.md) file. If you are unsure about the appropriate value for [LMAXMIX](../incar-tags/LMAXMIX.md), restart with fixed density using the regular **k** mesh and check that the total energy is identical to the SCF run. |

#### Step 2 (optionally): Create a backup
The simplest procedure is to create a new directory for the
band-structure calculation and copy the input files of the SCF
calculation (usually the [INCAR](../input-files/INCAR.md) file,
[POSCAR](../input-files/POSCAR.md) file, and the
[POTCAR](../input-files/POTCAR.md) file) as well as the
[CHGCAR](../input-files/CHGCAR.md) file to the new directory.

[TABLE]

Alternatively, backup the [OUTCAR](../output-files/OUTCAR.md) file,
[KPOINTS](../input-files/KPOINTS.md) file and possibly the
[OSZICAR](../output-files/OSZICAR.md) file and
[vaspout.h5](../output-files/Vaspout.h5.md) to be able to reconstruct
the SCF calculation, if needed.

#### Step 3: High-symmetry path
[Choose a high-symmetry path](#Choosing_a_high-symmetry_path) and set it
in the [KPOINTS](../input-files/KPOINTS.md) file.

#### Step 4: Prepare a restart with fixed density
Adjust the [INCAR](../input-files/INCAR.md) file:

- Remove any of the following tags, if present: [NSW](../incar-tags/NSW.md),
  [IBRION](../incar-tags/IBRION.md) and [ISTART](../incar-tags/ISTART.md).
- Add [`ICHARG`](../incar-tags/ICHARG.md)` = 11`. This restarts from the
  converged charge density read from the [CHGCAR](../input-files/CHGCAR.md)
  file and continues with the density held fixed.
- Add additional relevant tags as needed, i.e.,
  [LORBIT](../incar-tags/LORBIT.md)=11.

[TABLE]

#### Step 5: Run the NSCF calculation
Perform the NSCF calculation with the prepared files. This will read the
[CHGCAR](../input-files/CHGCAR.md) file and keep the density fixed.

|  |
|----|
| **Mind:** Any existing [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file triggers **[Option A](#Option_A:_Single_run)** unless you disable this by setting [`LKPOINTS_OPT`](../incar-tags/LKPOINTS_OPT.md)` = F`. |

#### Step 6: Plot the band structure
[py4vasp](https://vasp.at/py4vasp/latest/calculation/band/#py4vasp.calculation._band.Band.to_graph)
provides utilities for plotting the band structure. Run the following in
a Python notebook in the directory of the calculation:

    import py4vasp
    calc = py4vasp.Calculation.from_path(".")
    calc.band.plot()

[TABLE]

## Choosing a high-symmetry path
Band-structure calculations generally compute the **Kohn-Sham orbitals**
and eigenenergies along a path in reciprocal space which usually
connects high-symmetry points in the first **Brillouin zone**. Which
**k** points are high-symmetry points depends on the **space group** of
the structure.

Use external
tools^([\[1\]](#cite_note-seekpath-1)[\[2\]](#cite_note-bilbao:kvec-2))
to find the space group, plot the Brillouin zone, and pick a
high-symmetry **k** path. Extract the corresponding coordinates and
provide them in [KPOINTS](../input-files/KPOINTS.md)-file format, either
as a list of [explicit
coordinates](../input-files/KPOINTS.md) or (more
commonly) using [line
mode](../input-files/KPOINTS.md).

|  |
|----|
| **Tip:** The tools provide the coordinates and the labels for a given structure. Because these paths depend on the symmetry, take special care that the analysis is not tainted by finite precision or rounding (see [SYMPREC](../incar-tags/SYMPREC.md)). Also, keep in mind that the primitive and the conventional unit cell have different reciprocal coordinate systems. |

Example high-symmetry path for face-centered-cubic silicon:

     k points for band structure
     10  ! intersections 
     line
     Fractional
       0.50000  0.50000  0.50000   L
       0.00000  0.00000  0.00000   Γ
       
       0.00000  0.00000  0.00000   Γ
       0.00000  0.50000  0.50000   X
       
       0.00000  0.50000  0.50000   X
       0.25000  0.62500  0.62500   U
       
       0.37500  0.7500   0.37500   K
       0.00000  0.00000  0.00000   Γ

The empty lines and labels are optional and meant for readability. The
labels will be used by
[py4vasp](https://vasp.at/py4vasp/latest/index.html). VASP produces
equidistant **k** points for each segment. The example above would yield
10 points from *L* to *Γ*, 10 points from *Γ* to *X*, 10 from *X* to
*U*, and 10 from *K* to *Γ*, including endpoints. For further details
and instructions, please consult the section on [band-structure
calculations in the
KPOINTS](../input-files/KPOINTS.md)
documentation.

## Recommendations and advice
In case a [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file is present
([Option A](#Option_A:_Single_run)), VASP computes the band energies for
the **k** points of the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md)
file after SCF convergence is reached within the same submitted job.
There may, however, be a **computational advantage** to splitting the
run ([Option B](#Option_B:_Split_run)) because of different optimal
batching options for the **k** mesh.

There are additional advantages to using the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file for computing the
band structure [using hybrid
functionals](../methods/Band-structure_calculation_using_hybrid_functionals.md)
or [using meta-GGA
functionals](../methods/Band-structure_calculation_using_meta-GGA_functionals.md).
Refer to these references for details.

A number of **post-processing options** for the Kohn-Sham (KS) orbitals
can affect the computation of the band structure. Usually, these options
are set directly in the [INCAR](../input-files/INCAR.md) file: See, for
example, [LORBIT](../incar-tags/LORBIT.md)=11 or [constructing Wannier
orbitals](Constructing_Wannier_orbitals.md).

## Practical examples
We offer additional tutorials for calculating and visualizing DFT band
structures:

- [Bulk systems, Part
  1](https://www.vasp.at/tutorials/latest/bulk/part1/#bulk-e03): band
  structure of face-centered-cubic silicon.

&nbsp;

- [Bulk systems, Part
  2](https://www.vasp.at/tutorials/latest/bulk/part2/#Step-3.)): band
  structure of cubic-diamond silicon.

&nbsp;

- [Bulk systems, Part
  3](https://www.vasp.at/tutorials/latest/bulk/part3/#Step-3.)): band
  structure of face-centered-cubic nickel.

## Related tags and articles
[KPOINTS](../input-files/KPOINTS.md),
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md),

[ICHARG](../incar-tags/ICHARG.md), [LMAXMIX](../incar-tags/LMAXMIX.md)

[XC functionals](../redirects/XC_functionals.md), [Setting up an
electronic
minimization](Setting_up_an_electronic_minimization.md)

[Band-structure calculation using meta-GGA
functionals](../methods/Band-structure_calculation_using_meta-GGA_functionals.md),
[Band-structure calculation using hybrid
functionals](../methods/Band-structure_calculation_using_hybrid_functionals.md)

## References
1.  [↑](#cite_ref-seekpath_1-0)
    [www.materialscloud.org/work/tools/seekpath
    (2022).](https://www.materialscloud.org/work/tools/seekpath)
2.  [↑](#cite_ref-bilbao:kvec_2-0) [www.cryst.ehu.es/cryst/get_kvec.html
    (2022).](https://www.cryst.ehu.es/cryst/get_kvec.html)

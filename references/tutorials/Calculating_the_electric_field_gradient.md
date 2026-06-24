<!-- Source: https://vasp.at/wiki/index.php/Calculating_the_electric_field_gradient | revid: 36055 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Calculating the electric field gradient
Nuclei with a spin \> ± ½ are called quadrupolar nuclei. They have a
non-spherical shape and therefore a non-zero electric field gradient
(EFG) at the nucleus. The EFG is calculated using
[LEFG](../incar-tags/LEFG.md) ^([\[1\]](#cite_note-petrilli:prb:1998-1)). By
including the quadrupole moment of the isotopes, the quadrupole coupling
constants *C_(q)* can be calculated (multiple definitions exist in the
literature, ensure that you are correctly comparing). These are measured
using nuclear quadrupole resonance (NQR) spectroscopy, a type of zero-
to ultralow-field (ZULF) NMR, NMR, and Mössbauer spectroscopy. The
theory is covered in the [NMR category
page](../categories/Category-NMR.md) and [LEFG](../incar-tags/LEFG.md)
page.

## Contents

- [1 Step-by-step instructions](#Step-by-step_instructions)
  - [1.1 Step 1 (optional): Calculate the electric field gradient using
    a previously converged
    calculation](#Step_1_(optional):_Calculate_the_electric_field_gradient_using_a_previously_converged_calculation)
  - [1.2 Step 2a: Define the nuclear quadrupolar
    moments](#Step_2a:_Define_the_nuclear_quadrupolar_moments)
  - [1.3 Step 2b (optional): Determine a suitable energetic break
    value](#Step_2b_(optional):_Determine_a_suitable_energetic_break_value)
  - [1.4 Step 3: Converge the plane-wave energy
    cutoff](#Step_3:_Converge_the_plane-wave_energy_cutoff)
  - [1.5 Step 4: Converge the **k** point
    mesh](#Step_4:_Converge_the_k_point_mesh)
  - [1.6 Step 5: Compare to experiment](#Step_5:_Compare_to_experiment)
- [2 Recommendations and advice](#Recommendations_and_advice)
  - [2.1 Structure](#Structure)
  - [2.2 PAW pseudopotentials](#PAW_pseudopotentials)
  - [2.3 Additional tags](#Additional_tags)
- [3 Example scripts for convergence
  tests](#Example_scripts_for_convergence_tests)
  - [3.1 Energetic break criterion
    tests](#Energetic_break_criterion_tests)
  - [3.2 **k**-points tests](#k-points_tests)
  - [3.3 Energy cutoff tests](#Energy_cutoff_tests)
  - [3.4 Related tags and articles](#Related_tags_and_articles)
  - [3.5 References](#References)

## Step-by-step instructions
The electric field gradient is calculated post-self-consistent field
(post-SCF) using [LEFG](../incar-tags/LEFG.md). A well-converged SCF
calculation is therefore crucial. The electric field gradient is very
sensitive to several input parameters that must all be independently
tested. In particular, small differences in the structure can make big
differences to $V_{zz}$, up to 50 %
^([\[1\]](#cite_note-petrilli:prb:1998-1)); see the Advice section for
more details. Make sure to have a well-optimized structure before you
begin the convergence tests.

### Step 1 (optional): Calculate the electric field gradient using a previously converged calculation
Since the electric field gradient is calculated post-SCF, you can use a
previously converged [WAVECAR](../input-files/WAVECAR.md) with
[ISTART](../incar-tags/ISTART.md) = 1 and [NELM](../incar-tags/NELM.md) = 1.
The corresponding density, [CHGCAR](../input-files/CHGCAR.md) is calculated
from the [WAVECAR](../input-files/WAVECAR.md) file before the first
elementary step so it need not be included.

### Step 2a: Define the nuclear quadrupolar moments
The calculated electric field gradients are not observable in
experiment. Instead, the quadrupolar coupling constant can be calculated
so long as the nuclear quadrupolar moments are defined in
[QUAD_EFG](../incar-tags/QUAD_EFG.md). Each species in your
[POSCAR](../input-files/POSCAR.md) file should be defined; there is no need
to define each individual ion. A short table of values can be found in
Ref. ^([\[2\]](#cite_note-pyykko:molphys:2017-2)).

### Step 2b (optional): Determine a suitable energetic break value
The break condition for the self-consistency step
[EDIFF](../incar-tags/EDIFF.md) strongly influences the chemical shielding.
A setting of [EDIFF](../incar-tags/EDIFF.md) = 1E-8 eV is generally
recommended. Convergence is taken to be within 0.1 ppm.

### Step 3: Converge the plane-wave energy cutoff
A large plane-wave energy cutoff is required to fully converge the
electric field gradient. Perform multiple calculations while increasing
the basis set size, as defined in [ENCUT](../incar-tags/ENCUT.md),
incrementally (e.g., by 100 eV intervals). Convergence should be aimed
to be within 3 significant figures, although this will not be feasible
for heavier elements.

### Step 4: Converge the **k** point mesh
Similar to the basis, the **k** point mesh can strongly influence the
coupling constant. The **k** point mesh should be increased
incrementally, i.e., 1x1x1, 2x2x2, 3x3x3, until convergence within 3
significant figures is achieved. It is only necessary to converge the
**k** point mesh for crystals, gas-phase molecules should use the
Γ-point only.

### Step 5: Compare to experiment
The purpose of these calculations is to compare directly to experiment.
The EFG that has been calculated is not directly measurable but the
quadrupolar coupling constants *C_(q)* are.

## Recommendations and advice
Calculating the electric field gradient requires tightly converged
settings. As described in the step-wise introduction above, converging
with respect to [EDIFF](../incar-tags/EDIFF.md),
[ENCUT](../incar-tags/ENCUT.md), and the **k** point mesh is very
important. There are a few additional settings that should be
considered.

[TABLE]

### Structure
The electric field gradient can be **extremely** dependent on structure,
to the extent that using the experimental structure can improve results.
A small difference in the positions of atoms can make a huge difference
to the EFG. For the O in TiO₂ rutile, a shift in position from 0.305 in
internal coordinates to 0.3025 made a difference of 50 % to
$V_{zz}$ for the Ti
^([\[1\]](#cite_note-petrilli:prb:1998-1)). This is an atypical case but
highlights the importance of using a [well-optimized
structure](Structure_optimization.md),
ideally the experimental structure if available. This extreme
sensitivity to the structure is indicative of why the quadrupolar
coupling constant is so useful for determining information about a
system's chemical environment.

### PAW pseudopotentials
The standard [PAW
pseudopotentials](../categories/Category-Pseudopotentials.md)
[POTCAR](../input-files/POTCAR.md) used are sufficient for calculating the
electric field gradient. Using [GW
pseudopotentials](../input-files/Available_pseudopotentials.md)
can significantly improve results. Semi-core electrons can be important,
so [POTCAR](../input-files/POTCAR.md) files with *\*\_pv* or *\*\_sv* can
improve the results, as will the explicit inclusion of augmentation
channels with $d$-projectors.

### Additional tags
To ensure tight precision, the precision should be set to
[`PREC`](../incar-tags/PREC.md)` = Accurate`, rather than `Normal`. The
[LASPH](../incar-tags/LASPH.md) should be set to `.TRUE.`, turning on the
non-spherical contributions to the gradient of the density inside the
PAW spheres.

# Example scripts for convergence tests
Several tests are necessary to obtain various NMR parameters. Make sure
to change the example [INCAR](../input-files/INCAR.md) files to include the
tags for your desired calculation. We provide some example scripts
below:

|  |
|----|
| **Important:** Make sure to replace the [QUAD_EFG](../incar-tags/QUAD_EFG.md) in the [INCAR](../input-files/INCAR.md) with the values for the isotopes in your system. |

## Energetic break criterion tests
For converging the energetic break criterion for a single ionic step
([EDIFF](../incar-tags/EDIFF.md)), start with the 1E-4 and then increase by
orders of magnitude:

Energetic break criterion: **INCAR.nmr**

    ENCUT = 400              
    ISMEAR = 0; SIGMA = 0.01 
    EDIFF = 1E-4             
    PREC = Accurate          
    LASPH = .TRUE.           
    LEFG = .TRUE.            
    QUAD_EFG = 0. -696. 20.44 0. 2.860  # Nuclear quadrupolar moments for Pb I N O D
    LNMRCAR = .TRUE. 

Script to loop through [EDIFF](../incar-tags/EDIFF.md) from 1E-4 eV to 1E-8
eV:

    for a in 4 5 6 7 8
    do
    cp INCAR.nmr INCAR
    sed -i "s/1E-4/1E-$a/g" INCAR

    mpirun -np 4 $PATH_TO_EXECUTABLE/vasp_std

    cp OUTCAR OUTCAR.$a
    done

## **k**-points tests
For converging **k** points, start with the Γ-point and increase the
**k**-point mesh incrementally:

Initial Γ-only mesh: **KPOINTS.nmr**

    C
    0
    G
     1 1 1
     0 0 0

Script to go through **k**-point meshes from Γ-only to 8x8x8:

    for a in 1 2 4 6 8
    do
    cp KPOINTS.nmr KPOINTS
    sed -i "s/1 1 1/$a $a $a/g" KPOINTS

    mpirun -np 4 $PATH_TO_EXECUTABLE/vasp_std

    cp OUTCAR OUTCAR.$a
    done

## Energy cutoff tests
For converging the energy cutoff, start from at least the value of ENMAX
given in the [POTCAR](../input-files/POTCAR.md) file and then increase
incrementally in steps of 100 eV:

Initial [INCAR](../input-files/INCAR.md): **INCAR.nmr**

    ENCUT = 400              
    ISMEAR = 0; SIGMA = 0.01 
    EDIFF = 1E-8             
    PREC = Accurate          
    LASPH = .TRUE.           
    LEFG = .TRUE.            
    QUAD_EFG = 0. -696. 20.44 0. 2.860  # Nuclear quadrupolar moments for Pb I N O D

Script to loop through [ENCUT](../incar-tags/ENCUT.md) from 400 eV to 800
eV:

    for a in 400 500 600 700 800
    do
    cp INCAR.nmr INCAR
    sed -i "s/400/$a/g" INCAR

    mpirun -np 4 $PATH_TO_EXECUTABLE/vasp_std

    cp OUTCAR OUTCAR.$a
    done

## Related tags and articles
[LEFG](../incar-tags/LEFG.md), [QUAD_EFG](../incar-tags/QUAD_EFG.md)

## References
1.  ↑ ^([a](#cite_ref-petrilli:prb:1998_1-0))
    ^([b](#cite_ref-petrilli:prb:1998_1-1))
    ^([c](#cite_ref-petrilli:prb:1998_1-2)) [H. M. Petrilli, P. E.
    Blöchl, P. Blaha, and K. Schwarz, *Electric-field-gradient
    calculations using the projector augmented wave method*, Phys. Rev.
    B **57**, 14690 (1998).](https://doi.org/10.1103/PhysRevB.57.14690)
2.  [↑](#cite_ref-pyykko:molphys:2017_2-0) [P. Pyykkö, *Year-2017
    nuclear quadrupole moments*, Mol. Phys. **116**, 1328-1338
    (2018).](https://doi.org/10.1080/00268976.2018.1426131)

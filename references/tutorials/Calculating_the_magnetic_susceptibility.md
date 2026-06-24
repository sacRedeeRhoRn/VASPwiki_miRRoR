<!-- Source: https://vasp.at/wiki/index.php/Calculating_the_magnetic_susceptibility | revid: 30746 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Calculating the magnetic susceptibility
The [magnetic susceptibility](../incar-tags/LCHIMAG.md)
$\chi$ is the degree of magnetization of
a material in response to an applied magnetic field. It is a bulk
property, in contrast to the chemical shielding, which is for each
nucleus. Like the chemical shielding, the magnetic susceptibility is
calculated by linear response using [LCHIMAG](../incar-tags/LCHIMAG.md)
^([\[1\]](#cite_note-pickard:prb:2001-1)[\[2\]](#cite_note-yates:prb:2007-2)),
so they will both be shown in the same [OUTCAR](../output-files/OUTCAR.md)
file. The magnetic susceptibility is measured using the Guoy balance (or
method); alternatively, an Evans or Faraday balance can be used. The
theory is covered in the [NMR category
page](../categories/Category-NMR.md) and
[LCHIMAG](../incar-tags/LCHIMAG.md) page.

## Contents

- [1 Step-by-step instructions](#Step-by-step_instructions)
- [2 Recommendations and advice](#Recommendations_and_advice)
  - [2.1 PAW pseudopotentials](#PAW_pseudopotentials)
  - [2.2 Additional tags](#Additional_tags)
- [3 Example scripts for convergence
  tests](#Example_scripts_for_convergence_tests)
  - [3.1 Energetic break criterion
    tests](#Energetic_break_criterion_tests)
  - [3.2 **k**-points tests](#k-points_tests)
  - [3.3 Energy cutoff tests](#Energy_cutoff_tests)
  - [3.4 Related tags and articles](#Related_tags_and_articles)
  - [3.5 References](#References)

## Step-by-step instructions
The magnetic susceptibility is calculated post-self-consistent field
(post-SCF) using [LCHIMAG](../incar-tags/LCHIMAG.md). A well-converged
SCF calculation is therefore crucial. The magnetic susceptibility can be
sensitive to several input parameters that must all be independently
tested.

**Step 1 (optional):** Calculate the magnetic susceptibility using a
previously converged calculation

Since the magnetic susceptibility is calculated post-SCF, you can use a
previously converged [WAVECAR](../input-files/WAVECAR.md) with
[ISTART](../incar-tags/ISTART.md) = 1 and [NELM](../incar-tags/NELM.md) = 1.
The corresponding density, [CHGCAR](../input-files/CHGCAR.md) is calculated
from the [WAVECAR](../input-files/WAVECAR.md) file before the first
elementary step so it need not be included.

**Step 2 (optional):** Determine a suitable energetic break value

The break condition for the self-consistency step
[EDIFF](../incar-tags/EDIFF.md) strongly influences the magnetic
susceptibility. A setting of [EDIFF](../incar-tags/EDIFF.md) = `1E-8` eV is
generally recommended. Convergence is taken to be within 0.01
(dimensionless units).

**Step 3:** Converge the plane-wave basis

A larger than standard plane-wave energy cutoff is required to fully
converge the magnetic susceptibility. Perform multiple calculations
while increasing the basis set size, as defined in
[ENCUT](../incar-tags/ENCUT.md), incrementally (e.g., by 100 eV intervals).
Convergence should be aimed to be within 0.01 (dimensionless units). The
magnetic susceptibility is less dependent on the energy cutoff than the
chemical shielding is.

**Step 4:** Converge the **k** point mesh

Similar to the basis, the **k** point mesh can strongly influence the
magnetic susceptibility. The **k** point mesh should be increased
incrementally, i.e., 1x1x1, 2x2x2, 3x3x3, until convergence within 0.01
(dimensionless units) is achieved. It is slightly more dependent on
**k** point mesh than the chemical shieldings are.

**Step 5:** Compare to experiment

The purpose of these calculations is to compare to the experiment. The
computed magnetic susceptibilities can be directly compared to the
measured magnetic susceptibility, in contrast to the chemical shielding
^([\[3\]](#cite_note-mauri:louie:1996-3)).

## Recommendations and advice
Calculating the magnetic susceptibilities requires tightly converged
settings. As described in the step-wise introduction above, converging
with respect to [EDIFF](../incar-tags/EDIFF.md),
[ENCUT](../incar-tags/ENCUT.md), and the **k** point mesh is very
important. There are a few additional settings that should be
considered. Since the same tag is used, much of the advice for chemical
shieldings is applicable for the magnetic susceptibility.

### PAW pseudopotentials
The standard [PAW
pseudopotentials](../categories/Category-Pseudopotentials.md)
[POTCAR](../input-files/POTCAR.md) used are sufficient for calculating the
magnetic susceptibility. Small differences on the order of 0.1
(dimensionless units) are seen when using slightly different types of
[POTCAR](../input-files/POTCAR.md), e.g., GW (*\*\_GW*).

### Additional tags
To ensure tight precision, the precision should be set to
[`PREC`](../incar-tags/PREC.md)` = Accurate`, rather than `Normal`. There is
one additional tag, [ICHIBARE](../incar-tags/ICHIBARE.md) that can be
used, though the default is usually sufficient and increases the
computational load significantly.

# Example scripts for convergence tests
Several tests are necessary to obtain various NMR parameters. Make sure
to change the example [INCAR](../input-files/INCAR.md) files to include the
tags for your desired calculation. We provide some example scripts
below:

## Energetic break criterion tests
For converging the energetic break criterion for a single ionic step
([EDIFF](../incar-tags/EDIFF.md)), start with the 1E-4 and then increase by
orders of magnitude:

Energetic break criterion: **INCAR.nmr**

    PREC = Accurate        
    ENCUT = 400.0          
    EDIFF = 1E-4          
    ISMEAR = 0; SIGMA = 0.1 
    LREAL = A              
    LCHIMAG = .TRUE.       
    DQ = 0.001             
    ICHIBARE = 1           
    LNMR_SYM_RED = .TRUE.  
    NLSPLINE = .TRUE.    

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

    PREC = Accurate        
    ENCUT = 400.0          
    EDIFF = 1E-8          
    ISMEAR = 0; SIGMA = 0.1 
    LREAL = A              
    LCHIMAG = .TRUE.       
    DQ = 0.001             
    ICHIBARE = 1           
    LNMR_SYM_RED = .TRUE.  
    NLSPLINE = .TRUE.    

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
[LCHIMAG](../incar-tags/LCHIMAG.md),
[LVGVCALC](../incar-tags/LVGVCALC.md),
[LVGVAPPL](../incar-tags/LVGVAPPL.md)

## References
1.  [↑](#cite_ref-pickard:prb:2001_1-0) [C. J. Pickard and F. Mauri,
    *All-electron magnetic response with pseudopotentials: NMR chemical
    shifts*, Phys. Rev. B **63**, 245101
    (2001).](https://doi.org/10.1103/PhysRevB.63.245101)
2.  [↑](#cite_ref-yates:prb:2007_2-0) [J. R. Yates, C. J. Pickard,
    and F. Mauri, *Calculation of NMR chemical shifts for extended
    systems using ultrasoft pseudopotentials*, Phys. Rev. B **76**,
    024401 (2007).](https://doi.org/10.1103/PhysRevB.76.024401)
3.  [↑](#cite_ref-mauri:louie:1996_3-0) [F. Mauri and S. G. Louie,
    *Magnetic Susceptibility of Insulators from First Principles*, Phys.
    Rev. Lett. **76**, 4246
    (1996).](https://doi.org/10.1103/PhysRevLett.76.4246)

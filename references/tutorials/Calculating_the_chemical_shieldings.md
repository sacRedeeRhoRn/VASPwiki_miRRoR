<!-- Source: https://vasp.at/wiki/index.php/Calculating_the_chemical_shieldings | revid: 34808 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Calculating the chemical shieldings


The chemical shielding tensor *σ* is the relation between the induced
and external magnetic fields and describes how much the electrons shield
the nuclei from an external field. The absolute chemical shielding is
calculated by linear response using [LCHIMAG](../incar-tags/LCHIMAG.md)
<sup>[\[1\]](#cite_note-pickard:prb:2001-1)[\[2\]](#cite_note-yates:prb:2007-2)</sup>.
The chemical shielding is directly related to the chemical shift *δ*
recorded in nuclear magnetic resonance (NMR), cf. [NMR category
page](../categories/Category-NMR.md) and
[LCHIMAG](../incar-tags/LCHIMAG.md) page for details, and, indirectly, to
the resonance frequency. The theory is covered in the [NMR category
page](../categories/Category-NMR.md) and
[LCHIMAG](../incar-tags/LCHIMAG.md) page.

|  |
|----|
| **Warning:** The chemical shifts are calculated from the orbital magnetic response under the assumption that the system is an insulator. Smearing schemes intended for metals can generate nonsense. |


## Contents


- [1 Step-by-step
  instructions](#Step-by-step_instructions)
  - [1.1 Step 1
    (optional): Calculate the chemical shielding using a previously
    converged
    calculation](#Step_1_(optional):_Calculate_the_chemical_shielding_using_a_previously_converged_calculation)
  - [1.2 Step 2
    (optional): Determine a suitable energetic break
    value](#Step_2_(optional):_Determine_a_suitable_energetic_break_value)
  - [1.3 Step 3:
    Converge the plane-wave
    basis](#Step_3:_Converge_the_plane-wave_basis)
  - [1.4 Step 4:
    Converge the **k** point
    mesh](#Step_4:_Converge_the_k_point_mesh)
  - [1.5 Step 5:
    Compare to experiment](#Step_5:_Compare_to_experiment)
- [2
  Recommendations and
  advice](#Recommendations_and_advice)
  - [2.1 PAW
    pseudopotentials](#PAW_pseudopotentials)
  - [2.2
    Insufficient
    memory](#Insufficient_memory)
  - [2.3 Additional
    tags](#Additional_tags)
- [3 Example
  scripts for convergence
  tests](#Example_scripts_for_convergence_tests)
  - [3.1 Energetic
    break criterion tests](#Energetic_break_criterion_tests)
  - [3.2
    **k**-points tests](#k-points_tests)
  - [3.3 Energy
    cutoff tests](#Energy_cutoff_tests)
  - [3.4
    References](#References)


## Step-by-step instructions\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

The chemical shielding is calculated post-self-consistent field
(post-SCF) using [LCHIMAG](../incar-tags/LCHIMAG.md). A well-converged
SCF calculation is therefore crucial. The chemical shielding is very
sensitive to several input parameters that must all be independently
tested.

### Step 1 (optional): Calculate the chemical shielding using a previously converged calculation\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step 1 (optional): Calculate the chemical shielding using a previously converged calculation">edit</a> \| (./index.php.md): Calculate the chemical shielding using a previously converged calculation")\]

Since the chemical shielding is calculated post-SCF, you can use a
previously converged [WAVECAR](../input-files/WAVECAR.md) with
[ISTART](../incar-tags/ISTART.md) = 1 and [NELM](../incar-tags/NELM.md) = 1.
The corresponding density, [CHGCAR](../input-files/CHGCAR.md) is calculated
from the [WAVECAR](../input-files/WAVECAR.md) file before the first
elementary step so it need not be included.

### Step 2 (optional): Determine a suitable energetic break value\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 2 (optional): Determine a suitable energetic break value">edit</a> \| (./index.php.md): Determine a suitable energetic break value")\]

The break condition for the self-consistency step
[EDIFF](../incar-tags/EDIFF.md) strongly influences the chemical shielding.
A setting of [EDIFF](../incar-tags/EDIFF.md) = 1E-8 eV is generally
recommended. Convergence is taken to be within 0.1 ppm.

### Step 3: Converge the plane-wave basis\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Converge the plane-wave basis">edit</a> \| (./index.php.md)\]

A large plane-wave energy cutoff is required to fully converge the
chemical shieldings. Perform multiple calculations while increasing the
basis set size, as defined in [ENCUT](../incar-tags/ENCUT.md),
incrementally (e.g., by 100 eV intervals). Convergence should be aimed
to be within 0.1 ppm, although this will not be feasible for heavier
elements.

### Step 4: Converge the **k** point mesh\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Step 4: Converge the k point mesh">edit</a> \| (./index.php.md)\]

Similar to the basis, the **k** point mesh can strongly influence the
chemical shielding. The **k** point mesh should be increased
incrementally, i.e., 1x1x1, 2x2x2, 3x3x3, until convergence within 0.1
ppm is achieved. It is only necessary to converge the **k** point mesh
for crystals, gas-phase molecules should use the Γ-point only.

### Step 5: Compare to experiment\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 5: Compare to experiment">edit</a> \| (./index.php.md)\]

The purpose of these calculations is to compare to experiment. However,
the calculated absolute chemical shieldings are not directly comparable
to the measured chemical shift due to the lack of a reference. To avoid
bias from any single calculation, a series of calculated and their
corresponding experimental values are used. The experimental chemical
shifts are plotted against the calculated chemical shieldings as is
found in Fig. 3 of Ref.
<sup>[\[3\]](#cite_note-dewijs:laskowski:jcp:2017-3)</sup>.

## Recommendations and advice\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Recommendations and advice">edit</a> \| (./index.php.md)\]

Calculating the chemical shielding requires tightly converged settings.
As described in the step-wise introduction above, converging with
respect to [EDIFF](../incar-tags/EDIFF.md), [ENCUT](../incar-tags/ENCUT.md),
and the **k** point mesh is very important. There are a few additional
settings that should be considered.

### PAW pseudopotentials\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: PAW pseudopotentials">edit</a> \| (./index.php.md)\]

The standard PAW pseudopotentials [POTCAR](../input-files/POTCAR.md) used
are sufficient for calculating the chemical shielding. The GIPAW is
applied using the projector functions and partial waves that are stored
in the regular [POTCAR](../input-files/POTCAR.md) files. The completeness
of these projector functions and partial waves determines the quality of
the results. Using slightly different types of
[POTCAR](../input-files/POTCAR.md), e.g., GW (*\*\_GW*) or with additional
valence (*\*\_sv*, *\*\_pv*), can change the calculated shielding by a
few ppm for the first and second row *sp*-bonded elements (except for
H).

The PAW reconstruction with all-electron partial waves is crucial for
calculating the field on the nucleus. It is therefore important to use a
consistent exchange-correlation functional and so
[LEXCH](../incar-tags/LEXCH.md) in the [POTCAR](../input-files/POTCAR.md)
should not be overwritten with an explicit [GGA](../incar-tags/GGA.md) tag in
the [INCAR](../input-files/INCAR.md) if possible.

### Insufficient memory\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Insufficient memory">edit</a> \| (./index.php.md)\]

For calculating the chemical shieldings, speed had been favored over
saving memory, resulting in insufficient memory occasionally. Since the
linear response calculation is parallel over **k** points, this can be
used to economize on memory by performing a regular SCF calculation at
high accuracy on the full **k** point mesh and saving the
[CHGCAR](../input-files/CHGCAR.md) file. Using
[`ICHARG`](../incar-tags/ICHARG.md)` = 11`
start a chemical shielding calculation for each individual **k** point
in the first Brillouin zone (IBZ) separately, starting from
[CHGCAR](../input-files/CHGCAR.md). The shieldings can then be calculated
as a **k** point weighted average of the symmetrized shieldings of the
individual **k** points.

### Additional tags\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Additional tags">edit</a> \| (./index.php.md)\]

To ensure tight precision, the precision should be set to
[`PREC`](../incar-tags/PREC.md)` = Accurate`,
rather than `Normal`.

Several additional [INCAR](../input-files/INCAR.md) tags should be
considered. Specifically, [LASPH](../incar-tags/LASPH.md) should be set to
`.TRUE.`, turning on the non-spherical contributions to the gradient of
the density inside the PAW spheres. Occasionally, e.g. for systems
containing H or first-row elements, and short bonds, the two-center
contributions to the augmentation currents in the PAW spheres are
important. In this case, [LLRAUG](../incar-tags/LLRAUG.md) = .TRUE. should
be used
<sup>[\[4\]](#cite_note-dewijs:jcp:2013-4)[\[5\]](#cite_note-dewijs:jcp:2021-5)</sup>.

Calculating the chemical shift can also be sped up by utilizing
parallelisation. If you are using multiple k-points, then you can treat
these in parallel using [KPAR](../incar-tags/KPAR.md), reducing the overall
calculation time.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span
style="color: var(--vpurple);">Important:</span></strong> The
non-relativistic treatment of the orbital magnetism is suitable for
light nuclei.
<p>The <a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a> are scalar-relativistic.
To account for regularization within scalar-relativistic ZORA use <a
href="/wiki/LZORA" title="LZORA">LZORA</a> and to account for spin-orbit
coupling use <a href="/wiki/LSOSHIFT"
title="LSOSHIFT">LSOSHIFT</a>.</p></td>
</tr>
</tbody>
</table>

# Example scripts for convergence tests\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Example scripts for convergence tests">edit</a> \| (./index.php.md)\]

Several tests are necessary to obtain various NMR parameters. Make sure
to change the example [INCAR](../input-files/INCAR.md) files to include the
tags for your desired calculation. We provide some example scripts
below:

## Energetic break criterion tests\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Energetic break criterion tests">edit</a> \| (./index.php.md)\]

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

## **k**-points tests\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: k-points tests">edit</a> | (./index.php.md)\]

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

## Energy cutoff tests\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Energy cutoff tests">edit</a> \| (./index.php.md)\]

For converging the energy cutoff, start with the value of ENMAX given in
the [POTCAR](../input-files/POTCAR.md) file and then increase incrementally
in steps of 100 eV:

Initial
[INCAR](../input-files/INCAR.md):
**INCAR.nmr**

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

## References\[<a
href="/wiki/index.php?title=Calculating_the_chemical_shieldings&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-pickard:prb:2001_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.63.245101"
    class="external text" rel="nofollow">C. J. Pickard and F. Mauri,
    <em>All-electron magnetic response with pseudopotentials: NMR chemical
    shifts</em>, Phys. Rev. B <strong>63</strong>, 245101 (2001).</a>
2.  [↑](#cite_ref-yates:prb:2007_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.76.024401"
    class="external text" rel="nofollow">J. R. Yates, C. J. Pickard, and F.
    Mauri, <em>Calculation of NMR chemical shifts for extended systems using
    ultrasoft pseudopotentials</em>, Phys. Rev. B <strong>76</strong>,
    024401 (2007).</a>
3.  [↑](#cite_ref-dewijs:laskowski:jcp:2017_3-0)
    <a href="https://doi.org/10.1063/1.4975122" class="external text"
    rel="nofollow">G. A. de Wijs, R. Laskowski, P. Blaha, R. W. A. Havenith,
    G. Kresse, and M. Marsman, <em>NMR shieldings from density functional
    perturbation theory: GIPAW versus all-electron calculations</em>, J.
    Chem. Phys. <strong>146</strong>, 064115 (2017).</a>
4.  [↑](#cite_ref-dewijs:jcp:2013_4-0)
    <a href="https://doi.org/10.1063/1.4810799" class="external text"
    rel="nofollow">F. Vasconcelos, G.A. de Wijs, R. W. A. Havenith, M.
    Marsman, and G. Kresse, <em>Finite-field implementation of NMR chemical
    shieldings for molecules: Direct and converse gauge-including
    projector-augmented-wave methods</em>, J. Chem. Phys.
    <strong>139</strong>, 014109 (2013).</a>
5.  [↑](#cite_ref-dewijs:jcp:2021_5-0)
    <a href="https://doi.org/10.1063/5.0069637" class="external text"
    rel="nofollow">G.A. de Wijs, G. Kresse, R. W. A. Havenith, and M.
    Marsman, <em>Comparing GIPAW with numerically exact chemical shieldings:
    The role of two-center contributions to the induced current</em>, J.
    Chem. Phys. <strong>155</strong>, 234101 (2021).</a>



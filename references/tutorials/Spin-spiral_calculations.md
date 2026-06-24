<!-- Source: https://vasp.at/wiki/index.php/Spin-spiral_calculations | revid: 37307 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Spin-spiral calculations
**Spin-spiral calculations** model continuously rotating magnetic
structures without the need for large supercells. This page provides
step-by-step instructions for setting up, running, and analyzing
spin-spiral calculations. For the underlying formalism (the generalized
Bloch condition, the modified Hamiltonian, and the basis-set
requirements) see [Spin spirals](../theory/Spin_spirals.md).

## Contents

- [1 Prerequisites](#Prerequisites)
- [2 Step-by-step instructions](#Step-by-step_instructions)
  - [2.1 Step 1: Start from a converged magnetic
    state](#Step_1:_Start_from_a_converged_magnetic_state)
  - [2.2 Step 2: Set up the spin-spiral
    INCAR](#Step_2:_Set_up_the_spin-spiral_INCAR)
  - [2.3 Step 3: Constrain to a planar spiral
    (optional)](#Step_3:_Constrain_to_a_planar_spiral_(optional))
  - [2.4 Step 4: Extract local magnetic moments
    (optional)](#Step_4:_Extract_local_magnetic_moments_(optional))
  - [2.5 Step 5: Run the calculation](#Step_5:_Run_the_calculation)
- [3 Examples](#Examples)
  - [3.1 Example 1: Initializing the magnetic
    configuration](#Example_1:_Initializing_the_magnetic_configuration)
  - [3.2 Example 2: Spin-spiral energy of a NiI₂
    monolayer](#Example_2:_Spin-spiral_energy_of_a_NiI2_monolayer)
- [4 Magnon dispersion and exchange
  interactions](#Magnon_dispersion_and_exchange_interactions)
- [5 Related tags and articles](#Related_tags_and_articles)
- [6 References](#References)

## Prerequisites
Spin spirals are a noncollinear-magnetism feature. You need the
`vasp_ncl` executable that supports noncollinear magnetism
([`LNONCOLLINEAR`](../incar-tags/LNONCOLLINEAR.md)` = True`), and
it is helpful to be familiar with collinear magnetic calculations, the
[MAGMOM](../incar-tags/MAGMOM.md) tag, and [Setting up an electronic
minimization](Setting_up_an_electronic_minimization.md)
before starting.

## Step-by-step instructions
### Step 1: Start from a converged magnetic state
Begin with a converged collinear or noncollinear ground-state
calculation of the primitive cell, following [Setting up an electronic
minimization](Setting_up_an_electronic_minimization.md),
and keep the resulting [CHGCAR](../input-files/CHGCAR.md) as a starting
point for the spin-spiral run. The total energy and on-site magnetic
moments ([LORBIT](../incar-tags/LORBIT.md)) should be converged with
respect to **k**-mesh density and energy cutoff
([ENCUT](../incar-tags/ENCUT.md)).

[TABLE]

|  |
|----|
| **Tip:** Magnetism usually arises in d-electron and f-electron bands. To write the augmentation charges of those bands, set [`LMAXMIX`](../incar-tags/LMAXMIX.md)` = 4` (d electrons) or `6`. |

Choose the remaining electronic-minimization tags
([ALGO](../incar-tags/ALGO.md), [EDIFF](../incar-tags/EDIFF.md),
[NELM](../incar-tags/NELM.md), [ISMEAR](../incar-tags/ISMEAR.md)) as described
in [Setting up an electronic
minimization](Setting_up_an_electronic_minimization.md);
frustrated or incommensurate magnets often need a larger
[NELM](../incar-tags/NELM.md) and [`ALGO`](../incar-tags/ALGO.md)` = Conjugate`
is often most reliable.

Initialize the magnetic order with the [MAGMOM](../incar-tags/MAGMOM.md)
tag. In the noncollinear case, this takes three components per atom. If
no initial moments are given, the initial order is ferromagnetic, which
may trap the system in a local minimum even when the ground state is not
ferromagnetic.

### Step 2: Set up the spin-spiral INCAR
Add the following tags to the [INCAR](../input-files/INCAR.md):

    LNONCOLLINEAR = .TRUE.
    LSPIRAL       = .TRUE.
    QSPIRAL       = q1 q2 q3
    ISYM          = -1
    ENINI         = 300
    ENCUT         = 400

Here, `q1 q2 q3` are the components of the spin-spiral propagation
vector in direct (fractional) coordinates of the reciprocal lattice. In
a spin-spiral calculation, the magnetic configuration is set both by the
initial moments *within* the cell using the
[MAGMOM](../incar-tags/MAGMOM.md) tag, in the noncollinear
(three-component-per-atom) format, and by how the magnetization rotates
*between* cells (the [QSPIRAL](../incar-tags/QSPIRAL.md) vector). Worked
examples are given in the [Examples](#Examples) section below. Choose
the remaining electronic-minimization tags as in step 1.

|  |
|----|
| **Mind:** Symmetry must be switched off completely ([`ISYM`](../incar-tags/ISYM.md)` = -1`). VASP cannot account for the symmetry reduction introduced by a spin spiral, so leaving symmetry on produces incorrect results. |

|  |
|----|
| **Tip:** Set [ENCUT](../incar-tags/ENCUT.md) (or equivalently [ENMAX](../redirects/ENMAX.md)) at least 100 eV above [ENINI](../incar-tags/ENINI.md). VASP prints a runtime warning if the value is too small for the chosen **q** vector, *e.g.*: |

     ----------------------------------------------------------------------------- 
    |                                                                             |
    |           W    W    AA    RRRRR   N    N  II  N    N   GGGG   !!!           |
    |           W    W   A  A   R    R  NN   N  II  NN   N  G    G  !!!           |
    |           W    W  A    A  R    R  N N  N  II  N N  N  G       !!!           |
    |           W WW W  AAAAAA  RRRRR   N  N N  II  N  N N  G  GGG   !            |
    |           WW  WW  A    A  R   R   N   NN  II  N   NN  G    G                |
    |           W    W  A    A  R    R  N    N  II  N    N   GGGG   !!!           |
    |                                                                             |
    |      To represent the spin spiral you requested, with a kinetic             |
    |      energy cutoff of ENINI=  300.00 eV, choose ENMAX >  331.21 eV          |
    |      Currently ENMAX=  400.00 eV                                            |
    |                                                                             |
     -----------------------------------------------------------------------------

### Step 3: Constrain to a planar spiral (optional)
To prevent the magnetization density from developing a *z*-component,
set:

    LZEROZ = .TRUE.

This forces $m_z({\bf r})=0$ at each
step of the electronic minimization.

### Step 4: Extract local magnetic moments (optional)
Analyzing site-resolved local moments is less straightforward than
usual, because the spin-spiral period is generally incommensurate with
the unit cell, so the magnetization density is not cell-periodic:

[![](https://vasp.at/wiki/images/thumb/2/27/Ss3.png/300px-Ss3.png)](https://vasp.at/wiki/File:Ss3.png)

The standard analysis via [LORBIT](../incar-tags/LORBIT.md) (output in the
[PROCAR](../output-files/PROCAR.md) file and at the end of the
[OUTCAR](../output-files/OUTCAR.md) file) does not account for this. As a
workaround, use the constrained-moment infrastructure with a zero
penalty potential:

    I_CONSTRAINED_M = 1
    LAMBDA          = 0.0
    RWIGS           = <one radius per species>

This switches on the [constrained-magnetic-moment
approach](../incar-tags/I_CONSTRAINED_M.md) but sets the penalty
potential to zero ([LAMBDA](../incar-tags/LAMBDA.md) = 0.0). The
magnetization density is then integrated inside site-centered spheres of
radius [RWIGS](../incar-tags/RWIGS.md), and the resulting local moments are
written under `M_int` in the [OSZICAR](../output-files/OSZICAR.md) file,
*e.g.*:

     E_p =  0.00000E+00  lambda =  0.000E+00
    <lVp>=  0.00000E+00
     DBL =  0.00000E+00
     ion        MW_int                 M_int
      1  1.178  0.000  0.000    1.573  0.000  0.000
    RMM:   8    -0.819213822792E+01    0.53417E-07   -0.43965E-08  2542   0.310E-03

Here, the local moment on ion 1 (after iteration 8) is
$M=1.573\\\hat{x}\\\mu_{\rm B}$.

|  |
|----|
| **Mind:** Do not forget to set [RWIGS](../incar-tags/RWIGS.md) for every species; without it the integration spheres are undefined. |

### Step 5: Run the calculation
Run VASP as usual and monitor convergence in the
[OSZICAR](../output-files/OSZICAR.md) file. A spin-spiral calculation has
approximately the same cost as a standard noncollinear calculation of
the primitive cell.

## Examples
### Example 1: Initializing the magnetic configuration
The initial moments within the cell, together with the
[QSPIRAL](../incar-tags/QSPIRAL.md) vector, determine which magnetic
configuration the calculation starts from.

**Double-layer antiferromagnet.** Two magnetic atoms with initial
moments *M* along *y*, and ${\bf
q}=(0,0,\tfrac{1}{2})$:

    MAGMOM  = 0 M 0  0 M 0
    QSPIRAL = 0.0 0.0 0.5

[![](https://vasp.at/wiki/images/thumb/4/4e/Ss1.png/500px-Ss1.png)](https://vasp.at/wiki/File:Ss1.png)

**Flat spin spiral.** Two magnetic atoms with initial moments *M* along
*y* and *x*, respectively, and ${\bf
q}=(0,0,\tfrac{1}{2})$:

    MAGMOM  = 0 M 0  M 0 0
    QSPIRAL = 0.0 0.0 0.5

[![](https://vasp.at/wiki/images/thumb/8/85/Ss2.png/500px-Ss2.png)](https://vasp.at/wiki/File:Ss2.png)

|  |
|----|
| **Tip:** Both configurations obey the same generalized Bloch condition, ${\bf q}=(0,0,0.5)$, and during the electronic minimization, one may transform into the other if that lowers the total energy. The Bloch condition fixes the change in magnetization density from one cell to the next, but does not constrain the magnetic order *within* a cell. |

### Example 2: Spin-spiral energy of a NiI₂ monolayer
This example uses a spin-spiral calculation to obtain the total energy
of a flat spin spiral in a NiI₂ monolayer. The spin spiral is scanned
along the [QSPIRAL](../incar-tags/QSPIRAL.md) path Γ–M–K–Γ to find the
magnetic ground state. The triangular Ni sublattice is magnetically
frustrated, which stabilizes an incommensurate spiral.

[![](https://vasp.at/wiki/images/thumb/b/bc/NiI2_spinspiral_structure.png/600px-NiI2_spinspiral_structure.png)](https://vasp.at/wiki/File:NiI2_spinspiral_structure.png)

The flat in-plane spin spiral at the computed Γ–M minimum **Q** =
(0.214, 0, 0): the Ni moments rotate in the plane along **Q** with
period *λ* = 1/*Q* ≈ 4.7 *a*.

**Structure**: A 1T (CdI₂-type) NiI₂ monolayer, hexagonal *a* = 3.97 Å
with ≈8 Å of vacuum ([POSCAR](../input-files/POSCAR.md)):

    NiI2 1T monolayer
    1.0
       3.9697   0.0000    0.0000
      -1.9849   3.4379    0.0000
       0.0000   0.0000   11.0271
    Ni I
    1 2
    Direct
      0.0000 0.0000 0.5000
      0.3333 0.6667 0.6373
      0.6667 0.3333 0.3627

**INCAR**: One self-consistent calculation per **q**, changing only
[QSPIRAL](../incar-tags/QSPIRAL.md). The Ni moment is initialized in the
*xy*-plane and iodine is nonmagnetic:

    LNONCOLLINEAR = .TRUE.
    LSPIRAL       = .TRUE.
    QSPIRAL       = q1 q2 0.0
    ISYM          = -1
    ENINI         = 600
    ENCUT         = 700
    ISMEAR        = 0
    SIGMA         = 0.05
    MAGMOM        = 2 0 0  0 0 0  0 0 0

A Γ-centered 12×12×1 k-mesh and PBE Ni_pv and I PAW potentials were
used. The total energy *E*(**q**) is read from the
[OUTCAR](../output-files/OUTCAR.md).

**Result** — spin-spiral energy relative to the ferromagnetic state
(**q** = Γ):

|                    |                   |                           |
|--------------------|-------------------|---------------------------|
| **q** (fractional) | point / direction | *E*(**q**) − *E*(Γ) (meV) |
| (0, 0, 0)          | Γ (ferromagnetic) | 0.0                       |
| (0.143, 0, 0)      | Γ→M               | −12.4                     |
| (0.214, 0, 0)      | Γ→M (minimum)     | −14.5                     |
| (0.5, 0, 0)        | M                 | +40.2                     |
| (1/3, 1/3, 0)      | K                 | +8.2                      |
| (0.133, 0.133, 0)  | Γ→K (minimum)     | −15.9                     |

[![](https://vasp.at/wiki/images/thumb/3/3d/NiI2_spinspiral_energy.png/500px-NiI2_spinspiral_energy.png)](https://vasp.at/wiki/File:NiI2_spinspiral_energy.png)

Spin-spiral energy *E*(**q**) − *E*(Γ) of a monolayer NiI₂ along the
Γ–M–K–Γ path (PBE). The minima at incommensurate **q** indicate a
spin-spiral ground state; the Γ–M minimum near **q** ≈ (0.21, 0, 0)
matches the experimental helimagnetic vector.

The energy is lowest for an incommensurate spin spiral, not for the
ferromagnet (Γ) or the high-symmetry M and K points, reflecting the
frustration of the triangular Ni sublattice. Two shallow minima appear
along inequivalent in-plane directions — near **q** ≈ (0.21, 0, 0) along
Γ–M and **q** ≈ (0.13, 0.13, 0) along Γ–K — separated by a barrier of
only ≈1 meV, and the spiral is stabilized by ≈16 meV per formula unit
relative to the ferromagnet. The Γ–M minimum at **q** ≈ (0.21, 0, 0) is
in good agreement with the helimagnetic propagation vector **q** =
(0.220, 0, 0) measured for monolayer NiI₂ by spin-polarized scanning
tunneling microscopy.^([\[1\]](#cite_note-miao:pnas:25-1))

|  |
|----|
| **Tip:** The exact position of the incommensurate minimum depends on the [XC functional](../redirects/XC_functional.md), [PAW potentials](Choosing_pseudopotentials.md), and proper convergence of k-mesh density, and cutoff energy. |

## Magnon dispersion and exchange interactions
Scanning the spin-spiral energy *E*(**q**) as in [Example
2](#Example_2:_Spin-spiral_energy_of_a_NiI2_monolayer) is the basis of
the *frozen-magnon* method for extracting magnetic
interactions.^([\[2\]](#cite_note-marsman:prb:02-2)) Mapping the
computed energies onto a classical Heisenberg model,

$E({\bf q}) = E_0 - \sum_{\bf R} J({\bf R})\\
\cos({\bf q}\cdot{\bf R}),$

gives the interatomic exchange constants $J({\bf
R})$ as a Fourier transform of *E*(**q**). If the
ferromagnetic state is the ground state, the adiabatic magnon dispersion
follows from the same energies, $\hbar\omega({\bf
q}) \propto \[E({\bf q}) - E(0)\]/M$, with *M* the local
moment. If instead the minimum of *E*(**q**) lies at a finite **q** (as
for NiI₂) the system is predicted to order as an incommensurate spin
spiral with that propagation vector.

Practical notes:

- Use a fixed **k**-mesh and the same
  [ENINI](../incar-tags/ENINI.md)/[ENMAX](../redirects/ENMAX.md) for every
  **q**, since the relevant energy differences are only a few meV.
- Restart each point from the same converged charge density
  ([ICHARG](../incar-tags/ICHARG.md) = 1) for consistency across the scan.
- The mapping assumes rigid local moments; verify that the local moment
  is roughly **q**-independent (in Example 2 it varies by only a few
  percent).

|  |
|----|
| **Mind:** The [spin-spiral approach](../theory/Spin_spirals.md) is incompatible with [spin-orbit coupling](../redirects/Spin-orbit_coupling.md) ([`LSORBIT`](../incar-tags/LSORBIT.md)` = TRUE`), because spin-orbit coupling breaks the spin-rotational symmetry that the generalized Bloch condition relies on. |

## Related tags and articles
[Spin spirals](../theory/Spin_spirals.md) (Theory), [Setting up
an electronic
minimization](Setting_up_an_electronic_minimization.md)

[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md),
[MAGMOM](../incar-tags/MAGMOM.md), [ISYM](../incar-tags/ISYM.md),
[I_CONSTRAINED_M](../incar-tags/I_CONSTRAINED_M.md),
[LAMBDA](../incar-tags/LAMBDA.md), [RWIGS](../incar-tags/RWIGS.md),
[LORBIT](../incar-tags/LORBIT.md)

[LSPIRAL](../incar-tags/LSPIRAL.md), [QSPIRAL](../incar-tags/QSPIRAL.md),
[LZEROZ](../incar-tags/LZEROZ.md), [ENINI](../incar-tags/ENINI.md)

## References
1.  [↑](#cite_ref-miao:pnas:25_1-0) [M.-P. Miao, N. Liu, W.-H. Zhang,
    D.-B. Wang, W. Ji, and Y.-S. Fu, *Spin-resolved imaging of
    atomic-scale helimagnetism in mono- and bilayer NiI₂*, Proc. Natl.
    Acad. Sci. U.S.A. **122**, e2422868122
    (2025).](https://doi.org/10.1073/pnas.2422868122)
2.  [↑](#cite_ref-marsman:prb:02_2-0) [M. Marsman and J. Hafner, *Broken
    symmetries in the crystalline and magnetic structures of γ-iron*,
    Phys. Rev. B **66**, 224409
    (2002).](https://doi.org/10.1103/PhysRevB.66.224409)

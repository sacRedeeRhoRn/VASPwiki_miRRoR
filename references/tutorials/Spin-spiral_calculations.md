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


- [1
  Prerequisites](#prerequisites)
- [2 Step-by-step
  instructions](#step-by-step-instructions)
  - [2.1 Step 1:
    Start from a converged magnetic
    state](#step-1-start-from-a-converged-magnetic-state)
  - [2.2 Step 2:
    Set up the spin-spiral
    INCAR](#step-2-set-up-the-spin-spiral-incar)
  - [2.3 Step 3:
    Constrain to a planar spiral
    (optional)](#step-3-constrain-to-a-planar-spiral-optional))
  - [2.4 Step 4:
    Extract local magnetic moments
    (optional)](#step-4-extract-local-magnetic-moments-optional))
  - [2.5 Step 5:
    Run the calculation](#step-5-run-the-calculation)
- [3
  Examples](#examples)
  - [3.1 Example 1:
    Initializing the magnetic
    configuration](#example-1-initializing-the-magnetic-configuration)
  - [3.2 Example 2:
    Spin-spiral energy of a NiI<sub>2</sub>
    monolayer](#Example_2:_Spin-spiral_energy_of_a_NiI2_monolayer)
- [4 Magnon
  dispersion and exchange
  interactions](#magnon-dispersion-and-exchange-interactions)
- [5 Related tags
  and articles](#related-tags-and-articles)
- [6
  References](#references)


## Prerequisites\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Prerequisites">edit</a> \| (./index.php.md)\]

Spin spirals are a noncollinear-magnetism feature. You need the
`vasp_ncl` executable that supports noncollinear magnetism
([`LNONCOLLINEAR`](../incar-tags/LNONCOLLINEAR.md)` = True`), and
it is helpful to be familiar with collinear magnetic calculations, the
[MAGMOM](../incar-tags/MAGMOM.md) tag, and [Setting up an electronic
minimization](Setting_up_an_electronic_minimization.md)
before starting.

## Step-by-step instructions\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

### Step 1: Start from a converged magnetic state\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Start from a converged magnetic state">edit</a> \| (./index.php.md)\]

Begin with a converged collinear or noncollinear ground-state
calculation of the primitive cell, following [Setting up an electronic
minimization](Setting_up_an_electronic_minimization.md),
and keep the resulting [CHGCAR](../input-files/CHGCAR.md) as a starting
point for the spin-spiral run. The total energy and on-site magnetic
moments ([LORBIT](../incar-tags/LORBIT.md)) should be converged with
respect to **k**-mesh density and energy cutoff
([ENCUT](../incar-tags/ENCUT.md)).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
Symmetry:
<p>The introduction of a spin spiral will lower the symmetry of the
system. At present, VASP cannot correctly account for the presence of a
spin spiral in its symmetry analysis. Therefore, the use of symmetry
must be switched off in the subsequent steps by setting <a
href="/wiki/ISYM" title="ISYM"><code class="vasp-dark-link-panel"
style="padding: 2px">ISYM</code></a><code class="vasp-dark-link-panel"
style="padding: 2px"> = -1</code>. Generally, the number of irreducible
<strong>k</strong> points changes for different symmetry settings (<a
href="/wiki/ISYM" title="ISYM">ISYM</a>), and thus restarting from <a
href="/wiki/CHGCAR" title="CHGCAR">CHGCAR</a> should be preferred over
restarting from <a href="/wiki/WAVECAR" title="WAVECAR">WAVECAR</a>. You
may set <a href="/wiki/LWAVE" title="LWAVE"><code
class="vasp-dark-link-panel" style="padding: 2px">LWAVE</code></a><code
class="vasp-dark-link-panel" style="padding: 2px"> = False</code> to
avoid writing the <a href="/wiki/WAVECAR" title="WAVECAR">WAVECAR</a>.
It is not advantageous to switch off symmetry from the get-go, as using
symmetry reduces the computational effort and hence saves substantial
computational cost during the course of convergence studies.</p></td>
</tr>
</tbody>
</table>

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

### Step 2: Set up the spin-spiral INCAR\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Set up the spin-spiral INCAR">edit</a> \| (./index.php.md)\]

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
examples are given in the [Examples](#examples) section below. Choose
the remaining electronic-minimization tags as in step 1.

|  |
|----|
| **Mind:** Symmetry must be switched off completely ([`ISYM`](../incar-tags/ISYM.md)` = -1`). VASP cannot account for the symmetry reduction introduced by a spin spiral, so leaving symmetry on produces incorrect results. |

|  |
|----|
| **Tip:** Set [ENCUT](../incar-tags/ENCUT.md) (or equivalently <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) at least 100 eV above [ENINI](../incar-tags/ENINI.md). VASP prints a runtime warning if the value is too small for the chosen **q** vector, *e.g.*: |

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

### Step 3: Constrain to a planar spiral (optional)\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Constrain to a planar spiral (optional)">edit</a> \| (./index.php.md)")\]

To prevent the magnetization density from developing a *z*-component,
set:

    LZEROZ = .TRUE.

This forces $m_z({\bf r})=0$ at each step of the electronic minimization.

### Step 4: Extract local magnetic moments (optional)\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 4: Extract local magnetic moments (optional)">edit</a> \| (./index.php.md)")\]

Analyzing site-resolved local moments is less straightforward than
usual, because the spin-spiral period is generally incommensurate with
the unit cell, so the magnetization density is not cell-periodic:

<a href="/wiki/File:Ss3.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/2/27/Ss3.png/300px-Ss3.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/2/27/Ss3.png/450px-Ss3.png 1.5x, /wiki/images/thumb/2/27/Ss3.png/600px-Ss3.png 2x"
width="300" height="295" /></a>

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

### Step 5: Run the calculation\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Step 5: Run the calculation">edit</a> \| (./index.php.md)\]

Run VASP as usual and monitor convergence in the
[OSZICAR](../output-files/OSZICAR.md) file. A spin-spiral calculation has
approximately the same cost as a standard noncollinear calculation of
the primitive cell.

## Examples\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Examples">edit</a> \| (./index.php.md)\]

### Example 1: Initializing the magnetic configuration\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Example 1: Initializing the magnetic configuration">edit</a> \| (./index.php.md)\]

The initial moments within the cell, together with the
[QSPIRAL](../incar-tags/QSPIRAL.md) vector, determine which magnetic
configuration the calculation starts from.

**Double-layer antiferromagnet.** Two magnetic atoms with initial
moments *M* along *y*, and ${\bf q}=(0,0,\tfrac{1}{2})$:

    MAGMOM  = 0 M 0  0 M 0
    QSPIRAL = 0.0 0.0 0.5

<a href="/wiki/File:Ss1.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/4e/Ss1.png/500px-Ss1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/4/4e/Ss1.png 1.5x" width="500" height="207" /></a>

**Flat spin spiral.** Two magnetic atoms with initial moments *M* along
*y* and *x*, respectively, and ${\bf q}=(0,0,\tfrac{1}{2})$:

    MAGMOM  = 0 M 0  M 0 0
    QSPIRAL = 0.0 0.0 0.5

<a href="/wiki/File:Ss2.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/8/85/Ss2.png/500px-Ss2.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/8/85/Ss2.png 1.5x" width="500" height="208" /></a>

|  |
|----|
| **Tip:** Both configurations obey the same generalized Bloch condition, ${\bf q}=(0,0,0.5)$, and during the electronic minimization, one may transform into the other if that lowers the total energy. The Bloch condition fixes the change in magnetization density from one cell to the next, but does not constrain the magnetic order *within* a cell. |

### Example 2: Spin-spiral energy of a NiI<sub>2</sub> monolayer\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Example 2: Spin-spiral energy of a NiI2 monolayer">edit</a> \| (./index.php.md)\]

This example uses a spin-spiral calculation to obtain the total energy
of a flat spin spiral in a NiI<sub>2</sub> monolayer. The spin spiral is
scanned along the [QSPIRAL](../incar-tags/QSPIRAL.md) path Γ–M–K–Γ to
find the magnetic ground state. The triangular Ni sublattice is
magnetically frustrated, which stabilizes an incommensurate spiral.

<figure class="mw-halign-center" typeof="mw:File/Thumb">
<a href="/wiki/File:NiI2_spinspiral_structure.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/b/bc/NiI2_spinspiral_structure.png/600px-NiI2_spinspiral_structure.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/b/bc/NiI2_spinspiral_structure.png/900px-NiI2_spinspiral_structure.png 1.5x, /wiki/images/b/bc/NiI2_spinspiral_structure.png 2x"
width="600" height="288" /></a>
<figcaption>The flat in-plane spin spiral at the computed Γ–M minimum
<strong>Q</strong> = (0.214, 0, 0): the Ni moments rotate in the plane
along <strong>Q</strong> with period <em>λ</em> = 1/<em>Q</em> ≈ 4.7
<em>a</em>.</figcaption>
</figure>

**Structure**: A 1T (CdI<sub>2</sub>-type) NiI<sub>2</sub> monolayer,
hexagonal *a* = 3.97 Å with ≈8 Å of vacuum
([POSCAR](../input-files/POSCAR.md)):

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

<figure class="mw-halign-center" typeof="mw:File/Thumb">
<a href="/wiki/File:NiI2_spinspiral_energy.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/3/3d/NiI2_spinspiral_energy.png/500px-NiI2_spinspiral_energy.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/3/3d/NiI2_spinspiral_energy.png/750px-NiI2_spinspiral_energy.png 1.5x, /wiki/images/3/3d/NiI2_spinspiral_energy.png 2x"
width="500" height="333" /></a>
<figcaption>Spin-spiral energy <em>E</em>(<strong>q</strong>) −
<em>E</em>(Γ) of a monolayer NiI<sub>2</sub> along the Γ–M–K–Γ path
(PBE). The minima at incommensurate <strong>q</strong> indicate a
spin-spiral ground state; the Γ–M minimum near <strong>q</strong> ≈
(0.21, 0, 0) matches the experimental helimagnetic vector.</figcaption>
</figure>

The energy is lowest for an incommensurate spin spiral, not for the
ferromagnet (Γ) or the high-symmetry M and K points, reflecting the
frustration of the triangular Ni sublattice. Two shallow minima appear
along inequivalent in-plane directions — near **q** ≈ (0.21, 0, 0) along
Γ–M and **q** ≈ (0.13, 0.13, 0) along Γ–K — separated by a barrier of
only ≈1 meV, and the spiral is stabilized by ≈16 meV per formula unit
relative to the ferromagnet. The Γ–M minimum at **q** ≈ (0.21, 0, 0) is
in good agreement with the helimagnetic propagation vector **q** =
(0.220, 0, 0) measured for monolayer NiI<sub>2</sub> by spin-polarized
scanning tunneling
microscopy.<sup>[\[1\]](#cite_note-miao:pnas:25-1)</sup>

|  |
|----|
| **Tip:** The exact position of the incommensurate minimum depends on the <a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">XC functional</a>, [PAW potentials](Choosing_pseudopotentials.md), and proper convergence of k-mesh density, and cutoff energy. |

## Magnon dispersion and exchange interactions\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Magnon dispersion and exchange interactions">edit</a> \| (./index.php.md)\]

Scanning the spin-spiral energy *E*(**q**) as in [Example
2](#Example_2:_Spin-spiral_energy_of_a_NiI2_monolayer) is the basis of
the *frozen-magnon* method for extracting magnetic
interactions.<sup>[\[2\]](#cite_note-marsman:prb:02-2)</sup>
Mapping the computed energies onto a classical Heisenberg model,

$E({\bf q}) = E_0 - \sum_{\bf R} J({\bf R})\\ \cos({\bf q}\cdot{\bf R}),$

gives the interatomic exchange constants $J({\bf R})$
as a Fourier transform of *E*(**q**). If the ferromagnetic state is the
ground state, the adiabatic magnon dispersion follows from the same
energies, $\hbar\omega({\bf q}) \propto
\[E({\bf q}) - E(0)\]/M$, with *M* the local moment. If
instead the minimum of *E*(**q**) lies at a finite **q** (as for
NiI<sub>2</sub>) the system is predicted to order as an incommensurate
spin spiral with that propagation vector.

Practical notes:

- Use a fixed **k**-mesh and the same
  [ENINI](../incar-tags/ENINI.md)/<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>
  for every **q**, since the relevant energy differences are only a few
  meV.
- Restart each point from the same converged charge density
  ([ICHARG](../incar-tags/ICHARG.md) = 1) for consistency across the scan.
- The mapping assumes rigid local moments; verify that the local moment
  is roughly **q**-independent (in Example 2 it varies by only a few
  percent).

|  |
|----|
| **Mind:** The [spin-spiral approach](../theory/Spin_spirals.md) is incompatible with <a href="/wiki/Spin-orbit_coupling" class="mw-redirect"
title="Spin-orbit coupling">spin-orbit coupling</a> ([`LSORBIT`](../incar-tags/LSORBIT.md)` = TRUE`), because spin-orbit coupling breaks the spin-rotational symmetry that the generalized Bloch condition relies on. |

## Related tags and articles\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

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

## References\[<a
href="/wiki/index.php?title=Spin-spiral_calculations&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-miao:pnas:25_1-0)
    <a href="https://doi.org/10.1073/pnas.2422868122" class="external text"
    rel="nofollow">M.-P. Miao, N. Liu, W.-H. Zhang, D.-B. Wang, W. Ji, and
    Y.-S. Fu, <em>Spin-resolved imaging of atomic-scale helimagnetism in
    mono- and bilayer NiI<sub>2</sub></em>, Proc. Natl. Acad. Sci. U.S.A.
    <strong>122</strong>, e2422868122 (2025).</a>
2.  [↑](#cite_ref-marsman:prb:02_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.66.224409"
    class="external text" rel="nofollow">M. Marsman and J. Hafner,
    <em>Broken symmetries in the crystalline and magnetic structures of
    γ-iron</em>, Phys. Rev. B <strong>66</strong>, 224409 (2002).</a>



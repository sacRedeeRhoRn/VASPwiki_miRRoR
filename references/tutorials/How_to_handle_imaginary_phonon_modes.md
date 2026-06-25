<!-- Source: https://vasp.at/wiki/index.php/How_to_handle_imaginary_phonon_modes | revid: 36053 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# How to handle imaginary phonon modes


An imaginary (soft) phonon mode signals that the current structure is a
saddle point on the potential-energy surface: displacing atoms along the
mode eigenvector lowers the total energy. This page describes how to
detect imaginary modes, locate the instability in the Brillouin zone,
choose an appropriate working supercell, and follow the system to the
true energy minimum using the intrinsic-reaction-coordinate (IRC) method
or a frozen-phonon scan.

|  |
|----|
| **Mind:** An unrelaxed or poorly converged cell can produce spurious imaginary modes from [Pulay stress](Pulay_stress.md) or residual forces. If imaginary modes appear unexpectedly, first tighten the ionic relaxation ([ISIF](../incar-tags/ISIF.md)=3, tight [EDIFFG](../incar-tags/EDIFFG.md)) and recompute the phonons before drawing conclusions. |


## Contents


- [1 Step-by-step
  instructions](#Step-by-step_instructions)
  - [1.1 Step 1:
    Compute phonon
    frequencies](#Step_1:_Compute_phonon_frequencies)
  - [1.2 Step 2:
    Classify the modes](#Step_2:_Classify_the_modes)
  - [1.3 Step 3
    (optional): Map instabilities to the primitive cell via the phonon
    band
    structure](#Step_3_(optional):_Map_instabilities_to_the_primitive_cell_via_the_phonon_band_structure)
  - [1.4 Step 4:
    Determine the working
    supercell](#Step_4:_Determine_the_working_supercell)
  - [1.5 Step 5:
    Extract the eigenvector and set up the IRC starting
    structure](#Step_5:_Extract_the_eigenvector_and_set_up_the_IRC_starting_structure)
  - [1.6 Step 6:
    Follow the IRC to the energy
    minimum](#Step_6:_Follow_the_IRC_to_the_energy_minimum)
  - [1.7 Step 7:
    Relax from the determined
    minimum](#Step_7:_Relax_from_the_determined_minimum)
  - [1.8 Step 8:
    Verify the stability of the relaxed
    structure](#Step_8:_Verify_the_stability_of_the_relaxed_structure)
- [2
  Recommendations and
  advice](#Recommendations_and_advice)
- [3 Related tags
  and articles](#Related_tags_and_articles)
- [4
  References](#References)


## Step-by-step instructions\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

### Step 1: Compute phonon frequencies\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Compute phonon frequencies">edit</a> \| (./index.php.md)\]

Run a finite-differences phonon calculation on the structure of
interest. The same [INCAR](../input-files/INCAR.md) setup applies whether
you use the primitive cell (Γ-point modes only) or a supercell (to
access zone-boundary modes):

    IBRION = 6        ! exploit crystal symmetry (use IBRION=5 to disable symmetry)
    NFREE  = 2        ! central differences (±POTIM)
    POTIM  = 0.015    ! displacement amplitude (Å)
    PREC   = Accurate
    EDIFF  = 1E-8     ! tight convergence for reliable forces
    NSW    = 1
    LWAVE  = .FALSE.
    LCHARG = .FALSE.

Scale the **k**-point mesh inversely with supercell size. For example,
if the primitive cell uses an 8×8×8 mesh, a 2×2×2 supercell needs 4×4×4.

Imaginary modes appear in [OUTCAR](../output-files/OUTCAR.md) labelled
`f/i=`, while stable modes are labelled `f=`:

    f/i=   7.234 THz   45.423 2PiTHz  241.31 cm-1    29.92 meV

The full displacement eigenvector for each mode is printed in the block
"Eigenvectors and eigenvalues of the dynamical matrix" that follows the
frequency list.

Alternatively, read frequencies and eigenvectors directly with
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a>:


    import py4vasp, numpy as np
    calc = py4vasp.Calculation.from_path(".")
    mode_data = calc.phonon.mode.read()
    freqs = mode_data["frequencies"]   # complex eV; imag > 0 → imaginary mode
    evecs = mode_data["eigenvectors"]  # (n_modes, n_atoms, 3), mass-weighted


### Step 2: Classify the modes\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Classify the modes">edit</a> \| (./index.php.md)\]

Stable modes have a non-zero real part; imaginary (unstable) modes have
a non-zero imaginary part. Three acoustic modes always appear near zero
— this is a numerical artefact of the finite-differences procedure, not
a structural instability.

|                      |                                                 |
|----------------------|-------------------------------------------------|
| Imaginary part (meV) | Interpretation                                  |
| \< 0.5               | Acoustic mode — numerical noise, can be ignored |
| \> 5–20              | Genuine soft mode → structural instability      |

To identify the softest genuine optical mode with
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a>:


    # Threshold to exclude acoustic zeros
    optical_soft = np.where(freqs.imag * 1000 > 0.5)[0]   # imaginary part > 0.5 meV
    most_soft    = optical_soft[np.argmax(freqs[optical_soft].imag)]
    soft_vec     = evecs[most_soft]   # (n_atoms, 3) mass-weighted displacement pattern


If no mode exceeds the threshold, the structure is dynamically stable at
the computed **q**-points.

### Step 3 (optional): Map instabilities to the primitive cell via the phonon band structure\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 3 (optional): Map instabilities to the primitive cell via the phonon band structure">edit</a> \| (./index.php.md): Map instabilities to the primitive cell via the phonon band structure")\]

If Step 1 was run on a supercell, the interatomic force constants can be
Fourier-interpolated onto a dense **q**-path in the primitive-cell
Brillouin zone. This reveals at which **q**-vectors the instabilities
live and informs the choice of the smallest working cell in Step 4.
Imaginary branches are conventionally plotted as negative frequencies.

See
[Computing_the_phonon_dispersion_and_DOS](Computing_the_phonon_dispersion_and_DOS.md)
for the two-step procedure: a force-constants run followed by a
dispersion run with
[LPHON_DISPERSION](../incar-tags/LPHON_DISPERSION.md)=.TRUE. and
a [QPOINTS](../input-files/QPOINTS.md) file in line-mode format.

|  |
|----|
| **Tip:** For cubic perovskite ABO₃ structures the key high-symmetry points are: Γ (0,0,0) — ferroelectric uniform polar displacement; R (½,½,½) — antiferrodistortive octahedron tilts; X (½,0,0) — cell-doubling along one axis; M (½,½,0) — cell-doubling along two axes. The labels and fractional coordinates depend on the space group of the specific structure. |

|  |
|----|
| **Mind:** This calculation does not include the macroscopic electric field responsible for LO-TO splitting near Γ. Ferroelectric branches are therefore degenerate at Γ and absolute optical frequencies near Γ may differ from experiment. To capture LO-TO splitting, obtain Born effective charges and the high-frequency dielectric tensor via [LEPSILON](../incar-tags/LEPSILON.md)=.TRUE. or [LCALCEPS](../incar-tags/LCALCEPS.md)=.TRUE. and supply them via [PHON_BORN_CHARGES](../incar-tags/PHON_BORN_CHARGES.md) and [PHON_DIELECTRIC](../incar-tags/PHON_DIELECTRIC.md). This does not affect soft-mode identification. |

### Step 4: Determine the working supercell\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Step 4: Determine the working supercell">edit</a> \| (./index.php.md)\]

VASP always displaces atoms at Γ, so the instability must fold to Γ in
the chosen supercell.

- **Γ instability in the primitive cell** — use the primitive cell
  as-is; no supercell is needed.
- **Zone-boundary instability** — the **q**-vector of the soft mode
  determines the minimum supercell. For a mode at **q** = (*h*, *k*,
  *l*) in primitive-cell fractional coordinates, a supercell of
  dimensions (1/*h* × 1/*k* × 1/*l*) folds that **q** to Γ. For example,
  the X-point at (½, 0, 0) requires a 2×1×1 supercell, not a 2×2×2.

If the supercell from Step 1 is larger than the minimum required, build
the smaller cell and repeat Step 1. For zone-boundary modes the
displacement eigenvector must be applied with alternating signs across
the supercell images: atoms in the first primitive-cell image are
displaced along +**e**, atoms in the second image along −**e**, and so
on.

### Step 5: Extract the eigenvector and set up the IRC starting structure\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 5: Extract the eigenvector and set up the IRC starting structure">edit</a> \| (./index.php.md)\]

The intrinsic-reaction-coordinate (IRC) method requires the soft-mode
eigenvector as a *dimer-axis block* appended to the
[POSCAR](../input-files/POSCAR.md). Use the high-symmetry saddle-point
structure directly — no pre-displacement is needed because the forces
are zero there by symmetry.

Extract the eigenvector from
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> as shown in Step 2, or
read it from [OUTCAR](../output-files/OUTCAR.md): locate the block
"Eigenvectors and eigenvalues of the dynamical matrix", find the entry
labelled `f/i=` for the imaginary mode, and copy the three Cartesian
components listed for each atom.

Append the eigenvector to the [POSCAR](../input-files/POSCAR.md) after a
blank line following the last atomic position:

    BaTiO3 cubic (saddle point) + soft-mode dimer axis
    4.00
     1.0 0.0 0.0
     0.0 1.0 0.0
     0.0 0.0 1.0
    Ba Ti O
    1 1 3
    Direct
     0.000000  0.000000  0.000000
     0.500000  0.500000  0.500000
     0.500000  0.500000  0.000000
     0.500000  0.000000  0.500000
     0.000000  0.500000  0.500000

     -0.000156 -0.000282 -0.008871
     -0.012002 -0.021743 -0.684118
      0.005261  0.009530  0.592257
      0.005261  0.018823  0.299850
      0.010391  0.009530  0.299850

For zone-boundary modes, negate the dimer-block rows that correspond to
the second (and every alternating) primitive-cell image in the
supercell.

### Step 6: Follow the IRC to the energy minimum\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Step 6: Follow the IRC to the energy minimum">edit</a> \| (./index.php.md)\]

[IBRION](../incar-tags/IBRION.md)=40 activates the
intrinsic-reaction-coordinate method of Hratchian and Schlegel. Starting
from the saddle point, VASP propagates the structure along the
steepest-descent path in mass-weighted coordinates using a
damped-velocity-Verlet algorithm — no manual displacement or
energy-surface mapping is required.

    IBRION       = 40
    ISIF         = 2    ! cell fixed during the IRC path
    IRC_DIRECTION        = 1    ! +1 or −1 to choose which minimum to follow
    NSW          = 200  ! safety cap; IRC_STOP terminates the run earlier
    IRC_STOP             = 3    ! stop after energy rises for N consecutive steps
    IRC_VNORM0           = ...  ! velocity norm (Å/fs); controls step size
    IRC_DELTA0           = ...  ! path-accuracy tolerance (Å)
    IRC_MAXSTEP          = ...  ! upper bound on the adaptive time step (fs)
    IRC_MINSTEP          = ...  ! lower bound on the adaptive time step (fs)

The displacement per IRC step is approximately IRC_VNORM0 × IRC_MAXSTEP.
For a shallow double well (condensation energy ~10 meV) a step of ≤ 0.01
Å resolves the profile well. Increase IRC_VNORM0 if the run is very
slow; decrease it if the energy profile is jagged. Set IRC_DELTA0 to
roughly half the typical step displacement. Starting values of
IRC_VNORM0 = 0.02 Å/fs and IRC_DELTA0 = 0.01 Å are a reasonable first
attempt.

The IRC path and energies are recorded in
[OUTCAR](../output-files/OUTCAR.md) as:

    IRC (A):  0.05023  E(eV):  -135.7812

|  |
|----|
| **Mind:** If no `IRC (A):` lines appear in [OUTCAR](../output-files/OUTCAR.md), the dimer-axis block in the [POSCAR](../input-files/POSCAR.md) was not read correctly. Check that a blank line separates the last atomic coordinate from the first eigenvector row, and that there is exactly one row per atom. |

**Manual alternative (frozen-phonon scan):** If an explicit map of the
double-well potential is required, generate structures displaced along
the soft-mode eigenvector at several amplitudes λ. Start with roughly
±0.05 Å and widen the range until ΔE(λ) = *E*(λ) − *E*(0) clearly rises
on both sides. For each displaced structure run a static calculation
([IBRION](../incar-tags/IBRION.md)=−1, [NSW](../incar-tags/NSW.md)=0). Reuse
the [WAVECAR](../input-files/WAVECAR.md) from the λ = 0 reference as a
starting guess ([ISTART](../incar-tags/ISTART.md)=1) to accelerate SCF
convergence. Plot ΔE(λ) to read the condensation energy and identify
λ<sub>min</sub>, then proceed to Step 7 using the
[POSCAR](../input-files/POSCAR.md) at λ<sub>min</sub>.

### Step 7: Relax from the determined minimum\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Step 7: Relax from the determined minimum">edit</a> \| (./index.php.md)\]

Use the final ionic configuration from the IRC run
([CONTCAR](../output-files/CONTCAR.md)) or the displaced
[POSCAR](../input-files/POSCAR.md) at λ<sub>min</sub> from the
frozen-phonon scan as the starting geometry. The relaxation procedure is
identical in both cases:

    IBRION  = 2    ! conjugate-gradient relaxation
    ISIF    = 3    ! relax atoms, cell shape, and volume
    NSW     = ...  ! set large enough to reach convergence
    EDIFFG  = ...  ! force-convergence threshold (negative value, eV/Å)

Choose [NSW](../incar-tags/NSW.md) and [EDIFFG](../incar-tags/EDIFFG.md)
according to the required accuracy. For production calculations
[EDIFFG](../incar-tags/EDIFFG.md)=−0.01 is a common target; tighten to
[EDIFFG](../incar-tags/EDIFFG.md)=−0.001 if the relaxed structure will be
used as input for a follow-up phonon calculation (Step 8).

|  |
|----|
| **Mind:** The frozen-phonon scan constrains displacements to a single mode eigenvector. Even at the energy minimum along λ, forces transverse to the scan direction may be non-zero when the mode is degenerate. The full [ISIF](../incar-tags/ISIF.md)=3 relaxation in this step removes all residual forces and optimises the cell shape simultaneously. |

### Step 8: Verify the stability of the relaxed structure\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Step 8: Verify the stability of the relaxed structure">edit</a> \| (./index.php.md)\]

Re-run Step 1 on the fully relaxed geometry using the same
finite-differences setup. Confirm that no `f/i=` modes remain in
[OUTCAR](../output-files/OUTCAR.md). The symmetry lowering associated with
the structural transition typically lifts the degeneracy responsible for
the original instability, but competing instabilities at other
**q**-vectors may still be present and should be checked — in particular
if a supercell phonon dispersion (Step 3) showed multiple imaginary
branches.

## Recommendations and advice\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Recommendations and advice">edit</a> \| (./index.php.md)\]

- Always verify that the structure is fully relaxed before computing
  phonons. Residual forces from a geometry optimisation that converged
  on NSW rather than EDIFFG are a frequent source of spurious imaginary
  modes.
- Use [IBRION](../incar-tags/IBRION.md)=6 in preference to
  [IBRION](../incar-tags/IBRION.md)=5 for high-symmetry structures:
  symmetry reduction significantly decreases the number of displacements
  and the computational cost.
- For the phonon run, [EDIFF](../incar-tags/EDIFF.md)=1E-8 and
  [PREC](../incar-tags/PREC.md)=Accurate are the recommended minimum. A
  looser [EDIFF](../incar-tags/EDIFF.md) introduces noise into the force
  constants that can manifest as spurious low-frequency modes.
- If multiple imaginary modes appear at different **q**-points, start
  with the mode that has the largest imaginary frequency (the softest
  mode). It represents the dominant instability and the lowest-energy
  path away from the saddle point.
- After a successful IRC or relaxation run, always re-check the phonons
  on the new structure (Step 8). Symmetry lowering can stabilise the
  original instability but activate new ones.

## Related tags and articles\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

Tags: [IBRION](../incar-tags/IBRION.md), [NFREE](../incar-tags/NFREE.md),
[POTIM](../incar-tags/POTIM.md), [ISIF](../incar-tags/ISIF.md),
[EDIFFG](../incar-tags/EDIFFG.md), [NSW](../incar-tags/NSW.md),
[IRC_DIRECTION](../incar-tags/IRC_DIRECTION.md),
[IRC_STOP](../incar-tags/IRC_STOP.md),
[IRC_VNORM0](../incar-tags/IRC_VNORM0.md),
[IRC_DELTA0](../incar-tags/IRC_DELTA0.md),
[LPHON_DISPERSION](../incar-tags/LPHON_DISPERSION.md),
[LPHON_READ_FORCE_CONSTANTS](../incar-tags/LPHON_READ_FORCE_CONSTANTS.md),
[LEPSILON](../incar-tags/LEPSILON.md)

Files: [OUTCAR](../output-files/OUTCAR.md), [POSCAR](../input-files/POSCAR.md),
[CONTCAR](../output-files/CONTCAR.md), [QPOINTS](../input-files/QPOINTS.md)

[Phonons from finite
differences](Phonons_from_finite_differences.md),
[Computing the phonon dispersion and
DOS](Computing_the_phonon_dispersion_and_DOS.md),
[Intrinsic-reaction-coordinate
calculations](Intrinsic-reaction-coordinate_calculations.md),
[Structure
optimization](Structure_optimization.md)

## References\[<a
href="/wiki/index.php?title=How_to_handle_imaginary_phonon_modes&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]



<!-- Source: https://vasp.at/wiki/index.php/ALGO | revid: 37346 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ALGO


ALGO = \[string\]  
Default: **ALGO** = Normal 

Description: Selects the electronic-minimization algorithm and/or the
many-body method:

- [Electronic minimization](#Electronic-minimization_algorithms) (ground
  state)
  - *Self-consistency cycle*: `Normal` (default), `Fast`, `VeryFast`,
    `Exact`, `Subrot`
  - *Direct optimization*: `All` / `Conjugate`, `Damped`
  - *Postprocessing*: `Eigenval`, `None` / `Nothing`
- [Response functions, GW, BSE, and ACFDT/RPA](#GWALGOS)
  - `CHI`, `TDHF`, `BSE`, `Timeev`, `ACFDT` / `RPA`, `ACFDTR` / `RPAR`,
    and `CRPA`
  - *GW variants*: `EVGW0`, `EVGW`, `QPGW0`, `QPGW`, `GW0R`, `GWR`,
    `G0W0R`, `EVGW0R`

------------------------------------------------------------------------

|  |
|----|
| **Mind:** Available as of VASP 4.5 |

The ALGO tag has two kinds of
settings: For a ground-state calculation, it selects the
**electronic-minimization algorithm** (see [Electronic-minimization
algorithms](#Electronic-minimization_algorithms) section below); that
may be one of the self-consistency-cycle minimizers, the direct
optimizers, or the postprocessing modes. For
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>,
it instead selects the [algorithm for response functions, the GW
variant, BSE, time evolution, and ACFDT/RPA](#GWALGOS). The stopping
criterion is set using [EDIFF](EDIFF.md) and
[NELM](NELM.md). We recommend checking the [output during the
electronic minimization](#Output_during_the_electronic_minimization) as
described below to judge the convergence.

|  |
|----|
| **Tip:** To recompute the density of states (DOS), obtain the projected DOS or carry out any postprocessing from existing orbitals (e.g., a [WAVECAR](../input-files/WAVECAR.md) from a previous run) *without* re-optimizing them, set [`NELM`](NELM.md)` = 1`, [`LDIAG`](LDIAG.md)` = False`, and `ALGO`` = None`. Or to additionally recompute the one-electron energies set `ALGO`` = Eigenval`. |


## Contents


- [1
  Electronic-minimization
  algorithms](#Electronic-minimization_algorithms)
  - [1.1
    Recommendations](#Recommendations)
- [2 Output during
  the electronic
  minimization](#Output_during_the_electronic_minimization)
  - [2.1
    Line-search output (direct
    optimizers)](#Line-search_output_(direct_optimizers))
- [3 ALGO for
  response functions, GW, and
  ACFDT/RPA](#ALGO_for_response_functions,_GW,_and_ACFDT/RPA)
- [4 Related tags
  and articles](#Related_tags_and_articles)


## Electronic-minimization algorithms\[<a href="/wiki/index.php?title=ALGO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Electronic-minimization algorithms">edit</a> \| (./index.php.md)\]

For a [self-consistent ground-state
calculation](../tutorials/Setting_up_an_electronic_minimization.md),
ALGO selects how the orbitals
are optimized at each electronic step. Each value corresponds to a
setting of the lower-level tag [IALGO](IALGO.md). The
algorithms fall into two groups (see the *Class* column): the
[self-consistency-cycle](../theory/Self-consistency_cycle.md)
methods iterate the charge density with a [charge-density
mixer](../categories/Category-Density_mixing.md), whereas
the
[direct-optimization](../theory/Direct_optimization_of_the_orbitals.md)
methods minimize the energy functional directly, updating the density
from the orbitals without a charge mixer.

|  |  |  |  |  |
|----|----|----|----|----|
| ALGO | Algorithm | [IALGO](IALGO.md) | Class | Notes |
| `Normal` *(default)* | [blocked Davidson](../theory/Blocked-Davidson_algorithm.md) | 38 | self-consistency cycle | Robust default, recommended for most calculations. |
| `Fast` | [blocked Davidson](../theory/Blocked-Davidson_algorithm.md) + [RMM-DIIS](../theory/RMM-DIIS.md) | 68 | self-consistency cycle | Davidson for the initial phase, then [RMM-DIIS](../theory/RMM-DIIS.md); one Davidson sweep per ionic step (except the first). This setting is faster and cheaper per electronic step, but less robust and less reliable in the sense that it may diverge or cannot find the true minimum. Use to obtain a first estimate, but mind that orbitals (and hence forces, stress, etc.) may be less accurate compared to `Normal` or `All`. Updated in vasp.6.0.0; select `Old Fast` for the vasp.5 version. |
| `VeryFast` | [RMM-DIIS](../theory/RMM-DIIS.md) | 48 | self-consistency cycle | Fewest Hamiltonian evaluations but least robust. Not supported for [hybrid functionals](../methods/Category-Hybrid_functionals.md). Updated in vasp.6; select `Old VeryFast` for the vasp.5 version. Combine with [`LDIAG`](LDIAG.md)` = .FALSE.` to conserve the initial orbital order. |
| `Conjugate` / `All` | [blocked Davidson](../theory/Blocked-Davidson_algorithm.md) + all-band conjugate gradient | 58 | direct optimization | Simultaneous update of all orbitals. The two values are synonymous. Recommended together with the improved line-search algorithm ([`ISEARCH`](ISEARCH.md)` = 1`). Appropriate choice for magnetic systems and systems where `ALGO`` = Normal` failed. |
| `Damped` | [blocked Davidson](../theory/Blocked-Davidson_algorithm.md) + damped molecular dynamics | 53 | direct optimization | Damped velocity-friction dynamics for the orbitals. Robustness and time-to-solution strongly depend on setting [TIME](TIME.md) appropriately. |
| `Exact` | exact diagonalization | 90 | self-consistency cycle | Full diagonalization; expensive and memory-heavy. Use when many empty states are required (restarting from preconverged orbitals) or for testing. |
| `Subrot` | subspace rotation | 4 | self-consistency cycle | Diagonalization within the subspace spanned by the current orbitals. Rarely used stand-alone. |
| `Eigenval` | recompute eigenvalues | 3 | postprocessing | Recompute one-electron energies, the density of states, and selected postprocessing from fixed orbitals (e.g., read from the [WAVECAR](../input-files/WAVECAR.md) file). |
| `None` / `Nothing` | no orbital update | 2 | postprocessing | Recompute the density of states or postprocessing from fixed orbitals *and* one-electron energies (e.g., read from the [WAVECAR](../input-files/WAVECAR.md) file). |

|  |
|----|
| **Warning:** Only the iterative [self-consistency-cycle](../theory/Self-consistency_cycle.md) minimizers support potential-only functionals/methods, e.g., [`METAGGA`](METAGGA.md)` = MBJ` or [`LSFBXC`](LSFBXC.md)` = True`. This is because direct optimization relies on the gradient of the energy and not just the potential. |

|  |
|----|
| **Tip:** Except for `None`, `Nothing`, `Exact`, and `Eigenval` (which must be spelled out), only the first letter determines the selected algorithm. |

`Conjugate`, `Subrot`, `Eigenval`, `None`, and `Nothing` are supported
as of vasp.5.2.9. The `Old Fast`/`Old VeryFast` variants (also `of`/`fo`
and `ov`/`vo`) are available in vasp.6 and select the corresponding
vasp.5 algorithms. For more technical details, read
[IALGO](IALGO.md) and [LDIAG](LDIAG.md).

### Recommendations\[<a href="/wiki/index.php?title=ALGO&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Recommendations">edit</a> \| (./index.php.md)\]

- **Most systems**:
  `ALGO`` = Normal` (blocked
  Davidson) is the most robust choice and the default.
- **Large systems and molecular dynamics**:
  [RMM-DIIS](../theory/RMM-DIIS.md) (`Fast` or `VeryFast`) reduces
  the *O*(*N*<sup>3</sup>) orthonormalization cost and is faster for
  large cells; combine with [`LREAL`](LREAL.md)` = Auto`.
  VeryFast needs good initial orbitals (it uses a large
  [NELMDL](NELMDL.md)) and is the least robust on its own.
  For <a href="/wiki/MD_calculations" class="mw-redirect"
  title="MD calculations">MD calculations</a> and [structure
  optimization](../tutorials/Structure_optimization.md)
  or metals, also mind that barely occupied bands are less optimized
  ([WEIMIN](WEIMIN.md)).
- **<a href="/wiki/Magnetic_materials" class="mw-redirect"
  title="Magnetic materials">Magnetic materials</a>,
  <a href="/wiki/DFT%2BU" class="mw-redirect" title="DFT+U">DFT+U</a>,
  [meta-GGA](../categories/Category-Exchange-correlation_functionals.md) "Category:Exchange-correlation functionals"),
  [Hartree-Fock and hybrid
  functionals](../categories/Category-Exchange-correlation_functionals.md)_and_hybrid_functionals "Category:Exchange-correlation functionals")**:
  The [direct
  optimizers](../theory/Direct_optimization_of_the_orbitals.md)
  `ALGO`` = All` (or
  `Conjugate`) are more robust and recommended; use the improved line
  search ([`ISEARCH`](ISEARCH.md)` = 1`).
  `ALGO`` = VeryFast` is
  **not** supported for hybrid functionals.
- **Metals or small-gap systems with Hartree–Fock / meta-GGA**: You may
  try `ALGO`` = Damped` with
  an appropriate time step ([TIME](TIME.md)) and a somewhat
  larger [NBANDS](NBANDS.md), if other algorithms fail.
- **Potential-only functionals or methods** (e.g.,
  [`METAGGA`](METAGGA.md)` = MBJ` or
  [LSFBXC](LSFBXC.md)): use
  `ALGO`` = Normal`. Because
  these functionals provide only a potential and no consistent total
  energy, the iterative
  [self-consistency-cycle](../theory/Self-consistency_cycle.md)
  minimizers work by applying the Hamiltonian repeatedly without taking
  the expression of the energy into account.
- **Elongated geometries, systems including vacuum, slabs, surfaces**:
  prefer the mixing
  ([self-consistency-cycle](../theory/Self-consistency_cycle.md))
  algorithms (`Normal` or `Fast`). These systems are prone to charge
  sloshing, which can be reduced by fine-tuning the [mixing
  tags](../categories/Category-Density_mixing.md)
  ([AMIX](AMIX.md), [BMIX](BMIX.md), …); see
  [Troubleshooting electronic
  convergence](../tutorials/Troubleshooting_electronic_convergence.md).
  For fast convergence of the self-consistency cycle,
  [LMAXMIX](LMAXMIX.md) must be set appropriately, e.g.,
  [`LMAXMIX`](LMAXMIX.md)` = 6` for systems with *f*
  electrons.
- **Preparing many empty states** (e.g., for
  <a href="/wiki/GW_calculations" class="mw-redirect"
  title="GW calculations">GW</a> or
  [RPA](../methods/ACFDT__RPA_calculations.md)), run
  `ALGO`` = Exact` after a
  normal <a href="/wiki/Ground-state_calculations" class="mw-redirect"
  title="Ground-state calculations">ground-state calculation</a>.
- **Postprocessing from a [WAVECAR](../input-files/WAVECAR.md)**:
  `ALGO`` = Eigenval`
  recomputes one-electron energies and the [density of
  states](../categories/Category-Density_of_states.md);
  `ALGO`` = None` recomputes
  occupancies and the [density of
  states](../categories/Category-Density_of_states.md).

## Output during the electronic minimization\[<a href="/wiki/index.php?title=ALGO&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Output during the electronic minimization">edit</a> \| (./index.php.md)\]

At each electronic step, VASP writes one line to standard output and to
the [OSZICAR](../output-files/OSZICAR.md) file. For example:

          N       E                     dE             d eps       ncg     rms          rms(c)
    DAV:   1     0.230591997322E+03    0.23059E+03   -0.16471E+04 13824   0.142E+03
    DAV:   2     0.128984547176E+02   -0.21769E+03   -0.20617E+03 12600   0.334E+02
    DAV:   3    -0.871201735783E+01   -0.21610E+02   -0.21211E+02 14288   0.100E+02
    DAV:   4    -0.952629881459E+01   -0.81428E+00   -0.81287E+00 15680   0.208E+01
    DAV:   5    -0.954352651394E+01   -0.17228E-01   -0.17224E-01 15640   0.295E+00    0.119E+01
    ...

The leading label marks the algorithm (and phase) used in that step. SCF
runs from scratch always begin with a delay
([NELMDL](NELMDL.md) non-self-consistent blocked-Davidson
sweeps) at fixed density, so the first steps for `Fast`, `VeryFast`,
`All`, `Damped` (and all steps for `Normal`) are labeled `DAV:`:

|  |  |
|----|----|
| Label | Algorithm |
| `DAV:` | [blocked Davidson](../theory/Blocked-Davidson_algorithm.md) ([IALGO](IALGO.md)=38; ALGO=Normal and the initial phase of `Fast`, `VeryFast`, `All` and `Damped`) |
| `RMM:` | [RMM-DIIS](../theory/RMM-DIIS.md) ([IALGO](IALGO.md)=48; ALGO=VeryFast and the main phase of `Fast`) |
| `SDA:` / `CGA:` | steepest-descent / conjugate-gradient all-band step ([`IALGO`](IALGO.md)` = 58`; ALGO=All or `Conjugate`) |
| `DMP:` | damped dynamics ([`IALGO`](IALGO.md)` = 53`; `ALGO`` = Damped`) |
| `DIA:` | (subspace) diagonalization (`ALGO`` = Exact` or `Subrot`) |
| `EIG:` | eigenvalue recomputation (`ALGO`` = Eigenval`) |
| `NONE` | no orbital update (`ALGO`` = None/Nothing`) |

The columns are:

- **N**: index of the electronic (self-consistency) step.
- **E**: total (free) energy in eV at this step.
- **dE**: change of the total energy with respect to the previous step.
- **d eps**: change of the band-structure energy (sum of one-electron
  eigenvalues) due to the orbital optimization in this step. This should
  be comparable with **dE** of the subsequent step.
- **ncg**: number of evaluations of the Hamiltonian acting on an orbital
  (*H*Ψ) in this step.
- **rms**: root-mean-square norm of the residual vector
  $|(\mathbf{H}-\epsilon\mathbf{S})\Psi\rangle$, i.e.,
  how well the current orbitals solve the eigenvalue problem.
- The **last column** depends on the algorithm:
  - For the iterative
    [self-consistency-cycle](../theory/Self-consistency_cycle.md)
    minimizers, as well as the postprocessing modes, it is **rms(c)**,
    the root-mean-square change of the charge density in the
    [charge-density
    mixer](../categories/Category-Density_mixing.md). For
    the iterative
    [self-consistency-cycle](../theory/Self-consistency_cycle.md)
    minimizers, it appears only once charge-density mixing has started,
    i.e., after the [NELMDL](NELMDL.md) non-self-consistent
    steps.
  - For the
    [direct-minimization](../theory/Direct_optimization_of_the_orbitals.md)
    algorithms
    (`ALGO`` = All/Conjugate`
    and `Damped`), which update the density directly without a density
    mixer, the column is headed **ort** instead and reports the
    orthonormality error of the orbitals.

The electronic loop stops once the energy change **dE** drops below the
threshold set by [EDIFF](EDIFF.md), or after
[NELM](NELM.md) steps. See [Setting up an electronic
minimization](../tutorials/Setting_up_an_electronic_minimization.md)
for guidance on choosing these tags, and [IALGO](IALGO.md)
for further details on the algorithms.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vblue); --box-emph-color: var(--vblue); padding: 5px; color: var(--vdefault-text-nb); background: var(--vblue-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vblue);">Tip:</span></strong> In
order to judge convergence:
<ul>
<li>Plot the total energy <strong>E</strong> minus the final total
energy (<strong>E</strong> of the last step) as a function of electronic
steps. The decay should be exponential. You may observe accidental
stopping or very slow convergence if <span class="smj-container"
style="opacity:.5">$E-E_{final}$</span> is
noisy.</li>
<li>Plot <strong>rms(c)</strong> as a function of electronic steps
<strong>N</strong>. Large values indicate the electronic density is
still changing and perhaps fluctuating (charge sloshing).</li>
</ul></td>
</tr>
</tbody>
</table>

### Line-search output (direct optimizers)\[<a href="/wiki/index.php?title=ALGO&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Line-search output (direct optimizers)">edit</a> \| (./index.php.md)")\]

For `ALGO`` = All/Conjugate`,
each step also prints the diagnostics of the conjugate-gradient line
minimization ([ISEARCH](ISEARCH.md)), for example:

    CGA:   8    -0.815350365436E+01   -0.26844E+00   -0.26700E+00   896   0.102E+00   0.183E-02
    gam= 0.117 g(H,U,f)=  0.861E-01 0.436E-02 0.112E-01 ort(H,U,f) =-0.290E-01 0.260E-01 0.476E-02
    gam= 0.117 trial= 0.425  step=  1.5048 mean=  0.4252
     continued last = 0.638  step=  0.9339 harm=  0.9495 4th-ord=  0.9585 spline=  0.9339
     steps along line     -0.425E-04  0.425E-04  0.425E+00  0.143E+01  0.957E+00  0.638E+00
     energies along line   0.433E-05 -0.433E-05 -0.372E-01 -0.389E-01 -0.565E-01 -0.492E-01

- **gam** is the conjugate-gradient coefficient that mixes the previous
  search direction into the current one.
- **g(H,U,f)** are the norms of the energy gradient with respect to the
  three optimized degrees of freedom: the orbital coefficients (*H*),
  the subspace rotation (*U*), and the partial occupancies (*f*).
- **ort(H,U,f)** is the overlap of the current gradient with the
  previous search direction for each of these; it should be close to
  zero when the preceding line minimization was accurate.
- **trial**, **step**, and **mean** are the trial step length, the step
  actually taken, and the running mean of the trial step.
- **continued last … harm / 4th-ord / spline** are refined optimal-step
  estimates from a harmonic (second-order), fourth-order-polynomial, and
  spline fit when extra points are sampled along the line.
- **steps along line** and **energies along line** list the trial step
  lengths probed along the search direction and the corresponding total
  energies, from which the minimum is located.

 

## ALGO for response functions, <a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW</a>, and [ACFDT/RPA](../methods/ACFDT__RPA_calculations.md)\[<a href="/wiki/index.php?title=ALGO&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: ALGO for response functions, GW, and ACFDT/RPA">edit</a> \| (./index.php.md)\]

The following tags are available as of VASP.5.X.

- `ALGO`` = CHI` calculates
  the response functions only.

<!-- -->

- `ALGO`` = TDHF` selects TDHF
  (or
  [TDDFT](../methods/Time-dependent_density-functional_theory_calculations.md))
  calculations using the VASP internal Cassida code see
  <a href="/wiki/BSE_calculations" class="mw-redirect"
  title="BSE calculations">BSE calculations</a>, (available as of
  VASP.5.2.12)

<!-- -->

- `ALGO`` = BSE` selects BSE
  calculations using the VASP internal Cassida code see
  <a href="/wiki/BSE_calculations" class="mw-redirect"
  title="BSE calculations">BSE calculations</a>, (available as of
  VASP.5.4.1)

<!-- -->

- `ALGO`` = Timeev` performs a
  delta-pulse in time and then performs
  <a href="/wiki/Timepropagation" class="mw-redirect"
  title="Timepropagation">timepropagation</a>

<!-- -->

- `ALGO`` = ACFDT` selects RPA
  total energy calculations see [ACFDT/RPA
  calculations](../methods/ACFDT__RPA_calculations.md)

<!-- -->

- `ALGO`` = RPA` synonymous to
  ACFDT see [ACFDT/RPA
  calculations](../methods/ACFDT__RPA_calculations.md)
  (available as of VASP.5.3.1)

GW tags have been renamed in VASP as follows 


|                  |      |       |      |       |     |      |
|------------------|------|-------|------|-------|-----|------|
| \< 5.2.12        | scGW | scGW0 | GW   | GW0   | N/A | N/A  |
| \>= 5.2.12, \< 6 | QPGW | QPGW0 | GW   | GW0   | N/A | N/A  |
| \>= 6            | QPGW | QPGW0 | EVGW | EVGW0 | GWR | GW0R |

- `ALGO`` = EVGW0` selects
  single-shot *G*<sub>0</sub>*W*<sub>0</sub> calculations or partially
  self-consistent *GW* calculations. The orbitals (wavefunctions) of the
  previous groundstate calculations are maintained, and
  <a href="/wiki/GW_calculations#G0W0" class="mw-redirect"
  title="GW calculations">G0W0 calculations</a> are performed. If
  [NELM](NELM.md) is set, several iterations are performed,
  and the QP energies are updated in the calculation of *G* (for
  details, see <a href="/wiki/GW_calculations#gw0" class="mw-redirect"
  title="GW calculations">EVGW0 calculations</a>).

<!-- -->

- `ALGO`` = EVGW` selects
  partially self-consistent (eigenvalue-self-consistent) *GW*
  calculations. The orbitals of the previous ground-state calculation
  are maintained; over [NELM](NELM.md) iterations the QP
  energies are updated in the calculation of *G* AND *W* (for details,
  see <a href="/wiki/GW_calculations#qpgw" class="mw-redirect"
  title="GW calculations">self-consistent EVGW and QPGW calculations</a>).

<!-- -->

- `ALGO`` = QPGW0` selects
  self-consistent *GW* calculations including off-diagonal components of
  the self-energy. A full update of the QP energies AND one-electron
  orbitals is performed in the calculation of *G* only (for details see
  <a href="/wiki/GW_calculations#qpgw0" class="mw-redirect"
  title="GW calculations">QPGW0 calculations</a>).

<!-- -->

- `ALGO`` = QPGW` selects
  self-consistent *GW* calculations, including off-diagonal components
  of the self-energy. A full update of the QP energies AND one-electron
  orbitals is performed in the calculations of *G* AND *W* (for details,
  see <a href="/wiki/GW_calculations#qpgw" class="mw-redirect"
  title="GW calculations">QPGW calculations</a>).

Following tags are available as of VASP.6

- `ALGO`` = RPAR` selects low
  scaling RPA total energy calculations (for details see [ACFDT/RPA
  calculations](../methods/ACFDT__RPA_calculations.md))

<!-- -->

- `ALGO`` = ACFDTR` synonym
  for RPAR (for details see [ACFDT/RPA
  calculations](../methods/ACFDT__RPA_calculations.md))

<!-- -->

- `ALGO`` = ACFDTRK` in
  combination with [`LMP2LT`](LMP2LT.md)` = True` selects
  the low scaling MP2 total energy calculations (for details see the
  [MP2 ground state
  Tutorial](../tutorials/MP2_ground_state_calculation_-_Tutorial.md))

<!-- -->

- `ALGO`` = GW0R` selects
  self-consistent GW<sub>0</sub> calculations, where only the Green's
  function *G* is updated from the corresponding Dyson. The screened
  potential *W* remains unchanged after the first iteration.
  [NELM](NELM.md) iteration cycles are performed (see
  <a href="/wiki/GW_calculations#scGW0R" class="mw-redirect"
  title="GW calculations">self-consistent GW calculations</a>).

<!-- -->

- `ALGO`` = GWR` selects
  self-consistent GW calculations, where both, *G* and *W* are updated
  from the corresponding Dyson equation. [NELM](NELM.md)
  iteration cycles are performed. (for details see
  <a href="/wiki/GW_calculations#scGWR" class="mw-redirect"
  title="GW calculations">self-consistent GW calculations</a>).

<!-- -->

- `ALGO`` = G0W0R` selects
  single-shot GW calculations, non-interacting *G* and *W* are
  determined from Kohn-Sham system and [NELM](NELM.md) tag is
  ignored. Use this tag for single-shot QP energies and first-order
  corrections to the density matrix (for details, see
  <a href="/wiki/GW_calculations#G0W0R" class="mw-redirect"
  title="GW calculations">single-shot GW calculations</a>).

|  |
|----|
| **Important:** Changes as of VASP.6.3: |

- [NELMGW](NELMGW.md) replaces [NELM](NELM.md) in
  <a href="/wiki/GW_calculations#scGWR" class="mw-redirect"
  title="GW calculations">self-consistent GW calculations</a>.

<!-- -->

- `ALGO`` = CRPA` selects
  [constrained RPA
  calculations](../theory/Constrained–random-phase–approximation_formalism.md).

|  |
|----|
| **Important:** available as of VASP.6.4: |

- `ALGO`` = EVGW0R` selects
  the low-scaling analog of EVGW0, that is the low-scaling partially
  self-consistent GW calculations, where non-interacting *G* and *W* are
  determined from Kohn-Sham system and [NELMGW](NELMGW.md)
  specifies the number of self-consistent loops for *G*. *W* is kept on
  the Kohn-Sham level.

## Related tags and articles\[<a href="/wiki/index.php?title=ALGO&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Setting up an electronic
minimization](../tutorials/Setting_up_an_electronic_minimization.md),
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>,
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a>,
[ACFDT/RPA_calculations](../methods/ACFDT__RPA_calculations.md)

[IALGO](IALGO.md), [LDIAG](LDIAG.md),
[NELM](NELM.md), [NELMDL](NELMDL.md),
[EDIFF](EDIFF.md), [LMAXMIX](LMAXMIX.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ALGO-_incategory-HowTo)



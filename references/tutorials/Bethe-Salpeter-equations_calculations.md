<!-- Source: https://vasp.at/wiki/index.php/Bethe-Salpeter-equations_calculations | revid: 30526 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bethe-Salpeter-equations calculations


VASP offers a powerful module for solving the Bethe-Salpeter (BSE)
equation<sup>[\[1\]](#cite_note-albrecht:prl:98-1)[\[2\]](#cite_note-rohlfing:prl:98-2)</sup>.
The BSE can be used for obtaining the frequency-dependent dielectric
function with the excitonic effects and can be based on the ground-state
electronic structure in the DFT, hybrid-functional or *GW*
approximations.


## Contents


- [1 Solving
  Bethe-Salpeter equation](#Solving_Bethe-Salpeter_equation)
- [2 Bethe-Salpeter
  equation calculation](#Bethe-Salpeter_equation_calculation)
- [3 Model BSE
  (mBSE)](#Model_BSE_(mBSE))
- [4 Calculations
  beyond Tamm-Dancoff
  approximation](#Calculations_beyond_Tamm-Dancoff_approximation)
- [5 Calculations
  at finite wavevectors](#Calculations_at_finite_wavevectors)
- [6 Consistency
  tests](#Consistency_tests)
  - [6.1 First
    test: IP dielectric
    function](#First_test:_IP_dielectric_function)
  - [6.2 Second
    test: RPA dielectric
    function](#Second_test:_RPA_dielectric_function)
  - [6.3 Third
    test: RPA correlation
    energy](#Third_test:_RPA_correlation_energy)
- [7 Common
  issues](#Common_issues)
- [8 Related tags
  and articles](#Related_tags_and_articles)
- [9
  References](#References)


## Solving Bethe-Salpeter equation\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Solving Bethe-Salpeter equation">edit</a> \| (./index.php.md)\]

To take into account the excitonic effects or the electron-hole
interaction, one has to use approximations beyond the
independent-particle (IP) and the random-phase approximations
([RPA](../methods/RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md)).
In VASP, it is done via the algorithm selected by
[ALGO](../incar-tags/ALGO.md) = BSE. These essentially solves the same
equations (Casida/Bethe-Salpeter) but differ in the way the screening of
the Coulomb potential is treated. The TDHF approach uses the
exact-correlation kernel $f_{\rm xc}$,
whereas BSE requires the $W(\omega \to 0)$ from a preceding *GW* calculation. Thus, in order to
perform TDHF or BSE calculations, one has to provide the ground-state
orbitals ([WAVECAR](../input-files/WAVECAR.md)) and the derivatives of the
orbitals with respect to $k$
([WAVEDER](../input-files/WAVEDER.md)). In addition, the BSE calculation
requires files storing the screened Coulomb kernel produced in a *GW*
calculation, i.e., [Wxxxx.tmp](../input-files/Wxxxx.tmp.md).

In summary, both TDHF and BSE approaches require a preceding
ground-state calculation, however, the TDHF does not need the preceding
*GW* and can be performed with the DFT or hybrid-functional orbitals and
energies.

## Bethe-Salpeter equation calculation\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Bethe-Salpeter equation calculation">edit</a> \| (./index.php.md)\]

The BSE calculations require a preceding *GW* step to determine the
screened Coulomb kernel $W_{GG'}(q,\omega \to 0 )$. The details on *GW* calculations can be found in the
practical guide to
[*GW*](../methods/Practical_guide_to_GW_calculations.md)
calculations. Here, we note that during the *GW* calculation, VASP
writes this kernel into the following files

    W0001.tmp, W0002.tmp, ..., W{NKPTS}.tmp

and

    WFULL0001.tmp, WFULL0002.tmp, ..., WFULL{NKPTS}.tmp.

The files [Wxxxx.tmp](../input-files/Wxxxx.tmp.md) store only the
diagonal terms of the kernel and are fairly small, whereas the files
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) store the full
matrix. It is important to make sure in the *GW* step that the flag
[LWAVE](../incar-tags/LWAVE.md) = .TRUE. is set, so that the
[WAVECAR](../input-files/WAVECAR.md) stores the one-electron *GW* energies
and the one-electron orbitals, if the *GW* calculation is
self-consistent. In the low-scaling *GW* algorithm use the
[NOMEGA_DUMP](../incar-tags/NOMEGA_DUMP.md) tag to produce the
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) files.

For the self-consistent *GW* calculations the following flags should be
added

    LOPTICS   = .TRUE. 
    LPEAD     = .TRUE.

in order to update the [WAVEDER](../input-files/WAVEDER.md) using finite
differences ([LPEAD](../incar-tags/LPEAD.md) = .TRUE.). The type of *GW*
calculation is selected with the [ALGO](../incar-tags/ALGO.md) tag, which is
discussed in great detail in the practical guide to *GW* calculations.

Once the *GW* step is completed, the BSE calculation can be performed
using the following setup

    SYSTEM    = Si
    NBANDS    = same as in GW calculation
    ISMEAR    = 0
    SIGMA     = 0.05
    ALGO      = BSE
    NBANDSO   = 4       ! determines how many occupied bands are used
    NBANDSV   = 8       ! determines how many unoccupied (virtual) bands are used
    OMEGAMAX  = desired_maximum_excitation_energy 

Considering that quasiparticle energies in *GW* converge very slowly
with the number of unoccupied bands and require large
[NBANDS](../incar-tags/NBANDS.md), the number of bands included in the BSE
calculation should be restricted explicitly by setting the occupied and
unoccupied bands ([NBANDSO](../incar-tags/NBANDSO.md) and
[NBANDSV](../incar-tags/NBANDSV.md)) included in the BSE Hamiltonian.

VASP tries to use sensible defaults, but it is highly recommended to
check the [OUTCAR](../output-files/OUTCAR.md) file and make sure that the
right bands are included. The tag [OMEGAMAX](../incar-tags/OMEGAMAX.md)
specifies the maximum excitation energy of included electron-hole pairs
and the pairs with the one-electron energy difference beyond this limit
are not included in the BSE Hamiltonian. Hint: The convergence with
respect to [NBANDSV](../incar-tags/NBANDSV.md) and
[OMEGAMAX](../incar-tags/OMEGAMAX.md) should be thoroughly checked as
the real part of the dielectric function, as well as the correlation
energy, is usually very sensitive to these values, whereas the imaginary
part of the dielectric function converges quickly.

At the beginning of the BSE calculation, VASP will try to read the
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) files and if these
files are not found, VASP will read the
[Wxxxx.tmp](../input-files/Wxxxx.tmp.md) files. For small isotropic bulk
systems, the diagonal approximation of the dielectric screening may be
sufficient and yields results very similar to the calculation with the
full dielectric tensor
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md). Nevertheless, for
molecules and atoms as well as surfaces, the full-screened Coulomb
kernel is strictly required.

Both TDHF and BSE approaches write the calculated frequency-dependent
dielectric function as well as the excitonic energies in the
[vasprun.xml](../output-files/Vasprun.xml.md) file.

## Model BSE (mBSE)\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Model BSE (mBSE)">edit</a> \| (./index.php.md)")\]

BSE calculations can be performed using a model dielectric
function<sup>[\[3\]](#cite_note-bokdam:scr:2016-3)[\[4\]](#cite_note-tal:prr:2020-4)</sup>.
In this approach the calculation of the screened Coulomb potential is
not required. Instead, the model dielectric function can be used to
describe the screening of the Coulomb potential by setting the tag
[LMODELHF](../incar-tags/LMODELHF.md) with parameters
[AEXX](../incar-tags/AEXX.md) and [HFSCREEN](../incar-tags/HFSCREEN.md).

Model BSE calculation can be performed the following steps:

1.  ground-state calculation
2.  GW calculation (optional in model BSE calculation)
3.  optical absorption calculation via model BSE

For example, an optical absorption calculation of bulk Si can be
performed using a model dielectric function as described in Ref.
<sup>[\[4\]](#cite_note-tal:prr:2020-4)</sup>.

    SYSTEM    = Si
    ISMEAR    = 0 
    SIGMA     = 0.05
    NBANDS    = 16      ! or any larger desired value
    ALGO      = D       ! Damped algorithm often required for HF type calculations, ALGO = Normal might work as well
    LHFCALC   = .TRUE. 
    LMODELHF  = .TRUE. 
    AEXX      = 0.083
    HFSCREEN  = 1.22
    LOPTICS   = .TRUE.  ! can also be done in an additional intermediate step

In the second step, the dielectric function is evaluated by solving the
Casida equation

    SYSTEM    = Si
    ISMEAR    = 0 
    SIGMA     = 0.05
    NBANDS    = 16     
    ALGO      = TDHF
    IBSE      = 0
    NBANDSO   = 4       ! number of occupied bands
    NBANDSV   = 8       ! number of unoccupied bands
    LHARTREE  = .TRUE.
    LADDER    = .TRUE.
    LFXC      = .FALSE. ! local xc kernel is disabled in mBSE 
    LMODELHF  = .TRUE. 
    AEXX      = 0.083
    HFSCREEN  = 1.22

## Calculations beyond Tamm-Dancoff approximation\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Calculations beyond Tamm-Dancoff approximation">edit</a> \| (./index.php.md)\]

The TDHF and BSE calculations beyond the Tamm-Dancoff approximation
(TDA)<sup>[\[5\]](#cite_note-sander:prb:15-5)</sup>
can be performed by setting the [ANTIRES](../incar-tags/ANTIRES.md) = 2
in the [INCAR](../input-files/INCAR.md) file

    SYSTEM       = Si
    NBANDS       = same as in GW calculation
    ISMEAR       = 0
    SIGMA        = 0.05
    ALGO         = BSE  
    ANTIRES      = 2      ! beyond Tamm-Dancoff
    LORBITALREAL = .TRUE. 
    NBANDSO      = 4 
    NBANDSV      = 8

The flag [LORBITALREAL](../incar-tags/LORBITALREAL.md) = .TRUE.
forces VASP to make the orbitals $\phi({\bf r})$ real valued at the Gamma point as well as k-points at
the edges of the Brillouin zone. This can improve the performance of
BSE/TDHF calculations but it should be used consistently with the
ground-state calculation.

## Calculations at finite wavevectors\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Calculations at finite wavevectors">edit</a> \| (./index.php.md)\]

VASP can also calculate the dielectric function at a
${\bf q}$-vector compatible with the k-point grid
(finite-momentum excitons).

    SYSTEM       = Si
    NBANDS       = same as in GW calculation
    ISMEAR       = 0 
    SIGMA        = 0.05
    ALGO         = BSE  
    ANTIRES      = 2 
    KPOINT_BSE   = 3 -1 0 0  ! q-point index,  three integers
    LORBITALREAL = .TRUE.
    NBANDSO      = 4 
    NBANDSV      = 8

The tag [KPOINT_BSE](../incar-tags/KPOINT_BSE.md) sets the
${\bf q}$-point and the shift at which the dielectric
function is calculated. The first integer specifies the index of the
${\bf q}$-point and the other three values shift the
provided ${\bf q}$-point by an arbitrary reciprocal vector
$\bf G$. The reciprocal lattice vector is supplied by
three integer values $n_i$ with
${\bf G}= n_1 {\bf G}_1+n_2 {\bf G}_2+n_3 {\bf G}_3$.
This feature is only supported as of VASP 6 (in VASP 5 the feature can
be enabled, but the results are erroneous).

|  |
|----|
| **Mind:** In the limit of infinitesimal momentum $\bf q$, $\varepsilon_{\alpha\beta}(q \to 0)$ is a $3\times 3$ tensor, where $\alpha=\\x,y,z\\$ and $\beta=\\x,y,z\\$. However, at a finite momentum $\varepsilon(\bf q \neq 0)$ is a scalar, i.e., has a single component. |

## Consistency tests\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Consistency tests">edit</a> \| (./index.php.md)\]

In order to verify the results obtained in the BSE calculation, one can
perform a number of consistency tests.

### First test: IP dielectric function\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: First test: IP dielectric function">edit</a> \| (./index.php.md)\]

The BSE code can be used to reproduce the independent particle spectrum
if the RPA and the ladder diagrams are switched off

    LADDER   = .FALSE. 
    LHARTREE = .FALSE.

This should yield exactly the same dielectric function as the preceding
calculation with [LOPTICS](../incar-tags/LOPTICS.md) = .TRUE. We
recommend to set the complex shift manually in the BSE as well as the
preceding optics calculations, e.g. [CSHIFT](../incar-tags/CSHIFT.md) =
0.4. The dielectric functions produced in these calculations should be
identical.

### Second test: RPA dielectric function\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Second test: RPA dielectric function">edit</a> \| (./index.php.md)\]

The RPA/*GW* dielectric function can be used to verify the correctness
of the RPA dielectric function calculated via the BSE algorithm. The RPA
dielectric function in the BSE code can be calculated by switching off
the ladder diagrams while keeping the RPA terms, i.e., the BSE
calculation should be performed with the following tags

    ANTIRES   = 2
    LHARTREE  = .TRUE.
    LADDER    = .FALSE.
    CSHIFT    = 0.4

The same dielectric function should be obtained via the *GW* code by
setting these flags

    ALGO      = CHI 
    NOMEGA    = 200
    CSHIFT    = 0.4

Make sure that a large [CSHIFT](../incar-tags/CSHIFT.md) is selected as
the *GW* code calculates the polarizability at very few frequency
points. Note that the *GW* code does not use the TDA, so
[ANTIRES](../incar-tags/ANTIRES.md) = 2 is required for the TDHF/BSE
calculation. In our experience, the agreement can be made practically
perfect provided sufficient frequency points are used and all available
occupied and virtual orbitals are included in the BSE step.

### Third test: RPA correlation energy\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Third test: RPA correlation energy">edit</a> \| (./index.php.md)\]

The BSE code can be used to calculate the correlation energy via the
plasmon equation. This correlation energy can be compared with the [RPA
contributions](../methods/ACFDT__RPA_calculations.md) to
the correlation energies for each ${\bf q}$-point, which can be found in the
[OUTCAR](../output-files/OUTCAR.md) file of the ACFDT/RPA calculation
performed with [ALGO](../incar-tags/ALGO.md) = RPA:

    q-point correlation energy      -0.232563      0.000000
    q-point correlation energy      -0.571667      0.000000
    q-point correlation energy      -0.176976      0.000000

For instance, if the BSE calculation is performed at the second
${\bf q}$-point

    ANTIRES    = 2
    LADDER     = .FALSE.
    LHARTREE   = .TRUE.
    KPOINT_BSE = 2 0 0 0

the same correlation energy should be found in the corresponding
[OUTCAR](../output-files/OUTCAR.md) file:

    plasmon correlation energy        -0.5716670828

For exact compatibility, [ENCUT](../incar-tags/ENCUT.md) and
[ENCUTGW](../incar-tags/ENCUTGW.md) should be set to the same values in
all calculations, while the head and wings of the dielectric matrix
should not be included in the ACFDT/RPA calculations, i.e., remove the
[WAVEDER](../input-files/WAVEDER.md) file prior to the ACFDT/RPA
calculation. In the BSE/RPA calculation removing the
[WAVEDER](../input-files/WAVEDER.md) file is not required. Furthermore,
[NBANDS](../incar-tags/NBANDS.md) in the ACFDT/RPA calculation must be
identical to the number of included bands
[NBANDSO](../incar-tags/NBANDSO.md) plus
[NBANDSV](../incar-tags/NBANDSV.md) in the BSE/RPA, so that the same
number of excitation pairs are included in both calculations. Also, the
[OMEGAMAX](../incar-tags/OMEGAMAX.md) tag in the BSE calculation should
not be set.

## Common issues\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Common issues">edit</a> \| (./index.php.md)\]

If the dielectric matrix contains only zeros in the
[vasprun.xml](../output-files/Vasprun.xml.md) file, the
[WAVEDER](../input-files/WAVEDER.md) file was not read or is incompatible
to the [WAVEDER](../input-files/WAVEDER.md) file. This requires a
recalculation of the [WAVEDER](../input-files/WAVEDER.md) file. This can
be achieved even after *GW* calculations using the following
intermediate step:

    ALGO      = Nothing
    LOPTICS   = .TRUE.
    LPEAD     = .TRUE.

The flag [LPEAD](../incar-tags/LPEAD.md) = .TRUE. is strictly required and
enforces a "numerical" differentiation of the orbitals with respect to
$k$. Calculating the derivatives of the orbitals with
respect to $k$
analytically is not possible at this point, since the Hamiltonian that
was used to determine the orbitals is unknown to VASP.

## Related tags and articles\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ALGO](../incar-tags/ALGO.md), [LOPTICS](../incar-tags/LOPTICS.md),
[LPEAD](../incar-tags/LPEAD.md), [LHFCALC](../incar-tags/LHFCALC.md),
[LRPA](../incar-tags/LRPA.md), [LADDER](../incar-tags/LADDER.md),
[LHARTREE](../incar-tags/LHARTREE.md),
[NBANDSV](../incar-tags/NBANDSV.md), [NBANDSO](../incar-tags/NBANDSO.md),
[OMEGAMAX](../incar-tags/OMEGAMAX.md), [LFXC](../incar-tags/LFXC.md),
[ANTIRES](../incar-tags/ANTIRES.md), [NBSEEIG](../incar-tags/NBSEEIG.md),
[BSEFATBAND](../output-files/BSEFATBAND.md)

## References\[<a
href="/wiki/index.php?title=Bethe-Salpeter-equations_calculations&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-albrecht:prl:98_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.80.4510"
    class="external text" rel="nofollow">S. Albrecht, L. Reining, R. Del
    Sole, and G. Onida, Phys. Rev. Lett. <strong>80</strong>, 4510-4513
    (1998).</a>
2.  [↑](#cite_ref-rohlfing:prl:98_2-0)
    <a href="https://doi.org/10.1103/PhysRevLett.81.2312"
    class="external text" rel="nofollow">M. Rohlfing and S. G. Louie, Phys.
    Rev. Lett. <strong>81</strong>, 2312-2315 (1998).</a>
3.  [↑](#cite_ref-bokdam:scr:2016_3-0)
    <a href="https://doi.org/10.1038/srep28618" class="external text"
    rel="nofollow">M. Bokdam, T. Sander, A. Stroppa, S. Picozzi, D. D.
    Sarma, C. Franchini, and G. Kresse, Sci. Rep. <strong>6</strong>, 28618
    (2016).</a>
4.  ↑
    <sup>[a](#cite_ref-tal:prr:2020_4-0)</sup>
    <sup>[b](#cite_ref-tal:prr:2020_4-1)</sup>
    <a href="http://doi.org/10.1103/PhysRevResearch.2.032019"
    class="external text" rel="nofollow">A. Tal, P. Liu, G. Kresse, A.
    Pasquarello, <em>Accurate optical spectra through time-dependent density
    functional theory based on screening-dependent hybrid functionals</em>,
    Phys. Rev. Research <em>2</em>, 032019 (2020)</a>
5.  [↑](#cite_ref-sander:prb:15_5-0)
    <a href="https://doi.org/10.1103/PhysRevB.92.045209"
    class="external text" rel="nofollow">T. Sander, E. Maggio, and G.
    Kresse, <em>Beyond the Tamm-Dancoff approximation for extended systems
    using exact diagonalization</em>, Phys. Rev. B <strong>92</strong>,
    045209 (2015).</a>


------------------------------------------------------------------------



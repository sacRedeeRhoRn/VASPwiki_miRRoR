<!-- Source: https://vasp.at/wiki/index.php/GW_and_dielectric_matrix | revid: 35523 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GW and dielectric matrix



## Contents


- [1 Spectral
  Method](#spectral-method)
- [2 Direct
  calculation of the dielectric
  function](#direct-calculation-of-the-dielectric-function)
- [3 Local field
  effects](#local-field-effects)
- [4
  Output](#output)
- [5 Comparison
  with k-p and density perturbation
  theory](#comparison-with-k-p-and-density-perturbation-theory)
- [6 Technical
  tips](#technical-tips)


For GW calculations the frequency dependent dielectric matrix
$\epsilon(\omega)$ in the Random Phase Approximation
(RPA) is determined via the polarizability ${\bf \chi}$
and the Coulomb potential $V$ using
$\epsilon(\omega)= 1 -V \cdot \chi(\omega)$.

|  |
|----|
| **Mind:** [low-scaling GW algorithms](Practical_guide_to_GW_calculations.md) determine the dielectric matrix on the imaginary frequency axis and cannot be used to calculate ${\bf \epsilon}$ on the real frequency axis. |

The real-frequency dependent dielectric matrix can be calculated with
the quartic-scaling GW implementation, in which usability is limited to
relatively small unit cells containing a few dozen atoms at maximum.
Here, two algorithms are available and can be selected via
[LSPECTRAL](../incar-tags/LSPECTRAL.md). The methods are discussed
below.

If only the frequency-dependent dielectric matrix should be computed,
[ALGO](../incar-tags/ALGO.md)=*CHI* can be used to skip the calculation of
GW quasi-particle energies.

|  |
|----|
| **Mind:** [All GW calculations require a preceding DFT calculation with many unoccupied states.](Practical_guide_to_GW_calculations.md) |

There is a lecture available on our YouTube channel on calculating the
<a href="https://youtu.be/6F_WNIh6V7I" class="external text"
rel="nofollow">optical gap</a> and
<a href="https://youtu.be/3YKJZHmcGhY" class="external text"
rel="nofollow">dielectric properties</a>.

## Spectral Method\[<a
href="/wiki/index.php?title=GW_and_dielectric_matrix&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Spectral Method">edit</a> \| (./index.php.md)\]

The spectral method is selected by
[LSPECTRAL](../incar-tags/LSPECTRAL.md)=*.TRUE.*, which is the default
value. Here, VASP computes the polarizability in two steps.

First, the spectral density of the polarizability is calculated using
Fermi's golden
rule<sup>[\[1\]](#cite_note-gajdos:prb:2006-1)[\[2\]](#cite_note-shishkin:prb:2006-2)</sup>

$S_{{\bf G G}'}({\bf q},\omega) = \sum_{nm}\sum_{\bf k q}
\delta(\epsilon_{n\bf k} - \epsilon_{m\bf k-q} -\omega) \left\langle
{n\bf k} \right| {\bf G} \left| {m\bf k-q} \right\rangle \left\langle
{m\bf k-q}\right| {\bf G}' \left| {n\bf k}\right\rangle$

The delta function is approximated by a triangular function centered at
the transition energy. The real and imaginary part of the polarizability
is calculated in a second step using a Hilbert
transformation<sup>[\[2\]](#cite_note-shishkin:prb:2006-2)</sup>

$\chi_{{\bf G G}'}({\bf q},\omega) = \int \mathrm{d}\omega' S_{{\bf G
G}'}({\bf q},\omega') \left( \frac{1}{\omega-\omega' - i \eta } -
\frac{1}{\omega+\omega' + i \eta } \right)$

Here η is an infinitesimal that can be set manually by
[CSHIFT](../incar-tags/CSHIFT.md).

This integration is performed semi-analytically by restricting the
integration variable ω' to a frequency grid that is determined by
[NOMEGA](../incar-tags/NOMEGA.md), [OMEGATL](../incar-tags/OMEGATL.md),
[OMEGAMIN](../incar-tags/OMEGAMIN.md) and
[OMEGAMAX](../incar-tags/OMEGAMAX.md).

Together with the approximation of the delta function in the spectral
density (see above), the integration can be carried out analytically and
one arrives essentially at a matrix-vector product

$\chi_{{\bf G G}'}({\bf q},\omega_j) = \sum_{k=1}^{\rm NOMEGA} t_{jk}
S_{{\bf G G}'}({\bf q},\omega'_k)$

Only the integration weights $t_{jk}$
depend essentially on η, i.e. [CSHIFT](../incar-tags/CSHIFT.md). From the
explicit form of these weights one can deduce that contributions to the
dielectric function at low frequencies depend on the smallest grid
spacing $\Delta_{\min}=\omega'_1-\omega'_2$. These
contributions are suppressed only if $\eta>\Delta_\min$, but yield spurious contributions at low frequencies
in the dielectric function otherwise.

Furthermore, the frequency grid $\omega_j$ of
the complex polarizability is not restricted to the same grid as the
integration variable. That is $\omega_k\neq \omega'_j$ in general. In fact, the resolution of the frequency
grid of the polarizability can be much finer and is set with
[NEDOS](../incar-tags/NEDOS.md).

|  |
|----|
| **Tip:** To reduce spurious contributions in the imaginary part of the dielectric function at small frequencies one can reduce [CSHIFT](../incar-tags/CSHIFT.md) and increase [NOMEGA](../incar-tags/NOMEGA.md). |

However, reducing
[CSHIFT](../incar-tags/CSHIFT.md)
in the spectral method introduces additional spikes in the dielectric
function. Thus for visualization, one often performs a Lorentzian filter
on the raw data, even though such a filter typically shifts peaks of the
original dielectric function. There is no particular reason why the
Lorentzian filter should be used, since smoothing data is essentially
cosmetics; Gaussian smearing is also perfectly acceptable.

A minimal [INCAR](../input-files/INCAR.md) for such a calculation looks as
follows:

    ALGO = CHI   # skip quasi-particle energies 
    NOMEGA = 100 # number of frequency points

Next, an alternative approach, which already includes some sort of
smoothing of the dielectric function, is presented.

## Direct calculation of the dielectric function\[<a
href="/wiki/index.php?title=GW_and_dielectric_matrix&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Direct calculation of the dielectric function">edit</a> \| (./index.php.md)\]

The polarizability can be calculated directly without using a Hilbert
transformation via the formula of Adler and
Wiser.<sup>[\[3\]](#cite_note-adler:1962-3)[\[4\]](#cite_note-wiser:1963-4)</sup>

$\chi_{{\bf G G}'}({\bf q},\omega) = \sum_{nm}\sum_{\bf k q} \left(
\frac{\left\langle {n\bf k} \right| {\bf G} \left| {m\bf k-q}
\right\rangle \left\langle {m\bf k-q}\right| {\bf G}' \left| {n\bf
k}\right\rangle }{\omega-(\epsilon_{n\bf k} - \epsilon_{m\bf k-q}) - i
\eta } - \frac{\left\langle {n\bf k} \right| {\bf G} \left| {m\bf k-q}
\right\rangle \left\langle {m\bf k-q}\right| {\bf G}' \left| {n\bf
k}\right\rangle }{\omega+\epsilon_{n\bf k} - \epsilon_{m\bf k-q} + i
\eta } \right)$

Here [CSHIFT](../incar-tags/CSHIFT.md) influences the peak width of the
dielectric function directly.

This method is selected with
[LSPECTRAL](../incar-tags/LSPECTRAL.md)=*.FALSE.* and yields smoother
dielectric functions than the spectral method described above. Also, the
direct calculation requires less memory.

|  |
|----|
| **Warning:** The direct calculation of the polarizability is much slower than the spectral method. |

A minimal [INCAR](../input-files/INCAR.md) for such a calculation looks as
follows:

    ALGO = CHI          # skip quasi-particle energies 
    LSPECTRAL = .FALSE. # direct calculation of chi
    NOMEGA = 100        # number of frequency points

## Local field effects\[<a
href="/wiki/index.php?title=GW_and_dielectric_matrix&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Local field effects">edit</a> \| (./index.php.md)\]

Both methods support the inclusion of local field effects in the
dielectric function on the RPA level. These effects can be included with
with [LRPA](../incar-tags/LRPA.md)=*.TRUE.*.

|  |
|----|
| **Mind:** The GW routine is the only routine capable to include local field effects for the frequency-dependent dielectric function. |

## Output\[<a
href="/wiki/index.php?title=GW_and_dielectric_matrix&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The imaginary and real part of the frequency-dependent dielectric
function is determined in all GW calculations. It can be conveniently
grepped from the [OUTCAR](../output-files/OUTCAR.md) file using the command
(note the two spaces between the words)

    grep " dielectric  constant" OUTCAR

The first value is the frequency (in eV) and the other two are the real
and imaginary parts of the trace of the dielectric matrix.

Furthermore, VASP writes the following data into the
[OUTCAR](../output-files/OUTCAR.md) file.

- The head of the microscopic dielectric function (without local field
  effects): $\epsilon_{\rm mic}(\omega)
  = \lim_{{\bf q}\to 0} \epsilon_{\bf 00}({\bf q},\omega)$

<!-- -->

- Inverse macroscopic dielectric tensor:$\frac{1}{ \hat {\bf q} \cdot
  \epsilon_\infty(\omega)\cdot \hat {\bf q} } = \lim_{{\bf q}\to 0}
  \left\[\epsilon^{-1}\right\]_{\bf 00}({\bf q},\omega)$

The latter potentially includes local field effects depending on the
value of
[LRPA](../incar-tags/LRPA.md).
A detailed explanation of these quantities is found in the
<a href="/wiki/images/c/c0/VASP_lecture_Dielectric.pdf" class="internal"
title="VASP lecture Dielectric.pdf">lecture notes on dielectric
properties</a>.

|  |
|----|
| **Warning:** [OUTCAR](../output-files/OUTCAR.md) contains only a subset of the complete dielectric function ( the one restricted to [NOMEGA](../incar-tags/NOMEGA.md) points). |

The complete frequency dependence ([NEDOS](../incar-tags/NEDOS.md)
frequency points) is written to
[vasprun.xml](../output-files/Vasprun.xml.md) and has following format:

     <dielectricfunction comment="HEAD OF MICROSCOPIC DIELECTRIC TENSOR (INDEPENDENT PARTICLE)">
      <imag>
       <array>
        <dimension dim="1">gridpoints</dimension>
        <field>energy</field>
        <field>xx</field>
        <field>yy</field>
        <field>zz</field>
        <field>xy</field>
        <field>yz</field>
        <field>zx</field>
        <set> 
         <r>     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
         <r>     0.4627     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
         <r>     0.9250     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
         <r>     1.3866     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
         <r>     1.8472     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
         <r>     2.3065     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
            ...   ^          ^          ^          ^          ^          ^          ^   
                  |          |          |          |          |          |          |
                energy     eps_xx     eps_yy     esp_zz     esp_xy     eps_yz     eps_xz                    

## Comparison with k-p and density perturbation theory\[<a
href="/wiki/index.php?title=GW_and_dielectric_matrix&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Comparison with k-p and density perturbation theory">edit</a> \| (./index.php.md)\]

The calculated microscopic frequency-dependent dielectric function
without local field effects is the same function obtained using
[LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.*, as well as the one obtained
from density functional perturbation routines
([LEPSILON](../incar-tags/LEPSILON.md)=*.TRUE.*). In fact, it is
guaranteed that the results are identical to those determined using a
summation over conduction band states
([LOPTICS](../incar-tags/LOPTICS.md)). Differences for
[LSPECTRAL](../incar-tags/LSPECTRAL.md)=*.FALSE.* must be negligible,
and can be solely related to a different complex shift
[CSHIFT](../incar-tags/CSHIFT.md) (defaults for
[CSHIFT](../incar-tags/CSHIFT.md) are different in both routines). Setting
[CSHIFT](../incar-tags/CSHIFT.md) manually in the
[INCAR](../input-files/INCAR.md) file will remedy this issue. If differences
prevail, it might be required to increase [NEDOS](../incar-tags/NEDOS.md).
For [LSPECTRAL](../incar-tags/LSPECTRAL.md)=*.TRUE.* differences can
arise, because

- The GW routine uses fewer frequency points and different frequency
  grids than the optics routine or

<!-- -->

- again from a different complex shift.

Increasing [NOMEGA](../incar-tags/NOMEGA.md) should remove all
discrepancies.

## Technical tips\[<a
href="/wiki/index.php?title=GW_and_dielectric_matrix&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Technical tips">edit</a> \| (./index.php.md)\]

If full GW calculations are not required, it is possible to greatly
accelerate the calculations, by calculating the response functions only
at the $\Gamma$-point. This can be achieved by setting the following
values in the [INCAR](../input-files/INCAR.md) file:

     NKREDX = number of k-points in direction of the first lattice vector
     NKREDY = number of k-points in direction of the second lattice vector
     NKREDZ = number of k-points in direction of the third lattice vector

The calculation of the QP shifts can be bypassed by setting
[ALGO](../incar-tags/ALGO.md)=*CHI*. Furthermore, if only the static
response function is required the number of frequency points should be
set to [NOMEGA](../incar-tags/NOMEGA.md)=1 and
[LSPECTRAL](../incar-tags/LSPECTRAL.md)=*.FALSE.*

------------------------------------------------------------------------


1.  [↑](#cite_ref-gajdos:prb:2006_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.73.045112"
    class="external text" rel="nofollow">M. Gajdoš, K. Hummer, G. Kresse, J.
    Furthmüller, and F. Bechstedt, Phys. Rev. B <strong>73</strong>, 045112
    (2006).</a>
2.  ↑
    <sup>[a](#cite_ref-shishkin:prb:2006_2-0)</sup>
    <sup>[b](#cite_ref-shishkin:prb:2006_2-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.74.035101"
    class="external text" rel="nofollow">M. Shishkin and G. Kresse, Phys.
    Rev. B <strong>74</strong>, 035101 (2006).</a>
3.  [↑](#cite_ref-adler:1962_3-0)
    <a href="https://doi.org/10.1103/PhysRev.126.413" class="external text"
    rel="nofollow">S. L. Adler, Phys. Rev. <strong>126</strong>, 413
    (1962)</a>
4.  [↑](#cite_ref-wiser:1963_4-0)
    <a href="https://doi.org/10.1103/PhysRev.129.62" class="external text"
    rel="nofollow">N. Wiser, Phys. Rev. <strong>129</strong>, 62 (1963)</a>



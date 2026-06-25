<!-- Source: https://vasp.at/wiki/index.php/LHYPERFINE | revid: 31025 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LHYPERFINE


LHYPERFINE = .TRUE. \|
.FALSE.  
Default: **LHYPERFINE** = .FALSE. 

Description: compute the hyperfine tensors at the atomic sites
(available as of vasp.5.3.2).

------------------------------------------------------------------------

To have VASP compute the hyperfine tensors at the atomic sites, set

    LHYPERFINE = .TRUE.

|  |
|----|
| **Mind:** Spin-polarized calclulations [ISPIN](ISPIN.md) = 2 **must** be used. |

|  |
|----|
| **Warning:** Noncollinear calculations [LNONCOLLINEAR](LNONCOLLINEAR.md) = .TRUE. are not currently implemented for LHYPERFINE. There is not a warning message for this, which will be added in future releases, see [known issues.](../misc/Known_issues.md) |

The hyperfine tensor A<sup>I</sup> describes the interaction between a
nuclear spin S<sup>I</sup> (located at site **R**<sub>I</sub>) and the
electronic spin distribution S<sup>e</sup> (in most cases associated
with a paramagnetic defect state)
<sup>[\[1\]](#cite_note-szasz:prb:2013-1)</sup>:

$E=\sum_{ij} S^e_i A^I_{ij} S^I_j$

In general it is written as the sum of an isotropic part, the so-called
Fermi contact term, and an anisotropic (dipolar) part.

The Fermi contact term is given by

$(A^I_{\mathrm{iso}})_{ij}=
\frac{2}{3}\frac{\mu_0\gamma_e\gamma_I}{\langle
S_z\rangle}\delta_{ij}\int
\delta_T(\mathbf{r})\rho_s(\mathbf{r}+\mathbf{R}_I)d\mathbf{r}$

where ρ<sub>s</sub> is the spin density, μ<sub>0</sub> is the magnetic
susceptibility of free space, γ<sub>e</sub> the electron gyromagnetic
ratio, γ<sub>I</sub> the nuclear gyromagnetic ratio of the nucleus at
**R**<sub>I</sub>, and $\langle S_z \rangle$ the expectation value of the *z*-component of the
total electronic spin.

δ<sub>T</sub>(**r**) is a smeared out δ function, as described in the
Appendix of Ref.
<sup>[\[2\]](#cite_note-bloechl:prb:2000-2)</sup>.

The dipolar contributions to the hyperfine tensor are given by

$(A^I_{\mathrm{ani}})_{ij}=\frac{\mu_0}{4\pi}\frac{\gamma_e\gamma_I}{\langle
S_z\rangle} \int
\frac{\rho_s(\mathbf{r}+\mathbf{R}_I)}{r^3}\frac{3r_ir_j-\delta_{ij}r^2}{r^2}
d\mathbf{r}$

In the equations above *r*=\|**r**\|, *r*<sub>i</sub> the i-th component
of **r**, and **r** is taken relative to the position of the nucleus
**R**<sub>I</sub>.

The nuclear gyromagnetic ratios should be specified by means of the
[NGYROMAG](NGYROMAG.md)-tag.

A guide for <a href="/wiki/Calculating_the_hyperfine_coupling_constant"
class="mw-redirect"
title="Calculating the hyperfine coupling constant">calculating the
hyperfine coupling constant</a> is available.

|  |
|----|
| **Mind:** The Zeroth Order Regular Approximation (ZORA) is used to account for the relativistic effects in the hyperfine tensor calculations. |


## Contents


- [1
  Output](#output)
- [2
  Units](#units)
- [3
  Advice](#advice)
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


## Output\[<a
href="/wiki/index.php?title=LHYPERFINE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

As usual, all output is written to the [OUTCAR](../output-files/OUTCAR.md)
file. VASP writes three blocks of data. The first is for the Fermi
contact coupling parameter:

     Fermi contact (isotropic) hyperfine coupling parameter (MHz)
     -------------------------------------------------------------
      ion      A_pw      A_1PS     A_1AE     A_1c      A_tot
     -------------------------------------------------------------
       1       ...       ...       ...       ...       ...
      ..       ...       ...       ...       ...       ...

     -------------------------------------------------------------

with an entry for each ion on the [POSCAR](../input-files/POSCAR.md) file.
A<sub>pw</sub>, A<sub>1PS</sub>, A<sub>1AE</sub>, and A<sub>1c</sub> are
the plane wave, pseudo one-center, all-electron one-center, and
one-center core contributions to the Fermi contact term, respectively.
The total Fermi contact term is given by A<sub>tot</sub>.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span
style="color: var(--vpurple);">Important:</span></strong> We have chosen
<strong>NOT</strong> to include the core contributions A<sub>1c</sub> in
A<sub>tot</sub>. These are important to add when comparing to experiment
where they can contribute a significant proportion to the hyperfine
coupling constant (up to ~50 % for <sup>13</sup>C <sup><a
href="#cite_note-szasz:prb:2013-1"><span
class="cite-bracket">[</span>1<span
class="cite-bracket">]</span></a></sup>). If you want them to be
included, you should add them by hand to A<sub>tot</sub>:
<span class="smj-container" style="opacity:.5">$A_{tot + 1c} = A_{tot} + A_{1c} = (A_{pw} + A_{PS} + A_{AE}) + A_{1c}$</span>
<p>Core electronic contributions to the Fermi contact term are
calculated in the frozen valence approximation as proposed by Yazyev
<em>et al.</em><sup><a href="#cite_note-yazyev:prb:2005-3"><span
class="cite-bracket">[</span>3<span
class="cite-bracket">]</span></a></sup>.</p></td>
</tr>
</tbody>
</table>

The dipolar contributions are listed next:

     Dipolar hyperfine coupling parameters (MHz)
     ---------------------------------------------------------------------
      ion      A_xx      A_yy      A_zz      A_xy      A_xz      A_yz
     ---------------------------------------------------------------------
       1       ...       ...       ...       ...       ...       ...
      ..       ...       ...       ...       ...       ...       ...

     ---------------------------------------------------------------------

Again one line per ion in the [POSCAR](../input-files/POSCAR.md) file.

The total hyperfine tensors are written as:

     Total hyperfine coupling parameters after diagonalization (MHz)
     (convention: |A_zz| > |A_xx| > |A_yy|)
     ----------------------------------------------------------------------
      ion      A_xx      A_yy      A_zz     asymmetry (A_yy - A_xx)/ A_zz
     ----------------------------------------------------------------------
       1       ...       ...       ...         ...
      ..       ...       ...       ...         ...

     ----------------------------------------------------------------------

i.e., the tensors have been diagonalized and rearranged.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong> The
Fermi contact term is strongly dominated by the all-electron one-center
contribution A<sub>1AE</sub>.
<p>Unfortunately, this particular term is quite sensitive to the number
and eigenenergy of the all-electron partial waves that make up the
one-center basis set, <em>i.e.</em>, to the particulars of the PAW
dataset you are using. As a result, the Fermi contact term may strongly
depend on the choice of PAW dataset.</p></td>
</tr>
</tbody>
</table>

## Units\[<a
href="/wiki/index.php?title=LHYPERFINE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Units">edit</a> \| (./index.php.md)\]

The Fermi contact term $A$ is
measured in following units

$\[A\]= \left\[\mu_0\right\]\times \left\[g_e \mu_e\right\]\times
\left\[g_j \mu_j\right\]\times \left\[|\psi(0)|^2\right\] =
\frac{T^2m^3}{J}\times \frac{J}{T}\times \frac{MHz}{T}\times
\frac{1}{m^3} = MHz$

with $\mu_0=4\pi\times 10^{-7} T^2
m^3 J^{-1}$, $g_e\mu_e=9.28476377\times
10^{-24} J T^{-1}, |\psi(0)|^2=10^{30}m^{-3}$.
[NGYROMAG](NGYROMAG.md) is given in units of MHz/T.

## Advice\[<a
href="/wiki/index.php?title=LHYPERFINE&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Advice">edit</a> \| (./index.php.md)\]

It is possible that your system relaxes to a non-magnetic solution,
causing the hyperfine splitting to disappear (i.e. all zeros). If you
think your system should be magnetic, you can enforce it using
[NUPDOWN](NUPDOWN.md), which will return the hyperfine
splitting, cf. forum post:
<a href="https://vasp.at/forum/viewtopic.php?t=16921"
class="external free"
rel="nofollow">https://vasp.at/forum/viewtopic.php?t=16921</a>.
[NUPDOWN](NUPDOWN.md) will change the
`Total magnetic moment S=` at the start of the hyperfine coupling
section in the [OUTCAR](../output-files/OUTCAR.md).

|  |
|----|
| **Important:** For some cells, the total magnetic moment S can be very small (`grep " mag=" OSZICAR`), near zero. In the above equations, the isotropic and anisotropic components of the hyperfine coupling parameter (A<sup>I</sup><sub>iso</sub> and A<sup>I</sup><sub>ani</sub>) are calculated by dividing through by S (cf. ⟨S<sub>z</sub>⟩). To avoid division by zero, S is reset to 1 when S \< 10<sup>-3</sup>. `Total magnetic moment S=` is changed, changing the hyperfine coupling constants, too. These hyperfine coupling constants are likely not meaningful. In future versions of the code, there will be a warning message stating that S has been reset and the correct total magnetic moment will be printed. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LHYPERFINE&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NGYROMAG](NGYROMAG.md)

<a href="/wiki/Calculating_the_hyperfine_coupling_constant"
class="mw-redirect"
title="Calculating the hyperfine coupling constant">Calculating the
hyperfine coupling constant</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LHYPERFINE-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LHYPERFINE&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------


1.  ↑
    <sup>[a](#cite_ref-szasz:prb:2013_1-0)</sup>
    <sup>[b](#cite_ref-szasz:prb:2013_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.88.075202"
    class="external text" rel="nofollow">K. Szasz, T. Hornos, M. Marsman,
    and A. Gali, <em>Hyperfine coupling of point defects in semiconductors
    by hybrid density functional calculations: The role of core spin
    polarization</em>, Phys. Rev. B, <strong>88</strong>, 075202 (2013).</a>
2.  [↑](#cite_ref-bloechl:prb:2000_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.62.6158" class="external text"
    rel="nofollow">P. Bloechl, <em>First-principles calculations of defects
    in oxygen-deficient silica exposed to hydrogen</em>, Phys. Rev. B,
    <strong>62</strong>, 6158 (2000).</a>
3.  [↑](#cite_ref-yazyev:prb:2005_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.71.115110"
    class="external text" rel="nofollow">O. V. Yazyev, I. Tavernelli, L.
    Helm, and U. R. Roethlisberger, <em>Core spin-polarization correction in
    pseudopotential-based electronic structure calculations</em>, Phys. Rev.
    B <strong>71</strong>, 115110 (2006).</a>



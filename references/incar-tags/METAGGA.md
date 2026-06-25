<!-- Source: https://vasp.at/wiki/index.php/METAGGA | revid: 35874 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# METAGGA


METAGGA = \[string\]  
Default: **METAGGA** = The functional specified by
[LEXCH](LEXCH.md) in the [POTCAR](../input-files/POTCAR.md) if
[GGA](GGA.md) and [XC](XC.md) are also not specified. 

Description: Selects a meta-GGA exchange-correlation functional.

------------------------------------------------------------------------

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>If you select a meta-GGA functional, make sure that you use <a
href="#POTCAR_files:_required_information"
class="mw-selflink-fragment">POTCAR files that are suited for meta-GGA
functionals</a>. However, note that this requirement does not concern
the deorbitalized meta-GGAs, i.e. those that do not depend on the
kinetic-energy density, like SCAN-L.</li>
<li>Depending on the meta-GGA that is chosen, it may be recommended to
use a <a href="/wiki/Available_PAW_potentials" class="mw-redirect"
title="Available PAW potentials">PAW potential</a> that is more accurate
than the standard/recommended one. This is particularly the case with
functionals (e.g., MBJ or the Minnesota functionals like M06-L) that are
very different from the standard ones like PBE or SCAN. The reason is
that for such <em>special</em> functionals, using a PAW potential that
includes more states in the valence or that is harder may be required to
obtain results that are closer to the results that would be obtained
with an all-electron code. That also means that it may be a good idea to
do test calculations with different PAW potentials.</li>
<li>For accuracy, it is strongly recommended to set <a
href="/wiki/LASPH" title="LASPH">LASPH</a>=.TRUE. to <a
href="#Aspherical_contributions_related_to_one-center_terms"
class="mw-selflink-fragment">account for aspherical contributions to the
PAW one-centre terms</a>.</li>
<li>Since VASP.6.4.0 it is possible to use hybrid functionals that mix
meta-GGA and Hartree-Fock exchange (<a href="/wiki/AEXX"
title="AEXX">AEXX</a>). Furthermore, two new tags, <a
href="/wiki/AMGGAX" title="AMGGAX">AMGGAX</a> and <a href="/wiki/AMGGAC"
title="AMGGAC">AMGGAC</a>, were created.</li>
<li>The <a href="/wiki/XC" title="XC">XC</a> tag, available since
VASP.6.4.3, can be used to specify any linear combination of LDA, <a
href="/wiki/GGA" title="GGA">GGA</a> and <span
class="mw-selflink selflink">METAGGA</span> exchange-correlation
functionals.</li>
<li>The results obtained with the meta-GGA functionals that depend on
the Laplacian of the density <span class="smj-container"
style="opacity:.5">$\nabla^2n$</span> (e.g.,
SCAN-L) may not be reliable for large values of the energy cutoff <a
href="/wiki/ENCUT" title="ENCUT">ENCUT</a> due to numerical instability.
According to some tests, it is not recommended to use values of <a
href="/wiki/ENCUT" title="ENCUT">ENCUT</a> above 800 eV.</li>
</ul></td>
</tr>
</tbody>
</table>


## Contents


- [1 Available
  functionals](#available-functionals)
- [2 POTCAR files:
  required information](#potcar-files-required-information)
- [3 Aspherical
  contributions related to one-center
  terms](#aspherical-contributions-related-to-one-center-terms)
- [4 Convergence
  issues](#convergence-issues)
- [5 Related tags
  and articles](#related-tags-and-articles)
- [6
  References](#references)


## Available functionals\[<a href="/wiki/index.php?title=METAGGA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Available functionals">edit</a> \| (./index.php.md)\]

This table lists the meta-GGA functionals available in VASP. There are
essentially two types of meta-GGAs, that differ in the variable on which
they depend (in addition to $n$ and
$\nabla n$): the kinetic-energy density
$\tau$ or the Laplacian of the density
$\nabla^2n$. The names of functionals which end with
"\_X" and "\_C" correspond to exchange-only and correlation functionals,
respectively. Note that the implementation of
$\tau$-dependent meta-GGA functionals is described in
[^sun:prb:11-1].

|  |  |  |
|----|:--:|----|
| METAGGA= | Variable | Description |
| LIBXC |  | Any MGGA from the external library Libxc.[^marques:cpc:2012-2][^lehtola:sx:2018-3][^tran:arxiv:2026-4][^libxc-5] It is necessary to have [Libxc \>= 5.2.0 installed](../misc/Makefile.include.md) and VASP.6.3.0 or higher compiled with [precompiler options](../misc/Precompiler_options.md). The [LIBXC1](LIBXC1.md) and [LIBXC2](LIBXC2.md) tags (where examples are shown) are also required. |
| TPSS, TPSS_X or TPSS_C<sup>(1)</sup> | $\tau$ | TPSS.[^tao:prl:2003-6] |
| RTPSS, RTPSS_X or RTPSS_C<sup>(1)</sup> | $\tau$ | revTPSS is a revised version of TPSS.[^perdew:prl:2009-7] |
| M06L, M06L_X or M06L_C<sup>(1)</sup> | $\tau$ | M06-L.[^zhao:jcp:06-8] |
| MS0, MS0_X or MS0_C<sup>(1)</sup> | $\tau$ | MS0 corresponds to $\kappa=0.29$, $c=0.28771$ and $b=1.0$.[^sun:jcp:12-9][^sun:jcp:13-10] Note that the correlation component, called vPBEc or regTPSS in the literature, is a GGA. Available since VASP.5.4.1. |
| MS1, MS1_X or MS1_C<sup>(1)</sup> | $\tau$ | MS1 corresponds to $\kappa=0.404$, $c=0.18150$ and $b=1.0$.[^sun:jcp:13-10] Note that the correlation component, called vPBEc or regTPSS in the literature, is a GGA. Available since VASP.5.4.1. |
| MS2, MS2_X or MS2_C<sup>(1)</sup> | $\tau$ | MS2 corresponds to $\kappa=0.504$, $c=0.14601$ and $b=4.0$.[^sun:jcp:13-10] Note that the correlation component, called vPBEc or regTPSS in the literature, is a GGA. Available since VASP.5.4.1. |
| SCAN, SCAN_X or SCAN_C<sup>(1)</sup> | $\tau$ | SCAN.[^sun:prl:15-11] May possibly lead to numerical instabilities. rSCAN or r$^{2}$SCAN are more stable and should give similar results. Available since VASP.5.4.4. |
| RSCAN, RSCAN_X or RSCAN_C<sup>(1)</sup> | $\tau$ | rSCAN is a regularized version of SCAN that is numerically more stable.[^bartok:jcp:19-12] |
| R2SCAN, R2SCAN_X or R2SCAN_C<sup>(1)</sup> | $\tau$ | r$^{2}$SCAN is a regularized version of SCAN that is numerically more stable.[^furness:jpcl:20-13] Available since VASP.6.2.0, or in version 5.4.4 by <a
href="https://gitlab.com/dhamil/r2scan-subroutines/-/tree/master/vasp_patch_files"
class="external text" rel="nofollow">patch 4</a>. |
| SREGTM1, SREGTM2 or SREGTM3 | $\tau$ | sregTM[^francisco_a:jcp:2023-14] versions 1, 2 or 3 of a regularized Tao-Mo functional.[^tao:prl:2016-15] Available since VASP.6.4.3. |
| TASK_X<sup>(2)</sup> | $\tau$ | TASK exchange.[^aschebrock:prr:2019-16] Available since VASP.6.5.0. |
| LAK, LAK_X or LAK_C | $\tau$ | LAK.[^lebeda:prl:2024-17] Available since VASP.6.5.0. |
| MSPBEL, MSRPBEL or MSB86BL | $\tau$ | MS-PBEl, MS-RPBEl or MS-B86bl.[^smeets:jpca:2019-18] Available since VASP.6.5.0. |
| RMSPBEL, RMSRPBEL or RMSB86BL | $\tau$ | rMS-PBEl, rMS-RPBEl or rMS-B86bl.[^cai:jpcc:2024-19] Available since VASP.6.5.0. |
| SCANL | $\nabla^2n$ | SCAN-L[^mejia-rodriguez:pra:2017-20][^mejia-rodriguez:prb:2018-21] is a deorbitalized version of SCAN. Available since VASP.6.4.0. |
| RSCANL | $\nabla^2n$ | rSCAN-L is a deorbitalized version of rSCAN. Available since VASP.6.4.0. |
| R2SCANL | $\nabla^2n$ | r$^2$SCAN-L is a deorbitalized versions of r$^2$SCAN.[^mejia-rodriguez:prb:2020-22][^kaplan:prm:2022-23] Available since VASP.6.4.0. |
| OFR2 | $\nabla^2n$ | Orbital-free regularized-restored SCAN (OFR2).[^kaplan:prm:2022-23] Available since VASP.6.4.0. |
| SREGTM2L | $\nabla^2n$ | v2-sregTM-L is a deorbitalized versions of v2-sregTM.[^francisco_b:jcp:2023-24] Available since VASP.6.4.0. |
| MBJ<sup>(3)</sup> | $\nabla^2n,\tau$ | Modified Becke-Johnson potential.[^becke:jcp:06-25][^tran:prl:09-26] The [CMBJA](CMBJA.md), [CMBJB](CMBJB.md) and [CMBJE](CMBJE.md) tags correspond to $\alpha$, $\beta$ and the power $e=1/2$ (that can be modified) in Eq. (3) of Ref. [^tran:prl:09-26], respectively. The default values are $\alpha=-0.012$, $\beta=1.023$ bohr$^{1/2}$ and $e=1/2$.[^tran:prl:09-26] |
| LMBJ<sup>(3)</sup> | $\nabla^2n,\tau$ | The local MBJ (LMBJ) potential.[^rauch:jctc:2020-27][^rauch:prb:2020-28] The [CMBJA](CMBJA.md), [CMBJB](CMBJB.md), [CMBJE](CMBJE.md), [SMBJ](SMBJ.md), and [RSMBJ](RSMBJ.md) tags correspond to $\alpha$, $\beta$, the power $e=1$ (that can be modified) of $\bar{g}$, $\sigma$ and $r_{s}^{\mathrm{th}}$ in Eqs. (5)-(7) of Ref. [^rauch:prb:2020-28], respectively. The default values are (see erratum of Ref. [^rauch:prb:2020-28]) $\alpha=0.488$, $\beta=0.5$ bohr, $e=1$, $\sigma=2$ $\AA$ ($=3.78$ bohr), and $r_{s}^{\mathrm{th}}=7$ bohr (which corresponds to $n_{\mathrm{th}}=6.96\times10^{-4}$ e/bohr$^{3}$). |

(1) The exchange-only and
correlation-only implementations are available since VASP.6.4.3.

(2) In Ref.
[^aschebrock:prr:2019-16]
TASK exchange is combined with LDA-PW92
correlation.[^perdew1992-29]
This can be done with [XC](XC.md)=TASK_X PW92_C in
[INCAR](../input-files/INCAR.md).

(3) A few points about the MBJ and LMBJ
potentials:

- These are *potential-only* methods, *i.e.*, there is no corresponding
  exchange-correlation energy $E_{xc}$.
  The used expression for $E_{xc}$ is
  LDA, which is an arbitrary choice. This means that MBJ and LMBJ
  calculations can never be self-consistent with respect to the total
  energy, and thus we cannot compute Hellmann-Feynman forces (*i.e.*, no
  ionic relaxation, etc.). Actually, these potentials aim solely at a
  description of the electronic properties, primarily the band gap, or
  magnetic moments.
- MBJ and LMBJ calculations may converge very slowly, so the number of
  maximum electronic steps ([NELM](NELM.md)) should be set
  higher than usual.
- In the presence of an extended vacuum region (e.g., surfaces) or an
  interface, the average of $|\nabla n|/n$ has no meaning. Therefore, MBJ calculations should
  be done with a fixed value of $c$, which
  can be done with the [CMBJ](CMBJ.md) tag., or alternatively
  with the LMBJ that was proposed for the purpose to be applicable to
  systems with vacuum or interfaces.

## POTCAR files: required information\[<a href="/wiki/index.php?title=METAGGA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: POTCAR files: required information">edit</a> \| (./index.php.md)\]

Calculations with a meta-GGA that depends on the kinetic-energy density
require [POTCAR](../input-files/POTCAR.md) files that include information
on the kinetic-energy density of the core electrons. Almost all recent
[POTCAR](../input-files/POTCAR.md) files do fulfill this requirement, but
there are some notable exceptions like O_GW. To check whether a
particular [POTCAR](../input-files/POTCAR.md) contains this information,
type:

    grep kinetic POTCAR

This should yield at least the following lines (for each element on the
file):

    kinetic energy-density
    mkinetic energy-density pseudized

and for PAW datasets with partial core corrections:

    kinetic energy density (partial)

|  |
|----|
| **Mind:** For [POTCAR](../input-files/POTCAR.md) files without core electrons (H, He, Li_sv, Be_sv, and \_GW variants thereof) the `grep` command given above will not return the line about pseudized kinetic energy-density, since all electrons are considered as valence. These potentials can nevertheless be used for all meta-GGA functionals. |

## Aspherical contributions related to one-center terms\[<a href="/wiki/index.php?title=METAGGA&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Aspherical contributions related to one-center terms">edit</a> \| (./index.php.md)\]

[LASPH](LASPH.md) =.TRUE. should be selected if a meta-GGA
functional is selected. If [LASPH](LASPH.md) =.FALSE., the
one-center contributions are only calculated for a spherically averaged
density and kinetic-energy density. This means that the one-center
contributions to the Kohn-Sham potential are also spherical. Since the
PAW method describes the entire space using plane waves, errors are
often small even if the non-spherical contributions to the Kohn-Sham
potential are neglected inside the PAW spheres (additive augmentation,
as opposed to the APW or FLAPW method where the plane wave contribution
only describes the interstitial region between the atoms). Anyhow, if
the density is strongly non-spherical around some atoms in your
structure, [LASPH](LASPH.md) =.TRUE. must be selected.
Non-spherical terms are particularly encountered in d- and f-elements,
dimers, molecules, and solids with strong directional bonds.

## Convergence issues\[<a href="/wiki/index.php?title=METAGGA&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Convergence issues">edit</a> \| (./index.php.md)\]

If convergence problems are encountered, it is recommended to
preconverge the calculations using the PBE functional and start the
calculation from the [WAVECAR](../input-files/WAVECAR.md) file
corresponding to the PBE ground state. Furthermore,
[ALGO](ALGO.md) = A (conjugate gradient algorithm for
orbitals) is often more stable than charge density mixing, in particular
if the system contains vacuum regions.

## Related tags and articles\[<a href="/wiki/index.php?title=METAGGA&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBXC1](LIBXC1.md), [LIBXC2](LIBXC2.md),
[GGA](GGA.md), [XC](XC.md), [CMBJ](CMBJ.md),
[CMBJA](CMBJA.md), [CMBJB](CMBJB.md),
[CMBJE](CMBJE.md), [SMBJ](SMBJ.md),
[RSMBJ](RSMBJ.md), [LASPH](LASPH.md),
[LMAXTAU](LMAXTAU.md), [LMIXTAU](LMIXTAU.md),
[LASPH](LASPH.md), [AMGGAX](AMGGAX.md),
[AMGGAC](AMGGAC.md), [Band-structure calculation using
meta-GGA
functionals](../methods/Band-structure_calculation_using_meta-GGA_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-METAGGA-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=METAGGA&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^sun:prb:11-1]: [J. Sun, M. Marsman, G. Csonka, A. Ruzsinszky, P. Hao, Y.-S. Kim, G. Kresse, and J. P. Perdew, Phys. Rev. B **84**, 035117 (2011).](https://doi.org/10.1103/PhysRevB.84.035117)
[^marques:cpc:2012-2]: [M. A. L. Marques, M. J. T. Oliveira, and T. Burnus, Comput. Phys. Commun., **183**, 2272 (2012).](https://doi.org/10.1016/j.cpc.2012.05.007)
[^lehtola:sx:2018-3]: [S. Lehtola, C. Steigemann, M. J. T. Oliveira, and M. A. L. Marques, SoftwareX, **7**, 1 (2018).](https://doi.org/10.1016/j.softx.2017.11.002)
[^tran:arxiv:2026-4]: [F. Tran, S. Lehtola, S. Pittalis, and M. A. L. Marques, *Semi-Local Exchange-Correlation Approximations in Density Functional Theory*, arXiv **2602.17333** (2026).](https://doi.org/10.48550/arXiv.2602.17333)
[^libxc-5]: [https://libxc.gitlab.io](https://libxc.gitlab.io)
[^tao:prl:2003-6]: [J. Tao, J. P. Perdew, V. N. Staroverov, and G. E. Scuseria, *Climbing the Density Functional Ladder: Nonempirical Meta–Generalized Gradient Approximation Designed for Molecules and Solids*, Phys. Rev. Lett. **91**, 146401 (2003).](https://doi.org/10.1103/PhysRevLett.91.146401)
[^perdew:prl:2009-7]: [J. P. Perdew, A. Ruzsinszky, G. I. Csonka, L. A. Constantin, and J. Sun, *Workhorse Semilocal Density Functional for Condensed Matter Physics and Quantum Chemistry*, Phys. Rev. Lett. **103**, 026403 (2009).](http://doi.org/10.1103/PhysRevLett.103.026403)
[^zhao:jcp:06-8]: [Y. Zhao and D. G. Truhlar, J. Chem. Phys. **125**, 194101 (2006).](https://doi.org/10.1063/1.2370993)
[^sun:jcp:12-9]: [J. Sun, B. Xiao, and A. Ruzsinszky, J. Chem. Phys. **137**, 051101 (2012).](https://doi.org/10.1063/1.4742312)
[^sun:jcp:13-10]: [J. Sun, R. Haunschild, B. Xiao, I. W. Bulik, G. E. Scuseria, and J. P. Perdew, J. Chem. Phys. **138**, 044113 (2013).](https://doi.org/10.1063/1.4789414)
[^sun:prl:15-11]: [J. Sun, A. Ruzsinszky, and J. P. Perdew, Phys. Rev. Lett. **115**, 036402 (2015).](https://doi.org/10.1103/PhysRevLett.115.036402)
[^bartok:jcp:19-12]: [A. P. Bartók and J. R. Yates, J. Chem. Phys. **150**, 161101 (2019).](https://doi.org/10.1063/1.5094646)
[^furness:jpcl:20-13]: [J. W. Furness, A. D. Kaplan, J. Ning, J. P. Perdew, and J. Sun, J. Phys. Chem. Lett. **11**, 8208 (2020).](https://doi.org/10.1021/acs.jpclett.0c02405)
[^francisco_a:jcp:2023-14]: [H. Francisco, A. C. cancio, and S. B. Trickey, *Reworking the Tao–Mo exchange-correlation functional. I. Reconsideration and simplification*, J. Chem. Phys. **159**, 214102 (2023).](https://doi.org/10.1063/5.0167868)
[^tao:prl:2016-15]: [J. Tao and Y. Mo, *Accurate Semilocal Density Functional for Condensed-Matter Physics and Quantum Chemistry*, Phys. Rev. Lett. **117**, 073001 (2015).](https://doi.org/10.1103/PhysRevLett.117.073001)
[^aschebrock:prr:2019-16]: [T. Aschebrock and S. Kümmel, *Ultranonlocality and accurate band gaps from a meta-generalized gradient approximation*, Phys. Rev. Res. **1**, 033082 (2019)](https://doi.org/10.1103/PhysRevResearch.1.033082)
[^lebeda:prl:2024-17]: [T. Lebeda, T. Aschebrock, and S. Kümmel, *Balancing the Contributions to the Gradient Expansion: Accurate Binding and Band Gaps with a Nonempirical Meta-GGA*, Phys. Rev. Lett. **133**, 136402 (2024).](https://doi.org/10.1103/PhysRevLett.133.136402)
[^smeets:jpca:2019-18]: [E. W. S. Smeets, J. Voos, and G.-J. Kroes, J. Phys. Chem. A **123**, 5395 (2019).](http://doi.org/10.1021/acs.jpca.9b02914)
[^cai:jpcc:2024-19]: [Y. Cai, R. Michiels, F. De Luca, E. Neyts, X. Tu, A. Bogaerts, and N. Gerrits, J. Phys. Chem. C **128**, 8611 (2024).](https://doi.org/10.1021/acs.jpcc.4c01110)
[^mejia-rodriguez:pra:2017-20]: [D. Mejía-Rodríguez and S. B. Trickey, *Deorbitalization strategies for meta-generalized-gradient-approximation exchange-correlation functionals*, Phys. Rev. A **91**, 052512 (2017).](https://doi.org/10.1103/PhysRevA.96.052512)
[^mejia-rodriguez:prb:2018-21]: [D. Mejia-Rodriguez and S. B. Trickey, *Deorbitalized meta-GGA exchange-correlation functionals in solids*, Phys. Rev. B **98**, 115161 (2018).](https://doi.org/10.1103/PhysRevB.98.115161)
[^mejia-rodriguez:prb:2020-22]: [D. Mejía-Rodríguez and S. B. Trickey, *Meta-GGA performance in solids at almost GGA cost*, Phys. Rev. B **102**, 121109(R) (2020).](https://doi.org/10.1103/PhysRevB.102.121109)
[^kaplan:prm:2022-23]: [A. D. Kaplan and J. P. Perdew, Phys. Rev. Mater. **6**, 083803 (2022).](https://doi.org/10.1103/PhysRevMaterials.6.083803)
[^francisco_b:jcp:2023-24]: [H. Francisco, A. C. cancio, and S. B. Trickey, *Reworking the Tao–Mo exchange–correlation functional. II. De-orbitalization*, J. Chem. Phys. **159**, 214103 (2023).](https://doi.org/10.1063/5.0167873)
[^becke:jcp:06-25]: [A. D. Becke and E. R. Johnson, J. Chem. Phys. **124**, 221101 (2006).](https://doi.org/10.1063/1.2213970)
[^tran:prl:09-26]: [F. Tran and P. Blaha, Phys. Rev. Lett. **102**, 226401 (2009).](https://doi.org/10.1103/PhysRevLett.102.226401)
[^rauch:jctc:2020-27]: [T. Rauch, M. A. L. Marques, and S. Botti, *Local Modified Becke-Johnson Exchange-Correlation Potential for Interfaces, Surfaces, and Two-Dimensional Materials*, J. Chem. Theory Comput. **16**, 2654 (2020).](https://doi.org/10.1021/acs.jctc.9b01147)
[^rauch:prb:2020-28]: [T. Rauch, M. A. L. Marques, and S. Botti, *Accurate electronic band gaps of two-dimensional materials from the local modified Becke-Johnson potential*, Phys. Rev. B **101**, 245163 (2020).](https://doi.org/10.1103/PhysRevB.101.245163)
[^perdew1992-29]: [J. P. Perdew and Y. Wang, Phys. Rev. B **45**, 13244 (1992).](https://doi.org/10.1103/PhysRevB.45.13244)

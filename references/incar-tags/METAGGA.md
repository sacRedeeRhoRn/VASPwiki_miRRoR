<!-- Source: https://vasp.at/wiki/index.php/METAGGA | revid: 35874 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# METAGGA
METAGGA = \[string\]  
Default: **METAGGA** = The functional specified by
[LEXCH](LEXCH.md) in the [POTCAR](../input-files/POTCAR.md) if
[GGA](GGA.md) and [XC](XC.md) are also not specified. 

Description: Selects a meta-GGA exchange-correlation functional.

------------------------------------------------------------------------

[TABLE]

## Contents

- [1 Available functionals](#Available_functionals)
- [2 POTCAR files: required
  information](#POTCAR_files:_required_information)
- [3 Aspherical contributions related to one-center
  terms](#Aspherical_contributions_related_to_one-center_terms)
- [4 Convergence issues](#Convergence_issues)
- [5 Related tags and articles](#Related_tags_and_articles)
- [6 References](#References)

## Available functionals
This table lists the meta-GGA functionals available in VASP. There are
essentially two types of meta-GGAs, that differ in the variable on which
they depend (in addition to $n$ and
$\nabla n$): the kinetic-energy density
$\tau$ or the Laplacian of the density
$\nabla^2n$. The names of functionals
which end with "\_X" and "\_C" correspond to exchange-only and
correlation functionals, respectively. Note that the implementation of
$\tau$-dependent meta-GGA functionals is
described in ^([\[1\]](#cite_note-sun:prb:11-1)).

|  |  |  |
|----|:--:|----|
| METAGGA= | Variable | Description |
| LIBXC |  | Any MGGA from the external library Libxc.^([\[2\]](#cite_note-marques:cpc:2012-2)[\[3\]](#cite_note-lehtola:sx:2018-3)[\[4\]](#cite_note-tran:arxiv:2026-4)[\[5\]](#cite_note-libxc-5)) It is necessary to have [Libxc \>= 5.2.0 installed](../misc/Makefile.include.md) and VASP.6.3.0 or higher compiled with [precompiler options](../misc/Precompiler_options.md). The [LIBXC1](LIBXC1.md) and [LIBXC2](LIBXC2.md) tags (where examples are shown) are also required. |
| TPSS, TPSS_X or TPSS_C⁽¹⁾ | $\tau$ | TPSS.^([\[6\]](#cite_note-tao:prl:2003-6)) |
| RTPSS, RTPSS_X or RTPSS_C⁽¹⁾ | $\tau$ | revTPSS is a revised version of TPSS.^([\[7\]](#cite_note-perdew:prl:2009-7)) |
| M06L, M06L_X or M06L_C⁽¹⁾ | $\tau$ | M06-L.^([\[8\]](#cite_note-zhao:jcp:06-8)) |
| MS0, MS0_X or MS0_C⁽¹⁾ | $\tau$ | MS0 corresponds to $\kappa=0.29$, $c=0.28771$ and $b=1.0$.^([\[9\]](#cite_note-sun:jcp:12-9)[\[10\]](#cite_note-sun:jcp:13-10)) Note that the correlation component, called vPBEc or regTPSS in the literature, is a GGA. Available since VASP.5.4.1. |
| MS1, MS1_X or MS1_C⁽¹⁾ | $\tau$ | MS1 corresponds to $\kappa=0.404$, $c=0.18150$ and $b=1.0$.^([\[10\]](#cite_note-sun:jcp:13-10)) Note that the correlation component, called vPBEc or regTPSS in the literature, is a GGA. Available since VASP.5.4.1. |
| MS2, MS2_X or MS2_C⁽¹⁾ | $\tau$ | MS2 corresponds to $\kappa=0.504$, $c=0.14601$ and $b=4.0$.^([\[10\]](#cite_note-sun:jcp:13-10)) Note that the correlation component, called vPBEc or regTPSS in the literature, is a GGA. Available since VASP.5.4.1. |
| SCAN, SCAN_X or SCAN_C⁽¹⁾ | $\tau$ | SCAN.^([\[11\]](#cite_note-sun:prl:15-11)) May possibly lead to numerical instabilities. rSCAN or r$^{2}$SCAN are more stable and should give similar results. Available since VASP.5.4.4. |
| RSCAN, RSCAN_X or RSCAN_C⁽¹⁾ | $\tau$ | rSCAN is a regularized version of SCAN that is numerically more stable.^([\[12\]](#cite_note-bartok:jcp:19-12)) |
| R2SCAN, R2SCAN_X or R2SCAN_C⁽¹⁾ | $\tau$ | r$^{2}$SCAN is a regularized version of SCAN that is numerically more stable.^([\[13\]](#cite_note-furness:jpcl:20-13)) Available since VASP.6.2.0, or in version 5.4.4 by [patch 4](https://gitlab.com/dhamil/r2scan-subroutines/-/tree/master/vasp_patch_files). |
| SREGTM1, SREGTM2 or SREGTM3 | $\tau$ | sregTM^([\[14\]](#cite_note-francisco_a:jcp:2023-14)) versions 1, 2 or 3 of a regularized Tao-Mo functional.^([\[15\]](#cite_note-tao:prl:2016-15)) Available since VASP.6.4.3. |
| TASK_X⁽²⁾ | $\tau$ | TASK exchange.^([\[16\]](#cite_note-aschebrock:prr:2019-16)) Available since VASP.6.5.0. |
| LAK, LAK_X or LAK_C | $\tau$ | LAK.^([\[17\]](#cite_note-lebeda:prl:2024-17)) Available since VASP.6.5.0. |
| MSPBEL, MSRPBEL or MSB86BL | $\tau$ | MS-PBEl, MS-RPBEl or MS-B86bl.^([\[18\]](#cite_note-smeets:jpca:2019-18)) Available since VASP.6.5.0. |
| RMSPBEL, RMSRPBEL or RMSB86BL | $\tau$ | rMS-PBEl, rMS-RPBEl or rMS-B86bl.^([\[19\]](#cite_note-cai:jpcc:2024-19)) Available since VASP.6.5.0. |
| SCANL | $\nabla^2n$ | SCAN-L^([\[20\]](#cite_note-mejia-rodriguez:pra:2017-20)[\[21\]](#cite_note-mejia-rodriguez:prb:2018-21)) is a deorbitalized version of SCAN. Available since VASP.6.4.0. |
| RSCANL | $\nabla^2n$ | rSCAN-L is a deorbitalized version of rSCAN. Available since VASP.6.4.0. |
| R2SCANL | $\nabla^2n$ | r$^2$SCAN-L is a deorbitalized versions of r$^2$SCAN.^([\[22\]](#cite_note-mejia-rodriguez:prb:2020-22)[\[23\]](#cite_note-kaplan:prm:2022-23)) Available since VASP.6.4.0. |
| OFR2 | $\nabla^2n$ | Orbital-free regularized-restored SCAN (OFR2).^([\[23\]](#cite_note-kaplan:prm:2022-23)) Available since VASP.6.4.0. |
| SREGTM2L | $\nabla^2n$ | v2-sregTM-L is a deorbitalized versions of v2-sregTM.^([\[24\]](#cite_note-francisco_b:jcp:2023-24)) Available since VASP.6.4.0. |
| MBJ⁽³⁾ | $\nabla^2n,\tau$ | Modified Becke-Johnson potential.^([\[25\]](#cite_note-becke:jcp:06-25)[\[26\]](#cite_note-tran:prl:09-26)) The [CMBJA](CMBJA.md), [CMBJB](CMBJB.md) and [CMBJE](CMBJE.md) tags correspond to $\alpha$, $\beta$ and the power $e=1/2$ (that can be modified) in Eq. (3) of Ref. ^([\[26\]](#cite_note-tran:prl:09-26)), respectively. The default values are $\alpha=-0.012$, $\beta=1.023$ bohr$^{1/2}$ and $e=1/2$.^([\[26\]](#cite_note-tran:prl:09-26)) |
| LMBJ⁽³⁾ | $\nabla^2n,\tau$ | The local MBJ (LMBJ) potential.^([\[27\]](#cite_note-rauch:jctc:2020-27)[\[28\]](#cite_note-rauch:prb:2020-28)) The [CMBJA](CMBJA.md), [CMBJB](CMBJB.md), [CMBJE](CMBJE.md), [SMBJ](SMBJ.md), and [RSMBJ](RSMBJ.md) tags correspond to $\alpha$, $\beta$, the power $e=1$ (that can be modified) of $\bar{g}$, $\sigma$ and $r_{s}^{\mathrm{th}}$ in Eqs. (5)-(7) of Ref. ^([\[28\]](#cite_note-rauch:prb:2020-28)), respectively. The default values are (see erratum of Ref. ^([\[28\]](#cite_note-rauch:prb:2020-28))) $\alpha=0.488$, $\beta=0.5$ bohr, $e=1$, $\sigma=2$ $\AA$ ($=3.78$ bohr), and $r_{s}^{\mathrm{th}}=7$ bohr (which corresponds to $n_{\mathrm{th}}=6.96\times10^{-4}$ e/bohr$^{3}$). |

(1) The exchange-only and correlation-only implementations are available
since VASP.6.4.3.

(2) In Ref. ^([\[16\]](#cite_note-aschebrock:prr:2019-16)) TASK exchange
is combined with LDA-PW92
correlation.^([\[29\]](#cite_note-perdew1992-29)) This can be done with
[XC](XC.md)=TASK_X PW92_C in [INCAR](../input-files/INCAR.md).

(3) A few points about the MBJ and LMBJ potentials:

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
  interface, the average of $|\nabla n|/n$ has no meaning. Therefore, MBJ calculations should be done
  with a fixed value of $c$, which can
  be done with the [CMBJ](CMBJ.md) tag., or alternatively with
  the LMBJ that was proposed for the purpose to be applicable to systems
  with vacuum or interfaces.

## POTCAR files: required information
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

## Aspherical contributions related to one-center terms
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

## Convergence issues
If convergence problems are encountered, it is recommended to
preconverge the calculations using the PBE functional and start the
calculation from the [WAVECAR](../input-files/WAVECAR.md) file
corresponding to the PBE ground state. Furthermore,
[ALGO](ALGO.md) = A (conjugate gradient algorithm for
orbitals) is often more stable than charge density mixing, in particular
if the system contains vacuum regions.

## Related tags and articles
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

## References
1.  [↑](#cite_ref-sun:prb:11_1-0) [J. Sun, M. Marsman, G. Csonka, A.
    Ruzsinszky, P. Hao, Y.-S. Kim, G. Kresse, and J. P. Perdew, Phys.
    Rev. B **84**, 035117
    (2011).](https://doi.org/10.1103/PhysRevB.84.035117)
2.  [↑](#cite_ref-marques:cpc:2012_2-0) [M. A. L. Marques, M. J. T.
    Oliveira, and T. Burnus, Comput. Phys. Commun., **183**, 2272
    (2012).](https://doi.org/10.1016/j.cpc.2012.05.007)
3.  [↑](#cite_ref-lehtola:sx:2018_3-0) [S. Lehtola, C.
    Steigemann, M. J. T. Oliveira, and M. A. L. Marques, SoftwareX,
    **7**, 1 (2018).](https://doi.org/10.1016/j.softx.2017.11.002)
4.  [↑](#cite_ref-tran:arxiv:2026_4-0) [F. Tran, S. Lehtola, S.
    Pittalis, and M. A. L. Marques, *Semi-Local Exchange-Correlation
    Approximations in Density Functional Theory*, arXiv **2602.17333**
    (2026).](https://doi.org/10.48550/arXiv.2602.17333)
5.  [↑](#cite_ref-libxc_5-0)
    [https://libxc.gitlab.io](https://libxc.gitlab.io)
6.  [↑](#cite_ref-tao:prl:2003_6-0) [J. Tao, J. P. Perdew, V. N.
    Staroverov, and G. E. Scuseria, *Climbing the Density Functional
    Ladder: Nonempirical Meta–Generalized Gradient Approximation
    Designed for Molecules and Solids*, Phys. Rev. Lett. **91**, 146401
    (2003).](https://doi.org/10.1103/PhysRevLett.91.146401)
7.  [↑](#cite_ref-perdew:prl:2009_7-0) [J. P. Perdew, A.
    Ruzsinszky, G. I. Csonka, L. A. Constantin, and J. Sun, *Workhorse
    Semilocal Density Functional for Condensed Matter Physics and
    Quantum Chemistry*, Phys. Rev. Lett. **103**, 026403
    (2009).](http://doi.org/10.1103/PhysRevLett.103.026403)
8.  [↑](#cite_ref-zhao:jcp:06_8-0) [Y. Zhao and D. G. Truhlar, J. Chem.
    Phys. **125**, 194101 (2006).](https://doi.org/10.1063/1.2370993)
9.  [↑](#cite_ref-sun:jcp:12_9-0) [J. Sun, B. Xiao, and A.
    Ruzsinszky, J. Chem. Phys. **137**, 051101
    (2012).](https://doi.org/10.1063/1.4742312)
10. ↑ ^([a](#cite_ref-sun:jcp:13_10-0))
    ^([b](#cite_ref-sun:jcp:13_10-1)) ^([c](#cite_ref-sun:jcp:13_10-2))
    [J. Sun, R. Haunschild, B. Xiao, I. W. Bulik, G. E. Scuseria,
    and J. P. Perdew, J. Chem. Phys. **138**, 044113
    (2013).](https://doi.org/10.1063/1.4789414)
11. [↑](#cite_ref-sun:prl:15_11-0) [J. Sun, A. Ruzsinszky, and J. P.
    Perdew, Phys. Rev. Lett. **115**, 036402
    (2015).](https://doi.org/10.1103/PhysRevLett.115.036402)
12. [↑](#cite_ref-bartok:jcp:19_12-0) [A. P. Bartók and J. R. Yates, J.
    Chem. Phys. **150**, 161101
    (2019).](https://doi.org/10.1063/1.5094646)
13. [↑](#cite_ref-furness:jpcl:20_13-0) [J. W. Furness, A. D. Kaplan, J.
    Ning, J. P. Perdew, and J. Sun, J. Phys. Chem. Lett. **11**, 8208
    (2020).](https://doi.org/10.1021/acs.jpclett.0c02405)
14. [↑](#cite_ref-francisco_a:jcp:2023_14-0) [H. Francisco, A. C.
    cancio, and S. B. Trickey, *Reworking the Tao–Mo
    exchange-correlation functional. I. Reconsideration and
    simplification*, J. Chem. Phys. **159**, 214102
    (2023).](https://doi.org/10.1063/5.0167868)
15. [↑](#cite_ref-tao:prl:2016_15-0) [J. Tao and Y. Mo, *Accurate
    Semilocal Density Functional for Condensed-Matter Physics and
    Quantum Chemistry*, Phys. Rev. Lett. **117**, 073001
    (2015).](https://doi.org/10.1103/PhysRevLett.117.073001)
16. ↑ ^([a](#cite_ref-aschebrock:prr:2019_16-0))
    ^([b](#cite_ref-aschebrock:prr:2019_16-1)) [T. Aschebrock and S.
    Kümmel, *Ultranonlocality and accurate band gaps from a
    meta-generalized gradient approximation*, Phys. Rev. Res. **1**,
    033082 (2019)](https://doi.org/10.1103/PhysRevResearch.1.033082)
17. [↑](#cite_ref-lebeda:prl:2024_17-0) [T. Lebeda, T. Aschebrock,
    and S. Kümmel, *Balancing the Contributions to the Gradient
    Expansion: Accurate Binding and Band Gaps with a Nonempirical
    Meta-GGA*, Phys. Rev. Lett. **133**, 136402
    (2024).](https://doi.org/10.1103/PhysRevLett.133.136402)
18. [↑](#cite_ref-smeets:jpca:2019_18-0) [E. W. S. Smeets, J. Voos, and
    G.-J. Kroes, J. Phys. Chem. A **123**, 5395
    (2019).](http://doi.org/10.1021/acs.jpca.9b02914)
19. [↑](#cite_ref-cai:jpcc:2024_19-0) [Y. Cai, R. Michiels, F. De
    Luca, E. Neyts, X. Tu, A. Bogaerts, and N. Gerrits, J. Phys. Chem. C
    **128**, 8611 (2024).](https://doi.org/10.1021/acs.jpcc.4c01110)
20. [↑](#cite_ref-mejia-rodriguez:pra:2017_20-0) [D. Mejía-Rodríguez
    and S. B. Trickey, *Deorbitalization strategies for
    meta-generalized-gradient-approximation exchange-correlation
    functionals*, Phys. Rev. A **91**, 052512
    (2017).](https://doi.org/10.1103/PhysRevA.96.052512)
21. [↑](#cite_ref-mejia-rodriguez:prb:2018_21-0) [D. Mejia-Rodriguez
    and S. B. Trickey, *Deorbitalized meta-GGA exchange-correlation
    functionals in solids*, Phys. Rev. B **98**, 115161
    (2018).](https://doi.org/10.1103/PhysRevB.98.115161)
22. [↑](#cite_ref-mejia-rodriguez:prb:2020_22-0) [D. Mejía-Rodríguez
    and S. B. Trickey, *Meta-GGA performance in solids at almost GGA
    cost*, Phys. Rev. B **102**, 121109(R)
    (2020).](https://doi.org/10.1103/PhysRevB.102.121109)
23. ↑ ^([a](#cite_ref-kaplan:prm:2022_23-0))
    ^([b](#cite_ref-kaplan:prm:2022_23-1)) [A. D. Kaplan and J. P.
    Perdew, Phys. Rev. Mater. **6**, 083803
    (2022).](https://doi.org/10.1103/PhysRevMaterials.6.083803)
24. [↑](#cite_ref-francisco_b:jcp:2023_24-0) [H. Francisco, A. C.
    cancio, and S. B. Trickey, *Reworking the Tao–Mo
    exchange–correlation functional. II. De-orbitalization*, J. Chem.
    Phys. **159**, 214103 (2023).](https://doi.org/10.1063/5.0167873)
25. [↑](#cite_ref-becke:jcp:06_25-0) [A. D. Becke and E. R. Johnson, J.
    Chem. Phys. **124**, 221101
    (2006).](https://doi.org/10.1063/1.2213970)
26. ↑ ^([a](#cite_ref-tran:prl:09_26-0))
    ^([b](#cite_ref-tran:prl:09_26-1))
    ^([c](#cite_ref-tran:prl:09_26-2)) [F. Tran and P. Blaha, Phys. Rev.
    Lett. **102**, 226401
    (2009).](https://doi.org/10.1103/PhysRevLett.102.226401)
27. [↑](#cite_ref-rauch:jctc:2020_27-0) [T. Rauch, M. A. L. Marques,
    and S. Botti, *Local Modified Becke-Johnson Exchange-Correlation
    Potential for Interfaces, Surfaces, and Two-Dimensional
    Materials*, J. Chem. Theory Comput. **16**, 2654
    (2020).](https://doi.org/10.1021/acs.jctc.9b01147)
28. ↑ ^([a](#cite_ref-rauch:prb:2020_28-0))
    ^([b](#cite_ref-rauch:prb:2020_28-1))
    ^([c](#cite_ref-rauch:prb:2020_28-2)) [T. Rauch, M. A. L. Marques,
    and S. Botti, *Accurate electronic band gaps of two-dimensional
    materials from the local modified Becke-Johnson potential*, Phys.
    Rev. B **101**, 245163
    (2020).](https://doi.org/10.1103/PhysRevB.101.245163)
29. [↑](#cite_ref-perdew1992_29-0) [J. P. Perdew and Y. Wang, Phys. Rev.
    B **45**, 13244 (1992).](https://doi.org/10.1103/PhysRevB.45.13244)

------------------------------------------------------------------------

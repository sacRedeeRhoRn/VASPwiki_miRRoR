<!-- Source: https://vasp.at/wiki/index.php/XC | revid: 34547 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# XC
XC = Combination of functionals 

|  |  |  |
|----|----|----|
| Default: **XC** | = [GGA](GGA.md) | if the [GGA](GGA.md) tag is used |
|  | = [METAGGA](METAGGA.md) | if the [METAGGA](METAGGA.md) tag is used |
|  | = The functional specified by [LEXCH](LEXCH.md) in the [POTCAR](../input-files/POTCAR.md) file | if neither [GGA](GGA.md) nor [METAGGA](METAGGA.md) is used |

Description: Specifies a combination of exchange-correlation
functionals.

------------------------------------------------------------------------

A combination of semilocal (LDA, GGA, and METAGGA) functionals can be
set with the XC tag, which provides much more flexibility in the choice
of the functional compared to the [GGA](GGA.md) and
[METAGGA](METAGGA.md) tags. The functionals that can be
combined are the functionals implemented in VASP (listed at
[GGA](GGA.md) and [METAGGA](METAGGA.md)) and the
functionals implemented in
Libxc^([\[1\]](#cite_note-marques:cpc:2012-1)[\[2\]](#cite_note-lehtola:sx:2018-2)[\[3\]](#cite_note-tran:arxiv:2026-3)[\[4\]](#cite_note-libxc-4))
(listed on the Libxc website^([\[5\]](#cite_note-libxc_list-5))). The
combination can consist of up to 100 components; for each, a
multiplication factor can be set with the [XC_C](XC_C.md) tag.

|                                                   |
|---------------------------------------------------|
| **Mind:** This tag is available since VASP.6.4.3. |

## Examples of [INCAR](../input-files/INCAR.md)
- 50% of PBE^([\[6\]](#cite_note-perdew:prl:1996-6)) and 50% of
  PBEsol^([\[7\]](#cite_note-perdew:prl:2008-7))

&nbsp;

    XC = PE PS
    XC_C = 0.5 0.5

- SCAN exchange^([\[8\]](#cite_note-sun:prl:15-8)) combined with PBE
  correlation^([\[6\]](#cite_note-perdew:prl:1996-6))

&nbsp;

    XC = SCAN_X PBE_C

- 70% of B88^([\[9\]](#cite_note-becke:pra:1988-9)) (from Libxc) and 30%
  of PBE^([\[6\]](#cite_note-perdew:prl:1996-6)) for exchange and 100%
  of LYP (from Libxc) for
  correlation^([\[10\]](#cite_note-lee:prb:1988-10))

&nbsp;

    XC = GGA_X_B88 PBE_X GGA_C_LYP
    XC_C = 0.7 0.3 1.0

- 15% of HF, 63.75% of PBE^([\[6\]](#cite_note-perdew:prl:1996-6)), and
  21.25% of B88^([\[9\]](#cite_note-becke:pra:1988-9)) (from Libxc) for
  exchange and 75% of PBE^([\[6\]](#cite_note-perdew:prl:1996-6)) and
  25% of LYP^([\[10\]](#cite_note-lee:prb:1988-10)) (from Libxc) for
  correlation

&nbsp;

    LHFCALC = .TRUE.
    XC      = PE GGA_X_B88 GGA_C_LYP
    XC_C    = 0.75 0.25 0.25
    AEXX    = 0.15
    AGGAX   = 0.85

The PBE exchange is multiplied by $0.75\times0.85=0.6375$ and the B88 exchange by
$0.25\times0.85=0.2125$.

- 15% of HF, 63.75% of PBE^([\[6\]](#cite_note-perdew:prl:1996-6)), and
  21.25% of SCAN^([\[8\]](#cite_note-sun:prl:15-8)) for exchange and 75%
  of PBE^([\[6\]](#cite_note-perdew:prl:1996-6)) and 25% of
  SCAN^([\[8\]](#cite_note-sun:prl:15-8)) for correlation

&nbsp;

    LHFCALC = .TRUE.
    XC      = PE SCAN
    XC_C    = 0.75 0.25
    AEXX    = 0.15
    AGGAX   = 0.85
    AMGGAX  = 0.85

The PBE exchange is multiplied by $0.75\times0.85=0.6375$ and the SCAN exchange by
$0.25\times0.85=0.2125$.
[AGGAX](AGGAX.md) and [AMGGAX](AMGGAX.md)
multiply the exchange part of PBE and SCAN, respectively.

## Related tags and articles
[XC_C](XC_C.md), [XCm_Pn](XCm_Pn.md),
[GGA](GGA.md), [METAGGA](METAGGA.md)
[LIBXC1](LIBXC1.md), [LIBXC2](LIBXC2.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-XC-_incategory-Examples)

## References
1.  [↑](#cite_ref-marques:cpc:2012_1-0) [M. A. L. Marques, M. J. T.
    Oliveira, and T. Burnus, Comput. Phys. Commun., **183**, 2272
    (2012).](https://doi.org/10.1016/j.cpc.2012.05.007)
2.  [↑](#cite_ref-lehtola:sx:2018_2-0) [S. Lehtola, C.
    Steigemann, M. J. T. Oliveira, and M. A. L. Marques, SoftwareX,
    **7**, 1 (2018).](https://doi.org/10.1016/j.softx.2017.11.002)
3.  [↑](#cite_ref-tran:arxiv:2026_3-0) [F. Tran, S. Lehtola, S.
    Pittalis, and M. A. L. Marques, *Semi-Local Exchange-Correlation
    Approximations in Density Functional Theory*, arXiv **2602.17333**
    (2026).](https://doi.org/10.48550/arXiv.2602.17333)
4.  [↑](#cite_ref-libxc_4-0)
    [https://libxc.gitlab.io](https://libxc.gitlab.io)
5.  [↑](#cite_ref-libxc_list_5-0)
    [https://libxc.gitlab.io/functionals/](https://libxc.gitlab.io/functionals/)
6.  ↑ ^([a](#cite_ref-perdew:prl:1996_6-0))
    ^([b](#cite_ref-perdew:prl:1996_6-1))
    ^([c](#cite_ref-perdew:prl:1996_6-2))
    ^([d](#cite_ref-perdew:prl:1996_6-3))
    ^([e](#cite_ref-perdew:prl:1996_6-4))
    ^([f](#cite_ref-perdew:prl:1996_6-5))
    ^([g](#cite_ref-perdew:prl:1996_6-6)) [J. P. Perdew, K. Burke,
    and M. Ernzerhof, Phys. Rev. Lett., **77**, 3865
    (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
7.  [↑](#cite_ref-perdew:prl:2008_7-0) [J. P. Perdew, A.
    Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A.
    Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. **100**, 136406
    (2008).](https://doi.org/10.1103/PhysRevLett.100.136406)
8.  ↑ ^([a](#cite_ref-sun:prl:15_8-0)) ^([b](#cite_ref-sun:prl:15_8-1))
    ^([c](#cite_ref-sun:prl:15_8-2)) [J. Sun, A. Ruzsinszky, and J. P.
    Perdew, Phys. Rev. Lett. **115**, 036402
    (2015).](https://doi.org/10.1103/PhysRevLett.115.036402)
9.  ↑ ^([a](#cite_ref-becke:pra:1988_9-0))
    ^([b](#cite_ref-becke:pra:1988_9-1)) [A. D. Becke,
    *Density-functional exchange-energy approximation with correct
    asymptotic behavior*, Phys. Rev. A **38**, 3098
    (1988).](https://doi.org/10.1103/PhysRevA.38.3098)
10. ↑ ^([a](#cite_ref-lee:prb:1988_10-0))
    ^([b](#cite_ref-lee:prb:1988_10-1)) [C. Lee, W. Yang, and R. G.
    Parr, *Development of the Colle-Salvetti correlation-energy formula
    into a functional of the electron density*, Phys. Rev. B **37**, 785
    (1988).](https://doi.org/10.1103/PhysRevB.37.785)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/XC | revid: 34547 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# XC


XC = Combination of
functionals 

|  |  |  |
|----|----|----|
| Default: **XC** | = [GGA](GGA.md) | if the [GGA](GGA.md) tag is used |
|  | = [METAGGA](METAGGA.md) | if the [METAGGA](METAGGA.md) tag is used |
|  | = The functional specified by [LEXCH](LEXCH.md) in the [POTCAR](../input-files/POTCAR.md) file | if neither [GGA](GGA.md) nor [METAGGA](METAGGA.md) is used |

Description: Specifies a combination of exchange-correlation
functionals.

------------------------------------------------------------------------

A combination of semilocal (LDA, GGA, and METAGGA) functionals can be
set with the XC tag, which
provides much more flexibility in the choice of the functional compared
to the [GGA](GGA.md) and [METAGGA](METAGGA.md)
tags. The functionals that can be combined are the functionals
implemented in VASP (listed at [GGA](GGA.md) and
[METAGGA](METAGGA.md)) and the functionals implemented in
Libxc<sup>[\[1\]](#cite_note-marques:cpc:2012-1)[\[2\]](#cite_note-lehtola:sx:2018-2)[\[3\]](#cite_note-tran:arxiv:2026-3)[\[4\]](#cite_note-libxc-4)</sup>
(listed on the Libxc
website<sup>[\[5\]](#cite_note-libxc_list-5)</sup>).
The combination can consist of up to 100 components; for each, a
multiplication factor can be set with the [XC_C](XC_C.md) tag.

|  |
|----|
| **Mind:** This tag is available since VASP.6.4.3. |

## Examples of [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=XC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Examples of INCAR">edit</a> \| (./index.php.md)\]

- 50% of
  PBE<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>
  and 50% of
  PBEsol<sup>[\[7\]](#cite_note-perdew:prl:2008-7)</sup>

<!-- -->

    XC = PE PS
    XC_C = 0.5 0.5

- SCAN
  exchange<sup>[\[8\]](#cite_note-sun:prl:15-8)</sup>
  combined with PBE
  correlation<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>

<!-- -->

    XC = SCAN_X PBE_C

- 70% of
  B88<sup>[\[9\]](#cite_note-becke:pra:1988-9)</sup>
  (from Libxc) and 30% of
  PBE<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>
  for exchange and 100% of LYP (from Libxc) for
  correlation<sup>[\[10\]](#cite_note-lee:prb:1988-10)</sup>

<!-- -->

    XC = GGA_X_B88 PBE_X GGA_C_LYP
    XC_C = 0.7 0.3 1.0

- 15% of HF, 63.75% of
  PBE<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>,
  and 21.25% of
  B88<sup>[\[9\]](#cite_note-becke:pra:1988-9)</sup>
  (from Libxc) for exchange and 75% of
  PBE<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>
  and 25% of
  LYP<sup>[\[10\]](#cite_note-lee:prb:1988-10)</sup>
  (from Libxc) for correlation

<!-- -->

    LHFCALC = .TRUE.
    XC      = PE GGA_X_B88 GGA_C_LYP
    XC_C    = 0.75 0.25 0.25
    AEXX    = 0.15
    AGGAX   = 0.85

The PBE exchange is multiplied by $0.75\times0.85=0.6375$ and the B88 exchange by $0.25\times0.85=0.2125$.

- 15% of HF, 63.75% of
  PBE<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>,
  and 21.25% of
  SCAN<sup>[\[8\]](#cite_note-sun:prl:15-8)</sup>
  for exchange and 75% of
  PBE<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>
  and 25% of
  SCAN<sup>[\[8\]](#cite_note-sun:prl:15-8)</sup>
  for correlation

<!-- -->

    LHFCALC = .TRUE.
    XC      = PE SCAN
    XC_C    = 0.75 0.25
    AEXX    = 0.15
    AGGAX   = 0.85
    AMGGAX  = 0.85

The PBE exchange is multiplied by $0.75\times0.85=0.6375$ and the SCAN exchange by $0.25\times0.85=0.2125$. [AGGAX](AGGAX.md) and
[AMGGAX](AMGGAX.md) multiply the exchange part of PBE and
SCAN, respectively.

## Related tags and articles\[<a href="/wiki/index.php?title=XC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[XC_C](XC_C.md), [XCm_Pn](XCm_Pn.md),
[GGA](GGA.md), [METAGGA](METAGGA.md)
[LIBXC1](LIBXC1.md), [LIBXC2](LIBXC2.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-XC-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=XC&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-marques:cpc:2012_1-0)
    <a href="https://doi.org/10.1016/j.cpc.2012.05.007"
    class="external text" rel="nofollow">M. A. L. Marques, M. J. T.
    Oliveira, and T. Burnus, Comput. Phys. Commun., <strong>183</strong>,
    2272 (2012).</a>
2.  [↑](#cite_ref-lehtola:sx:2018_2-0)
    <a href="https://doi.org/10.1016/j.softx.2017.11.002"
    class="external text" rel="nofollow">S. Lehtola, C. Steigemann, M. J. T.
    Oliveira, and M. A. L. Marques, SoftwareX, <strong>7</strong>, 1
    (2018).</a>
3.  [↑](#cite_ref-tran:arxiv:2026_3-0)
    <a href="https://doi.org/10.48550/arXiv.2602.17333"
    class="external text" rel="nofollow">F. Tran, S. Lehtola, S. Pittalis,
    and M. A. L. Marques, <em>Semi-Local Exchange-Correlation Approximations
    in Density Functional Theory</em>, arXiv <strong>2602.17333</strong>
    (2026).</a>
4.  [↑](#cite_ref-libxc_4-0)
    <a href="https://libxc.gitlab.io" class="external text"
    rel="nofollow">https://libxc.gitlab.io</a>
5.  [↑](#cite_ref-libxc_list_5-0)
    <a href="https://libxc.gitlab.io/functionals/" class="external text"
    rel="nofollow">https://libxc.gitlab.io/functionals/</a>
6.  ↑
    <sup>[a](#cite_ref-perdew:prl:1996_6-0)</sup>
    <sup>[b](#cite_ref-perdew:prl:1996_6-1)</sup>
    <sup>[c](#cite_ref-perdew:prl:1996_6-2)</sup>
    <sup>[d](#cite_ref-perdew:prl:1996_6-3)</sup>
    <sup>[e](#cite_ref-perdew:prl:1996_6-4)</sup>
    <sup>[f](#cite_ref-perdew:prl:1996_6-5)</sup>
    <sup>[g](#cite_ref-perdew:prl:1996_6-6)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.77.3865"
    class="external text" rel="nofollow">J. P. Perdew, K. Burke, and M.
    Ernzerhof, Phys. Rev. Lett., <strong>77</strong>, 3865 (1996).</a>
7.  [↑](#cite_ref-perdew:prl:2008_7-0)
    <a href="https://doi.org/10.1103/PhysRevLett.100.136406"
    class="external text" rel="nofollow">J. P. Perdew, A. Ruzsinszky, G. I.
    Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K.
    Burke, Phys. Rev. Lett. <strong>100</strong>, 136406 (2008).</a>
8.  ↑
    <sup>[a](#cite_ref-sun:prl:15_8-0)</sup>
    <sup>[b](#cite_ref-sun:prl:15_8-1)</sup>
    <sup>[c](#cite_ref-sun:prl:15_8-2)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.115.036402"
    class="external text" rel="nofollow">J. Sun, A. Ruzsinszky, and J. P.
    Perdew, Phys. Rev. Lett. <strong>115</strong>, 036402 (2015).</a>
9.  ↑
    <sup>[a](#cite_ref-becke:pra:1988_9-0)</sup>
    <sup>[b](#cite_ref-becke:pra:1988_9-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevA.38.3098" class="external text"
    rel="nofollow">A. D. Becke, <em>Density-functional exchange-energy
    approximation with correct asymptotic behavior</em>, Phys. Rev. A
    <strong>38</strong>, 3098 (1988).</a>
10. ↑
    <sup>[a](#cite_ref-lee:prb:1988_10-0)</sup>
    <sup>[b](#cite_ref-lee:prb:1988_10-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.37.785" class="external text"
    rel="nofollow">C. Lee, W. Yang, and R. G. Parr, <em>Development of the
    Colle-Salvetti correlation-energy formula into a functional of the
    electron density</em>, Phys. Rev. B <strong>37</strong>, 785 (1988).</a>


------------------------------------------------------------------------



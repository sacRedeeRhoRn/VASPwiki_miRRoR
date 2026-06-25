<!-- Source: https://vasp.at/wiki/index.php/LIBXC1_Pn | revid: 34552 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBXC1_Pn


LIBXC1_Pn = \[real\] 

Description: LIBXC1_Pn, where
$n=1, 2, \ldots$ allows to specify the values of the
parameters of the functional implemented in Libxc that is called with
[LIBXC1](LIBXC1.md).

------------------------------------------------------------------------

For many of the functionals implemented in the library of
exchange-correlation functionals
Libxc<sup>[\[1\]](#cite_note-marques:cpc:2012-1)[\[2\]](#cite_note-lehtola:sx:2018-2)[\[3\]](#cite_note-tran:arxiv:2026-3)[\[4\]](#cite_note-libxc-4)</sup>
it is possible to modify the parameters if one does not want to use the
default values. If a functional from Libxc has parameters that can be
modified, then they are listed in [OUTCAR](../output-files/OUTCAR.md) below
"Parameters of Libxc functionals:" as P$n$
($n=1, 2, \ldots$).
LIBXC1_Pn and
[LIBXC2_Pn](LIBXC2_Pn.md) are for the functionals called
with [LIBXC1](LIBXC1.md) and
[LIBXC2](LIBXC2.md), respectively.

An example is given below for the GGA PBE
functional<sup>[\[5\]](#cite_note-perdew:prl:1996-5)</sup>
where the default parameters $\mu=0.21951$
in exchange and $\beta=0.066725$ in correlation are changed to
$\mu=10/81\approx0.12345679$ and
$\beta=0.046$ to get the PBEsol
functional<sup>[\[6\]](#cite_note-perdew:prl:2008-6)</sup>
(of course, the simpler way to use PBEsol from Libxc would be to call it
directly with [LIBXC1](LIBXC1.md)=GGA_X_PBE_SOL and
[LIBXC2](LIBXC2.md)=GGA_C_PBE_SOL).

    GGA = LIBXC
    LIBXC1 = GGA_X_PBE # or 101
    LIBXC2 = GGA_C_PBE # or 130
    LIBXC1_P2 = 0.12345679
    LIBXC2_P1 = 0.046

|  |
|----|
| **Mind:** The [ALDAX](ALDAX.md), [ALDAC](ALDAC.md), [AGGAX](AGGAX.md), [AGGAC](AGGAC.md), [AMGGAX](AMGGAX.md), and [AMGGAC](AMGGAC.md) tags are ignored if the Libxc functional is an exchange-correlation functional (those with a tag that contains XC) |

For Libxc functionals that are the semilocal component of a hybrid
functional, i.e. those with a tag that starts with HYB
([LHFCALC](LHFCALC.md)=.TRUE. will be set automatically if
such a functional is selected), the following explains how it works for
the mixing and screening parameters:

- Mixing parameter:
  - It is usually one of the parameters
    LIBXC1_Pn, and can
    therefore be modified.
  - For HYB_GGA_XC_PBEH, HYB_GGA_XC_B1WC, HYB_GGA_XC_HSE03,
    HYB_GGA_XC_HSE06, HYB_GGA_XC_HSE12, and HYB_GGA_XC_HSE12S, the value
    of [AEXX](AEXX.md) (even if not specified explicitly in
    [INCAR](../input-files/INCAR.md)) will be used and automatically passed
    to the corresponding parameter in Libxc. On the other hand, if this
    corresponding parameter
    (LIBXC1_Pn) is specified
    in [INCAR](../input-files/INCAR.md), then it will be used (instead of
    [AEXX](AEXX.md)), however note that it will be only for
    the semilocal component of the hybrid functional and not for the
    exact exchange that will still use [AEXX](AEXX.md).
  - For all hybrid functionals except those listed just above,
    [AEXX](AEXX.md) will not be considered for the semilocal
    component of the hybrid functional, but only for the exact exchange
    component. Therefore, a particular choice for the mixing parameter
    has to be done by specifying both [AEXX](AEXX.md) (for the
    exact exchange) and the appropriate
    LIBXC1_Pn (for the
    semilocal component).
  - The [ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
    [AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
    [AMGGAX](AMGGAX.md), and [AMGGAC](AMGGAC.md)
    tags are ignored if the Libxc functional is an hybrid functional
    (those with a tag that starts with HYB).
- Screening parameter:
  - It is usually one of the parameters
    LIBXC1_Pn if it is a
    screened functional, and can therefore be modified.
  - For HYB_GGA_XC_HSE03, HYB_GGA_XC_HSE06, HYB_GGA_XC_HSE12, and
    HYB_GGA_XC_HSE12S, the value of
    [HFSCREEN](HFSCREEN.md) (even if not specified
    explicitly in [INCAR](../input-files/INCAR.md)) will be used and
    automatically passed to the corresponding parameter in Libxc. On the
    other hand, if this corresponding parameter
    (LIBXC1_Pn) is specified
    in [INCAR](../input-files/INCAR.md), then it will be used (instead of
    [HFSCREEN](HFSCREEN.md)), however note that it will be
    only for the semilocal component of the hybrid functional and not
    for the exact exchange that will still use
    [HFSCREEN](HFSCREEN.md).
  - For all hybrid functionals except those listed just above,
    [HFSCREEN](HFSCREEN.md) will not be considered for the
    semilocal component of the hybrid functional, but only for the exact
    exchange component. Therefore, a particular choice for the screening
    parameter has to be done by specifying both
    [HFSCREEN](HFSCREEN.md) (for the exact exchange) and
    the appropriate LIBXC1_Pn
    (for the semilocal component).

## Related tags and articles\[<a
href="/wiki/index.php?title=LIBXC1_Pn&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBXC1](LIBXC1.md), [LIBXC2](LIBXC2.md),
[LIBXC2_Pn](LIBXC2_Pn.md),
[LTBOUNDLIBXC](LTBOUNDLIBXC.md), [XC](XC.md),
[XCm_Pn](XCm_Pn.md), [GGA](GGA.md),
[METAGGA](METAGGA.md), [LHFCALC](LHFCALC.md),
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAX](AMGGAX.md),
[AMGGAC](AMGGAC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md)

  
[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBXC1_Pn-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBXC1_Pn&amp;veaction=edit&amp;section=2"
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
5.  [↑](#cite_ref-perdew:prl:1996_5-0)
    <a href="https://doi.org/10.1103/PhysRevLett.77.3865"
    class="external text" rel="nofollow">J. P. Perdew, K. Burke, and M.
    Ernzerhof, Phys. Rev. Lett., <strong>77</strong>, 3865 (1996).</a>
6.  [↑](#cite_ref-perdew:prl:2008_6-0)
    <a href="https://doi.org/10.1103/PhysRevLett.100.136406"
    class="external text" rel="nofollow">J. P. Perdew, A. Ruzsinszky, G. I.
    Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K.
    Burke, Phys. Rev. Lett. <strong>100</strong>, 136406 (2008).</a>


------------------------------------------------------------------------



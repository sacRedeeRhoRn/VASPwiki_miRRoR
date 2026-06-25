<!-- Source: https://vasp.at/wiki/index.php/LIBXC1 | revid: 34548 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBXC1


LIBXC1 = \[string\] or
\[integer\] 

Description: LIBXC1 specifies
the exchange or exchange-correlation functional from the library of
exchange-correlation functionals
Libxc<sup>[\[1\]](#cite_note-marques:cpc:2012-1)[\[2\]](#cite_note-lehtola:sx:2018-2)[\[3\]](#cite_note-tran:arxiv:2026-3)[\[4\]](#cite_note-libxc-4)</sup>.

------------------------------------------------------------------------

|  |
|----|
| **Important:** This feature is available from VASP.6.3.0 onwards that needs to be compiled with [-DUSELIBXC](../misc/Precompiler_options.md). |

LIBXC1 and
[LIBXC2](LIBXC2.md) can be set to a label (string) or number
(integer) associated with a functional listed on the Libxc
website<sup>[\[5\]](#cite_note-libxc_list-5)</sup>,
e.g., `GGA_X_PBE` and `101` for PBE exchange. The label indicates if
this is an exchange (X), correlation (C), or exchange-correlation (XC)
functional, and which family it belongs to, namely LDA (LDA or HYB_LDA),
GGA (GGA or HYB_GGA) or meta-GGA (MGGA or HYB_MGGA). If
LIBXC1 corresponds to an
exchange functional, then it can be used in combination with
[LIBXC2](LIBXC2.md) for the correlation functional.

Libxc is a separate library package that has to be
downloaded<sup>[\[4\]](#cite_note-libxc-4)</sup>
and compiled before VASP is compiled with the corresponding [precompiler
options](../misc/Precompiler_options.md) and
[links to the
libraries](../misc/Makefile.include.md).

Calculations with Laplacian-dependent meta-GGA functionals and
meta-GGA-based hybrid functionals are possible since VASP.6.4.0.

|  |
|----|
| **Important:** To get correct results with meta-GGA functionals (see discussion at [LTBOUNDLIBXC](LTBOUNDLIBXC.md)), it is necessary to use Libxc from version 5.2.0 onwards (or the master version for the latest implemented functionals) and to [compile it with the option `--disable-fhc`](../misc/Makefile.include.md). |


## Contents


- [1 How
  to](#How_to)
- [2 Examples of
  INCAR](#Examples_of_INCAR)
- [3 Related tags
  and articles](#Related_tags_and_articles)
- [4
  References](#References)


## How to\[<a href="/wiki/index.php?title=LIBXC1&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

The allowed possibilities for
LIBXC1 and
[LIBXC2](LIBXC2.md) are the following:

- Both LIBXC1  and
  [LIBXC2](LIBXC2.md) are specified and correspond to
  exchange and correlation functionals, respectively.
- Only LIBXC1  is specified
  and corresponds to an exchange or exchange-correlation functional.

|  |
|----|
| **Warning:** If LIBXC1  is an exchange-correlation functional, then [LIBXC2](LIBXC2.md)  can not be used. |

- LIBXC1  and
  [LIBXC2](LIBXC2.md) can correspond to functionals of
  different families, e.g., a meta-GGA and a GGA, respectively.

Regarding other tags in [INCAR](../input-files/INCAR.md) related to Libxc:

- One also has to specify [GGA](GGA.md) = LIBXC for LDA, GGA
  and GGA-based hybrid functionals or [METAGGA](METAGGA.md)
  = LIBXC for meta-GGA functionals and meta-GGA-based hybrid
  functionals. Note that if one of the tags
  (LIBXC1  or
  [LIBXC2](LIBXC2.md) ) corresponds to a meta-GGA, while the
  other corresponds to a GGA or LDA, then
  [METAGGA](METAGGA.md) = LIBXC (and not
  [GGA](GGA.md) = LIBXC) has to be specified.
- Many of the functionals implemented in Libxc have parameters that can
  be modified. This can be done via the tags
  [LIBXC1_Pn](LIBXC1_Pn.md) and
  [LIBXC2_Pn](LIBXC2_Pn.md), where
  $n=1, 2, \ldots$.
- The tag [LTBOUNDLIBXC](LTBOUNDLIBXC.md), which is
  .FALSE. by default, allows to enforce the lower bound on the
  kinetic-energy density ($\tau_{\sigma}^{\mathrm{W}}<\tau_{\sigma}$) with
  $\tau_{\sigma}=\max(\tau_{\sigma},\tau_{\sigma}^{\mathrm{W}})$ before $\tau_{\sigma}$ is used in a meta-GGA functional from Libxc.

For calculations with hybrid functionals
([LHFCALC](LHFCALC.md)=True), the following provides some
explanations:

- The Libxc functionals whose tag starts with HYB already include the
  mixing parameter. Therefore, for them, the
  [ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
  [AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
  [AMGGAX](AMGGAX.md), and [AMGGAC](AMGGAC.md)
  tags can not be used (more information on how to modify the mixing and
  screening parameters can be found at
  [LIBXC1_Pn](LIBXC1_Pn.md)). However, it is still
  necessary to set [AEXX](AEXX.md) at the proper value.
- If the semilocal component of the hybrid functional is constructed
  using Libxc functionals that do not contain HYB in the tag, then
  [ALDAX](ALDAX.md), [AGGAX](AGGAX.md),
  [ALDAC](ALDAC.md), and [AGGAC](AGGAC.md) will be
  used and multiply

$E_{\mathrm{x}}^{\mathrm{LDA}}=\int\epsilon_{\mathrm{x}}^{\mathrm{LDA}}(n)d^{3}r$

$\Delta
E_{\mathrm{x}}^{\mathrm{GGA}}=\int\left(\epsilon_{\mathrm{x}}^{\mathrm{GGA}}(n,\nabla
n) - \epsilon_{\mathrm{x}}^{\mathrm{LDA}}(n)\right)d^{3}r$

$E_{\mathrm{c}}^{\mathrm{LDA}}=\int\epsilon_{\mathrm{c}}^{\mathrm{LDA}}(n)d^{3}r$

$\Delta
E_{\mathrm{c}}^{\mathrm{GGA}}=\int\left(\epsilon_{\mathrm{c}}^{\mathrm{GGA}}(n,\nabla
n) - \epsilon_{\mathrm{c}}^{\mathrm{LDA}}(n)\right)d^{3}r$

respectively, where $\epsilon_{\mathrm{x}}^{\mathrm{LDA}}(n)=-\left(3/4\right)\left(3/\pi\right)^{1/3}n^{4/3}$ and $\epsilon_{\mathrm{c}}^{\mathrm{LDA}}(n)=\epsilon_{\mathrm{c}}^{\mathrm{GGA}}(n,\nabla
n=0)$.

## Examples of [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=LIBXC1&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Examples of INCAR">edit</a> \| (./index.php.md)\]

- PBE<sup>[\[6\]](#cite_note-perdew:prl:1996-6)</sup>

<!-- -->

    GGA = LIBXC
    LIBXC1 = GGA_X_PBE # or 101
    LIBXC2 = GGA_C_PBE # or 130

- SCAN<sup>[\[7\]](#cite_note-sun:prl:15-7)</sup>

<!-- -->

    METAGGA = LIBXC
    LIBXC1 = MGGA_X_SCAN # or 263
    LIBXC2 = MGGA_C_SCAN # or 267

- PBEh
  (PBE0)<sup>[\[8\]](#cite_note-adamo:jcp:1999-8)</sup>

<!-- -->

    LHFCALC = .TRUE.
    AEXX = 0.25
    GGA = LIBXC
    LIBXC1 = HYB_GGA_XC_PBEH # or 406

- SCAN0

<!-- -->

    LHFCALC = .TRUE.
    AEXX = 0.25
    METAGGA = LIBXC
    LIBXC1 = MGGA_X_SCAN # or 263
    LIBXC2 = MGGA_C_SCAN # or 267

## Related tags and articles\[<a href="/wiki/index.php?title=LIBXC1&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBXC2](LIBXC2.md),
[LIBXC1_Pn](LIBXC1_Pn.md),
[LIBXC2_Pn](LIBXC2_Pn.md),
[LTBOUNDLIBXC](LTBOUNDLIBXC.md),
[GGA](GGA.md), [METAGGA](METAGGA.md),
[LHFCALC](LHFCALC.md), [AEXX](AEXX.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md), [List
of hybrid
functionals](../methods/List_of_hybrid_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBXC1-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LIBXC1&amp;veaction=edit&amp;section=4"
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
4.  ↑ <sup>[a](#cite_ref-libxc_4-0)</sup>
    <sup>[b](#cite_ref-libxc_4-1)</sup>
    <a href="https://libxc.gitlab.io" class="external text"
    rel="nofollow">https://libxc.gitlab.io</a>
5.  [↑](#cite_ref-libxc_list_5-0)
    <a href="https://libxc.gitlab.io/functionals/" class="external text"
    rel="nofollow">https://libxc.gitlab.io/functionals/</a>
6.  [↑](#cite_ref-perdew:prl:1996_6-0)
    <a href="https://doi.org/10.1103/PhysRevLett.77.3865"
    class="external text" rel="nofollow">J. P. Perdew, K. Burke, and M.
    Ernzerhof, Phys. Rev. Lett., <strong>77</strong>, 3865 (1996).</a>
7.  [↑](#cite_ref-sun:prl:15_7-0)
    <a href="https://doi.org/10.1103/PhysRevLett.115.036402"
    class="external text" rel="nofollow">J. Sun, A. Ruzsinszky, and J. P.
    Perdew, Phys. Rev. Lett. <strong>115</strong>, 036402 (2015).</a>
8.  [↑](#cite_ref-adamo:jcp:1999_8-0)
    <a href="https://doi.org/10.1063/1.478522" class="external text"
    rel="nofollow">C. Adamo and V. Barone, Phys. Rev. Lett.,
    <strong>110</strong>, 6158 (1999).</a>


------------------------------------------------------------------------



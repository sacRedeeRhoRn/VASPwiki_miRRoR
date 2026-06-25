<!-- Source: https://vasp.at/wiki/index.php/GGA | revid: 34546 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GGA


GGA = \[string\]  
Default: **GGA** = The functional specified by
[LEXCH](LEXCH.md) in the [POTCAR](../input-files/POTCAR.md) if
[METAGGA](METAGGA.md) and [XC](XC.md) are also not
specified. 

Description: Selects a LDA or GGA
<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">exchange-correlation
functional</a>.

------------------------------------------------------------------------

|  |
|----|
| **Important:** VASP recalculates the exchange-correlation energy inside the PAW sphere and corrects the atomic energies given by the [POTCAR](../input-files/POTCAR.md) file. For this to work, the original LEXCH tag must not be modified in the [POTCAR](../input-files/POTCAR.md) file. |

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>When the OR, BO, MK, ML or CX GGA is used in combination with the
nonlocal vdW-DF functional of Dion <em>et al.</em><sup><a
href="#cite_note-dion:prl:2004-1"><span
class="cite-bracket">[</span>1<span
class="cite-bracket">]</span></a></sup>, the GGA component of the
correlation should in principle be turned off with <a href="/wiki/AGGAC"
title="AGGAC">AGGAC</a>=0 (see <a
href="/wiki/Nonlocal_vdW-DF_functionals"
title="Nonlocal vdW-DF functionals">nonlocal vdW-DF
functionals</a>).</li>
<li>The <a href="/wiki/XC" title="XC">XC</a> tag, available since
VASP.6.4.3, can be used to specify any linear combination of LDA, <span
class="mw-selflink selflink">GGA</span> and <a href="/wiki/METAGGA"
title="METAGGA">METAGGA</a> exchange-correlation functionals.</li>
</ul></td>
</tr>
</tbody>
</table>

## Available functionals\[<a href="/wiki/index.php?title=GGA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Available functionals">edit</a> \| (./index.php.md)\]

This table lists the LDA and GGA functionals available in VASP. The
names of functionals which end with "\_X" and "\_C" correspond to
exchange-only and correlation functionals, respectively.

|  |  |  |
|----|----|----|
| GGA= | Type | Description |
| LIBXC (or LI) | LDA/GGA | Any LDA or GGA from the external library Libxc.<sup>[\[2\]](#cite_note-marques:cpc:2012-2)[\[3\]](#cite_note-lehtola:sx:2018-3)[\[4\]](#cite_note-tran:arxiv:2026-4)[\[5\]](#cite_note-libxc-5)</sup> It is necessary to have [Libxc \>= 5.2.0 installed](../misc/Makefile.include.md) and VASP.6.3.0 or higher compiled with [precompiler options](../misc/Precompiler_options.md). The [LIBXC1](LIBXC1.md) and [LIBXC2](LIBXC2.md) tags (where examples are shown) are also required. |
| CA (or PZ)<sup>(1)</sup> | LDA | Slater exchange<sup>[\[6\]](#cite_note-dirac:mpcps:1930-6)</sup> + Perdew-Zunger parametrization of Ceperley-Alder Monte Carlo correlation data.<sup>[\[7\]](#cite_note-ceperley1980-7)[\[8\]](#cite_note-perdewzunger1981-8)</sup> |
| PW92<sup>(1)</sup> | LDA | Slater exchange<sup>[\[6\]](#cite_note-dirac:mpcps:1930-6)</sup> + Perdew-Wang parametrization of Ceperley-Alder Monte Carlo correlation data.<sup>[\[7\]](#cite_note-ceperley1980-7)[\[9\]](#cite_note-perdew1992-9)</sup> Available since VASP.6.5.0. |
| SL<sup>(1)</sup> | LDA | Slater exchange only.<sup>[\[6\]](#cite_note-dirac:mpcps:1930-6)</sup> Available since VASP.6.4.3. |
| CA_C (or PZ_C) | LDA | Correlation-only Perdew-Zunger parametrization of Ceperley-Alder Monte Carlo correlation data.<sup>[\[7\]](#cite_note-ceperley1980-7)[\[8\]](#cite_note-perdewzunger1981-8)</sup> Available since VASP.6.4.3. |
| PW92_C | LDA | Correlation-only Perdew-Wang parametrization of Ceperley-Alder Monte Carlo correlation data.<sup>[\[7\]](#cite_note-ceperley1980-7)[\[9\]](#cite_note-perdew1992-9)</sup> Available since VASP.6.5.0. |
| VW<sup>(1)</sup> | LDA | Slater exchange<sup>[\[6\]](#cite_note-dirac:mpcps:1930-6)</sup> + Vosko-Wilk-Nusair correlation (VWN5).<sup>[\[10\]](#cite_note-vosko1980-10)</sup> |
| HL<sup>(1)</sup> | LDA | Slater exchange<sup>[\[6\]](#cite_note-dirac:mpcps:1930-6)</sup> + Hedin-Lundqvist correlation.<sup>[\[11\]](#cite_note-hedin1971-11)</sup> |
| WI<sup>(1)</sup> | LDA | Slater exchange<sup>[\[6\]](#cite_note-dirac:mpcps:1930-6)</sup> + Wigner correlation<sup>[\[12\]](#cite_note-Wigner:tfs:1938-12)</sup> (Eq. (3.2) in Ref. <sup>[\[13\]](#cite_note-pines:ssp:1955-13)</sup>). |
| PE | GGA | Perdew-Burke-Ernzerhof (PBE).<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> |
| PBE_X | GGA | Exchange-only Perdew-Burke-Ernzerhof.<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> Available since VASP.6.4.3. |
| PBE_C | GGA | Correlation-only Perdew-Burke-Ernzerhof.<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> Available since VASP.6.4.3. |
| RE | GGA | Revised PBE from Zhang and Yang (revPBE).<sup>[\[15\]](#cite_note-zhang1998-15)</sup> |
| RP | GGA | Revised PBE from Hammer *et al*. (RPBE).<sup>[\[16\]](#cite_note-hammer1999-16)</sup> |
| PS | GGA | Revised PBE for solids (PBEsol).<sup>[\[17\]](#cite_note-perdew:prl:2008-17)</sup> |
| AM | GGA | Armiento-Mattsson (AM05).<sup>[\[18\]](#cite_note-armiento:prb:05-18)[\[19\]](#cite_note-mattson:jcp:08-19)[\[20\]](#cite_note-mattson:prb:09-20)</sup> |
| 91<sup>(1)</sup> | GGA | Perdew-Wang (PW91).<sup>[\[21\]](#cite_note-perdew:prb:1991-21)</sup> |
| B3<sup>(1)</sup> | GGA | B3LYP<sup>[\[22\]](#cite_note-stephens:jpc:1994-22)</sup> with VWN3<sup>[\[10\]](#cite_note-vosko1980-10)</sup> for LDA correlation. |
| B5<sup>(1)</sup> | GGA | B3LYP<sup>[\[22\]](#cite_note-stephens:jpc:1994-22)</sup> with VWN5<sup>[\[10\]](#cite_note-vosko1980-10)</sup> for LDA correlation. |
| OR<sup>(2)</sup> | GGA | optPBE exchange<sup>[\[23\]](#cite_note-klimes:jpcm:2010-23)</sup> + PBE correlation.<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> |
| BO<sup>(2)</sup> | GGA | optB88 exchange<sup>[\[23\]](#cite_note-klimes:jpcm:2010-23)</sup> + PBE correlation.<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> [PARAM1](PARAM1.md)=0.1833333333 for $\beta$ and [PARAM2](PARAM2.md)=0.22 for $\mu$ also need to be specified. |
| MK<sup>(2)</sup> | GGA | optB86b exchange<sup>[\[24\]](#cite_note-klimes:prb:2011-24)</sup> + PBE correlation.<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> The [PARAM1](PARAM1.md) and [PARAM2](PARAM2.md) tags can be used to modify the parameters $\mu$ and $\kappa$, respectively. |
| ML<sup>(2)</sup> | GGA | PW86R exchange<sup>[\[25\]](#cite_note-lee:prb:2010-25)</sup> + PBE correlation.<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> |
| CX<sup>(2)</sup> | GGA | CX (LV-PW86r) exchange<sup>[\[26\]](#cite_note-berland:prb:2014-26)</sup> + PBE correlation.<sup>[\[14\]](#cite_note-perdew:prl:1996-14)</sup> |
| BF | GGA | BEEF (requires VASP compiled with [-Dlibbeef](../misc/Precompiler_options.md)).<sup>[\[27\]](#cite_note-beef2012-27)</sup> |

(1) The Slater LDA exchange includes
relativistic
effects.<sup>[\[28\]](#cite_note-macdonald:jpc:1979-28)</sup>

(2) The exchange component was designed
in particular to be used as the exchange component of [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)
and with [AGGAC](AGGAC.md)=0 such that only LDA is used for
the local correlation, see [list of nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md).

## Related tags and articles\[<a href="/wiki/index.php?title=GGA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBXC1](LIBXC1.md), [LIBXC2](LIBXC2.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[METAGGA](METAGGA.md), [XC](XC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-GGA-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=GGA&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-dion:prl:2004_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.92.246401"
    class="external text" rel="nofollow">M. Dion, H. Rydberg, E. Schröder,
    D. C. Langreth, and B. I. Lundqvist, Phys. Rev. Lett.
    <strong>92</strong>, 246401 (2004).</a>
2.  [↑](#cite_ref-marques:cpc:2012_2-0)
    <a href="https://doi.org/10.1016/j.cpc.2012.05.007"
    class="external text" rel="nofollow">M. A. L. Marques, M. J. T.
    Oliveira, and T. Burnus, Comput. Phys. Commun., <strong>183</strong>,
    2272 (2012).</a>
3.  [↑](#cite_ref-lehtola:sx:2018_3-0)
    <a href="https://doi.org/10.1016/j.softx.2017.11.002"
    class="external text" rel="nofollow">S. Lehtola, C. Steigemann, M. J. T.
    Oliveira, and M. A. L. Marques, SoftwareX, <strong>7</strong>, 1
    (2018).</a>
4.  [↑](#cite_ref-tran:arxiv:2026_4-0)
    <a href="https://doi.org/10.48550/arXiv.2602.17333"
    class="external text" rel="nofollow">F. Tran, S. Lehtola, S. Pittalis,
    and M. A. L. Marques, <em>Semi-Local Exchange-Correlation Approximations
    in Density Functional Theory</em>, arXiv <strong>2602.17333</strong>
    (2026).</a>
5.  [↑](#cite_ref-libxc_5-0)
    <a href="https://libxc.gitlab.io" class="external text"
    rel="nofollow">https://libxc.gitlab.io</a>
6.  ↑
    <sup>[a](#cite_ref-dirac:mpcps:1930_6-0)</sup>
    <sup>[b](#cite_ref-dirac:mpcps:1930_6-1)</sup>
    <sup>[c](#cite_ref-dirac:mpcps:1930_6-2)</sup>
    <sup>[d](#cite_ref-dirac:mpcps:1930_6-3)</sup>
    <sup>[e](#cite_ref-dirac:mpcps:1930_6-4)</sup>
    <sup>[f](#cite_ref-dirac:mpcps:1930_6-5)</sup>
    <a href="https://doi.org/10.1017/S0305004100016108"
    class="external text" rel="nofollow">P. A. M. Dirac, Math. Proc.
    Cambridge Philos. Soc. <strong>26</strong>, 376 (1930).</a>
7.  ↑
    <sup>[a](#cite_ref-ceperley1980_7-0)</sup>
    <sup>[b](#cite_ref-ceperley1980_7-1)</sup>
    <sup>[c](#cite_ref-ceperley1980_7-2)</sup>
    <sup>[d](#cite_ref-ceperley1980_7-3)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.45.566"
    class="external text" rel="nofollow">D. M. Ceperley and B. J. Alder,
    Phys. Rev. Lett. <strong>45</strong>, 566 (1980).</a>
8.  ↑
    <sup>[a](#cite_ref-perdewzunger1981_8-0)</sup>
    <sup>[b](#cite_ref-perdewzunger1981_8-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.23.5048" class="external text"
    rel="nofollow">J. P. Perdew and A. Zunger, Phys. Rev. B
    <strong>23</strong>, 5048 (1981).</a>
9.  ↑
    <sup>[a](#cite_ref-perdew1992_9-0)</sup>
    <sup>[b](#cite_ref-perdew1992_9-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.45.13244"
    class="external text" rel="nofollow">J. P. Perdew and Y. Wang, Phys.
    Rev. B <strong>45</strong>, 13244 (1992).</a>
10. ↑
    <sup>[a](#cite_ref-vosko1980_10-0)</sup>
    <sup>[b](#cite_ref-vosko1980_10-1)</sup>
    <sup>[c](#cite_ref-vosko1980_10-2)</sup>
    <a href="https://doi.org/10.1139/p80-159" class="external text"
    rel="nofollow">S. H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys.
    <strong>58</strong>, 1200 (1980).</a>
11. [↑](#cite_ref-hedin1971_11-0)
    <a href="https://doi.org/10.1088/0022-3719/4/14/022"
    class="external text" rel="nofollow">L. Hedin and B. I. Lundqvist, J.
    Phys. C <strong>4</strong>, 2064 (1971).</a>
12. [↑](#cite_ref-Wigner:tfs:1938_12-0)
    <a href="http://doi.org/10.1039/TF9383400678" class="external text"
    rel="nofollow">E. Wigner, Trans. Faraday Soc. <strong>34</strong>, 678
    (1938).</a>
13. [↑](#cite_ref-pines:ssp:1955_13-0)
    <a href="https://doi.org/10.1016/S0081-1947(08)60681-5"
    class="external text" rel="nofollow">D. Pines, in Solid State Physics,
    edited by F. Seitz and D. Turnbull (Academic, New York, 1955), Vol. I,
    p. 367.</a>
14. ↑
    <sup>[a](#cite_ref-perdew:prl:1996_14-0)</sup>
    <sup>[b](#cite_ref-perdew:prl:1996_14-1)</sup>
    <sup>[c](#cite_ref-perdew:prl:1996_14-2)</sup>
    <sup>[d](#cite_ref-perdew:prl:1996_14-3)</sup>
    <sup>[e](#cite_ref-perdew:prl:1996_14-4)</sup>
    <sup>[f](#cite_ref-perdew:prl:1996_14-5)</sup>
    <sup>[g](#cite_ref-perdew:prl:1996_14-6)</sup>
    <sup>[h](#cite_ref-perdew:prl:1996_14-7)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.77.3865"
    class="external text" rel="nofollow">J. P. Perdew, K. Burke, and M.
    Ernzerhof, Phys. Rev. Lett., <strong>77</strong>, 3865 (1996).</a>
15. [↑](#cite_ref-zhang1998_15-0)
    <a href="https://doi.org/10.1103/PhysRevLett.80.890"
    class="external text" rel="nofollow">Y. Zhang and W. Yang, Phys. Rev.
    Lett. <strong>80</strong>, 890 (1998).</a>
16. [↑](#cite_ref-hammer1999_16-0)
    <a href="https://doi.org/10.1103/PhysRevB.59.7413" class="external text"
    rel="nofollow">B. Hammer, L. B. Hansen, and J. K. Nørskov, Phys. Rev. B
    <strong>59</strong>, 7413 (1999).</a>
17. [↑](#cite_ref-perdew:prl:2008_17-0)
    <a href="https://doi.org/10.1103/PhysRevLett.100.136406"
    class="external text" rel="nofollow">J. P. Perdew, A. Ruzsinszky, G. I.
    Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K.
    Burke, Phys. Rev. Lett. <strong>100</strong>, 136406 (2008).</a>
18. [↑](#cite_ref-armiento:prb:05_18-0)
    <a href="https://doi.org/10.1103/PhysRevB.72.085108"
    class="external text" rel="nofollow">R. Armiento and A. E. Mattsson,
    Phys. Rev. B <strong>72</strong>, 085108 (2005).</a>
19. [↑](#cite_ref-mattson:jcp:08_19-0)
    <a href="https://doi.org/10.1063/1.2835596" class="external text"
    rel="nofollow">A. E. Mattsson, R. Armiento, J. Paier, G. Kresse, J. M.
    Wills, and T. R. Mattsson, J. Chem. Phys. <strong>128</strong>, 084714
    (2008).</a>
20. [↑](#cite_ref-mattson:prb:09_20-0)
    <a href="https://doi.org/10.1103/PhysRevB.79.155101"
    class="external text" rel="nofollow">A. E. Mattsson and R. Armiento,
    Phys. Rev. B <strong>79</strong>, 155101 (2009).</a>
21. [↑](#cite_ref-perdew:prb:1991_21-0)
    <a href="https://doi.org/10.1103/PhysRevB.46.6671" class="external text"
    rel="nofollow">J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson,
    M. R. Pederson, D. J. Singh, and C. Fiolhais, Phys. Rev. B
    <strong>46</strong>, 6671 (1992).</a>
22. ↑
    <sup>[a](#cite_ref-stephens:jpc:1994_22-0)</sup>
    <sup>[b](#cite_ref-stephens:jpc:1994_22-1)</sup>
    <a href="https://doi.org/10.1021/j100096a001" class="external text"
    rel="nofollow">P. J. Stephens, F. J. Devlin, C. F. Chabalowski, and M.
    J. Frisch, J. Phys. Chem. <strong>98</strong>, 11623 (1994).</a>
23. ↑
    <sup>[a](#cite_ref-klimes:jpcm:2010_23-0)</sup>
    <sup>[b](#cite_ref-klimes:jpcm:2010_23-1)</sup>
    <a href="https://doi.org/10.1088/0953-8984/22/2/022201"
    class="external text" rel="nofollow">J. Klimeš, D. R. Bowler, and A.
    Michaelides, J. Phys.: Condens. Matter <strong>22</strong>, 022201
    (2010).</a>
24. [↑](#cite_ref-klimes:prb:2011_24-0)
    <a href="https://doi.org/10.1103/PhysRevB.83.195131"
    class="external text" rel="nofollow">J. Klimeš, D. R. Bowler, and A.
    Michaelides, Phys. Rev. B <strong>83</strong>, 195131 (2011).</a>
25. [↑](#cite_ref-lee:prb:2010_25-0)
    <a href="https://doi.org/10.1103/PhysRevB.82.081101"
    class="external text" rel="nofollow">K. Lee, E. D. Murray, L. Kong, B.
    I. Lundqvist, and D. C. Langreth, Phys. Rev. B <strong>82</strong>,
    081101(R) (2010).</a>
26. [↑](#cite_ref-berland:prb:2014_26-0)
    <a href="https://doi.org/10.1103/PhysRevB.89.035412"
    class="external text" rel="nofollow">K. Berland and P. Hyldgaard, Phys.
    Rev. B <strong>89</strong>, 035412 (2014).</a>
27. [↑](#cite_ref-beef2012_27-0)
    <a href="https://doi.org/10.1103/PhysRevB.85.235149"
    class="external text" rel="nofollow">J. Wellendorff, K. T. Lundgaard, A.
    Møgelhøj, V. Petzold, D. D. Landis, Jens K. Nørskov, T. Bligaard, and K.
    W. Jacobsen, Phys. Rev. B <strong>85</strong>, 235149 (2012).</a>
28. [↑](#cite_ref-macdonald:jpc:1979_28-0)
    <a href="https://.doi.org/10.1088/0022-3719/12/15/007"
    class="external text" rel="nofollow">A. H. MacDonald and S. H. Vosko,
    <em>A relativistic density functional formalism</em>, J. Phys. C
    <strong>12</strong>, 2977 (1979).</a>


------------------------------------------------------------------------



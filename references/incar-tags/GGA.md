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
nonlocal vdW-DF functional of Dion <em>et al.</em>[^dion:prl:2004-1], the GGA component of the
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
| LIBXC (or LI) | LDA/GGA | Any LDA or GGA from the external library Libxc.[^marques:cpc:2012-2][^lehtola:sx:2018-3][^tran:arxiv:2026-4][^libxc-5] It is necessary to have [Libxc \>= 5.2.0 installed](../misc/Makefile.include.md) and VASP.6.3.0 or higher compiled with [precompiler options](../misc/Precompiler_options.md). The [LIBXC1](LIBXC1.md) and [LIBXC2](LIBXC2.md) tags (where examples are shown) are also required. |
| CA (or PZ)<sup>(1)</sup> | LDA | Slater exchange[^dirac:mpcps:1930-6] + Perdew-Zunger parametrization of Ceperley-Alder Monte Carlo correlation data.[^ceperley1980-7][^perdewzunger1981-8] |
| PW92<sup>(1)</sup> | LDA | Slater exchange[^dirac:mpcps:1930-6] + Perdew-Wang parametrization of Ceperley-Alder Monte Carlo correlation data.[^ceperley1980-7][^perdew1992-9] Available since VASP.6.5.0. |
| SL<sup>(1)</sup> | LDA | Slater exchange only.[^dirac:mpcps:1930-6] Available since VASP.6.4.3. |
| CA_C (or PZ_C) | LDA | Correlation-only Perdew-Zunger parametrization of Ceperley-Alder Monte Carlo correlation data.[^ceperley1980-7][^perdewzunger1981-8] Available since VASP.6.4.3. |
| PW92_C | LDA | Correlation-only Perdew-Wang parametrization of Ceperley-Alder Monte Carlo correlation data.[^ceperley1980-7][^perdew1992-9] Available since VASP.6.5.0. |
| VW<sup>(1)</sup> | LDA | Slater exchange[^dirac:mpcps:1930-6] + Vosko-Wilk-Nusair correlation (VWN5).[^vosko1980-10] |
| HL<sup>(1)</sup> | LDA | Slater exchange[^dirac:mpcps:1930-6] + Hedin-Lundqvist correlation.[^hedin1971-11] |
| WI<sup>(1)</sup> | LDA | Slater exchange[^dirac:mpcps:1930-6] + Wigner correlation[^Wigner:tfs:1938-12] (Eq. (3.2) in Ref. [^pines:ssp:1955-13]). |
| PE | GGA | Perdew-Burke-Ernzerhof (PBE).[^perdew:prl:1996-14] |
| PBE_X | GGA | Exchange-only Perdew-Burke-Ernzerhof.[^perdew:prl:1996-14] Available since VASP.6.4.3. |
| PBE_C | GGA | Correlation-only Perdew-Burke-Ernzerhof.[^perdew:prl:1996-14] Available since VASP.6.4.3. |
| RE | GGA | Revised PBE from Zhang and Yang (revPBE).[^zhang1998-15] |
| RP | GGA | Revised PBE from Hammer *et al*. (RPBE).[^hammer1999-16] |
| PS | GGA | Revised PBE for solids (PBEsol).[^perdew:prl:2008-17] |
| AM | GGA | Armiento-Mattsson (AM05).[^armiento:prb:05-18][^mattson:jcp:08-19][^mattson:prb:09-20] |
| 91<sup>(1)</sup> | GGA | Perdew-Wang (PW91).[^perdew:prb:1991-21] |
| B3<sup>(1)</sup> | GGA | B3LYP[^stephens:jpc:1994-22] with VWN3[^vosko1980-10] for LDA correlation. |
| B5<sup>(1)</sup> | GGA | B3LYP[^stephens:jpc:1994-22] with VWN5[^vosko1980-10] for LDA correlation. |
| OR<sup>(2)</sup> | GGA | optPBE exchange[^klimes:jpcm:2010-23] + PBE correlation.[^perdew:prl:1996-14] |
| BO<sup>(2)</sup> | GGA | optB88 exchange[^klimes:jpcm:2010-23] + PBE correlation.[^perdew:prl:1996-14] [PARAM1](PARAM1.md)=0.1833333333 for $\beta$ and [PARAM2](PARAM2.md)=0.22 for $\mu$ also need to be specified. |
| MK<sup>(2)</sup> | GGA | optB86b exchange[^klimes:prb:2011-24] + PBE correlation.[^perdew:prl:1996-14] The [PARAM1](PARAM1.md) and [PARAM2](PARAM2.md) tags can be used to modify the parameters $\mu$ and $\kappa$, respectively. |
| ML<sup>(2)</sup> | GGA | PW86R exchange[^lee:prb:2010-25] + PBE correlation.[^perdew:prl:1996-14] |
| CX<sup>(2)</sup> | GGA | CX (LV-PW86r) exchange[^berland:prb:2014-26] + PBE correlation.[^perdew:prl:1996-14] |
| BF | GGA | BEEF (requires VASP compiled with [-Dlibbeef](../misc/Precompiler_options.md)).[^beef2012-27] |

(1) The Slater LDA exchange includes
relativistic
effects.[^macdonald:jpc:1979-28]

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
------------------------------------------------------------------------

[^dion:prl:2004-1]: [M. Dion, H. Rydberg, E. Schröder, D. C. Langreth, and B. I. Lundqvist, Phys. Rev. Lett. **92**, 246401 (2004).](https://doi.org/10.1103/PhysRevLett.92.246401)
[^marques:cpc:2012-2]: [M. A. L. Marques, M. J. T. Oliveira, and T. Burnus, Comput. Phys. Commun., **183**, 2272 (2012).](https://doi.org/10.1016/j.cpc.2012.05.007)
[^lehtola:sx:2018-3]: [S. Lehtola, C. Steigemann, M. J. T. Oliveira, and M. A. L. Marques, SoftwareX, **7**, 1 (2018).](https://doi.org/10.1016/j.softx.2017.11.002)
[^tran:arxiv:2026-4]: [F. Tran, S. Lehtola, S. Pittalis, and M. A. L. Marques, *Semi-Local Exchange-Correlation Approximations in Density Functional Theory*, arXiv **2602.17333** (2026).](https://doi.org/10.48550/arXiv.2602.17333)
[^libxc-5]: [https://libxc.gitlab.io](https://libxc.gitlab.io)
[^dirac:mpcps:1930-6]: [P. A. M. Dirac, Math. Proc. Cambridge Philos. Soc. **26**, 376 (1930).](https://doi.org/10.1017/S0305004100016108)
[^ceperley1980-7]: [D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. **45**, 566 (1980).](https://doi.org/10.1103/PhysRevLett.45.566)
[^perdewzunger1981-8]: [J. P. Perdew and A. Zunger, Phys. Rev. B **23**, 5048 (1981).](https://doi.org/10.1103/PhysRevB.23.5048)
[^perdew1992-9]: [J. P. Perdew and Y. Wang, Phys. Rev. B **45**, 13244 (1992).](https://doi.org/10.1103/PhysRevB.45.13244)
[^vosko1980-10]: [S. H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys. **58**, 1200 (1980).](https://doi.org/10.1139/p80-159)
[^hedin1971-11]: [L. Hedin and B. I. Lundqvist, J. Phys. C **4**, 2064 (1971).](https://doi.org/10.1088/0022-3719/4/14/022)
[^Wigner:tfs:1938-12]: [E. Wigner, Trans. Faraday Soc. **34**, 678 (1938).](http://doi.org/10.1039/TF9383400678)
[^pines:ssp:1955-13]: [D. Pines, in Solid State Physics, edited by F. Seitz and D. Turnbull (Academic, New York, 1955), Vol. I, p. 367.](https://doi.org/10.1016/S0081-1947(08)60681-5)
[^perdew:prl:1996-14]: [J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett., **77**, 3865 (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
[^zhang1998-15]: [Y. Zhang and W. Yang, Phys. Rev. Lett. **80**, 890 (1998).](https://doi.org/10.1103/PhysRevLett.80.890)
[^hammer1999-16]: [B. Hammer, L. B. Hansen, and J. K. Nørskov, Phys. Rev. B **59**, 7413 (1999).](https://doi.org/10.1103/PhysRevB.59.7413)
[^perdew:prl:2008-17]: [J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. **100**, 136406 (2008).](https://doi.org/10.1103/PhysRevLett.100.136406)
[^armiento:prb:05-18]: [R. Armiento and A. E. Mattsson, Phys. Rev. B **72**, 085108 (2005).](https://doi.org/10.1103/PhysRevB.72.085108)
[^mattson:jcp:08-19]: [A. E. Mattsson, R. Armiento, J. Paier, G. Kresse, J. M. Wills, and T. R. Mattsson, J. Chem. Phys. **128**, 084714 (2008).](https://doi.org/10.1063/1.2835596)
[^mattson:prb:09-20]: [A. E. Mattsson and R. Armiento, Phys. Rev. B **79**, 155101 (2009).](https://doi.org/10.1103/PhysRevB.79.155101)
[^perdew:prb:1991-21]: [J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Phys. Rev. B **46**, 6671 (1992).](https://doi.org/10.1103/PhysRevB.46.6671)
[^stephens:jpc:1994-22]: [P. J. Stephens, F. J. Devlin, C. F. Chabalowski, and M. J. Frisch, J. Phys. Chem. **98**, 11623 (1994).](https://doi.org/10.1021/j100096a001)
[^klimes:jpcm:2010-23]: [J. Klimeš, D. R. Bowler, and A. Michaelides, J. Phys.: Condens. Matter **22**, 022201 (2010).](https://doi.org/10.1088/0953-8984/22/2/022201)
[^klimes:prb:2011-24]: [J. Klimeš, D. R. Bowler, and A. Michaelides, Phys. Rev. B **83**, 195131 (2011).](https://doi.org/10.1103/PhysRevB.83.195131)
[^lee:prb:2010-25]: [K. Lee, E. D. Murray, L. Kong, B. I. Lundqvist, and D. C. Langreth, Phys. Rev. B **82**, 081101(R) (2010).](https://doi.org/10.1103/PhysRevB.82.081101)
[^berland:prb:2014-26]: [K. Berland and P. Hyldgaard, Phys. Rev. B **89**, 035412 (2014).](https://doi.org/10.1103/PhysRevB.89.035412)
[^beef2012-27]: [J. Wellendorff, K. T. Lundgaard, A. Møgelhøj, V. Petzold, D. D. Landis, Jens K. Nørskov, T. Bligaard, and K. W. Jacobsen, Phys. Rev. B **85**, 235149 (2012).](https://doi.org/10.1103/PhysRevB.85.235149)
[^macdonald:jpc:1979-28]: [A. H. MacDonald and S. H. Vosko, *A relativistic density functional formalism*, J. Phys. C **12**, 2977 (1979).](https://.doi.org/10.1088/0022-3719/12/15/007)

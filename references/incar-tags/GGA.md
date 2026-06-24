<!-- Source: https://vasp.at/wiki/index.php/GGA | revid: 34546 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GGA
GGA = \[string\]  
Default: **GGA** = The functional specified by
[LEXCH](LEXCH.md) in the [POTCAR](../input-files/POTCAR.md) if
[METAGGA](METAGGA.md) and [XC](XC.md) are also not
specified. 

Description: Selects a LDA or GGA [exchange-correlation
functional](../redirects/Exchange-correlation_functionals.md).

------------------------------------------------------------------------

|  |
|----|
| **Important:** VASP recalculates the exchange-correlation energy inside the PAW sphere and corrects the atomic energies given by the [POTCAR](../input-files/POTCAR.md) file. For this to work, the original LEXCH tag must not be modified in the [POTCAR](../input-files/POTCAR.md) file. |

[TABLE]

## Available functionals
This table lists the LDA and GGA functionals available in VASP. The
names of functionals which end with "\_X" and "\_C" correspond to
exchange-only and correlation functionals, respectively.

|  |  |  |
|----|----|----|
| GGA= | Type | Description |
| LIBXC (or LI) | LDA/GGA | Any LDA or GGA from the external library Libxc.^([\[2\]](#cite_note-marques:cpc:2012-2)[\[3\]](#cite_note-lehtola:sx:2018-3)[\[4\]](#cite_note-tran:arxiv:2026-4)[\[5\]](#cite_note-libxc-5)) It is necessary to have [Libxc \>= 5.2.0 installed](../misc/Makefile.include.md) and VASP.6.3.0 or higher compiled with [precompiler options](../misc/Precompiler_options.md). The [LIBXC1](LIBXC1.md) and [LIBXC2](LIBXC2.md) tags (where examples are shown) are also required. |
| CA (or PZ)⁽¹⁾ | LDA | Slater exchange^([\[6\]](#cite_note-dirac:mpcps:1930-6)) + Perdew-Zunger parametrization of Ceperley-Alder Monte Carlo correlation data.^([\[7\]](#cite_note-ceperley1980-7)[\[8\]](#cite_note-perdewzunger1981-8)) |
| PW92⁽¹⁾ | LDA | Slater exchange^([\[6\]](#cite_note-dirac:mpcps:1930-6)) + Perdew-Wang parametrization of Ceperley-Alder Monte Carlo correlation data.^([\[7\]](#cite_note-ceperley1980-7)[\[9\]](#cite_note-perdew1992-9)) Available since VASP.6.5.0. |
| SL⁽¹⁾ | LDA | Slater exchange only.^([\[6\]](#cite_note-dirac:mpcps:1930-6)) Available since VASP.6.4.3. |
| CA_C (or PZ_C) | LDA | Correlation-only Perdew-Zunger parametrization of Ceperley-Alder Monte Carlo correlation data.^([\[7\]](#cite_note-ceperley1980-7)[\[8\]](#cite_note-perdewzunger1981-8)) Available since VASP.6.4.3. |
| PW92_C | LDA | Correlation-only Perdew-Wang parametrization of Ceperley-Alder Monte Carlo correlation data.^([\[7\]](#cite_note-ceperley1980-7)[\[9\]](#cite_note-perdew1992-9)) Available since VASP.6.5.0. |
| VW⁽¹⁾ | LDA | Slater exchange^([\[6\]](#cite_note-dirac:mpcps:1930-6)) + Vosko-Wilk-Nusair correlation (VWN5).^([\[10\]](#cite_note-vosko1980-10)) |
| HL⁽¹⁾ | LDA | Slater exchange^([\[6\]](#cite_note-dirac:mpcps:1930-6)) + Hedin-Lundqvist correlation.^([\[11\]](#cite_note-hedin1971-11)) |
| WI⁽¹⁾ | LDA | Slater exchange^([\[6\]](#cite_note-dirac:mpcps:1930-6)) + Wigner correlation^([\[12\]](#cite_note-Wigner:tfs:1938-12)) (Eq. (3.2) in Ref. ^([\[13\]](#cite_note-pines:ssp:1955-13))). |
| PE | GGA | Perdew-Burke-Ernzerhof (PBE).^([\[14\]](#cite_note-perdew:prl:1996-14)) |
| PBE_X | GGA | Exchange-only Perdew-Burke-Ernzerhof.^([\[14\]](#cite_note-perdew:prl:1996-14)) Available since VASP.6.4.3. |
| PBE_C | GGA | Correlation-only Perdew-Burke-Ernzerhof.^([\[14\]](#cite_note-perdew:prl:1996-14)) Available since VASP.6.4.3. |
| RE | GGA | Revised PBE from Zhang and Yang (revPBE).^([\[15\]](#cite_note-zhang1998-15)) |
| RP | GGA | Revised PBE from Hammer *et al*. (RPBE).^([\[16\]](#cite_note-hammer1999-16)) |
| PS | GGA | Revised PBE for solids (PBEsol).^([\[17\]](#cite_note-perdew:prl:2008-17)) |
| AM | GGA | Armiento-Mattsson (AM05).^([\[18\]](#cite_note-armiento:prb:05-18)[\[19\]](#cite_note-mattson:jcp:08-19)[\[20\]](#cite_note-mattson:prb:09-20)) |
| 91⁽¹⁾ | GGA | Perdew-Wang (PW91).^([\[21\]](#cite_note-perdew:prb:1991-21)) |
| B3⁽¹⁾ | GGA | B3LYP^([\[22\]](#cite_note-stephens:jpc:1994-22)) with VWN3^([\[10\]](#cite_note-vosko1980-10)) for LDA correlation. |
| B5⁽¹⁾ | GGA | B3LYP^([\[22\]](#cite_note-stephens:jpc:1994-22)) with VWN5^([\[10\]](#cite_note-vosko1980-10)) for LDA correlation. |
| OR⁽²⁾ | GGA | optPBE exchange^([\[23\]](#cite_note-klimes:jpcm:2010-23)) + PBE correlation.^([\[14\]](#cite_note-perdew:prl:1996-14)) |
| BO⁽²⁾ | GGA | optB88 exchange^([\[23\]](#cite_note-klimes:jpcm:2010-23)) + PBE correlation.^([\[14\]](#cite_note-perdew:prl:1996-14)) [PARAM1](PARAM1.md)=0.1833333333 for $\beta$ and [PARAM2](PARAM2.md)=0.22 for $\mu$ also need to be specified. |
| MK⁽²⁾ | GGA | optB86b exchange^([\[24\]](#cite_note-klimes:prb:2011-24)) + PBE correlation.^([\[14\]](#cite_note-perdew:prl:1996-14)) The [PARAM1](PARAM1.md) and [PARAM2](PARAM2.md) tags can be used to modify the parameters $\mu$ and $\kappa$, respectively. |
| ML⁽²⁾ | GGA | PW86R exchange^([\[25\]](#cite_note-lee:prb:2010-25)) + PBE correlation.^([\[14\]](#cite_note-perdew:prl:1996-14)) |
| CX⁽²⁾ | GGA | CX (LV-PW86r) exchange^([\[26\]](#cite_note-berland:prb:2014-26)) + PBE correlation.^([\[14\]](#cite_note-perdew:prl:1996-14)) |
| BF | GGA | BEEF (requires VASP compiled with [-Dlibbeef](../misc/Precompiler_options.md)).^([\[27\]](#cite_note-beef2012-27)) |

(1) The Slater LDA exchange includes relativistic
effects.^([\[28\]](#cite_note-macdonald:jpc:1979-28))

(2) The exchange component was designed in particular to be used as the
exchange component of [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)
and with [AGGAC](AGGAC.md)=0 such that only LDA is used for
the local correlation, see [list of nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md).

## Related tags and articles
[LIBXC1](LIBXC1.md), [LIBXC2](LIBXC2.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[METAGGA](METAGGA.md), [XC](XC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-GGA-_incategory-Examples)

## References
1.  [↑](#cite_ref-dion:prl:2004_1-0) [M. Dion, H. Rydberg, E.
    Schröder, D. C. Langreth, and B. I. Lundqvist, Phys. Rev. Lett.
    **92**, 246401
    (2004).](https://doi.org/10.1103/PhysRevLett.92.246401)
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
6.  ↑ ^([a](#cite_ref-dirac:mpcps:1930_6-0))
    ^([b](#cite_ref-dirac:mpcps:1930_6-1))
    ^([c](#cite_ref-dirac:mpcps:1930_6-2))
    ^([d](#cite_ref-dirac:mpcps:1930_6-3))
    ^([e](#cite_ref-dirac:mpcps:1930_6-4))
    ^([f](#cite_ref-dirac:mpcps:1930_6-5)) [P. A. M. Dirac, Math. Proc.
    Cambridge Philos. Soc. **26**, 376
    (1930).](https://doi.org/10.1017/S0305004100016108)
7.  ↑ ^([a](#cite_ref-ceperley1980_7-0))
    ^([b](#cite_ref-ceperley1980_7-1))
    ^([c](#cite_ref-ceperley1980_7-2))
    ^([d](#cite_ref-ceperley1980_7-3)) [D. M. Ceperley and B. J. Alder,
    Phys. Rev. Lett. **45**, 566
    (1980).](https://doi.org/10.1103/PhysRevLett.45.566)
8.  ↑ ^([a](#cite_ref-perdewzunger1981_8-0))
    ^([b](#cite_ref-perdewzunger1981_8-1)) [J. P. Perdew and A. Zunger,
    Phys. Rev. B **23**, 5048
    (1981).](https://doi.org/10.1103/PhysRevB.23.5048)
9.  ↑ ^([a](#cite_ref-perdew1992_9-0)) ^([b](#cite_ref-perdew1992_9-1))
    [J. P. Perdew and Y. Wang, Phys. Rev. B **45**, 13244
    (1992).](https://doi.org/10.1103/PhysRevB.45.13244)
10. ↑ ^([a](#cite_ref-vosko1980_10-0)) ^([b](#cite_ref-vosko1980_10-1))
    ^([c](#cite_ref-vosko1980_10-2)) [S. H. Vosko, L. Wilk, and M.
    Nusair, Can. J. Phys. **58**, 1200
    (1980).](https://doi.org/10.1139/p80-159)
11. [↑](#cite_ref-hedin1971_11-0) [L. Hedin and B. I. Lundqvist, J.
    Phys. C **4**, 2064
    (1971).](https://doi.org/10.1088/0022-3719/4/14/022)
12. [↑](#cite_ref-Wigner:tfs:1938_12-0) [E. Wigner, Trans. Faraday Soc.
    **34**, 678 (1938).](http://doi.org/10.1039/TF9383400678)
13. [↑](#cite_ref-pines:ssp:1955_13-0) [D. Pines, in Solid State
    Physics, edited by F. Seitz and D. Turnbull (Academic, New York,
    1955), Vol. I, p.
    367.](https://doi.org/10.1016/S0081-1947(08)60681-5)
14. ↑ ^([a](#cite_ref-perdew:prl:1996_14-0))
    ^([b](#cite_ref-perdew:prl:1996_14-1))
    ^([c](#cite_ref-perdew:prl:1996_14-2))
    ^([d](#cite_ref-perdew:prl:1996_14-3))
    ^([e](#cite_ref-perdew:prl:1996_14-4))
    ^([f](#cite_ref-perdew:prl:1996_14-5))
    ^([g](#cite_ref-perdew:prl:1996_14-6))
    ^([h](#cite_ref-perdew:prl:1996_14-7)) [J. P. Perdew, K. Burke,
    and M. Ernzerhof, Phys. Rev. Lett., **77**, 3865
    (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
15. [↑](#cite_ref-zhang1998_15-0) [Y. Zhang and W. Yang, Phys. Rev.
    Lett. **80**, 890
    (1998).](https://doi.org/10.1103/PhysRevLett.80.890)
16. [↑](#cite_ref-hammer1999_16-0) [B. Hammer, L. B. Hansen, and J. K.
    Nørskov, Phys. Rev. B **59**, 7413
    (1999).](https://doi.org/10.1103/PhysRevB.59.7413)
17. [↑](#cite_ref-perdew:prl:2008_17-0) [J. P. Perdew, A.
    Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A.
    Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. **100**, 136406
    (2008).](https://doi.org/10.1103/PhysRevLett.100.136406)
18. [↑](#cite_ref-armiento:prb:05_18-0) [R. Armiento and A. E. Mattsson,
    Phys. Rev. B **72**, 085108
    (2005).](https://doi.org/10.1103/PhysRevB.72.085108)
19. [↑](#cite_ref-mattson:jcp:08_19-0) [A. E. Mattsson, R. Armiento, J.
    Paier, G. Kresse, J. M. Wills, and T. R. Mattsson, J. Chem. Phys.
    **128**, 084714 (2008).](https://doi.org/10.1063/1.2835596)
20. [↑](#cite_ref-mattson:prb:09_20-0) [A. E. Mattsson and R. Armiento,
    Phys. Rev. B **79**, 155101
    (2009).](https://doi.org/10.1103/PhysRevB.79.155101)
21. [↑](#cite_ref-perdew:prb:1991_21-0) [J. P. Perdew, J. A.
    Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh,
    and C. Fiolhais, Phys. Rev. B **46**, 6671
    (1992).](https://doi.org/10.1103/PhysRevB.46.6671)
22. ↑ ^([a](#cite_ref-stephens:jpc:1994_22-0))
    ^([b](#cite_ref-stephens:jpc:1994_22-1)) [P. J. Stephens, F. J.
    Devlin, C. F. Chabalowski, and M. J. Frisch, J. Phys. Chem. **98**,
    11623 (1994).](https://doi.org/10.1021/j100096a001)
23. ↑ ^([a](#cite_ref-klimes:jpcm:2010_23-0))
    ^([b](#cite_ref-klimes:jpcm:2010_23-1)) [J. Klimeš, D. R. Bowler,
    and A. Michaelides, J. Phys.: Condens. Matter **22**, 022201
    (2010).](https://doi.org/10.1088/0953-8984/22/2/022201)
24. [↑](#cite_ref-klimes:prb:2011_24-0) [J. Klimeš, D. R. Bowler, and A.
    Michaelides, Phys. Rev. B **83**, 195131
    (2011).](https://doi.org/10.1103/PhysRevB.83.195131)
25. [↑](#cite_ref-lee:prb:2010_25-0) [K. Lee, E. D. Murray, L.
    Kong, B. I. Lundqvist, and D. C. Langreth, Phys. Rev. B **82**,
    081101(R) (2010).](https://doi.org/10.1103/PhysRevB.82.081101)
26. [↑](#cite_ref-berland:prb:2014_26-0) [K. Berland and P. Hyldgaard,
    Phys. Rev. B **89**, 035412
    (2014).](https://doi.org/10.1103/PhysRevB.89.035412)
27. [↑](#cite_ref-beef2012_27-0) [J. Wellendorff, K. T. Lundgaard, A.
    Møgelhøj, V. Petzold, D. D. Landis, Jens K. Nørskov, T. Bligaard,
    and K. W. Jacobsen, Phys. Rev. B **85**, 235149
    (2012).](https://doi.org/10.1103/PhysRevB.85.235149)
28. [↑](#cite_ref-macdonald:jpc:1979_28-0) [A. H. MacDonald and S. H.
    Vosko, *A relativistic density functional formalism*, J. Phys. C
    **12**, 2977 (1979).](https://.doi.org/10.1088/0022-3719/12/15/007)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/List_of_hybrid_functionals | revid: 34119 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# List of hybrid functionals
A certain number of [unscreened and screened hybrid
functionals](Hybrid_functionals-_formalism.md)
are available in VASP, and furthermore if VASP is
[compiled](../misc/Makefile.include.md)
with the library of exchange-correlation functionals Libxc, then most of
the existing hybrid functionals can be
used^([\[1\]](#cite_note-libxc_list-1)). Examples of
[INCAR](../input-files/INCAR.md) files are shown below. Since VASP.6.4.0 it
is possible to use hybrid functionals that mix meta-GGA and Hartree-Fock
exchange. Note that it is in general recommended to use the PBE
[POTCAR](../input-files/POTCAR.md) files for hybrid functionals.

## Contents

- [1 Range-separated hybrid
  functionals](#Range-separated_hybrid_functionals)
- [2 Unscreened hybrid functionals](#Unscreened_hybrid_functionals)
- [3 Related tags and articles](#Related_tags_and_articles)
- [4 References](#References)

### Range-separated hybrid functionals
- HSE06^([\[2\]](#cite_note-krukau:jcp:06-2))

&nbsp;

    LHFCALC = .TRUE.
    GGA = PE
    HFSCREEN = 0.2

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

- HSE03^([\[3\]](#cite_note-heyd:jcp:03-3)[\[4\]](#cite_note-heyd:jcp:04-4)[\[5\]](#cite_note-heyd:jcp:06-5))

&nbsp;

    LHFCALC = .TRUE.
    GGA = PE
    HFSCREEN = 0.3

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

- HSEsol^([\[6\]](#cite_note-schimka:jcp:11-6))

&nbsp;

    LHFCALC = .TRUE.
    GGA = PS
    HFSCREEN = 0.2

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

- Dielectric-dependent hybrid (DDH)
  RS-DDH^([\[7\]](#cite_note-skone:prb:2016-7))

&nbsp;

    LHFCALC = .TRUE.
    LMODELHF = .TRUE.
    AEXX = $\varepsilon_{\infty}^{-1}$
    BEXX = 0.25
    HFSCREEN = $\mu$
    GGA = PE

where $\varepsilon_{\infty}^{-1}$ is
the inverse dielectric constant and $\mu$ is the range-separation parameter. See a detailed description
of the DDH functionals in the documentation for the
[LMODELHF](../incar-tags/LMODELHF.md) tag as well as
[here](Hybrid_functionals-_formalism.md)_with_different_mixings "Hybrid functionals: formalism").

- Dielectric-dependent hybrid (DDH)
  DD-RSH-CAM,^([\[8\]](#cite_note-chen2018nonempirical-8))DSH^([\[9\]](#cite_note-cui2018doubly-9))

&nbsp;

    LHFCALC = .TRUE.
    LMODELHF = .TRUE.
    AEXX = $\varepsilon_{\infty}^{-1}$
    HFSCREEN = $\mu$
    GGA = PE

with the default value [BEXX](../incar-tags/BEXX.md)=1 and where
$\varepsilon_{\infty}^{-1}$ is the
inverse dielectric constant and $\mu$ is
the range-separation parameter. See a detailed description of the DDH
functionals in the documentation for the
[LMODELHF](../incar-tags/LMODELHF.md) tag as well as
[here](Hybrid_functionals-_formalism.md)_with_different_mixings "Hybrid functionals: formalism").

- RSHXLDA^([\[10\]](#cite_note-gerber:jcp:2007-10))

&nbsp;

    LHFCALC = .TRUE.
    LRHFCALC = .TRUE.
    GGA = CA (or PZ)
    HFSCREEN = 0.75 # Optimal value for solids
    ALDAC = 1.0     # Necessary since correlation is by default not included when AEXX=1

with the default value [AEXX](../incar-tags/AEXX.md)=1.

- RSHXPBE^([\[11\]](#cite_note-gerber:cpl:2005-11))

&nbsp;

    LHFCALC = .TRUE.
    LRHFCALC = .TRUE.
    GGA = PE
    HFSCREEN = 0.91 # Optimal value for the enthalpies of formation of molecules
    ALDAC = 1.0     # Necessary since correlation is by default not included when AEXX=1
    AGGAC = 1.0     # Necessary since correlation is by default not included when AEXX=1

with the default values [AEXX](../incar-tags/AEXX.md)=1.

- sX-LDA^([\[12\]](#cite_note-bylander:prb:90-12))

&nbsp;

    LHFCALC = .TRUE.
    LTHOMAS = .TRUE.
    GGA = CA (or PZ)
    HFSCREEN = $k_{\rm TF}$
    ALDAC = 1.0     # Necessary since correlation is by default not included when AEXX=1
    AGGAC = 1.0     # Necessary since correlation is by default not included when AEXX=1

with the default value [AEXX](../incar-tags/AEXX.md)=1 and where
$k_{\rm TF}$ is the Thomas-Fermi
screening. More details can be found at
[LTHOMAS](../incar-tags/LTHOMAS.md) as well as
[here](Hybrid_functionals-_formalism.md) "Hybrid functionals: formalism").

### Unscreened hybrid functionals
- PBE0
  (PBEh)^([\[13\]](#cite_note-perdew:jcp:1996-13)[\[14\]](#cite_note-ernzerhof:jcp:99-14)[\[15\]](#cite_note-adamo:jcp:1999-15))

&nbsp;

    LHFCALC = .TRUE.
    GGA = PE

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

- B3LYP^([\[16\]](#cite_note-stephens:jpc:94-16)) with VWN3 (or VWN5)
  for LDA correlation

&nbsp;

    LHFCALC = .TRUE. 
    GGA     = B3 (or B5)
    AEXX    = 0.2
    AGGAX   = 0.72 
    AGGAC   = 0.81 
    ALDAC   = 0.19

with the default value
[ALDAX](../incar-tags/ALDAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.8.

- B3PW91^([\[17\]](#cite_note-becke:jcp:93-17)) (using Libxc, see the
  tag [LIBXC1](../incar-tags/LIBXC1.md))

&nbsp;

    LHFCALC = .TRUE.
    GGA = LIBXC
    LIBXC1 = HYB_GGA_XC_B3PW91 # or 401
    AEXX = 0.2

- B1-WC^([\[18\]](#cite_note-bilc:prb:08-18)) (using Libxc, see the tag
  [LIBXC1](../incar-tags/LIBXC1.md))

&nbsp;

    LHFCALC = .TRUE.
    GGA = LIBXC
    LIBXC1 = HYB_GGA_XC_B1WC # or 412
    AEXX = 0.16

- SCAN0

&nbsp;

    LHFCALC = .TRUE.
    METAGGA = SCAN

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AMGGAX](../incar-tags/AMGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75, and
[AMGGAC](../incar-tags/AMGGAC.md)=1.

- Hartree-Fock (no correlation)

&nbsp;

    LHFCALC = .TRUE. 
    AEXX    = 1

with the default values
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0,
[ALDAC](../incar-tags/ALDAC.md)=0, and [AGGAC](../incar-tags/AGGAC.md)=0.

  

[TABLE]

## Related tags and articles
[GGA](../incar-tags/GGA.md), [METAGGA](../incar-tags/METAGGA.md),
[LIBXC1](../incar-tags/LIBXC1.md), [LIBXC2](../incar-tags/LIBXC2.md),
[AEXX](../incar-tags/AEXX.md), [BEXX](../incar-tags/BEXX.md),
[ALDAX](../incar-tags/ALDAX.md), [ALDAC](../incar-tags/ALDAC.md),
[AGGAX](../incar-tags/AGGAX.md), [AGGAC](../incar-tags/AGGAC.md),
[AMGGAX](../incar-tags/AMGGAX.md), [AMGGAC](../incar-tags/AMGGAC.md),
[LHFCALC](../incar-tags/LHFCALC.md),
[HFSCREEN](../incar-tags/HFSCREEN.md),
[LMODELHF](../incar-tags/LMODELHF.md),
[LTHOMAS](../incar-tags/LTHOMAS.md),
[LRHFCALC](../incar-tags/LRHFCALC.md), [Hybrid functionals:
formalism](Hybrid_functionals-_formalism.md)

## References
1.  [↑](#cite_ref-libxc_list_1-0)
    [https://libxc.gitlab.io/functionals/](https://libxc.gitlab.io/functionals/)
2.  [↑](#cite_ref-krukau:jcp:06_2-0) [A. V. Krukau , O. A. Vydrov, A. F.
    Izmaylov, and G. E. Scuseria, J. Chem. Phys. **125**, 224106
    (2006).](https://doi.org/10.1063/1.2404663)
3.  [↑](#cite_ref-heyd:jcp:03_3-0) [J. Heyd, G. E. Scuseria, and M.
    Ernzerhof, J. Chem. Phys. **118**, 8207
    (2003).](https://doi.org/10.1063/1.1564060)
4.  [↑](#cite_ref-heyd:jcp:04_4-0) [J. Heyd and G. E. Scuseria, J. Chem.
    Phys. **121**, 1187 (2004).](https://doi.org/10.1063/1.1760074)
5.  [↑](#cite_ref-heyd:jcp:06_5-0) [J. Heyd, G. E. Scuseria, and M.
    Ernzerhof, J. Chem. Phys. **124**, 219906
    (2006).](https://doi.org/10.1063/1.2204597)
6.  [↑](#cite_ref-schimka:jcp:11_6-0) [L. Schimka, J. Harl, and G.
    Kresse, J. Chem. Phys. **134**, 024116
    (2011).](https://doi.org/10.1063/1.3524336)
7.  [↑](#cite_ref-skone:prb:2016_7-0) [J. H. Skone, M. Govoni, and G.
    Galli, *Nonempirical range-separated hybrid functionals for solids
    and molecules*, Phys. Rev. B **93**, 235106
    (2016).](http://doi.org/10.1103/PhysRevB.93.235106)
8.  [↑](#cite_ref-chen2018nonempirical_8-0) [W. Chen, G. Miceli, G.M.
    Rignanese, and A. Pasquarello, *Nonempirical dielectric-dependent
    hybrid functional with range separation for semiconductors and
    insulators*, Phys. Rev. Mater. **2**, 073803
    (2018).](https://doi.org/10.1103/PhysRevMaterials.2.073803)
9.  [↑](#cite_ref-cui2018doubly_9-0) [Z.H. Cui, Y.C. Wang, M.Y.
    Zhang, X. Xu, and H. Jiang, *Doubly Screened Hybrid Functional: An
    Accurate First-Principles Approach for Both Narrow- and Wide-Gap
    Semiconductors* J. Phys. Chem. Lett., **9**, 2338-2345
    (2018).](https://doi.org/10.1021/acs.jpclett.8b00919)
10. [↑](#cite_ref-gerber:jcp:2007_10-0) [I. C. Gerber, J. G. Ángyán, M.
    Marsman, and G. Kresse, *Range separated hybrid density functional
    with long-range Hartree-Fock exchange applied to solids*, J. Chem.
    Phys. **127**, 054101 (2007).](http://doi.org/10.1063/1.2759209)
11. [↑](#cite_ref-gerber:cpl:2005_11-0) [I. C. Gerber and J. G. Ángyán,
    *Hybrid functional with separated range*, Chem. Phys. Lett. **415**,
    100 (2005).](http://doi.org/10.1016/j.cplett.2005.08.060)
12. [↑](#cite_ref-bylander:prb:90_12-0) [D. M. Bylander and L. Kleinman,
    Phys. Rev. B **41**, 7868
    (1990).](https://doi.org/10.1103/PhysRevB.41.7868)
13. [↑](#cite_ref-perdew:jcp:1996_13-0) [J. P. Perdew, M. Ernzerhof,
    and K. Burke, J. Chem. Phys. **105**, 9982
    (1996).](https://doi.org/10.1063/1.472933)
14. [↑](#cite_ref-ernzerhof:jcp:99_14-0) [M. Ernzerhof and G. E.
    Scuseria, J. Chem. Phys. **110**, 5029
    (1999).](https://doi.org/10.1063/1.478401)
15. [↑](#cite_ref-adamo:jcp:1999_15-0) [C. Adamo and V. Barone, Phys.
    Rev. Lett., **110**, 6158 (1999).](https://doi.org/10.1063/1.478522)
16. [↑](#cite_ref-stephens:jpc:94_16-0) [P. J. Stephens, F. J.
    Devlin, C. F. Chabalowski, and M. J. Frisch, J. Phys. Chem. **98**,
    11623 (1994).](https://doi.org/10.1021/j100096a001)
17. [↑](#cite_ref-becke:jcp:93_17-0) [A. D. Becke, J. Chem. Phys.
    **98**, 5648 (1993).](https://doi.org/10.1063/1.464913)
18. [↑](#cite_ref-bilc:prb:08_18-0) [D. I. Bilc, R. Orlando, R. Shaltaf,
    G.-M. Rignanese, J. Iniguez, and P. Ghosez, Phys. Rev. B **77**,
    165107 (2008).](https://doi.org/10.1103/PhysRevB.77.165107)

------------------------------------------------------------------------

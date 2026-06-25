<!-- Source: https://vasp.at/wiki/index.php/List_of_hybrid_functionals | revid: 34119 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# List of hybrid functionals


A certain number of [unscreened and screened hybrid
functionals](Hybrid_functionals-_formalism.md)
are available in VASP, and furthermore if VASP is
[compiled](../misc/Makefile.include.md)
with the library of exchange-correlation functionals Libxc, then most of
the existing hybrid functionals can be
used<sup>[\[1\]](#cite_note-libxc_list-1)</sup>.
Examples of [INCAR](../input-files/INCAR.md) files are shown below. Since
VASP.6.4.0 it is possible to use hybrid functionals that mix meta-GGA
and Hartree-Fock exchange. Note that it is in general recommended to use
the PBE [POTCAR](../input-files/POTCAR.md) files for hybrid functionals.


## Contents


- [1
  Range-separated hybrid
  functionals](#range-separated-hybrid-functionals)
- [2 Unscreened
  hybrid functionals](#unscreened-hybrid-functionals)
- [3 Related tags
  and articles](#related-tags-and-articles)
- [4
  References](#references)


### Range-separated hybrid functionals\[<a
href="/wiki/index.php?title=List_of_hybrid_functionals&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Range-separated hybrid functionals">edit</a> \| (./index.php.md)\]

 

- HSE06<sup>[\[2\]](#cite_note-krukau:jcp:06-2)</sup>

<!-- -->

    LHFCALC = .TRUE.
    GGA = PE
    HFSCREEN = 0.2

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

 

- HSE03<sup>[\[3\]](#cite_note-heyd:jcp:03-3)[\[4\]](#cite_note-heyd:jcp:04-4)[\[5\]](#cite_note-heyd:jcp:06-5)</sup>

<!-- -->

    LHFCALC = .TRUE.
    GGA = PE
    HFSCREEN = 0.3

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

 

- HSEsol<sup>[\[6\]](#cite_note-schimka:jcp:11-6)</sup>

<!-- -->

    LHFCALC = .TRUE.
    GGA = PS
    HFSCREEN = 0.2

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

 

- Dielectric-dependent hybrid (DDH)
  RS-DDH<sup>[\[7\]](#cite_note-skone:prb:2016-7)</sup>

<!-- -->

    LHFCALC = .TRUE.
    LMODELHF = .TRUE.
    AEXX = $\varepsilon_{\infty}^{-1}$
    BEXX = 0.25
    HFSCREEN = $\mu$
    GGA = PE

where $\varepsilon_{\infty}^{-1}$ is the inverse dielectric constant and
$\mu$ is the range-separation parameter. See a detailed
description of the DDH functionals in the documentation for the
[LMODELHF](../incar-tags/LMODELHF.md) tag as well as
[here](Hybrid_functionals-_formalism.md)_with_different_mixings "Hybrid functionals: formalism").

 

- Dielectric-dependent hybrid (DDH)
  DD-RSH-CAM,<sup>[\[8\]](#cite_note-chen2018nonempirical-8)</sup>DSH<sup>[\[9\]](#cite_note-cui2018doubly-9)</sup>

<!-- -->

    LHFCALC = .TRUE.
    LMODELHF = .TRUE.
    AEXX = $\varepsilon_{\infty}^{-1}$
    HFSCREEN = $\mu$
    GGA = PE

with the default value [BEXX](../incar-tags/BEXX.md)=1 and where
$\varepsilon_{\infty}^{-1}$ is the inverse dielectric
constant and $\mu$ is the
range-separation parameter. See a detailed description of the DDH
functionals in the documentation for the
[LMODELHF](../incar-tags/LMODELHF.md) tag as well as
[here](Hybrid_functionals-_formalism.md)_with_different_mixings "Hybrid functionals: formalism").

 

- RSHXLDA<sup>[\[10\]](#cite_note-gerber:jcp:2007-10)</sup>

<!-- -->

    LHFCALC = .TRUE.
    LRHFCALC = .TRUE.
    GGA = CA (or PZ)
    HFSCREEN = 0.75 # Optimal value for solids
    ALDAC = 1.0     # Necessary since correlation is by default not included when AEXX=1

with the default value [AEXX](../incar-tags/AEXX.md)=1.

 

- RSHXPBE<sup>[\[11\]](#cite_note-gerber:cpl:2005-11)</sup>

<!-- -->

    LHFCALC = .TRUE.
    LRHFCALC = .TRUE.
    GGA = PE
    HFSCREEN = 0.91 # Optimal value for the enthalpies of formation of molecules
    ALDAC = 1.0     # Necessary since correlation is by default not included when AEXX=1
    AGGAC = 1.0     # Necessary since correlation is by default not included when AEXX=1

with the default values [AEXX](../incar-tags/AEXX.md)=1.

 

- sX-LDA<sup>[\[12\]](#cite_note-bylander:prb:90-12)</sup>

<!-- -->

    LHFCALC = .TRUE.
    LTHOMAS = .TRUE.
    GGA = CA (or PZ)
    HFSCREEN = $k_{\rm TF}$
    ALDAC = 1.0     # Necessary since correlation is by default not included when AEXX=1
    AGGAC = 1.0     # Necessary since correlation is by default not included when AEXX=1

with the default value [AEXX](../incar-tags/AEXX.md)=1 and where
$k_{\rm TF}$ is the Thomas-Fermi screening. More
details can be found at [LTHOMAS](../incar-tags/LTHOMAS.md) as well as
[here](Hybrid_functionals-_formalism.md) "Hybrid functionals: formalism").

### Unscreened hybrid functionals\[<a
href="/wiki/index.php?title=List_of_hybrid_functionals&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Unscreened hybrid functionals">edit</a> \| (./index.php.md)\]

 

- PBE0
  (PBEh)<sup>[\[13\]](#cite_note-perdew:jcp:1996-13)[\[14\]](#cite_note-ernzerhof:jcp:99-14)[\[15\]](#cite_note-adamo:jcp:1999-15)</sup>

<!-- -->

    LHFCALC = .TRUE.
    GGA = PE

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75,
[AGGAC](../incar-tags/AGGAC.md)=1, and [ALDAC](../incar-tags/ALDAC.md)=1.

 

- B3LYP<sup>[\[16\]](#cite_note-stephens:jpc:94-16)</sup>
  with VWN3 (or VWN5) for LDA correlation

<!-- -->

    LHFCALC = .TRUE. 
    GGA     = B3 (or B5)
    AEXX    = 0.2
    AGGAX   = 0.72 
    AGGAC   = 0.81 
    ALDAC   = 0.19

with the default value
[ALDAX](../incar-tags/ALDAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.8.

 

- B3PW91<sup>[\[17\]](#cite_note-becke:jcp:93-17)</sup>
  (using Libxc, see the tag [LIBXC1](../incar-tags/LIBXC1.md))

<!-- -->

    LHFCALC = .TRUE.
    GGA = LIBXC
    LIBXC1 = HYB_GGA_XC_B3PW91 # or 401
    AEXX = 0.2

 

- B1-WC<sup>[\[18\]](#cite_note-bilc:prb:08-18)</sup>
  (using Libxc, see the tag [LIBXC1](../incar-tags/LIBXC1.md))

<!-- -->

    LHFCALC = .TRUE.
    GGA = LIBXC
    LIBXC1 = HYB_GGA_XC_B1WC # or 412
    AEXX = 0.16

 

- SCAN0

<!-- -->

    LHFCALC = .TRUE.
    METAGGA = SCAN

with the default values [AEXX](../incar-tags/AEXX.md)=0.25,
[AMGGAX](../incar-tags/AMGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0.75, and
[AMGGAC](../incar-tags/AMGGAC.md)=1.

 

- Hartree-Fock (no correlation)

<!-- -->

    LHFCALC = .TRUE. 
    AEXX    = 1

with the default values
[AGGAX](../incar-tags/AGGAX.md)=1-[AEXX](../incar-tags/AEXX.md)=0,
[ALDAC](../incar-tags/ALDAC.md)=0, and [AGGAC](../incar-tags/AGGAC.md)=0.

  

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
Note the default values when <a href="/wiki/LHFCALC"
title="LHFCALC">LHFCALC</a>=.TRUE.:
<ul>
<li><a href="/wiki/ALDAX" title="ALDAX">ALDAX</a>, <a href="/wiki/AGGAX"
title="AGGAX">AGGAX</a> and <a href="/wiki/AMGGAX"
title="AMGGAX">AMGGAX</a> are set to 1-<a href="/wiki/AEXX"
title="AEXX">AEXX</a>.</li>
<li><a href="/wiki/ALDAC" title="ALDAC">ALDAC</a>, <a href="/wiki/AGGAC"
title="AGGAC">AGGAC</a> and <a href="/wiki/AMGGAC"
title="AMGGAC">AMGGAC</a> are set to 0 if <a href="/wiki/AEXX"
title="AEXX">AEXX</a>=1 or to 1 if <a href="/wiki/AEXX"
title="AEXX">AEXX</a><span class="smj-container"
style="opacity:.5">$\neq$</span>1.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=List_of_hybrid_functionals&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

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

## References\[<a
href="/wiki/index.php?title=List_of_hybrid_functionals&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-libxc_list_1-0)
    <a href="https://libxc.gitlab.io/functionals/" class="external text"
    rel="nofollow">https://libxc.gitlab.io/functionals/</a>
2.  [↑](#cite_ref-krukau:jcp:06_2-0)
    <a href="https://doi.org/10.1063/1.2404663" class="external text"
    rel="nofollow">A. V. Krukau , O. A. Vydrov, A. F. Izmaylov, and G. E.
    Scuseria, J. Chem. Phys. <strong>125</strong>, 224106 (2006).</a>
3.  [↑](#cite_ref-heyd:jcp:03_3-0)
    <a href="https://doi.org/10.1063/1.1564060" class="external text"
    rel="nofollow">J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys.
    <strong>118</strong>, 8207 (2003).</a>
4.  [↑](#cite_ref-heyd:jcp:04_4-0)
    <a href="https://doi.org/10.1063/1.1760074" class="external text"
    rel="nofollow">J. Heyd and G. E. Scuseria, J. Chem. Phys.
    <strong>121</strong>, 1187 (2004).</a>
5.  [↑](#cite_ref-heyd:jcp:06_5-0)
    <a href="https://doi.org/10.1063/1.2204597" class="external text"
    rel="nofollow">J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys.
    <strong>124</strong>, 219906 (2006).</a>
6.  [↑](#cite_ref-schimka:jcp:11_6-0)
    <a href="https://doi.org/10.1063/1.3524336" class="external text"
    rel="nofollow">L. Schimka, J. Harl, and G. Kresse, J. Chem. Phys.
    <strong>134</strong>, 024116 (2011).</a>
7.  [↑](#cite_ref-skone:prb:2016_7-0)
    <a href="http://doi.org/10.1103/PhysRevB.93.235106"
    class="external text" rel="nofollow">J. H. Skone, M. Govoni, and G.
    Galli, <em>Nonempirical range-separated hybrid functionals for solids
    and molecules</em>, Phys. Rev. B <strong>93</strong>, 235106 (2016).</a>
8.  [↑](#cite_ref-chen2018nonempirical_8-0)
    <a href="https://doi.org/10.1103/PhysRevMaterials.2.073803"
    class="external text" rel="nofollow">W. Chen, G. Miceli, G.M. Rignanese,
    and A. Pasquarello, <em>Nonempirical dielectric-dependent hybrid
    functional with range separation for semiconductors and insulators</em>,
    Phys. Rev. Mater. <strong>2</strong>, 073803 (2018).</a>
9.  [↑](#cite_ref-cui2018doubly_9-0)
    <a href="https://doi.org/10.1021/acs.jpclett.8b00919"
    class="external text" rel="nofollow">Z.H. Cui, Y.C. Wang, M.Y. Zhang, X.
    Xu, and H. Jiang, <em>Doubly Screened Hybrid Functional: An Accurate
    First-Principles Approach for Both Narrow- and Wide-Gap
    Semiconductors</em> J. Phys. Chem. Lett., <strong>9</strong>, 2338-2345
    (2018).</a>
10. [↑](#cite_ref-gerber:jcp:2007_10-0)
    <a href="http://doi.org/10.1063/1.2759209" class="external text"
    rel="nofollow">I. C. Gerber, J. G. Ángyán, M. Marsman, and G. Kresse,
    <em>Range separated hybrid density functional with long-range
    Hartree-Fock exchange applied to solids</em>, J. Chem. Phys.
    <strong>127</strong>, 054101 (2007).</a>
11. [↑](#cite_ref-gerber:cpl:2005_11-0)
    <a href="http://doi.org/10.1016/j.cplett.2005.08.060"
    class="external text" rel="nofollow">I. C. Gerber and J. G. Ángyán,
    <em>Hybrid functional with separated range</em>, Chem. Phys. Lett.
    <strong>415</strong>, 100 (2005).</a>
12. [↑](#cite_ref-bylander:prb:90_12-0)
    <a href="https://doi.org/10.1103/PhysRevB.41.7868" class="external text"
    rel="nofollow">D. M. Bylander and L. Kleinman, Phys. Rev. B
    <strong>41</strong>, 7868 (1990).</a>
13. [↑](#cite_ref-perdew:jcp:1996_13-0)
    <a href="https://doi.org/10.1063/1.472933" class="external text"
    rel="nofollow">J. P. Perdew, M. Ernzerhof, and K. Burke, J. Chem. Phys.
    <strong>105</strong>, 9982 (1996).</a>
14. [↑](#cite_ref-ernzerhof:jcp:99_14-0)
    <a href="https://doi.org/10.1063/1.478401" class="external text"
    rel="nofollow">M. Ernzerhof and G. E. Scuseria, J. Chem. Phys.
    <strong>110</strong>, 5029 (1999).</a>
15. [↑](#cite_ref-adamo:jcp:1999_15-0)
    <a href="https://doi.org/10.1063/1.478522" class="external text"
    rel="nofollow">C. Adamo and V. Barone, Phys. Rev. Lett.,
    <strong>110</strong>, 6158 (1999).</a>
16. [↑](#cite_ref-stephens:jpc:94_16-0)
    <a href="https://doi.org/10.1021/j100096a001" class="external text"
    rel="nofollow">P. J. Stephens, F. J. Devlin, C. F. Chabalowski, and M.
    J. Frisch, J. Phys. Chem. <strong>98</strong>, 11623 (1994).</a>
17. [↑](#cite_ref-becke:jcp:93_17-0)
    <a href="https://doi.org/10.1063/1.464913" class="external text"
    rel="nofollow">A. D. Becke, J. Chem. Phys. <strong>98</strong>, 5648
    (1993).</a>
18. [↑](#cite_ref-bilc:prb:08_18-0)
    <a href="https://doi.org/10.1103/PhysRevB.77.165107"
    class="external text" rel="nofollow">D. I. Bilc, R. Orlando, R. Shaltaf,
    G.-M. Rignanese, J. Iniguez, and P. Ghosez, Phys. Rev. B
    <strong>77</strong>, 165107 (2008).</a>


------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/Category:Van_der_Waals_functionals | revid: 34494 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Van der Waals functionals


The semilocal (SL) and hybrid exchange-correlation functionals do not
include the London dispersion forces. Therefore, they can not be applied
reliably on systems where the London dispersion forces play an important
role. To account more properly for the London dispersion forces in DFT,
a correlation dispersion term can be added to the semilocal or hybrid
functional.<sup>[\[1\]](#cite_note-grimme:cr:2016-1)[\[2\]](#cite_note-hermann:cr:2017-2)</sup>
This leads to the so-called **van der Waals functionals**:

$E_{\text{xc}}^{\text{vdW}} = E_{\text{xc}}^{\text{SL/hybrid}} +
E_{\text{c,disp}}.$

There are essentially three types of dispersion terms
$E_{\text{c,disp}}$ that are available in VASP, and a
brief sketch of them is given below along with links to pages that
provide more detail. Note that
[libMBD](../incar-tags/LIBMBD_METHOD.md) is an external package
that provides the Tkatchenko-Scheffler atom-pairwise methods and their
many-body dispersion extensions.


## Contents


- [1 Types of
  approximations](#types-of-approximations)
  - [1.1
    Atom-pairwise
    methods](#atom-pairwise-methods)
  - [1.2 Many-body
    dispersion methods](#many-body-dispersion-methods)
  - [1.3 Nonlocal
    vdW-DF functionals](#nonlocal-vdw-df-functionals)
- [2
  References](#references)


## Types of approximations\[<a
href="/wiki/index.php?title=Category:Van_der_Waals_functionals&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Types of approximations">edit</a> \| (./index.php.md)\]

### Atom-pairwise methods\[<a
href="/wiki/index.php?title=Category:Van_der_Waals_functionals&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Atom-pairwise methods">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Dft%2Bd.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/9/95/Dft%2Bd.png/300px-Dft%2Bd.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/9/95/Dft%2Bd.png/450px-Dft%2Bd.png 1.5x, /wiki/images/thumb/9/95/Dft%2Bd.png/600px-Dft%2Bd.png 2x"
width="300" height="216" /></a>
<figcaption>Dipole-dipole interactions between atoms (black dots) and
quadrupole-dipole interactions (purple arrows). All of these terms are
pairwise. Adapted from Fig. 2 in Ref. <sup><a
href="#cite_note-hermann:cr:2017-2">[2]</a></sup>.</figcaption>
</figure>

They consist of a sum over the atoms pairs $A$-$B$:

$E_{\text{c,disp}} =
-\sum_{A<B}\sum_{n=6,8,10,\ldots}f_{n}^{\text{damp}}(R_{AB})\frac{C_{n}^{AB}}{R_{AB}^{n}},$

where $C_{n}^{AB}$
are the dispersion coefficients, $R_{AB}$ is
the distance between atoms $A$ and
$B$, and $f_{n}^{\text{damp}}$ is a damping function. Several variants of such
atom-pair corrections exist and the most popular of them, listed below,
are available in VASP and are selected with the
[IVDW](../incar-tags/IVDW.md) tag.

- [DFT-D2](DFT-D2.md)<sup>[\[3\]](#cite_note-grimme:jcc:06-3)</sup>
- [DFT-D3](DFT-D3.md)<sup>[\[4\]](#cite_note-grimme:jcp:10-4)[\[5\]](#cite_note-grimme:jcc:11-5)</sup>
- [simple-DFT-D3](Simple-DFT-D3.md)<sup>[\[6\]](#cite_note-ehlert:joss:2024-6)[\[7\]](#cite_note-sdftd3_1-7)[\[8\]](#cite_note-sdftd3_2-8)</sup>
  (available as of VASP.6.6.0 as [external
  package](../misc/Makefile.include.md))
- [DFT-D4](DFT-D4.md)<sup>[\[9\]](#cite_note-caldeweyher:jcp:2019-9)[\[10\]](#cite_note-dftd4_1-10)[\[11\]](#cite_note-dftd4_2-11)</sup>
  (available as of VASP.6.2 as [external
  package](../misc/Makefile.include.md))
- [DFT-ulg](DFT-ulg.md)<sup>[\[12\]](#cite_note-kim:jpcl:2012-12)</sup>
- [Tkatchenko-Scheffler
  method](Tkatchenko-Scheffler_method.md)<sup>[\[13\]](#cite_note-tkatchenko:prl:09-13)</sup>
- [Tkatchenko-Scheffler method with iterative Hirshfeld
  partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md)<sup>[\[14\]](#cite_note-bucko:jctc:13-14)[\[15\]](#cite_note-bucko:jcp:14-15)</sup>
- [Self-consistent screening in Tkatchenko-Scheffler
  method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md)<sup>[\[16\]](#cite_note-tkatchenko:prl:12-16)</sup>
- [Library libMBD of many-body dispersion
  methods](../incar-tags/LIBMBD_METHOD.md)<sup>[\[17\]](#cite_note-libmbd_1-17)[\[18\]](#cite_note-libmbd_2-18)[\[19\]](#cite_note-hermann:jcp:2023-19)</sup>
  (available as of VASP.6.4.3 as [external
  package](../misc/Makefile.include.md))
- [DDsC dispersion
  correction](DDsC_dispersion_correction.md)<sup>[\[20\]](#cite_note-steinmann:jcp:11-20)[\[21\]](#cite_note-steinmann:jctc:11-21)</sup>


### Many-body dispersion methods\[<a
href="/wiki/index.php?title=Category:Van_der_Waals_functionals&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Many-body dispersion methods">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Mbd.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/0/0c/Mbd.png/300px-Mbd.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/0c/Mbd.png/450px-Mbd.png 1.5x, /wiki/images/thumb/0/0c/Mbd.png/600px-Mbd.png 2x"
width="300" height="240" /></a>
<figcaption>Dipole-dipole interactions between atoms (black dots) in
many-body dispersions include the previously considered 2-body
(pairwise) terms shown with purple arrows, in addition to the 3-, 4-,
N-body dipole interaction terms shown with green arrows. Adapted from
Fig. 2 in Ref. <sup><a href="#cite_note-hermann:cr:2017-2">[2]</a></sup>.</figcaption>
</figure>

These methods are based on the random-phase expression for the
correlation energy, which is expressed as an integral over the frequency
$\omega$ involving the frequency-dependent
polarizability ${\mathbf{A}}_{LR}$:

$E_{\mathrm{c,disp}} =
-\int_{\mathrm{FBZ}}\frac{d{\mathbf{k}}}{v_{\mathrm{FBZ}}}
\int_0^{\infty} {\frac{d\omega}{2\pi}} \\ {\mathrm{Tr}}\left \\
\mathrm{ln} \left ({\mathbf{1}}-{\mathbf{A}}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}}) \right ) \right \\.$

These methods, listed below, are selected with the
[IVDW](../incar-tags/IVDW.md) tag.

- [Many-body dispersion
  energy](Many-body_dispersion_energy.md)<sup>[\[16\]](#cite_note-tkatchenko:prl:12-16)[\[22\]](#cite_note-ambrosetti:jcp:14-22)</sup>
- [Many-body dispersion energy with fractionally ionic model for
  polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)<sup>[\[23\]](#cite_note-gould:jctc:2016_a-23)[\[24\]](#cite_note-gould:jctc:2016_b-24)</sup>
- [Library libMBD of many-body dispersion
  methods](../incar-tags/LIBMBD_METHOD.md)<sup>[\[17\]](#cite_note-libmbd_1-17)[\[18\]](#cite_note-libmbd_2-18)[\[19\]](#cite_note-hermann:jcp:2023-19)</sup>


### Nonlocal vdW-DF functionals\[<a
href="/wiki/index.php?title=Category:Van_der_Waals_functionals&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Nonlocal vdW-DF functionals">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Non_local_dft.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/74/Non_local_dft.png/300px-Non_local_dft.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/74/Non_local_dft.png/450px-Non_local_dft.png 1.5x, /wiki/images/thumb/7/74/Non_local_dft.png/600px-Non_local_dft.png 2x"
width="300" height="222" /></a>
<figcaption>Nonlocal DFT interaction (purple arrows) between pairwise
dipole fluctuations in the density. Adapted from Fig. 2 in Ref. <sup><a
href="#cite_note-hermann:cr:2017-2">[2]</a></sup>.</figcaption>
</figure>

These are density functionals that require a double spatial integration
and are, therefore, nonlocal:

$E_{\text{c,disp}} = \frac{1}{2}\int\int n(\textbf{r})
\Phi\left(\textbf{r},\textbf{r}'\right) n(\textbf{r}') d^{3}rd^{3}r',$

where the kernel $\Phi$ depends
on the electronic density $n$, its
derivative $\nabla n$ as
well as on the interelectronic distance $\left\vert\bf{r}-\bf{r}'\right\vert$. The nonlocal
functionals are more expensive to calculate than semilocal functionals,
however, they are efficiently implemented by using FFTs
<sup>[\[25\]](#cite_note-romanperez:prl:09-25)</sup>.
These methods are selected with the
[LUSE_VDW](../incar-tags/LUSE_VDW.md) and
[IVDW_NL](../incar-tags/IVDW_NL.md) tags.

- [Nonlocal vdW-DF
  functionals](Nonlocal_vdW-DF_functionals.md)


## References\[<a
href="/wiki/index.php?title=Category:Van_der_Waals_functionals&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-grimme:cr:2016_1-0)
    <a href="https://doi.org/10.1021/acs.chemrev.5b00533"
    class="external text" rel="nofollow">S. Grimme, A. hansen, J. G.
    Brandenburg, and C. Bannwarth, <em>Dispersion-Corrected Mean-Field
    Electronic Structure Methods</em>, Chem. Rev. <strong>116</strong>, 5105
    (2016).</a>
2.  ↑
    <sup>[a](#cite_ref-hermann:cr:2017_2-0)</sup>
    <sup>[b](#cite_ref-hermann:cr:2017_2-1)</sup>
    <sup>[c](#cite_ref-hermann:cr:2017_2-2)</sup>
    <sup>[d](#cite_ref-hermann:cr:2017_2-3)</sup>
    <a href="https://doi.org/10.1021/acs.chemrev.6b00446"
    class="external text" rel="nofollow">J. Hermann, R. A. DiStasio Jr., and
    A. Tkatchenko, <em>First-Principles Models for van der Waals
    Interactions in Molecules and Materials: Concepts, Theory, and
    Applications</em>, Chem. Rev. <strong>117</strong>, 4714 (2017).</a>
3.  [↑](#cite_ref-grimme:jcc:06_3-0)
    <a href="https://doi.org/10.1002/jcc.20495" class="external text"
    rel="nofollow">S. Grimme, J. Comput. Chem. <strong>27</strong>, 1787
    (2006).</a>
4.  [↑](#cite_ref-grimme:jcp:10_4-0)
    <a href="https://doi.org/10.1063/1.3382344" class="external text"
    rel="nofollow">S. Grimme, J. Antony, S. Ehrlich, and S. Krieg, J. Chem.
    Phys. <strong>132</strong>, 154104 (2010).</a>
5.  [↑](#cite_ref-grimme:jcc:11_5-0)
    <a href="https://doi.org/10.1002/jcc.21759" class="external text"
    rel="nofollow">S. Grimme, S. Ehrlich, and L. Goerigk, J. Comput. Chem.
    <strong>32</strong>, 1456 (2011).</a>
6.  [↑](#cite_ref-ehlert:joss:2024_6-0)
    <a href="https://doi.org/10.21105/joss.07169" class="external text"
    rel="nofollow">S. Ehlert, <em>Simple dft-d3: library first
    implementation of the d3 dispersion correction</em>, J. Open Source
    Softw. <strong>9</strong>, 7169 (2024).</a>
7.  [↑](#cite_ref-sdftd3_1_7-0)
    <a href="https://dftd3.readthedocs.io/" class="external text"
    rel="nofollow">https://dftd3.readthedocs.io</a>
8.  [↑](#cite_ref-sdftd3_2_8-0)
    <a href="https://github.com/dftd3/" class="external text"
    rel="nofollow">https://github.com/dftd3</a>
9.  [↑](#cite_ref-caldeweyher:jcp:2019_9-0)
    <a href="https://doi.org/10.1063/1.5090222" class="external text"
    rel="nofollow">E. Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S.
    Spicher, C. Bannwarth, and S. Grimme, J. Chem. Phys.
    <strong>150</strong>, 154122 (2019).</a>
10. [↑](#cite_ref-dftd4_1_10-0)
    <a href="https://dftd4.readthedocs.io/" class="external text"
    rel="nofollow">https://dftd4.readthedocs.io</a>
11. [↑](#cite_ref-dftd4_2_11-0)
    <a href="https://github.com/dftd4/" class="external text"
    rel="nofollow">https://github.com/dftd4</a>
12. [↑](#cite_ref-kim:jpcl:2012_12-0)
    <a href="https://doi.org/10.1021/jz2016395" class="external text"
    rel="nofollow">H. Kim, J.-M. Choi, and W. A. Goddard, III, J. Phys.
    Chem. Lett. <strong>3</strong>, 360 (2012).</a>
13. [↑](#cite_ref-tkatchenko:prl:09_13-0)
    <a href="https://doi.org/10.1103/PhysRevLett.102.073005"
    class="external text" rel="nofollow">A. Tkatchenko and M. Scheffler,
    Phys. Rev. Lett. <strong>102</strong>, 073005 (2009).</a>
14. [↑](#cite_ref-bucko:jctc:13_14-0)
    <a href="https://doi.org/10.1021/ct400694h" class="external text"
    rel="nofollow">T. Bučko, S. Lebègue, J. Hafner, and J. G. Ángyán, J.
    Chem. Theory Comput. <strong>9</strong>, 4293 (2013)</a>
15. [↑](#cite_ref-bucko:jcp:14_15-0)
    <a href="https://doi.org/10.1063/1.4890003" class="external text"
    rel="nofollow">T. Bučko, S. Lebègue, J. G. Ángyán, and J. Hafner, J.
    Chem. Phys. <strong>141</strong>, 034114 (2014).</a>
16. ↑
    <sup>[a](#cite_ref-tkatchenko:prl:12_16-0)</sup>
    <sup>[b](#cite_ref-tkatchenko:prl:12_16-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.108.236402"
    class="external text" rel="nofollow">A. Tkatchenko, R. A. DiStasio, Jr.,
    R. Car, and M. Scheffler, Phys. Rev. Lett. <strong>108</strong>, 236402
    (2012).</a>
17. ↑
    <sup>[a](#cite_ref-libmbd_1_17-0)</sup>
    <sup>[b](#cite_ref-libmbd_1_17-1)</sup>
    <a href="https://libmbd.github.io/" class="external text"
    rel="nofollow">https://libmbd.github.io/</a>
18. ↑
    <sup>[a](#cite_ref-libmbd_2_18-0)</sup>
    <sup>[b](#cite_ref-libmbd_2_18-1)</sup>
    <a href="https://github.com/libmbd/" class="external text"
    rel="nofollow">https://github.com/libmbd/</a>
19. ↑
    <sup>[a](#cite_ref-hermann:jcp:2023_19-0)</sup>
    <sup>[b](#cite_ref-hermann:jcp:2023_19-1)</sup>
    <a href="https://doi.org/10.1063/5.0170972" class="external text"
    rel="nofollow">J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi,
    R. J. Maurer, and A. Tkatchenko, <em>libMBD: A general-purpose package
    for scalable quantum many-body dispersion calculations</em>, J. Chem.
    Phys. <strong>159</strong>, 174802 (2023).</a>
20. [↑](#cite_ref-steinmann:jcp:11_20-0)
    <a href="https://doi.org/10.1063/1.3545985" class="external text"
    rel="nofollow">S. N. Steinmann and C. Corminboeuf, J. Chem. Phys.
    <strong>134</strong>, 044117 (2011).</a>
21. [↑](#cite_ref-steinmann:jctc:11_21-0)
    <a href="https://doi.org/10.1021/ct200602x" class="external text"
    rel="nofollow">S. N. Steinmann and C. Corminboeuf, J. Chem. Theory
    Comput. <strong>7</strong>, 3567 (2011).</a>
22. [↑](#cite_ref-ambrosetti:jcp:14_22-0)
    <a href="https://doi.org/10.1063/1.4865104" class="external text"
    rel="nofollow">A. Ambrosetti, A. M. Reilly, and R. A. DiStasio Jr., J.
    Chem. Phys. <strong>140</strong>, 018A508 (2014).</a>
23. [↑](#cite_ref-gould:jctc:2016_a_23-0)
    <a href="https://doi.org/10.1021/acs.jctc.6b00361" class="external text"
    rel="nofollow">T. Gould and T. Bučko, <em>C6 Coefficients and Dipole
    Polarizabilities for All Atoms and Many Ions in Rows 1–6 of the Periodic
    Table</em>, J. Chem. Theory Comput. <strong>12</strong>, 3603
    (2016).</a>
24. [↑](#cite_ref-gould:jctc:2016_b_24-0)
    <a href="https://doi.org/10.1021/acs.jctc.6b00925" class="external text"
    rel="nofollow">T. Gould, S. Lebègue, J. G. Ángyán, and T. Bučko, <em>A
    Fractionally Ionic Approach to Polarizability and van der Waals
    Many-Body Dispersion Calculations</em>, J. Chem. Theory Comput.
    <strong>12</strong>, 5920 (2016).</a>
25. [↑](#cite_ref-romanperez:prl:09_25-0)
    <a href="https://doi.org/10.1103/PhysRevLett.103.096102"
    class="external text" rel="nofollow">G. Román-Pérez and J. M. Soler,
    Phys. Rev. Lett. <strong>103</strong>, 096102 (2009).</a>



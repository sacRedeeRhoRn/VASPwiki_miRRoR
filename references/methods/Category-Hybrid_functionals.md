<!-- Source: https://vasp.at/wiki/index.php/Category:Hybrid_functionals | revid: 36697 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Hybrid functionals


**Hybrid functionals** go beyond the semilocal approximations by mixing
the Hartree-Fock (HF) and semilocal (SL)
exchange<sup>[\[1\]](#cite_note-becke:jcp:93-1)</sup>:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a E_{\mathrm{x}}^{\mathrm{HF}} +
(1-a)E_{\mathrm{x}}^{\mathrm{SL}} + E_{\mathrm{c}}^{\mathrm{SL}}$

where $a$ is the
mixing parameter that determines the relative weights of HF and
semilocal exchange.

Depending on the type of systems or the property under consideration
they can be more accurate than semilocal (GGA, meta-GGA) functionals.
For instance, hybrid functionals are usually more suited for calculating
the electronic and magnetic properties of nonmetallic systems. They are
particularly recommended for bandgap
calculations.<sup>[\[2\]](#cite_note-heyd:jcp:05-2)[\[3\]](#cite_note-chen2018nonempirical-3)</sup>
Polarons<sup>[\[4\]](#cite_note-franchini:nrm:21-4)</sup>
or defect
states<sup>[\[5\]](#cite_note-oba:prb:08-5)</sup>
are among properties that can also be better described by hybrid
functionals. Note that hybrid functionals are also often good at
treating [strongly correlated
electrons](Category-Strongly_correlated_electrons.md).<sup>[\[6\]](#cite_note-liu2019assessing-6)</sup>

- 

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>Evaluating the HF exchange is computationally very demanding,
leading to <strong>a computational time that is one or several orders of
magnitude larger than with semilocal functionals</strong>. Therefore, a
proper assessment of the available computational resources and
parallelization strategies becomes increasingly important.</li>
<li>Some properties cannot be computed using hybrid functionals because
the corresponding implementations are not yet available. A
non-exhaustive list includes <a
href="/wiki/Electron-phonon_interactions_theory"
title="Electron-phonon interactions theory">electron-phonon
interactions</a>, <a
href="/wiki/Phonons_from_density-functional-perturbation_theory"
title="Phonons from density-functional-perturbation theory">phonons from
density-functional-perturbation theory</a>, and <a
href="/wiki/Calculating_the_chemical_shieldings"
title="Calculating the chemical shieldings">NMR shielding</a>. However,
note that hybrid functionals can be used if the phonons are calculated
using the <a href="/wiki/Phonons_from_finite_differences"
title="Phonons from finite differences">finite differences
method</a>.</li>
</ul></td>
</tr>
</tbody>
</table>


## Contents


- [1
  Overview](#Overview)
- [2 Technical
  points](#Technical_points)
- [3 Additional
  resources](#Additional_resources)
  - [3.1
    Tutorials](#Tutorials)
  - [3.2
    Lectures](#Lectures)
  - [3.3 How
    to](#How_to)
  - [3.4 Further
    reading](#Further_reading)
- [4
  References](#References)


## Overview\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Overview">edit</a> \| (./index.php.md)\]

The hybrid functionals can be divided into families according to the
type of semilocal approximation that is used (LDA, GGA, or MGGA) and the
interelectronic range at which the HF exchange is applied: at full range
(unscreened hybrids) or either at short or long range (called screened
or range-separated hybrids). From the practical point of view, the
short-range hybrid functionals like
HSE06<sup>[\[7\]](#cite_note-krukau:jcp:06-7)</sup>
are preferable for periodic solids, since leading to faster convergence
with respect to the number of k-points (or size of the unit cell).

The different families of hybrid functionals available in VASP are
described in details at [formalism of the HF method and
hybrids](Hybrid_functionals-_formalism.md)
along with examples and links to the corresponding
[INCAR](../input-files/INCAR.md) files.

Details about the implementation of the unscreened hybrid functionals
can be found in the work of Paier et
al.,<sup>[\[8\]](#cite_note-paier:jcp:05-8)</sup>
while details specific to the screened hybrid functionals can be found
in Refs.
<sup>[\[9\]](#cite_note-paier:jcp:06-9)[\[10\]](#cite_note-angyan:jpa:2006-10)</sup>
Refs.
<sup>[\[11\]](#cite_note-cui2018doubly-11)[\[6\]](#cite_note-liu2019assessing-6)</sup>
report the development of dielectric-dependent hybrid functionals, which
provide very accurate band gaps and are also available in VASP.

Note that as in most other codes, hybrid functionals are implemented in
VASP within the generalized KS
scheme,<sup>[\[12\]](#cite_note-seidl:prb:96-12)</sup>
which means that the total energy is minimized, as in the HF theory,
with respect to the orbitals instead of the electron density.

VASP offers a convenient way to generate the [band structure with hybrid
functionals](Band-structure_calculation_using_hybrid_functionals.md).

## Technical points\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Technical points">edit</a> \| (./index.php.md)\]

- The unscreened Coulomb potential used to evaluate the exchange
  integral in HF has an integrable Coulomb singularity that leads to
  slow convergence with respect to supercell size (or equivalently **k**
  point sampling). To make the computations feasible requires special
  treatment of the [Coulomb
  singularity](Coulomb_singularity.md).

<!-- -->

- The [Downsampling of the HF
  operator](Downsampling_of_the_Hartree-Fock_operator.md)
  allows for the use of a coarser **k** point sampling for the HF
  operator, and therefore faster
  calculations.<sup>[\[9\]](#cite_note-paier:jcp:06-9)</sup>
  However, this option should be use with care for metals.

<!-- -->

- The Adaptively Compressed Exchange
  Operator,<sup>[\[13\]](#cite_note-linlin:jctc:2016-13)</sup>
  that allows for a more efficient evaluation of the Fock operator, is
  used if the Davidson algorithm ([ALGO](../incar-tags/ALGO.md) = Normal,
  the default) is selected (see [LFOCKACE](../incar-tags/LFOCKACE.md)
  for more details).

## Additional resources\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Tutorials\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/hybrids/part1"
  class="external text" rel="nofollow">hybrid calculations</a>.

### Lectures\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on
  <a href="https://youtu.be/zNc0bx8FTlU" class="external text"
  rel="nofollow">hybrid functionals</a>.

### How to\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

- [Formalism of the HF method and
  hybrids](Hybrid_functionals-_formalism.md).
  The various families are described.
- [List of available hybrid
  functionals](List_of_hybrid_functionals.md)
  and how to specify them in the [INCAR](../input-files/INCAR.md) file.
- [Downsampling of the Hartree-Fock
  operator](Downsampling_of_the_Hartree-Fock_operator.md)
  to reduce the computational cost.
- [band-structure calculation using hybrid
  functionals](Band-structure_calculation_using_hybrid_functionals.md).

### Further reading\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Further reading">edit</a> \| (./index.php.md)\]

In addition to the works already cited above, the selected publications
listed below describe methodological developments or computational
studies performed using the hybrid functionals implemented in VASP.

- The B3LYP functional applied to solid-state systems and its failure
  for
  metals<sup>[\[14\]](#cite_note-paier:jcp:07-14)</sup>.
- Applications of hybrid functionals to selected materials:
  Ceria,<sup>[\[15\]](#cite_note-juarez:prb:07-15)</sup>
  lead
  chalcogenides,<sup>[\[16\]](#cite_note-hummer:prb:07-16)</sup>
  CO adsorption on
  metals,<sup>[\[17\]](#cite_note-stroppa:prb:07-17)[\[18\]](#cite_note-stroppa:njp:08-18)</sup>
  excitonic
  properties,<sup>[\[19\]](#cite_note-paier:prb:08-19)</sup>
  SrTiO and BaTiO,
  <sup>[\[20\]](#cite_note-wahl:prb:08-20)</sup>
  perovskites,<sup>[\[21\]](#cite_note-franchini:jpcm:14-21)</sup>
  and transition-metal
  oxides.<sup>[\[22\]](#cite_note-gopidi:prb:26-22)</sup>
- HSEsol hybrid
  functional.<sup>[\[23\]](#cite_note-schimka:jcp:11-23)</sup>
- Analysis of the HSE parameter
  space.<sup>[\[24\]](#cite_note-moussa:jcp:12-24)</sup>
- Automated workflow for non-empirical Wannier-localized optimal tuning
  of range-separated hybrid
  functionals.<sup>[\[25\]](#cite_note-gant:cpc:26-25)</sup>

## References\[<a
href="/wiki/index.php?title=Category:Hybrid_functionals&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-becke:jcp:93_1-0)
    <a href="https://doi.org/10.1063/1.464913" class="external text"
    rel="nofollow">A. D. Becke, J. Chem. Phys. <strong>98</strong>, 5648
    (1993).</a>
2.  [↑](#cite_ref-heyd:jcp:05_2-0)
    <a href="https://doi.org/10.1063/1.2085170" class="external text"
    rel="nofollow">J. Heyd, J. E. Peralta, G. E. Scuseria, and R. L. Martin,
    <em>Energy band gaps and lattice parameters evaluated with the
    Heyd-Scuseria-Ernzerhof screened hybrid functional</em>, J. Chem. Phys.
    <strong>123</strong>, 174101 (2005).</a>
3.  [↑](#cite_ref-chen2018nonempirical_3-0)
    <a href="https://doi.org/10.1103/PhysRevMaterials.2.073803"
    class="external text" rel="nofollow">W. Chen, G. Miceli, G.M. Rignanese,
    and A. Pasquarello, <em>Nonempirical dielectric-dependent hybrid
    functional with range separation for semiconductors and insulators</em>,
    Phys. Rev. Mater. <strong>2</strong>, 073803 (2018).</a>
4.  [↑](#cite_ref-franchini:nrm:21_4-0)
    <a href="https://doi.org/10.1038/s41578-021-00289-w"
    class="external text" rel="nofollow">C. Franchini, M. Reticcioli, M.
    Setvin, and U. Diebold, <em>Polarons in Materials</em>, Nat. Rev. Mat.
    <strong>6</strong>, 560 (2021).</a>
5.  [↑](#cite_ref-oba:prb:08_5-0)
    <a href="https://doi.org/10.1103/PhysRevB.77.245202"
    class="external text" rel="nofollow">F. Oba, A. Togo, I. Tanaka, J.
    Paier, and G. Kresse, Phys. Rev. B <strong>77</strong>, 245202
    (2008).</a>
6.  ↑
    <sup>[a](#cite_ref-liu2019assessing_6-0)</sup>
    <sup>[b](#cite_ref-liu2019assessing_6-1)</sup>
    <a href="https://doi.org/10.1088/1361-648x/ab4150" class="external text"
    rel="nofollow">P. Liu, C. Franchini, M. Marsman, and G. Kresse,
    <em>Assessing model-dielectric-dependent hybrid functionals on the
    antiferromagnetic transition-metal monoxides MnO, FeO, CoO, and
    NiO</em>, J. Phys.: Condens. Matter <strong>32</strong>, 015502
    (2020).</a>
7.  [↑](#cite_ref-krukau:jcp:06_7-0)
    <a href="https://doi.org/10.1063/1.2404663" class="external text"
    rel="nofollow">A. V. Krukau , O. A. Vydrov, A. F. Izmaylov, and G. E.
    Scuseria, J. Chem. Phys. <strong>125</strong>, 224106 (2006).</a>
8.  [↑](#cite_ref-paier:jcp:05_8-0)
    <a href="https://doi.org/10.1063/1.1926272" class="external text"
    rel="nofollow">J. Paier, R. Hirschl, M. Marsman, and G. Kresse, J. Chem.
    Phys. <strong>122</strong>, 234102 (2005).</a>
9.  ↑
    <sup>[a](#cite_ref-paier:jcp:06_9-0)</sup>
    <sup>[b](#cite_ref-paier:jcp:06_9-1)</sup>
    <a href="https://doi.org/10.1063/1.2187006" class="external text"
    rel="nofollow">J. Paier, M. Marsman, K. Hummer, G. Kresse, I.C. Gerber,
    and J.G. Ángyán, J. Chem. Phys. <strong>124</strong>, 154709 (2006).</a>
10. [↑](#cite_ref-angyan:jpa:2006_10-0)
    <a href="http://dx.doi.org/10.1088/0305-4470/39/27/005"
    class="external text" rel="nofollow">J. G. Ángyán, I. Gerber, and M.
    Marsman, <em>Spherical harmonic expansion of short-range screened
    Coulomb interactions</em>, J. Phys. A: Math. Gen. <strong>39</strong>,
    8613 (2006).</a>
11. [↑](#cite_ref-cui2018doubly_11-0)
    <a href="https://doi.org/10.1021/acs.jpclett.8b00919"
    class="external text" rel="nofollow">Z.H. Cui, Y.C. Wang, M.Y. Zhang, X.
    Xu, and H. Jiang, <em>Doubly Screened Hybrid Functional: An Accurate
    First-Principles Approach for Both Narrow- and Wide-Gap
    Semiconductors</em> J. Phys. Chem. Lett., <strong>9</strong>, 2338-2345
    (2018).</a>
12. [↑](#cite_ref-seidl:prb:96_12-0)
    <a href="https://doi.org/10.1103/PhysRevB.53.3764" class="external text"
    rel="nofollow">A. Seidl, A. Görling, P. Vogl, J.A. Majewski, and M.
    Levy, Phys. Rev. B <strong>53</strong>, 3764 (1996).</a>
13. [↑](#cite_ref-linlin:jctc:2016_13-0)
    <a href="https://doi.org/10.1021/acs.jctc.6b00092" class="external text"
    rel="nofollow">L. Lin, J. Chem. Theory Comput. <strong>12</strong>,
    2242-2249 (2016).</a>
14. [↑](#cite_ref-paier:jcp:07_14-0)
    <a href="https://doi.org/10.1063/1.2747249" class="external text"
    rel="nofollow">J. Paier, M. Marsman, and G. Kresse, J. Chem. Phys.
    <strong>127</strong>, 024103 (2007).</a>
15. [↑](#cite_ref-juarez:prb:07_15-0)
    <a href="https://doi.org/10.1103/PhysRevB.75.045121"
    class="external text" rel="nofollow">J. L. F. Da Silva, M. V.
    Ganduglia-Pirovano, J. Sauer, V. Bayer, and G. Kresse, Phys. Rev. B
    <strong>75</strong>, 045121 (2007).</a>
16. [↑](#cite_ref-hummer:prb:07_16-0)
    <a href="https://doi.org/10.1103/PhysRevB.75.195211"
    class="external text" rel="nofollow">Hummer, A. Grüneis, and G. Kresse,
    Phys. Rev. B <strong>75</strong>, 195211 (2007).</a>
17. [↑](#cite_ref-stroppa:prb:07_17-0)
    <a href="https://doi.org/10.1103/PhysRevB.76.195440"
    class="external text" rel="nofollow">A. Stroppa, K. Termentzidis, J.
    Paier, G. Kresse, and J. Hafner, Phys. Rev. B <strong>76</strong>,
    195440 (2007).</a>
18. [↑](#cite_ref-stroppa:njp:08_18-0)
    <a href="https://doi.org/10.1088/1367-2630/10/6/063020"
    class="external text" rel="nofollow">A. Stroppa and G. Kresse, New
    Journal of Physics <strong>10</strong>, 063020 (2008).</a>
19. [↑](#cite_ref-paier:prb:08_19-0)
    <a href="https://doi.org/10.1103/PhysRevB.78.121201"
    class="external text" rel="nofollow">J. Paier, M. Marsman, and G.
    Kresse, Phys. Rev. B <strong>78</strong>, 121201(R) (2008).</a>
20. [↑](#cite_ref-wahl:prb:08_20-0)
    <a href="https://doi.org/10.1103/PhysRevB.78.104116"
    class="external text" rel="nofollow">R. Wahl, D. Vogtenhuber, and G.
    Kresse, Phys. Rev. B <strong>78</strong>, 104116 (2008).</a>
21. [↑](#cite_ref-franchini:jpcm:14_21-0)
    <a href="http://dx.doi.org/10.1088/0953-8984/26/25/253202"
    class="external text" rel="nofollow">C. Franchini, <em>Hybrid
    functionals applied to perovskites</em>, J. Phys.: Condens. Matter
    <strong>26</strong>, 253202 (2014).</a>
22. [↑](#cite_ref-gopidi:prb:26_22-0)
    <a href="https://doi.org/10.1103/myd5-l4f4" class="external text"
    rel="nofollow">H. R. Gopidi, R. Zhang, Y. Wang, A. Patra, J. Sun, A.
    Ruzsinszky, J. P. Perdew, and P. Canepa, <em>Reducing self-interaction
    error in transition-metal oxides with different exact-exchange fractions
    for energy and density</em>, Phys. Rev, B <strong>113</strong>, 165115
    (2026).</a>
23. [↑](#cite_ref-schimka:jcp:11_23-0)
    <a href="https://doi.org/10.1063/1.3524336" class="external text"
    rel="nofollow">L. Schimka, J. Harl, and G. Kresse, J. Chem. Phys.
    <strong>134</strong>, 024116 (2011).</a>
24. [↑](#cite_ref-moussa:jcp:12_24-0)
    <a href="http://doi.org/10.1063/1.4722993" class="external text"
    rel="nofollow">J. E. Moussa, P. A. Schultz, and J. R. Chelikowsky,
    <em>Analysis of the Heyd-Scuseria-Ernzerhof density functional parameter
    space</em>, J. Chem. Phys. <strong>136</strong>, 204117 (2012).</a>
25. [↑](#cite_ref-gant:cpc:26_25-0)
    <a href="https://doi.org/10.1016/j.cpc.2025.109995"
    class="external text" rel="nofollow">S. E. Gant, F. Ricci, G. Ohad, A.
    Ramasubramaniam, L. Kronik, and J. B. Neaton, <em>Automated workflow for
    non-empirical Wannier-localized optimal tuning of range-separated hybrid
    functionals</em>, Comput. Phys. Commun. <strong>320</strong>, 109995
    (2026).</a>



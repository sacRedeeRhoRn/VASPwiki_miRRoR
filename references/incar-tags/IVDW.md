<!-- Source: https://vasp.at/wiki/index.php/IVDW | revid: 34375 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IVDW


IVDW = \[integer\] 

|                   |     |                 |
|-------------------|-----|-----------------|
| Default: **IVDW** | = 0 | (no correction) |

Description: IVDW specifies a
vdW dispersion term of the atom-pairwise or many-body type.

------------------------------------------------------------------------

## Available vdW atom-pairwise and many-body methods\[<a href="/wiki/index.php?title=IVDW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Available vdW atom-pairwise and many-body methods">edit</a> \| (./index.php.md)\]

With all methods listed below, a dispersion correction is added to the
total energy, but also to the atomic forces and stress tensor, such that
lattice relaxations, molecular dynamics, and vibrational analysis (via
finite differences) can be performed. Note, however, that these
correction schemes are currently not available for phonon calculations
based on [density functional perturbation
theory](../theory/Phonons-_Theory.md).

|  |  |  |
|----|----|----|
| IVDW= | Type | Description |
| 1 or 10 | pairwise | [DFT-D2](../methods/DFT-D2.md) method of Grimme.<sup>[\[1\]](#cite_note-grimme:jcc:06-1)</sup> Available as of VASP.5.2.11. |
| 11 | pairwise | [DFT-D3](../methods/DFT-D3.md) method of Grimme with zero-damping function.<sup>[\[2\]](#cite_note-grimme:jcp:10-2)</sup> Available as of VASP.5.3.4. |
| 12 | pairwise | [DFT-D3](../methods/DFT-D3.md) method with Becke-Johnson damping function.<sup>[\[3\]](#cite_note-grimme:jcc:11-3)</sup> Available as of VASP.5.3.4. |
| 15 | pairwise | DFT-D3 methods available in the [simple-DFT-D3](../methods/Simple-DFT-D3.md) library.<sup>[\[4\]](#cite_note-ehlert:joss:2024-4)[\[5\]](#cite_note-sdftd3_1-5)[\[6\]](#cite_note-sdftd3_2-6)</sup> Available as of VASP.6.6.0 as [external package](../misc/Makefile.include.md). |
| 13 | pairwise | [DFT-D4](../methods/DFT-D4.md) method.<sup>[\[7\]](#cite_note-caldeweyher:jcp:2019-7)[\[8\]](#cite_note-dftd4_1-8)[\[9\]](#cite_note-dftd4_2-9)</sup> Available as of VASP.6.2 as [external package](../misc/Makefile.include.md). |
| 3 | pairwise | [DFT-ulg](../methods/DFT-ulg.md)<sup>[\[10\]](#cite_note-kim:jpcl:2012-10)</sup> method. Available as of VASP.5.3.5. |
| 4 | pairwise | [dDsC dispersion correction](../methods/DDsC_dispersion_correction.md)<sup>[\[11\]](#cite_note-steinmann:jcp:11-11)[\[12\]](#cite_note-steinmann:jctc:11-12)</sup> method. Available as of VASP.5.4.1. |
| 2 or 20 | pairwise | [Tkatchenko-Scheffler method](../methods/Tkatchenko-Scheffler_method.md).<sup>[\[13\]](#cite_note-tkatchenko:prl:09-13)</sup> Available as of VASP.5.3.3. |
| 21 | pairwise | [Tkatchenko-Scheffler method with iterative Hirshfeld partitioning](../methods/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md).<sup>[\[14\]](#cite_note-bucko:jctc:13-14)[\[15\]](#cite_note-bucko:jcp:14-15)</sup> Available as of VASP.5.3.5. |
| 202 | many-body | [Many-body dispersion energy](../methods/Many-body_dispersion_energy.md) method (MBD@rsSCS).<sup>[\[16\]](#cite_note-tkatchenko:prl:12-16)[\[17\]](#cite_note-ambrosetti:jcp:14-17)</sup> Available as of VASP.5.4.1. |
| 263 | many-body | [Many-body dispersion energy with fractionally ionic model for polarizability](../methods/Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md) method (MBD@rSC/FI).<sup>[\[18\]](#cite_note-gould:jctc:2016_a-18)[\[19\]](#cite_note-gould:jctc:2016_b-19)</sup> Available as of VASP.6.1.0. |
| 14 | pairwise and many-body | One of the methods available in the library [libMBD](LIBMBD_METHOD.md) of many-body dispersion methods.<sup>[\[20\]](#cite_note-libmbd_1-20)[\[21\]](#cite_note-libmbd_2-21)[\[22\]](#cite_note-hermann:jcp:2023-22)</sup> Available as of VASP.6.4.3 as [external package](../misc/Makefile.include.md). |

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>The <a href="/wiki/LIBMBD_METHOD" title="LIBMBD METHOD">libMBD</a>
implementations (<span class="mw-selflink selflink">IVDW</span>=14) of
the Tkatchenko-Scheffler methods and their MBD extensions are much
faster (analytical calculation of the forces) than the VASP
implementations (numerical calculation of the forces). Therefore, it is
strongly recommended to use the <a href="/wiki/LIBMBD_METHOD"
title="LIBMBD METHOD">libMBD</a> implementation if available.</li>
<li>The parameter <a href="/wiki/LVDW" class="mw-redirect"
title="LVDW">LVDW</a> used in previous versions of VASP (5.2.11 and
later) to activate the <a href="/wiki/DFT-D2" title="DFT-D2">DFT-D2</a>
method is now obsolete. If <a href="/wiki/LVDW" class="mw-redirect"
title="LVDW">LVDW</a>=<em>.TRUE.</em> is defined, <span
class="mw-selflink selflink">IVDW</span> is automatically set to 1
(unless <span class="mw-selflink selflink">IVDW</span> is specified in
<a href="/wiki/INCAR" title="INCAR">INCAR</a>).</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=IVDW&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[DFT-D2](../methods/DFT-D2.md), [DFT-D3](../methods/DFT-D3.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md),
[DFT-D4](../methods/DFT-D4.md), [Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
[Self-consistent screening in Tkatchenko-Scheffler
method](../methods/Self-consistent_screening_in_Tkatchenko-Scheffler_method.md),
[Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](../methods/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
[Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md),
[Many-body dispersion energy with fractionally ionic model for
polarizability](../methods/Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md),
[DFT-ulg](../methods/DFT-ulg.md), [dDsC dispersion
correction](../methods/DDsC_dispersion_correction.md),
[LIBMBD_METHOD](LIBMBD_METHOD.md)

See also the alternative vdW-DF functionals:
[LUSE_VDW](LUSE_VDW.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md).

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IVDW-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=IVDW&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-grimme:jcc:06_1-0)
    <a href="https://doi.org/10.1002/jcc.20495" class="external text"
    rel="nofollow">S. Grimme, J. Comput. Chem. <strong>27</strong>, 1787
    (2006).</a>
2.  [↑](#cite_ref-grimme:jcp:10_2-0)
    <a href="https://doi.org/10.1063/1.3382344" class="external text"
    rel="nofollow">S. Grimme, J. Antony, S. Ehrlich, and S. Krieg, J. Chem.
    Phys. <strong>132</strong>, 154104 (2010).</a>
3.  [↑](#cite_ref-grimme:jcc:11_3-0)
    <a href="https://doi.org/10.1002/jcc.21759" class="external text"
    rel="nofollow">S. Grimme, S. Ehrlich, and L. Goerigk, J. Comput. Chem.
    <strong>32</strong>, 1456 (2011).</a>
4.  [↑](#cite_ref-ehlert:joss:2024_4-0)
    <a href="https://doi.org/10.21105/joss.07169" class="external text"
    rel="nofollow">S. Ehlert, <em>Simple dft-d3: library first
    implementation of the d3 dispersion correction</em>, J. Open Source
    Softw. <strong>9</strong>, 7169 (2024).</a>
5.  [↑](#cite_ref-sdftd3_1_5-0)
    <a href="https://dftd3.readthedocs.io/" class="external text"
    rel="nofollow">https://dftd3.readthedocs.io</a>
6.  [↑](#cite_ref-sdftd3_2_6-0)
    <a href="https://github.com/dftd3/" class="external text"
    rel="nofollow">https://github.com/dftd3</a>
7.  [↑](#cite_ref-caldeweyher:jcp:2019_7-0)
    <a href="https://doi.org/10.1063/1.5090222" class="external text"
    rel="nofollow">E. Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S.
    Spicher, C. Bannwarth, and S. Grimme, J. Chem. Phys.
    <strong>150</strong>, 154122 (2019).</a>
8.  [↑](#cite_ref-dftd4_1_8-0)
    <a href="https://dftd4.readthedocs.io/" class="external text"
    rel="nofollow">https://dftd4.readthedocs.io</a>
9.  [↑](#cite_ref-dftd4_2_9-0)
    <a href="https://github.com/dftd4/" class="external text"
    rel="nofollow">https://github.com/dftd4</a>
10. [↑](#cite_ref-kim:jpcl:2012_10-0)
    <a href="https://doi.org/10.1021/jz2016395" class="external text"
    rel="nofollow">H. Kim, J.-M. Choi, and W. A. Goddard, III, J. Phys.
    Chem. Lett. <strong>3</strong>, 360 (2012).</a>
11. [↑](#cite_ref-steinmann:jcp:11_11-0)
    <a href="https://doi.org/10.1063/1.3545985" class="external text"
    rel="nofollow">S. N. Steinmann and C. Corminboeuf, J. Chem. Phys.
    <strong>134</strong>, 044117 (2011).</a>
12. [↑](#cite_ref-steinmann:jctc:11_12-0)
    <a href="https://doi.org/10.1021/ct200602x" class="external text"
    rel="nofollow">S. N. Steinmann and C. Corminboeuf, J. Chem. Theory
    Comput. <strong>7</strong>, 3567 (2011).</a>
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
16. [↑](#cite_ref-tkatchenko:prl:12_16-0)
    <a href="https://doi.org/10.1103/PhysRevLett.108.236402"
    class="external text" rel="nofollow">A. Tkatchenko, R. A. DiStasio, Jr.,
    R. Car, and M. Scheffler, Phys. Rev. Lett. <strong>108</strong>, 236402
    (2012).</a>
17. [↑](#cite_ref-ambrosetti:jcp:14_17-0)
    <a href="https://doi.org/10.1063/1.4865104" class="external text"
    rel="nofollow">A. Ambrosetti, A. M. Reilly, and R. A. DiStasio Jr., J.
    Chem. Phys. <strong>140</strong>, 018A508 (2014).</a>
18. [↑](#cite_ref-gould:jctc:2016_a_18-0)
    <a href="https://doi.org/10.1021/acs.jctc.6b00361" class="external text"
    rel="nofollow">T. Gould and T. Bučko, <em>C6 Coefficients and Dipole
    Polarizabilities for All Atoms and Many Ions in Rows 1–6 of the Periodic
    Table</em>, J. Chem. Theory Comput. <strong>12</strong>, 3603
    (2016).</a>
19. [↑](#cite_ref-gould:jctc:2016_b_19-0)
    <a href="https://doi.org/10.1021/acs.jctc.6b00925" class="external text"
    rel="nofollow">T. Gould, S. Lebègue, J. G. Ángyán, and T. Bučko, <em>A
    Fractionally Ionic Approach to Polarizability and van der Waals
    Many-Body Dispersion Calculations</em>, J. Chem. Theory Comput.
    <strong>12</strong>, 5920 (2016).</a>
20. [↑](#cite_ref-libmbd_1_20-0)
    <a href="https://libmbd.github.io/" class="external text"
    rel="nofollow">https://libmbd.github.io/</a>
21. [↑](#cite_ref-libmbd_2_21-0)
    <a href="https://github.com/libmbd/" class="external text"
    rel="nofollow">https://github.com/libmbd/</a>
22. [↑](#cite_ref-hermann:jcp:2023_22-0)
    <a href="https://doi.org/10.1063/5.0170972" class="external text"
    rel="nofollow">J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi,
    R. J. Maurer, and A. Tkatchenko, <em>libMBD: A general-purpose package
    for scalable quantum many-body dispersion calculations</em>, J. Chem.
    Phys. <strong>159</strong>, 174802 (2023).</a>


------------------------------------------------------------------------



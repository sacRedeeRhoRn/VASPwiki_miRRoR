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
| 1 or 10 | pairwise | [DFT-D2](../methods/DFT-D2.md) method of Grimme.[^grimme:jcc:06-1] Available as of VASP.5.2.11. |
| 11 | pairwise | [DFT-D3](../methods/DFT-D3.md) method of Grimme with zero-damping function.[^grimme:jcp:10-2] Available as of VASP.5.3.4. |
| 12 | pairwise | [DFT-D3](../methods/DFT-D3.md) method with Becke-Johnson damping function.[^grimme:jcc:11-3] Available as of VASP.5.3.4. |
| 15 | pairwise | DFT-D3 methods available in the [simple-DFT-D3](../methods/Simple-DFT-D3.md) library.[^ehlert:joss:2024-4][^sdftd3_1-5][^sdftd3_2-6] Available as of VASP.6.6.0 as [external package](../misc/Makefile.include.md). |
| 13 | pairwise | [DFT-D4](../methods/DFT-D4.md) method.[^caldeweyher:jcp:2019-7][^dftd4_1-8][^dftd4_2-9] Available as of VASP.6.2 as [external package](../misc/Makefile.include.md). |
| 3 | pairwise | [DFT-ulg](../methods/DFT-ulg.md)[^kim:jpcl:2012-10] method. Available as of VASP.5.3.5. |
| 4 | pairwise | [dDsC dispersion correction](../methods/DDsC_dispersion_correction.md)[^steinmann:jcp:11-11][^steinmann:jctc:11-12] method. Available as of VASP.5.4.1. |
| 2 or 20 | pairwise | [Tkatchenko-Scheffler method](../methods/Tkatchenko-Scheffler_method.md).[^tkatchenko:prl:09-13] Available as of VASP.5.3.3. |
| 21 | pairwise | [Tkatchenko-Scheffler method with iterative Hirshfeld partitioning](../methods/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md).[^bucko:jctc:13-14][^bucko:jcp:14-15] Available as of VASP.5.3.5. |
| 202 | many-body | [Many-body dispersion energy](../methods/Many-body_dispersion_energy.md) method (MBD@rsSCS).[^tkatchenko:prl:12-16][^ambrosetti:jcp:14-17] Available as of VASP.5.4.1. |
| 263 | many-body | [Many-body dispersion energy with fractionally ionic model for polarizability](../methods/Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md) method (MBD@rSC/FI).[^gould:jctc:2016_a-18][^gould:jctc:2016_b-19] Available as of VASP.6.1.0. |
| 14 | pairwise and many-body | One of the methods available in the library [libMBD](LIBMBD_METHOD.md) of many-body dispersion methods.[^libmbd_1-20][^libmbd_2-21][^hermann:jcp:2023-22] Available as of VASP.6.4.3 as [external package](../misc/Makefile.include.md). |

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
------------------------------------------------------------------------

[^grimme:jcc:06-1]: [S. Grimme, J. Comput. Chem. **27**, 1787 (2006).](https://doi.org/10.1002/jcc.20495)
[^grimme:jcp:10-2]: [S. Grimme, J. Antony, S. Ehrlich, and S. Krieg, J. Chem. Phys. **132**, 154104 (2010).](https://doi.org/10.1063/1.3382344)
[^grimme:jcc:11-3]: [S. Grimme, S. Ehrlich, and L. Goerigk, J. Comput. Chem. **32**, 1456 (2011).](https://doi.org/10.1002/jcc.21759)
[^ehlert:joss:2024-4]: [S. Ehlert, *Simple dft-d3: library first implementation of the d3 dispersion correction*, J. Open Source Softw. **9**, 7169 (2024).](https://doi.org/10.21105/joss.07169)
[^sdftd3_1-5]: [https://dftd3.readthedocs.io](https://dftd3.readthedocs.io/)
[^sdftd3_2-6]: [https://github.com/dftd3](https://github.com/dftd3/)
[^caldeweyher:jcp:2019-7]: [E. Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, and S. Grimme, J. Chem. Phys. **150**, 154122 (2019).](https://doi.org/10.1063/1.5090222)
[^dftd4_1-8]: [https://dftd4.readthedocs.io](https://dftd4.readthedocs.io/)
[^dftd4_2-9]: [https://github.com/dftd4](https://github.com/dftd4/)
[^kim:jpcl:2012-10]: [H. Kim, J.-M. Choi, and W. A. Goddard, III, J. Phys. Chem. Lett. **3**, 360 (2012).](https://doi.org/10.1021/jz2016395)
[^steinmann:jcp:11-11]: [S. N. Steinmann and C. Corminboeuf, J. Chem. Phys. **134**, 044117 (2011).](https://doi.org/10.1063/1.3545985)
[^steinmann:jctc:11-12]: [S. N. Steinmann and C. Corminboeuf, J. Chem. Theory Comput. **7**, 3567 (2011).](https://doi.org/10.1021/ct200602x)
[^tkatchenko:prl:09-13]: [A. Tkatchenko and M. Scheffler, Phys. Rev. Lett. **102**, 073005 (2009).](https://doi.org/10.1103/PhysRevLett.102.073005)
[^bucko:jctc:13-14]: [T. Bučko, S. Lebègue, J. Hafner, and J. G. Ángyán, J. Chem. Theory Comput. **9**, 4293 (2013)](https://doi.org/10.1021/ct400694h)
[^bucko:jcp:14-15]: [T. Bučko, S. Lebègue, J. G. Ángyán, and J. Hafner, J. Chem. Phys. **141**, 034114 (2014).](https://doi.org/10.1063/1.4890003)
[^tkatchenko:prl:12-16]: [A. Tkatchenko, R. A. DiStasio, Jr., R. Car, and M. Scheffler, Phys. Rev. Lett. **108**, 236402 (2012).](https://doi.org/10.1103/PhysRevLett.108.236402)
[^ambrosetti:jcp:14-17]: [A. Ambrosetti, A. M. Reilly, and R. A. DiStasio Jr., J. Chem. Phys. **140**, 018A508 (2014).](https://doi.org/10.1063/1.4865104)
[^gould:jctc:2016_a-18]: [T. Gould and T. Bučko, *C6 Coefficients and Dipole Polarizabilities for All Atoms and Many Ions in Rows 1–6 of the Periodic Table*, J. Chem. Theory Comput. **12**, 3603 (2016).](https://doi.org/10.1021/acs.jctc.6b00361)
[^gould:jctc:2016_b-19]: [T. Gould, S. Lebègue, J. G. Ángyán, and T. Bučko, *A Fractionally Ionic Approach to Polarizability and van der Waals Many-Body Dispersion Calculations*, J. Chem. Theory Comput. **12**, 5920 (2016).](https://doi.org/10.1021/acs.jctc.6b00925)
[^libmbd_1-20]: [https://libmbd.github.io/](https://libmbd.github.io/)
[^libmbd_2-21]: [https://github.com/libmbd/](https://github.com/libmbd/)
[^hermann:jcp:2023-22]: [J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko, *libMBD: A general-purpose package for scalable quantum many-body dispersion calculations*, J. Chem. Phys. **159**, 174802 (2023).](https://doi.org/10.1063/5.0170972)

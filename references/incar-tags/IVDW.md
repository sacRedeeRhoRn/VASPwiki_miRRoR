<!-- Source: https://vasp.at/wiki/index.php/IVDW | revid: 34375 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IVDW
IVDW = \[integer\] 

|                   |     |                 |
|-------------------|-----|-----------------|
| Default: **IVDW** | = 0 | (no correction) |

Description: IVDW specifies a vdW dispersion term of the atom-pairwise
or many-body type.

------------------------------------------------------------------------

## Available vdW atom-pairwise and many-body methods
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
| 1 or 10 | pairwise | [DFT-D2](../methods/DFT-D2.md) method of Grimme.^([\[1\]](#cite_note-grimme:jcc:06-1)) Available as of VASP.5.2.11. |
| 11 | pairwise | [DFT-D3](../methods/DFT-D3.md) method of Grimme with zero-damping function.^([\[2\]](#cite_note-grimme:jcp:10-2)) Available as of VASP.5.3.4. |
| 12 | pairwise | [DFT-D3](../methods/DFT-D3.md) method with Becke-Johnson damping function.^([\[3\]](#cite_note-grimme:jcc:11-3)) Available as of VASP.5.3.4. |
| 15 | pairwise | DFT-D3 methods available in the [simple-DFT-D3](../methods/Simple-DFT-D3.md) library.^([\[4\]](#cite_note-ehlert:joss:2024-4)[\[5\]](#cite_note-sdftd3_1-5)[\[6\]](#cite_note-sdftd3_2-6)) Available as of VASP.6.6.0 as [external package](../misc/Makefile.include.md). |
| 13 | pairwise | [DFT-D4](../methods/DFT-D4.md) method.^([\[7\]](#cite_note-caldeweyher:jcp:2019-7)[\[8\]](#cite_note-dftd4_1-8)[\[9\]](#cite_note-dftd4_2-9)) Available as of VASP.6.2 as [external package](../misc/Makefile.include.md). |
| 3 | pairwise | [DFT-ulg](../methods/DFT-ulg.md)^([\[10\]](#cite_note-kim:jpcl:2012-10)) method. Available as of VASP.5.3.5. |
| 4 | pairwise | [dDsC dispersion correction](../methods/DDsC_dispersion_correction.md)^([\[11\]](#cite_note-steinmann:jcp:11-11)[\[12\]](#cite_note-steinmann:jctc:11-12)) method. Available as of VASP.5.4.1. |
| 2 or 20 | pairwise | [Tkatchenko-Scheffler method](../methods/Tkatchenko-Scheffler_method.md).^([\[13\]](#cite_note-tkatchenko:prl:09-13)) Available as of VASP.5.3.3. |
| 21 | pairwise | [Tkatchenko-Scheffler method with iterative Hirshfeld partitioning](../methods/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md).^([\[14\]](#cite_note-bucko:jctc:13-14)[\[15\]](#cite_note-bucko:jcp:14-15)) Available as of VASP.5.3.5. |
| 202 | many-body | [Many-body dispersion energy](../methods/Many-body_dispersion_energy.md) method (MBD@rsSCS).^([\[16\]](#cite_note-tkatchenko:prl:12-16)[\[17\]](#cite_note-ambrosetti:jcp:14-17)) Available as of VASP.5.4.1. |
| 263 | many-body | [Many-body dispersion energy with fractionally ionic model for polarizability](../methods/Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md) method (MBD@rSC/FI).^([\[18\]](#cite_note-gould:jctc:2016_a-18)[\[19\]](#cite_note-gould:jctc:2016_b-19)) Available as of VASP.6.1.0. |
| 14 | pairwise and many-body | One of the methods available in the library [libMBD](LIBMBD_METHOD.md) of many-body dispersion methods.^([\[20\]](#cite_note-libmbd_1-20)[\[21\]](#cite_note-libmbd_2-21)[\[22\]](#cite_note-hermann:jcp:2023-22)) Available as of VASP.6.4.3 as [external package](../misc/Makefile.include.md). |

[TABLE]

## Related tags and articles
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

## References
1.  [↑](#cite_ref-grimme:jcc:06_1-0) [S. Grimme, J. Comput. Chem.
    **27**, 1787 (2006).](https://doi.org/10.1002/jcc.20495)
2.  [↑](#cite_ref-grimme:jcp:10_2-0) [S. Grimme, J. Antony, S. Ehrlich,
    and S. Krieg, J. Chem. Phys. **132**, 154104
    (2010).](https://doi.org/10.1063/1.3382344)
3.  [↑](#cite_ref-grimme:jcc:11_3-0) [S. Grimme, S. Ehrlich, and L.
    Goerigk, J. Comput. Chem. **32**, 1456
    (2011).](https://doi.org/10.1002/jcc.21759)
4.  [↑](#cite_ref-ehlert:joss:2024_4-0) [S. Ehlert, *Simple dft-d3:
    library first implementation of the d3 dispersion correction*, J.
    Open Source Softw. **9**, 7169
    (2024).](https://doi.org/10.21105/joss.07169)
5.  [↑](#cite_ref-sdftd3_1_5-0)
    [https://dftd3.readthedocs.io](https://dftd3.readthedocs.io/)
6.  [↑](#cite_ref-sdftd3_2_6-0)
    [https://github.com/dftd3](https://github.com/dftd3/)
7.  [↑](#cite_ref-caldeweyher:jcp:2019_7-0) [E. Caldeweyher, S.
    Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, and S.
    Grimme, J. Chem. Phys. **150**, 154122
    (2019).](https://doi.org/10.1063/1.5090222)
8.  [↑](#cite_ref-dftd4_1_8-0)
    [https://dftd4.readthedocs.io](https://dftd4.readthedocs.io/)
9.  [↑](#cite_ref-dftd4_2_9-0)
    [https://github.com/dftd4](https://github.com/dftd4/)
10. [↑](#cite_ref-kim:jpcl:2012_10-0) [H. Kim, J.-M. Choi, and W. A.
    Goddard, III, J. Phys. Chem. Lett. **3**, 360
    (2012).](https://doi.org/10.1021/jz2016395)
11. [↑](#cite_ref-steinmann:jcp:11_11-0) [S. N. Steinmann and C.
    Corminboeuf, J. Chem. Phys. **134**, 044117
    (2011).](https://doi.org/10.1063/1.3545985)
12. [↑](#cite_ref-steinmann:jctc:11_12-0) [S. N. Steinmann and C.
    Corminboeuf, J. Chem. Theory Comput. **7**, 3567
    (2011).](https://doi.org/10.1021/ct200602x)
13. [↑](#cite_ref-tkatchenko:prl:09_13-0) [A. Tkatchenko and M.
    Scheffler, Phys. Rev. Lett. **102**, 073005
    (2009).](https://doi.org/10.1103/PhysRevLett.102.073005)
14. [↑](#cite_ref-bucko:jctc:13_14-0) [T. Bučko, S. Lebègue, J. Hafner,
    and J. G. Ángyán, J. Chem. Theory Comput. **9**, 4293
    (2013)](https://doi.org/10.1021/ct400694h)
15. [↑](#cite_ref-bucko:jcp:14_15-0) [T. Bučko, S. Lebègue, J. G.
    Ángyán, and J. Hafner, J. Chem. Phys. **141**, 034114
    (2014).](https://doi.org/10.1063/1.4890003)
16. [↑](#cite_ref-tkatchenko:prl:12_16-0) [A. Tkatchenko, R. A.
    DiStasio, Jr., R. Car, and M. Scheffler, Phys. Rev. Lett. **108**,
    236402 (2012).](https://doi.org/10.1103/PhysRevLett.108.236402)
17. [↑](#cite_ref-ambrosetti:jcp:14_17-0) [A. Ambrosetti, A. M. Reilly,
    and R. A. DiStasio Jr., J. Chem. Phys. **140**, 018A508
    (2014).](https://doi.org/10.1063/1.4865104)
18. [↑](#cite_ref-gould:jctc:2016_a_18-0) [T. Gould and T. Bučko, *C6
    Coefficients and Dipole Polarizabilities for All Atoms and Many Ions
    in Rows 1–6 of the Periodic Table*, J. Chem. Theory Comput. **12**,
    3603 (2016).](https://doi.org/10.1021/acs.jctc.6b00361)
19. [↑](#cite_ref-gould:jctc:2016_b_19-0) [T. Gould, S. Lebègue, J. G.
    Ángyán, and T. Bučko, *A Fractionally Ionic Approach to
    Polarizability and van der Waals Many-Body Dispersion
    Calculations*, J. Chem. Theory Comput. **12**, 5920
    (2016).](https://doi.org/10.1021/acs.jctc.6b00925)
20. [↑](#cite_ref-libmbd_1_20-0)
    [https://libmbd.github.io/](https://libmbd.github.io/)
21. [↑](#cite_ref-libmbd_2_21-0)
    [https://github.com/libmbd/](https://github.com/libmbd/)
22. [↑](#cite_ref-hermann:jcp:2023_22-0) [J. Hermann, M. Stöhr, S.
    Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko,
    *libMBD: A general-purpose package for scalable quantum many-body
    dispersion calculations*, J. Chem. Phys. **159**, 174802
    (2023).](https://doi.org/10.1063/5.0170972)

------------------------------------------------------------------------

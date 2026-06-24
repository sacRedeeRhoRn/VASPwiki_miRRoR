<!-- Source: https://vasp.at/wiki/index.php/Category:Van_der_Waals_functionals | revid: 34494 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Van der Waals functionals
The semilocal (SL) and hybrid exchange-correlation functionals do not
include the London dispersion forces. Therefore, they can not be applied
reliably on systems where the London dispersion forces play an important
role. To account more properly for the London dispersion forces in DFT,
a correlation dispersion term can be added to the semilocal or hybrid
functional.^([\[1\]](#cite_note-grimme:cr:2016-1)[\[2\]](#cite_note-hermann:cr:2017-2))
This leads to the so-called **van der Waals functionals**:

$E_{\text{xc}}^{\text{vdW}} =
E_{\text{xc}}^{\text{SL/hybrid}} + E_{\text{c,disp}}.$

There are essentially three types of dispersion terms
$E_{\text{c,disp}}$ that are available
in VASP, and a brief sketch of them is given below along with links to
pages that provide more detail. Note that
[libMBD](../incar-tags/LIBMBD_METHOD.md) is an external package
that provides the Tkatchenko-Scheffler atom-pairwise methods and their
many-body dispersion extensions.

## Contents

- [1 Types of approximations](#Types_of_approximations)
  - [1.1 Atom-pairwise methods](#Atom-pairwise_methods)
  - [1.2 Many-body dispersion methods](#Many-body_dispersion_methods)
  - [1.3 Nonlocal vdW-DF functionals](#Nonlocal_vdW-DF_functionals)
- [2 References](#References)

## Types of approximations
### Atom-pairwise methods
[![](https://vasp.at/wiki/images/thumb/9/95/Dft%2Bd.png/300px-Dft%2Bd.png)](https://vasp.at/wiki/File:Dft%2Bd.png)

Dipole-dipole interactions between atoms (black dots) and
quadrupole-dipole interactions (purple arrows). All of these terms are
pairwise. Adapted from Fig. 2 in Ref.
^([\[2\]](#cite_note-hermann:cr:2017-2)).

They consist of a sum over the atoms pairs $A$-$B$:

$E_{\text{c,disp}} =
-\sum_{A<B}\sum_{n=6,8,10,\ldots}f_{n}^{\text{damp}}(R_{AB})\frac{C_{n}^{AB}}{R_{AB}^{n}},$

where $C_{n}^{AB}$ are the dispersion
coefficients, $R_{AB}$ is the distance
between atoms $A$ and
$B$, and $f_{n}^{\text{damp}}$ is a damping function. Several variants
of such atom-pair corrections exist and the most popular of them, listed
below, are available in VASP and are selected with the
[IVDW](../incar-tags/IVDW.md) tag.

- [DFT-D2](DFT-D2.md)^([\[3\]](#cite_note-grimme:jcc:06-3))
- [DFT-D3](DFT-D3.md)^([\[4\]](#cite_note-grimme:jcp:10-4)[\[5\]](#cite_note-grimme:jcc:11-5))
- [simple-DFT-D3](Simple-DFT-D3.md)^([\[6\]](#cite_note-ehlert:joss:2024-6)[\[7\]](#cite_note-sdftd3_1-7)[\[8\]](#cite_note-sdftd3_2-8))
  (available as of VASP.6.6.0 as [external
  package](../misc/Makefile.include.md))
- [DFT-D4](DFT-D4.md)^([\[9\]](#cite_note-caldeweyher:jcp:2019-9)[\[10\]](#cite_note-dftd4_1-10)[\[11\]](#cite_note-dftd4_2-11))
  (available as of VASP.6.2 as [external
  package](../misc/Makefile.include.md))
- [DFT-ulg](DFT-ulg.md)^([\[12\]](#cite_note-kim:jpcl:2012-12))
- [Tkatchenko-Scheffler
  method](Tkatchenko-Scheffler_method.md)^([\[13\]](#cite_note-tkatchenko:prl:09-13))
- [Tkatchenko-Scheffler method with iterative Hirshfeld
  partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md)^([\[14\]](#cite_note-bucko:jctc:13-14)[\[15\]](#cite_note-bucko:jcp:14-15))
- [Self-consistent screening in Tkatchenko-Scheffler
  method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md)^([\[16\]](#cite_note-tkatchenko:prl:12-16))
- [Library libMBD of many-body dispersion
  methods](../incar-tags/LIBMBD_METHOD.md)^([\[17\]](#cite_note-libmbd_1-17)[\[18\]](#cite_note-libmbd_2-18)[\[19\]](#cite_note-hermann:jcp:2023-19))
  (available as of VASP.6.4.3 as [external
  package](../misc/Makefile.include.md))
- [DDsC dispersion
  correction](DDsC_dispersion_correction.md)^([\[20\]](#cite_note-steinmann:jcp:11-20)[\[21\]](#cite_note-steinmann:jctc:11-21))

### Many-body dispersion methods
[![](https://vasp.at/wiki/images/thumb/0/0c/Mbd.png/300px-Mbd.png)](https://vasp.at/wiki/File:Mbd.png)

Dipole-dipole interactions between atoms (black dots) in many-body
dispersions include the previously considered 2-body (pairwise) terms
shown with purple arrows, in addition to the 3-, 4-, N-body dipole
interaction terms shown with green arrows. Adapted from Fig. 2 in Ref.
^([\[2\]](#cite_note-hermann:cr:2017-2)).

These methods are based on the random-phase expression for the
correlation energy, which is expressed as an integral over the frequency
$\omega$ involving the
frequency-dependent polarizability ${\mathbf{A}}_{LR}$:

$E_{\mathrm{c,disp}} =
-\int_{\mathrm{FBZ}}\frac{d{\mathbf{k}}}{v_{\mathrm{FBZ}}}
\int_0^{\infty} {\frac{d\omega}{2\pi}} \\ {\mathrm{Tr}}\left \\
\mathrm{ln} \left ({\mathbf{1}}-{\mathbf{A}}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}}) \right ) \right \\.$

These methods, listed below, are selected with the
[IVDW](../incar-tags/IVDW.md) tag.

- [Many-body dispersion
  energy](Many-body_dispersion_energy.md)^([\[16\]](#cite_note-tkatchenko:prl:12-16)[\[22\]](#cite_note-ambrosetti:jcp:14-22))
- [Many-body dispersion energy with fractionally ionic model for
  polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)^([\[23\]](#cite_note-gould:jctc:2016_a-23)[\[24\]](#cite_note-gould:jctc:2016_b-24))
- [Library libMBD of many-body dispersion
  methods](../incar-tags/LIBMBD_METHOD.md)^([\[17\]](#cite_note-libmbd_1-17)[\[18\]](#cite_note-libmbd_2-18)[\[19\]](#cite_note-hermann:jcp:2023-19))

### Nonlocal vdW-DF functionals
[![](https://vasp.at/wiki/images/thumb/7/74/Non_local_dft.png/300px-Non_local_dft.png)](https://vasp.at/wiki/File:Non_local_dft.png)

Nonlocal DFT interaction (purple arrows) between pairwise dipole
fluctuations in the density. Adapted from Fig. 2 in Ref.
^([\[2\]](#cite_note-hermann:cr:2017-2)).

These are density functionals that require a double spatial integration
and are, therefore, nonlocal:

$E_{\text{c,disp}} = \frac{1}{2}\int\int
n(\textbf{r}) \Phi\left(\textbf{r},\textbf{r}'\right) n(\textbf{r}')
d^{3}rd^{3}r',$

where the kernel $\Phi$ depends on the
electronic density $n$, its derivative
$\nabla n$ as well as on the
interelectronic distance $\left\vert\bf{r}-\bf{r}'\right\vert$. The nonlocal functionals
are more expensive to calculate than semilocal functionals, however,
they are efficiently implemented by using FFTs
^([\[25\]](#cite_note-romanperez:prl:09-25)). These methods are selected
with the [LUSE_VDW](../incar-tags/LUSE_VDW.md) and
[IVDW_NL](../incar-tags/IVDW_NL.md) tags.

- [Nonlocal vdW-DF
  functionals](Nonlocal_vdW-DF_functionals.md)

## References
1.  [↑](#cite_ref-grimme:cr:2016_1-0) [S. Grimme, A. hansen, J. G.
    Brandenburg, and C. Bannwarth, *Dispersion-Corrected Mean-Field
    Electronic Structure Methods*, Chem. Rev. **116**, 5105
    (2016).](https://doi.org/10.1021/acs.chemrev.5b00533)
2.  ↑ ^([a](#cite_ref-hermann:cr:2017_2-0))
    ^([b](#cite_ref-hermann:cr:2017_2-1))
    ^([c](#cite_ref-hermann:cr:2017_2-2))
    ^([d](#cite_ref-hermann:cr:2017_2-3)) [J. Hermann, R. A. DiStasio
    Jr., and A. Tkatchenko, *First-Principles Models for van der Waals
    Interactions in Molecules and Materials: Concepts, Theory, and
    Applications*, Chem. Rev. **117**, 4714
    (2017).](https://doi.org/10.1021/acs.chemrev.6b00446)
3.  [↑](#cite_ref-grimme:jcc:06_3-0) [S. Grimme, J. Comput. Chem.
    **27**, 1787 (2006).](https://doi.org/10.1002/jcc.20495)
4.  [↑](#cite_ref-grimme:jcp:10_4-0) [S. Grimme, J. Antony, S. Ehrlich,
    and S. Krieg, J. Chem. Phys. **132**, 154104
    (2010).](https://doi.org/10.1063/1.3382344)
5.  [↑](#cite_ref-grimme:jcc:11_5-0) [S. Grimme, S. Ehrlich, and L.
    Goerigk, J. Comput. Chem. **32**, 1456
    (2011).](https://doi.org/10.1002/jcc.21759)
6.  [↑](#cite_ref-ehlert:joss:2024_6-0) [S. Ehlert, *Simple dft-d3:
    library first implementation of the d3 dispersion correction*, J.
    Open Source Softw. **9**, 7169
    (2024).](https://doi.org/10.21105/joss.07169)
7.  [↑](#cite_ref-sdftd3_1_7-0)
    [https://dftd3.readthedocs.io](https://dftd3.readthedocs.io/)
8.  [↑](#cite_ref-sdftd3_2_8-0)
    [https://github.com/dftd3](https://github.com/dftd3/)
9.  [↑](#cite_ref-caldeweyher:jcp:2019_9-0) [E. Caldeweyher, S.
    Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, and S.
    Grimme, J. Chem. Phys. **150**, 154122
    (2019).](https://doi.org/10.1063/1.5090222)
10. [↑](#cite_ref-dftd4_1_10-0)
    [https://dftd4.readthedocs.io](https://dftd4.readthedocs.io/)
11. [↑](#cite_ref-dftd4_2_11-0)
    [https://github.com/dftd4](https://github.com/dftd4/)
12. [↑](#cite_ref-kim:jpcl:2012_12-0) [H. Kim, J.-M. Choi, and W. A.
    Goddard, III, J. Phys. Chem. Lett. **3**, 360
    (2012).](https://doi.org/10.1021/jz2016395)
13. [↑](#cite_ref-tkatchenko:prl:09_13-0) [A. Tkatchenko and M.
    Scheffler, Phys. Rev. Lett. **102**, 073005
    (2009).](https://doi.org/10.1103/PhysRevLett.102.073005)
14. [↑](#cite_ref-bucko:jctc:13_14-0) [T. Bučko, S. Lebègue, J. Hafner,
    and J. G. Ángyán, J. Chem. Theory Comput. **9**, 4293
    (2013)](https://doi.org/10.1021/ct400694h)
15. [↑](#cite_ref-bucko:jcp:14_15-0) [T. Bučko, S. Lebègue, J. G.
    Ángyán, and J. Hafner, J. Chem. Phys. **141**, 034114
    (2014).](https://doi.org/10.1063/1.4890003)
16. ↑ ^([a](#cite_ref-tkatchenko:prl:12_16-0))
    ^([b](#cite_ref-tkatchenko:prl:12_16-1)) [A. Tkatchenko, R. A.
    DiStasio, Jr., R. Car, and M. Scheffler, Phys. Rev. Lett. **108**,
    236402 (2012).](https://doi.org/10.1103/PhysRevLett.108.236402)
17. ↑ ^([a](#cite_ref-libmbd_1_17-0)) ^([b](#cite_ref-libmbd_1_17-1))
    [https://libmbd.github.io/](https://libmbd.github.io/)
18. ↑ ^([a](#cite_ref-libmbd_2_18-0)) ^([b](#cite_ref-libmbd_2_18-1))
    [https://github.com/libmbd/](https://github.com/libmbd/)
19. ↑ ^([a](#cite_ref-hermann:jcp:2023_19-0))
    ^([b](#cite_ref-hermann:jcp:2023_19-1)) [J. Hermann, M. Stöhr, S.
    Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko,
    *libMBD: A general-purpose package for scalable quantum many-body
    dispersion calculations*, J. Chem. Phys. **159**, 174802
    (2023).](https://doi.org/10.1063/5.0170972)
20. [↑](#cite_ref-steinmann:jcp:11_20-0) [S. N. Steinmann and C.
    Corminboeuf, J. Chem. Phys. **134**, 044117
    (2011).](https://doi.org/10.1063/1.3545985)
21. [↑](#cite_ref-steinmann:jctc:11_21-0) [S. N. Steinmann and C.
    Corminboeuf, J. Chem. Theory Comput. **7**, 3567
    (2011).](https://doi.org/10.1021/ct200602x)
22. [↑](#cite_ref-ambrosetti:jcp:14_22-0) [A. Ambrosetti, A. M. Reilly,
    and R. A. DiStasio Jr., J. Chem. Phys. **140**, 018A508
    (2014).](https://doi.org/10.1063/1.4865104)
23. [↑](#cite_ref-gould:jctc:2016_a_23-0) [T. Gould and T. Bučko, *C6
    Coefficients and Dipole Polarizabilities for All Atoms and Many Ions
    in Rows 1–6 of the Periodic Table*, J. Chem. Theory Comput. **12**,
    3603 (2016).](https://doi.org/10.1021/acs.jctc.6b00361)
24. [↑](#cite_ref-gould:jctc:2016_b_24-0) [T. Gould, S. Lebègue, J. G.
    Ángyán, and T. Bučko, *A Fractionally Ionic Approach to
    Polarizability and van der Waals Many-Body Dispersion
    Calculations*, J. Chem. Theory Comput. **12**, 5920
    (2016).](https://doi.org/10.1021/acs.jctc.6b00925)
25. [↑](#cite_ref-romanperez:prl:09_25-0) [G. Román-Pérez and J. M.
    Soler, Phys. Rev. Lett. **103**, 096102
    (2009).](https://doi.org/10.1103/PhysRevLett.103.096102)

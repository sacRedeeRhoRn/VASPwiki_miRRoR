<!-- Source: https://vasp.at/wiki/index.php/Category:Van_der_Waals_functionals | revid: 34494 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Van der Waals functionals


The semilocal (SL) and hybrid exchange-correlation functionals do not
include the London dispersion forces. Therefore, they can not be applied
reliably on systems where the London dispersion forces play an important
role. To account more properly for the London dispersion forces in DFT,
a correlation dispersion term can be added to the semilocal or hybrid
functional.[^grimme:cr:2016-1][^hermann:cr:2017-2]
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
pairwise. Adapted from Fig. 2 in Ref. [^hermann:cr:2017-2].</figcaption>
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

- [DFT-D2](DFT-D2.md)[^grimme:jcc:06-3]
- [DFT-D3](DFT-D3.md)[^grimme:jcp:10-4][^grimme:jcc:11-5]
- [simple-DFT-D3](Simple-DFT-D3.md)[^ehlert:joss:2024-6][^sdftd3_1-7][^sdftd3_2-8]
  (available as of VASP.6.6.0 as [external
  package](../misc/Makefile.include.md))
- [DFT-D4](DFT-D4.md)[^caldeweyher:jcp:2019-9][^dftd4_1-10][^dftd4_2-11]
  (available as of VASP.6.2 as [external
  package](../misc/Makefile.include.md))
- [DFT-ulg](DFT-ulg.md)[^kim:jpcl:2012-12]
- [Tkatchenko-Scheffler
  method](Tkatchenko-Scheffler_method.md)[^tkatchenko:prl:09-13]
- [Tkatchenko-Scheffler method with iterative Hirshfeld
  partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md)[^bucko:jctc:13-14][^bucko:jcp:14-15]
- [Self-consistent screening in Tkatchenko-Scheffler
  method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md)[^tkatchenko:prl:12-16]
- [Library libMBD of many-body dispersion
  methods](../incar-tags/LIBMBD_METHOD.md)[^libmbd_1-17][^libmbd_2-18][^hermann:jcp:2023-19]
  (available as of VASP.6.4.3 as [external
  package](../misc/Makefile.include.md))
- [DDsC dispersion
  correction](DDsC_dispersion_correction.md)[^steinmann:jcp:11-20][^steinmann:jctc:11-21]


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
Fig. 2 in Ref. [^hermann:cr:2017-2].</figcaption>
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
  energy](Many-body_dispersion_energy.md)[^tkatchenko:prl:12-16][^ambrosetti:jcp:14-22]
- [Many-body dispersion energy with fractionally ionic model for
  polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)[^gould:jctc:2016_a-23][^gould:jctc:2016_b-24]
- [Library libMBD of many-body dispersion
  methods](../incar-tags/LIBMBD_METHOD.md)[^libmbd_1-17][^libmbd_2-18][^hermann:jcp:2023-19]


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
dipole fluctuations in the density. Adapted from Fig. 2 in Ref. [^hermann:cr:2017-2].</figcaption>
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
[^romanperez:prl:09-25].
These methods are selected with the
[LUSE_VDW](../incar-tags/LUSE_VDW.md) and
[IVDW_NL](../incar-tags/IVDW_NL.md) tags.

- [Nonlocal vdW-DF
  functionals](Nonlocal_vdW-DF_functionals.md)


## References\[<a
href="/wiki/index.php?title=Category:Van_der_Waals_functionals&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^grimme:cr:2016-1]: [S. Grimme, A. hansen, J. G. Brandenburg, and C. Bannwarth, *Dispersion-Corrected Mean-Field Electronic Structure Methods*, Chem. Rev. **116**, 5105 (2016).](https://doi.org/10.1021/acs.chemrev.5b00533)
[^hermann:cr:2017-2]: [J. Hermann, R. A. DiStasio Jr., and A. Tkatchenko, *First-Principles Models for van der Waals Interactions in Molecules and Materials: Concepts, Theory, and Applications*, Chem. Rev. **117**, 4714 (2017).](https://doi.org/10.1021/acs.chemrev.6b00446)
[^grimme:jcc:06-3]: [S. Grimme, J. Comput. Chem. **27**, 1787 (2006).](https://doi.org/10.1002/jcc.20495)
[^grimme:jcp:10-4]: [S. Grimme, J. Antony, S. Ehrlich, and S. Krieg, J. Chem. Phys. **132**, 154104 (2010).](https://doi.org/10.1063/1.3382344)
[^grimme:jcc:11-5]: [S. Grimme, S. Ehrlich, and L. Goerigk, J. Comput. Chem. **32**, 1456 (2011).](https://doi.org/10.1002/jcc.21759)
[^ehlert:joss:2024-6]: [S. Ehlert, *Simple dft-d3: library first implementation of the d3 dispersion correction*, J. Open Source Softw. **9**, 7169 (2024).](https://doi.org/10.21105/joss.07169)
[^sdftd3_1-7]: [https://dftd3.readthedocs.io](https://dftd3.readthedocs.io/)
[^sdftd3_2-8]: [https://github.com/dftd3](https://github.com/dftd3/)
[^caldeweyher:jcp:2019-9]: [E. Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, and S. Grimme, J. Chem. Phys. **150**, 154122 (2019).](https://doi.org/10.1063/1.5090222)
[^dftd4_1-10]: [https://dftd4.readthedocs.io](https://dftd4.readthedocs.io/)
[^dftd4_2-11]: [https://github.com/dftd4](https://github.com/dftd4/)
[^kim:jpcl:2012-12]: [H. Kim, J.-M. Choi, and W. A. Goddard, III, J. Phys. Chem. Lett. **3**, 360 (2012).](https://doi.org/10.1021/jz2016395)
[^tkatchenko:prl:09-13]: [A. Tkatchenko and M. Scheffler, Phys. Rev. Lett. **102**, 073005 (2009).](https://doi.org/10.1103/PhysRevLett.102.073005)
[^bucko:jctc:13-14]: [T. Bučko, S. Lebègue, J. Hafner, and J. G. Ángyán, J. Chem. Theory Comput. **9**, 4293 (2013)](https://doi.org/10.1021/ct400694h)
[^bucko:jcp:14-15]: [T. Bučko, S. Lebègue, J. G. Ángyán, and J. Hafner, J. Chem. Phys. **141**, 034114 (2014).](https://doi.org/10.1063/1.4890003)
[^tkatchenko:prl:12-16]: [A. Tkatchenko, R. A. DiStasio, Jr., R. Car, and M. Scheffler, Phys. Rev. Lett. **108**, 236402 (2012).](https://doi.org/10.1103/PhysRevLett.108.236402)
[^libmbd_1-17]: [https://libmbd.github.io/](https://libmbd.github.io/)
[^libmbd_2-18]: [https://github.com/libmbd/](https://github.com/libmbd/)
[^hermann:jcp:2023-19]: [J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko, *libMBD: A general-purpose package for scalable quantum many-body dispersion calculations*, J. Chem. Phys. **159**, 174802 (2023).](https://doi.org/10.1063/5.0170972)
[^steinmann:jcp:11-20]: [S. N. Steinmann and C. Corminboeuf, J. Chem. Phys. **134**, 044117 (2011).](https://doi.org/10.1063/1.3545985)
[^steinmann:jctc:11-21]: [S. N. Steinmann and C. Corminboeuf, J. Chem. Theory Comput. **7**, 3567 (2011).](https://doi.org/10.1021/ct200602x)
[^ambrosetti:jcp:14-22]: [A. Ambrosetti, A. M. Reilly, and R. A. DiStasio Jr., J. Chem. Phys. **140**, 018A508 (2014).](https://doi.org/10.1063/1.4865104)
[^gould:jctc:2016_a-23]: [T. Gould and T. Bučko, *C6 Coefficients and Dipole Polarizabilities for All Atoms and Many Ions in Rows 1–6 of the Periodic Table*, J. Chem. Theory Comput. **12**, 3603 (2016).](https://doi.org/10.1021/acs.jctc.6b00361)
[^gould:jctc:2016_b-24]: [T. Gould, S. Lebègue, J. G. Ángyán, and T. Bučko, *A Fractionally Ionic Approach to Polarizability and van der Waals Many-Body Dispersion Calculations*, J. Chem. Theory Comput. **12**, 5920 (2016).](https://doi.org/10.1021/acs.jctc.6b00925)
[^romanperez:prl:09-25]: [G. Román-Pérez and J. M. Soler, Phys. Rev. Lett. **103**, 096102 (2009).](https://doi.org/10.1103/PhysRevLett.103.096102)

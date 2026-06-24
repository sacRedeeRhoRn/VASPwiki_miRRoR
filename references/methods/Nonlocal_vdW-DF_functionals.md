<!-- Source: https://vasp.at/wiki/index.php/Nonlocal_vdW-DF_functionals | revid: 36793 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Nonlocal vdW-DF functionals
The vdW-DF method originally proposed by Dion *et
al.*^([\[1\]](#cite_note-dion:prl:2004-1)) consists of a semilocal or
hybrid exchange-correlation functional $E_{\text{xc}}^{\text{SL/hybrid}}$ that is augmented with a
nonlocal correlation functional $E_{\text{c,disp}}$ that approximately accounts for dispersion
interactions:

$E_{\text{xc}}^{\text{vdW}} =
E_{\text{xc}}^{\text{SL/hybrid}} + E_{\text{c,disp}},$

where

$E_{\text{c,disp}} = \frac{1}{2}\int\int
n(\textbf{r}) \Phi\left(\textbf{r},\textbf{r}'\right) n(\textbf{r}')
d^{3}rd^{3}r',$

with a kernel $\Phi$ that depends on the
electronic density $n$, its derivative
$\nabla n$ as well as on the
interelectronic distance $\left\vert\bf{r}-\bf{r}'\right\vert$. In VASP, the calculation
of $E_{\text{c,disp}}$ is done using
the algorithm of Román-Pérez and
Soler^([\[2\]](#cite_note-romanperez:prl:09-2)) that is based on FFTs
and the convolution theorem to calculate efficiently the double
real-space integral. Several versions of the vdW-DF functionals proposed
in the literature can be used (see list below).

The vdW-DF functionals are available since the 5.2.12.26May2011 version
of VASP for the calculation of total energies and forces. The stress
tensor calculation for the cell optimization
([ISIF](../incar-tags/ISIF.md)=3) is available since the VASP
5.2.12.11Nov2011 version for spin-unpolarized systems and VASP 5.3.1 for
spin-polarized systems. They have been implemented by J. Klimeš. If you
make use of the vdW-DF functionals presented in this section, we ask you
to cite Ref. ^([\[3\]](#cite_note-klimes:prb:2011-3)). Please also cite
the original vdW-DF paper of Dion *et
al.*^([\[1\]](#cite_note-dion:prl:2004-1)) and the paper of Román-Pérez
and Soler^([\[2\]](#cite_note-romanperez:prl:09-2)).

In versions of VASP prior to 6.4.0, a meta-GGA functional (e.g., SCAN)
could be combined only with the rVV10 nonlocal functional. Conversely, a
GGA functional could be combined only with the original nonlocal
functional of Dion *et al.*. This restriction is lifted since VASP.6.4.0
thanks to the introduction of the [IVDW_NL](../incar-tags/IVDW_NL.md)
tag. Since VASP.6.4.0, the spin-polarized formulation of the nonlocal
vdW correlation term^([\[4\]](#cite_note-thonhauser:prl:2015-4)) is
available. It can be switched on with the logical tag
[LSPIN_VDW](../incar-tags/LSPIN_VDW.md) (.FALSE. by default), however
its use is limited to the the functional of Dion *et al.* (not available
for rVV10) and only when the nonlocal term is combined with a
[GGA](../incar-tags/GGA.md) functional. In other cases (and in prior versions
of VASP), the nonlocal correlation functional is evaluated with the sum
of the spin-up and spin-down electron densities.

An overview of the performance of the vdW-DF functionals can be found
for instance in Ref.
^([\[3\]](#cite_note-klimes:prb:2011-3)[\[5\]](#cite_note-berland:rpp:2015-5)[\[6\]](#cite_note-tran:prm:19-6)).

  

|  |
|----|
| **Important:** Some nonlocal vdW-DF result in very noisy energies, which can degrade the convergence to the electronic groundstate. Conjugate-gradient algorithms are particularly prone to show issues, such as a sudden increase in the energy. If [ALGO](../incar-tags/ALGO.md) = all (conjugate gradient algorithm) fails to converge, try to use denser FFT grids, for instance by setting [PREC](../incar-tags/PREC.md) = Accurate. |

[TABLE]

## Contents

- [1 List of nonlocal vdW-DF
  functionals](#List_of_nonlocal_vdW-DF_functionals)
- [2 Important technical remarks](#Important_technical_remarks)
  - [2.1 Kernel file vdw_kernel.bindat](#Kernel_file_vdw_kernel.bindat)
  - [2.2 POTCAR file](#POTCAR_file)
  - [2.3 Computational time](#Computational_time)
- [3 Related Tags and Sections](#Related_Tags_and_Sections)
- [4 References](#References)

## List of nonlocal vdW-DF functionals
- To add a nonlocal correlation energy $E_{\text{c,disp}}$ to the semilocal or hybrid
  exchange-correlation energy (selected with the [GGA](../incar-tags/GGA.md),
  [METAGGA](../incar-tags/METAGGA.md) or [XC](../incar-tags/XC.md) tag) one
  needs to set [LUSE_VDW](../incar-tags/LUSE_VDW.md)=.TRUE. (and
  optionally [IVDW_NL](../incar-tags/IVDW_NL.md)) in the
  [INCAR](../input-files/INCAR.md) file.

&nbsp;

- Since vdW-DF functionals tend to yield less spherical densities than
  standard GGA functionals, it is recommended to set
  [LASPH](../incar-tags/LASPH.md)=.TRUE. to get reasonably accurate
  contributions from the spheres around the atoms.

Examples of [INCAR](../input-files/INCAR.md) files are shown below.

- **vdW-DF** of Dion *et al.*^([\[1\]](#cite_note-dion:prl:2004-1)):

&nbsp;

    GGA       = RE
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    LASPH     = .TRUE.

- **vdW-DF2** of Lee *et al.* (2nd version of
  vdW-DF)^([\[7\]](#cite_note-lee:prb:2010-7)):

&nbsp;

    GGA       = ML
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    ZAB_VDW   = -1.8867 # the default is -0.8491
    LASPH     = .TRUE.

- **optPBE-vdW** of Klimeš *et
  al.*^([\[8\]](#cite_note-klimes:jpcm:2010-8)):

&nbsp;

    GGA       = OR
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    LASPH     = .TRUE.

- **optB88-vdW** of Klimeš *et
  al.*^([\[8\]](#cite_note-klimes:jpcm:2010-8)):

&nbsp;

    GGA       = BO
    PARAM1    = 0.1833333333
    PARAM2    = 0.22
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    LASPH     = .TRUE.

- **optB86b-vdW** of Klimeš *et
  al.*^([\[3\]](#cite_note-klimes:prb:2011-3)):

&nbsp;

    GGA       = MK
    PARAM1    = 0.1234 
    PARAM2    = 1.0
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    LASPH     = .TRUE.

- **BEEF-vdW** of Wellendorff *et al.*^([\[9\]](#cite_note-beef2012-9)):

&nbsp;

    GGA       = BF
    LUSE_VDW  = .TRUE.
    ZAB_VDW   = -1.8867 # the default is -0.8491
    LASPH     = .TRUE.

or

    GGA       = LIBXC
    LIBXC1    = GGA_XC_BEEFVDW
    LUSE_VDW  = .TRUE.
    ZAB_VDW   = -1.8867 # the default is -0.8491
    LASPH     = .TRUE.

Note that the GGA functional BEEF^([\[9\]](#cite_note-beef2012-9)) is
available only via an external library, either libbeef
([-Dlibbeef](../misc/Precompiler_options.md))
or Libxc
([-DUSELIBXC](../misc/Precompiler_options.md)).

- **rev-vdW-DF2** (also known as vdW-DF2-B86R) of
  Hamada^([\[10\]](#cite_note-hamada:prb:14-10)):

&nbsp;

    GGA       = MK
    PARAM1    = 0.1234568 # =10/81
    PARAM2    = 0.7114
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    ZAB_VDW   = -1.8867 # the default is -0.8491
    LASPH     = .TRUE.

In the vdW-DF2, BEEF-vdW and rev-vdW-DF2 functionals, the nonlocal
correlation consists of the Dion *et al.* functional, but with the
parameter $Z_{ab}$ that is changed from
-0.8491 (the default value in VASP) to -1.8867 by setting
[ZAB_VDW](../redirects/ZAB_VDW.md)=-1.8867.

- **vdW-DF-cx** of Berland and
  Hyldgaard^([\[11\]](#cite_note-berland:prb:2014-11)):

&nbsp;

    GGA       = CX
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    LASPH     = .TRUE.

- **vdW-DF3-opt1** of Chakraborty *et al.*
  ^([\[12\]](#cite_note-chakraborty:jctc:2020-12)):

&nbsp;

    GGA       = BO
    PARAM1    = 0.1122334456
    PARAM2    = 0.1234568 # =10/81
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    IVDW_NL   = 3
    ALPHA_VDW = 0.94950 # default for IVDW_NL=3 but can be overwritten by this tag
    GAMMA_VDW = 1.12    # default for IVDW_NL=3 but can be overwritten by this tag
    LASPH     = .TRUE.

- **vdW-DF3-opt2** of Chakraborty *et al.*
  ^([\[12\]](#cite_note-chakraborty:jctc:2020-12)):

&nbsp;

    GGA       = MK
    PARAM1    = 0.1234568 # =10/81
    PARAM2    = 0.58
    AGGAC     = 0.0
    LUSE_VDW  = .TRUE.
    IVDW_NL   = 4
    ZAB_VDW   = -1.8867 # the default is -0.8491
    ALPHA_VDW = 0.28248 # default for IVDW_NL=4 but can be overwritten by this tag
    GAMMA_VDW = 1.29    # default for IVDW_NL=4 but can be overwritten by this tag
    LASPH     = .TRUE.

- **rVV10** of Sabatini *et al.*
  ^([\[13\]](#cite_note-sabatini:prb:2013-13)):

&nbsp;

    GGA       = ML
    LUSE_VDW  = .TRUE.
    IVDW_NL   = 2
    BPARAM    = 6.3     # default but can be overwritten by this tag
    CPARAM    = 0.0093  # default but can be overwritten by this tag
    LASPH     = .TRUE.

- **SCAN+rVV10** of Peng *et al.*
  ^([\[14\]](#cite_note-peng:prx:2016-14)):

&nbsp;

    METAGGA   = SCAN
    LUSE_VDW  = .TRUE.
    BPARAM    = 15.7    # the default value is 6.3
    CPARAM    = 0.0093  # default but can be overwritten by this tag
    LASPH     = .TRUE.

- **PBE+rVV10L** of Peng and Perdew
  ^([\[15\]](#cite_note-peng:prb:2017-15)):

&nbsp;

    GGA       = PE
    LUSE_VDW  = .TRUE.
    BPARAM    = 10      # the default value is 6.3
    CPARAM    = 0.0093  # default but can be overwritten by this tag
    LASPH     = .TRUE.

- **r$^2$SCAN+rVV10** of Ning *et al.*
  ^([\[16\]](#cite_note-ning:prb:2022-16)):

&nbsp;

    METAGGA   = R2SCAN
    LUSE_VDW  = .TRUE.
    BPARAM    = 11.95   # the default value is 6.3
    CPARAM    = 0.0093  # default but can be overwritten by this tag
    LASPH     = .TRUE.

- **Opt(MS+rVV10)** of Kothakonda *et al.*
  ^([\[17\]](#cite_note-kothakonda:jpcc:26-17)):

&nbsp;

    XC        = MS2
    XC1_P1    = 0.2501   # the default value is 0.504
    XC1_P2    = 0.3916   # the default value is 0.14601
    XC1_P3    = 0.9104   # the default value is 4.0
    LUSE_VDW  = .TRUE.
    BPARAM    = 26.26    # the default value is 6.3
    CPARAM    = 0.0093   # default but can be overwritten by this tag
    LASPH     = .TRUE.

## Important technical remarks
### Kernel file vdw_kernel.bindat
- **Until VASP.6.4.2**: The calculation of the nonlocal correlation
  functional of Dion *et al.* (used when
  [IVDW_NL](../incar-tags/IVDW_NL.md)=1, which means for all functionals
  listed above except rVV10, SCAN+rVV10 and r$^2$SCAN+rVV10) requires a precalculated kernel which is
  distributed via the VASP download portal (vdw_kernel.bindat.gz has to
  be decompressed). If VASP does not find this file, the kernel is
  calculated, which is however extremely demanding (several hours!).
  Thus, the kernel needs to be either copied to the VASP run directory
  for each calculation or can be stored in a central location and read
  from there. The location needs to be set in routine *PHI_GENERATE*.
  This does not work on some clusters and the kernel needs to be copied
  into the working directory in such cases. The distributed file uses
  little endian convention and can not be read on big endian machines.
  The big endian version of the file is available also from the VASP
  portal. In the case of the rVV10 nonlocal correlation functional, no
  precalculated kernel is required and it is calculated on the fly,
  which is however much less demanding than in the case of the
  functional of Dion *et al.*.
- **Since VASP.6.4.3**: The calculation of the kernel for the functional
  of Dion *et al.* ([IVDW_NL](../incar-tags/IVDW_NL.md)=1), as well as
  for [IVDW_NL](../incar-tags/IVDW_NL.md)=3 and 4, is tremendously
  faster: the default value of a parameter has been reduced (with
  basically no loss of accuracy) and the calculation has been
  parallelized (with MPI and OpenACC for GPUs). Therefore, starting a
  calculation without vdw_kernel.bindat file present in the directory
  should be no problem for the computational time, and a
  vdw_kernel.bindat file will be generated rather efficiently during the
  first iteration. Note that a file vdw_kernel.bindat that was generated
  for a given kernel ([IVDW_NL](../incar-tags/IVDW_NL.md)=1, 3 or 4) can
  not be used for a calculation using another kernel, and in such a case
  the incompatibility of the vdw_kernel.bindat file will be detected and
  a new vdw_kernel.bindat file automatically generated to replace the
  incompatible one.

### POTCAR file
- There are no special [POTCAR](../input-files/POTCAR.md) files for the
  vdW-DF functionals and the PBE or LDA [POTCAR](../input-files/POTCAR.md)
  files can be used. Currently the evaluation of the nonlocal
  correlation functional is not done fully within the PAW method, but
  the sum of the pseudo-valence density and partial core density is
  used. This approximation works rather well, as is discussed in
  ^([\[3\]](#cite_note-klimes:prb:2011-3)), and the accuracy generally
  increases when the number of valence electrons is increased or when
  harder PAW datasets are used. For example, for adsorption it is
  recommended to compare the adsorption energy obtained with standard
  PAW datasets and more-electron [POTCAR](../input-files/POTCAR.md) files
  for both PBE calculations and vdW-DF calculations to assess the
  quality of the results.

### Computational time
- The evaluation of the nonlocal correlation energy requires some
  additional time. Most of it is spent on performing FFTs to evaluate
  the energy and potential. Thus the additional time is determined by
  the number of FFT grid points, basically the size of the simulation
  cell. It is almost independent on the number of the atoms in the cell,
  but increases with the amount of vacuum in the cell. The relative
  increase is high for isolated molecules in large cells, but small for
  solids in smaller cells with many k-points.

## Related Tags and Sections
[LUSE_VDW](../incar-tags/LUSE_VDW.md),
[IVDW_NL](../incar-tags/IVDW_NL.md),
[LSPIN_VDW](../incar-tags/LSPIN_VDW.md),
[ZAB_VDW](../redirects/ZAB_VDW.md),
[ALPHA_VDW](../incar-tags/ALPHA_VDW.md),
[GAMMA_VDW](../incar-tags/GAMMA_VDW.md),
[BPARAM](../incar-tags/BPARAM.md), [CPARAM](../incar-tags/CPARAM.md),
[GGA](../incar-tags/GGA.md), [AGGAC](../incar-tags/AGGAC.md),
[PARAM1](../incar-tags/PARAM1.md), [PARAM2](../incar-tags/PARAM2.md),
[METAGGA](../incar-tags/METAGGA.md)

See also the alternative atom-pairwise and many-body dispersion methods:
[IVDW](../incar-tags/IVDW.md)

## References
1.  ↑ ^([a](#cite_ref-dion:prl:2004_1-0))
    ^([b](#cite_ref-dion:prl:2004_1-1))
    ^([c](#cite_ref-dion:prl:2004_1-2)) [M. Dion, H. Rydberg, E.
    Schröder, D. C. Langreth, and B. I. Lundqvist, Phys. Rev. Lett.
    **92**, 246401
    (2004).](https://doi.org/10.1103/PhysRevLett.92.246401)
2.  ↑ ^([a](#cite_ref-romanperez:prl:09_2-0))
    ^([b](#cite_ref-romanperez:prl:09_2-1)) [G. Román-Pérez and J. M.
    Soler, Phys. Rev. Lett. **103**, 096102
    (2009).](https://doi.org/10.1103/PhysRevLett.103.096102)
3.  ↑ ^([a](#cite_ref-klimes:prb:2011_3-0))
    ^([b](#cite_ref-klimes:prb:2011_3-1))
    ^([c](#cite_ref-klimes:prb:2011_3-2))
    ^([d](#cite_ref-klimes:prb:2011_3-3)) [J. Klimeš, D. R. Bowler,
    and A. Michaelides, Phys. Rev. B **83**, 195131
    (2011).](https://doi.org/10.1103/PhysRevB.83.195131)
4.  [↑](#cite_ref-thonhauser:prl:2015_4-0) [T. Thonhauser, S.
    Zuluaga, C. A. Arter, K. Berland, E. Schröder, and P. Hyldgaard,
    Phys. Rev. Lett. **115**, 136402
    (2015).](http://doi.org/10.1103/PhysRevLett.115.136402)
5.  [↑](#cite_ref-berland:rpp:2015_5-0) [K. Berland, V. R. Cooper, K.
    Lee, E. Schröder, T. Thonhauser, P. Hyldgaard, and B. I. Lundqvist,
    Rep. Prog. Phys. **78**, 066501
    (2015).](https://doi.org/10.1088/0034-4885/78/6/066501)
6.  [↑](#cite_ref-tran:prm:19_6-0) [F. Tran, L. Kalantari, B. Traoré, X.
    Rocquefelte, and P. Blaha, Phys. Rev. Mater. **3**, 0637602
    (2019).](https://doi.org/10.1103/PhysRevMaterials.3.063602)
7.  [↑](#cite_ref-lee:prb:2010_7-0) [K. Lee, E. D. Murray, L.
    Kong, B. I. Lundqvist, and D. C. Langreth, Phys. Rev. B **82**,
    081101(R) (2010).](https://doi.org/10.1103/PhysRevB.82.081101)
8.  ↑ ^([a](#cite_ref-klimes:jpcm:2010_8-0))
    ^([b](#cite_ref-klimes:jpcm:2010_8-1)) [J. Klimeš, D. R. Bowler,
    and A. Michaelides, J. Phys.: Condens. Matter **22**, 022201
    (2010).](https://doi.org/10.1088/0953-8984/22/2/022201)
9.  ↑ ^([a](#cite_ref-beef2012_9-0)) ^([b](#cite_ref-beef2012_9-1)) [J.
    Wellendorff, K. T. Lundgaard, A. Møgelhøj, V. Petzold, D. D. Landis,
    Jens K. Nørskov, T. Bligaard, and K. W. Jacobsen, Phys. Rev. B
    **85**, 235149 (2012).](https://doi.org/10.1103/PhysRevB.85.235149)
10. [↑](#cite_ref-hamada:prb:14_10-0) [I. Hamada, Phys. Rev. B **89**,
    121103 (2014).](https://doi.org/10.1103/PhysRevB.89.121103)
11. [↑](#cite_ref-berland:prb:2014_11-0) [K. Berland and P. Hyldgaard,
    Phys. Rev. B **89**, 035412
    (2014).](https://doi.org/10.1103/PhysRevB.89.035412)
12. ↑ ^([a](#cite_ref-chakraborty:jctc:2020_12-0))
    ^([b](#cite_ref-chakraborty:jctc:2020_12-1)) [D. Chakraborty, K.
    Berland, and T. Thonhauser, *Next-Generation Nonlocal van der Waals
    Density Functional*, J. Chem. Theory Comput. **16**, 5893
    (2020).](https://doi.org/10.1021/acs.jctc.0c00471)
13. [↑](#cite_ref-sabatini:prb:2013_13-0) [R. Sabatini, T. Gorni, and S.
    de Gironcoli, Phys. Rev. B **87**, 041108(R)
    (2013).](http://doi.org/10.1103/PhysRevB.87.041108)
14. [↑](#cite_ref-peng:prx:2016_14-0) [H. Peng, Z.-H. Yang, J. P.
    Perdew, and J. Sun, Phys. Rev. X **6**, 041005
    (2016).](https://doi.org/10.1103/PhysRevX.6.041005)
15. [↑](#cite_ref-peng:prb:2017_15-0) [H. Peng and J. P. Perdew,
    *Rehabilitation of the Perdew-Burke-Ernzerhof generalized gradient
    approximation for layered materials*, Phys. Rev. B **95**, 081105(R)
    (2017).](https://doi.org/10.1103/PhysRevB.95.081105)
16. [↑](#cite_ref-ning:prb:2022_16-0) [J. Ning, M. Kothakonda, J. W.
    Furness, A. D. Kaplan, S. Ehlert, J. G. Brandenburg, J. P. Perdew,
    and J. Sun, *Workhorse minimally empirical dispersion-corrected
    density functional with tests for weakly bound systems:
    r²SCAN+rVV⁢10*, Phys. Rev. B **106**, 075422
    (2022).](https://doi.org/10.1103/PhysRevB.106.075422)
17. [↑](#cite_ref-kothakonda:jpcc:26_17-0) [M. Kothakonda, A. Patra, R.
    Zhang, J. Ning, J. Furness, Q. Zhao, and J. Sun, *Toward Chemical
    Accuracy for Chemi- and Physisorption with an Efficient Density
    Functional*, J. Phys. Chem. C **130**, 2997
    (2026).](https://doi.org/10.1021/acs.jpcc.5c08744)

------------------------------------------------------------------------

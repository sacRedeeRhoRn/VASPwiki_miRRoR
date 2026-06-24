<!-- Source: https://vasp.at/wiki/index.php/XCm_Pn | revid: 34551 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# XCm_Pn
XCm_Pn = \[real\] 

Description: XCm_Pn, where $m=1, 2, \ldots$ and $n=1, 2, \ldots$ allows
to modify the parameters in a semilocal functional.

------------------------------------------------------------------------

The XCm_Pn tag allows to modify the parameters in the semilocal
functional set with the [XC](XC.md) tag. In XCm_Pn,
$m=1, 2, \ldots$ refers to the
$m$th component of the functional and
$n=1, 2, \ldots$ to the
$n$th parameter of this
$m$th functional component.

The XCm_Pn tag can be used for functionals that are implemented in VASP
or in Libxc.

- Functionals in VASP:

The number of functionals with modifiable parameters is for the moment
very limited and concerns only a few MGGAs. Among the functionals listed
at [METAGGA](METAGGA.md), there is MS0, MS1, and
MS2,^([\[1\]](#cite_note-sun:jcp:12-1)[\[2\]](#cite_note-sun:jcp:13-2))
for instance. The functionals with modifiable parameters can be found by
searching for "XC%PARAM" in the subroutine SET_XC_DATA in the setex.F
file.

- Functionals in Libxc:

For many of the functionals implemented in the library of
exchange-correlation functionals
Libxc^([\[3\]](#cite_note-marques:cpc:2012-3)[\[4\]](#cite_note-lehtola:sx:2018-4)[\[5\]](#cite_note-tran:arxiv:2026-5)[\[6\]](#cite_note-libxc-6))
it is possible to modify the parameters. If a functional from Libxc has
modifiable parameters, then they are listed in
[OUTCAR](../output-files/OUTCAR.md) below "Parameters of Libxc functionals:"
as P$n$ ($n=1, 2,
\ldots$). Note that [LIBXC1_Pn](LIBXC1_Pn.md)
and [LIBXC2_Pn](LIBXC2_Pn.md) are equivalent to XCm_Pn
when the functional is set with the tag [GGA](GGA.md) or
[METAGGA](METAGGA.md).

More information about the mixing and screening parameters in hybrid
functionals can be found at [LIBXC1_Pn](LIBXC1_Pn.md).

|                                                 |
|-------------------------------------------------|
| **Mind:** XCm_Pn is available since VASP.6.4.3. |

### Examples
- In the GGA PBE functional,^([\[7\]](#cite_note-perdew:prl:1996-7)) as
  implemented in Libxc, the default parameters $\mu=0.21951$ in exchange and $\beta=0.066725$ in correlation are changed to
  $\mu=10/81\approx0.12345679$ and
  $\beta=0.046$ to get the PBEsol
  functional^([\[8\]](#cite_note-perdew:prl:2008-8)) (of course, the
  simpler way to use PBEsol from Libxc would be to call it directly with
  "[XC](XC.md)=GGA_X_PBE_SOL GGA_C_PBE_SOL"). This example is
  equivalent to the one given for
  [LIBXC1_Pn](LIBXC1_Pn.md).

&nbsp;

    XC = GGA_X_PBE GGA_C_PBE
    XC1_P2 = 0.12345679    #parameter mu, which is the 2nd parameter in GGA_X_PBE
    XC2_P1 = 0.046         #parameter beta, which is the 1st parameter in GGA_C_PBE

- In the MGGA MS1 functional the default parameters
  $\kappa=0.404$, $c=0.18150$ and $b=1.0$ in
  exchange (see Table I in Ref. ^([\[2\]](#cite_note-sun:jcp:13-2))) are
  changed to $\kappa=0.504$,
  $c=0.14601$ and $b=4.0$ to get the MS2 functional.

&nbsp;

    XC = MS1
    XC1_P1 = 0.504    #parameter kappa, which is the 1st parameter in MS0, MS1, and MS2
    XC1_P2 = 0.14601  #parameter c, which is the 2nd parameter in MS0, MS1, and MS2
    XC1_P3 = 4.0      #parameter b, which is the 3rd parameter in MS0, MS1, and MS2

## Related tags and articles
[XC](XC.md), [XC_C](XC_C.md), [GGA](GGA.md),
[METAGGA](METAGGA.md), [LIBXC1](LIBXC1.md),
[LIBXC2](LIBXC2.md),
[LIBXC1_Pn](LIBXC1_Pn.md),
[LIBXC2_Pn](LIBXC2_Pn.md)

## References
1.  [↑](#cite_ref-sun:jcp:12_1-0) [J. Sun, B. Xiao, and A.
    Ruzsinszky, J. Chem. Phys. **137**, 051101
    (2012).](https://doi.org/10.1063/1.4742312)
2.  ↑ ^([a](#cite_ref-sun:jcp:13_2-0)) ^([b](#cite_ref-sun:jcp:13_2-1))
    [J. Sun, R. Haunschild, B. Xiao, I. W. Bulik, G. E. Scuseria,
    and J. P. Perdew, J. Chem. Phys. **138**, 044113
    (2013).](https://doi.org/10.1063/1.4789414)
3.  [↑](#cite_ref-marques:cpc:2012_3-0) [M. A. L. Marques, M. J. T.
    Oliveira, and T. Burnus, Comput. Phys. Commun., **183**, 2272
    (2012).](https://doi.org/10.1016/j.cpc.2012.05.007)
4.  [↑](#cite_ref-lehtola:sx:2018_4-0) [S. Lehtola, C.
    Steigemann, M. J. T. Oliveira, and M. A. L. Marques, SoftwareX,
    **7**, 1 (2018).](https://doi.org/10.1016/j.softx.2017.11.002)
5.  [↑](#cite_ref-tran:arxiv:2026_5-0) [F. Tran, S. Lehtola, S.
    Pittalis, and M. A. L. Marques, *Semi-Local Exchange-Correlation
    Approximations in Density Functional Theory*, arXiv **2602.17333**
    (2026).](https://doi.org/10.48550/arXiv.2602.17333)
6.  [↑](#cite_ref-libxc_6-0)
    [https://libxc.gitlab.io](https://libxc.gitlab.io)
7.  [↑](#cite_ref-perdew:prl:1996_7-0) [J. P. Perdew, K. Burke, and M.
    Ernzerhof, Phys. Rev. Lett., **77**, 3865
    (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
8.  [↑](#cite_ref-perdew:prl:2008_8-0) [J. P. Perdew, A.
    Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A.
    Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. **100**, 136406
    (2008).](https://doi.org/10.1103/PhysRevLett.100.136406)

------------------------------------------------------------------------

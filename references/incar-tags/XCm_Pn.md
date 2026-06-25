<!-- Source: https://vasp.at/wiki/index.php/XCm_Pn | revid: 34551 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# XCm_Pn


XCm_Pn = \[real\] 

Description: XCm_Pn, where
$m=1, 2, \ldots$ and $n=1, 2, \ldots$ allows to modify the parameters in a semilocal
functional.

------------------------------------------------------------------------

The XCm_Pn tag allows to
modify the parameters in the semilocal functional set with the
[XC](XC.md) tag. In
XCm_Pn,
$m=1, 2, \ldots$ refers to the
$m$th component of the functional and
$n=1, 2, \ldots$ to the $n$th
parameter of this $m$th
functional component.

The XCm_Pn tag can be used for
functionals that are implemented in VASP or in Libxc.

- Functionals in VASP:

The number of functionals with modifiable parameters is for the moment
very limited and concerns only a few MGGAs. Among the functionals listed
at [METAGGA](METAGGA.md), there is MS0, MS1, and
MS2,[^sun:jcp:12-1][^sun:jcp:13-2]
for instance. The functionals with modifiable parameters can be found by
searching for "XC%PARAM" in the subroutine SET_XC_DATA in the setex.F
file.

- Functionals in Libxc:

For many of the functionals implemented in the library of
exchange-correlation functionals
Libxc[^marques:cpc:2012-3][^lehtola:sx:2018-4][^tran:arxiv:2026-5][^libxc-6]
it is possible to modify the parameters. If a functional from Libxc has
modifiable parameters, then they are listed in
[OUTCAR](../output-files/OUTCAR.md) below "Parameters of Libxc functionals:"
as P$n$
($n=1, 2, \ldots$). Note that
[LIBXC1_Pn](LIBXC1_Pn.md) and
[LIBXC2_Pn](LIBXC2_Pn.md) are equivalent to
XCm_Pn when the functional is
set with the tag [GGA](GGA.md) or
[METAGGA](METAGGA.md).

More information about the mixing and screening parameters in hybrid
functionals can be found at [LIBXC1_Pn](LIBXC1_Pn.md).

|  |
|----|
| **Mind:** XCm_Pn is available since VASP.6.4.3. |

### Examples\[<a href="/wiki/index.php?title=XCm_Pn&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Examples">edit</a> \| (./index.php.md)\]

- In the GGA PBE
  functional,[^perdew:prl:1996-7]
  as implemented in Libxc, the default parameters
  $\mu=0.21951$ in exchange and
  $\beta=0.066725$ in correlation are changed to
  $\mu=10/81\approx0.12345679$ and
  $\beta=0.046$ to get the PBEsol
  functional[^perdew:prl:2008-8]
  (of course, the simpler way to use PBEsol from Libxc would be to call
  it directly with "[XC](XC.md)=GGA_X_PBE_SOL GGA_C_PBE_SOL").
  This example is equivalent to the one given for
  [LIBXC1_Pn](LIBXC1_Pn.md).

<!-- -->

    XC = GGA_X_PBE GGA_C_PBE
    XC1_P2 = 0.12345679    #parameter mu, which is the 2nd parameter in GGA_X_PBE
    XC2_P1 = 0.046         #parameter beta, which is the 1st parameter in GGA_C_PBE

- In the MGGA MS1 functional the default parameters
  $\kappa=0.404$, $c=0.18150$
  and $b=1.0$ in
  exchange (see Table I in Ref.
  [^sun:jcp:13-2])
  are changed to $\kappa=0.504$, $c=0.14601$
  and $b=4.0$ to
  get the MS2 functional.

<!-- -->

    XC = MS1
    XC1_P1 = 0.504    #parameter kappa, which is the 1st parameter in MS0, MS1, and MS2
    XC1_P2 = 0.14601  #parameter c, which is the 2nd parameter in MS0, MS1, and MS2
    XC1_P3 = 4.0      #parameter b, which is the 3rd parameter in MS0, MS1, and MS2

## Related tags and articles\[<a href="/wiki/index.php?title=XCm_Pn&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[XC](XC.md), [XC_C](XC_C.md), [GGA](GGA.md),
[METAGGA](METAGGA.md), [LIBXC1](LIBXC1.md),
[LIBXC2](LIBXC2.md),
[LIBXC1_Pn](LIBXC1_Pn.md),
[LIBXC2_Pn](LIBXC2_Pn.md)

## References\[<a href="/wiki/index.php?title=XCm_Pn&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^sun:jcp:12-1]: [J. Sun, B. Xiao, and A. Ruzsinszky, J. Chem. Phys. **137**, 051101 (2012).](https://doi.org/10.1063/1.4742312)
[^sun:jcp:13-2]: [J. Sun, R. Haunschild, B. Xiao, I. W. Bulik, G. E. Scuseria, and J. P. Perdew, J. Chem. Phys. **138**, 044113 (2013).](https://doi.org/10.1063/1.4789414)
[^marques:cpc:2012-3]: [M. A. L. Marques, M. J. T. Oliveira, and T. Burnus, Comput. Phys. Commun., **183**, 2272 (2012).](https://doi.org/10.1016/j.cpc.2012.05.007)
[^lehtola:sx:2018-4]: [S. Lehtola, C. Steigemann, M. J. T. Oliveira, and M. A. L. Marques, SoftwareX, **7**, 1 (2018).](https://doi.org/10.1016/j.softx.2017.11.002)
[^tran:arxiv:2026-5]: [F. Tran, S. Lehtola, S. Pittalis, and M. A. L. Marques, *Semi-Local Exchange-Correlation Approximations in Density Functional Theory*, arXiv **2602.17333** (2026).](https://doi.org/10.48550/arXiv.2602.17333)
[^libxc-6]: [https://libxc.gitlab.io](https://libxc.gitlab.io)
[^perdew:prl:1996-7]: [J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett., **77**, 3865 (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
[^perdew:prl:2008-8]: [J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. **100**, 136406 (2008).](https://doi.org/10.1103/PhysRevLett.100.136406)

<!-- Source: https://vasp.at/wiki/index.php/Category:DFT%2BU | revid: 36498 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:DFT+U


The LDA and semilocal GGA functionals often fail to describe systems
with localized (strongly correlated) $d$ or
$f$ electrons (this manifests itself primarily in the form
of unrealistic one-electron energies or too small magnetic moments). In
some cases this can be remedied by introducing on the
$d$ or $f$ atom a
strong intra-atomic interaction in a simplified (screened) Hartree-Fock
like manner ($E^{\text{HF}}\[\hat{n}\]$), as an on-site replacement of the LDA/GGA functional:

$E_{\text{xc}}^{\text{DFT}+U}\[n,\hat{n}\] =
E_{\text{xc}}^{\text{DFT}}\[n\] + E^{\text{HF}}\[\hat{n}\] -
E_{\text{dc}}\[\hat{n}\]$

where $E_{\text{dc}}\[\hat{n}\]$ is the double-counting term and
$\hat{n}$ is the on-site occupancy matrix of the
$d$ or $f$ electrons.
This approach is known as the DFT+U method (traditionally called
LSDA+U[^anisimov:prb:91-1]).

The first VASP DFT+U calculations, including some additional technical
details on the VASP implementation, can be found in Ref.
[^rohrbach:jcp:03-2]
(the original implementation was done by Olivier Bengone
[^Bengone:prb:00-3]
and Georg Kresse).

More detail about the formalism is provided below.


## Contents


- [1
  Theory](#theory)
- [2 Additional
  resources](#additional-resources)
  - [2.1 How
    to](#how-to)
  - [2.2
    Tutorials](#tutorials)
  - [2.3
    Lectures](#lectures)
- [3
  References](#references)


## Theory\[<a
href="/wiki/index.php?title=Category:DFT%2BU&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theory">edit</a> \| (./index.php.md)\]

DFT+U is a method that was proposed to improve the description of
systems with strongly correlated $d$ or
$f$ electrons, like antiferromagnetic NiO for instance,
that are usually inaccurately described with the standard LDA and GGA
functionals[^anisimov:prb:91-1].
Several variants of the DFT+U method exist (see Refs.
[^Ylvisaker:prb:2009-4][^Himmetoglu:ijqc:2014-5]
for reviews) that differ for instance in the way the double counting
term $E_{\text{dc}}\[\hat{n}\]$ is calculated. Three variants of them are implemented
in VASP, whose formalism is briefly summarized below.

- [LDAUTYPE](../incar-tags/LDAUTYPE.md)=1: The rotationally invariant
  DFT+U introduced by Liechtenstein *et
  al.*[^liechtenstein:prb:95-6]

This particular flavour of DFT+U is of the form

$E^{\rm HF}\[{\hat n}\]=\frac{1}{2} \sum_{\\\gamma\}
(U_{\gamma_1\gamma_3\gamma_2\gamma_4} -
U_{\gamma_1\gamma_3\gamma_4\gamma_2}){ \hat n}_{\gamma_1\gamma_2}{\hat
n}_{\gamma_3\gamma_4}$

and is determined by the PAW on-site occupancies


${\hat n}_{\gamma_1\gamma_2} = \langle \Psi^{s_2} \mid m_2 \rangle
\langle m_1 \mid \Psi^{s_1} \rangle$

and the (unscreened) on-site electron-electron interaction

$U_{\gamma_1\gamma_3\gamma_2\gamma_4}= \langle m_1 m_3 \mid
\frac{1}{|\mathbf{r}-\mathbf{r}^\prime|} \mid m_2 m_4 \rangle
\delta_{s_1 s_2} \delta_{s_3 s_4}$

where $|m\rangle$
represents a real spherical harmonics of angular momentum
$l$=[LDAUL](../incar-tags/LDAUL.md).

The unscreened electron-electron interaction $U_{\gamma_{1}\gamma_{3}\gamma_{2}\gamma_{4}}$ can
be written in terms of the Slater integrals $F^0$,
$F^2$, $F^4$, and
$F^6$ ($f$
electrons). Using values for the Slater integrals calculated from atomic
orbitals, however, would lead to a large overestimation of the true
electron-electron interaction, since in solids the Coulomb interaction
is screened (especially $F^0$).

In practice these integrals are often treated as parameters, *i.e.*,
adjusted to reach agreement with experiment for a property like for
instance the equilibrium volume, the magnetic moment or the band gap.
They are normally specified in terms of the effective on-site Coulomb-
and exchange parameters, $U$ and
$J$ ([LDAUU](../incar-tags/LDAUU.md) and
[LDAUJ](../incar-tags/LDAUJ.md), respectively). $U$ and
$J$ can also be extracted from constrained-DFT
calculations[^vaugier:prb:2012-7][^kaltak:thesis2015-8].

These translate into values for the Slater integrals in the following
way (as implemented in VASP at the moment):

|  |  |  |  |  |
|----|----|----|----|----|
| $L\\$ | $F^0\\$ | $F^2\\$ | $F^4\\$ | $F^6\\$ |
| $1\\$ | $U\\$ | $5J\\$ | \- | \- |
| $2\\$ | $U\\$ | $\frac{14}{1+0.625}J$ | $0.625 F^2\\$ | \- |
| $3\\$ | $U\\$ | $\frac{6435}{286+195 \cdot 0.668+250 \cdot 0.494}J$ | $0.668 F^2\\$ | $0.494 F^2\\$ |

The essence of the DFT+U method consists of the assumption that one may
now write the total energy as:

$E^{\mathrm{DFT}+U}\[n,\hat
n\]=E^{\mathrm{DFT}}\[n\]+E^{\mathrm{HF}}\[\hat
n\]-E_{\mathrm{dc}}\[\hat n\]$

where the Hartree-Fock-like interaction replaces the semilocal on-site
due to the fact that one subtracts a double-counting energy
$E_{\mathrm{dc}}$, which supposedly equals the on-site
semilocal contribution to the total energy,

$E_{\mathrm{dc}}\[\hat n\] = \frac{U}{2} {\hat n}_{\mathrm{tot}}({\hat
n}_{\mathrm{tot}}-1) - \frac{J}{2} \sum_\sigma {\hat
n}^\sigma_{\mathrm{tot}}({\hat n}^\sigma_{\mathrm{tot}}-1).$

- [LDAUTYPE](../incar-tags/LDAUTYPE.md)=2: The simplified (rotationally
  invariant) approach to the DFT+U, introduced by Dudarev *et
  al.*[^dudarev:prb:98-9]

This flavour of DFT+U is of the following form:

$E^{\mathrm{DFT+U}}=E^{\mathrm{DFT}}+\frac{(U-J)}{2}\sum_\sigma \left\[
\left(\sum_{m_1} n_{m_1,m_1}^{\sigma}\right) - \left(\sum_{m_1,m_2}
\hat n_{m_1,m_2}^{\sigma} \hat n_{m_2,m_1}^{\sigma} \right) \right\].$

This can be understood as adding a penalty functional to the semilocal
total energy expression that forces the [on-site occupancy
matrix](#occmat) in the direction of idempotency,

$\hat n^{\sigma} = \hat n^{\sigma} \hat n^{\sigma}$.

Real matrices are only idempotent when their eigenvalues are either 1 or
0, which for an occupancy matrix translates to either fully occupied or
fully unoccupied levels.

**Note**: in Dudarev's approach the parameters
$U$ and $J$ do not
enter seperately, only the difference $U-J$ is
meaningful.

- [LDAUTYPE](../incar-tags/LDAUTYPE.md)=3: This option is for the
  calculation of the parameter $U$ using
  the linear response approach from Ref.
  [^cococcioni:2005-10].
  The steps to use this method are shown for [the example of
  NiO](../misc/Calculate_U_for_LSDA+U.md).

<!-- -->

- [LDAUTYPE](../incar-tags/LDAUTYPE.md)=4: same as
  [LDAUTYPE](../incar-tags/LDAUTYPE.md)=1, but without exchange
  splitting (i.e., the total spin-up plus spin-down occupancy matrix is
  used). The double-counting term is given by

$E_{\mathrm{dc}}\[\hat n\] = \frac{U}{2} {\hat n}_{\mathrm{tot}}({\hat
n}_{\mathrm{tot}}-1) - \frac{J}{2} \sum_\sigma {\hat
n}^\sigma_{\mathrm{tot}}({\hat n}^\sigma_{\mathrm{tot}}-1).$

## Additional resources\[<a
href="/wiki/index.php?title=Category:DFT%2BU&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### How to\[<a
href="/wiki/index.php?title=Category:DFT%2BU&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

DFT+U can be switched on with the [LDAU](../incar-tags/LDAU.md) tag, while
the [LDAUTYPE](../incar-tags/LDAUTYPE.md) tag determines the DFT+U
flavor that is used. [LDAUL](../incar-tags/LDAUL.md) specifies the
$l$-quantum number for which the on-site interaction is
added, and the effective on-site Coulomb and exchange interactions are
set (in eV) with the [LDAUU](../incar-tags/LDAUU.md) and
[LDAUJ](../incar-tags/LDAUJ.md) tags, respectively. Note that it is
recommended to increase [LMAXMIX](../incar-tags/LMAXMIX.md) to 4 for
*d*-electrons or 6 for *f*-elements.

### Tutorials\[<a
href="/wiki/index.php?title=Category:DFT%2BU&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/bulk/part3/#bulk-e09"
  class="external text" rel="nofollow">DFT+U</a> on NiO.
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part1/#mag-e04"
  class="external text" rel="nofollow">LSDA+U and pseudopotential
  selection of NiO</a> and
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part2/#mag-e05"
  class="external text" rel="nofollow">Heisenberg model for NiO using
  DFT+U</a>.

### Lectures\[<a
href="/wiki/index.php?title=Category:DFT%2BU&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on
  <a href="https://youtu.be/6F_WNIh6V7I" class="external text"
  rel="nofollow">the optical gap</a>, introduces DFT+U towards the end
  of the lecture.

## References\[<a
href="/wiki/index.php?title=Category:DFT%2BU&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^anisimov:prb:91-1]: [V. I. Anisimov, J. Zaanen, and O. K. Andersen, Phys. Rev. B **44**, 943 (1991).](https://doi.org/10.1103/PhysRevB.44.943)
[^rohrbach:jcp:03-2]: [A. Rohrbach, J. Hafner, and G. Kresse J. Phys.: Condens. Matter **15**, 979 (2003).](https://doi.org/10.1088/0953-8984/15/6/325)
[^Bengone:prb:00-3]: [O. Bengone, M. Alouani, P. Blöchl, and J. Hugel, Phys. Rev. B **62**, 16392 (2000).](https://doi.org/10.1103/PhysRevB.62.16392)
[^Ylvisaker:prb:2009-4]: [E. R. Ylvisaker and W. E. Pickett, Phys. Rev. B **79**, 035103 (2009).](https://doi.org/10.1103/PhysRevB.79.035103)
[^Himmetoglu:ijqc:2014-5]: [B. Himmetoglu, A. Floris, S. de Gironcoli, and M. Cococcioni, Int. J. Quantum Chem. **114**. 14 (2014).](https://doi.org/10.1002/qua.24521)
[^liechtenstein:prb:95-6]: [A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Phys. Rev. B **52**, R5467 (1995).](https://doi.org/10.1103/PhysRevB.52.R5467)
[^vaugier:prb:2012-7]: [L. Vaugier, H. Jiang, and S. Biermann, Phys. Rev. B **86**, 165105 (2012).](https://doi.org/10.1103/PhysRevB.86.165105)
[^kaltak:thesis2015-8]: [M. Kaltak, Thesis: Merging GW with DMFT (2015).](https://utheses.univie.ac.at/detail/33771#)
[^dudarev:prb:98-9]: [S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Phys. Rev. B **57**, 1505 (1998).](https://doi.org/10.1103/PhysRevB.57.1505)
[^cococcioni:2005-10]: [M. Cococcioni and S. de Gironcoli, Phys. Rev. B **71**, 035105 (2005).](https://doi.org/10.1103/PhysRevB.71.035105)

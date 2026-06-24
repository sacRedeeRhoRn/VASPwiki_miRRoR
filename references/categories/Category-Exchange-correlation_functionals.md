<!-- Source: https://vasp.at/wiki/index.php/Category:Exchange-correlation_functionals | revid: 34700 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Exchange-correlation functionals
In the Kohn-Sham (KS) formulation of density-functional theory
(DFT),^([\[1\]](#cite_note-hohenberg:pr:1964-1)[\[2\]](#cite_note-kohn:pr:1965-2))
the total energy is given by

$E_{\rm tot}^{\rm DFT} =
-\frac{1}{2}\sum_{i}\int\psi_{i}^{\*}({\bf r})\nabla^{2}\psi_{i}({\bf
r})d^{3}r - \sum_{A}\int\frac{Z_{A}}{\left\vert{\bf r}-{\bf
R}_{A}\right\vert}n({\bf r})d^{3}r + \frac{1}{2}\int\int\frac{n({\bf
r})n({\bf r'})}{\left\vert{\bf r}-{\bf r'}\right\vert}d^{3}rd^{3}r' +
E_{\rm xc} + \frac{1}{2}\sum_{A\ne
B}\frac{Z_{A}Z_{B}}{\left\vert{\bf R}_{A}-{\bf R}_{B}\right\vert}$

where the terms on the right-hand side represent the non-interacting
kinetic energy of the electrons, the electrons-nuclei attraction energy,
the classical Coulomb electron-electron repulsive energy, the
exchange-correlation energy, and the nuclei-nuclei repulsion energy,
respectively. The KS orbitals $\psi_{i}$ and the electron density $n=\sum_{i}\left\vert\psi_{i}\right\vert^{2}$ that are used
to evaluate $E_{\rm tot}^{\rm DFT}$ are
obtained by [solving self-consistently the (generalized) KS
equations](Category-Electronic_minimization.md)

$\left(-\frac{1}{2}\nabla^{2}
-\sum_{A}\frac{Z_{A}}{\left\vert{\bf r}-{\bf R}_{A}\right\vert} +
\int\frac{n({\bf r'})}{\left\vert{\bf r}-{\bf r'}\right\vert}d^{3}r' +
\hat{v}_{\rm xc}({\bf r})\right)\psi_{i}({\bf r}) =
\epsilon_{i}\psi_{i}({\bf r}).$

The only terms in $E_{\rm tot}^{\rm DFT}$ and in the (g)KS equations that are not known exactly are the
**exchange-correlation energy functional** $E_{\rm xc}$ and **potential** $\hat{v}_{\rm xc}$. Therefore, the accuracy of the calculated
properties depends strongly on the approximations used for
$E_{\rm xc}$ and $\hat{v}_{\rm xc}$.

Note that depending on the type of approximation for
$E_{\rm xc}$ the potential
$\hat{v}_{\rm xc}$ is calculated either
as the derivative with respect to the density, $v_{\rm xc}=\delta E_{\rm xc}/\delta n$ (KS
scheme^([\[2\]](#cite_note-kohn:pr:1965-2))), or as the derivative with
respect to the orbitals, $\hat{v}_{\mathrm{xc}}\psi_{i}=\delta
E_{\mathrm{xc}}/\delta\psi_{i}^{\*}$ (generalized KS
scheme^([\[3\]](#cite_note-seidl:prb:96-3))).

Several hundreds of approximations for the **exchange and correlation**
have been
proposed.^([\[4\]](#cite_note-libxc_list-4)[\[5\]](#cite_note-tran:arxiv:2026-5)[\[6\]](#cite_note-dellasala:ijqc:2016-6)[\[7\]](#cite_note-mardirossian:mp:2017-7))
They can be classified into families like the local density
approximation (LDA), semilocal approximations (generalized gradient
approximation ([GGA](../incar-tags/GGA.md)) and
[METAGGA](../incar-tags/METAGGA.md)), or
[hybrid](../methods/Category-Hybrid_functionals.md).
There is also the possibility to include a [van der Waals
correction](../methods/Category-Van_der_Waals_functionals.md)
or an on-site Coulomb repulsion using
[DFT+U](../methods/Category-DFT+U.md) on top of another
functional. The different types of approximations available in VASP are
listed below. Also mentioned are the many-body methods for an accurate
calculation of the correlation energy, which, however, are not DFT
methods.

## Contents

- [1 Which exchange-correlation method to
  choose?](#Which_exchange-correlation_method_to_choose?)
- [2 Types of approximations](#Types_of_approximations)
  - [2.1 Local density approximation
    (LDA)](#Local_density_approximation_(LDA))
  - [2.2 Generalized gradient approximation
    (GGA)](#Generalized_gradient_approximation_(GGA))
  - [2.3 Meta generalized gradient approximation
    (meta-GGA)](#Meta_generalized_gradient_approximation_(meta-GGA))
  - [2.4 Hartree-Fock (HF) and hybrid
    functionals](#Hartree-Fock_(HF)_and_hybrid_functionals)
  - [2.5 Exact exchange optimized-effective potential (EXX-OEP),
    localized Hartree-Fock (LHF), and Krieger-Li-Iafrate
    (KLI)](#Exact_exchange_optimized-effective_potential_(EXX-OEP),_localized_Hartree-Fock_(LHF),_and_Krieger-Li-Iafrate_(KLI))
  - [2.6 Density functional theory plus U
    (DFT+U)](#Density_functional_theory_plus_U_(DFT+U))
  - [2.7 van der Waals (vdW)
    functionals](#van_der_Waals_(vdW)_functionals)
  - [2.8 Many-body methods](#Many-body_methods)
- [3 References](#References)

### Which exchange-correlation method to choose?
Among the hundreds of methods
available,^([\[4\]](#cite_note-libxc_list-4)[\[5\]](#cite_note-tran:arxiv:2026-5)[\[6\]](#cite_note-dellasala:ijqc:2016-6)[\[7\]](#cite_note-mardirossian:mp:2017-7))
the choice for the exchange and correlation method should be done by
considering the following points:

- **Appropriate for the studied system and property**:
  - Some functionals were constructed without emphasis on a particular
    property or class of systems, while others were developed
    specifically for van der Waals interactions, strongly correlated
    systems, or band gap calculation, for instance.
  - Therefore, a method should be appropriately chosen according to the
    information found in the literature.
- **Computational power**:
  - The hybrid functionals and the many-body methods are computationally
    much more expensive (by orders of magnitude!) than the (semi)local
    approximations. Thus, it is especially important for such methods to
    have a rough idea of the required computational time and memory.
    This can be done by first considering systems of smaller size and
    reduced parameters (basis-set size and k-point mesh), and then
    increasing them gradually to see how the calculation time evolves.
  - If the calculations are unaffordable given the available computer
    power, then using a cheaper method should be considered. For
    instance, for strongly correlated systems, the DFT+U may be as
    reliable as the much more costly hybrid functionals.

## Types of approximations
### Local density approximation (LDA)
The LDA functionals are purely local in the sense that they depend
solely on the **electron density $n$**:

$E_{\mathrm{xc}}^{\mathrm{LDA}}=\int\epsilon_{\mathrm{xc}}^{\mathrm{LDA}}(n)d^{3}r$

with a corresponding potential given by

$v_{\mathrm{xc}}^{\mathrm{LDA}} =
\frac{\partial\epsilon_{\mathrm{xc}}^{\mathrm{LDA}}}{\partial n}.$

The most common LDA functionals, e.g.
Slater+Perdew-Zunger,^([\[8\]](#cite_note-dirac:mpcps:1930-8)[\[9\]](#cite_note-ceperley1980-9)[\[10\]](#cite_note-perdewzunger1981-10))
provide the (nearly) exact exchange-correlation energy for the
homogeneous electron gas. However, they are in general quite inaccurate
for real systems and rarely used nowadays.

- [GGA](../incar-tags/GGA.md),[XC](../incar-tags/XC.md)

### Generalized gradient approximation (GGA)
Compared to LDA there is an additional dependency on the **gradient of
the electron density $\nabla n$**:

$E_{\mathrm{xc}}^{\mathrm{GGA}}=\int\epsilon_{\mathrm{xc}}^{\mathrm{GGA}}(n,\nabla
n)d^{3}r$

leading to an additional term in the potential:

$v_{\mathrm{xc}}^{\mathrm{GGA}} =
\frac{\partial\epsilon_{\mathrm{xc}}^{\mathrm{GGA}}}{\partial n} -
\nabla\cdot\frac{\partial\epsilon_{\mathrm{xc}}^{\mathrm{GGA}}}{\partial\nabla
n}.$

The GGA functional that has been the most commonly used in solid-state
physics is PBE,^([\[11\]](#cite_note-perdew:prl:1996-11)) and is still
widely used in particular for the geometry optimization.

- [GGA](../incar-tags/GGA.md),[XC](../incar-tags/XC.md)

### Meta generalized gradient approximation (meta-GGA)
Compared to the GGAs, the meta-GGA functionals depend additionally on
the **kinetic-energy density $\tau$**
and/or the **Laplacian of the electron density $\nabla^{2}n$**:

$E_{\mathrm{xc}}^{\mathrm{MGGA}}=\int\epsilon_{\mathrm{xc}}^{\mathrm{MGGA}}(n,\nabla
n,\nabla^{2}n,\tau)d^{3}r$

leading to

$\hat{v}_{\mathrm{xc}}^{\mathrm{MGGA}}\psi_{i} =
\frac{\delta E_{\mathrm{xc}}^{\mathrm{MGGA}}}{\delta\psi_{i}^{\*}} =
\left(\frac{\partial\epsilon_{\mathrm{xc}}^{\mathrm{MGGA}}}{\partial
n} -
\nabla\cdot\frac{\partial\epsilon_{\mathrm{xc}}^{\mathrm{MGGA}}}{\partial\nabla
n} +
\nabla^2\frac{\partial\epsilon_{\mathrm{xc}}^{\mathrm{MGGA}}}{\partial\nabla^2
n} \right)\psi_{i} -
\frac{1}{2}\nabla\cdot\left(\frac{\partial\epsilon_{\mathrm{xc}}^{\mathrm{MGGA}}}{\partial
\tau} \nabla\psi_{i}\right).$

The last term is of non-multiplicative type and arises due to the
dependency of the functional on $\tau$.^([\[12\]](#cite_note-neumann:mp:1996-12)[\[13\]](#cite_note-sun:prb:11-13))
Thus, the $\tau$-dependency leads to a
method that belongs to the generalized KS scheme.

Although meta-GGAs are slightly more expensive than GGAs, they are still
fast to evaluate and appropriate for very large systems. Furthermore,
meta-GGAs, like SCAN,^([\[14\]](#cite_note-sun:prl:15-14)) can be more
accurate than GGAs and more broadly applicable.

- [METAGGA](../incar-tags/METAGGA.md),[XC](../incar-tags/XC.md)
- [band-structure calculation using meta-GGA
  functionals](../methods/Band-structure_calculation_using_meta-GGA_functionals.md)

### Hartree-Fock (HF) and hybrid functionals
In hybrid functionals^([\[15\]](#cite_note-becke:jcp:93-15)) the
exchange part consists of a linear combination of the **HF exchange**
and a semilocal (e.g., GGA) functional:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=\alpha
E_{\mathrm{x}}^{\mathrm{HF}} +
(1-\alpha)E_{\mathrm{x}}^{\mathrm{SL}} + E_{\mathrm{c}}^{\mathrm{SL}}$

where $\alpha$ determines the relative
amount of HF and semilocal exchange. The hybrid functionals can be
divided into families according to the interelectronic range at which
the HF exchange is applied: at full range (unscreened hybrids) or either
at short or long range (called screened or range-separated hybrids).
From the practical point of view, the short-range hybrid functionals
like HSE06^([\[16\]](#cite_note-krukau:jcp:06-16)) are preferable for
periodic solids, since leading to faster convergence with respect to the
number of k-points (or size of the unit cell).

The HF method, where $E_{\mathrm{xc}}=E_{\mathrm{x}}^{\mathrm{HF}}$, is not
accurate since correlation is entirely missing, however it is the basis
of the many-body methods.

On the technical side, $E_{\mathrm{x}}^{\mathrm{HF}}$ is expensive to evaluate and,
since it is orbital-dependent, it leads to a nonlocal potential
implemented in the generalized KS scheme.

- [Hybrid
  functionals](../methods/Category-Hybrid_functionals.md)
- [Hybrid_functionals -
  formalism](../methods/Hybrid_functionals-_formalism.md)

### Exact exchange optimized-effective potential (EXX-OEP), localized Hartree-Fock (LHF), and Krieger-Li-Iafrate (KLI)
In these methods the minimization of the exact-exchange HF energy
expression is done with respect to the electron density
$n$, instead of with respect to the
orbitals $\psi_i$. That means that a
local (in the sense of multiplicative) KS potential is calculated.
EXX-OEP^([\[17\]](#cite_note-Sharp:pr:1992-17)) provides the exact
exchange potential, however, performing such calculations is non-trivial
in particular since the unoccupied orbitals are required.
LHF^([\[18\]](#cite_note-dellasala:jcp:2001-18)) is an approximation to
EXX-OEP that alleviates the use of unoccupied orbitals, while
KLI^([\[19\]](#cite_note-krieger:pra:1992-19)) is a further
approximation.

These methods are available in VASP, but not documented. Note, however,
that the tests SiC_OEP and SiC_OEPR of the testsuite use these methods.

### Density functional theory plus U (DFT+U)
The semilocal approximations, LDA and GGA in particular, often fail to
describe systems with localized (strongly correlated)
$d$ or $f$ electrons (this manifests itself primarily in the form of
unrealistic one-electron energies or too small magnetic moments). In
some cases this can be remedied by introducing on the
$d$ or $f$ atom a strong intra-atomic interaction in a simplified
(screened) Hartree-Fock like manner ($E_{\text{HF}}\[\hat{n}\]$), as an on-site replacement of the
semilocal functional:

$E_{\text{xc}}^{\text{DFT}+U}\[n,\hat{n}\] =
E_{\text{xc}}^{\text{SL}}\[n\] + E^{\text{HF}}\[\hat{n}\] -
E_{\text{dc}}\[\hat{n}\]$

where $E_{\text{dc}}\[\hat{n}\]$ is the
double-counting term, that removes some of the on-site
exchange-correlation effects present in $E_{\text{xc}}^{\text{SL}}\[n\]$, and $\hat{n}$ is the on-site occupancy matrix of the
$d$ or $f$ electrons. This approach, known as the DFT+U method
(traditionally called LSDA+U,^([\[20\]](#cite_note-anisimov:prb:91-20)))
can often be used as a cheap alternative to the much more costly hybrid
functionals. Several variants of the DFT+U method exist, differing
mostly in the expression for $E_{\text{dc}}\[\hat{n}\]$.

- [DFT+U](../methods/Category-DFT+U.md)

### van der Waals (vdW) functionals
The semilocal and hybrid functionals do not include the London
dispersion forces. Therefore, they can not be applied reliably on
systems where the London dispersion forces play an important role. To
account more properly for the London dispersion forces in DFT, a
correlation dispersion term can be added to the semilocal or hybrid
functional.^([\[21\]](#cite_note-grimme:cr:2016-21)[\[22\]](#cite_note-hermann:cr:2017-22))
This leads to the so-called **van der Waals functionals**:

$E_{\text{xc}}^{\text{vdW}} =
E_{\text{xc}}^{\text{SL/hybrid}} + E_{\text{c,disp}}.$

Most of the existing approximations for calculating
$E_{\text{c,disp}}$ belong to one of
these types: atom-pairwise, many-body dispersion, or nonlocal vdW-DF
functionals.

- [Van der Waals
  functionals](../methods/Category-Van_der_Waals_functionals.md)

### Many-body methods
Methods based on many-body perturbation theory provide a first-principle
approach to the correlation effects. They allow to calculate accurately
the total energy or the electronic structure of materials. Such methods
lie formally outside the DFT framework, although strong connections to
DFT can be
made.^([\[23\]](#cite_note-capelle:bjp:2006-23)[\[24\]](#cite_note-kuemmel:rmp:2008-24))
Some of the most known many-body methods are the random-phase
approximation (RPA) and GW. The disadvantage of these methods is to be
computationally much more expensive than DFT.

Also quite popular is
DFT+DMFT,^([\[25\]](#cite_note-kotliar:rmp:2006-25)) which is a
non-perturbative method to calculate the correlation effects. It can be
regarded as a many-body extension of DFT+U and is also mainly used for
systems with strongly correlated $d$ or
$f$ electrons.

- [Many-body perturbation
  theory](Category-Many-body_perturbation_theory.md)
- [DFT+DMFT](../tutorials/DFT+DMFT_calculations.md)

## References
1.  [↑](#cite_ref-hohenberg:pr:1964_1-0) [P. Hohenberg and W. Kohn,
    Phys. Rev. **136**, B864
    (1964).](https://doi.org/10.1103/PhysRev.136.B864)
2.  ↑ ^([a](#cite_ref-kohn:pr:1965_2-0))
    ^([b](#cite_ref-kohn:pr:1965_2-1)) [W. Kohn and L. J. Sham,
    *Self-Consistent Equations Including Exchange and Correlation
    Effects*, Phys. Rev. **140**, A1133
    (1965).](https://doi.org/10.1103/PhysRev.140.A1133)
3.  [↑](#cite_ref-seidl:prb:96_3-0) [A. Seidl, A. Görling, P. Vogl, J.A.
    Majewski, and M. Levy, Phys. Rev. B **53**, 3764
    (1996).](https://doi.org/10.1103/PhysRevB.53.3764)
4.  ↑ ^([a](#cite_ref-libxc_list_4-0)) ^([b](#cite_ref-libxc_list_4-1))
    [https://libxc.gitlab.io/functionals/](https://libxc.gitlab.io/functionals/)
5.  ↑ ^([a](#cite_ref-tran:arxiv:2026_5-0))
    ^([b](#cite_ref-tran:arxiv:2026_5-1)) [F. Tran, S. Lehtola, S.
    Pittalis, and M. A. L. Marques, *Semi-Local Exchange-Correlation
    Approximations in Density Functional Theory*, arXiv **2602.17333**
    (2026).](https://doi.org/10.48550/arXiv.2602.17333)
6.  ↑ ^([a](#cite_ref-dellasala:ijqc:2016_6-0))
    ^([b](#cite_ref-dellasala:ijqc:2016_6-1)) [F. Della Sala, E.
    Fabiano, and L. A. Constantin, *Kinetic-energy-density dependent
    semilocal exchange-correlation functionals*, Int. J. Quantum Chem.
    **116**, 1641 (2016).](https://doi.org/10.1002/qua.25224)
7.  ↑ ^([a](#cite_ref-mardirossian:mp:2017_7-0))
    ^([b](#cite_ref-mardirossian:mp:2017_7-1)) [N. Mardirossian and M.
    Head-Gordon, *Thirty years of density functional theory in
    computational chemistry: an overview and extensive assessment of 200
    density functionals*, Mol. Phys. **115**, 2315
    (2017).](https://doi.org/10.1080/00268976.2017.1333644)
8.  [↑](#cite_ref-dirac:mpcps:1930_8-0) [P. A. M. Dirac, Math. Proc.
    Cambridge Philos. Soc. **26**, 376
    (1930).](https://doi.org/10.1017/S0305004100016108)
9.  [↑](#cite_ref-ceperley1980_9-0) [D. M. Ceperley and B. J. Alder,
    Phys. Rev. Lett. **45**, 566
    (1980).](https://doi.org/10.1103/PhysRevLett.45.566)
10. [↑](#cite_ref-perdewzunger1981_10-0) [J. P. Perdew and A. Zunger,
    Phys. Rev. B **23**, 5048
    (1981).](https://doi.org/10.1103/PhysRevB.23.5048)
11. [↑](#cite_ref-perdew:prl:1996_11-0) [J. P. Perdew, K. Burke, and M.
    Ernzerhof, Phys. Rev. Lett., **77**, 3865
    (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
12. [↑](#cite_ref-neumann:mp:1996_12-0) [R. Neumann, R. H. Nobes,
    and N. C. Handy, *Exchange functionals and potentials*, Mol. Phys.
    **87**, 1 (1996).](https://doi.org/10.1080/00268979600100011)
13. [↑](#cite_ref-sun:prb:11_13-0) [J. Sun, M. Marsman, G. Csonka, A.
    Ruzsinszky, P. Hao, Y.-S. Kim, G. Kresse, and J. P. Perdew, Phys.
    Rev. B **84**, 035117
    (2011).](https://doi.org/10.1103/PhysRevB.84.035117)
14. [↑](#cite_ref-sun:prl:15_14-0) [J. Sun, A. Ruzsinszky, and J. P.
    Perdew, Phys. Rev. Lett. **115**, 036402
    (2015).](https://doi.org/10.1103/PhysRevLett.115.036402)
15. [↑](#cite_ref-becke:jcp:93_15-0) [A. D. Becke, J. Chem. Phys.
    **98**, 5648 (1993).](https://doi.org/10.1063/1.464913)
16. [↑](#cite_ref-krukau:jcp:06_16-0) [A. V. Krukau , O. A.
    Vydrov, A. F. Izmaylov, and G. E. Scuseria, J. Chem. Phys. **125**,
    224106 (2006).](https://doi.org/10.1063/1.2404663)
17. [↑](#cite_ref-Sharp:pr:1992_17-0) [R. T. Sharp and G. K. Horton, *A
    Variational Approach to the Unipotential Many-Electron Problem*,
    Phys. Rev. **90**, 317
    (1953).](https://doi.org/10.1103/PhysRev.90.317)
18. [↑](#cite_ref-dellasala:jcp:2001_18-0) [F. Della Sala and A.
    Görling, *Efficient localized Hartree–Fock methods as effective
    exact-exchange Kohn–Sham methods for molecules*, J. Chem. Phys.
    **115**, 5718 (2001).](http://doi.org/10.1063/1.1398093)
19. [↑](#cite_ref-krieger:pra:1992_19-0) [J. B. Krieger, Y. Li,
    and G. J. Iafrate, *Construction and application of an accurate
    local spin-polarized Kohn-Sham potential with integer discontinuity:
    Exchange-only theory*, Phys. Rev. A **45**, 101
    (1992).](https://doi.org/10.1103/PhysRevA.45.101)
20. [↑](#cite_ref-anisimov:prb:91_20-0) [V. I. Anisimov, J. Zaanen,
    and O. K. Andersen, Phys. Rev. B **44**, 943
    (1991).](https://doi.org/10.1103/PhysRevB.44.943)
21. [↑](#cite_ref-grimme:cr:2016_21-0) [S. Grimme, A. hansen, J. G.
    Brandenburg, and C. Bannwarth, *Dispersion-Corrected Mean-Field
    Electronic Structure Methods*, Chem. Rev. **116**, 5105
    (2016).](https://doi.org/10.1021/acs.chemrev.5b00533)
22. [↑](#cite_ref-hermann:cr:2017_22-0) [J. Hermann, R. A. DiStasio Jr.,
    and A. Tkatchenko, *First-Principles Models for van der Waals
    Interactions in Molecules and Materials: Concepts, Theory, and
    Applications*, Chem. Rev. **117**, 4714
    (2017).](https://doi.org/10.1021/acs.chemrev.6b00446)
23. [↑](#cite_ref-capelle:bjp:2006_23-0) [K. Capelle, *A Bird’s-Eye View
    of Density-Functional Theory*, Braz. J. Phys. **36**, 1318
    (2006).](https://doi.org/10.1590/S0103-97332006000700035)
24. [↑](#cite_ref-kuemmel:rmp:2008_24-0) [S. Kümmel and L. Kronik,
    *Orbital-dependent density functionals: Theory and applications*,
    Rev. Mod. Phys. **80**, 3
    (2008).](http://doi.org/10.1103/RevModPhys.80.3)
25. [↑](#cite_ref-kotliar:rmp:2006_25-0) [G. Kotliar, S. Y. Savrasov, K.
    Haule, V. S. Oudovenko, O. Parcollet, and C. A. Marianetti,
    *Electronic structure calculations with dynamical mean-field
    theory*, Rev. Mod. Phys. **78**, 865
    (2006)](https://link.aps.org/doi/10.1103/RevModPhys.78.865)

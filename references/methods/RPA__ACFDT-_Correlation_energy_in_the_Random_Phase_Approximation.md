<!-- Source: https://vasp.at/wiki/index.php/RPA/ACFDT:_Correlation_energy_in_the_Random_Phase_Approximation | revid: 35515 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# RPA/ACFDT: Correlation energy in the Random Phase Approximation
## Contents

- [1 Diagrammatic approach to the correlation
  energy](#Diagrammatic_approach_to_the_correlation_energy)
  - [1.1 Gell-Mann and Low theorem](#Gell-Mann_and_Low_theorem)
  - [1.2 Diagrammatic perturbation
    theory](#Diagrammatic_perturbation_theory)
- [2 The random-phase approximation](#The_random-phase_approximation)
- [3 Computational Complexity](#Computational_Complexity)
  - [3.1 Quartic scaling RPA: Direct
    calculation](#Quartic_scaling_RPA:_Direct_calculation)
  - [3.2 Cubic scaling RPA: Contraction of imaginary time Green's
    functions](#Cubic_scaling_RPA:_Contraction_of_imaginary_time_Green's_functions)
- [4 Basis set convergence of RPA-ACFDT
  calculations](#Basis_set_convergence_of_RPA-ACFDT_calculations)
- [5 Matsubara Formalism: Metallic systems at finite
  Temperature](#Matsubara_Formalism:_Metallic_systems_at_finite_Temperature)
- [6 Related tags and articles](#Related_tags_and_articles)
- [7 References](#References)

ACFDT stands for the adiabatic connection fluctuation dissipation
theorem and is an alternative way to derive the energy expression for
the correlation energy in the random phase approximation (RPA). In the
following, the diagrammatic description is presented. For the ACFDT
formulation, the reader is referred to the
literature.^([\[1\]](#cite_note-harl:2008-1)) There is also a lecture
[introducing RPA](https://youtu.be/0hV5bTpY89M) on our YouTube channel.

## Diagrammatic approach to the correlation energy
The correlation energy $E_c$ is defined
as the missing piece of the Hartree-Fock energy $E_{x}$ to the total energy, that is $E_{tot} = E_{x} + E_c$. The exact form of
$E_c$ is unknown and can be calculated
only approximately for a realistic system. The Random Phase
Approximation (RPA) is such an approximation that provides access to
$E_c$. The RPA was first studied by Bohm
and Pines for the homogeneous electron gas and was later recognized by
Gell-Mann and Brueckner as an approximation of $E_c$ that can be expressed in the same language as Feynman
used a few years earlier to describe the positron.
^([\[2\]](#cite_note-bohm:pr:82-2)[\[3\]](#cite_note-gell-mann:pr:106-3)[\[4\]](#cite_note-feynman:pr:76-4))

Feynman's diagrammatic approach is based on quantum field theory (QFT),
which in turn is based on the Gell-Mann and Low theorem. This theorem
states that the eigenstate of an interacting Hamiltonian can be
expressed in terms of the eigenstates of the non-interacting
one.^([\[5\]](#cite_note-gell-mann:pr:84-5)) For this reason, each
diagrammatic calculation, like the RPA or
[GW](GW_approximation_of_Hedin's_equations.md),
requires the solution of the non-interacting Hamiltonian
$H_0$ of the system, like for instance
the Hartree-Fock energies and orbitals or the solutions of the Kohn-Sham
Hamiltonian $\epsilon_{n\bf k}, \phi_{n\bf k}$.

QFT is commonly formulated in the Dirac (also known as interaction)
picture, where dynamics described by the interaction part
$\hat V$ of the fully interacting
Hamiltonian $\hat H=\hat H_0+\hat V$ are
singled out via time-dependent operators like $\hat V(t)=e^{i\hat H_0t}\hat Ve^{-i\hat H_0t}$. These
operators act on states like the non-interacting groundstate of the
system $|\Psi_0\rangle$, causing
fluctuations at a specific point in time. The main idea of QFT is to
understand observations, which can be measured by an observer, as a
collective phenomenon of all possible
fluctuations.^([\[6\]](#cite_note-mattuck:2012-6))

Thereby, fluctuations are understood as the creation of virtual
electrons (and holes) that interact with each other and are annihilated
after some time. Formally this is achieved by introducing creation
$\hat\psi^\dagger({\bf r},t)$ and
annihilation operators $\hat\psi({\bf r},t)$ that satisfy following relations

$\hat\psi({\bf r},t)|\Psi_0\rangle = 0 =\langle
\Psi_0 | \hat\psi({\bf r},t)$

$\lbrace \psi({\bf r},t),\psi^\dagger({\bf
r},t)\rbrace = \psi^\dagger({\bf r},t)\psi^\dagger({\bf r},t) +
\psi^\dagger({\bf r},t),\psi({\bf r},t) = i\delta({\bf r}-{\bf r}')$

$\lbrace\psi^\dagger({\bf r},t),\psi^\dagger({\bf
r},t) \rbrace = 0 = \lbrace\psi({\bf r},t),\psi({\bf r},t) \rbrace.$

The first relation defines the non-interacting groundstate
$|\Psi_0\rangle$ as the Fermi vacuum
(the groundstate in the absence of any fluctuations), while the second
and third anti-commutator relations are a consequence of the Pauli
principle. In fact, all operators that describe measurable quantities of
a system of interacting electrons can be represented in terms of
$\psi^\dagger({\bf r},t)$ and
$\psi({\bf r},t)$ alone; additional
objects are not necessary.

However, the time-ordering operator

$\hat T \hat A(t)\hat B(t') = \Theta(t-t') \hat
A(t)\hat B(t') - \Theta(t'-t)\hat B(t')\hat A(t),$

where $\Theta(t)$ is the unit step
function, and the time-evolution operator

$\hat S(t,t_0)=\hat T e^{-i\int_{t_0}^t \hat
V(t'){\rm d}t'}$

are helpful quantities, since they allow to formulate the Gell-Mann and
Low theorem as follows.

### Gell-Mann and Low theorem
Using adiabatic coupling of the interaction $\hat
V(t) \to \hat V_\eta(t) = e^{-\eta|t|} \hat V$, Gell-Mann
and Low proved that the vectors

$\frac{|\Omega_\nu\rangle}{\langle
\Omega_\nu|\Psi_\nu\rangle} =\lim_{\eta\to0}\frac{\hat
S_\eta(0,-\infty)|\Psi_\nu\rangle}{\langle
\Omega_\nu|\Psi_\nu\rangle}$

are the eigenstates of the interacting
Hamiltonian.^([\[5\]](#cite_note-gell-mann:pr:84-5))

We follow the common literature and suppress the infinitesimal
$\eta$ in the following bearing in mind
that the limit $\eta \to 0$ is performed
at the very end of the
calculation.^([\[7\]](#cite_note-negele:1988-7)[\[8\]](#cite_note-fetter:2003-8))

### Diagrammatic perturbation theory
A consequence of the Gell-Mann and Low theorem, is the following form of
the interacting groundstate energy^([\[8\]](#cite_note-fetter:2003-8))

$E_{tot}=E_0 = \langle \Omega_0|\hat
H|\Omega_0\rangle = \frac{\langle\Psi_0| \hat S(\infty,-\infty)\hat
H|\Psi_0\rangle}{\langle \Psi_0|\hat
S(\infty,-\infty)|\Psi_0\rangle},$

which can be seen as starting point of diagrammatic perturbation theory.
The expression above is used to derive all possible approximations by
expanding the time-evolution operator $\hat S$ into a series. The resulting matrix-elements of creation and
annihilation operators are evaluated term by term using the canonical
anti-commutator relations defined above (Wick's
theorem^([\[9\]](#cite_note-wick:1950-9))). It follows that all terms in
perturbation theory are expressed by only two quantities, the
non-interacting Feynman propagator

$G_0(1,2) = -i \sum_{n{\bf k}} \phi({\bf
r}_2)\phi^\*({\bf r}_1) e^{-i(\epsilon_{n \bf
k}-\epsilon_F)(t_2-t_1)}\left\[ f_{n\bf k}\Theta(t_2-t_1) - (1-f_{n\bf
k})\Theta(t_1-t_2)\right\], \quad 1 = ({\bf r}_1,t_1), 2 = ({\bf
r}_2,t_2)$

and the Coulomb interaction

$V(1,2) = \frac{\delta( t_1-t_2)}{|{\bf
r}_1-{\bf r}_2|}.$

Then, each term in the series corresponds to an integral over space-time
coordinates $({\bf r},t)$.

Feynman diagrams are used to illustrate which terms are considered in
the perturbation series. The illustration is usually achieved with
so-called Feynman rules that map a specific diagram to an integral (and
vice versa). For instance the second order diagram

[![](https://vasp.at/wiki/images/thumb/d/df/DMP2.png/100px-DMP2.png)](https://vasp.at/wiki/File:DMP2.png)

is also known as the direct Møller-Plessett term and stands for
following integral

$E^{(2)}_{\rm dMP}=\int{\rm d}(1,2,3,4)
G_0(1,2)G_0(2,1) V(1,3)V(2,4) G_0(3,4)G_0(4,3), \quad {\rm
d}(1,\cdots,4) = {\rm d}{\bf r}_1{\rm d}t_1\cdots {\rm d}{\bf r}_4{\rm
d}t_4$

All Feynman rules can be found in the book of Negele and Orland or
elsewhere.^([\[7\]](#cite_note-negele:1988-7)[\[8\]](#cite_note-fetter:2003-8))

## The random-phase approximation
The RPA is obtained from neglecting all second and higher order terms in
the perturbation series of the groundstate energy, except of those which
can be expressed soley in terms of the independent particle
polarizability

$\chi_0(1,2) = -i G_0(1,2) G_0(2,1)$

corresponding to the "bubble" diagram

[![](https://vasp.at/wiki/images/thumb/8/8b/Chi.png/50px-Chi.png)](https://vasp.at/wiki/File:Chi.png)

Because of the symmetric time property $\chi_0(t_2-t_1)=\chi_0(t_1-t_2)$, the independent particle
polarizability is of bosonic character. Because the RPA neglects all
non-bosonic terms in the perturbation series, it corresponds essentially
to a "bosonization" of the many-body problem for which the n-th order
term can be written analytically as^([\[7\]](#cite_note-negele:1988-7))

$E^{(n)}_{\rm dMP} =
\frac1{2n}\int_{-\infty}^\infty\frac{{\rm d}\omega}{2\pi} {\rm
Tr}\left\[ \tilde \chi_0(\omega) \cdot V \right\]^n.$

Here, the trace of the matrix product is most effectively done in
reciprocal space $\left\[\tilde \chi_0(\omega)
\cdot V\right\]({\bf q+G}_1,{\bf q+G}_2) = \sum_{\bf G} \tilde
\chi_0({\bf q+G}_1,{\bf G},\omega)V({\bf q+G},{\bf q+G}_2)$
using the Fourier transformed polarizability $\tilde \chi_0({\bf q+G}_1,{\bf q+G}_2,\omega)$, the diagonal
Coulomb potential $V({\bf q+G}_1,{\bf
q+G}_2)=\frac{ \delta_{ {\bf G}_1 {\bf G}_2 } }{|{\bf q+G}_1|}$ and the conserved crystal momentum ${\bf q}$ in the first Brillouin zone.

All bubble terms of order $n \ge 2$ can
be written in a closed form using the series for the logarithm
$\ln(1-x)+x=-\sum_{n=2}^\infty \frac{x^n}{n}$ and define the correlation part of the RPA energy

$E_c^{\rm RPA} = \int\frac{ {\rm d}\omega}{2\pi}
{\rm Tr}\left\lbrace \ln\left\[ 1-\tilde \chi_0(\omega)\cdot V
\right\] + \tilde \chi_0(\omega)\cdot V \right\rbrace.$

There are two first order contributions to the total energy that yield
the exact exchange energy $E_x=T+V_{ext}+V_h+V_x$, which is usually determined separately.

## Computational Complexity
The calculation of the RPA integral requires the determination of the
independent particle polarizability matrix $\tilde
\chi^0_{\bf GG'}({\bf q},\omega_n)=\tilde \chi_0({\bf q+G},{\bf
q+G}',\omega_n)$ on each of the $N_{\bf
q}$ sampling points of the first Brillouin zone for
$N_{\omega}$ frequency points. The
number of frequency points is reduced drastically, by performing the
integration over the imaginary frequency axis $\omega\to i\omega$.^([\[10\]](#cite_note-kaltak:2014-10))

The independent particle polarizability on the imaginary axis can be
determined with two alternative methods.

### Quartic scaling RPA: Direct calculation
Direct calculation of $\tilde\chi^0$
using the formula of Adler and
Wiser^([\[11\]](#cite_note-adler:1962-11))
^([\[12\]](#cite_note-wiser:1963-12))

$\tilde\chi^0_{{\bf GG}'}({\bf q},i\omega) =
\sum\limits_{{\bf k}\in BZ}\sum\limits_{n,n'} \frac{ f_{n{\bf k}}(1 -
f_{n{\bf k-q}}) }{ \epsilon_{n{\bf k-q}}-\epsilon_{n{\bf k}} -i
\omega } \langle \phi_{n {\bf k-q}} | e^{i{\bf Gr}} | \phi_{n'{\bf
k}} \rangle \langle \phi_{n' {\bf k}} | e^{-i{\bf G'r'}} |
\phi_{n'{\bf k-q}} \rangle$

yields an RPA algorithm that has a computational cost of
$N_\omega N_{\bf k}^2 N_{\bf G}^4$.
Because the number of plane waves $N_{\bf G}$ scales linearly with the system size (number of electrons in
the unit cell), the direct calculation of the polarizability is
unfavourable for large system sizes, e.g. for more than ~20 atoms in the
unit cell.

### Cubic scaling RPA: Contraction of imaginary time Green's functions
An alternative way to determine $\tilde\chi^0$ is to frist determine imaginary time Green's functions of the
form^([\[13\]](#cite_note-rojas:prl:1995-13))

$G_0({\bf r,r'},i\tau) = \sum\limits_{{\bf k}\in
BZ}\sum\limits_{n} \phi_{n{\bf k}}({\bf r})\phi_{n \bf k}^\*({\bf
r'}) e^{-(\epsilon_{n\bf k}-\epsilon_{F})\tau}\left\[
\Theta(-\tau)f_{n\bf k}-\Theta(\tau)(1-f_{n\bf k}) \right\]$

and to perform afterwards a Fourier transformation into reciprocal and
imaginary frequency space of

$\chi_0({\bf r,r'},i\tau) = -G_0({\bf r,r'},i\tau)
G_0({\bf r',r},-i\tau).$

Although more evolved, this approach has the advantage that the
computational cost for the determination of $\tilde \chi_0$ scales with $N_\omega
N_{\bf k} N_{\bf G}^3$ and is essentially only cubic in
system size. The space-time method allows to study relatively large
systems with the RPA.^([\[14\]](#cite_note-kaltak:prb:2014-14))

## Basis set convergence of RPA-ACFDT calculations
The expression for the ACFDT-RPA correlation energy written in terms of
reciprocal lattice vectors reads:

$E_{\rm c}^{\rm RPA}=\int_{0}^{\infty}
\frac{\mathrm{d}\omega}{2\pi} \sum_{{\mathbf{q}}\in \mathbf{BZ}
}\sum_{{\mathbf{G}}}
\left\\(\mathrm{ln}\[1-\tilde\chi^0({\mathbf{q}},\mathrm{i}\omega)V({\mathbf{q}})\])_{{\mathbf{G,G}}}
+V_{{\mathbf{G,G}}}({\mathbf{q}})\tilde\chi^0({\mathbf{q}},{\mathrm{i}}\omega)
\right\\$.

The sum over reciprocal lattice vectors has to be truncated at some
$\mathbf{G}_{\mathrm{max}}$, determined
by $\frac{\hbar^2|{\mathbf{G}}+{\mathbf{q}}|^2}{2\mathrm{m}_e}$
\< [ENCUTGW](../incar-tags/ENCUTGW.md), which can be set in the
[INCAR](../input-files/INCAR.md) file. The default value is
$\frac{2}{3}\times$
[ENCUT](../incar-tags/ENCUT.md), which experience has taught us not to
change. For systematic convergence tests, instead increase
[ENCUT](../incar-tags/ENCUT.md) and repeat steps 1 to 4, but be aware that
the "maximum number of plane-waves" changes when
[ENCUT](../incar-tags/ENCUT.md) is increased. Note that it is virtually
impossible, to converge absolute correlation energies. Rather
concentrate on relative energies (e.g. energy differences between two
solids, or between a solid and the constituent atoms).

Since correlation energies converge very slowly with respect to
$\mathbf{G}_{\rm max }$, VASP
automatically extrapolates to the infinite basis set limit using a
linear regression to the equation:
^([\[1\]](#cite_note-harl:2008-1)[\[15\]](#cite_note-harl:2010-15)[\[16\]](#cite_note-klimes:2014-16))

$E_{\mathrm{c}}({\mathbf{G}})=E_{\mathrm{c}}(\infty)+\frac{A}{{\mathbf{G}}^3}$.

Furthermore, the Coulomb kernel is smoothly truncated between
[ENCUTGWSOFT](../incar-tags/ENCUTGWSOFT.md) and
[ENCUTGW](../incar-tags/ENCUTGW.md) using a simple cosine like window
function (Hann window function). Alternatively, the basis set
extrapolation can be performed by setting
[LSCK](../incar-tags/LSCK.md)=.TRUE., using the squeezed Coulomb kernel
method.^([\[17\]](#cite_note-riemelmoser:jcp:2020-17))

The default for [ENCUTGWSOFT](../incar-tags/ENCUTGWSOFT.md) is
0.8$\times$[ENCUTGW](../incar-tags/ENCUTGW.md) (again we do not recommend
to change this default).

The integral over $\omega$ is evaluated
by means of a highly accurate minimax
integration.^([\[10\]](#cite_note-kaltak:2014-10)) The number of
$\omega$ points is determined by the
flag [NOMEGA](../incar-tags/NOMEGA.md), whereas the energy range of
transitions is determined by the band gap and the energy difference
between the lowest occupied and highest unoccupied one-electron orbital.
VASP determines these values automatically (from vasp.5.4.1 on), and the
user should only carefully converge with respect to the number of
frequency points [NOMEGA](../incar-tags/NOMEGA.md). A good choice is
usually [NOMEGA](../incar-tags/NOMEGA.md)=12, however, for large gap
systems one might obtain $\mu$eV
convergence per atom already using 8 points, whereas for metals up to
[NOMEGA](../incar-tags/NOMEGA.md)=24 frequency points are sometimes
necessary, in particular, for large unit cells.

Strictly adhere to the steps outlines above. Specifically, be aware that
steps two and three require the [WAVECAR](../input-files/WAVECAR.md) file
generated in step one, whereas step four requires the
[WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) file generated in step three
(generated by setting [LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.*).

  

## Matsubara Formalism: Metallic systems at finite Temperature
The zero-temperature formalism of many-body perturbation theory breaks
down for metals (systems with zero energy band-gap) as pointed out by
Kohn and Luttinger.^([\[18\]](#cite_note-KohnLuttinger:PR:1960-18)) This
conundrum is lifted by considering diagrammatic perturbation theory at
finite temperature $T>0$, which may be
understood by an analytical continuation of the real-time
$t$ to the imaginary time axis
$-i\tau$. Matsubara has shown that this
Wick rotation in time $t\to-i\tau$
reveals an intriguing connection to the inverse temperature
$\beta=1/T$ of the
system.^([\[19\]](#cite_note-Matsubara:PTP:1955-19)) More precisely,
Matsubara has shown that all terms in perturbation theory at finite
temperature can be expressed as integrals of imaginary time quantities
(such as the polarizability $\chi(-i\tau)$) over the fundamental interval $-\beta\le\tau\le\beta$.

As a consequence, one decomposes imaginary time quantities into a
Fourier series with period $\beta$ that
determines the spacing of the Fourier modes. For instance the imaginary
polarizability can be written as

$\chi(-i\tau)=\frac1\beta\sum_{m=-\infty}^\infty
\tilde \chi(i\nu_m)e^{-i\nu_m\tau},\quad \nu_m=\frac{2m}\beta\pi$

and the corresponding random-phase approximation of the correlation
energy at finite temperature becomes a series over (in this case,
bosonic) Matsubara frequencies

$\Omega_c^{\rm RPA}=\frac12\frac1\beta
\sum_{m=-\infty}^\infty {\rm Tr}\left\lbrace \ln\left\[ 1 -\tilde
\chi(i\nu_m) V \right\] -\tilde \chi(i\nu_m) V \right\rbrace,\quad
\nu_m=\frac{2m}\beta\pi$

The Matsubara formalism has the advantage that all contributions to the
Green's function and the polarizability are mathematically well-defined,
including contributions from states close to the chemical potential
$\epsilon_{n{\bf k}}\approx \mu$, such
that Matsubara series also converge for metallic systems.

Although formally convenient, the Matsubara series converges poorly with
the number of considered terms in practice. VASP, therefore, uses a
compressed representation of the Fourier modes by employing the
Minimax-Isometry method.^([\[20\]](#cite_note-Kaltak:PRB:2020-20)) This
approach converges exponentially with the number of considered frequency
points.

## Related tags and articles
- [ACFDT/RPA
  calculations](ACFDT__RPA_calculations.md) —
  practical step-by-step guide
- [Many-body perturbation
  theory](../redirects/Many-body_perturbation_theory.md)
  — parent topic (RPA, GW, BSE, MP2)
- [Low-scaling GW and
  RPA](../theory/Category-Low-scaling_GW_and_RPA.md)
  — low-scaling algorithms
- [ALGO](../incar-tags/ALGO.md) for response functions and ACFDT
  calculations
- [ENCUTGW](../incar-tags/ENCUTGW.md), to set cutoff for response
  functions
- [NOMEGA](../incar-tags/NOMEGA.md), number of frequency points
- [LFINITE_TEMPERATURE](../incar-tags/LFINITE_TEMPERATURE.md)
  switches on Matsubara (finite temperature) formalism

## References
1.  ↑ ^([a](#cite_ref-harl:2008_1-0)) ^([b](#cite_ref-harl:2008_1-1))
    [J. Harl and G. Kresse, Phys. Rev. B **77**, 045136
    (2008).](https://doi.org/10.1103/PhysRevB.81.115126)
2.  [↑](#cite_ref-bohm:pr:82_2-0) [D. Bohm and D. Pines, J. Phys.
    **82**, 625 (1951).](https://doi.org/10.1103/PhysRev.82.625)
3.  [↑](#cite_ref-gell-mann:pr:106_3-0) [M. Gell-Mann and K.
    Brueckner, J. Phys. **106**, 364
    (1957).](https://doi.org/10.1103/PhysRev.106.364)
4.  [↑](#cite_ref-feynman:pr:76_4-0) [R. P. Feynman, J. Phys. **76**,
    749 (1948).](https://doi.org/10.1103/PhysRev.76.749)
5.  ↑ ^([a](#cite_ref-gell-mann:pr:84_5-0))
    ^([b](#cite_ref-gell-mann:pr:84_5-1)) [M. Gell-Mann and F. Low, J.
    Phys. **84**, 350 (1951).](https://doi.org/10.1103/PhysRev.84.350)
6.  [↑](#cite_ref-mattuck:2012_6-0) [R. D. Mattuck, Dover Books on
    Physics
    (2012).](https://books.google.at/books?id=1P_DAgAAQBAJ&hl=en)
7.  ↑ ^([a](#cite_ref-negele:1988_7-0))
    ^([b](#cite_ref-negele:1988_7-1)) ^([c](#cite_ref-negele:1988_7-2))
    [J. Negele and H. Orland, Frontiers in Physics
    (1988).](https://books.google.at/books/about/Quantum_many_particle_systems.html?id=EV8sAAAAYAAJ&redir_esc=y)
8.  ↑ ^([a](#cite_ref-fetter:2003_8-0))
    ^([b](#cite_ref-fetter:2003_8-1)) ^([c](#cite_ref-fetter:2003_8-2))
    [A. L. Fetter and J. D. Walecka, Dover Books on Physics
    (2003).](https://books.google.at/books/about/Quantum_Theory_of_Many_particle_Systems.html?id=0wekf1s83b0C&redir_esc=y)
9.  [↑](#cite_ref-wick:1950_9-0) [G. C. Wick, Phys. Rev. **80**, 268
    (1950).](https://doi.org/10.1103/PhysRev.80.268)
10. ↑ ^([a](#cite_ref-kaltak:2014_10-0))
    ^([b](#cite_ref-kaltak:2014_10-1)) [M. Kaltak, J. Klimeš, and G.
    Kresse, J. Chem. Theory Comput. **10**, 2498-2507
    (2014).](https://doi.org/10.1021/ct5001268)
11. [↑](#cite_ref-adler:1962_11-0) [S. L. Adler, Phys. Rev. **126**, 413
    (1962)](https://doi.org/10.1103/PhysRev.126.413)
12. [↑](#cite_ref-wiser:1963_12-0) [N. Wiser, Phys. Rev. **129**, 62
    (1963)](https://doi.org/10.1103/PhysRev.129.62)
13. [↑](#cite_ref-rojas:prl:1995_13-0) [H. N. Rojas, R. W. Godby,
    and R. J. Needs, Phys. Rev. Lett. **74**, 1827
    (1995).](https://doi.org/10.1103/PhysRevLett.74.1827)
14. [↑](#cite_ref-kaltak:prb:2014_14-0) [M. Kaltak, J. Klimeš, and G.
    Kresse, Phys. Rev. B **90**, 054115
    (2014).](https://doi.org/10.1103/PhysRevB.90.054115)
15. [↑](#cite_ref-harl:2010_15-0) [J. Harl, L. Schimka, and G. Kresse,
    Phys. Rev. B **81**, 115126
    (2010).](https://doi.org/10.1103/PhysRevB.81.115126)
16. [↑](#cite_ref-klimes:2014_16-0) [J. Klimeš, M. Kaltak, and G.
    Kresse, Phys. Rev. B **90**, 075125
    (2014).](https://doi.org/10.1103/PhysRevB.90.075125)
17. [↑](#cite_ref-riemelmoser:jcp:2020_17-0) [S. Riemelmoser, M. Kaltak,
    and G. Kresse, J. Chem. Phys. **152(13)**, 134103
    (2020).](https://doi.org/10.1063/5.0002246)
18. [↑](#cite_ref-KohnLuttinger:PR:1960_18-0) [W. Kohn and J. M.
    Luttinger, Phys. Rev. **118**, 41
    (1960).](https://doi.org/10.1103/PhysRev.118.41)
19. [↑](#cite_ref-Matsubara:PTP:1955_19-0) [T. Matsubara, Prog. Theor.
    Phys. **14**, 351 (1955).](https://doi.org/10.1143/PTP.14.351)
20. [↑](#cite_ref-Kaltak:PRB:2020_20-0) [M. Kaltak and G. Kresse, Phys.
    Rev. B. **101**, 205145
    (2020).](https://doi.org/10.1103/PhysRevB.101.205145)

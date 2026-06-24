<!-- Source: https://vasp.at/wiki/index.php/GW_approximation_of_Hedin%27s_equations | revid: 24251 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GW approximation of Hedin's equations
## Contents

- [1 Green's functions](#Green's_functions)
- [2 Single Shot: G₀W₀](#Single_Shot:_G0W0)
- [3 Partially self-consistent: GW₀ or
  EVGW₀](#Partially_self-consistent:_GW0_or_EVGW0)
- [4 Self-consistent Quasi-particle approximation:
  scQPGW₀](#Self-consistent_Quasi-particle_approximation:_scQPGW0)
- [5 Low-scaling GW: The Space-time
  Formalism](#Low-scaling_GW:_The_Space-time_Formalism)
- [6 Theory](#Theory)
- [7 Limitations of GW](#Limitations_of_GW)
- [8 References](#References)

## Green's functions
The GW method can be understood in terms of the following eigenvalue
equation^([\[1\]](#cite_note-HybertsenLouie-1))

$(T+V_{ext}+V_h)\phi_{n{\bf k}}({\bf r})+\int
d{\bf r}\Sigma({\bf r},{\bf r}',\omega=E_{n{\bf k}})\phi_{n{\bf
k}}({\bf r}') = E_{n{\bf k}}\phi_{n{\bf k}}({\bf r})$

Here $T$ is the kinetic energy,
$V_{ext}$ the external potential of the
nuclei, $V_h$ the Hartree potential and
$E_{n{\bf k}}$ the quasiparticle
energies with orbitals $\phi_{n{\bf k}}$. In contrast to DFT, the exchange-correlation potential is
replaced by the many-body self-energy $\Sigma$ and should be obtained together with the Green's function
$G$, the irreducible polarizability
$\chi$, the screened Coulomb interaction
$W$ and the irreducible vertex function
$\Gamma$ in a self-consistent procedure.
For completeness, these equations are^([\[2\]](#cite_note-Hedin-2))

$G(1,2)=G_0(1,2)+\int d(3,4)
G_0(1,3)\Sigma(3,4)G(4,2)$

$\chi(1,2)=\int d(3,4) G(1,3)G(4,1)\Gamma(3,4;2)$

$W(1,2)=V(1,2)+\int d(3,4) V(1,3)\chi(3,4)W(4,2)$

$\Sigma(1,2)=\int d(3,4) G(1,3)\Gamma(3,2;4)W(4,1)$

$\Gamma(1,2;3)=\delta(1,2)\delta(1,3)+\int
d(4,5,6,7)\frac{\delta\Sigma(1,2)}{\delta
G(4,5)}G(4,6)G(7,5)\Gamma(6,7;3)$

Here the common notation $1=({\bf r}_1,t_1)$ was adopted and $V$ denotes
the bare Coulomb interaction. Note, that these equations are exact and
provide an alternative to the Schrödinger equation for the many-body
problem. Nevertheless, approximations are necessary for realistic
systems. The most popular one is the GW approximation and is obtained by
neglecting the equation for the vertex function and using the bare
vertex instead:

$\Gamma(1,2;3)=\delta(1,2)\delta(1,3)$

This means that the equations for the polarizability and self-energy
reduce to

$\chi(1,2)=G(1,2)G(2,1)$

$\Sigma(1,2)=G(1,2)W(2,1)$

while the equations for the Green's function and the screened potential
remain the same.

However, in practice, these equations are usually solved in reciprocal
space in the frequency domain

$W_{{\bf G}{\bf G}'}({\bf
q},\omega)=\left\[\delta_{{\bf G}{\bf G}'}-\chi_{{\bf G}{\bf G}'}({\bf
q},\omega)V_{{\bf G}{\bf G}'}({\bf q})\right\]^{-1}V_{{\bf G}{\bf
G}'}({\bf q})$

$G_{{\bf G}{\bf G}'}({\bf
q},\omega)=\left\[\delta_{{\bf G}{\bf G}'}-\Sigma_{{\bf G}{\bf
G}'}({\bf q},\omega)G^{(0)}_{{\bf G}{\bf G}'}({\bf
q})\right\]^{-1}G^{(0)}_{{\bf G}{\bf G}'}({\bf q})$

In principle Hedin's equations have to be solved self-consistently,
where in the first iteration $G^{(0)}$
is the non-interacting Green's function

$G^{(0)}({\bf r},{\bf r}',\omega)=\sum_{n{\bf
k}}\frac{\phi_{n{\bf k}}^{\*(0)} ({\bf r})\phi^{(0)}_{n{\bf k}} ({\bf
r}')}{\omega-E^{(0)}_{n{\bf k}}}$

with $\phi^{(0)}_{n{\bf k}}$ being a
set of one-electron orbitals and $E_{n{\bf
k}}^{(0)}$ the corresponding energies. Afterwards the
polarizability $\chi^{(0)}$ is
determined, followed by the screened potential $W^{(0)}$ and the self-energy $\Sigma^{(0)}$. This means that GW calculations require a first
guess for the one-electron eigensystem, which is usually taken from a
preceding DFT step.

In principle, one has to repeat all steps by the updating the Green's
function with the Dyson equation given above in each iteration cycle
until self-consistency is reached. In practice, this is hardly ever done
due to computational complexity on the one hand (in fact fully
self-consistent GW calculations are available as of VASP 6 only).

On the other hand, one observes that by keeping the screened potential
$W$ in the first iteration to the DFT
level one benefits from error
cancelling,^([\[3\]](#cite_note-shishkin:prl:07-3)) which is the reason
why often the screening is kept on the DFT level and one aims at
self-consistency in Green's function only.

Following possible approaches are applied in practice and selectable
within VASP with the [ALGO](../incar-tags/ALGO.md) tag.

## Single Shot: G₀W₀
Performing only one GW iteration step is commonly referred to the G₀W₀
method. Here the self-energy $\Sigma^{(0)}$ is determined and the corresponding eigenvalue equation is
solved.^([\[1\]](#cite_note-HybertsenLouie-1)) Formally, this is a five
step precedure

- Determine the independent particle polarizability
  $\chi^{(0)}_{\bf GG'}({\bf q},\omega)$
- Determine the screened Coulomb potential $W^{(0)}_{\bf GG'}({\bf q},\omega)$
- Determine the self-energy $\Sigma^{(0)}({\bf
  r,r'},\omega)$
- Solve the eigenvalue equation $(T+V_{ext}+V_h)\phi_{n{\bf k}}({\bf r})+\int d{\bf
  r}\Sigma^{(0)}\left({\bf r},{\bf r}',\omega=E^{(1)}_{n{\bf
  k}}\right)\phi_{n{\bf k}}({\bf r}') = E^{(1)}_{n{\bf k}}\phi_{n{\bf
  k}}({\bf r})$ for the quasi-particle energies
  $E_{n\bf k}^{(1)}$.

To save further computation time, the self-energy is linearized with a
series expansion around the Kohn-Sham eigenvalues $\epsilon_{n\bf k}$

$\Sigma^{(0)}({\bf
r,r'},\omega)\approx\Sigma^{(0)}({\bf r,r'},\epsilon_{n{\bf k}})+
\left.\frac{\partial\Sigma^{(0)}}{\partial \omega}({\bf
r,r'},\omega)\right|_{\omega=\epsilon_{n{\bf
k}}}(\omega-\epsilon_{n{\bf k}})$

and the renormalization factor $Z^{(0)}_{n{\bf
k}}=\left\[ 1-{\rm Re}\left( \left.\frac{\partial\Sigma^{(0)}}{\partial
\omega}({\bf r,r'},\omega)\right|_{\omega=\epsilon_{n{\bf
k}}}\right)\right\]^{-1}$ is introduced. This allows to obtain
the G₀W₀ quasi-particle energies from following
equation^([\[1\]](#cite_note-HybertsenLouie-1))

$E^{(1)}_{n\bf k}=\epsilon_{n\bf k}+ Z_{n\bf
k}^{(0)} {\rm Re}\left\[ \langle \phi_{n\bf k}|
-\frac{\Delta}2+V_{ext}+V_h+\Sigma^{(0)}(\omega=\epsilon_{n\bf k})
-\epsilon_{n\bf k} |\phi_{n\bf k}\rangle \right\]$

The G₀W₀ method avoids the direct computation of the Green's function
and neglects self-consistency in $G$
completely. In fact, only the Kohn-Sham energies are updated from
$\epsilon_{n\bf k}\to E^{(1)}_{n\bf k}$, while the orbitals remain unchanged. This is the reason why
the G₀W₀ method is internally selected as of VASP6 with
[ALGO](../incar-tags/ALGO.md) =EVGW0 ("eigenvalue GW") in combination with
[NELM](../incar-tags/NELM.md)=1 to indicate one single iteration, even
though the method is commonly known as the G₀W₀ approach. To keep
backwards-compatibility, however, [ALGO](../incar-tags/ALGO.md)=G0W0 is
still supported in VASP6.

Note that avoiding self-consistency might seem a drastic step at first
sight. However, the G₀W₀ method often yields satisfactory results with
band-gaps close to experimental measurements and is often employed for
realistic band gap
calculations.^([\[4\]](#cite_note-shishkin-PRB74-4)[\[5\]](#cite_note-shishkin-PRB75-5))

## Partially self-consistent: GW₀ or EVGW₀
The G₀W₀ quasi-particle energies can be used to update the poles of the
Green's function in the spectral representation $G^{(i)}({\bf r},{\bf r}',\omega)=\sum_{n{\bf k}}\frac{\phi_{n{\bf
k}}^{\*(0)} ({\bf r})\phi^{(0)}_{n{\bf k}} ({\bf
r}')}{\omega-E^{(i)}_{n{\bf k}}}$ which in turn can be used
to update the self-energy via $\Sigma^{(0)} =
G^{(i)}W^{(0)}$. This allows to form a partial
self-consistency loop, where the screening is kept on the DFT level. The
method is commonly known as GW₀, even though only eigenvalues are
updated:

- Determine the independent particle polarizability
  $\chi^{(0)}_{\bf GG'}({\bf q},\omega)$
- Determine the screened Coulomb potential $W^{(0)}_{\bf GG'}({\bf q},\omega)$ and keep it fixed in the
  following
- Determine the self-energy $\Sigma^{(j)}({\bf
  r,r'},\omega)= G^{(j)}W^{(0)}$.
- Update quasi-particle energies $E^{(j+1)}_{n\bf
  k}=\epsilon_{n\bf k}+ Z_{n\bf k}^{(j)} {\rm Re}\left\[ \langle
  \phi_{n\bf k}|
  -\frac{\Delta}2+V_{ext}+V_h+\Sigma^{(j)}(\omega=E^{(j)}_{n\bf k})
  -\epsilon_{n\bf k} |\phi_{n\bf k}\rangle \right\]$. In
  the first iteration use $E_{n\bf
  k}^{(0)}=\epsilon_{n\bf k}$

The last two steps are repeated until self-consistency is reached. The
GW₀ method is computationally slightly more expensive than the
single-shot approach, but yields often excellent agreement with
experimentally measured band gaps while being computationally affordable
at the same
time.^([\[4\]](#cite_note-shishkin-PRB74-4)[\[5\]](#cite_note-shishkin-PRB75-5))

Note that the GW₀ and its single-shot approach do not allow for updates
in the Kohn-Sham orbitals $\phi_{n\bf k}$, merely the eigenvalues are updated. Furthermore, the name
GW₀ indicates an update in the Green's function as a solution of the
Dyson equation, while the used spectral representation of the Green's
function above is strictly speaking correct only in the single-shot
approach. Since VASP6 allows to update the Green's function from the
solution of the corresponding Dyson equation, the commonly known GW₀
method is also selectable with [ALGO](../incar-tags/ALGO.md)=EVGW0
("eigenvalue GW") and the number of iteration is set with
[NELM](../incar-tags/NELM.md).

## Self-consistent Quasi-particle approximation: scQPGW₀
In addition to eigenvalues one can use the self-consistent
Quasi-particle GW0 approach (scQPGW0) to update the orbitals
$\phi_{n\bf k}\to \psi^{(j)}_{n\bf k}$
as well. This approach was presented first by Faleev et.
al,^([\[6\]](#cite_note-Faleev-6)) and used a hermitized self-energy
$\Sigma^{\rm herm}=\frac{\Sigma+\Sigma^\dagger}2$ in the eigenvalue equation to determine both, quasi-particle
energies $E_{n\bf k}$ and corresponding
orbitals $\psi_{n\bf k}$.

In contrast to the Faleev approach one may consider a generalized
eigenvalue problem instead that is obtained consistently from the
linearization of the self-energy $\Sigma(E^{(j+1)})\approx \Sigma(E^{(j)}) +
\xi(E^{(j)})(E^{(j+1)}-E^{(j)})$ (where $\xi(E^{(j)})=\partial\Sigma(E^{(j)})/ \partial E^{(j)}$) and
reads^([\[3\]](#cite_note-shishkin:prl:07-3))

$\underbrace{\left\[ T + V_{ext}+V_h +
\Sigma\left(E_{n\bf k}^{(j)}\right) - \xi\left(E^{(j)}_{n\bf k}\right)
E^{(j)}_{n\bf k}\right\]}_{{\bf H}(E^{(j)}_{n\bf k})}
\left|\psi_{n\bf k}^{(j+1)} \right\rangle = E^{(j+1)}_{n\bf
k}\underbrace{\left\[1-\xi(E^{(j)}_{n\bf k}) \right\]}_{{\bf
S}(E^{(j)}_{n\bf k})} \left|\psi_{n\bf k}^{(j+1)} \right\rangle$

The resulting Hamiltonian ${\bf H}$ and
overlap matrix ${\bf H}$ are
non-hermitian in general, implying that the resulting orbitals
$\left|\psi_{n\bf k}^{(j+1)} \right\rangle$ are not normalized to 1. Therefore, VASP determines the
hermitian parts $H= \frac{ {\bf H} + {\bf
H}^\dagger }{2}, S = \frac{ {\bf S} + {\bf S}^\dagger }{2}$
and diagonalizes following matrix instead

$S^{-1/2} H S^{-1/2} = U \Lambda U^\dagger$

The resulting diagonal matrix $\Lambda$
contains the new quasi-particles, while the unitary matrix
$U$ determine the new orbitals
$\psi_{n\bf k}^{(j+1)} = \sum_{m}U_{nm}
\psi_{m\bf k}^{(j+1)}$. The method can be selected in VASP
with [ALGO](../incar-tags/ALGO.md)=QPGW0. See
[here](../redirects/GW_calculations.md) for more
information.

## Low-scaling GW: The Space-time Formalism
Available as of VASP.6 are low-scaling algorithms for
[ACFDT/RPA](RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md).^([\[7\]](#cite_note-kaltak:prb:2014-7))
This page describes the formalism of the corresponding low-scaling GW
approach.^([\[8\]](#cite_note-liu:prb:2016-8)) A theoretical description
of the ACFDT/RPA total energies is found
[here](ACFDT__RPA_calculations.md).
A brief summary regarding GW theory is given below, while a practical
guide can be found
[here](../redirects/GW_calculations.md).

## Theory
The GW implementations in VASP described in the papers of Shishkin *et
al.*^([\[9\]](#cite_note-shishkin:prb:2006-9)[\[10\]](#cite_note-shishkin:prb:2007-10))
avoid storage of the Green's function $G$ as well as Fourier transformations between time and frequency
domain entirely. That is, all calculations are performed solely on the
real frequency axis using Kramers-Kronig transformations for
convolutions in the equation of $\chi$
and $\Sigma$ in reciprocal space and
results in a relatively high computational cost that scales with
$N^4$ (number of electrons).

The scaling with system size can, however, be reduced to
$N^3$ by performing a so-called
Wick-rotation to imaginary time $t\to i\tau$.^([\[11\]](#cite_note-rojas:prl:1995-11)) This rotation
changes the signature of the Minkowski space-time $\eta=(-+++)$ to the euclidean one $\eta=(++++)$, where correlation functions, like the Green's
function do not oscillate in time.

Following the [low scaling ACFDT/RPA
algorithms](../redirects/Groundstate_in_the_Random_Phase_Approximation.md)
the euclidean space-time implementation determines first, the
non-interacting Green's function on the imaginary time axis in real
space

$G({\bf r},{\bf r}',i\tau)=-\sum_{n{\bf
k}}\phi_{n{\bf k}}^{(0)}({\bf r}) \phi_{n{\bf k}}^{\*(0)}({\bf r}')
e^{-(\epsilon_{n{\bf k}}-\mu)\tau}\left\[\Theta(\tau)(1-f_{n{\bf
k}})-\Theta(-\tau)f_{n{\bf k}}\right\]$

Here $\Theta$ is the step function and
$f_{n{\bf k}}$ the occupation number of
the state $\phi_{n{\bf k}}^{(0)}$.
Because the Green's function is non-oscillatory on the imaginary time
axis it can be represented on a coarse grid $\tau_{m}$, where the number of time points can be selected in
VASP via the [NOMEGA](../incar-tags/NOMEGA.md) tag. Usually 12 to 16
points are sufficient for insulators and small band gap
systems.^([\[12\]](#cite_note-kaltak:2014-12))

Subsequently, the irreducible polarizability is calculated from a
contraction of two imaginary time Green's functions

$\chi({\bf r},{\bf r}',i\tau_m) = -G({\bf r},{\bf
r}',i\tau_m)G({\bf r}',{\bf r},-i\tau_m)$

Afterwards, the same compressed Fourier transformation as for the [low
scaling ACFDT/RPA
algorithms](../redirects/Groundstate_in_the_Random_Phase_Approximation.md)
is employed to obtain the irreducible polarizability in reciprocal space
on the imaginary frequency axis $\chi({\bf r},{\bf
r}',i\tau_m) \to \chi_{{\bf G}{\bf G}'}({\bf q},i \omega_n)$.^([\[12\]](#cite_note-kaltak:2014-12)[\[8\]](#cite_note-liu:prb:2016-8))

The next step is the computation of the screened potential

$W_{{\bf G}{\bf G}'}({\bf
q},i\omega_m)=\left\[\delta_{{\bf G}{\bf G}'}-\chi_{{\bf G}{\bf
G}'}({\bf q},i\omega_m)V_{{\bf G}{\bf G}'}({\bf
q})\right\]^{-1}V_{{\bf G}{\bf G}'}({\bf q})$

  
followed by the inverse Fourier transform $W_{{\bf G}{\bf G}'}({\bf q},i \omega_n) \to \chi({\bf r},{\bf
r}',i\tau_m)$ and the calculation of the self-energy

$\Sigma({\bf r},{\bf r}',i\tau_m) = -G({\bf
r},{\bf r}',i\tau_m)W({\bf r}',{\bf r},i\tau_m)$

From here, several routes are possible including all approximations
mentioned above, that is the single-shot, EVG₀ and QPEVG₀ approximation.
All approximations have one point in common.

In contrast to the real-frequency implementation, the low-scaling GW
algorithms require an analytical continuation of the self-energy from
the imaginary frequency axis to the real axis. In general, this is an
ill-defined problem and usually prone to errors, since the self-energy
is known on a finite set of points. VASP determines internally a Padé
approximation of the self-energy $\Sigma(z)$ from the calculated set of [NOMEGA](../incar-tags/NOMEGA.md)
points $\Sigma(i\omega_n)$ and solves
the non-linear eigenvalue problem

$\left\[ T+V_{ext}+V_h+\Sigma(z)
\right\]\left|\phi_{n\bf k}\right\rangle = z\left| \phi_{n\bf k}
\right\rangle$

on the real frequency axis $z=\omega$.

Because preceding Fourier transformations have been carried out with
exponentially suppressed errors, the analytical continuation
$\Sigma(z)$ of the self-energy can be
determined with high accuracy. The analytical continuation typically
yields energies that differ less than 20 meV from quasi-particle
energies obtained from the real-frequency
calculation.^([\[8\]](#cite_note-liu:prb:2016-8))

In addition, the space-time formulation allows to solve the full Dyson
equation for $G({\bf r,r'},i\tau)$ with
decent computational cost.^([\[13\]](#cite_note-grumet:prb:2018-13))
This approach is known as the self-consistent GW approach (scGW) and is
available as of VASP6.

## Limitations of GW
From a physical point of view, the scGW method yields mostly
unsatisfactory results compared to experiment. Notably, the band gaps
are significantly overestimated compared to experiment, and plasmonic
satellites are entirely missing in the spectral
function.^([\[14\]](#cite_note-grumet-14))

The fact that "sloppier" GW flavours, such as EVGW₀ or even the
single-shot approach yield more accurate results is due to fortuitous
error cancelling and can be understood in terms of the band-gap
$\Delta$ of a system. The DFT gap is
typically smaller than the GW band gap and yields, therefore, a larger
dielectric function $\epsilon(\omega)=1-\chi(\omega)V$ (the polarizability is
inverse proportional to the band gap of the system). Although the band
gap is corrected by GW, at the same time the screening of the Coulomb
interaction is weakened. Forcing self-consistency only increases the
effect and deteriorates the agreement with experimental band gaps. The
rather disappointing results of the self-consistent GW approximation
shows the general limitations of Hedin's equations in the absence of
vertex corrections. It can be shown that inclusion of vertex corrections
yields band gaps that are again in agreement with
experiment.^([\[3\]](#cite_note-shishkin:prl:07-3))

## References
1.  ↑ ^([a](#cite_ref-HybertsenLouie_1-0))
    ^([b](#cite_ref-HybertsenLouie_1-1))
    ^([c](#cite_ref-HybertsenLouie_1-2)) [M. S. Hybertsen, S. G. Louie
    Phys. Ref. B 34, 5390
    (1986)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.34.5390)
2.  [↑](#cite_ref-Hedin_2-0) [L. Hedin, Phys. Rev. 139, A796
    (1965)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.139.A796)
3.  ↑ ^([a](#cite_ref-shishkin:prl:07_3-0))
    ^([b](#cite_ref-shishkin:prl:07_3-1))
    ^([c](#cite_ref-shishkin:prl:07_3-2)) [M. Shishkin, M. Marsman,
    and G. Kresse, Phys. Rev. Lett. 99, 246403
    (2007).](http://link.aps.org/doi/10.1103/PhysRevLett.99.246403)
4.  ↑ ^([a](#cite_ref-shishkin-PRB74_4-0))
    ^([b](#cite_ref-shishkin-PRB74_4-1)) [M. Shishkin and G. Kresse,
    Phys. Rev. B 74, 035101
    (2006).](http://link.aps.org/doi/10.1103/PhysRevB.74.035101)
5.  ↑ ^([a](#cite_ref-shishkin-PRB75_5-0))
    ^([b](#cite_ref-shishkin-PRB75_5-1)) [M. Shishkin and G. Kresse,
    Phys. Rev. B 75, 235102
    (2007).](http://link.aps.org/doi/10.1103/PhysRevB.75.235102)
6.  [↑](#cite_ref-Faleev_6-0) [S. V. Faleev, M. Schilfgaarde and T.
    Kotani, Phys. Rev. Lett. 93, 126406
    (2004).](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.93.126406)
7.  [↑](#cite_ref-kaltak:prb:2014_7-0) [M. Kaltak, J. Klimeš, and G.
    Kresse, Phys. Rev. B **90**, 054115
    (2014).](https://doi.org/10.1103/PhysRevB.90.054115)
8.  ↑ ^([a](#cite_ref-liu:prb:2016_8-0))
    ^([b](#cite_ref-liu:prb:2016_8-1))
    ^([c](#cite_ref-liu:prb:2016_8-2)) [P. Liu, M. Kaltak, J. Klimes,
    and G. Kresse, Phys. Rev. B **94**, 165109
    (2016).](https://doi.org/10.1103/PhysRevB.94.165109)
9.  [↑](#cite_ref-shishkin:prb:2006_9-0) [M. Shishkin and G. Kresse,
    Phys. Rev. B **74**, 035101
    (2006).](https://doi.org/10.1103/PhysRevB.74.035101)
10. [↑](#cite_ref-shishkin:prb:2007_10-0) [M. Shishkin and G. Kresse,
    Phys. Rev. B **75**, 235102
    (2007).](https://doi.org/10.1103/PhysRevB.75.235102)
11. [↑](#cite_ref-rojas:prl:1995_11-0) [H. N. Rojas, R. W. Godby,
    and R. J. Needs, Phys. Rev. Lett. **74**, 1827
    (1995).](https://doi.org/10.1103/PhysRevLett.74.1827)
12. ↑ ^([a](#cite_ref-kaltak:2014_12-0))
    ^([b](#cite_ref-kaltak:2014_12-1)) [M. Kaltak, J. Klimeš, and G.
    Kresse, J. Chem. Theory Comput. **10**, 2498-2507
    (2014).](https://doi.org/10.1021/ct5001268)
13. [↑](#cite_ref-grumet:prb:2018_13-0) [M. Grumet, P. Liu, M.
    Kaltak, J. Klimeš, and G. Kresse, Phys. Rev. B **98**, 155143
    (2018).](https://doi.org/10.1103/PhysRevB.98.155143)
14. [↑](#cite_ref-grumet_14-0) [M. Grumet, P. Liu, M. Kaltak, J. Klimeš
    and Georg Kresse, Phys. Ref. B 98, 155143
    (2018).](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.98.155143)

------------------------------------------------------------------------

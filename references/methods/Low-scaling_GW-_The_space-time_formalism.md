<!-- Source: https://vasp.at/wiki/index.php/Low-scaling_GW:_The_space-time_formalism | revid: 34901 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Low-scaling GW: The space-time formalism
Available as of VASP.6 are low-scaling algorithms for
[ACFDT/RPA](RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md).^([\[1\]](#cite_note-kaltak:prb:2014-1))
This page describes the formalism of the corresponding low-scaling GW
approach.^([\[2\]](#cite_note-liu:prb:2016-2)) A theoretical description
of the ACFDT/RPA total energies is found
[here](ACFDT__RPA_calculations.md).
A brief summary regarding GW theory is given below, while a practical
guide can be found
[here](../redirects/GW_calculations.md).

## Theory
The GW implementations in VASP described in the papers of Shishkin *et
al.*^([\[3\]](#cite_note-shishkin:prb:2006-3)[\[4\]](#cite_note-shishkin:prb:2007-4))
avoid storage of the Green's function $G$ as well as Fourier transformations between time and frequency
domain entirely. That is, all calculations are performed solely on the
real frequency axis using Kramers-Kronig transformations for
convolutions in the equation of $\chi$
and $\Sigma$ in reciprocal space and
results in a relatively high computational cost that scales with
$N^4$ (number of electrons).

The scaling with system size can, however, be reduced to
$N^3$ by performing a so-called
Wick-rotation to imaginary time $t\to i\tau$.^([\[5\]](#cite_note-rojas:prl:1995-5)) This rotation changes
the signature of the Minkowski space-time $\eta=(-+++)$ to the euclidean one $\eta=(++++)$, where correlation functions, like the Green's
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
systems.^([\[6\]](#cite_note-kaltak:2014-6))

Subsequently, the irreducible polarizability is calculated from a
contraction of two imaginary time Green's functions

$\chi({\bf r},{\bf r}',i\tau_m) = -G({\bf r},{\bf
r}',i\tau_m)G({\bf r}',{\bf r},-i\tau_m)$

Afterwards, the same compressed Fourier transformation as for the [low
scaling ACFDT/RPA
algorithms](../redirects/Groundstate_in_the_Random_Phase_Approximation.md)
is employed to obtain the irreducible polarizability in reciprocal space
on the imaginary frequency axis $\chi({\bf r},{\bf
r}',i\tau_m) \to \chi_{{\bf G}{\bf G}'}({\bf q},i \omega_n)$.^([\[6\]](#cite_note-kaltak:2014-6)[\[2\]](#cite_note-liu:prb:2016-2))

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
calculation.^([\[2\]](#cite_note-liu:prb:2016-2))

In addition, the space-time formulation allows to solve the full Dyson
equation for $G({\bf r,r'},i\tau)$ with
decent computational cost.^([\[7\]](#cite_note-grumet:prb:2018-7)) This
approach is known as the self-consistent GW approach (scGW) and is
available as of VASP6.

### Finite temperature formalism
The zero-temperature formalism of many-body perturbation theory breaks
down for metals (systems with zero energy band-gap) as pointed out by
Kohn and Luttinger.^([\[8\]](#cite_note-KohnLuttinger:PR:1960-8)) This
conundrum is lifted by considering diagrammatic perturbation theory at
finite temperature $T>0$, which may be
understood by an analytical continuation of the real-time
$t$ to the imaginary time axis
$-i\tau$. Matsubara has shown that this
Wick rotation in time $t\to-i\tau$
reveals an intriguing connection to the inverse temperature
$\beta=1/T$ of the
system.^([\[9\]](#cite_note-Matsubara:PTP:1955-9)) More precisely,
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
Minimax-Isometry method.^([\[10\]](#cite_note-Kaltak:PRB:2020-10)) This
approach converges exponentially with the number of considered frequency
points.

## References
1.  [↑](#cite_ref-kaltak:prb:2014_1-0) [M. Kaltak, J. Klimeš, and G.
    Kresse, Phys. Rev. B **90**, 054115
    (2014).](https://doi.org/10.1103/PhysRevB.90.054115)
2.  ↑ ^([a](#cite_ref-liu:prb:2016_2-0))
    ^([b](#cite_ref-liu:prb:2016_2-1))
    ^([c](#cite_ref-liu:prb:2016_2-2)) [P. Liu, M. Kaltak, J. Klimes,
    and G. Kresse, Phys. Rev. B **94**, 165109
    (2016).](https://doi.org/10.1103/PhysRevB.94.165109)
3.  [↑](#cite_ref-shishkin:prb:2006_3-0) [M. Shishkin and G. Kresse,
    Phys. Rev. B **74**, 035101
    (2006).](https://doi.org/10.1103/PhysRevB.74.035101)
4.  [↑](#cite_ref-shishkin:prb:2007_4-0) [M. Shishkin and G. Kresse,
    Phys. Rev. B **75**, 235102
    (2007).](https://doi.org/10.1103/PhysRevB.75.235102)
5.  [↑](#cite_ref-rojas:prl:1995_5-0) [H. N. Rojas, R. W. Godby,
    and R. J. Needs, Phys. Rev. Lett. **74**, 1827
    (1995).](https://doi.org/10.1103/PhysRevLett.74.1827)
6.  ↑ ^([a](#cite_ref-kaltak:2014_6-0))
    ^([b](#cite_ref-kaltak:2014_6-1)) [M. Kaltak, J. Klimeš, and G.
    Kresse, J. Chem. Theory Comput. **10**, 2498-2507
    (2014).](https://doi.org/10.1021/ct5001268)
7.  [↑](#cite_ref-grumet:prb:2018_7-0) [M. Grumet, P. Liu, M. Kaltak, J.
    Klimeš, and G. Kresse, Phys. Rev. B **98**, 155143
    (2018).](https://doi.org/10.1103/PhysRevB.98.155143)
8.  [↑](#cite_ref-KohnLuttinger:PR:1960_8-0) [W. Kohn and J. M.
    Luttinger, Phys. Rev. **118**, 41
    (1960).](https://doi.org/10.1103/PhysRev.118.41)
9.  [↑](#cite_ref-Matsubara:PTP:1955_9-0) [T. Matsubara, Prog. Theor.
    Phys. **14**, 351 (1955).](https://doi.org/10.1143/PTP.14.351)
10. [↑](#cite_ref-Kaltak:PRB:2020_10-0) [M. Kaltak and G. Kresse, Phys.
    Rev. B. **101**, 205145
    (2020).](https://doi.org/10.1103/PhysRevB.101.205145)

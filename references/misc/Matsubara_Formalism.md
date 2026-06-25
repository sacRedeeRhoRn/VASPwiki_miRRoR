<!-- Source: https://vasp.at/wiki/index.php/Matsubara_Formalism | revid: 20706 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Matsubara Formalism


The zero-temperature formalism of many-body perturbation theory breaks
down for metals (systems with zero energy band-gap) as pointed out by
Kohn and
Luttinger.[^KohnLuttinger:PR:1960-1]
This conundrum is lifted by considering diagrammatic perturbation theory
at finite temperature $T>0$, which
may be understood by an analytical continuation of the real-time
$t$ to the imaginary time axis $-i\tau$.
Matsubara has shown that this Wick rotation in time
$t\to-i\tau$ reveals an intriguing connection to the
inverse temperature $\beta=1/T$ of
the
system.[^Matsubara:PTP:1955-2]
More precisely, Matsubara has shown that all terms in perturbation
theory at finite temperature can be expressed as integrals of imaginary
time quantities (such as the polarizability $\chi(-i\tau)$) over the fundamental interval
$-\beta\le\tau\le\beta$.

As a consequence, one decomposes imaginary time quantities into a
Fourier series with period $\beta$ that
determines the spacing of the Fourier modes. For instance the imaginary
polarizability can be written as

$\chi(-i\tau)=\frac1\beta\sum_{m=-\infty}^\infty \tilde
\chi(i\nu_m)e^{-i\nu_m\tau},\quad \nu_m=\frac{2m}\beta\pi$

and the corresponding random-phase approximation of the correlation
energy at finite temperature becomes a series over (in this case,
bosonic) Matsubara frequencies

$\Omega_c^{\rm RPA}=\frac12\frac1\beta \sum_{m=-\infty}^\infty {\rm
Tr}\left\lbrace \ln\left\[ 1 -\tilde \chi(i\nu_m) V \right\] -\tilde
\chi(i\nu_m) V \right\rbrace,\quad \nu_m=\frac{2m}\beta\pi$

The Matsubara formalism has the advantage that all contributions to the
Green's function and the polarizability are mathematically well-defined,
including contributions from states close to the chemical potential
$\epsilon_{n{\bf k}}\approx \mu$, such that Matsubara
series also converge for metallic systems.

Although formally convenient, the Matsubara series converges poorly with
the number of considered terms in practice. VASP, therefore, uses a
compressed representation of the Fourier modes by employing the
Minimax-Isometry
method.[^Kaltak:PRB:2020-3]
This approach converges exponentially with the number of considered
frequency points.

[^KohnLuttinger:PR:1960-1]: [W. Kohn and J. M. Luttinger, Phys. Rev. **118**, 41 (1960).](https://doi.org/10.1103/PhysRev.118.41)
[^Matsubara:PTP:1955-2]: [T. Matsubara, Prog. Theor. Phys. **14**, 351 (1955).](https://doi.org/10.1143/PTP.14.351)
[^Kaltak:PRB:2020-3]: [M. Kaltak and G. Kresse, Phys. Rev. B. **101**, 205145 (2020).](https://doi.org/10.1103/PhysRevB.101.205145)

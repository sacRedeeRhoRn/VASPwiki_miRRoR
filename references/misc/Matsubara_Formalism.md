<!-- Source: https://vasp.at/wiki/index.php/Matsubara_Formalism | revid: 20706 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Matsubara Formalism


The zero-temperature formalism of many-body perturbation theory breaks
down for metals (systems with zero energy band-gap) as pointed out by
Kohn and
Luttinger.<sup>[\[1\]](#cite_note-KohnLuttinger:PR:1960-1)</sup>
This conundrum is lifted by considering diagrammatic perturbation theory
at finite temperature $T>0$, which
may be understood by an analytical continuation of the real-time
$t$ to the imaginary time axis $-i\tau$.
Matsubara has shown that this Wick rotation in time
$t\to-i\tau$ reveals an intriguing connection to the
inverse temperature $\beta=1/T$ of
the
system.<sup>[\[2\]](#cite_note-Matsubara:PTP:1955-2)</sup>
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
method.<sup>[\[3\]](#cite_note-Kaltak:PRB:2020-3)</sup>
This approach converges exponentially with the number of considered
frequency points.


1.  [↑](#cite_ref-KohnLuttinger:PR:1960_1-0)
    <a href="https://doi.org/10.1103/PhysRev.118.41" class="external text"
    rel="nofollow">W. Kohn and J. M. Luttinger, Phys. Rev.
    <strong>118</strong>, 41 (1960).</a>
2.  [↑](#cite_ref-Matsubara:PTP:1955_2-0)
    <a href="https://doi.org/10.1143/PTP.14.351" class="external text"
    rel="nofollow">T. Matsubara, Prog. Theor. Phys. <strong>14</strong>, 351
    (1955).</a>
3.  [↑](#cite_ref-Kaltak:PRB:2020_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.101.205145"
    class="external text" rel="nofollow">M. Kaltak and G. Kresse, Phys. Rev.
    B. <strong>101</strong>, 205145 (2020).</a>



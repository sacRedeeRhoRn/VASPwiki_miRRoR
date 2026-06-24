<!-- Source: https://vasp.at/wiki/index.php/Bethe-Salpeter_equation | revid: 28479 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bethe-Salpeter equation
The Bethe-Salpeter equation (BSE) was first derived and applied in the
context of particle physics and QED in 1951
^([\[1\]](#cite_note-salpeter:pr:1951-1)). The first application of BSE
in solids was done by Hanke and Sham
^([\[2\]](#cite_note-hanke:prl:1979-2)), who calculated the absorption
spectrum of bulk silicon in qualitative agreement with experiment. Since
then numerous works have shown successful applications of BSE for
describing optical properties of materials and BSE has become the state
of the art for *ab initio* simulation of absorption spectra.

## Contents

- [1 Theory](#Theory)
- [2 Implementation](#Implementation)
  - [2.1 Tamm-Dancoff approximation](#Tamm-Dancoff_approximation)
- [3 References](#References)

## Theory
The Bethe-Salpeter equation is a Dyson like equation for the four-point
polarization function $L(1,3,2,4)$,
which can be found by summing up an infinite series of non-interacting
polarization functions $L_0(1,3,2,4)$
connected via the interaction kernel $\Xi'(6,5,7,8)$

$L(1,3,2,4)=L_0(1,3,2,4)+\int
\mathrm{d}5\mathrm{d}6\mathrm{d}7\mathrm{d}8
L_0(1,3,6,5)\Xi'(6,5,7,8)L(7,8,2,4).$

Here, the common notation is used $1\to{\mathbf{r}_1,t_1}$. The interaction kernel contains the
full self-energy $\Sigma$ including the
Hartree term and reads

$\Xi'(2,1,3,4)=\frac{\delta\[\Sigma_{\rm
H}(12)+\Sigma^{\rm xc}(12)\]}{\delta
G(34)}=\delta(1,2)\delta(3^+,4)V(1,3)+\Xi(2,1,3,4)$.

In practical calculations the $\Sigma^{\rm xc}$ is approximated via the GW self-energy

$\Xi(2,1,3,4)=-\frac{\delta\[G(12)W(1^+2)\]}{\delta
G(34)}=-\delta(1,3)\delta(2,4)W(1^+2)-G(12)\frac{\delta W(1^+2)}{\delta
G(34)}.$

The variation of the screened potential w.r.t. the Green's function is
of order $W^2$ and is usually neglected.
Thus, the Bethe-Salpeter equation takes a simplified from

$L(1,3,2,4)=L_0(1,3,2,4)+\int
\mathrm{d}5\mathrm{d}6\mathrm{d}7\mathrm{d}8L_0(1,3,6,5)\[\delta(5,6)\delta(7,8)V(5,8)-\delta(5,7)\delta(6,8)W(5^+6)\]L(7,8,2,4)$

This equation can be represented by an infinite sum of Feynman diagrams

[![](https://vasp.at/wiki/images/thumb/2/23/Bse_graph.png/700px-Bse_graph.png)](https://vasp.at/wiki/File:Bse_graph.png)

Diagrammatic representation of the Bethe-Salpeter equation for the
polarizability function $L$.

The interaction in BSE is described by two terms, the bare Coulomb
interaction $v$ and the attractive
screened potential $W$. Since the
$W$ term originated from the GW
self-energy, the same level of approximation is used, i.e., the random
phase approximation (RPA). However, the important difference is that in
BSE the static approximation is usually used, i.e.,
$W(\omega=0)$. The dynamical effects in
the screened potential are shown to cancel out to a large extent with
the dynamical effects in the polarizability $L_0$.

Finally, the macroscopic dielectric function can be found by making the
connection to the two-point polarizability $\chi(1,2)=L(1,1^+,2,2^+)$

$\varepsilon^{-1}(1,2)=\delta(1,2)+\int
\mathrm{d}3 V(1,3)\chi(3,2)$

## Implementation
The poles of the response function $L$
correspond to the excitation energies including the excitonic effects.
For practical reasons, it is more efficient to reformulate the
Bethe-Salpeter equation in the the transition space and solve it as a
non-hermitian eigenvalue problem, where the excitation energies
correspond to the eigenvalues $\omega_\lambda$^([\[3\]](#cite_note-sander:prb:15-3))

$\left(\begin{array}{cc} \mathbf{A} & \mathbf{B}
\\ \mathbf{B}^\* & \mathbf{A}^\*
\end{array}\right)\left(\begin{array}{l} \mathbf{X}_\lambda \\
\mathbf{Y}_\lambda
\end{array}\right)=\omega_\lambda\left(\begin{array}{cc} \mathbf{1} &
\mathbf{0} \\ \mathbf{0} & -\mathbf{1}
\end{array}\right)\left(\begin{array}{l} \mathbf{X}_\lambda \\
\mathbf{Y}_\lambda \end{array}\right)~.$

  
The matrices $A$ and
$A^\*$ describe the resonant and
anti-resonant transitions between the occupied $v,v'$ and unoccupied $c,c'$
states

$A_{vc}^{v'c'} =
(\varepsilon_v-\varepsilon_c)\delta_{vv'}\delta_{cc'} + \langle
cv'|V|vc'\rangle - \langle cv'|W|c'v\rangle.$

The energies and orbitals of these states are usually obtained in a
$G_0W_0$ calculation, but DFT and Hybrid
functional calculations can be used as well. The electron-electron
interaction and electron-hole interaction are described via the bare
Coulomb $V$ and the screened potential
$W$.

The coupling between resonant and anti-resonant terms is described via
terms $B$ and $B^\*$

$B_{vc}^{v'c'} = \langle vv'|V|cc'\rangle -
\langle vv'|W|c'c\rangle.$

Due to the presence of this coupling, the Bethe-Salpeter Hamiltonian is
non-Hermitian.

### Tamm-Dancoff approximation
A common approximation to the BSE is the Tamm-Dancoff approximation
(TDA), which neglects the coupling between resonant and anti-resonant
terms, i.e., $B$ and
$B^\*$. Hence, the TDA reduces the BSE
to a Hermitian problem

$AX_\lambda=\omega_\lambda X_\lambda~.$

In reciprocal space, the matrix $A$ is
written as

$A_{vc\mathbf{k}}^{v'c'\mathbf{k}'} =
(\varepsilon_v-\varepsilon_c)\delta_{vv'}\delta_{cc'}\delta_{\mathbf{kk}'}+
\frac{2}{\Omega}\sum_{\mathbf{G}\neq0}\bar{V}_\mathbf{G}(\mathbf{q})\langle
c\mathbf{k}|e^{i\mathbf{Gr}}|v\mathbf{k}\rangle\langle
v'\mathbf{k}'|e^{-i\mathbf{Gr}}|c'\mathbf{k}'\rangle
-\frac{2}{\Omega}\sum_{\mathbf{G,G}'}W_{\mathbf{G,G}'}(\mathbf{q},\omega)\delta_{\mathbf{q,k-k}'}
\langle c\mathbf{k}|e^{i(\mathbf{q+G})}|c'\mathbf{k}'\rangle \langle
v'\mathbf{k}'|e^{-i(\mathbf{q+G})}|v\mathbf{k}\rangle,$

where $\Omega$ is the cell volume,
$\bar{V}$ is the bare Coulomb potential
without the long-range part

$\bar{V}_{\mathbf{G}}(\mathbf{q})=\begin{cases} 0
& \text { if } G=0 \\ V_{\mathbf{G}}(\mathbf{q})=\frac{4
\pi}{|\mathbf{q}+\mathbf{G}|^2} & \text { else } \end{cases}~,$

and the screened Coulomb potential $W_{\mathbf{G}, \mathbf{G}^{\prime}}(\mathbf{q}, \omega)=\frac{4 \pi
\epsilon_{\mathbf{G}, \mathbf{G}^{\prime}}^{-1}(\mathbf{q},
\omega)}{|\mathbf{q}+\mathbf{G}|\left|\mathbf{q}+\mathbf{G}^{\prime}\right|}.$

Here, the dielectric function $\epsilon_\mathbf{G,G'}(\mathbf{q})$ describes the screening
in $W$ within the random-phase
approximation (RPA)

$\epsilon_{\mathbf{G},
\mathbf{G}^{\prime}}^{-1}(\mathbf{q}, \omega)=\delta_{\mathbf{G},
\mathbf{G}^{\prime}}+\frac{4 \pi}{|\mathbf{q}+\mathbf{G}|^2}
\chi_{\mathbf{G}, \mathbf{G}^{\prime}}^{\mathrm{RPA}}(\mathbf{q},
\omega).$

Although the dielectric function is frequency-dependent, the static
approximation $W_{\mathbf{G},
\mathbf{G}^{\prime}}(\mathbf{q}, \omega=0)$ is considered a
standard for practical BSE calculations.

## References
1.  [↑](#cite_ref-salpeter:pr:1951_1-0) [E. E. Salpeter and H. A. Bethe,
    *A Relativistic Equation for Bound-State Problems*, Phys. Rev.
    **84**, 1232-1242 (1951)](http://dx.doi.org/10.1103/PhysRev.84.1232)
2.  [↑](#cite_ref-hanke:prl:1979_2-0) [W. Hanke and L. J. Sham,
    *Many-Particle Effects in the Optical Excitations of a
    Semiconductor*, Phys. Rev. Lett. **43**, 387-390
    (1979)](http://dx.doi.org/10.1103/PhysRevLett.43.387)
3.  [↑](#cite_ref-sander:prb:15_3-0) [T. Sander, E. Maggio, and G.
    Kresse, *Beyond the Tamm-Dancoff approximation for extended systems
    using exact diagonalization*, Phys. Rev. B **92**, 045209
    (2015).](https://doi.org/10.1103/PhysRevB.92.045209)

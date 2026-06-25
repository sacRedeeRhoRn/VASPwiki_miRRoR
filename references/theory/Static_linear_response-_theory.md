<!-- Source: https://vasp.at/wiki/index.php/Static_linear_response:_theory | revid: 33073 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Static linear response: theory


Let’s consider three types of static perturbations

1.  atomic displacements $u_m$ with
    $m=I\alpha$ with $I=\\1..N_\text{atoms}\\$ and $\alpha=\\1..3\\$
2.  homogeneous strains $\eta_j$
    with $j=\\1..6\\$
3.  static electric field $\mathcal{E}_\alpha$ with $\alpha=\\1..3\\$

By performing a Taylor expansion of the total energy
$E$ in terms of these perturbations we
obtain[^wu:prb:2005-1]

$\begin{aligned} E(u,\mathcal{E},\eta) = &E_0 + \\ &\frac{\partial
E}{\partial u_m} u_m + \frac{\partial E}{\partial \mathcal{E}_\alpha}
\mathcal{E}_\alpha+ \frac{\partial E}{\partial \eta_j} \eta_j + \\
&\frac{1}{2} \frac{\partial^2 E} {\partial u_m \partial u_n } u_m u_n +
\frac{1}{2} \frac{\partial^2 E} {\partial \mathcal{E}_\alpha \partial
\mathcal{E}_\beta } \mathcal{E}_\alpha \mathcal{E}_\beta +
\frac{1}{2} \frac{\partial^2 E} {\partial \eta_j \partial \eta_k} \eta_j
\eta_k + \\ &\frac{\partial^2 E}{\partial u_m \partial
\mathcal{E}_\alpha} u_m \mathcal{E}_\alpha + \frac{\partial^2
E}{\partial u_m \partial \eta_j} u_m \eta_j + \frac{\partial^2
E}{\partial \mathcal{E}_\alpha \partial \eta_j} \mathcal{E}_\alpha
\eta_j + \text{terms of higher order} \end{aligned}$

  
The derivatives of the energy with respect to an electric field are the
polarization, with respect to atomic displacements are the forces, with
respect to changes in the lattice vectors are the stress tensor.

$P_\alpha = -\frac{\partial E}{\partial \mathcal{E}_\alpha} \qquad
\text{polarization}$

$F_m = -\Omega_0\frac{\partial E}{\partial u_m} \qquad \text{forces}$

$\sigma_j = \frac{\partial E}{\partial \eta_j} \qquad \text{stresses}$

This leads to the following ‘clamped-ion’ or ‘frozen-ion’ definitions:

$\overline{\chi}_{\alpha\beta} = - \frac{\partial^2 E}{\partial
\mathcal{E}_\alpha \partial \mathcal{E}_\beta} |_{u,\eta} \qquad
\text{dielectric susceptibility}$

$\overline{C}_{jk} = \frac{\partial^2 E}{\partial \eta_j \partial
\eta_k} |_{u,\mathcal{E}} \qquad \text{elastic tensor}$

$\Phi_{mn}=\Omega_0 \frac{\partial^2 E}{\partial u_m \partial u_n}
|_{\mathcal{E},\eta} \qquad \text{force-constants}$

$\overline{e}_{\alpha k} = \frac{\partial^2 E}{\partial
\mathcal{E}_\alpha \partial \eta_k} |_{u} \qquad \text{piezoelectric
tensor}$

$Z^\*_{m\alpha}=-\Omega_0 \frac{\partial^2 E}{\partial u_m \partial
\mathcal{E}_\alpha} |_{\eta} \qquad \text{Born effective charges}$

$\Xi_{mj}=-\Omega_0 \frac{\partial^2 E}{\partial u_m \partial \eta_j}
|_{\mathcal{E}} \qquad \text{force response internal strain tensor}$

  
To compare with experimental results, however, the static response
properties should take into account the ionic relaxation. This follows
from the Taylor expansion above by looking at the ionic positions where
the energy is minimal:

$\tilde{E}(\mathcal{E},\eta) = \text{min}_u E(u,\mathcal{E},\eta)$

The physical ‘relaxed-ion’ tensors are

$\begin{aligned} \chi_{\alpha\beta} &= \overline{\chi}_{\alpha\beta} +
\Omega_0^{-1} Z^\*_{m\alpha} (\Phi)^{-1}_{mn} Z^\*_{n\beta} \qquad
\text{dielectric susceptibility}\\ C_{jk} &= \overline{C}_{jk} +
\Omega_0^{-1} \Xi_{mj} (\Phi)^{-1}_{mn} \Xi_{nk} \qquad \text{elastic
tensor}\\ e_{\alpha j} &= \overline{e}_{\alpha j} +
\Omega_0^{-1}Z^\*_{m\alpha} (\Phi)^{-1}_{mn} \Xi_{nj} \qquad
\text{piezoelectric tensor} \end{aligned}$

The second term on the right-hand side of each of these equations is
called the ionic contributions to the dielectric susceptibility, elastic
tensor, and piezoelectric tensor.

The ionic contributions to the dielectric tensor are:
$\epsilon^{\text{ion}}_{ij}=\frac{4\pi}{\Omega} \sum_{kl} Z^\*_{ik}
\Phi^{-1}_{kl} Z^\*_{lj}$

The ionic contributions to the elastic tensor
$C^{\text{ion}}_{ik}= \sum_{kl} \Xi_{ij} \Phi^{-1}_{jk} \Xi_{kl}$

The ionic contributions to the piezoelectric tensor
$e^{\text{ion}}_{ij}= \sum_{kl} Z^\*_{ij} \Phi^{-1}_{jk} \Xi_{kl}$

## References\[<a
href="/wiki/index.php?title=Static_linear_response:_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^wu:prb:2005-1]: [X. Wu, D. Vanderbilt, and D. R. Hamann, Phys. Rev. B **72**, 035105 (2005).](https://doi.org/10.1103/PhysRevB.72.035105)

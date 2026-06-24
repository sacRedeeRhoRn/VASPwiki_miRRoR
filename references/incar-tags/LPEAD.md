<!-- Source: https://vasp.at/wiki/index.php/LPEAD | revid: 27977 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LPEAD
LPEAD = .TRUE. \| .FALSE  
Default: **LPEAD** = .FALSE. 

Description: for LPEAD=.TRUE., the derivative of the cell-periodic part
of the orbitals w.r.t. **k**, \|∇_(**k**)u_(n**k**)⟩, is calculated
using finite differences ("perturbation expansion after discretization"
(PEAD)^([\[1\]](#cite_note-nunes:prb:01-1)[\[2\]](#cite_note-souza:prl:02-2))).

------------------------------------------------------------------------

The derivative of the cell-periodic part of the orbitals w.r.t. **k**,
**k**, \|∇_(**k**)u_(n**k**)⟩, may be written as:

$|\mathbf{\nabla_{k}} \tilde{u}_{n\mathbf{k}}
\rangle = \sum_{n\neq n'} \frac{| \tilde{u}_{n'\mathbf{k}} \rangle
\langle \tilde{u}_{n'\mathbf{k}} |
\frac{\partial\left\[H(\mathbf{k})-\epsilon_{n\mathbf{k}}S(\mathbf{k})\right\]}{\partial
\mathbf{k}} | \tilde{u}_{n\mathbf{k}}
\rangle}{\epsilon_{n\mathbf{k}}-\epsilon_{n'\mathbf{k}}}$

where H(**k**) and S(**k**) are the Hamiltonian and overlap operator for
the cell-periodic part of the orbitals, and the sum over *n*´ must
include a sufficiently large number of unoccupied states.

It may also be found as the solution to the following linear Sternheimer
equation (see [LEPSILON](LEPSILON.md)):

$\left\[H(\mathbf{k})-\epsilon_{n\mathbf{k}}S(\mathbf{k})\right\]
|\mathbf{\nabla_{k}} \tilde{u}_{n\mathbf{k}} \rangle
=-\frac{\partial\left\[H(\mathbf{k})-\epsilon_{n\mathbf{k}}S(\mathbf{k})\right\]}
{\partial \mathbf{k}}|\tilde{u}_{n\mathbf{k}} \rangle$

Alternatively one may compute $\nabla_{\mathbf{k}} \tilde{u}_{n\mathbf{k}}$ from finite
differences (LPEAD=.TRUE.):

$\frac{\partial | \tilde{u}_{n\mathbf{k}_j}
\rangle}{\partial k}= \frac{ie}{2\Delta k} \sum^N_{m=1} \left\[ |
\tilde{u}_{m\mathbf{k}_{j+1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j+1})\rangle - |
\tilde{u}_{m\mathbf{k}_{j-1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j-1})\rangle\right\]$

where *m* runs over the *N* occupied bands of the system,
Δ*k*=**k**_(j+1)-**k**_(j), and

$S_{nm}(\mathbf{k}_j,\mathbf{k}_{j+1})= \langle
\tilde{u}_{n\mathbf{k}_{j}}| \tilde{u}_{m\mathbf{k}_{j+1}}\rangle$.

As mentioned in the context of [the self-consistent response to finite
electric
fields](../theory/Berry_phases_and_finite_electric_fields.md)
one may derive analoguous expressions for \|∇_(**k**)u_(n**k**)⟩ using
higher-order finite difference approximations.

When LPEAD=.TRUE., VASP will compute \|∇_(**k**)u_(n**k**)⟩ using the
aforementioned finite difference scheme. The order of the finite
difference approximation can be specified by means of the
[IPEAD](IPEAD.md)-tag (default:
[IPEAD](IPEAD.md)=4).

These tags may be used in combination with
[LOPTICS](LOPTICS.md)=.TRUE. and
[LEPSILON](LEPSILON.md)=.TRUE..

------------------------------------------------------------------------

- N.B. Please note that LPEAD = .TRUE. **is not supported for metallic
  systems**.

  

## Related tags and articles
[IPEAD](IPEAD.md), [LEPSILON](LEPSILON.md),
[LOPTICS](LOPTICS.md),
[LCALCEPS](LCALCEPS.md),
[EFIELD_PEAD](EFIELD_PEAD.md), [Berry phases and finite
electric
fields](../theory/Berry_phases_and_finite_electric_fields.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPEAD-_incategory-Examples)

## References
1.  [↑](#cite_ref-nunes:prb:01_1-0) [R. W. Nunes and X. Gonze, Phys.
    Rev. B 63, 155107
    (2001).](http://link.aps.org/doi/10.1103/PhysRevB.63.155107)
2.  [↑](#cite_ref-souza:prl:02_2-0) [I. Souza, J. Íñiguez, and D.
    Vanderbilt, Phys. Rev. Lett. 89, 117602
    (2002).](http://link.aps.org/doi/10.1103/PhysRevLett.89.117602)

------------------------------------------------------------------------

------------------------------------------------------------------------

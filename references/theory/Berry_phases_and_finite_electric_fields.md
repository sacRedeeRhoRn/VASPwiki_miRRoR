<!-- Source: https://vasp.at/wiki/index.php/Berry_phases_and_finite_electric_fields | revid: 30684 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Berry phases and finite electric fields
## Contents

- [1 Modern Theory of Polarization](#Modern_Theory_of_Polarization)
  - [1.1 Berry phase expression for the macroscopic
    polarization](#Berry_phase_expression_for_the_macroscopic_polarization)
  - [1.2 Computational aspects](#Computational_aspects)
- [2 Self-consistent response to finite electric
  fields](#Self-consistent_response_to_finite_electric_fields)
  - [2.1 Response properties](#Response_properties)
- [3 Related Tags and Sections](#Related_Tags_and_Sections)
- [4 References](#References)

## Modern Theory of Polarization
### Berry phase expression for the macroscopic polarization
Calculating the change in dipole moment per unit cell under PBC's, is a
nontrivial task. In general one *cannot* define it as the first moment
of the induced change in charge density δ(**r**), through

$\Delta \mathbf{P}= \frac{1}{\Omega_{0}}
\int_{\Omega_{0}} \mathbf{r} \delta \left( \mathbf{r} \right) d^{3}r$

without introducing a dependency on the shape of Ω₀, the chosen unit
cell.^([\[1\]](#cite_note-Vogl78-1))

Recently King-Smith and
Vanderbilt^([\[2\]](#cite_note-Vanderbilt93I-2)), building on the work
of Resta^([\[3\]](#cite_note-Resta92-3)), showed that the electronic
contribution to the difference in polarization Δ**P**_(e), due to a
finite adiabatic change in the Hamiltonian of a system, can be
identified as a *geometric quantum phase* or *Berry phase* of the
valence wave functions. We will briefly summarize the essential results
(for a review of geometric quantum phases in polarization theory see the
papers of
Resta^([\[4\]](#cite_note-Resta94-4)[\[5\]](#cite_note-Resta96-5))).

Central to the modern theory of polarization is the proposition of
Resta^([\[3\]](#cite_note-Resta92-3)) to write the electronic
contribution to the change in polarization due to a finite adiabatic
change in the Kohn-Sham Hamiltonian of the crystalline solid, as

$\Delta \mathbf{P}_{e}=
\int^{\lambda_{2}}_{\lambda_{1}}{\partial \mathbf{P}_{e} \over
\partial \lambda} d\lambda$

with

${\partial \mathbf{P}_{e} \over \partial
\lambda}= {i |e| \hbar \over N \Omega_{0} m_{e}} \sum_{\mathbf{k}}
\sum^{M}_{n=1} \sum^{\infty}_{m=M+1} {\langle
\psi^{\left(\lambda\right)}_{n\mathbf{k}} | \mathbf{\hat{p}} |
\psi^{\left(\lambda\right)}_{m\mathbf{k}}\rangle \langle
\psi^{\left(\lambda\right)}_{m\mathbf{k}} | \partial
V^{\left(\lambda\right)}/\partial \lambda |
\psi^{\left(\lambda\right)}_{n\mathbf{k}}\rangle \over \left(
\epsilon^{\left(\lambda\right)}_{n\mathbf{k}}-
\epsilon^{\left(\lambda\right)}_{m\mathbf{k}} \right)^{2}}+
\mathrm{c.c.}$

where *m_(e)* and *e* are the electronic mass and charge, *N* is the
number of unit cells in the crystal, Ω₀ is the unit cell volume, *M* is
the number of occupied bands, **p** is the momentum operator, and the
functions ψ^((λ))_(n**k**) are the usual Bloch solutions to the
crystalline Hamiltonian. Within Kohn-Sham density-functional theory, the
potential V^((λ)) is to be interpreted as the Kohn-Sham potential
V^((λ))_(KS), where λ parameterizes some change in this potential, for
instance due to the displacement of an atom in the unit cell.

King-Smith and Vanderbilt^([\[2\]](#cite_note-Vanderbilt93I-2)) have
cast this expression in a form in which the conduction band states
ψ^((λ))_(m**k**) no longer explicitly appear, and they show that [the
change in polarization](#PolarizationChange1) along an arbitrary path,
can be found from only a knowledge of the system at the end points

$\Delta \mathbf{P}_{e}=
\mathbf{P}^{\left(\lambda_{2} \right)}_{e} -
\mathbf{P}^{\left(\lambda_{1}\right)}_{e}$

with

$\mathbf{P}^{\left(\lambda\right)}_{e}=-{if|e|\over 8\pi^{3}}
\sum^{M}_{n=1}\int_{BZ} d^{3}k \langle
u^{\left(\lambda\right)}_{n\mathbf{k}} | \nabla_{\mathbf{k}} |
u^{\left(\lambda\right)}_{n\mathbf{k}} \rangle$

where *f* is the occupation number of the states in the valence bands,
u^((λ))_(n**k**) is the cell-periodic part of the Bloch function
ψ^((λ))_(n**k**), and the sum *n* runs over all *M* occupied bands.

The physics behind [the equation above](#Polarization) becomes more
transparent when this expression is written in terms of the Wannier
functions of the occupied bands,

$\mathbf{P}^{\left(\lambda\right)}_{e}=-{f |e|
\over \Omega_{0}} \sum^{M}_{n=1} \langle W^{\left(\lambda\right)}_{n}
| \mathbf{r} |W^{\left(\lambda\right)}_{n} \rangle$

where W_(n) is the Wannier function corresponding to valence band *n*.

This shows the change in polarization of a solid, induced by an
adiabatic change in the Hamiltonian, to be proportional to the
displacement of the charge centers **r**_(n)=⟨ W^((λ))_(n)\|**r**\|
W^((λ))_(n)⟩, of the Wannier functions corresponding to the valence
bands.

It is important to realize that the [polarization in terms of
Bloch](#Polarization) or [Wannier](#Wannier) functions, and consequently
the [change in polarization](#PolarizationChange2), is only well-defined
modulo *fe***R**/Ω₀, where **R** is a lattice vector. This indeterminacy
stems from the fact that the charge center of a Wannier function is only
invariant modulo **R**, with respect to the choice of phase of the Bloch
functions.

In practice one is usually interested in polarization changes
\|Δ**P**_(e)\| \<\< \|*fe***R**₁/Ω₀\|, where **R**₁ is the shortest
nonzero lattice vector. An arbitrary term *fe***R**/Ω₀ can therefore
often be removed by simple inspection of the results. In cases where
\|Δ**P**_(e)\| is of the same order of magnitude as *fe***R**₁/Ω₀ any
uncertainty can always be removed by dividing the total change in the
Hamiltonian λ₁→λ₂ into a number of intervals.

### Computational aspects
In general, the direct evaluation of [**P**_(e)^((λ))](#Polarization) is
useless, because there is no specific relationship between the phases of
the eigenvectors u^((λ))_(**k**n) generated by a numerical
diagonalization routine. This problem is circumvented by dividing the
Brillouin zone integration in two parts, a two-dimensional integral and
a line integral, and by transforming [the above](#Polarization) into
three equations, which separately provide the components of
**P**_(e)^((λ)) along the directions of three reciprocal lattice vectors
**G**₁, **G**₂, and **G**₃, which together span a unit cell of the
reciprocal lattice. The component of **P**_(e)^((λ)) along for instance
**G**₁ can be found from

$\mathbf{G}_{1} \cdot
\mathbf{P}_{e}^{\left(\lambda\right)}=-{if|e|\over 8\pi^{3}}
\int_{A} dk_{2}dk_{3} \sum^{M}_{n=1} \int^{|\mathbf{G}_{1}|}_{0}
dk_{1} \langle u^{\left(\lambda\right)}_{n\mathbf{k}}
|\partial/\partial k_{1} | u^{\left(\lambda\right)}_{n\mathbf{k}}
\rangle$

where the two-dimensional integral is taken over the area *A*, spanned
by **G**₂ and **G**₃, and the line integral runs over a line segment
parallel to **G**₁. Interchanging the indices *1*, *2* and *3* in [the
equation above](#Polarization2) yields the expressions for two other
components of **P**_(e)^((λ)).

Thus the electronic part of the polarization **P**_(e)^((λ)) is given
(modulo *fe***R**/Ω₀) by the sum

$\sum^{3}_{i=1}(\mathbf{P}_{e}^{\left(\lambda\right)})_{i}=\sum^{3}_{i=1}
\left(\mathbf{G}_{i} \cdot
\mathbf{P}_{e}^{\left(\lambda\right)}\right) {\mathbf{R}_{i} \over
2\pi}$

where the lattice vectors **R**_(i) obey the relationship
**R**_(i)·**G**_(j)=2πδ_(ij).

The integration over *A* in [the above](#Polarization2), is
straightforward and can be performed by sampling a 2D Monkhorst-Pack
mesh of *k*-points,^([\[6\]](#cite_note-MonkhorstPack-6)) termed the
*perpendicular mesh* or **k**_(⊥)-mesh by King-Smith and Vanderbilt.
However, to remove the influence of the random phase of the functions
u^((λ))_(n**k**), introduced by the diagonalization routine, King-Smith
and Vanderbilt^([\[2\]](#cite_note-Vanderbilt93I-2)) propose to replace
the line integral alias integration in the *parallel* or **G**_(\|\|)
direction by,

$\phi^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right)=\mathrm{Im}
\left\\\ln \prod^{J-1}_{j=0} \mathrm{det} \left( \langle
u^{\left(\lambda\right)}_{m\mathbf{k}_{j}} |
u^{\left(\lambda\right)}_{n\mathbf{k}_{j+1}}\rangle \right)\right\\$

which is evaluated by calculating the cell-periodic parts of the wave
functions at a string of *J* *k*-points, **k**_(j)=
**k**_(⊥)+j**G**_(\|\|)/*J* (with *j*=0,..,*J*-1), and where for
sufficiently large *J* one has that

$\phi^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right)=
-i\sum^{M}_{n=1} \int^{|\mathbf{G}_{\parallel}|}_{0}
dk_{\parallel} \langle u^{\left(\lambda\right)}_{n\mathbf{k}} |
\partial/\partial k_{\parallel} |
u^{\left(\lambda\right)}_{n\mathbf{k}} \rangle$

**Note**: the determinant appearing in [the equation above](#CyclicForm)
is the determinant of the *M*×*M* matrix formed by letting *n* and *m*
run over all valence bands.

The crucial step, instrumental in removing the random phase, is that the
functions u^((λ))_(n**k**_(J)) are not obtained from an independent
diagonalization, but found through their relationship with the functions
u^((λ))_(n**k**₀),

$u^{\left(\lambda\right)}_{n\mathbf{k}_{J}}(\mathbf{r})=
e^{-i\mathbf{G}_{\parallel}\cdot \mathbf{r}}
u^{\left(\lambda\right)}_{n\mathbf{k}_{0}}(\mathbf{r})$

This way the product [φ_(J)^((λ))](#CyclicForm) becomes cyclic, and
contains both u^((λ))_(n**k**_(j)) as well as its complex conjugate for
every *k*-point in the string, thus removing the random phase.

In practice [**G**_(\|\|)·**P**_(e)^((λ))](#Polarization2) is evaluated
by way of the following summation over the **k**_(⊥)-mesh,

$(\mathbf{P}_{e}^{\left(\lambda\right)})_{i} =
\frac{f|e|\mathbf{R}_{i}}{2\pi\Omega_{0}}
\left(\frac{1}{N_{k_{\perp}}}\sum_{\mathbf{k}_{\perp}}
\mathrm{Im}\ln
\frac{D^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right)}{\langle
D \rangle} +\mathrm{Im}\ln \langle D \rangle\right)$

where

$D^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right)=
\prod^{J-1}_{j=0} \mathrm{det} \left( \langle
u^{\left(\lambda\right)}_{m\mathbf{k}_{j}} |
u^{\left(\lambda\right)}_{n\mathbf{k}_{j+1}}\rangle \right)$

with **k**_(j)= **k**_(⊥)+j**G**_(\|\|)/*J* (with *j*=0,..,*J*-1), and

$\langle D \rangle =
\frac{1}{N_{k_{\perp}}}\sum_{\mathbf{k}_{\perp}}
D^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right),$

and where we used **R**_(i)·**G**_(j)=2πδ_(ij).

Assuming the *D*_(J)^((λ))(**k**_(⊥)) are reasonably well-clustered
around ⟨*D*⟩, all terms *D*_(J)^((λ))(**k**_(⊥))/⟨*D*⟩ will lie on the
same branch of the logarithm. This makes it less likely that
(**P**_(e)^((λ)))_(i) will pick up a spurious contribution (of
*n***R**_(i)/*N*_(**k**_(⊥))).

## Self-consistent response to finite electric fields
As of version 5.2, VASP can calculate the ground state of an insulating
system under the application of a finite homogeneous electric field. The
VASP implementation closely follows the *PEAD* (Perturbation Expression
After Discretization) approach of Nunes and
Gonze^([\[7\]](#cite_note-nunes:prb:01-7)) and the work of Souza *et
al.*.^([\[8\]](#cite_note-souza:prl:02-8))

In short: to determine the ground state of an insulating system under
the application of a finite homogeneous electric field *ε*, VASP solves
for the field-polarized Bloch functions {*ψ*^((*ε*))} by minimizing the
electric enthalpy functional:

$E\[\\\psi^{({\mathcal E})}\\,{\mathcal E}\]=
E_{0}\[\\\psi^{({\mathcal E})}\\\]-\Omega {\mathcal E} \cdot
\mathbf{P}\[\\\psi^{({\mathcal E})}\\\],$

where **P**\[{*ψ*^((*ε*))}\] is the macroscopic polarization as defined
in the [modern theory of polarization](#Modern_Theory_of_Polarization):

$\mathbf{P}\[\\\psi^{({\mathcal
E})}\\\]=-\frac{2ie}{(2\pi)^3}\sum_n \int_{\mathrm{BZ}} d\mathbf{k}
\langle u^{({\mathcal E})}_{n\mathbf{k}}| \nabla_{\mathbf{k}}|
u^{({\mathcal E})}_{n\mathbf{k}} \rangle$

and u^((*ε*))_(n**k**) is the cell-periodic part of
*ψ*^((*ε*))_(n**k**).

The second term on the right-hand side of the [electric enthalpy
functional](#EdotP) introduces a corresponding additional term to the
Hamiltonian

$H |\psi^{({\mathcal
E})}_{n\mathbf{k}}\rangle=H_0 |\psi^{({\mathcal
E})}_{n\mathbf{k}}\rangle -\Omega {\mathcal E}\cdot \frac{\delta
\mathbf{P}\left\[\\\psi^{({\mathcal E})} \\\right\]}{\delta \langle
\psi^{({\mathcal E})}_{n\mathbf{k}}|}.$

Following the work of Nunes and
Gonze^([\[7\]](#cite_note-nunes:prb:01-7)) we write,

$\frac{\delta \mathbf{P}\left\[\\\psi^{({\mathcal
E})} \\\right\]}{\delta \langle \psi^{({\mathcal E})}_{n\mathbf{k}}|}=
-\frac{ie}{2\Delta k} \sum^N_{m=1} \left\[ | u^{({\mathcal
E})}_{m\mathbf{k}_{j+1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j+1}) - | u^{({\mathcal
E})}_{m\mathbf{k}_{j-1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j-1})\right\]$

where *m* runs over the *N* occupied bands of the system,
Δ*k*=\|**k**_(j+1)-**k**_(j)\|, and

$S_{nm}(\mathbf{k}_j,\mathbf{k}_{j+1})= \langle
u^{({\mathcal E})}_{n\mathbf{k}_{j}}| u^{({\mathcal
E})}_{m\mathbf{k}_{j+1}}\rangle .$

This Hamiltonian allows one to solve for {*ψ*^((*ε*))} by means of a
[direct optimization
method](https://vasp.at/wiki/index.php/index.php)").

**Note**: By analogy, it can be shown that

$\frac{\partial |u_{n\mathbf{k}_j}
\rangle}{\partial k}= \frac{ie}{2\Delta k} \sum^N_{m=1} \left\[ |
u^{({\mathcal E})}_{m\mathbf{k}_{j+1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j+1}) - | u^{({\mathcal
E})}_{m\mathbf{k}_{j-1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j-1})\right\]$

in the sense of a first-order finite difference scheme (higher-order
stencils may be similarly defined).^([\[7\]](#cite_note-nunes:prb:01-7))

**Note**: One should be aware that when the electric field is chosen to
be too large, the electric enthalpy functional will lose its minima, and
VASP will not be able to find a stationary solution for the
field-polarized orbitals. This is discussed in some detail by Souza *et
al.*.^([\[8\]](#cite_note-souza:prl:02-8)) VASP will produce a warning
if:

$e|\mathcal{E}\cdot
\mathbf{a}_i|>\frac{1}{10}E_{\mathrm{gap}}/N_i,$

where *E*_(gap) is the bandgap, **a**_(i) are the lattice vectors, and
*N*_(i) is the number of **k**-points along the reciprocal lattice
vector *i*, in the regular (*N*₁×*N*₂×*N*₃) **k**-mesh. The factor 1/10
is chosen to be on the safe side. If one does not include unoccupied
bands, VASP is obviously not able to determine the bandgap and can not
check whether the electric field might be too large. This will also
produce a warning message.

### Response properties
The change in the macroscopic polarization due to the electric field *ε*
defines the ion-clamped static dielectric tensor

$\epsilon^\infty_{ij}=\delta_{ij}+
\frac{4\pi}{\epsilon_0}\frac{\partial P_i}{\partial {\mathcal E}_j},
\qquad {i,j=x,y,z},$

the change in the Hellmann-Feynman forces due to *ε*, the Born effective
charge tensors

$Z^\*_{ij}=\frac{\Omega}{e}\frac{\partial
P_i}{\partial u_j} =\frac{1}{e}\frac{\partial F_j}{\partial
\mathcal{E}_i}, \qquad {i,j=x,y,z},$

and the ion-clamped piezoelectric tensor of the system

$e^{(0)}_{ij}=-\frac{\partial \sigma_i}{\partial
\mathcal{E}_j}, \qquad {i=xx, yy, zz, xy, yz, zx}\quad{j=x,y,z},$

is found as the change in the stress tensor.

## Related Tags and Sections
[LCALCPOL](../incar-tags/LCALCPOL.md),
[LCALCEPS](../incar-tags/LCALCEPS.md),
[EFIELD_PEAD](../incar-tags/EFIELD_PEAD.md),
[LPEAD](../incar-tags/LPEAD.md), [IPEAD](../incar-tags/IPEAD.md),
[LBERRY](../incar-tags/LBERRY.md), [IGPAR](../incar-tags/IGPAR.md),
[NPPSTR](../incar-tags/NPPSTR.md), [DIPOL](../incar-tags/DIPOL.md)

## References
1.  [↑](#cite_ref-Vogl78_1-0) [P. Vogl, J. Phys. C: Solid State Phys.
    11, 251 (1978).](http://dx.doi.org/10.1088/0022-3719/11/2/011)
2.  ↑ ^([a](#cite_ref-Vanderbilt93I_2-0))
    ^([b](#cite_ref-Vanderbilt93I_2-1))
    ^([c](#cite_ref-Vanderbilt93I_2-2)) [R. D. King-Smith and D.
    Vanderbilt, Phys. Rev. B 47, 1651
    (1993).](http://link.aps.org/doi/10.1103/PhysRevB.47.1651)
3.  ↑ ^([a](#cite_ref-Resta92_3-0)) ^([b](#cite_ref-Resta92_3-1)) [R.
    Resta, Ferroelectrics 136, 51
    (1992).](http://dx.doi.org/10.1080/00150199208016065)
4.  [↑](#cite_ref-Resta94_4-0) [R. Resta, Rev. Mod. Phys. 66, 899
    (1994).](http://link.aps.org/doi/10.1103/RevModPhys.66.899)
5.  [↑](#cite_ref-Resta96_5-0) R. Resta, in *Berry Phase in Electronic
    Wavefunctions*, Troisième Cycle de la Physique en Suisse Romande,
    Année Academique 1995-96, (1996).
6.  [↑](#cite_ref-MonkhorstPack_6-0) [H. J. Monkhorst and J. D. Pack,
    Phys. Rev. B 13, 5188
    (1976).](http://link.aps.org/doi/10.1103/PhysRevB.13.5188)
7.  ↑ ^([a](#cite_ref-nunes:prb:01_7-0))
    ^([b](#cite_ref-nunes:prb:01_7-1))
    ^([c](#cite_ref-nunes:prb:01_7-2)) [R. W. Nunes and X. Gonze, Phys.
    Rev. B 63, 155107
    (2001).](http://link.aps.org/doi/10.1103/PhysRevB.63.155107)
8.  ↑ ^([a](#cite_ref-souza:prl:02_8-0))
    ^([b](#cite_ref-souza:prl:02_8-1)) [I. Souza, J. Íñiguez, and D.
    Vanderbilt, Phys. Rev. Lett. 89, 117602
    (2002).](http://link.aps.org/doi/10.1103/PhysRevLett.89.117602)

------------------------------------------------------------------------

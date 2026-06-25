<!-- Source: https://vasp.at/wiki/index.php/Berry_phases_and_finite_electric_fields | revid: 30684 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Berry phases and finite electric fields



## Contents


- [1 Modern Theory
  of Polarization](#Modern_Theory_of_Polarization)
  - [1.1 Berry
    phase expression for the macroscopic
    polarization](#Berry_phase_expression_for_the_macroscopic_polarization)
  - [1.2
    Computational
    aspects](#Computational_aspects)
- [2
  Self-consistent response to finite electric
  fields](#Self-consistent_response_to_finite_electric_fields)
  - [2.1 Response
    properties](#Response_properties)
- [3 Related Tags
  and Sections](#Related_Tags_and_Sections)
- [4
  References](#References)


## Modern Theory of Polarization\[<a
href="/wiki/index.php?title=Berry_phases_and_finite_electric_fields&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Modern Theory of Polarization">edit</a> \| (./index.php.md)\]

### Berry phase expression for the macroscopic polarization\[<a
href="/wiki/index.php?title=Berry_phases_and_finite_electric_fields&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Berry phase expression for the macroscopic polarization">edit</a> \| (./index.php.md)\]

Calculating the change in dipole moment per unit cell under PBC's, is a
nontrivial task. In general one *cannot* define it as the first moment
of the induced change in charge density δ(**r**), through

$\Delta \mathbf{P}= \frac{1}{\Omega_{0}} \int_{\Omega_{0}} \mathbf{r}
\delta \left( \mathbf{r} \right) d^{3}r$

without introducing a dependency on the shape of Ω<sub>0</sub>, the
chosen unit
cell.<sup>[\[1\]](#cite_note-Vogl78-1)</sup>

Recently King-Smith and
Vanderbilt<sup>[\[2\]](#cite_note-Vanderbilt93I-2)</sup>,
building on the work of
Resta<sup>[\[3\]](#cite_note-Resta92-3)</sup>,
showed that the electronic contribution to the difference in
polarization Δ**P**<sub>e</sub>, due to a finite adiabatic change in the
Hamiltonian of a system, can be identified as a *geometric quantum
phase* or *Berry phase* of the valence wave functions. We will briefly
summarize the essential results (for a review of geometric quantum
phases in polarization theory see the papers of
Resta<sup>[\[4\]](#cite_note-Resta94-4)[\[5\]](#cite_note-Resta96-5)</sup>).

Central to the modern theory of polarization is the proposition of
Resta<sup>[\[3\]](#cite_note-Resta92-3)</sup>
to write the electronic contribution to the change in polarization due
to a finite adiabatic change in the Kohn-Sham Hamiltonian of the
crystalline solid, as

 

$\Delta \mathbf{P}_{e}= \int^{\lambda_{2}}_{\lambda_{1}}{\partial
\mathbf{P}_{e} \over \partial \lambda} d\lambda$

with

${\partial \mathbf{P}_{e} \over \partial \lambda}= {i |e| \hbar \over
N \Omega_{0} m_{e}} \sum_{\mathbf{k}} \sum^{M}_{n=1}
\sum^{\infty}_{m=M+1} {\langle
\psi^{\left(\lambda\right)}_{n\mathbf{k}} | \mathbf{\hat{p}} |
\psi^{\left(\lambda\right)}_{m\mathbf{k}}\rangle \langle
\psi^{\left(\lambda\right)}_{m\mathbf{k}} | \partial
V^{\left(\lambda\right)}/\partial \lambda |
\psi^{\left(\lambda\right)}_{n\mathbf{k}}\rangle \over \left(
\epsilon^{\left(\lambda\right)}_{n\mathbf{k}}-
\epsilon^{\left(\lambda\right)}_{m\mathbf{k}} \right)^{2}}+
\mathrm{c.c.}$

where *m<sub>e</sub>* and *e* are the electronic mass and charge, *N* is
the number of unit cells in the crystal, Ω<sub>0</sub> is the unit cell
volume, *M* is the number of occupied bands, **p** is the momentum
operator, and the functions ψ<sup>(λ)</sup><sub>n**k**</sub> are the
usual Bloch solutions to the crystalline Hamiltonian. Within Kohn-Sham
density-functional theory, the potential V<sup>(λ)</sup> is to be
interpreted as the Kohn-Sham potential V<sup>(λ)</sup><sub>KS</sub>,
where λ parameterizes some change in this potential, for instance due to
the displacement of an atom in the unit cell.

King-Smith and
Vanderbilt<sup>[\[2\]](#cite_note-Vanderbilt93I-2)</sup>
have cast this expression in a form in which the conduction band states
ψ<sup>(λ)</sup><sub>m**k**</sub> no longer explicitly appear, and they
show that [the change in polarization](#PolarizationChange1) along an
arbitrary path, can be found from only a knowledge of the system at the
end points

 

$\Delta \mathbf{P}_{e}= \mathbf{P}^{\left(\lambda_{2} \right)}_{e} -
\mathbf{P}^{\left(\lambda_{1}\right)}_{e}$

with

 

$\mathbf{P}^{\left(\lambda\right)}_{e}=-{if|e|\over 8\pi^{3}}
\sum^{M}_{n=1}\int_{BZ} d^{3}k \langle
u^{\left(\lambda\right)}_{n\mathbf{k}} | \nabla_{\mathbf{k}} |
u^{\left(\lambda\right)}_{n\mathbf{k}} \rangle$

where *f* is the occupation number of the states in the valence bands,
u<sup>(λ)</sup><sub>n**k**</sub> is the cell-periodic part of the Bloch
function ψ<sup>(λ)</sup><sub>n**k**</sub>, and the sum *n* runs over all
*M* occupied bands.

The physics behind [the equation above](#Polarization) becomes more
transparent when this expression is written in terms of the Wannier
functions of the occupied bands,

 

$\mathbf{P}^{\left(\lambda\right)}_{e}=-{f |e| \over \Omega_{0}}
\sum^{M}_{n=1} \langle W^{\left(\lambda\right)}_{n} | \mathbf{r}
|W^{\left(\lambda\right)}_{n} \rangle$

where W<sub>n</sub> is the Wannier function corresponding to valence
band *n*.

This shows the change in polarization of a solid, induced by an
adiabatic change in the Hamiltonian, to be proportional to the
displacement of the charge centers **r**<sub>n</sub>=⟨
W<sup>(λ)</sup><sub>n</sub>\|**r**\| W<sup>(λ)</sup><sub>n</sub>⟩, of
the Wannier functions corresponding to the valence bands.

It is important to realize that the [polarization in terms of
Bloch](#Polarization) or [Wannier](#Wannier) functions, and consequently
the [change in polarization](#PolarizationChange2), is only well-defined
modulo *fe***R**/Ω<sub>0</sub>, where **R** is a lattice vector. This
indeterminacy stems from the fact that the charge center of a Wannier
function is only invariant modulo **R**, with respect to the choice of
phase of the Bloch functions.

In practice one is usually interested in polarization changes
\|Δ**P**<sub>e</sub>\| \<\< \|*fe***R**<sub>1</sub>/Ω<sub>0</sub>\|,
where **R**<sub>1</sub> is the shortest nonzero lattice vector. An
arbitrary term *fe***R**/Ω<sub>0</sub> can therefore often be removed by
simple inspection of the results. In cases where \|Δ**P**<sub>e</sub>\|
is of the same order of magnitude as *fe***R**<sub>1</sub>/Ω<sub>0</sub>
any uncertainty can always be removed by dividing the total change in
the Hamiltonian λ<sub>1</sub>→λ<sub>2</sub> into a number of intervals.

### Computational aspects\[<a
href="/wiki/index.php?title=Berry_phases_and_finite_electric_fields&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Computational aspects">edit</a> \| (./index.php.md)\]

In general, the direct evaluation of
[**P**<sub>e</sub><sup>(λ)</sup>](#Polarization) is useless, because
there is no specific relationship between the phases of the eigenvectors
u<sup>(λ)</sup><sub>**k**n</sub> generated by a numerical
diagonalization routine. This problem is circumvented by dividing the
Brillouin zone integration in two parts, a two-dimensional integral and
a line integral, and by transforming [the above](#Polarization) into
three equations, which separately provide the components of
**P**<sub>e</sub><sup>(λ)</sup> along the directions of three reciprocal
lattice vectors **G**<sub>1</sub>, **G**<sub>2</sub>, and
**G**<sub>3</sub>, which together span a unit cell of the reciprocal
lattice. The component of **P**<sub>e</sub><sup>(λ)</sup> along for
instance **G**<sub>1</sub> can be found from

 

$\mathbf{G}_{1} \cdot
\mathbf{P}_{e}^{\left(\lambda\right)}=-{if|e|\over 8\pi^{3}}
\int_{A} dk_{2}dk_{3} \sum^{M}_{n=1} \int^{|\mathbf{G}_{1}|}_{0}
dk_{1} \langle u^{\left(\lambda\right)}_{n\mathbf{k}}
|\partial/\partial k_{1} | u^{\left(\lambda\right)}_{n\mathbf{k}}
\rangle$

where the two-dimensional integral is taken over the area *A*, spanned
by **G**<sub>2</sub> and **G**<sub>3</sub>, and the line integral runs
over a line segment parallel to **G**<sub>1</sub>. Interchanging the
indices *1*, *2* and *3* in [the equation above](#Polarization2) yields
the expressions for two other components of
**P**<sub>e</sub><sup>(λ)</sup>.

Thus the electronic part of the polarization
**P**<sub>e</sub><sup>(λ)</sup> is given (modulo
*fe***R**/Ω<sub>0</sub>) by the sum

$\sum^{3}_{i=1}(\mathbf{P}_{e}^{\left(\lambda\right)})_{i}=\sum^{3}_{i=1}
\left(\mathbf{G}_{i} \cdot
\mathbf{P}_{e}^{\left(\lambda\right)}\right) {\mathbf{R}_{i} \over
2\pi}$

where the lattice vectors **R**<sub>i</sub> obey the relationship
**R**<sub>i</sub>·**G**<sub>j</sub>=2πδ<sub>ij</sub>.

The integration over *A* in [the above](#Polarization2), is
straightforward and can be performed by sampling a 2D Monkhorst-Pack
mesh of
*k*-points,<sup>[\[6\]](#cite_note-MonkhorstPack-6)</sup>
termed the *perpendicular mesh* or **k**<sub>⊥</sub>-mesh by King-Smith
and Vanderbilt. However, to remove the influence of the random phase of
the functions u<sup>(λ)</sup><sub>n**k**</sub>, introduced by the
diagonalization routine, King-Smith and
Vanderbilt<sup>[\[2\]](#cite_note-Vanderbilt93I-2)</sup>
propose to replace the line integral alias integration in the *parallel*
or **G**<sub>\|\|</sub> direction by,

 

$\phi^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right)=\mathrm{Im}
\left\\\ln \prod^{J-1}_{j=0} \mathrm{det} \left( \langle
u^{\left(\lambda\right)}_{m\mathbf{k}_{j}} |
u^{\left(\lambda\right)}_{n\mathbf{k}_{j+1}}\rangle \right)\right\\$

which is evaluated by calculating the cell-periodic parts of the wave
functions at a string of *J* *k*-points, **k**<sub>j</sub>=
**k**<sub>⊥</sub>+j**G**<sub>\|\|</sub>/*J* (with *j*=0,..,*J*-1), and
where for sufficiently large *J* one has that

 

$\phi^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right)=
-i\sum^{M}_{n=1} \int^{|\mathbf{G}_{\parallel}|}_{0}
dk_{\parallel} \langle u^{\left(\lambda\right)}_{n\mathbf{k}} |
\partial/\partial k_{\parallel} |
u^{\left(\lambda\right)}_{n\mathbf{k}} \rangle$

**Note**: the determinant appearing in [the equation above](#CyclicForm)
is the determinant of the *M*×*M* matrix formed by letting *n* and *m*
run over all valence bands.

The crucial step, instrumental in removing the random phase, is that the
functions u<sup>(λ)</sup><sub>n**k**<sub>J</sub></sub> are not obtained
from an independent diagonalization, but found through their
relationship with the functions
u<sup>(λ)</sup><sub>n**k**<sub>0</sub></sub>,

 

$u^{\left(\lambda\right)}_{n\mathbf{k}_{J}}(\mathbf{r})=
e^{-i\mathbf{G}_{\parallel}\cdot \mathbf{r}}
u^{\left(\lambda\right)}_{n\mathbf{k}_{0}}(\mathbf{r})$

This way the product [φ<sub>J</sub><sup>(λ)</sup>](#CyclicForm) becomes
cyclic, and contains both u<sup>(λ)</sup><sub>n**k**<sub>j</sub></sub>
as well as its complex conjugate for every *k*-point in the string, thus
removing the random phase.

In practice
[**G**<sub>\|\|</sub>·**P**<sub>e</sub><sup>(λ)</sup>](#Polarization2)
is evaluated by way of the following summation over the
**k**<sub>⊥</sub>-mesh,

 

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

with **k**<sub>j</sub>= **k**<sub>⊥</sub>+j**G**<sub>\|\|</sub>/*J*
(with *j*=0,..,*J*-1), and

$\langle D \rangle = \frac{1}{N_{k_{\perp}}}\sum_{\mathbf{k}_{\perp}}
D^{\left(\lambda\right)}_{J}\left(\mathbf{k}_{\perp}\right),$

and where we used **R**<sub>i</sub>·**G**<sub>j</sub>=2πδ<sub>ij</sub>.

Assuming the *D*<sub>J</sub><sup>(λ)</sup>(**k**<sub>⊥</sub>) are
reasonably well-clustered around ⟨*D*⟩, all terms
*D*<sub>J</sub><sup>(λ)</sup>(**k**<sub>⊥</sub>)/⟨*D*⟩ will lie on the
same branch of the logarithm. This makes it less likely that
(**P**<sub>e</sub><sup>(λ)</sup>)<sub>i</sub> will pick up a spurious
contribution (of *n***R**<sub>i</sub>/*N*<sub>**k**<sub>⊥</sub></sub>).

## Self-consistent response to finite electric fields\[<a
href="/wiki/index.php?title=Berry_phases_and_finite_electric_fields&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Self-consistent response to finite electric fields">edit</a> \| (./index.php.md)\]

As of version 5.2, VASP can calculate the ground state of an insulating
system under the application of a finite homogeneous electric field. The
VASP implementation closely follows the *PEAD* (Perturbation Expression
After Discretization) approach of Nunes and
Gonze<sup>[\[7\]](#cite_note-nunes:prb:01-7)</sup>
and the work of Souza *et
al.*.<sup>[\[8\]](#cite_note-souza:prl:02-8)</sup>

In short: to determine the ground state of an insulating system under
the application of a finite homogeneous electric field
*ε*, VASP solves for the
field-polarized Bloch functions
{*ψ*<sup>(*ε*)</sup>} by minimizing
the electric enthalpy functional:

 

$E\[\\\psi^{({\mathcal E})}\\,{\mathcal E}\]= E_{0}\[\\\psi^{({\mathcal
E})}\\\]-\Omega {\mathcal E} \cdot \mathbf{P}\[\\\psi^{({\mathcal
E})}\\\],$

where **P**\[{*ψ*<sup>(*ε*)</sup>}\]
is the macroscopic polarization as defined in the [modern theory of
polarization](#Modern_Theory_of_Polarization):

 

$\mathbf{P}\[\\\psi^{({\mathcal E})}\\\]=-\frac{2ie}{(2\pi)^3}\sum_n
\int_{\mathrm{BZ}} d\mathbf{k} \langle u^{({\mathcal
E})}_{n\mathbf{k}}| \nabla_{\mathbf{k}}| u^{({\mathcal
E})}_{n\mathbf{k}} \rangle$

and
u<sup>(*ε*)</sup><sub>n**k**</sub>
is the cell-periodic part of
*ψ*<sup>(*ε*)</sup><sub>n**k**</sub>.

The second term on the right-hand side of the [electric enthalpy
functional](#EdotP) introduces a corresponding additional term to the
Hamiltonian

 

$H
|\psi^{({\mathcal E})}_{n\mathbf{k}}\rangle=H_0 |\psi^{({\mathcal
E})}_{n\mathbf{k}}\rangle -\Omega {\mathcal E}\cdot \frac{\delta
\mathbf{P}\left\[\\\psi^{({\mathcal E})} \\\right\]}{\delta \langle
\psi^{({\mathcal E})}_{n\mathbf{k}}|}.$

Following the work of Nunes and
Gonze<sup>[\[7\]](#cite_note-nunes:prb:01-7)</sup>
we write,

$\frac{\delta \mathbf{P}\left\[\\\psi^{({\mathcal E})} \\\right\]}{\delta
\langle \psi^{({\mathcal E})}_{n\mathbf{k}}|}= -\frac{ie}{2\Delta k}
\sum^N_{m=1} \left\[ | u^{({\mathcal E})}_{m\mathbf{k}_{j+1}}
\rangle S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j+1}) - | u^{({\mathcal
E})}_{m\mathbf{k}_{j-1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j-1})\right\]$

where *m* runs over the *N* occupied bands of the system,
Δ*k*=\|**k**<sub>j+1</sub>-**k**<sub>j</sub>\|, and

$S_{nm}(\mathbf{k}_j,\mathbf{k}_{j+1})= \langle u^{({\mathcal
E})}_{n\mathbf{k}_{j}}| u^{({\mathcal
E})}_{m\mathbf{k}_{j+1}}\rangle .$

This Hamiltonian allows one to solve for
{*ψ*<sup>(*ε*)</sup>} by means of a
<a
href="/wiki/index.php?title=Direct_optimization_method&amp;action=edit&amp;redlink=1"
class="new"
title="Direct optimization method (page does not exist)">direct
optimization method</a>.

**Note**: By analogy, it can be shown that

$\frac{\partial |u_{n\mathbf{k}_j} \rangle}{\partial k}=
\frac{ie}{2\Delta k} \sum^N_{m=1} \left\[ | u^{({\mathcal
E})}_{m\mathbf{k}_{j+1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j+1}) - | u^{({\mathcal
E})}_{m\mathbf{k}_{j-1}} \rangle
S^{-1}_{mn}(\mathbf{k}_j,\mathbf{k}_{j-1})\right\]$

in the sense of a first-order finite difference scheme (higher-order
stencils may be similarly
defined).<sup>[\[7\]](#cite_note-nunes:prb:01-7)</sup>

**Note**: One should be aware that when the electric field is chosen to
be too large, the electric enthalpy functional will lose its minima, and
VASP will not be able to find a stationary solution for the
field-polarized orbitals. This is discussed in some detail by Souza *et
al.*.<sup>[\[8\]](#cite_note-souza:prl:02-8)</sup>
VASP will produce a warning if:

$e|\mathcal{E}\cdot \mathbf{a}_i|>\frac{1}{10}E_{\mathrm{gap}}/N_i,$

where *E*<sub>gap</sub> is the bandgap, **a**<sub>i</sub> are the
lattice vectors, and *N*<sub>i</sub> is the number of **k**-points along
the reciprocal lattice vector *i*, in the regular
(*N*<sub>1</sub>×*N*<sub>2</sub>×*N*<sub>3</sub>) **k**-mesh. The factor
1/10 is chosen to be on the safe side. If one does not include
unoccupied bands, VASP is obviously not able to determine the bandgap
and can not check whether the electric field might be too large. This
will also produce a warning message.

### Response properties\[<a
href="/wiki/index.php?title=Berry_phases_and_finite_electric_fields&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Response properties">edit</a> \| (./index.php.md)\]

The change in the macroscopic polarization due to the electric field
*ε* defines the ion-clamped static
dielectric tensor

$\epsilon^\infty_{ij}=\delta_{ij}+
\frac{4\pi}{\epsilon_0}\frac{\partial P_i}{\partial {\mathcal E}_j},
\qquad {i,j=x,y,z},$

the change in the Hellmann-Feynman forces due to
*ε*, the Born effective charge
tensors

$Z^\*_{ij}=\frac{\Omega}{e}\frac{\partial P_i}{\partial u_j}
=\frac{1}{e}\frac{\partial F_j}{\partial \mathcal{E}_i}, \qquad
{i,j=x,y,z},$

and the ion-clamped piezoelectric tensor of the system

$e^{(0)}_{ij}=-\frac{\partial \sigma_i}{\partial \mathcal{E}_j}, \qquad
{i=xx, yy, zz, xy, yz, zx}\quad{j=x,y,z},$

is found as the change in the stress tensor.

## Related Tags and Sections\[<a
href="/wiki/index.php?title=Berry_phases_and_finite_electric_fields&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[LCALCPOL](../incar-tags/LCALCPOL.md),
[LCALCEPS](../incar-tags/LCALCEPS.md),
[EFIELD_PEAD](../incar-tags/EFIELD_PEAD.md),
[LPEAD](../incar-tags/LPEAD.md), [IPEAD](../incar-tags/IPEAD.md),
[LBERRY](../incar-tags/LBERRY.md), [IGPAR](../incar-tags/IGPAR.md),
[NPPSTR](../incar-tags/NPPSTR.md), [DIPOL](../incar-tags/DIPOL.md)

## References\[<a
href="/wiki/index.php?title=Berry_phases_and_finite_electric_fields&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-Vogl78_1-0)
    <a href="http://dx.doi.org/10.1088/0022-3719/11/2/011"
    class="external text" rel="nofollow">P. Vogl, J. Phys. C: Solid State
    Phys. 11, 251 (1978).</a>
2.  ↑
    <sup>[a](#cite_ref-Vanderbilt93I_2-0)</sup>
    <sup>[b](#cite_ref-Vanderbilt93I_2-1)</sup>
    <sup>[c](#cite_ref-Vanderbilt93I_2-2)</sup>
    <a href="http://link.aps.org/doi/10.1103/PhysRevB.47.1651"
    class="external text" rel="nofollow">R. D. King-Smith and D. Vanderbilt,
    Phys. Rev. B 47, 1651 (1993).</a>
3.  ↑
    <sup>[a](#cite_ref-Resta92_3-0)</sup>
    <sup>[b](#cite_ref-Resta92_3-1)</sup>
    <a href="http://dx.doi.org/10.1080/00150199208016065"
    class="external text" rel="nofollow">R. Resta, Ferroelectrics 136, 51
    (1992).</a>
4.  [↑](#cite_ref-Resta94_4-0)
    <a href="http://link.aps.org/doi/10.1103/RevModPhys.66.899"
    class="external text" rel="nofollow">R. Resta, Rev. Mod. Phys. 66, 899
    (1994).</a>
5.  [↑](#cite_ref-Resta96_5-0)
    R. Resta, in *Berry Phase in Electronic
    Wavefunctions*, Troisième Cycle de la Physique en Suisse Romande,
    Année Academique 1995-96, (1996).
6.  [↑](#cite_ref-MonkhorstPack_6-0)
    <a href="http://link.aps.org/doi/10.1103/PhysRevB.13.5188"
    class="external text" rel="nofollow">H. J. Monkhorst and J. D. Pack,
    Phys. Rev. B 13, 5188 (1976).</a>
7.  ↑
    <sup>[a](#cite_ref-nunes:prb:01_7-0)</sup>
    <sup>[b](#cite_ref-nunes:prb:01_7-1)</sup>
    <sup>[c](#cite_ref-nunes:prb:01_7-2)</sup>
    <a href="http://link.aps.org/doi/10.1103/PhysRevB.63.155107"
    class="external text" rel="nofollow">R. W. Nunes and X. Gonze, Phys.
    Rev. B 63, 155107 (2001).</a>
8.  ↑
    <sup>[a](#cite_ref-souza:prl:02_8-0)</sup>
    <sup>[b](#cite_ref-souza:prl:02_8-1)</sup>
    <a href="http://link.aps.org/doi/10.1103/PhysRevLett.89.117602"
    class="external text" rel="nofollow">I. Souza, J. Íñiguez, and D.
    Vanderbilt, Phys. Rev. Lett. 89, 117602 (2002).</a>


------------------------------------------------------------------------



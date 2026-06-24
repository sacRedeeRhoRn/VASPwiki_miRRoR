<!-- Source: https://vasp.at/wiki/index.php/Integrating_over_all_orbitals | revid: 32816 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Integrating over all orbitals
Computing expectation values of observables *O* over all Kohn-Sham
orbitals is an important concept relevant to most *ab initio*
calculations. Typically, we can evaluate these expectation values as
integral over all orbitals

$\langle O \rangle = \sum_n
\frac{1}{\Omega_{\mathrm{BZ}}} \int_{\Omega_{\mathrm{BZ}}}
O_{n\mathbf{k}} \\ \Theta(\epsilon_{\mathrm{F}} -
\epsilon_{n\mathbf{k}}) \\ d^{3}k,$

where Ω_(BZ) is the volume of the Brillouin zone, *O*_(n**k**) is the
expectation value of the observable with a single Kohn-Sham orbital, and
Θ is the [Heaviside step
function](https://en.wikipedia.org/wiki/Heaviside_step_function) and
limits the integral to orbitals with eigenvalues ϵ_(n**k**) below the
Fermi energy ϵ_(F).

When evaluating the integral above numerically, we need to address two
concerns: (i) We need to discretize the **k**-point integral since we do
not know the analytic expression of the observable. (ii) A sharp
function cutoff like the Heaviside function is numerically unstable so
we need robust smearing methods.

## Contents

- [1 Integrating over **k** points](#Integrating_over_k_points)
- [2 Integrating near the Fermi
  energy](#Integrating_near_the_Fermi_energy)
- [3 Tetrahedron method](#Tetrahedron_method)
- [4 Determining the Fermi energy](#Determining_the_Fermi_energy)
- [5 Related tags and sections](#Related_tags_and_sections)
- [6 References](#References)

## Integrating over **k** points
Discretizing the **k**-point integral involves replacing the continuous
integral over the Brillouin zone by a **k**-point
mesh.^([\[1\]](#cite_note-baldereschi:prb:1973-1)[\[2\]](#cite_note-chadi:prb:1973-2)[\[3\]](#cite_note-monkhorst:prb:1976-3))

$\frac{1}{\Omega_{\mathrm{BZ}}}
\int_{\Omega_{\mathrm{BZ}}} \to \sum_{\mathbf{k}} w_{\mathbf{k}}.$

A **k**-point mesh consists of **k**-point coordinates and associated
weights *w*_(**k**). In general, any mesh could be chosen but for
periodic boundaries the optimal one are equidistant grids. In VASP, we
select this sampling by a [KPOINTS](../input-files/KPOINTS.md) file or the
[KSPACING](../incar-tags/KSPACING.md) tag.

We can improve the integrals further because the crystal exhibits
certain symmetries. Often we can deduce the value *O*_(n**k**) from a
different symmetry-equivalent **k** point. VASP automatically analyzes
the symmetry of the crystal and reduces the **k** point mesh to the
irreducible Brillouin zone. The weights of each irreducible **k** point
measure how many equivalent **k** points exist in the reducible
Brillouin zone.

## Integrating near the Fermi energy
[![](https://vasp.at/wiki/images/thumb/1/14/Integrated.png/400px-Integrated.png)](https://vasp.at/wiki/File:Integrated.png)

Occupation of different smearing techniques near the Fermi energy ϵ_(F).
The energy is measured in units of the smearing σ
([SIGMA](../incar-tags/SIGMA.md)). The Methfessel-Paxton method (cyan) is
closer to the step function than the Gaussian distribution (blue) but
also has nonmonotonous features. The smearing Fermi-Dirac distribution
(purple) corresponds to a temperature but is much broader at the same
value of σ.

We want to replace the Heaviside step function by a smooth equivalent to
make the integral numerically stable. Otherwise small changes in the
energies would toggle the inclusion of a sample *O*_(n**k**) close to
the Fermi energy.

$\sum_{n\mathbf{k}}
\Theta(\epsilon_{\mathrm{F}} - \epsilon_{n\mathbf{k}}) \ldots \to
\sum_{n\mathbf{k}} f_\sigma(\epsilon_{n\mathbf{k}}) \ldots$

Here, the occupations *f*_(σ)(ϵ_(n**k**)) approach 1 for energies far
below the Fermi energy ϵ_(F) and 0 for energies far above it. The
parameter σ determines how wide the broadened step function is.

In the figure, we illustrate the different smearing methods implemented
in VASP. The Fermi-Dirac smearing
([`ISMEAR`](../incar-tags/ISMEAR.md)` = -1`) uses σ as the temperature in
the Fermi-Dirac distribution^([\[4\]](#cite_note-mermin:pra:1965-4))

$f_\sigma(\epsilon) =
\Bigl\[\exp(\frac{\epsilon-\epsilon_{\mathrm{F}}}{\sigma})+1\Bigr\]^{-1}~.$

One can also use the complementary error function
([`ISMEAR`](../incar-tags/ISMEAR.md)` = 0`) which results from integrating
a Gaussian distribution as the occupation
function.^([\[5\]](#cite_note-devita:phd:1992-5)) This leads to a
narrower edge than the Fermi-Dirac distribution for the same σ and a
faster approach to the asymptotic behavior

$f_\sigma(\epsilon) = \frac{1}{2}
\text{erfc}\Bigl\[\frac{\epsilon-\epsilon_{\mathrm{F}}}{\sigma}\Bigr\]~.$

Methfessel and Paxton ^([\[6\]](#cite_note-methfessel:prb:1989-6))
developed higher order approximations to the step function
([`ISMEAR`](../incar-tags/ISMEAR.md)` > 0`).

$f_\sigma(\epsilon) = \frac{1}{2}
\text{erfc}\Bigl\[\frac{\epsilon-\epsilon_{\mathrm{F}}}{\sigma}\Bigr\] +
\exp\Bigl\[-\bigl(\frac{\epsilon-\epsilon_{\mathrm{F}}}{\sigma}\bigr)^2\Bigr\]
\sum_{i=1}^{n} \frac{(-1)^i}{4^i i! \sqrt\pi}
H_{2i-1}\Bigl\[\frac{\epsilon-\epsilon_{\mathrm{F}}}{\sigma}\Bigr\]~.$

Here, *n* is the order of the expansion and *H*_(j) is the j-th Hermite
polynomial. The first order Methfessel-Paxton smearing is shown in the
figure. This method leads to an even narrower distribution but
introduces a nonmonotonous behavior that can lead to problems in
semiconductors and insulators.

A consequence of these broadening techniques is that the total energy is
no longer variational (or minimal). It is necessary to replace the total
energy by some generalized free energy

$F = E - \sum_{n\mathbf{k}} w_{\mathbf{k}}
\sigma S\[f_\sigma(\epsilon_{n\mathbf{k}})\].$

For the Fermi-Dirac statistics, we might interpret this as the free
energy of the electrons at some finite temperature σ = *k*_(B)*T*. There
is no straightforward interpretation of the free energy in the case of
Gaussian or Methfessel-Paxton smearing. Despite this, it is possible to
obtain an accurate extrapolation for σ → 0 from results at finite σ
using the formula

$E_0 = E(\sigma \to 0) = \frac{1}{2} (F + E)~.$

*E*₀ is a meaningful physical quantity for the ground state energy of
the system. Importantly, the [calculated
forces](../methods/Category-Forces.md) are the derivatives of
the free energy *F* and not of *E*₀. Nonetheless, the difference of the
forces is generally small and acceptable it a suitable σ is used.

When we consider *E*₀ as our target property, the smearing methods serve
as a mathematical tool to obtain faster convergence with respect to the
number of k-points. Generally, the Gaussian broadening requires more
careful tuning of the width σ compared to the Methfessel-Paxton method.
If σ is too large, the energy *E*(σ → 0) will converge to the wrong
value even for an infinite **k**-point mesh. If σ is too small, we
require a much denser **k**-point mesh and a significantly larger
computational cost. With the Methfessel-Paxton method the sharper edge
usually averts the necessity of tuning σ. However, since the occupation
function is nonmonotonous, it is **not** suitable to describe systems
with a bandgap.

## Tetrahedron method
[![](https://vasp.at/wiki/images/thumb/2/25/Tetrahedron.png/400px-Tetrahedron.png)](https://vasp.at/wiki/File:Tetrahedron.png)

Four **k** points forming a single tetrahedron with ordered eigenvalues
ϵ₁, ϵ₂, ϵ₃, and ϵ₄. The lines show the occupation of the orbitals with
changing Fermi energy ϵ_(F) where the darkest line corresponds to the
lowest and the brightest line to the highest eigenvalue. For the
Gaussian smearing (blue) every **k** point is considered individually
leading to half filling when the Fermi energy reaches the eigenvalue.
The tetrahedron method (red) does not fill any orbital if the Fermi
energy is outside of the bounds of the tetrahedron.

The tetrahedron method is an alternative approach to address the sharp
edge of the Heaviside step function. Instead of considering each **k**
point individually, we triangulate the **k**-point mesh, i.e., we split
it into as many tetrahedra as necessary to cover the whole Brillouin
zone. We use a linear interpolation of the band energies ϵ_(n**k**)
within each tetrahedron the band energies.
Blöchl^([\[7\]](#cite_note-bloechl:prb:1994-7)) derived correction terms
to cancel the linearization errors of the tetrahedron method.

With this interpolation, we can solve integral over the Brillouin zone
analytically considering each tetrahedron individually. It does not
require a choice of a width σ like the broadening methods. The figure
illustrates the difference between broadening and interpolation method.
A broadening method like the Gaussian smearing considers every **k**
point individually. Therefore, it will start filling the orbital as soon
as the Fermi energy reaches the width σ of the broadening. In the
tetrahedron method, the **k** points of the tetrahedron only get
occupied once the Fermi energy exceeds the lowest eigenvalue. Similarly,
it is completely filled once the Fermi energy exceeds the maximum value.
As a consequence, the occupations of the different **k** points are much
closer to each other.

Overall, the tetrahedron method yields very accurate occupations with
minimal user input. It is very well suited to obtain accurate integral
(e.g. total energy) and band onsets (e.g. density of state). The main
drawback is that the Blöchel's correction of the linearization errors is
not variational with respect to the partial occupancies. Therefore the
calculated forces might be wrong by a few percent. If accurate forces
are required we recommend a finite temperature method.

## Determining the Fermi energy
One important example of integrals over all orbitals is the calculation
of the Fermi energy. In this case, the observable is identity and the
sum of all occupations should be equal to the number of electrons
*N*_(e)

$\sum_{n\mathbf{k}}
f_\sigma(\epsilon_{n\mathbf{k}}) = N_{\mathrm{e}}~.$

This leads to a straightforward interval-bisection algorithm to compute
the Fermi energy. We guess bounds for the Fermi energy and then compute
the sum of all occupations in the middle of the interval. If this
results in a number larger than the number of electrons, we replace the
upper bound otherwise we replace the lower one.

Note that this algorithm is not deterministic for systems with a
bandgap, where any Fermi energy in the gap would be fine. VASP achieves
more consistent results for these system by a good initial guess for the
Fermi energy (see [EFERMI](../incar-tags/EFERMI.md)). This potentially
leads to an early exit of the bisection algorithm so that only for
metals many iterations of bisection are considered.

## Related tags and sections
[KPOINTS](../input-files/KPOINTS.md), [ISMEAR](../incar-tags/ISMEAR.md),
[SIGMA](../incar-tags/SIGMA.md), [Smearing
technique](../tutorials/Smearing_technique.md)

## References
1.  [↑](#cite_ref-baldereschi:prb:1973_1-0) [A. Baldereschi, Phys. Rev.
    B **7**, 5212 (1973).](https://doi.org/10.1103/PhysRevB.7.5212)
2.  [↑](#cite_ref-chadi:prb:1973_2-0) [D.J. Chadi and M.L. Cohen, Phys.
    Rev. B **8**, 5747 (1973).](https://doi.org/10.1103/PhysRevB.8.5747)
3.  [↑](#cite_ref-monkhorst:prb:1976_3-0) [H.J. Monkhorst and J.D. Pack,
    Phys. Rev. B **13**, 5188
    (1976).](https://doi.org/10.1103/PhysRevB.13.5188)
4.  [↑](#cite_ref-mermin:pra:1965_4-0) [N.D. Mermin, Phys. Rev. **137**,
    A1441 (1965).](https://doi.org/10.1103/PhysRev.137.A1441)
5.  [↑](#cite_ref-devita:phd:1992_5-0) \[ A. De Vita, PhD Thesis, Keele
    University 1992; A. De Vita and M.J. Gillan, preprint (Aug. 1992).\]
6.  [↑](#cite_ref-methfessel:prb:1989_6-0) [M. Methfessel and A.T.
    Paxton, Phys. Rev. B **40**, 3616
    (1989).](https://doi.org/10.1103/PhysRevB.40.3616)
7.  [↑](#cite_ref-bloechl:prb:1994_7-0) [P.E. Blöchl, O. Jepsen, and
    O.K. Andersen, Phys. Rev. B **49**, 16223
    (1994).](https://doi.org/10.1103/PhysRevB.49.16223)

------------------------------------------------------------------------

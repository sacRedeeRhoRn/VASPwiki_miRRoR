<!-- Source: https://vasp.at/wiki/index.php/Biased_molecular_dynamics | revid: 36463 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Biased molecular dynamics


*Biased molecular dynamics'* (MD) refers to advanced [MD-simulation
methods](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
that introduce a *bias potential*. One of the most important purposes of
using bias potentials is to enhance the sampling of phase space with low
probability density (e.g., transition regions of chemical reactions).
Depending on the type of sampling and in combination with the
corresponding statistical methods one then has access to important
thermodynamic quantities like, e.g., free energies. Biased molecular
dynamics comes in very different flavors such as, e.g., umbrella
sampling<sup>[\[1\]](#cite_note-torrie:jcp:1977-1)</sup>
and umbrella
integration<sup>[\[2\]](#cite_note-kaestner:jcp:2005-2)</sup>,
to name a few. For a comprehensive description (especially about
umbrella sampling), we refer the interested user to Ref.
<sup>[\[3\]](#cite_note-frenkel:ap-book:2002-3)</sup>
written by D. Frenkel and B. Smit.

The probability density for a geometric parameter ξ of the system driven
by a Hamiltonian

$H(q,p) = T(p) + V(q), \\$

with *T*(*p*), and *V*(*q*) being kinetic, and potential energies,
respectively, can be written as

$P(\xi_i)=\frac{\int\delta\Big(\xi(q)-\xi_i\Big)
\exp\left\\-H(q,p)/k_B\\T\right\\ dq\\dp}{\int
\exp\left\\-H(q,p)/k_B\\T\right\\dq\\dp} =
\langle\delta\Big(\xi(q)-\xi_i\Big)\rangle_{H}.$

The term $\langle X \rangle_H$ stands for a thermal average of quantity *X* evaluated
for the system driven by the Hamiltonian *H*.

If the system is modified by adding a bias potential
$\tilde{V}(\xi)$ acting on one or multiple selected
internal coordinates of the system ξ=ξ(*q*), the Hamiltonian takes the
form

$\tilde{H}(q,p) = H(q,p) + \tilde{V}(\xi),$

and the probability density of ξ in the biased ensemble is

$\tilde{P}(\xi_i)= \frac{\int \delta\Big(\xi(q)-\xi_i\Big)
\exp\left\\-\tilde{H}(q,p)/k_B\\T\right\\ dq\\dp}{\int
\exp\left\\-\tilde{H}(q,p)/k_B\\T\right\\dq\\dp} =
\langle\delta\Big(\xi(q)-\xi_i\Big)\rangle_{\tilde{H}}.$

It can be shown that the biased and unbiased averages are related via

$P(\xi_i)=\tilde{P}(\xi_i)
\frac{\exp\left\\\tilde{V}(\xi)/k_B\\T\right\}{\langle
\exp\left\\\tilde{V}(\xi)/k_B\\T\right\\ \rangle_{\tilde{H}}}.$

More generally, an observable

$\langle A \rangle_{H} = \frac{\int A(q)
\exp\left\\-H(q,p)/k_B\\T\right\\ dq\\dp}{\int
\exp\left\\-H(q,p)/k_B\\T\right\\dq\\dp}$

can be expressed in terms of thermal averages within the biased ensemble
as

$\langle A \rangle_{H} =\frac{\langle A(q)
\\\exp\left\\\tilde{V}(\xi)/k_B\\T\right\\ \rangle_{\tilde{H}}}{\langle
\exp\left\\\tilde{V}(\xi)/k_B\\T\right\\ \rangle_{\tilde{H}}}.$

One of the most popular methods using bias potentials is umbrella
sampling<sup>[\[1\]](#cite_note-torrie:jcp:1977-1)</sup>.
This method uses a bias potential to enhance sampling of ξ in regions
with low *P*(ξ<sub>*i*</sub>), e.g., transition regions of chemical
reactions. The correct distributions are recovered afterward using the
equation for $\langle A \rangle_{H}$ above.

### How to\[<a
href="/wiki/index.php?title=Biased_molecular_dynamics&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

For a description of biased molecular dynamics see
Biased molecular dynamics.

- For a biased molecular dynamics run with [Andersen
  thermostat](../tutorials/Andersen_thermostat.md), one has
  to:

1.  Set the standard MD-related tags: [IBRION](../incar-tags/IBRION.md)=0,
    [TEBEG](../incar-tags/TEBEG.md), [POTIM](../incar-tags/POTIM.md), and
    [NSW](../incar-tags/NSW.md).
2.  Choose thermostat:
    1.  Set [MDALGO](../incar-tags/MDALGO.md)=1 (or
        [MDALGO](../incar-tags/MDALGO.md)=11 in VASP 5.x), and choose an
        appropriate setting for
        [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md).
    2.  Set [MDALGO](../incar-tags/MDALGO.md)=2 (or
        [MDALGO](../incar-tags/MDALGO.md)=21 in VASP 5.x), and choose an
        appropriate setting for [SMASS](../incar-tags/SMASS.md).
3.  In order to avoid updating of the bias potential, set
    [HILLS_BIN](../incar-tags/HILLS_BIN.md)=[NSW](../incar-tags/NSW.md).
4.  Define collective variables in the
    [ICONST](../input-files/ICONST.md)-file, and set the `STATUS` parameter
    for the collective variables to 5.
5.  Define the bias potential in the
    [PENALTYPOT](../input-files/PENALTYPOT.md) file if necessary.

The values of all collective variables for each MD step are listed in
the [REPORT](../output-files/REPORT.md) file. Check the lines after the
string `Metadynamics`.

## Related tags and articles\[<a
href="/wiki/index.php?title=Biased_molecular_dynamics&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ICONST](../input-files/ICONST.md),
[PENALTYPOT](../input-files/PENALTYPOT.md),
[HILLS_BIN](../incar-tags/HILLS_BIN.md),
[FBIAS_R0](../incar-tags/FBIAS_R0.md),
[FBIAS_A](../incar-tags/FBIAS_A.md), [FBIAS_D](../incar-tags/FBIAS_D.md),
[SPRING_K](../incar-tags/SPRING_K.md),
[SPRING_R0](../incar-tags/SPRING_R0.md),
[SPRING_V0](../incar-tags/SPRING_V0.md),
[REPORT](../output-files/REPORT.md)

[Biased molecular dynamics
calculations](../tutorials/Biased_molecular_dynamics_calculations.md)

## References\[<a
href="/wiki/index.php?title=Biased_molecular_dynamics&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-torrie:jcp:1977_1-0)</sup>
    <sup>[b](#cite_ref-torrie:jcp:1977_1-1)</sup>
    <a href="http://doi.org/10.1016/0021-9991(77)90121-8"
    class="external text" rel="nofollow">G. M. Torrie and J. P. Valleau, J.
    Comp. Phys. <strong>23</strong>, 187 (1977).</a>
2.  [↑](#cite_ref-kaestner:jcp:2005_2-0)
    <a href="https://doi.org/10.1063/1.2052648" class="external text"
    rel="nofollow">J. Kästner, and W. Thiel, <em>Bridging the gap between
    thermodynamic integration and umbrella sampling provides a novel
    analysis method: “Umbrella integration”</em>, J. Chem. Phys.
    <strong>123</strong>, 144104 (2005).</a>
3.  [↑](#cite_ref-frenkel:ap-book:2002_3-0)
    <a href="http://doi.org/10.1016/0021-9991(77)90121-8"
    class="external text" rel="nofollow">D. Frenkel and B. Smit,
    <em>Understanding molecular simulations: from algorithms to
    applications</em>, Academic Press: San Diego, 2002.</a>



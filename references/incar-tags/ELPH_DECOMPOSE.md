<!-- Source: https://vasp.at/wiki/index.php/ELPH_DECOMPOSE | revid: 33076 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_DECOMPOSE


ELPH_DECOMPOSE = \[string\]  
Default: **ELPH_DECOMPOSE** = VDPR 

Description: Chooses which contributions to include in the computation
of the electron-phonon matrix elements.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The electron-phonon matrix element can be formulated in the
[projector-augmented-wave (PAW)
method](../methods/Projector-augmented-wave_formalism.md)
in terms of individual
contributions<sup>[\[1\]](#cite_note-engel:prb:2022-1)</sup>.
Each contribution can be included by specifying the associated letter in
ELPH_DECOMPOSE. We suggest two
different combinations to define matrix elements:

`ELPH_DECOMPOSE`` = VDPR` - "All-electron" (AE) matrix element<sup>[\[1\]](#cite_note-engel:prb:2022-1)[\[2\]](#cite_note-chaput:prb:2019-2)</sup>  
This is the de-facto standard definition of the electron-phonon matrix
element expressed in the language of the PAW method. The AE matrix
element can be used in the framework of many-body perturbation theory
without any further restrictions. It should also be used if one is not
interested in the final observables, but in the values of the matrix
elements themselves, for example, to study scattering channels.

`ELPH_DECOMPOSE`` = VDQ` - "Pseudo" (PS) matrix element<sup>[\[1\]](#cite_note-engel:prb:2022-1)[\[3\]](#cite_note-engel:prb:2020-3)</sup>  
This matrix element arises naturally from the PAW formulation of the
phonon-induced band-structure renormalization in the adiabatic
Rayleigh-Schrödinger perturbation theory. It is only really well-defined
in this particular context. However, when using the PS matrix element
instead of the AE matrix element, the electron self-energy converges
much faster with respect to the number of intermediate states. Despite
its definition from an adiabatic theory, we recommend to use the PS
matrix element also to compute the [non-adiabatic band-structure
renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)<sup>[\[1\]](#cite_note-engel:prb:2022-1)</sup>.
In our experience, the PS matrix element is furthermore well suited to
perform [transport
calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md),
since the difference between AE and PS matrix elements is small for
scattering processes close to the Fermi edge. In any case, it is always
recommended to compare observables computed with the PS matrix elements
against the same observables computed with the AE matrix elements.

## Available contributions\[<a
href="/wiki/index.php?title=ELPH_DECOMPOSE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Available contributions">edit</a> \| (./index.php.md)\]

V - Derivative of pseudopotential, $\tilde{v}$  
$g^{(\text{V})}_{m \mathbf{k}', n \mathbf{k}, a} \equiv \langle
\tilde{\psi}_{m \mathbf{k}'} | \frac{\partial \tilde{v}}{\partial
u_{a}} | \tilde{\psi}_{n \mathbf{k}} \rangle$

This term is the pure plane-wave contribution to the total PAW matrix
element. If the PAW augmentation region were vanishingly small, this
would be the sole contribution.

D - Derivative of PAW strength parameters, $D_{a, ij}$  
$g^{(\text{D})}_{m \mathbf{k}', n \mathbf{k}, a} \equiv \sum_{bij}
\langle \tilde{\psi}_{m \mathbf{k}'} | \tilde{p}_{b i} \rangle
\frac{\partial D_{b, ij}}{\partial u_{a}} \langle \tilde{p}_{b j} |
\tilde{\psi}_{n \mathbf{k}} \rangle$

This contribution stems from the PAW treatment of the electronic
Hamiltonian. It is of the same nature as $g^{(\text{V})}$ but is treated in the local basis inside the
augmentation region. For a detailed discussion of the PAW strength
parameters, we refer to Ref.
<sup>[\[4\]](#cite_note-kresse:prb:99-4)</sup>.

P - Derivative of PAW projectors, $|\tilde{p}_{ai}\rangle$  
$\begin{split} g^{(\text{P})}_{m \mathbf{k}', n \mathbf{k}, a} & \equiv
\sum_{ij} \langle \tilde{\psi}_{m \mathbf{k}'} | \frac{\partial
\tilde{p}_{a i}}{\partial u_{a}} \rangle ( D_{a, ij} -
\varepsilon_{n \mathbf{k}} Q_{a, ij} ) \langle \tilde{p}_{a j} |
\tilde{\psi}_{n \mathbf{k}} \rangle \\ & + \sum_{ij} \langle
\tilde{\psi}_{m \mathbf{k}'} | \tilde{p}_{a i} \rangle ( D_{a, ij} -
\varepsilon_{m \mathbf{k}'} Q_{a, ij} ) \langle \frac{\partial
\tilde{p}_{a j}}{\partial u_{a}} | \tilde{\psi}_{n \mathbf{k}}
\rangle \end{split}$

R - Derivative of PAW partial waves, $|\phi_{ai}\rangle$ and $|\tilde{\phi}_{ai}\rangle$  
$g^{(\text{R})}_{m \mathbf{k}', n \mathbf{k}, a} \equiv (\varepsilon_{n
\mathbf{k}} - \varepsilon_{m \mathbf{k}'}) \sum_{ij} \langle
\tilde{\psi}_{m \mathbf{k}'} | \tilde{p}_{a i} \rangle R_{a, ij}
\langle \tilde{p}_{a j} | \tilde{\psi}_{n \mathbf{k}} \rangle$

with $R_{a, ij} \equiv \langle
\phi_{a i} | \frac{\partial \phi_{a j}}{\partial u_{a}} \rangle -
\langle \tilde{\phi}_{a i} | \frac{\partial \tilde{\phi}_{a
j}}{\partial u_{a}} \rangle$

Q - Derivative of PAW projectors, $|\tilde{p}_{ai}\rangle$ (different eigenvalues)  
$\begin{split} g^{(\text{Q})}_{m \mathbf{k}', n \mathbf{k}, a} & \equiv
\sum_{ij} \langle \tilde{\psi}_{m \mathbf{k}'} | \frac{\partial
\tilde{p}_{a i}}{\partial u_{a}} \rangle ( D_{a, ij} -
\varepsilon_{n \mathbf{k}} Q_{a, ij} ) \langle \tilde{p}_{a j} |
\tilde{\psi}_{n \mathbf{k}} \rangle \\ & + \sum_{ij} \langle
\tilde{\psi}_{m \mathbf{k}'} | \tilde{p}_{a i} \rangle ( D_{a, ij} -
\varepsilon_{n \mathbf{k}} Q_{a, ij} ) \langle \frac{\partial
\tilde{p}_{a j}}{\partial u_{a}} | \tilde{\psi}_{n \mathbf{k}}
\rangle \end{split}$

This contribution is very similar to $g^{(\text{P})}$. The only difference is in the Kohn-Sham eigenvalues.
While $g^{(\text{P})}$ uses the eigenvalues of both the initial and final
state (so $\varepsilon_{n \mathbf{k}}$ and $\varepsilon_{m \mathbf{k}'}$), $g^{(\text{Q})}$ only uses the eigenvalues of the initial state
($\varepsilon_{n \mathbf{k}}$).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_DECOMPOSE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Projector-augmented-wave
  formalism](../methods/Projector-augmented-wave_formalism.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)
- [ELPH_DRIVER](ELPH_DRIVER.md)

## References\[<a
href="/wiki/index.php?title=ELPH_DECOMPOSE&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-engel:prb:2022_1-0)</sup>
    <sup>[b](#cite_ref-engel:prb:2022_1-1)</sup>
    <sup>[c](#cite_ref-engel:prb:2022_1-2)</sup>
    <sup>[d](#cite_ref-engel:prb:2022_1-3)</sup>
    <a href="https://link.aps.org/doi/10.1103/PhysRevB.106.094316"
    class="external text" rel="nofollow">M. Engel, H. Miranda, L. Chaput, A.
    Togo, C. Verdi, M. Marsman, and G. Kresse, <em>Zero-point
    renormalization of the band gap of semiconductors and insulators using
    the projector augmented wave method</em>, Phys. Rev. B
    <strong>106</strong>, 094316 (2022).</a>
2.  [↑](#cite_ref-chaput:prb:2019_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.100.174304"
    class="external text" rel="nofollow">L. Chaput, A. Togo, and I. Tanaka,
    <em>Finite-displacement computation of the electron-phonon interaction
    within the projector augmented-wave method</em>, Phys. Rev. B
    <strong>100</strong>, 174304 (2019).</a>
3.  [↑](#cite_ref-engel:prb:2020_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.101.184302"
    class="external text" rel="nofollow">M. Engel, M. Marsman, C. Franchini,
    and G. Kresse, <em>Electron-phonon interactions using the projector
    augmented-wave method and Wannier functions</em>, Phys. Rev. B
    <strong>101</strong>, 184302 (2020).</a>
4.  [↑](#cite_ref-kresse:prb:99_4-0)
    <a href="https://doi.org/10.1103/PhysRevB.59.1758" class="external text"
    rel="nofollow">I. G. Kresse and D. Joubert, Phys. Rev. B
    <strong>59</strong>, 1758 (1999).</a>



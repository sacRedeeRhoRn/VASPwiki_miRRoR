<!-- Source: https://vasp.at/wiki/index.php/Constrained%E2%80%93random-phase%E2%80%93approximation_formalism | revid: 37021 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Constrained–random-phase–approximation formalism


The **constrained random-phase approximation** (cRPA) is a method that
allows to calculate the effective interaction parameter U, J and J' for
model Hamiltonians. The main idea is to neglect screening effects of
specific **target states** in the screened Coulomb interaction W of the
<a href="/wiki/The_GW_approximation_of_Hedin%27s_equations"
class="mw-redirect"
title="The GW approximation of Hedin&#39;s equations">GW method</a>. The
resulting partially screened Coulomb interaction is often evaluated in a
localized basis that spans the target space and is described by the
model Hamiltonian. Usually, the target space is low-dimensional (up to 5
states) and therefore allows for the application of a higher level
theory, such as [dynamical mean-field
theory](../tutorials/DFT+DMFT_calculations.md) (DMFT).

This page introduces the theoretical foundations of cRPA. The [first
section](#Tight-binding_model_Hamiltonian) presents the tight-binding
model Hamiltonian and the
<a href="/wiki/Wannier_basis" class="mw-redirect"
title="Wannier basis">Wannier basis</a> used to represent the target
states. The [second
section](#Effective_Coulomb_kernel_in_constrained_random-phase_approximation)
describes four methods for computing the effective Coulomb kernel by
excluding screening contributions from the target space. The [final
section](#Off-center_interactions) covers off-center Coulomb integrals
for extended models.


## Contents


- [1 Tight-binding
  model Hamiltonian](#Tight-binding_model_Hamiltonian)
  - [1.1 Wannier
    basis and target space](#Wannier_basis_and_target_space)
  - [1.2 Definition
    of model parameters: Hopping and Coulomb
    repulsion](#Definition_of_model_parameters:_Hopping_and_Coulomb_repulsion)
- [2 Effective
  Coulomb kernel in constrained random-phase
  approximation](#Effective_Coulomb_kernel_in_constrained_random-phase_approximation)
  - [2.1 Band
    method](#Band_method)
  - [2.2
    Disentanglement-cRPA method
    (d-cRPA)](#Disentanglement-cRPA_method_(d-cRPA))
  - [2.3
    Weighted-cRPA method
    (w-cRPA)](#Weighted-cRPA_method_(w-cRPA))
  - [2.4
    Projector-cRPA method
    (p-cRPA)](#Projector-cRPA_method_(p-cRPA))
    - [2.4.1
      Caveats of
      p-cRPA](#Caveats_of_p-cRPA)
  - [2.5
    Spectral-cRPA method
    (s-cRPA)](#Spectral-cRPA_method_(s-cRPA))
- [3 Off-center
  interactions](#Off-center_interactions)
- [4 Additional
  resources](#Additional_resources)
  - [4.1
    Lectures](#Lectures)
- [5 Related tags
  and articles](#Related_tags_and_articles)
- [6
  References](#References)


## Tight-binding model Hamiltonian\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Tight-binding model Hamiltonian">edit</a> \| (./index.php.md)\]

A model Hamiltonian describes a small subset of electrons around the
chemical potential and has, in second quantization, the following form

$H
= \sum_\sigma \sum_{<ij>} t_{ij}^\sigma c_{i\sigma}^\dagger
c_{j\sigma} + \sum_{\sigma\sigma'} \sum_{<ijkl>}
U_{ijkl}^{\sigma\sigma'} c_{i\sigma}^\dagger c_{k\sigma'}^\dagger
c_{j\sigma} c_{l\sigma'}$

Here, $i,j,k,l$ are
site and $\sigma,\sigma'$ spin indices, respectively and the symbol
$<\cdots>$ indicates summation over nearest neighbors.
The hopping matrix elements $t_{ij}^\sigma$ describe the hopping of electrons (of same spin)
between site $i$ and
$j$, while the effective Coulomb matrix elements
$U_{ijkl}^{\sigma\sigma'}$ describe the interaction of
electrons between sites.

### Wannier basis and target space\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Wannier basis and target space">edit</a> \| (./index.php.md)\]

To use model Hamiltonians successfully a localized basis set is chosen.
In most applications this basis set consists of
<a href="/wiki/Wannier_states" class="mw-redirect"
title="Wannier states">Wannier states</a> that are connected with the
Bloch functions $\psi_{n\bf k}^\sigma ({\bf
r}) = e^{i{\bf k r}} u_{n\bf k}({r})$ of band
$n$ at k-point $\bf{k}$ with
spin $\sigma$ via

$|
w_{i\bf R}^\sigma \rangle = \frac{1}{N_k}\sum_{n\bf k} e^{-i {\bf k
R}} T_{i n}^{\sigma({\bf k})} | \psi_{n\bf k}^\sigma \rangle$

Usually, the target states and thus the appropriate basis set is
localized such that the interaction between periodic images can be
neglected. This allows to work with Wannier functions in the unit cell
at $\bf R=0$:

$|
w_{i}^\sigma \rangle = \frac{1}{N_k}\sum_{n\bf k} T_{i
n}^{\sigma({\bf k})} | \psi_{n\bf k}^\sigma \rangle$

|  |
|----|
| **Mind:** Here, $T$ instead of the widely used $U$ notation for the transformation matrix is used to avoid confusion with the Hubbard parameter. |

In practice, one builds a model Hamiltonian only for a small subset of
Bloch functions. These **target states** are typically centered around
the chemical potential (or Fermi energy see
[EFERMI](../incar-tags/EFERMI.md)) and are strongly localized around ions.
The model Hamiltonian can be solved successfully only if the target
states are well-represented by the
<a href="/wiki/Wannier_basis" class="mw-redirect"
title="Wannier basis">Wannier basis</a>.

|  |
|----|
| **Tip:** As an indicator of the quality of the Wannier representation, compare the [original band structure](../tutorials/Band-structure_calculation_using_density-functional_theory.md) with the Wannier interpolated one. |

In the following example considering SrVO3, the target space consists of
three Bloch bands (red bands) that may be represented well by three
Wannier states:

<figure class="mw-halign-center" typeof="mw:File">
<a href="/wiki/File:SrVO3_t2g_bands.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/8/8e/SrVO3_t2g_bands.png/250px-SrVO3_t2g_bands.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/8/8e/SrVO3_t2g_bands.png/375px-SrVO3_t2g_bands.png 1.5x, /wiki/images/thumb/8/8e/SrVO3_t2g_bands.png/500px-SrVO3_t2g_bands.png 2x"
width="250" height="233" /></a>
</figure>

The complete target space is spanned by a certain number of Bloch bands.
These bands can be selected with the
[NCRPA_BANDS](../incar-tags/NCRPA_BANDS.md) tag. Refer to the [full
SrVO3 cRPA calculation](../misc/CRPA_of_SrVO3.md) for more
details of the setup.

More often, however, one has delocalized states that mix with the target
space of the model. Without including these additional states in the
<a href="/wiki/Wannier_basis" class="mw-redirect"
title="Wannier basis">Wannier basis</a>, a good representation of the
band structure is not possible. Below is an example (face-centered-cubic
Ni), where the delocalized s-band (blue) crosses the five target
d-states (red):

<figure class="mw-halign-center" typeof="mw:File">
<a href="/wiki/File:Ni_d_s_bands.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/48/Ni_d_s_bands.png/250px-Ni_d_s_bands.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/48/Ni_d_s_bands.png/375px-Ni_d_s_bands.png 1.5x, /wiki/images/thumb/4/48/Ni_d_s_bands.png/500px-Ni_d_s_bands.png 2x"
width="250" height="230" /></a>
</figure>

Due to the hybridization of s and d electrons, the system requires at
least six <a href="/wiki/Wannier_states" class="mw-redirect"
title="Wannier states">Wannier states</a> to properly represent the
electronic structure of five target states. The selection of target
states in the <a href="/wiki/Wannier_basis" class="mw-redirect"
title="Wannier basis">Wannier basis</a> is done with the
[NTARGET_STATES](../incar-tags/NTARGET_STATES.md).

If a modification of the band structure is acceptable within an energy
window, these five target states might be **disentangled** from the
remaining ones, and one arrives at the following picture:

<figure class="mw-halign-center" typeof="mw:File">
<a href="/wiki/File:Ni_d_bands_decoupled.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/e/ec/Ni_d_bands_decoupled.png/250px-Ni_d_bands_decoupled.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/e/ec/Ni_d_bands_decoupled.png/375px-Ni_d_bands_decoupled.png 1.5x, /wiki/images/thumb/e/ec/Ni_d_bands_decoupled.png/500px-Ni_d_bands_decoupled.png 2x"
width="250" height="232" /></a>
</figure>

Here, the original Bloch bands (gray lines) are projected to five
non-crossing Wannier states.

In the following $\cal T$
denotes the **target space**, that is, the states described by the model
Hamiltonian.

### Definition of model parameters: Hopping and Coulomb repulsion\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Definition of model parameters: Hopping and Coulomb repulsion">edit</a> \| (./index.php.md)\]

The calculation of the hopping matrix $t$ depends on
the theory that is used to solve the effective model. For instance, in
[DFT+DMFT](../tutorials/DFT+DMFT_calculations.md) (often
termed LDA+DMFT) one calculates the hopping matrix from Kohn-Sham
energies, while in GW+DMFT [GW quasi-particle
energies](../methods/GW_approximation_of_Hedin's_equations.md)
are used. If $\epsilon^\sigma_{n\bf k}$ denotes these one-electron energies and
$\mu^\sigma$ is the corresponding Fermi energy, the
hopping matrix elements are calculated with following formula

$t_{ij}^\sigma = \frac{1}{N_k}\sum_{n\bf k}T_{in}^{\*\sigma({\bf k})}
(\epsilon^\sigma_{n{\bf k}} - \mu^\sigma) T_{jn}^{\sigma({\bf k})}$

Similarly, Coulomb matrix elements are evaluated from the Bloch
representation of the effective Coulomb kernel
$U_{{\bf G G}'}({\bf q})$ via

$U_{ijkl}^{\sigma\sigma'} = \frac{1}{N^3_k}\sum_{{\bf k k
q}}\sum_{n_1n_2n_3n_4} T_{in_1}^{\*\sigma({\bf k})}
T_{jn_2}^{\sigma({\bf k-q})} \langle u^\sigma_{n_1\bf k}| e^{-i({\bf
q + G})\cdot {\bf r}} |u^\sigma_{n_2\bf k-q}\rangle
U^{\sigma\sigma'}_{{\bf G G}'}({\bf q}) \langle u^{\sigma'}{n_3\bf
k'-q}| e^{i({\bf q - G'})\cdot {\bf r'} }|u^{\sigma'}{n_4\bf
k'}\rangle T_{kn_3}^{\*\sigma'({\bf k'-q})} T_{ln_4}^{\sigma'({\bf
k'})}$

|  |
|----|
| **Mind:** The effective Coulomb kernel is frequency-dependent and thus the effective interaction in the model as well. |

In most applications, however, one considers the static limit
$U=U(\omega\to 0)$.

In practice, one often simplifies the model Hamiltonian further and
works with the Hubbard-Kanamori
parameters:<sup>[\[1\]](#cite_note-vaugier:prb:86-1)</sup>

${\cal U }^{\sigma\sigma'} = \frac 1 N \sum_{i\in \cal T}
U_{iiii}^{\sigma\sigma'}$

${\cal U' }^{\sigma\sigma'} = \frac{1}{N(N-1)}\sum_{i,j \in{\cal T},
i\neq j}^N U_{ijji}^{\sigma\sigma'}$

${\cal J }^{\sigma\sigma'} = \frac{1}{N(N-1)} \sum_{i,j \in{\cal T},
i\neq j}^N U_{ijij}^{\sigma\sigma'}$

Here, $N$ specifies
the number of <a href="/wiki/Wannier_functions" class="mw-redirect"
title="Wannier functions">Wannier functions</a> in the target space
$\cal T$.

## Effective Coulomb kernel in constrained random-phase approximation\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Effective Coulomb kernel in constrained random-phase approximation">edit</a> \| (./index.php.md)\]

In analogy to the [screened Coulomb kernel in
GW](../methods/GW_approximation_of_Hedin's_equations.md),
the effective Coulomb kernel is calculated as

$U^{\sigma\sigma'}\*{{\bf G}{\bf G}'}({\bf
q},i\omega)=\left\[\delta\*{{\bf G}{\bf
G}'}-(\chi^{\sigma\sigma'}\*{{\bf G}{\bf G}'}({\bf q},i\omega) -
\tilde\chi^{\sigma\sigma'}\*{{\bf G}{\bf G}'}({\bf q},i\omega) ) \cdot
V_{{\bf G}{\bf G}'}({\bf q})\right\]^{-1}V_{{\bf G}{\bf G}'}({\bf q})$

In contrast to the
<a href="/wiki/GW_method" class="mw-redirect" title="GW method">GW
method</a>, however, the polarizability contains all RPA-screening
effects except those from the target space. These effects are described
by the correlated polarizability $\tilde \chi$.

In the following four cRPA methods are presented for the calculation of
$\tilde \chi$. Note, all methods below reduce to the
**band method** if the target space forms an isolated set of bands.

### Band method\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Band method">edit</a> \| (./index.php.md)\]

The simplest way to define the target polarizability is to use the
expression of Adler and
Wiser<sup>[\[2\]](#cite_note-adler:1962-2)[\[3\]](#cite_note-wiser:1963-3)[\[4\]](#cite_note-aryasetiawan:prb70-4)</sup>

$\tilde \chi^\sigma_{{\bf G,G}'}({\bf q},i\omega)= \frac
1{N_k}\sum_{\bf k}\sum_{nn'\in{\cal T}} \frac{ f_{n\bf k}-f_{n'\bf
k-q} }{ \epsilon_{n{\bf k}} - \epsilon_{n'\bf k-q} - i \omega }
\langle u_{n {\bf k }}^{\sigma } |e^{-i \bf (G+q) r}| u_{n'{\bf
k-q}}^{ \sigma' } \rangle \langle u_{n' {\bf k-q}}^{\sigma' } |e^{-i
\bf (G'-q)r'} | u_{n{\bf k }}^{ \sigma } \rangle$

This approach is most accurate for an isolated target space
$\cal T$ as depicted in the first example above.

|  |
|----|
| **Mind:** Target bands can be selected with [NCRPA_BANDS](../incar-tags/NCRPA_BANDS.md). |

|  |
|----|
| **Warning:** This method is not recommended for systems with entangled target states. |

### Disentanglement-cRPA method (d-cRPA)\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Disentanglement-cRPA method (d-cRPA)">edit</a> \| (./index.php.md)")\]

Miyake, Aryasetiawan, and
Imada<sup>[\[5\]](#cite_note-miyake:prb:80-5)</sup>
propose to disentangle the target space from the full space by
diagonalizing the Hamiltonian in both spaces independently. This yields
a disentangled band structure similar to the one shown in the third
example above. The corresponding target polarizability reduces to a
constrained Adler and Wiser
expression<sup>[\[2\]](#cite_note-adler:1962-2)[\[3\]](#cite_note-wiser:1963-3)</sup>

$\tilde \chi^\sigma_{{\bf G,G}'}({\bf q},i\omega)= \frac
1{N_k}\sum_{\bf k}\sum_{nn'\in{\cal T}} \frac{ f_{n\bf k}-f_{n'\bf
k-q} }{ \tilde\epsilon_{n{\bf k}} - \tilde\epsilon_{n'\bf k-q} - i
\omega } \langle \tilde u_{n {\bf k }}^{\sigma } |e^{-i \bf (G+q) r}|
\tilde u_{n'{\bf k-q}}^{ \sigma' } \rangle \langle \tilde u_{n' {\bf
k-q}}^{\sigma' } |e^{-i \bf (G'-q)r'} | \tilde u_{n{\bf k }}^{ \sigma
} \rangle$,

where $\tilde \epsilon_{n\bf
k}^\sigma$ is the disentangled band structure. The
resulting Hubbard-Kanamori interactions depend on the chosen energy
window of the Wannier functions.

|  |
|----|
| **Mind:** Typically, this method yields the largest Hubbard-Kanamori interactions and is selected with [LDISENTANGLED](../incar-tags/LDISENTANGLED.md) tag. |

### Weighted-cRPA method (w-cRPA)\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Weighted-cRPA method (w-cRPA)">edit</a> \| (./index.php.md)")\]

Sasioglu, Friedrich and Blügel propose an alternative
approach.<sup>[\[6\]](#cite_note-sasioglu:prb:83-6)</sup>
They calculate the screening effects within the target space as follows:

$\tilde \chi^\sigma_{{\bf G,G}'}({\bf q},i\omega)= \frac
1{N_k}\sum_{nn'{\bf k}} \frac{ f_{n\bf k}-f_{n'\bf k-q} }{
\epsilon_{n{\bf k}} - \epsilon_{n'\bf k-q} - i \omega } p_{n\bf k
}^{\sigma} p_{n'\bf k-p }^{\sigma'} \langle u_{n {\bf k }}^{\sigma }
|e^{-i \bf (G+q) r}| u_{n'{\bf k-q}}^{ \sigma' } \rangle \langle
u_{n' {\bf k-q}}^{\sigma' } |e^{-i \bf (G'-q)r'} | u_{n'{\bf k }}^{
\sigma } \rangle$

Here, the weighting factors

$p_{n\bf k}^\sigma = \sum_{i\in\cal T} |T_{i n}^{\sigma({\bf k})}|^2
, \quad 0 \le p_{n\bf k}^\sigma \le 1$

measure the probability for $|\psi_{n\bf k}^\sigma\rangle$ being in the target space. This method does not alter
the band structure, however, neglects screening effects within the
target space as shown in next section. Typically, the weighted-cRPA
method yields the smallest Hubbard-Kanamori interactions.

|  |
|----|
| **Mind:** This method is selected with the [LWEIGHTED](../incar-tags/LWEIGHTED.md) tag. |

### Projector-cRPA method (p-cRPA)\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Projector-cRPA method (p-cRPA)">edit</a> \| (./index.php.md)")\]

A consistent expression for the target polarizability gives rise to the
projector-cRPA (p-cRPA) method. The main goal is to subdivide the target
from the full Fock space in a Wannier
basis.<sup>[\[7\]](#cite_note-kaltak:prb:2025:2-7)</sup>
To this end, we work with the target projectors

$P_{mn}^{\sigma({\bf k})} = \sum_{i\in \cal T} T_{i m}^{\*\sigma({\bf
k})} T_{i n}^{\sigma({\bf k})}$

that filter out target space contributions to each Bloch state. Using
these projectors, the target polarizability for the projector method
reads<sup>[\[8\]](#cite_note-kaltak:thesis2015-8)</sup>

$\tilde \chi^\sigma_{{\bf G,G}'}({\bf q},i\omega)= \frac
1{N_k}\sum_{nn'{\bf k}} \frac{ f_{n\bf k}-f_{n'\bf k-q} }{
\epsilon_{n{\bf k}} - \epsilon_{n'\bf k-q} - i \omega } \sum_{m_1m_2'
} P_{m_1 n }^{\*\sigma ({\bf k })} \langle u_{m_1 {\bf k }}^{\sigma }
|e^{-i \bf (G+q) r}| u_{m_2'{\bf k-q}}^{ \sigma' } \rangle P_{m_2'
n'}^{ \sigma' ({\bf k-q})} \sum_{m_1'm_2 } P_{m_2 n'}^{\*\sigma' ({\bf
k-q})} \langle u_{m_2 {\bf k-q}}^{\sigma' } |e^{-i \bf (G'-q)r'} |
u_{m_1'{\bf k }}^{ \sigma } \rangle P_{m_1' n }^{ \sigma ({\bf k })}$

The projector method usually results in larger (smaller)
Hubbard-Kanamori interactions than the weighted-cRPA
(disentanglement-cRPA) method.

|  |
|----|
| **Mind:** The projector method is the default cRPA. |

#### Caveats of p-cRPA\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Caveats of p-cRPA">edit</a> \| (./index.php.md)\]

The p-cRPA method employs a regularization of the projectors. This
regularization is not conserving the number of
electrons.<sup>[\[9\]](#cite_note-kaltak:prb:2025-9)</sup>
As a consequence, the long-wave limit calculated from k-p perturbation
theory can become negative and deteriorate **k**-point convergence
drastically. For such cases, the [WAVEDER](../input-files/WAVEDER.md) file
should be deleted before the cRPA step. Other cRPA methods do not suffer
from this problem and the usage of the long-wave limit is strongly
encouraged.

### Spectral-cRPA method (s-cRPA)\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Spectral-cRPA method (s-cRPA)">edit</a> \| (./index.php.md)")\]

The spectral-cRPA method (s-cRPA) is a robust approach that remedies the
main drawbacks of both w-cRPA and
p-cRPA.<sup>[\[9\]](#cite_note-kaltak:prb:2025-9)</sup>
This method uses the eigenspectrum of the original projectors

$P_{nm}^{({\bf k})} \approx \Theta_{n}^{({\bf k})}\delta_{nm}$

where the eigenvalues $\Theta_{n}^{({\bf k})}$ are ordered by the leverage score. The leverage score
measures how strongly each Bloch state contributes to the Wannier
orbitals in the target space. At each **k**-point, it selects exactly
$N$ target states (typically $N=5$ for
d-electrons). Bloch states with the strongest contribution from Wannier
orbitals are included in the calculation of the correlated
polarizability $\tilde\chi$,
while states with the weakest contribution are neglected and allowed to
screen the effective interaction.

The key advantages of s-cRPA are:

- **Positive interactions**: The electron number is always conserved (in
  contrast to p-cRPA)
- **Largest interaction values**: removes most intra-d screening effects
  (in contrast to w-cRPA)

|  |
|----|
| **Mind:** Select the s-cRPA method with [LSCRPA](../incar-tags/LSCRPA.md). |

|  |
|----|
| **Tip:** Recommended for all cRPA calculations as of VASP version 6.6.0 |

## Off-center interactions\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Off-center interactions">edit</a> \| (./index.php.md)\]

Off-center Coulomb integrals can be evaluated using
[`ALGO`](../incar-tags/ALGO.md)` = 2e4wa` or by adding
[`LTWO_CENTRE`](../incar-tags/LTWO_CENTRE.md)` = T`.

When chosen, the system calculates two types of integrals:

- Bare integrals (stored in the [VRijkl](../output-files/VRijkl.md) file)

$V_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf r}\int {\rm d}{\bf r}'
\frac{w_{i}^{\*\sigma}({\bf r}) w_{j}^{\sigma}({\bf r})
w_{k}^{\*\sigma'}({\bf r}'+{\bf R}) w_{l}^{\sigma'}({\bf r}'+{\bf
R})}{|{\bf r}-{\bf r}'|}$

- Effectively screened integrals (stored in the
  [URijkl](../output-files/URijkl.md) file)

$U_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf r}\int {\rm d}{\bf r}'
w_{i}^{\*\sigma}({\bf r}) w_{j}^{\sigma}({\bf r}) U({\bf r},{\bf
r}',\omega) w_{k}^{\*\sigma'}({\bf r}'+{\bf R}) w_{l}^{\sigma'}({\bf
r}'+{\bf R})$

The extent of displacement vectors ${\bf R}$ is
automatically determined based on the selected **k**-point grid.

The calculation of these integrals occurs as a post-processing step. For
bare, off-center Coulomb integrals ([VRijkl](../output-files/VRijkl.md)), a
valid [WAVECAR](../input-files/WAVECAR.md) file must be present in the
working directory. For effectively screened Coulomb integrals
([URijkl](../output-files/URijkl.md)), both a valid
[WAVECAR](../input-files/WAVECAR.md) file and
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) files are required.
The [WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) files are
automatically generated following a successful
[`ALGO`](../incar-tags/ALGO.md)` = CRPA` job.

The basis orbitals can be selected with
[LOCALIZED_BASIS](LOCALIZED_BASIS.md).

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

## Additional resources\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Lectures\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- <a href="https://youtu.be/6F_WNIh6V7I" class="external text"
  rel="nofollow">Optical gap and the constrained random-phase
  approximation</a>

## Related tags and articles\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ALGO](../incar-tags/ALGO.md),
[NTARGET_STATES](../incar-tags/NTARGET_STATES.md),
[NCRPA_BANDS](../incar-tags/NCRPA_BANDS.md),
[LOCALIZED_BASIS](LOCALIZED_BASIS.md),
[LDISENTANGLED](../incar-tags/LDISENTANGLED.md),
[LWEIGHTED](../incar-tags/LWEIGHTED.md),
[NUM_WANN](../incar-tags/NUM_WANN.md),
[WANNIER90_WIN](../incar-tags/WANNIER90_WIN.md),
[ENCUTGW](../incar-tags/ENCUTGW.md), [VCUTOFF](../incar-tags/VCUTOFF.md),
[VIJKL](../output-files/VIJKL.md), [UIJKL](../output-files/UIJKL.md),
[URijkl](../output-files/URijkl.md), [VRijkl](../output-files/VRijkl.md),
[LTWO_CENTRE](../incar-tags/LTWO_CENTRE.md),
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md)

[cRPA of SrVO3](../misc/CRPA_of_SrVO3.md), [Bandstructure and
CRPA of
SrVO3](../misc/Bandstructure_and_CRPA_of_SrVO3.md)

## References\[<a
href="/wiki/index.php?title=Constrained%E2%80%93random-phase%E2%80%93approximation_formalism&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-vaugier:prb:86_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.86.165105"
    class="external text" rel="nofollow">L. Vaugier, H. Jiang, and S.
    Biermann, Phys. Rev. B <strong>86</strong>, 165105 (2012).</a>
2.  ↑
    <sup>[a](#cite_ref-adler:1962_2-0)</sup>
    <sup>[b](#cite_ref-adler:1962_2-1)</sup>
    <a href="https://doi.org/10.1103/PhysRev.126.413" class="external text"
    rel="nofollow">S. L. Adler, Phys. Rev. <strong>126</strong>, 413
    (1962)</a>
3.  ↑
    <sup>[a](#cite_ref-wiser:1963_3-0)</sup>
    <sup>[b](#cite_ref-wiser:1963_3-1)</sup>
    <a href="https://doi.org/10.1103/PhysRev.129.62" class="external text"
    rel="nofollow">N. Wiser, Phys. Rev. <strong>129</strong>, 62 (1963)</a>
4.  [↑](#cite_ref-aryasetiawan:prb70_4-0)
    <a href="https://doi.org/10.1103/PhysRevB.70.195104"
    class="external text" rel="nofollow">F. Aryasetiawan, M. Imada, A.
    Georges, G. Kotliar, S. Biermann, and A. I. Lichtenstein, Phys. Rev. B
    <strong>70</strong>, 195104 (2004).</a>
5.  [↑](#cite_ref-miyake:prb:80_5-0)
    <a href="https://doi.org/10.1103/PhysRevB.80.155134"
    class="external text" rel="nofollow">T. Miyake, F. Aryasetiawan, and M.
    Imada, Phys. Rev. B <strong>80</strong>, 155134 (2009).</a>
6.  [↑](#cite_ref-sasioglu:prb:83_6-0)
    <a href="https://doi.org/10.1103/PhysRevB.83.121101"
    class="external text" rel="nofollow">E. Sasioglu, C. Friedrich, and S.
    Blügel, Phys. Rev. B <strong>83</strong>, 121101 (2011).</a>
7.  [↑](#cite_ref-kaltak:prb:2025:2_7-0)
    <a href="https://doi.org/10.1103/PhysRevB.111.195144"
    class="external text" rel="nofollow">M. Kaltak, I. R. Reddy and B. Kim,
    Phys. Rev. B <strong>111</strong>, 195144 (2025).</a>
8.  [↑](#cite_ref-kaltak:thesis2015_8-0)
    <a href="https://utheses.univie.ac.at/detail/33771#"
    class="external text" rel="nofollow">M. Kaltak, Thesis: Merging GW with
    DMFT (2015).</a>
9.  ↑
    <sup>[a](#cite_ref-kaltak:prb:2025_9-0)</sup>
    <sup>[b](#cite_ref-kaltak:prb:2025_9-1)</sup>
    <a href="https://doi.org/10.1103/m3gh-g6r6" class="external text"
    rel="nofollow">M. Kaltak, A. Hampel, M. Schlipf, I. R. Reddy, B. Kim and
    G. Kresse, Phys. Rev. B <strong>112</strong>, 245102 (2025).</a>



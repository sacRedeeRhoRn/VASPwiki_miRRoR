<!-- Source: https://vasp.at/wiki/index.php/Category:Electron-phonon_interactions | revid: 34101 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Electron-phonon interactions


In many systems, it suffices to treat the
<a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic</a> and
<a href="/wiki/Phonons" class="mw-redirect" title="Phonons">vibrational
degrees of freedom</a> (phonons) separately, because electrons are much
faster than the motion of nuclei. This treatment is approximate and can
be corrected by including **electron-phonon coupling**. This entails the
coupling of the two systems while still treating the two systems
separately. In fact, electron-phonon scattering is the prevalent effect
in a wide range of applications, such as the mobility of semiconductors
or the conductivity of metals at room temperature.

The inclusion of the effects of the ionic degrees of freedom in the
electronic structure is important in the determination of many physical
observables such as the
[bandgap](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md),
spectral functions, [electronic
conductivity](Category-Dielectric_properties.md),
Seebeck coefficient or electronic thermal conductivity, to name a few.


## Contents


- [1 Stochastic
  displacements approach](#stochastic-displacements-approach)
- [2 Many-body
  perturbation theory](#many-body-perturbation-theory)
  - [2.1
    Electron-phonon potential from
    supercells](#electron-phonon-potential-from-supercells)
  - [2.2 Physical
    observables (or electron-phonon matrix
    elements)](#physical-observables-or-electron-phonon-matrix-elements))
- [3 Choosing the
  right approach](#choosing-the-right-approach)
- [4 Additional
  resources](#additional-resources)
  - [4.1
    Tutorials](#tutorials)
- [5
  References](#references)


## Stochastic displacements approach\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Stochastic displacements approach">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Monte_carlo_on-shot.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/6/65/Monte_carlo_on-shot.png/400px-Monte_carlo_on-shot.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/6/65/Monte_carlo_on-shot.png/600px-Monte_carlo_on-shot.png 1.5x, /wiki/images/thumb/6/65/Monte_carlo_on-shot.png/800px-Monte_carlo_on-shot.png 2x"
width="400" height="251" /></a>
<figcaption>The equilbrium structure is split into a series of Monte
Carlo (MC) structures to model the electron-phonon interactions. The
one-shot method approximates the full MC approach using a single
supercell.</figcaption>
</figure>

The stochastic approach allows obtaining the bandgap renormalization and
an approximation of the electronic spectral function due to the ionic
degrees of freedom under the static approximation using a supercell
approach. This has the advantage that it can be easily implemented and
used with different levels of theory to describe the electronic states,
such as different
<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">exchange-correlation
functionals</a> or even the [GW
approximation](../theory/Category-GW.md). The disadvantage is
that the approach does not include time-dependent or dynamical effects
of the phonons (static approximation) and, hence, it does not provide
transport properties (see <a href="#Many-body_perturbation_theory"
class="mw-selflink-fragment">perturbation theory</a>).

To displace the atoms along a set of random or a single specially chosen
direction
<sup>[\[1\]](#cite_note-zacharias:prb:2016-1)</sup>,
this approach requires the knowledge of the
<a href="/wiki/Phonons" class="mw-redirect" title="Phonons">phonons</a>
on a supercell. The displacement length is determined by the temperature
of the ionic system. The desired can be directly obtained by averaging
over the set of randomly displaced supercells, or from the
aforementioned special displacement pattern.

The theory of [electron-phonon interactions from statistical
sampling](../theory/Electron-phonon_interactions_theory.md)
is covered elsewhere, as is [a how
to](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md).


## Many-body perturbation theory\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Many-body perturbation theory">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:FM_DW_diagrams.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/43/FM_DW_diagrams.png/400px-FM_DW_diagrams.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/43/FM_DW_diagrams.png/600px-FM_DW_diagrams.png 1.5x, /wiki/images/thumb/4/43/FM_DW_diagrams.png/800px-FM_DW_diagrams.png 2x"
width="400" height="220" /></a>
<figcaption>In many-body perturbation theory, the two lowest order
contributions to the <a
href="/wiki/Electron-phonon_interactions_theory#Electron_self-energy"
title="Electron-phonon interactions theory">electron self-energy</a> are
the <a href="/wiki/ELPH_SELFEN_FAN"
title="ELPH SELFEN FAN">Fan-Migdal</a> and <a
href="/wiki/ELPH_SELFEN_DW" title="ELPH SELFEN DW">Debye-Waller</a>
contributions in the Feynman diagram representation.</figcaption>
</figure>

Another approach to include **electron-phonon coupling** employs the
methods and language of many-body perturbation theory, where the
coupling is included as a [perturbation of the electronic or phononic
states](../theory/Electron-phonon_interactions_theory.md).
In the case of the perturbation of the electronic states, we can access
the [bandgap
renormalization](../theory/Electron-phonon_interactions_theory.md)
as well as [electronic transport
coefficients](../theory/Electronic_transport_coefficients.md)
with the inclusion of phonon scattering.

|  |
|----|
| **Important:** Electron-phonon interactions from perturbation theory require VASP to be compiled with [HDF5 support](Category-HDF5_support.md). |

This approach entails computing the [*electron-phonon matrix
element*](../theory/Electronic_transport_coefficients.md)
and the [phonon-induced electron
self-energy](../theory/Electron-phonon_interactions_theory.md).
Within the framework of density-functional theory, this requires the
knowledge of the change of Kohn-Sham potential with an ionic
perturbation as well as the initial and final electronic Kohn-Sham
states. The electron-phonon potential must be generated from a supercell
calculation, which is then used to calculate the phonon-induced electron
self-energy and, thereby, the physical observables.

### [Electron-phonon potential from supercells](../tutorials/Electron-phonon_potential_from_supercells.md)\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Electron-phonon potential from supercells">edit</a> \| (./index.php.md)\]

We obtain the derivatives of the Kohn-Sham potential with respect to the
ionic displacements

$\partial_{I \alpha} V (\mathbf{r}) = \frac{\partial V(r)}{\partial
R_{I\alpha}}$

with $I$ the ion
index and $\alpha$
denoting the Cartesian direction in which it is displaced. The main
output file is
[phelel_params.hdf5](../input-files/Phelel_params.hdf5.md),
which is required for computing the matrix elements in the next step.

- How to compute the [electron-phonon potential from
  supercells](../tutorials/Electron-phonon_potential_from_supercells.md)

### Physical observables (or electron-phonon matrix elements)\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Physical observables (or electron-phonon matrix elements)">edit</a> \| (./index.php.md)")\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Elphon-workflow.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/44/Elphon-workflow.png/400px-Elphon-workflow.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/44/Elphon-workflow.png/600px-Elphon-workflow.png 1.5x, /wiki/images/thumb/4/44/Elphon-workflow.png/800px-Elphon-workflow.png 2x"
width="400" height="192" /></a>
<figcaption>General workflow when running electron-phonon calculations
using perturbation theory.</figcaption>
</figure>

These physical observables include the [zero-point renormalization
(ZPR)](../theory/Electron-phonon_interactions_theory.md),
and transport coefficients such as the [electrical
conductivity](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md),
[carrier
mobility](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md),
and [thermopower and the ZT figure of
merit](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).
These [electronic transport
coefficients](../theory/Electronic_transport_coefficients.md)
are derived from the electron-phonon matrix elements via the scattering
lifetimes according to an approximation defined by
[ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md),
and Onsager coefficients, which depend on the [chemical
potential](../theory/Chemical_potential_in_electron-phonon_interactions.md).

To compute the physical observables, the phonon-induced electron
self-energy is computed in the primitive cell. The main tag that
provides convenient defaults depending on the observable of interest is
[ELPH_MODE](../incar-tags/ELPH_MODE.md). The computation of the
self-energy requires evaluating the electron-phonon matrix elements

$g_{mn \mathbf{k}, \nu \mathbf{q}} \equiv \langle \psi_{m \mathbf{k} -
\mathbf{q}} | \partial_{\nu \mathbf{q}} V | \psi_{n \mathbf{k}}
\rangle.$

By default, we avoid writing the matrix elements, because it is a huge
data set which is distributed for optimal use of the computational
resources.

For details on the setup and practical advice, we recommend reading

- [Bandgap renormalization due to electron-phonon
  coupling](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport coefficients including electron-phonon
  scattering](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- See the [ELPH_DRIVER](../incar-tags/ELPH_DRIVER.md) tag to obtain
  the electron-phonon matrix elements for further post-processing

The standard output of the electron-phonon code is organized using
so-called [electron-phonon
accumulators](../misc/Electron-phonon_accumulators.md).
This increases the efficiency of the code by reusing the computed
electron-phonon matrix elements. For details on how to interpret the
output, consult the
[output](../misc/Electron-phonon_accumulators.md)
section on the
[accumulators](../misc/Electron-phonon_accumulators.md)
page.

## Choosing the right approach\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Choosing the right approach">edit</a> \| (./index.php.md)\]

Both the <a href="#Stochastic_displacements_approach"
class="mw-selflink-fragment">stochastic approach</a> (SA) as well as the
<a href="#Many-body_perturbation_theory"
class="mw-selflink-fragment">perturbative approach</a> (PA) have
advantages and limitations. Depending on the application, there is often
one approach that is much more suitable than the other. This section is
dedicated to highlighting the differences and respective advantages
between SA and PA so that choosing the correct approach becomes easier.

Likely the biggest deciding factor between SA and PA are the observables
that can be calculated:

- To compute [transport coefficients including electron-phonon
  scattering](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md),
  the PA is the only possible choice. Transport calculations need to
  include time-dependent, i.e. dynamical, effects of the phonons. These
  effectively yield electronic quasiparticle lifetimes that influence
  properties such as the electronic conductivity
  $\sigma$, the Seebeck coefficient
  $S$ and the electronic contribution to the thermal
  conductivity $\kappa_e$.

<!-- -->

- The SA can calculate the renormalization of the fundamental bandgap of
  semiconductors and insulators, but not for metallic systems.
  Additionally it is difficult to infer the renormalization of the band
  structure at arbitrary k points in the primitive unit cell, as one
  would need a map of the states in the displaced supercell to the
  primitive cell that is not readily available and stated are heavily
  entangles. In comparison, the PA employs [many-body perturbation
  theory to calculate entire band-structure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md),
  not just for gaped systems but also for metallic systems.

In materials that are strongly anharmonic, such as very soft materials
with weakly bound atoms, the SA has a clear edge over PA. This is
because the PA is limited by the harmonic approximation of phonons and
only considers terms in the electron-phonon interaction up to second
order in the atomic displacements. On the other hand, the SA computes
the electron-phonon interaction implicitly during the [electronic
minimization
procedure](Category-Electronic_minimization.md)
in the displaced geometry and is hence not limited to the harmonic
approximation of phonons.

Furthermore, the SA can directly utilize higher-level
<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">exchange-correlation
functionals</a> such as [METAGGA](../incar-tags/METAGGA.md), [hybrid
functionals](../methods/Category-Hybrid_functionals.md)
and [beyond-DFT
methods](Category-Many-body_perturbation_theory.md)
such as the [GW approximation](../theory/Category-GW.md). While
it is in principle possible to integrate these features also into the
PA, this is currently not supported. Therefore, when the quasiparticle
shifts due to electron-electron interactions become important, it is
possible to use the PA method in combination with the [GW
approximation](../theory/Category-GW.md)
<sup>[\[2\]](#cite_note-karsai:njp:2018-2)</sup>.

Another key difference is how PA and SA handle polar materials: In polar
materials, longitudinal optical phonons can induce [long-range
electrostatic
fields](../theory/Phonons-_Theory.md) "Phonons: Theory")
(Fröhlich interaction) that are difficult to capture in even very large
supercells. The PA can deal with this via a [special treatment of the
dipole
interaction](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
that explicitly accounts for the missing long-range character in finite
supercells. The SA, however, has no such correction scheme, which can be
detrimental for strongly polar materials. In this case, one can only try
to keep increasing the supercell size in hopes of arriving at a
physically meaningful result.

## Additional resources\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Tutorials\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorials for
  <a href="https://www.vasp.at/tutorials/latest/electron-phonon/part1/"
  class="external text" rel="nofollow">bandgap renormalization from
  perturbation theory</a>.
- Tutorials for
  <a href="https://www.vasp.at/tutorials/latest/electron-phonon/part2/"
  class="external text" rel="nofollow">bandgap renormalization from
  stochastic displacements</a>.
- Tutorials for
  <a href="https://www.vasp.at/tutorials/latest/electron-phonon/part3/"
  class="external text" rel="nofollow">plotting the electron-phonon matrix
  elements and using VASP+phelel</a>.
- Tutorials for
  <a href="https://www.vasp.at/tutorials/latest/electron-phonon/part4/"
  class="external text" rel="nofollow">transport properties:
  conductivity</a>.

**NB** There was a [known
issue](../misc/Known_issues.md) for
electron-phonon calculations using [`ISPIN`](../incar-tags/ISPIN.md)` = 2`
for VASP 6.5.0 and 6.5.1 that was fixed in VASP 6.6.0 (see
<a href="https://vasp.at/forum/viewtopic.php?t=20541#p33020"
class="external text" rel="nofollow">this forum post</a>), which is
relevant for Fe bulk in this tutorial.

- Tutorials for
  <a href="https://www.vasp.at/tutorials/latest/electron-phonon/part5/"
  class="external text" rel="nofollow">transport properties: mobility and
  ZT figure of merit</a>.

## References\[<a
href="/wiki/index.php?title=Category:Electron-phonon_interactions&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-zacharias:prb:2016_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.94.075125"
    class="external text" rel="nofollow">M. Zacharias and F. Giustino, Phys.
    Rev. B <strong>94</strong>, 075125 (2016).</a>
2.  [↑](#cite_ref-karsai:njp:2018_2-0)
    <a href="https://doi.org/10.1088/1367-2630/aaf53f" class="external text"
    rel="nofollow">F. Karsai, M. Engel, E. Flage-Larssen, and G. Kresse, New
    J. of Phys. <strong>20</strong>, 123008 (2018).</a>



<!-- Source: https://vasp.at/wiki/index.php/Chemical_potential_in_electron-phonon_interactions | revid: 33049 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Chemical potential in electron-phonon interactions


The <a href="https://en.wikipedia.org/wiki/Chemical_potential"
class="external text" rel="nofollow">chemical potential</a>
$\mu$ (make sure not to mistake the chemical potential
$\mu$ for the mobility $\mu_e$ or
$\mu_h$) is the energy that can be released that due to
a change in particle number. Its accurate determination is a key
ingredient in the computation of [electronic transport
coefficients](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
such as electrical conductivity, carrier mobility, and thermopower.
These quantities depend sensitively on the occupation of electronic
states near the Fermi level, since only states within a few
*k<sub>B</sub>T* of the Fermi energy contribute significantly to
transport. We employ the frozen-band approximation, which assumes that
the electronic potential and eigenvalues computed for the undoped system
remain unchanged when electrons are added or removed.

Because the occupation of states is governed by the Fermi–Dirac
distribution, an accurate evaluation of the chemical potential as a
function of temperature and doping is essential. Even small inaccuracies
in $\mu$ can lead to large errors in transport properties.


## Contents


- [1
  Definition](#definition)
- [2 Carrier
  density and doping](#carrier-density-and-doping)
- [3 Why the
  chemical potential
  matters](#why-the-chemical-potential-matters)
- [4 Different ways
  to specify carriers](#different-ways-to-specify-carriers)
- [5 Related tags
  and articles](#related-tags-and-articles)


## Definition\[<a
href="/wiki/index.php?title=Chemical_potential_in_electron-phonon_interactions&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Definition">edit</a> \| (./index.php.md)\]

At finite temperature, the chemical potential
$\mu$ is defined by requiring that the total number of
electrons *N<sub>e</sub>* equals the number of occupied states:

$N_e = \frac{1}{N_\mathbf{k}} \sum_{n\mathbf{k}}
f(\varepsilon_{n\mathbf{k}}, T, \mu)$

where:

$N_\mathbf{k}$ is the total number of k-points used to
sample the Brillouin zone,

$\varepsilon_{n\mathbf{k}}$ are the electronic
eigenvalues,

$f(\varepsilon, T, \mu) = \frac{1}{e^{\frac{\varepsilon -
\mu}{k_\mathrm{B} T}} + 1}$ is the Fermi–Dirac
occupation function

This equation implicitly defines $\mu(T)$ for a
given total number of electrons $N_e$.

## Carrier density and doping\[<a
href="/wiki/index.php?title=Chemical_potential_in_electron-phonon_interactions&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Carrier density and doping">edit</a> \| (./index.php.md)\]

In doped or non-stoichiometric systems, the total number of electrons
includes additional carriers introduced by doping. The number of
carriers per unit cell (or per simulation cell) is given by:

$N_\text{carriers} = \frac{1}{N_\mathbf{k}} \sum_{n\mathbf{k}} \left\[
f(\varepsilon_{n\mathbf{k}}, T, \mu) - f(\varepsilon_{n\mathbf{k}}, 0,
\epsilon_F) \right\]$

where $\epsilon_F$
is fermi energy of the neutral (undoped) system. Positive
*N<sub>carriers</sub>* corresponds to n-type doping (extra electrons),
while negative *N<sub>carriers</sub>* corresponds to p-type doping
(holes).

The carrier concentration (number of carriers per unit volume) is then:

$n_e = \frac{N_\text{carriers}}{\Omega} = \frac{1}{N_\mathbf{k}\Omega}
\sum_{n\mathbf{k}} \left\[ f(\varepsilon_{n\mathbf{k}}, T, \mu) -
f(\varepsilon_{n\mathbf{k}}, 0, \epsilon_F) \right\]$

where $\Omega$ is
the volume of the cell.

If the target carrier concentration *n<sub>e</sub>* is known, the
chemical potential $\mu$ can be
determined by numerically inverting this equation. This relation links
the chemical potential directly to the carrier density at a given
temperature, serving as the foundation for transport coefficient
calculations.

## Why the chemical potential matters\[<a
href="/wiki/index.php?title=Chemical_potential_in_electron-phonon_interactions&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Why the chemical potential matters">edit</a> \| (./index.php.md)\]

At zero temperature in an undoped system, the chemical potential
coincides with the Fermi energy. However, in real materials and
realistic conditions:

- The system may be doped, i.e., it contains additional electrons or
  holes.
- The system may be at finite temperature, which modifies the balance
  between electron and hole occupations.
- The transport coefficients are dominated by states within a narrow
  energy window around the chemical potential, so even small
  inaccuracies can lead to large errors.

Thus, in any calculation of electron–phonon interaction and related
transport properties, it is crucial to have a consistent way of
specifying and determining the chemical potential.

## Different ways to specify carriers\[<a
href="/wiki/index.php?title=Chemical_potential_in_electron-phonon_interactions&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Different ways to specify carriers">edit</a> \| (./index.php.md)\]

There are several equivalent, but practically distinct, ways of
describing the carrier concentration in a solid. Each corresponds to a
different way of constraining or shifting the chemical potential in the
calculation:

Shift of the chemical potential  
One can directly specify a shift of the chemical potential with respect
to the undoped zero-temperature Fermi energy. This approach is
straightforward when the doping is weak and the Fermi level remains
inside the same band. This is can be set with the
[ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md) tag. A range can
also be supplied using
[ELPH_SELFEN_MU_RANGE](../incar-tags/ELPH_SELFEN_MU_RANGE.md).

<!-- -->

Carrier density  
Alternatively, one can specify the additional carrier density (per
volume). This is the natural way to connect with experimental
conditions, where doping levels are often given as carrier densities
(e.g. 10<sup>18</sup> cm<sup>-3</sup>). The calculation must then solve
self-consistently for the chemical potential that yields the specified
carrier density. This is can be set with the
[ELPH_SELFEN_CARRIER_DEN](../incar-tags/ELPH_SELFEN_CARRIER_DEN.md)
tag. A range can also be supplied using
[ELPH_SELFEN_CARRIER_DEN_RANGE](../incar-tags/ELPH_SELFEN_CARRIER_DEN_RANGE.md).

<!-- -->

Extra carriers per unit cell  
Finally, one may work in terms of the number of additional carriers per
unit cell. This is a natural choice in periodic first-principles
calculations, where the fundamental unit is the primitive cell. Again, a
self-consistent procedure determines the chemical potential consistent
with the requested number of carriers. This is can be set with the
[ELPH_SELFEN_CARRIER_PER_CELL](../incar-tags/ELPH_SELFEN_CARRIER_PER_CELL.md)
tag.

Each of these perspectives can be translated into the others, but
depending on the context, one choice may be more convenient. For
example, experiments usually quote carrier density, while theoretical
band-structure calculations naturally yield the relation between
chemical potential and extra carriers per cell.

## Related tags and articles\[<a
href="/wiki/index.php?title=Chemical_potential_in_electron-phonon_interactions&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [Electronic transport
  coefficients](Electronic_transport_coefficients.md)
- [ELPH_RUN](../incar-tags/ELPH_RUN.md)
- [ELPH_SELFEN_CARRIER_DEN](../incar-tags/ELPH_SELFEN_CARRIER_DEN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](../incar-tags/ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_CARRIER_PER_CELL](../incar-tags/ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_SELFEN_TEMPS](../incar-tags/ELPH_SELFEN_TEMPS.md)
- [ELPH_SELFEN_TEMPS_RANGE](../incar-tags/ELPH_SELFEN_TEMPS_RANGE.md)
- [ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md)
- [ELPH_SELFEN_MU_RANGE](../incar-tags/ELPH_SELFEN_MU_RANGE.md)
- [EFERMI](../incar-tags/EFERMI.md)



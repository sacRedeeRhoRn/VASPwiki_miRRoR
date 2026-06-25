<!-- Source: https://vasp.at/wiki/index.php/Langevin_thermostat | revid: 32301 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Langevin thermostat


The Langevin
thermostat[^allen:book:1991-1][^hoover:prl:1982-2][^evans:jcp:1983-3]
maintains the temperature through a modification of Newton's equations
of motion

$\dot{r_i} = p_i/m_i \qquad \dot{p_i} = F_i - {\gamma}_i\\p_i + f_i,$

where *F<sub>i</sub>* is the force acting on atom *i* due to the
interaction potential, γ<sub>i</sub> is a friction coefficient, and
*f<sub>i</sub>* is a random force simulating the random kicks by the
damping of particles between each other due to friction. The random
numbers are chosen from a Gaussian distribution with the following
variance

$\sigma_i^2 = 2\\m_i\{\gamma}_i\\k_B\\T/{\Delta}t$

with Δ*t* being the time-step used in the MD to integrate the equations
of motion. Obviously, Langevin dynamics is identical to the classical
Hamiltonian in the limit of vanishing γ.

- [NVT ensemble](../misc/NVT_ensemble.md):

The friction coefficient is set by the
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) parameter.

- [NpT ensemble](../misc/NpT_ensemble.md):

As for the [NVT ensemble](../misc/NVT_ensemble.md) the
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) parameter has to
be set. If the [NpT ensemble](../misc/NpT_ensemble.md) is used
(by setting [ISIF](../incar-tags/ISIF.md)=3) additionally the friction
coefficient of the lattice
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) has to be
provided too.

The Langevin thermostat is selected by MDALGO=3.

## Related tags and articles\[<a
href="/wiki/index.php?title=Langevin_thermostat&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [Andersen
thermostat](Andersen_thermostat.md),
[Nosé-Hoover
thermostat](Nosé-Hoover_thermostat.md),
[CSVR thermostat](../theory/CSVR_thermostat.md), [Nosé-Hoover
chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md),
[ISIF](../incar-tags/ISIF.md), [MDALGO](../incar-tags/MDALGO.md),
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md),
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md)

## References\[<a
href="/wiki/index.php?title=Langevin_thermostat&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^allen:book:1991-1]: [M. P. Allen and D. J. Tildesley, *Computer simulation of liquids* (Oxford university press: New York, 1991).](https://books.google.co.jp/books?id=WFExDwAAQBAJ&lpg=PP1&hl=ja&pg=PP1#v=onepage&q&f=false)
[^hoover:prl:1982-2]: [W. G. Hoover, A. J. C. Ladd, and B. Moran, Phys. Rev. Lett. **48**, 1818 (1982).](https://doi.org/10.1103/PhysRevLett.48.1818)
[^evans:jcp:1983-3]: [D. J. Evans, J. Chem. Phys. **78**, 3297 (1983).](https://doi.org/10.1063/1.445195)

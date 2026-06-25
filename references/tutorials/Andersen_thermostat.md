<!-- Source: https://vasp.at/wiki/index.php/Andersen_thermostat | revid: 32304 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Andersen thermostat


In the approach proposed by Andersen
[^andersen:jcp:1980-1]
the system is thermally coupled to a fictitious heat bath with the
desired temperature. The coupling is represented by stochastic
collisions that act occasionally on randomly selected particles. In
particular the momentum of the *lucky* particle at every collision step
is instantaneously chosen at random from the Boltzmann distribution at
the selected temperature. The collision probability is defined as an
average number of collisions per atom and time-step and the collision
frequency occurs with the following distribution

$P(t)=\nu e^{-\nu t}.$

The exponent of this the distribution ($\nu t$) is
controlled by the flag
[ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md). Since
$t$ is the time step in the calculation
[ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md) has to be scaled if
the time step changes. The total number of collisions with the heat-bath
is written out to the file [REPORT](../output-files/REPORT.md) for each MD
step.

A very good implementation of the Andersen thermostat can be found in
chapter 6.1.1 of reference
[^frenkel:book:1996-2].

The Andersen thermostat is selected by setting
[MDALGO](../incar-tags/MDALGO.md)=1.

## Related tags and articles\[<a
href="/wiki/index.php?title=Andersen_thermostat&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [Nosé-Hoover
thermostat](Nosé-Hoover_thermostat.md),
[Langevin thermostat](Langevin_thermostat.md),
[CSVR thermostat](../theory/CSVR_thermostat.md), [Nosé-Hoover
chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md),
[ISIF](../incar-tags/ISIF.md), [MDALGO](../incar-tags/MDALGO.md),
[ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)

## References\[<a
href="/wiki/index.php?title=Andersen_thermostat&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^andersen:jcp:1980-1]: [H. C. Andersen, J. Chem. Phys. **72**, 2384 (1980).](https://doi.org/10.1063/1.439486)
[^frenkel:book:1996-2]: [D. Frenkel and B. Smit, Understanding Molecular Simulation (Academic Press, London, 1996).](https://doi.org/10.1016/B978-0-12-267351-1.X5000-7)

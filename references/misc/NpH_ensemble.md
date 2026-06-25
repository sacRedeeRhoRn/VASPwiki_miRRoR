<!-- Source: https://vasp.at/wiki/index.php/NpH_ensemble | revid: 32848 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NpH ensemble


The NpH ensemble
(isoenthalpic–isobaric ensemble) is a [statistical
ensemble](../categories/Category-Ensembles.md) that is used to
study material properties under the conditions of a constant particle
number N, a pressure p fluctuating around an equilibrium pressure
$\langle p \rangle$ and a conserved enthalpy H (up to
numerical inaccuracies). This page describes how to sample the NpH
ensemble from a
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> run.

**Instructions for setting up a NpH ensemble**

To run an NpH
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a>
simulation [`MDALGO`](../incar-tags/MDALGO.md)` = 3` has to be used. The
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) and
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) have to be
zero to disable any thermostatting. By setting the tag
[`LANGEVIN_GAMMA`](../incar-tags/LANGEVIN_GAMMA.md)` = 0` the
friction term and the stochastic term of the [Langevin
thermostat](../tutorials/Langevin_thermostat.md) will be
zero, such that the velocities are determined by the Hellmann-Feynman
forces or machine-learned force fields only. Setting the tag
[`LANGEVIN_GAMMA_L`](../incar-tags/LANGEVIN_GAMMA_L.md)` = 0`,
removes the stochastic term and the friction term from the barostat,
resulting in a box update depending solely on the kinetic stress tensor.
The inertia of lattice degrees-of-freedom is controlled with the
[PMASS](../incar-tags/PMASS.md) tag.

|  |  |
|----|----|
| NpH ensemble | Langevin |
| [MDALGO](../incar-tags/MDALGO.md) | 3 |
| [ISIF](../incar-tags/ISIF.md) | 3 |
| [LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) | 0 |
| [LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) | 0 |
| optional tags to set | [PMASS](../incar-tags/PMASS.md) |

It is recommended to equilibrate the system of interest with an
[NPT](NpT_ensemble.md)
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> run
before starting the NpH run. A general guide for molecular-dynamics
simulations can be found on the
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> page.

*An example [INCAR](../input-files/INCAR.md) file for the NpH ensemble*

     #INCAR molecular-dynamics tags NpH ensemble 
     IBRION = 0                   # choose molecular-dynamics 
     MDALGO = 3                   # using Langevin thermostat
     ISIF = 3                     # compute stress tensor and allow change of box volume/shape 
     TEBEG = 300                  # set temperature 
     NSW = 10000                  # number of time steps 
     POTIM = 1.0                  # time step in femto seconds 
     LANGEVIN_GAMMA = 0.0 0.0     # setting friction and stochastic term of Langevin thermostat zero
     LANGEVIN_GAMMA_L = 0.0       # setting friction and stochastic term of Langevin barostat zero

|  |
|----|
| **Mind:** This [INCAR](../input-files/INCAR.md) file only contains the parameters for the molecular-dynamics part. The <a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> or the <a href="/wiki/Machine-learned_force_fields" class="mw-redirect"
title="Machine-learned force fields">machine learning</a> tags have to be added. |

## Related tags and articles\[<a
href="/wiki/index.php?title=NpH_ensemble&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [ISIF](../incar-tags/ISIF.md),
[MDALGO](../incar-tags/MDALGO.md),
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md),
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md),
[Ensembles](../categories/Category-Ensembles.md)



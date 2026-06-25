<!-- Source: https://vasp.at/wiki/index.php/NpT_ensemble | revid: 20295 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NpT ensemble


The NpT ensemble
(isothermal-isobaric ensemble) is a [statistical
ensemble](../categories/Category-Ensembles.md) that is used to
study material properties under the conditions of a constant particle
number N, a pressure p fluctuating around an equilibrium value
$\langle p \rangle$ and a temperature T fluctuating
around an equilibrium value $\langle T \rangle$. This page describes how to sample the NpT ensemble
from a
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> run.

**Instructions for setting up an NpT ensemble**

The Parinello-Rahman
algorithm[^parrinello:prl:1980-1][^parrinello:jap:1981-2]
is the method of choice when setting up an NpT
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> run. To
use the Parinello-Rahman algorithm the [Langevin
thermostat](../tutorials/Langevin_thermostat.md) has to be
adjusted for an NpT simulation by setting the
[ISIF](../incar-tags/ISIF.md)=3 in the [INCAR](../input-files/INCAR.md) file.
Otherwise, the lattice is not allowed to change during the simulation,
preventing VASP from keeping the pressure constant. Additionally the
user can set [LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) as
when simulating a [NVT ensemble](NVT_ensemble.md), the
tag [LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) which
is a friction coefficient for the lattice degrees of freedom and the
[PMASS](../incar-tags/PMASS.md) tag to assign a fictitious mass to the
lattice degrees of freedom.

|  |  |
|----|----|
| NpT ensemble | Langevin |
| [MDALGO](../incar-tags/MDALGO.md) | 3 |
| [ISIF](../incar-tags/ISIF.md) | 3 |
| additional tags to set | [LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md), [LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) |
| optional tags to set | [PMASS](../incar-tags/PMASS.md) |

The additional tags in the column for the thermostat have to be set
because the default values are zero resulting in a different ensemble.
To use the NpT ensemble VASP has to be compiled with the precompiler
flag <a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">-Dtbdyn</a>. A general guide for
molecular-dynamics simulations can be found on the
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> page.

*An example [INCAR](../input-files/INCAR.md) file for the NpT ensemble*

     #INCAR molecular-dynamics tags NpT ensemble 
     IBRION = 0                      # choose molecular-dynamics 
     MDALGO = 3                      # using Langevin thermostat
     ISIF = 3                        # compute stress tensor and change box volume/shape 
     TEBEG = 300                     # set temperature 
     NSW = 10000                     # number of time steps 
     POTIM = 1.0                     # time step in femto seconds 
     LANGEVIN_GAMMA = 10.0 10.0 10.0 # Langevin friction coefficient for three atomic species
     LANGEVIN_GAMMA_L = 10.0         # Langevin friction coefficient for lattice degrees of freedom
     PMASS = 1000                    # the fictitious mass of the lattice degrees of freedom

|  |
|----|
| **Mind:** This [INCAR](../input-files/INCAR.md) file only contains the parameters for the molecular-dynamics part. The <a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> or the <a href="/wiki/Machine-learned_force_fields" class="mw-redirect"
title="Machine-learned force fields">machine learning</a> tags have to be added. |

|  |
|----|
| **Warning:** Calculations of systems with limited long-range order (e.g. liquids) may lead to irreversible deformations of the cell within this ensemble. For those systems one must use an [ICONST](../input-files/ICONST.md) file containing constraints for the Bravais lattice. |

## Related tags and articles\[<a
href="/wiki/index.php?title=NpT_ensemble&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [ISIF](../incar-tags/ISIF.md),
[MDALGO](../incar-tags/MDALGO.md),
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md),
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md),
[PMASS](../incar-tags/PMASS.md),
[Ensembles](../categories/Category-Ensembles.md),
[ICONST](../input-files/ICONST.md)

## References\[<a
href="/wiki/index.php?title=NpT_ensemble&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^parrinello:prl:1980-1]: [M. Parrinello and A. Rahman, Phys. Rev. Lett. **45**, 1196 (1980).](https://doi.org/10.1103/PhysRevLett.45.1196)
[^parrinello:jap:1981-2]: [M. Parrinello and A. Rahman, J. Appl. Phys. **52**, 7182 (1981).](https://doi.org/10.1063/1.328693)

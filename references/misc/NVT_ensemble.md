<!-- Source: https://vasp.at/wiki/index.php/NVT_ensemble | revid: 32841 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NVT ensemble


The NVT ensemble (canonical
ensemble) is a [statistical
ensemble](../categories/Category-Ensembles.md) that is used to
study material properties under the conditions of a constant particle
number N, constant volume V and a temperature fluctuating around an
equilibrium value $\langle T \rangle$. This page describes how to sample the NVT ensemble
from a
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> run.

**Instructions for setting up an NVT ensemble**

There are multiple choices of thermostats to control the temperature for
the NVT ensemble: The stochastic [Andersen
thermostat](../tutorials/Andersen_thermostat.md), [Langevin
thermostat](../tutorials/Langevin_thermostat.md) and [CSVR
thermostat](../theory/CSVR_thermostat.md), as well as the
deterministic [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md),
[Nosé-Hoover chain
thermostat](Nosé-Hoover_chain_thermostat.md)
and [Multiple Andersen
thermostats](../incar-tags/MDALGO.md)
can be used. See table for the corresponding
[MDALGO](../incar-tags/MDALGO.md) setting and related tags.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| NVT ensemble | Nosé-Hoover<sup>[\[1\]](#cite_note-legacy-nh-1)</sup> | Andersen | Nosé-Hoover | Langevin | Nosé-Hoover chain | CSVR | Multiple Andersen |
| [MDALGO](../incar-tags/MDALGO.md) | 0 | 1 | 2 | 3 | 4 | 5 | 13 |
| additional tags to set | [SMASS](../incar-tags/SMASS.md) | [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md) | [SMASS](../incar-tags/SMASS.md) | [LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) | [NHC_NCHAINS](../incar-tags/NHC_NCHAINS.md), [NHC_PERIOD](NHC_PERIOD.md), [NHC_NRESPA](../incar-tags/NHC_NRESPA.md), [NHC_NS](../incar-tags/NHC_NS.md) | [CSVR_PERIOD](CSVR_PERIOD.md) | [NSUBSYS](../incar-tags/NSUBSYS.md), [TSUBSYS](../incar-tags/TSUBSYS.md), [PSUBSYS](../incar-tags/PSUBSYS.md) |

The additional tags in the column for every thermostat have to be set.
For example, the [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
needs the additional [SMASS](../incar-tags/SMASS.md) tag. To enforce
constant volume throughout the calculation, set
[`ISIF`](../incar-tags/ISIF.md)` < 3`. In NVT MD runs there is no control
over pressure because the volume is fixed. The average value will
therefore depend on the initial lattice given in the
[POSCAR](../input-files/POSCAR.md) file. It is often desirable to
equilibrate the lattice degrees of freedom, for example, by running an
[NpT simulation](NpT_ensemble.md) or by performing
structure and volume optimization with
[`IBRION`](../incar-tags/IBRION.md)` = 1 or 2` and setting
[`ISIF`](../incar-tags/ISIF.md)` > 2`. A general guide for
molecular-dynamics simulations can be found on the
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> page.

*Example [INCAR](../input-files/INCAR.md) file for the [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)*

     #INCAR molecular-dynamics tags NVT ensemble 
     IBRION = 0                   # choose molecular dynamics 
     MDALGO = 2                   # use Nosé-Hoover thermostat 
     ISIF = 2                     # compute stress tensor but do not change box volume/shape 
     TEBEG = 300                  # set temperature 
     NSW = 10000                  # number of time steps 
     POTIM = 1.0                  # time step in femto seconds 
     SMASS = 1.0                  # setting the virtual mass for the Nosé-Hoover thermostat

|  |
|----|
| **Mind:** This [INCAR](../input-files/INCAR.md) file only contains the parameters for the molecular-dynamics part. The <a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> or the <a href="/wiki/Machine-learned_force_fields" class="mw-redirect"
title="Machine-learned force fields">machine learning</a> tags have to be added. |

## Related tags and articles\[<a
href="/wiki/index.php?title=NVT_ensemble&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [ISIF](../incar-tags/ISIF.md),
[MDALGO](../incar-tags/MDALGO.md),
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md),
[SMASS](../incar-tags/SMASS.md),[ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md),
[NSUBSYS](../incar-tags/NSUBSYS.md), [TSUBSYS](../incar-tags/TSUBSYS.md),
[PSUBSYS](../incar-tags/PSUBSYS.md)

## Footnotes and references\[<a
href="/wiki/index.php?title=NVT_ensemble&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Footnotes and references">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-legacy-nh_1-0)
    If possible, use another Nosé–Hoover
    thermostat implementation, e.g.
    [`MDALGO`](../incar-tags/MDALGO.md)` = 2`, see also comments
    [here](../incar-tags/MDALGO.md).



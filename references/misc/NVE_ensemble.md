<!-- Source: https://vasp.at/wiki/index.php/NVE_ensemble | revid: 32847 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NVE ensemble


The NVE ensemble
(micro-canonical ensemble) is a [statistical
ensemble](../categories/Category-Ensembles.md) that is used to
study material properties under the conditions of a constant particle
number N, constant volume V and a conserved internal energy E (up to
numerical inaccuracies). This page describes how to sample the NVE
ensemble from a
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> run.

**Instructions for setting up a NVE ensemble**

There are multiple ways to set up a
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> run which
samples from the NVE ensemble in VASP. All options have in common that
one of the available thermostats is selected but effectively disabled
via their respective coupling parameters. The simplest and recommended
way is to use the [Andersen
thermostat](../tutorials/Andersen_thermostat.md) and setting
the collision probability
([ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)) with the
fictitious heat bath to zero. Another possibility is to enable the
[Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
and select the special value -3 for the mass of the virtual degree of
freedom ([SMASS](../incar-tags/SMASS.md)). Both presented options will
switch the thermostat off, such that the velocities are determined by
the [Hellmann-Feynman
forces](../theory/Hellmann-Feynman_forces.md) or
<a href="/wiki/Machine-learned_force_fields" class="mw-redirect"
title="Machine-learned force fields">Machine-learned force fields</a>
only. See the following table for the corresponding
[MDALGO](../incar-tags/MDALGO.md) setting and related tags.

|  |  |  |
|----|----|----|
| NVE ensemble | Andersen | Nosé-Hoover |
| [MDALGO](../incar-tags/MDALGO.md) | 1 | 2 |
| additional tags to set | [`ANDERSEN_PROB`](../incar-tags/ANDERSEN_PROB.md)` = 0.0` | [`SMASS`](../incar-tags/SMASS.md)` = -3` |

The additional tags in the column for every thermostat have to be set to
the given values. Otherwise the NVE ensemble will not be realized.

|  |
|----|
| **Deprecated:** VASP comes with another, older implementation of the [Nosé-Hoover thermostat](../tutorials/Nosé-Hoover_thermostat.md) which can be selected with [`MDALGO`](../incar-tags/MDALGO.md)` = 0`. However, we recommend [`MDALGO`](../incar-tags/MDALGO.md)` = 2` as stated above because the older variant comes with some drawbacks regarding post-processing: the atom coordinates in output files will always be wrapped back into the box if atoms cross the periodic boundaries. This makes it impossible to carry out certain analysis, e.g. computing the mean squared displacement (MSD). |

To enforce constant volume throughout the calculation, set
[`ISIF`](../incar-tags/ISIF.md)` < 3`. In NVE MD runs there is no control
over temperature and pressure, their respective averages depend on the
initial structure (lattice, atom positions provided in
[POSCAR](../input-files/POSCAR.md)) and initial velocities (either set in
[POSCAR](../input-files/POSCAR.md) or via [TEBEG](../incar-tags/TEBEG.md)).
Hence, it is often desirable to equilibrate the system before sampling
from the NVE ensemble. This can be achieved in various ways, for
example, the system can be thermalized by performing an MD simulation in
the [NVT ensemble](NVT_ensemble.md) or thermalized and
additionally its cell equilibrated via the [NpT
ensemble](NpT_ensemble.md). Preparatory steps may also
include non-MD algorithms, like structure and volume optimization with
[`IBRION`](../incar-tags/IBRION.md)` = 1 or 2` and setting
[`ISIF`](../incar-tags/ISIF.md)` > 2`. A general guide for
molecular-dynamics simulations can be found on the
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">molecular-dynamics</a> page.

*An example [INCAR](../input-files/INCAR.md) file for the [Andersen
thermostat](../tutorials/Andersen_thermostat.md)*

     #INCAR molecular-dynamics tags NVE ensemble 
     IBRION = 0                   # choose molecular-dynamics 
     MDALGO = 1                   # using Andersen thermostat
     ISIF = 2                     # compute stress tensor but do not change box volume/shape 
     TEBEG = 300                  # set temperature 
     NSW = 10000                  # number of time steps 
     POTIM = 1.0                  # time step in femto seconds 
     ANDERSEN_PROB = 0.0          # setting Andersen collision probability to zero to get NVE enseble

|  |
|----|
| **Mind:** This [INCAR](../input-files/INCAR.md) file only contains the parameters for the molecular-dynamics part. The <a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> or the <a href="/wiki/Machine-learned_force_fields" class="mw-redirect"
title="Machine-learned force fields">machine learning</a> tags have to be added. |

## Related tags and articles\[<a
href="/wiki/index.php?title=NVE_ensemble&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [ISIF](../incar-tags/ISIF.md),
[MDALGO](../incar-tags/MDALGO.md),
[Ensembles](../categories/Category-Ensembles.md)



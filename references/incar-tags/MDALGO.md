<!-- Source: https://vasp.at/wiki/index.php/MDALGO | revid: 32807 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MDALGO


MDALGO = 0 \| 1 \| 2 \| 3 \| 4
\| 5 \| 11 \| 21 \| 13  
Default: **MDALGO** = 0 

Description: Specifies the
<a href="/wiki/Thermostat" class="mw-redirect"
title="Thermostat">thermostat</a> and lattice dynamics for
[molecular-dynamics
calculations](../tutorials/Molecular-dynamics_calculations.md)
(in case [`IBRION`](IBRION.md)` = 0`).

------------------------------------------------------------------------

The algorithm for the <a href="/wiki/Thermostat" class="mw-redirect"
title="Thermostat">thermostat</a> and lattice dynamics is a crucial
choise for any [molecular-dynamics (MD)
calculations](../tutorials/Molecular-dynamics_calculations.md)
([`IBRION`](IBRION.md)` = 0`). In combination with the
selected lattice degrees of freedom ([ISIF](ISIF.md)),
MDALGO determines the
<a href="/wiki/Ensemble" class="mw-redirect"
title="Ensemble">ensemble</a> that is sampled during the [MD
run](../tutorials/Molecular-dynamics_calculations.md).
The main output file is the [REPORT](../output-files/REPORT.md) file.

MDALGO can be applied in the
context of standard [molecular-dynamics
calculations](../tutorials/Molecular-dynamics_calculations.md),
[constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md),
[metadynamics
calculations](../tutorials/Metadynamics_calculations.md),
the [slow-growth
approach](../theory/Slow-growth_approach.md), monitoring
geometric parameters using the [ICONST](../input-files/ICONST.md) file,
[biased molecular
dynamics](../theory/Biased_molecular_dynamics.md),
and more.

|  |
|----|
| **Mind:** `MDALGO`` >= 0` requires compilation with the precompiler option [`-Dtbdyn`](../misc/Precompiler_options.md). This option is present by default in all [makefile.include](../misc/Makefile.include.md) templates since VASP 5.4.4. |


## Contents


- [1
  Options](#Options)
  - [1.1 MDALGO =
    1: Andersen thermostat](#MDALGO_=_1:_Andersen_thermostat)
  - [1.2 MDALGO =
    2: Nosé-Hoover
    thermostat](#MDALGO_=_2:_Nosé-Hoover_thermostat)
  - [1.3 MDALGO =
    3: Langevin thermostat](#MDALGO_=_3:_Langevin_thermostat)
  - [1.4 MDALGO =
    4: Nosé-Hoover chain
    thermostat](#MDALGO_=_4:_Nosé-Hoover_chain_thermostat)
  - [1.5 MDALGO =
    5: Canonical sampling through velocity-rescaling (CSVR
    thermostat)](#MDALGO_=_5:_Canonical_sampling_through_velocity-rescaling_(CSVR_thermostat))
  - [1.6 MDALGO =
    13: Multiple Andersen
    thermostats](#MDALGO_=_13:_Multiple_Andersen_thermostats)
  - [1.7 MDALGO = 0
    (deprecated)](#MDALGO_=_0_(deprecated))
  - [1.8 MDALGO =
    11 (deprecated)](#MDALGO_=_11_(deprecated))
  - [1.9 MDALGO =
    21 (deprecated)](#MDALGO_=_21_(deprecated))
- [2 Related tags
  and articles](#Related_tags_and_articles)
- [3
  References](#References)


## Options\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Options">edit</a> \| (./index.php.md)\]

### `MDALGO`` = 1`: [Andersen thermostat](../tutorials/Andersen_thermostat.md)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 1: Andersen thermostat">edit</a> \| (./index.php.md)\]

The [Andersen
thermostat](../tutorials/Andersen_thermostat.md) can be used
to sample an [NVT ensemble](../misc/NVT_ensemble.md) or [NVE
ensemble](../misc/NVE_ensemble.md). It requires setting an
appropriate value for
[ANDERSEN_PROB](ANDERSEN_PROB.md). For an [NVE
ensemble](../misc/NVE_ensemble.md), set
[`ANDERSEN_PROB`](ANDERSEN_PROB.md)` = 0.0`. This is
usually done after thermalization to a certain target temperature.

|  |
|----|
| **Tip:** Leave the value for [TEBEG](TEBEG.md) that was set in the thermalization. For [`TEBEG`](TEBEG.md)` < 0.1`, some part of the code assumes it is used for [structure optimization](../tutorials/Structure_optimization.md) and not an [MD run](../tutorials/Molecular-dynamics_calculations.md). |

### `MDALGO`` = 2`: [Nosé-Hoover thermostat](../tutorials/Nosé-Hoover_thermostat.md)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 2: Nosé-Hoover thermostat">edit</a> \| (./index.php.md)\]

The [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
is currently only available for the [NVT
ensemble](../misc/NVT_ensemble.md). It requires setting an
appropriate value for [SMASS](SMASS.md).

|  |
|----|
| **Tip:** The [Nosé-Hoover thermostat](../tutorials/Nosé-Hoover_thermostat.md) is a special case of the [Nosé-Hoover chain thermostat](../misc/Nosé-Hoover_chain_thermostat.md) (`MDALGO`` = 4` with [NHC_NCHAINS](NHC_NCHAINS.md) = 1 ). The control tags for `MDALGO`` = 4` may be more convenient to use than the older implementation (`MDALGO`` = 2`). |

### `MDALGO`` = 3`: [Langevin thermostat](../tutorials/Langevin_thermostat.md)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 3: Langevin thermostat">edit</a> \| (./index.php.md)\]

The [Langevin
thermostat](../tutorials/Langevin_thermostat.md) is
available for sampling the [NVT
ensemble](../misc/NVT_ensemble.md), [NpT
ensemble](../misc/NpT_ensemble.md) and [NpH
ensemble](../misc/NpH_ensemble.md). The Langevin dynamics in
the [NpT ensemble](../misc/NpT_ensemble.md) is calculated by
the method of Parrinello and
Rahman<sup>[\[1\]](#cite_note-parrinello:prl:1980-1)[\[2\]](#cite_note-parrinello:jap:1981-2)</sup>
combined with a [Langevin
thermostat](../tutorials/Langevin_thermostat.md).

- [NVT ensemble](../misc/NVT_ensemble.md): Set an appropriate
  value for the friction coefficients
  ([LANGEVIN_GAMMA](LANGEVIN_GAMMA.md)) for all
  species in the [POSCAR](../input-files/POSCAR.md) file to enables the
  [Langevin
  thermostat](../tutorials/Langevin_thermostat.md). Fix the
  cell shape and volume with [`ISIF`](ISIF.md)` <= 2`.
- [NpT ensemble](../misc/NpT_ensemble.md): To enable lattice
  dynamics set [`ISIF`](ISIF.md)` = 3` and specify a separate
  set of friction coefficient for the lattice degrees-of-freedom
  ([LANGEVIN_GAMMA_L](LANGEVIN_GAMMA_L.md)) as
  well as a ficticious mass for the lattice degrees-of-freedom
  ([PMASS](PMASS.md)). At the moment, dynamics with *fixed
  volume+variable shape* ([`ISIF`](ISIF.md)` = 4`) or *fixed
  shape+variable volume* ([`ISIF`](ISIF.md)` = 7`) are not
  available. Optionally, one may define an external pressure
  ([PSTRESS](PSTRESS.md)). Like for the NVT ensemble, set
  an appropriate value for the friction coefficients
  ([LANGEVIN_GAMMA](LANGEVIN_GAMMA.md)) for all
  species in the [POSCAR](../input-files/POSCAR.md) file to enables the
  [Langevin
  thermostat](../tutorials/Langevin_thermostat.md).

Also see [stochastic boundary
conditions](../misc/Stochastic_boundary_conditions.md).

### `MDALGO`` = 4`: [Nosé-Hoover chain thermostat](../misc/Nosé-Hoover_chain_thermostat.md)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 4: Nosé-Hoover chain thermostat">edit</a> \| (./index.php.md)\]

The [Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md)
can be only used to sample an [NVT
ensemble](../misc/NVT_ensemble.md) and requires selecting the
number of thermostats in the chain via
[NHC_NCHAINS](NHC_NCHAINS.md) as well as choosing an
appropriate setting for the thermostat parameter
[NHC_PERIOD](../misc/NHC_PERIOD.md).

### `MDALGO`` = 5`: [Canonical sampling through velocity-rescaling (CSVR thermostat)](../theory/CSVR_thermostat.md)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 5: Canonical sampling through velocity-rescaling (CSVR thermostat)">edit</a> \| (./index.php.md)")\]

|  |
|----|
| **Mind:** This option is available as of VASP 6.4.3. |

The [CSVR thermostat](../theory/CSVR_thermostat.md) can be
used to sample an [NVT ensemble](../misc/NVT_ensemble.md). It
requires setting [CSVR_PERIOD](../misc/CSVR_PERIOD.md).

### `MDALGO`` = 13`: Multiple [Andersen thermostats](../tutorials/Andersen_thermostat.md)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 13: Multiple Andersen thermostats">edit</a> \| (./index.php.md)\]


Up to three user-defined atomic subsystems may be coupled with
independent [Andersen
thermostats](../tutorials/Andersen_thermostat.md)<sup>[\[3\]](#cite_note-andersen:jcp:1980-3)</sup>
(`MDALGO`` = 1`). The
[POSCAR](../input-files/POSCAR.md) file must be organized such that the
positions of atoms of subsystem *i+1* are defined after those for the
subsystem *i*, and the following tags must be set:
[NSUBSYS](NSUBSYS.md), [TSUBSYS](TSUBSYS.md),
and [PSUBSYS](PSUBSYS.md).

### `MDALGO`` = 0` (deprecated)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 0 (deprecated)">edit</a> \| (./index.php.md)")\]

Selects a [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
which allows sampling the [NVT
ensemble](../misc/NVT_ensemble.md) at temperature
[TEBEG](TEBEG.md). The [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
requires an appropriate setting for [SMASS](SMASS.md). To
sample an [NVE ensemble](../misc/NVE_ensemble.md) set
[`SMASS`](SMASS.md)` = -3`.

|  |
|----|
| **Deprecated:** If possible, we recommend using one of the newer Nosé-Hoover thermostat implementations VASP provides (`MDALGO`` = 2 or 4`). While the results (ensemble averages) should be identical ,this variant comes with some drawbacks regarding post-processing: the atom coordinates in output files will always be wrapped back into the box if atoms cross the periodic boundaries. This makes it impossible to carry out certain analysis, e.g., computing the mean squared displacement (MSD). |

### `MDALGO`` = 11` (deprecated)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 11 (deprecated)">edit</a> \| (./index.php.md)")\]

For VASP 5.x MDALGO = 11 
selects the [Andersen
thermostat](../tutorials/Andersen_thermostat.md). This is
replaced by `MDALGO`` = 1`.

### `MDALGO`` = 21` (deprecated)\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: MDALGO = 21 (deprecated)">edit</a> \| (./index.php.md)")\]

For VASP 5.x it selects the [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md).
This is replaced by
`MDALGO`` = 2`.

## Related tags and articles\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

|  |  |
|:--:|:--:|
| <a href="/wiki/Thermostats" class="mw-redirect"
title="Thermostats">thermostats</a> | related <a href="/wiki/INCAR_tag" class="mw-redirect" title="INCAR tag">INCAR
tag</a> |
| [Langevin thermostat and dynamics](../tutorials/Langevin_thermostat.md) | [LANGEVIN_GAMMA](LANGEVIN_GAMMA.md), [LANGEVIN_GAMMA_L](LANGEVIN_GAMMA_L.md), [PMASS](PMASS.md), [PSTRESS](PSTRESS.md) |
| [Andersen thermostat](../tutorials/Andersen_thermostat.md) | [ANDERSEN_PROB](ANDERSEN_PROB.md) |
| Multiple [Andersen thermostats](../tutorials/Andersen_thermostat.md) | [NSUBSYS](NSUBSYS.md), [TSUBSYS](TSUBSYS.md), [PSUBSYS](PSUBSYS.md) |
| [Nosé-Hoover thermostat](../tutorials/Nosé-Hoover_thermostat.md) | [SMASS](SMASS.md) |
| [Nosé-Hoover chain thermostat](../misc/Nosé-Hoover_chain_thermostat.md) | [NHC_NCHAINS](NHC_NCHAINS.md), [NHC_PERIOD](../misc/NHC_PERIOD.md), [NHC_NRESPA](NHC_NRESPA.md), [NHC_NS](NHC_NS.md) |
| [CSVR thermostat](../theory/CSVR_thermostat.md) | [CSVR_PERIOD](../misc/CSVR_PERIOD.md) |

General MD-related tags: [IBRION](IBRION.md),
[NSW](NSW.md), [POTIM](POTIM.md),
[ISIF](ISIF.md),
[RANDOM_SEED](RANDOM_SEED.md)

MD output: [REPORT](../output-files/REPORT.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-MDALGO-_incategory-Howto)

## References\[<a href="/wiki/index.php?title=MDALGO&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-parrinello:prl:1980_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.45.1196"
    class="external text" rel="nofollow">M. Parrinello and A. Rahman, Phys.
    Rev. Lett. <strong>45</strong>, 1196 (1980).</a>
2.  [↑](#cite_ref-parrinello:jap:1981_2-0)
    <a href="https://doi.org/10.1063/1.328693" class="external text"
    rel="nofollow">M. Parrinello and A. Rahman, J. Appl. Phys.
    <strong>52</strong>, 7182 (1981).</a>
3.  [↑](#cite_ref-andersen:jcp:1980_3-0)
    <a href="https://doi.org/10.1063/1.439486" class="external text"
    rel="nofollow">H. C. Andersen, J. Chem. Phys. <strong>72</strong>, 2384
    (1980).</a>



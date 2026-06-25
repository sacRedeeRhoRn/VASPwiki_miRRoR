<!-- Source: https://vasp.at/wiki/index.php/Category:Thermostats | revid: 32322 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Thermostats


**Thermostats** are used in
<a href="/wiki/MD" class="mw-redirect" title="MD">molecular-dynamics
calculations</a> within the [NVT
ensemble](../misc/NVT_ensemble.md) and [NpT
ensemble](../misc/NpT_ensemble.md) in order to apply a certain
temperature to the ionic degrees of freedom.

Choose between stochastic **thermostats**:

- [Andersen thermostat](../tutorials/Andersen_thermostat.md)
- [Langevin thermostat](../tutorials/Langevin_thermostat.md)
- [CSVR thermostat](../theory/CSVR_thermostat.md)

and deterministic **thermostats**:

- [Nosé-Hoover
  thermostat](../tutorials/Nosé-Hoover_thermostat.md)
- [Nosé-Hoover chain
  thermostat](../misc/Nosé-Hoover_chain_thermostat.md)

|  |
|----|
| **Mind:** All **thermostats** are available in the [NVT ensemble](../misc/NVT_ensemble.md) but currently only the [Langevin thermostat](../tutorials/Langevin_thermostat.md) is available for the [NpT ensemble](../misc/NpT_ensemble.md). |

The following table gives an overview of the possible combination of
<a href="/wiki/Ensembles" class="mw-redirect"
title="Ensembles">ensembles</a> and **thermostats** in VASP:

|  |  |  |  |  |  |  |
|----|:--:|:--:|:--:|:--:|:--:|:--:|
|  | Thermostat |  |  |  |  |  |
| [Ensemble](Category-Ensembles.md) | [Andersen](../tutorials/Andersen_thermostat.md) | [Nosé-Hoover](../tutorials/Nosé-Hoover_thermostat.md) | [Langevin](../tutorials/Langevin_thermostat.md) | [Nosé-Hoover chain](../misc/Nosé-Hoover_chain_thermostat.md) | [CSVR](../theory/CSVR_thermostat.md) | [Multiple Andersen](../incar-tags/MDALGO.md) |
| [Microcanonical (NVE)](../misc/NVE_ensemble.md) | [MDALGO](../incar-tags/MDALGO.md)=1, [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)=0.0 |  |  |  |  |  |
| [Canonical (NVT)](../misc/NVT_ensemble.md) | [MDALGO](../incar-tags/MDALGO.md)=1 | [MDALGO](../incar-tags/MDALGO.md)=2 | [MDALGO](../incar-tags/MDALGO.md)=3 | [MDALGO](../incar-tags/MDALGO.md)=4 | [MDALGO](../incar-tags/MDALGO.md)=5 | [MDALGO](../incar-tags/MDALGO.md)=13 |
|  | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 | [ISIF](../incar-tags/ISIF.md)=2 |
| [Isobaric-isothermal (NpT)](../misc/NpT_ensemble.md) | not available | not available | [MDALGO](../incar-tags/MDALGO.md)=3 | not available | not available | not available |
|  |  |  | [ISIF](../incar-tags/ISIF.md)=3 |  |  |  |
| [Isoenthalpic-isobaric (NpH)](../misc/NpH_ensemble.md) | [MDALGO](../incar-tags/MDALGO.md)=3, [ISIF](../incar-tags/ISIF.md)=3, [LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md)=[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md)=0.0 |  |  |  |  |  |



<!-- Source: https://vasp.at/wiki/index.php/NHC_PERIOD | revid: 32338 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NHC_PERIOD


NHC_PERIOD = \[real\]  
Default: **NHC_PERIOD** = 40 

Description: Time scale of the [Nosé-Hoover
chain](Nosé-Hoover_chain_thermostat.md)
in terms of the number of MD steps.

------------------------------------------------------------------------

NHC_PERIOD sets the time scale
($\tau$) of the [Nosé-Hoover chain
thermostat](Nosé-Hoover_chain_thermostat.md).
It is expressed in terms of the number of MD steps and must be
interpreted in combination with the time step set by
[POTIM](../incar-tags/POTIM.md). The setting
NHC_PERIOD=0 corresponds will
generate the NVE ensemble.

|  |
|----|
| **Tip:** The value of NHC_PERIOD should correspond to a characteristic time scale in the system. If this is unknown, NHC_PERIOD should be set to a value between 20 and 200. |

## Related tags and articles\[<a
href="/wiki/index.php?title=NHC_PERIOD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[POTIM](../incar-tags/POTIM.md),
[NHC_NCHAINS](../incar-tags/NHC_NCHAINS.md), [Nosé-Hoover chain
thermostat](Nosé-Hoover_chain_thermostat.md)

------------------------------------------------------------------------



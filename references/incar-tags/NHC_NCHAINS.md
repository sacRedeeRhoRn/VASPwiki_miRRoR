<!-- Source: https://vasp.at/wiki/index.php/NHC_NCHAINS | revid: 32337 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NHC_NCHAINS


NHC_NCHAINS = \[integer\]  
Default: **NHC_NCHAINS** = 0 

Description: Length of the Nosé-Hoover chain.

------------------------------------------------------------------------

NHC_NCHAINS sets the length of
the chain for the [Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md).
Typically, this tag is set to a value between 1 and 5. The maximal
allowed value is 20.

In case NHC_NCHAINS=0, the
thermostat is switched off and the underlying dynamics generate a
[microcanonical (NVE) ensemble](../misc/NVE_ensemble.md).
NHC_NCHAINS=1 corresponds to
the [standard Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=NHC_NCHAINS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NHC_PERIOD](../misc/NHC_PERIOD.md), [Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md)

------------------------------------------------------------------------



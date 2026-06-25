<!-- Source: https://vasp.at/wiki/index.php/NHC_NRESPA | revid: 32339 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NHC_NRESPA


NHC_NRESPA = \[integer\]  
Default: **NHC_NRESPA** = 1 

Description: The number of subdivisions of the integration step used in
propagation of thermostat variables in the [Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md).

------------------------------------------------------------------------

NHC_NRESPA sets the number of
subdivisions of the integration step used in propagation of thermostat
variables in the \[\[Nosé-Hoover chain thermostat. This might be needed
in accurate calculations where, due to rapidly varying terms appearing
in thermostat variables propagators could cause significant drifts of
total energy (including energy contributions due to thermostat), which
is a conserved quantity.

  

## Related tags and articles\[<a
href="/wiki/index.php?title=NHC_NRESPA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NHC_PERIOD](../misc/NHC_PERIOD.md),
[NHC_NS](NHC_NS.md), [Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md)

------------------------------------------------------------------------



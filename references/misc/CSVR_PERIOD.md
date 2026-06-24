<!-- Source: https://vasp.at/wiki/index.php/CSVR_PERIOD | revid: 22612 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CSVR_PERIOD
CSVR_PERIOD = \[real\]  
Default: **CSVR_PERIOD** = 0 

Description: Time scale of the [CSVR
thermostat](../theory/CSVR_thermostat.md) in terms of the
number of MD steps.

------------------------------------------------------------------------

CSVR_PERIOD sets the time scale ($\tau$)
of the [CSVR thermostat](../theory/CSVR_thermostat.md). It is
expressed in terms of the number of MD steps and must be interpreted in
combination with the time step set by [POTIM](../incar-tags/POTIM.md).
Typically, CSVR_PERIOD should take the values corresponding to 2-2000
fs, whereby the smaller the value, the more aggressive the
thermostating. The special setting CSVR_PERIOD=0 generates the NVE
ensemble.

## Related tags and articles
[POTIM](../incar-tags/POTIM.md), [CSVR
thermostat](../theory/CSVR_thermostat.md)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/NTAUPAR | revid: 24279 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NTAUPAR
NTAUPAR = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **NTAUPAR** | = depends on [MAXMEM](MAXMEM.md) | used in low scaling [GW](../methods/GW_approximation_of_Hedin's_equations.md) and RPA/ACFDT calculations. |

Description: NTAUPAR available as of VASP.6, specifies the number of MPI
groups sharing same imaginary time grid points. The default value of
NTAUPAR is set to the largest possible value supported on the compute
nodes to speed up the GW or RPA calculation.

------------------------------------------------------------------------

NTAUPAR has the biggest impact on memory usage as well as total runtime
for low-scaling GW and RPA calculations. If not found in the
[INCAR](../input-files/INCAR.md), NTAUPAR is set automatically based on the
value of [MAXMEM](MAXMEM.md) (the available memory for each
rank on each compute node), such that the GW and RPA job fits in the RAM
on each compute node.

If [MAXMEM](MAXMEM.md) is not set, VASP looks in
"/proc/meminfo" for "MemAvailable" to set
[MAXMEM](MAXMEM.md) internally, otherwise the code uses the
value provided in the [INCAR](../input-files/INCAR.md).

NTAUPAR=[NOMEGA](NOMEGA.md) is the maximum value possible,
while NTAUPAR=1 is the smallest possible value.

## Related tags and articles
[NOMEGAPAR](NOMEGAPAR.md),
[NOMEGA](NOMEGA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NTAUPAR-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/NOMEGAR | revid: 16970 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NOMEGAR
NOMEGAR = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **NOMEGAR** | = [NOMEGA](NOMEGA.md) | for [GW calculations](../redirects/GW_calculations.md) |
|  | = 0 | for [ACFDT calculations](../redirects/ACFDT_calculations.md) |

Description: NOMEGAR specifies the number of frequency grid points along
the real axis.

------------------------------------------------------------------------

Usually NOMEGAR equals [NOMEGA](NOMEGA.md). If NOMEGAR is
smaller than [NOMEGA](NOMEGA.md) (for instance 0),
frequencies along the imaginary time axis are included (this feature is
currently not fully supported).

## Related tags and articles
[NOMEGA](NOMEGA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NOMEGAR-_incategory-Examples)

------------------------------------------------------------------------

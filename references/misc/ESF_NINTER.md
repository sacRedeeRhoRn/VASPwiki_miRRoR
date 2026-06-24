<!-- Source: https://vasp.at/wiki/index.php/ESF_NINTER | revid: 27631 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ESF_NINTER
ESF_NINTER = \[integer\]  
Default: **ESF_NINTER** = 15 

Description: ESF_NINTER sets the maximum number of interpolation steps
for the electronic structure factor
([ESF_SPLINES](ESF_SPLINES.md)).

------------------------------------------------------------------------

If the threshold set by [ESF_CONV](ESF_CONV.md) has not
been reached within ESF_NINTER iterations VASP will print a warning
about insufficient convergence.

## Related tags and articles
[ESF_SPLINES](ESF_SPLINES.md),
[ESF_CONV](ESF_CONV.md),
[LOPTICS](../incar-tags/LOPTICS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ESF_SPLINES-_incategory-Examples)

  

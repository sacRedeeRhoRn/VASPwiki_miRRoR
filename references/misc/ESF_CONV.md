<!-- Source: https://vasp.at/wiki/index.php/ESF_CONV | revid: 27627 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ESF_CONV
ESF_CONV = \[real\]  
Default: **ESF_CONV** = 0.01 

Description: Sets the convergence criterion for
[ESF_SPLINES](ESF_SPLINES.md), i.e., the threshold for
the energy difference between two interpolations (in eV).

------------------------------------------------------------------------

If the energy between two interpolated k-point grids is less than
ESF_CONV the calculation is considered to be converged. If the threshold
has not been reached within [ESF_NINTER](ESF_NINTER.md)
iterations VASP will print a warning about insufficient convergence.

## Related tags and articles
[ESF_SPLINES](ESF_SPLINES.md),
[ESF_NINTER](ESF_NINTER.md),
[LOPTICS](../incar-tags/LOPTICS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ESF_SPLINES-_incategory-Examples)

  

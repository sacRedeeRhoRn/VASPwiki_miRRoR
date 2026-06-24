<!-- Source: https://vasp.at/wiki/index.php/LDOWNSAMPLE | revid: 35909 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDOWNSAMPLE
LDOWNSAMPLE = \[logical\]  
Default: **LDOWNSAMPLE** = .FALSE. 

Description: LDOWNSAMPLE selects a sub-grid of k-points defined in
[KPOINTS](../input-files/KPOINTS.md) from
[WAVECAR](../input-files/WAVECAR.md)

------------------------------------------------------------------------

If LDOWNSAMPLE is present, VASP selects a sub-grid of k-points defined
in [KPOINTS](../input-files/KPOINTS.md) and stored in the
[WAVECAR](../input-files/WAVECAR.md) file. This option is automatically
selected for [cRPA
calculations](../theory/Constrained–random-phase–approximation_formalism.md),
where it can be beneficial to perform the Wannier projection on a denser
k-point grid than the actual cRPA calculation. For this purpose, the
Wannier projection should be written to
[WANPROJ](../input-files/WANPROJ.md).

This tag is not restricted to cRPA jobs and can be used for any other
task that start from a pre-calculated [WAVECAR](../input-files/WAVECAR.md)
and/or [WANPROJ](../input-files/WANPROJ.md) file.

By default, the automatic search for the grid multiplier applies the
same factor in all three reciprocal-lattice directions. For anisotropic
k-point grids where the dense-to-coarse ratio differs per direction, set
[K_MULTIPLY](K_MULTIPLY.md) explicitly. Setting
[K_MULTIPLY](K_MULTIPLY.md) in the
[INCAR](../input-files/INCAR.md) automatically enables LDOWNSAMPLE.

## Related tags and articles
[K_MULTIPLY](K_MULTIPLY.md),
[LWANNIER90](LWANNIER90.md),
[LWANNIER90_RUN](LWANNIER90_RUN.md),
[WANPROJ](../input-files/WANPROJ.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LDOWNSAMPLE-_incategory-Examples)

------------------------------------------------------------------------

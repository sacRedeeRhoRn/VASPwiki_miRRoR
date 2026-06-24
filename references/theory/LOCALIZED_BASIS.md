<!-- Source: https://vasp.at/wiki/index.php/LOCALIZED_BASIS | revid: 35241 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LOCALIZED_BASIS
LOCALIZED_BASIS = MLWF \| BLOCH \| LOCPROJ 

Description: Specifies which basis is used for Coulomb matrix elements
in constrained random-phase approximation (cRPA) calculations.

------------------------------------------------------------------------

This tag is effective for [`ALGO`](../incar-tags/ALGO.md)` = CRPA`\[R\] and
[`ALGO`](../incar-tags/ALGO.md)` = 2E4W` and is ignored otherwise. The tag
affects how [NTARGET_STATES](../incar-tags/NTARGET_STATES.md) is
interpreted. For instance

    LOCALIZED_BASIS = BLOCH
    NTARGET_STATES = 1 4 5 8 

evaluates the Coulomb matrix elements in the Bloch basis for band 1, 4,
5 and 8.

In contrast,

    LOCALIZED_BASIS = MLWF
    NTARGET_STATES = 1 4 5 8 

evaluates the Coulomb matrix elements in the [Wannier
basis](../incar-tags/LWANNIER90.md) for the states 1, 4, 5 and 8
defined in the [INCAR](../input-files/INCAR.md) file or read from the
[WANPROJ](../input-files/WANPROJ.md) file.

## Related tags and articles
[ALGO](../incar-tags/ALGO.md),
[NCRPA_BANDS](../incar-tags/NCRPA_BANDS.md),
[NTARGET_STATES](../incar-tags/NTARGET_STATES.md),
[LOCPROJ](../incar-tags/LOCPROJ.md), [VIJKL](../output-files/VIJKL.md),
[UIJKL](../output-files/UIJKL.md), [VRijkl](../output-files/VRijkl.md),
[URijkl](../output-files/URijkl.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LOCALIZED_BASIS-_incategory-Howto)

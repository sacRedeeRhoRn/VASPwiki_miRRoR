<!-- Source: https://vasp.at/wiki/index.php/NTARGET_STATES | revid: 36496 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NTARGET_STATES
NTARGET_STATES = \[integer array\] 

Description: Controls which Wannier states are excluded in constrained
random-phase approximation. Check also
[NCRPA_BANDS](NCRPA_BANDS.md).

------------------------------------------------------------------------

This tag is effective for [`ALGO`](ALGO.md)` = CRPA` and
ignored otherwise. For instance

    NTARGET_STATES = 1 2 4 

selects the Wannier state 1, 2 and 4, where the ordering of the Wannier
states depends on the chosen basis set.

## Related tags and articles
[ALGO](ALGO.md),
[NCRPA_BANDS](NCRPA_BANDS.md),
[LOCALIZED_BASIS](../theory/LOCALIZED_BASIS.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NTARGET_STATES-_incategory-Howto)

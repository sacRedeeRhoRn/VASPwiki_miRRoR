<!-- Source: https://vasp.at/wiki/index.php/NCRPA_BANDS | revid: 35239 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NCRPA_BANDS
NCRPA_BANDS = \[integer array\] 

Description: Controls which bands are excluded in the constrained
random-phase approximation. Check also
[NTARGET_STATES](NTARGET_STATES.md).

------------------------------------------------------------------------

This tag is effective for [`ALGO`](ALGO.md)` = CRPA` and
ignored otherwise.

For instance

    NCRPA_BANDS = 21 22 23 

removes all screening effects between bands 21, 22 and 23 from the
constrained random-phase approximation of the screened Coulomb
interaction.

## Related tags and articles
[ALGO](ALGO.md),
[NTARGET_STATES](NTARGET_STATES.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NCRPA_BANDS-_incategory-Howto)

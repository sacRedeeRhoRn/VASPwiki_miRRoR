<!-- Source: https://vasp.at/wiki/index.php/NCORE_IN_IMAGE1 | revid: 26797 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NCORE_IN_IMAGE1
NCORE_IN_IMAGE1 = \[integer\]  
Default: **NCORE_IN_IMAGE1** = 0 

Description: This tag specifies the number of cores in the first image.

------------------------------------------------------------------------

This tag works for two images, specifically, if
[VCAIMAGES](VCAIMAGES.md) is set (this also sets
[IMAGES](IMAGES.md)=2).
[VCAIMAGES](VCAIMAGES.md) splits the available cores into
two groups both working independently in the subdirectories 01 and 02.
The tag NCORE_IN_IMAGE1 defines how many of cores are used for the first
image (01). The remainder of the cores is used for the second image
(working in the subdirectory 02).

## Related tags and articles
[VCAIMAGES](VCAIMAGES.md),
[IMAGES](IMAGES.md), [SCALEE](SCALEE.md)

------------------------------------------------------------------------

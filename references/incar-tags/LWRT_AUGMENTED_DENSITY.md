<!-- Source: https://vasp.at/wiki/index.php/LWRT_AUGMENTED_DENSITY | revid: 34639 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWRT_AUGMENTED_DENSITY
LWRT_AUGMENTED_DENSITY = .TRUE. \| .FALSE.  
Default: **LWRT_AUGMENTED_DENSITY** = .TRUE. 

  
Description: Switch for [WRT_DENSITY](WRT_DENSITY.md)
to write without augmentation (compensation charge=0).

------------------------------------------------------------------------

With `LWRT_AUGMENTED_DENSITY`` = F` the densities can be written without
augmentation (compensation charge=0). Mind that the augmented densities
are still used during [electronic
minimization](../redirects/Electronic_minimization.md)
to evaluate the [XC functional](../redirects/XC_functional.md)
(unlike for the [MGGA](METAGGA.md) specific tag
[LNOAUGXC](LNOAUGXC.md)).

## Related tags and articles
[WRT_DENSITY](WRT_DENSITY.md),
[ENCUT](ENCUT.md), [NGXF](NGXF.md),
[NGYF](NGYF.md), [NGZF](NGZF.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWRT_AUGMENTED_DENSITY-_incategory-HowTo)

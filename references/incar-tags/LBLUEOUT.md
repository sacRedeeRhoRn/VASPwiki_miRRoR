<!-- Source: https://vasp.at/wiki/index.php/LBLUEOUT | revid: 36167 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LBLUEOUT
LBLUEOUT = .TRUE.\|.FALSE.  
Default: **LBLUEOUT** = .FALSE. 

Description: for LBLUEOUT=.TRUE., VASP writes output for the free-energy
gradient calculation to the [REPORT](../output-files/REPORT.md) file (in
case VASP was compiled with
[-Dtbdyn](../redirects/Precompiler_flags.md)).

------------------------------------------------------------------------

If LBLUEOUT=.TRUE., the information needed to compute the free-energy
gradient is written in the [REPORT](../output-files/REPORT.md) file after
each molecular-dynamics step ([MDALGO](MDALGO.md)=1 \| 2),
check the lines after the header:

    >Blue_moon
           lambda         |z|^(-1/2)      GkT           |z|^(-1/2)*(lambda+GkT)

For the theory of the blue-moon ensemble we refer to
[here](../redirects/Blue-moon_ensemble.md).

## Related tags and articles
[IBRION](IBRION.md), [MDALGO](MDALGO.md),
[ICONST](../input-files/ICONST.md), [Blue-moon
ensemble](../redirects/Blue-moon_ensemble.md), [Slow-growth
approach](../theory/Slow-growth_approach.md)

[Constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LBLUEOUT-_incategory-Examples)

------------------------------------------------------------------------

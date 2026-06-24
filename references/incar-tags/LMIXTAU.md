<!-- Source: https://vasp.at/wiki/index.php/LMIXTAU | revid: 29384 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMIXTAU
LMIXTAU = .TRUE. \| .FALSE.  
Default: **LMIXTAU** = .FALSE. 

Description: send the kinetic-energy density through the [density
mixer](../redirects/Density_mixing.md) as well.

------------------------------------------------------------------------

In many cases, the [density-mixing
scheme](../redirects/Density_mixing.md) works well enough without
passing the kinetic-energy density through the mixer. Therefore VASP
uses LMIXTAU=.FALSE. per default. However, when the self-consistency
cycle fails to converge for one of the algorithms exploiting [density
mixing](../redirects/Density_mixing.md), e.g,
[IALGO](IALGO.md)=38 or 48, we recommend setting
LMIXTAU=.TRUE..

## Related tags and articles
[METAGGA](METAGGA.md), [LMAXTAU](LMAXTAU.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMIXTAU-_incategory-Examples)

------------------------------------------------------------------------

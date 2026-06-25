<!-- Source: https://vasp.at/wiki/index.php/LBLUEOUT | revid: 36167 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LBLUEOUT


LBLUEOUT = .TRUE.\|.FALSE.  
Default: **LBLUEOUT** = .FALSE. 

Description: for
LBLUEOUT=.TRUE., VASP writes
output for the free-energy gradient calculation to the
[REPORT](../output-files/REPORT.md) file (in case VASP was compiled with
<a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">-Dtbdyn</a>).

------------------------------------------------------------------------

If LBLUEOUT=.TRUE., the information needed to compute the free-energy
gradient is written in the [REPORT](../output-files/REPORT.md) file after
each molecular-dynamics step ([MDALGO](MDALGO.md)=1 \| 2),
check the lines after the header:

    >Blue_moon
           lambda         |z|^(-1/2)      GkT           |z|^(-1/2)*(lambda+GkT)

For the theory of the blue-moon ensemble we refer to
<a href="/wiki/Blue-moon_ensemble" class="mw-redirect"
title="Blue-moon ensemble">here</a>.

## Related tags and articles\[<a href="/wiki/index.php?title=LBLUEOUT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBRION](IBRION.md), [MDALGO](MDALGO.md),
[ICONST](../input-files/ICONST.md),
<a href="/wiki/Blue-moon_ensemble" class="mw-redirect"
title="Blue-moon ensemble">Blue-moon ensemble</a>, [Slow-growth
approach](../theory/Slow-growth_approach.md)

[Constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LBLUEOUT-_incategory-Examples)

------------------------------------------------------------------------



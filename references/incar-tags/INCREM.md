<!-- Source: https://vasp.at/wiki/index.php/INCREM | revid: 26809 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# INCREM


INCREM = \[real array\]  
Default: **INCREM** = 0 

Description: INCREM controls
the transformation velocity in the slow-growth approach (in case VASP
was compiled with
[-Dtbdyn](../misc/Precompiler_options.md)).

------------------------------------------------------------------------

In [slow-growth
simulations](../theory/Slow-growth_approach.md)
([MDALGO](MDALGO.md)=1 \| 2), the value of each controlled
geometric parameter with `STATUS=0` is increased by
INCREM in every simulation
step.

It must be supplied for each controlled geometric parameter for which
`STATUS=0` was specified in the [ICONST](../input-files/ICONST.md)-file.

## Related tags and articles\[<a href="/wiki/index.php?title=INCREM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[MDALGO](MDALGO.md), [ICONST](../input-files/ICONST.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-INCREM-_incategory-Examples)

------------------------------------------------------------------------



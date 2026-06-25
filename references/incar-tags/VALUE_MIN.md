<!-- Source: https://vasp.at/wiki/index.php/VALUE_MIN | revid: 16100 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VALUE_MIN


VALUE_MIN = \[real array\] 

Description: VALUE_MIN sets
the lower limits for the monitoring of geometric parameters (in case
VASP was compiled with
[-Dtbdyn](../misc/Precompiler_options.md)).

------------------------------------------------------------------------

For [MDALGO](MDALGO.md)=1 \| 2, the geometric parameters
defined in the [ICONST](../input-files/ICONST.md) file may be monitored
without being subjected to a constraint or bias potential (`STATUS=7` in
the [ICONST](../input-files/ICONST.md) file).

If all values of monitored parameters defined in the
[ICONST](../input-files/ICONST.md) file (`STATUS=7`) are smaller than
VALUE_MIN or larger than
[VALUE_MAX](VALUE_MAX.md), the simulation terminates.

Upper limits for monitored coordinates, must be supplied for each
geometric parameter in the [ICONST](../input-files/ICONST.md) file with
`STATUS=7`.

## Related tags and articles\[<a
href="/wiki/index.php?title=VALUE_MIN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VALUE_MAX](VALUE_MAX.md),
[MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VALUE_MIN-_incategory-Examples)

------------------------------------------------------------------------



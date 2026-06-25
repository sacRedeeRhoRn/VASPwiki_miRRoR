<!-- Source: https://vasp.at/wiki/index.php/Vasp.lock | revid: 27101 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# vasp.lock


The vasp.lock file is only
used in combination with [ICHARG](../incar-tags/ICHARG.md)=5. In each SCF
step before constructing the new charge density VASP checks if the
vasp.lock file is present, and
if not waits before continuing. The file is empty, and its content is
not considered in any way by VASP.

## Related tags and articles\[<a
href="/wiki/index.php?title=Vasp.lock&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ICHARG](../incar-tags/ICHARG.md), [GAMMA](GAMMA.md)



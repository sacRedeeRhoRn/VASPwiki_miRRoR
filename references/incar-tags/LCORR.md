<!-- Source: https://vasp.at/wiki/index.php/LCORR | revid: 21819 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LCORR


LCORR = \[logical\]  
Default: **LCORR** = .TRUE. 

Description: Controls whether Harris corrections are calculated or not.

------------------------------------------------------------------------

Based on the ideas of the [Harris-Foulkes
functional](../methods/Harris-Foulkes_functional.md)
it is possible to derive a correction to the forces for non fully
self-consistent calculations, we call these corrections Harris
corrections. For
LCORR=*.TRUE.* these
corrections are calculated and included in the stress-tensor and the
forces. The contributions are explicitly written to the file
[OUTCAR](../output-files/OUTCAR.md) and help to show how well forces and
stress are converged. For surfaces, the correction term might be
relatively large and testing has shown that the corrected forces
converge much faster to the exact forces than uncorrected forces.

## Related tags and articles\[<a href="/wiki/index.php?title=LCORR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Harris-Foulkes
functional](../methods/Harris-Foulkes_functional.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LCORR-_incategory-Examples)

------------------------------------------------------------------------



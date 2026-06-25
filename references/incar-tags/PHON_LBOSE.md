<!-- Source: https://vasp.at/wiki/index.php/PHON_LBOSE | revid: 33380 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PHON_LBOSE


PHON_LBOSE = \[logical\]  
Default: **PHON_LBOSE** = .TRUE. 

Description: Determines whether structures in the sampling are created
according to Bose-Einstein or Maxwell-Boltzmann statistics.

------------------------------------------------------------------------

For PHON_LBOSE=*.TRUE.*
Bose-Einstein statistics is used.

For PHON_LBOSE=*.FALSE.*
Maxwell-Boltzmann statistics is used.

For further usage of this tag see: [Electron-phonon interactions from
Monte-Carlo
sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md).

  

|  |
|----|
| **Warning:** This tag does not work together with [PHON_NSTRUCT](PHON_NSTRUCT.md)=0. |

  

|  |
|----|
| **Mind:** This feature is available for VASP \>= 6.0. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PHON_LBOSE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Electron-phonon interactions from Monte-Carlo
sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md),
[PHON_LMC](PHON_LMC.md),
[PHON_NSTRUCT](PHON_NSTRUCT.md),
[PHON_TLIST](PHON_TLIST.md),
[TEBEG](TEBEG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PHON_LBOES-_incategory-Examples)

------------------------------------------------------------------------



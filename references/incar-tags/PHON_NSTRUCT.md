<!-- Source: https://vasp.at/wiki/index.php/PHON_NSTRUCT | revid: 33381 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PHON_NSTRUCT


PHON_NSTRUCT = \[integer\]  
Default: **PHON_NSTRUCT** = none 

Description: Sets the number of structures for electron-phonon
interactions from Monte-Carlo (MC) sampling.

------------------------------------------------------------------------

For PHON_NSTRUCT=-1 the
eigenvalues and eigenvectors of the dynamic matrix are written to the
file [DYNMATFULL](../input-files/DYNMATFULL.md).

For PHON_NSTRUCT=0 the ZG
configuration[^zacharias:prb:2016-1]
(one-shot) method is executed.

For PHON_NSTRUCT\>0 that many
MC structures are prepared.

For further usage of this tag see: [Electron-phonon interactions from
Monte-Carlo
sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md).

|  |
|----|
| **Mind:** This feature is available for VASP \>= 6.0. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PHON_NSTRUCT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Electron-phonon interactions from Monte-Carlo
sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md),
[PHON_LMC](PHON_LMC.md),
[PHON_LBOSE](PHON_LBOSE.md),
[PHON_TLIST](PHON_TLIST.md),
[TEBEG](TEBEG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PHON_NSTRUCT-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=PHON_NSTRUCT&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^zacharias:prb:2016-1]: [M. Zacharias and F. Giustino, Phys. Rev. B **94**, 075125 (2016).](https://doi.org/10.1103/PhysRevB.94.075125)

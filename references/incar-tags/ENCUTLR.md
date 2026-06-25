<!-- Source: https://vasp.at/wiki/index.php/ENCUTLR | revid: 27959 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENCUTLR


ENCUTLR = \[real\]  
Default: **ENCUTLR** = 50 eV 

Description: Reciprocal space cutoff for the treatment of the long-range
contribution.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Similar to the [treatment of the long-range part of the
force-constants](../theory/Phonons-_Theory.md) "Phonons: Theory"),
the potential and the PAW strengths also require a special
treatment[^engel:prb:2022-1]
in polar materials. The correction scheme involves an Ewald summation
over reciprocal lattice vectors that converges rapidly in reciprocal
space. ENCUTLR controls the
number of G-vectors included in the Ewald sum in the same way as
[ENCUT](ENCUT.md) controls the number of G-vectors
(plane-wave components) of the electronic Kohn-Sham orbitals.

## Related tags and articles\[<a href="/wiki/index.php?title=ENCUTLR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [IFC_LR](IFC_LR.md)
- [ELPH_LR](ELPH_LR.md)
- [PHON_G_CUTOFF](PHON_G_CUTOFF.md)

## References\[<a href="/wiki/index.php?title=ENCUTLR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^engel:prb:2022-1]: [M. Engel, H. Miranda, L. Chaput, A. Togo, C. Verdi, M. Marsman, and G. Kresse, *Zero-point renormalization of the band gap of semiconductors and insulators using the projector augmented wave method*, Phys. Rev. B **106**, 094316 (2022).](https://link.aps.org/doi/10.1103/PhysRevB.106.094316)

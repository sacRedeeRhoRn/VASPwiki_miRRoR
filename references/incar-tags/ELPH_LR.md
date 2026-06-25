<!-- Source: https://vasp.at/wiki/index.php/ELPH_LR | revid: 32879 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_LR


ELPH_LR = \[integer\]  
Default: **ELPH_LR** = 1 

Description: Controls the treatment of the long-range part of the
electron-phonon potential.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This tag controls the treatment of the long-range electrostatic
contributions to the electron-phonon coupling arising in polar
dielectric materials.

|  |
|----|
| **Mind:** In this case, the required Born effective charges and dielectric tensor are read from the [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md) file. |

## Modes\[<a href="/wiki/index.php?title=ELPH_LR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Modes">edit</a> \| (./index.php.md)\]

`ELPH_LR`` ≤ 0`  
No long-range correction scheme is applied to the electron-phonon
coupling. This is most likely very inaccurate for semiconductors and
insulators with non-vanishing Born effective charge.

`ELPH_LR`` = 1`  
Dipole corrections are applied to the electron-phonon
coupling<sup>[\[1\]](#cite_note-engel:prb:2022-1)</sup>.

## Related tags and articles\[<a href="/wiki/index.php?title=ELPH_LR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [IFC_LR](IFC_LR.md)

## References\[<a href="/wiki/index.php?title=ELPH_LR&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-engel:prb:2022_1-0)
    <a href="https://link.aps.org/doi/10.1103/PhysRevB.106.094316"
    class="external text" rel="nofollow">M. Engel, H. Miranda, L. Chaput, A.
    Togo, C. Verdi, M. Marsman, and G. Kresse, <em>Zero-point
    renormalization of the band gap of semiconductors and insulators using
    the projector augmented wave method</em>, Phys. Rev. B
    <strong>106</strong>, 094316 (2022).</a>



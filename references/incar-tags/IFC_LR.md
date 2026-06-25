<!-- Source: https://vasp.at/wiki/index.php/IFC_LR | revid: 32877 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IFC_LR


IFC_LR = \[integer\]  
Default: **IFC_LR** = 1 

Description: Controls the treatment of the long-range part of the
interatomic force constants during electron-phonon calculations.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This tag controls the treatment of the [long-range electrostatic
contributions to the interatomic force constants
(IFC)](../theory/Phonons-_Theory.md)
arising in polar dielectric materials.
`IFC_LR`` = 1` has the same
effect as [`LPHON_POLAR`](LPHON_POLAR.md)` = True` but
is used in the context of electron-phonon interactions.

|  |
|----|
| **Mind:** In this case, the required Born effective charges and dielectric tensor are read from the [phelel_params.hdf5](../input-files/Phelel_params.hdf5.md) file. |

## Modes\[<a href="/wiki/index.php?title=IFC_LR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Modes">edit</a> \| (./index.php.md)\]

`IFC_LR`` ≤ 0`  
No long-range correction scheme is applied to the IFC matrix. This is
most likely very inaccurate for semiconductors and insulators with
non-vanishing Born effective charge.

`IFC_LR`` = 1`  
Dipole corrections are applied to the IFC matrix.

## Related tags and articles\[<a href="/wiki/index.php?title=IFC_LR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_LR](ELPH_LR.md)



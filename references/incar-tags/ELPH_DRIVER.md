<!-- Source: https://vasp.at/wiki/index.php/ELPH_DRIVER | revid: 33359 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_DRIVER


ELPH_DRIVER = el \| mels  
Default: **ELPH_DRIVER** = el 

Description: Chooses which driver to use for electron-phonon
calculations.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

|  |
|----|
| **Warning:** There was a [known issue](../misc/Known_issues.md) for electron-phonon calculations using [`ISPIN`](ISPIN.md)` = 2` for VASP 6.5.0 and 6.5.1 that was fixed in VASP 6.6.0. |

------------------------------------------------------------------------

This is a high-level tag that chooses what to compute during an
electron-phonon calculation. Currently, the following drivers are
supported:

`ELPH_DRIVER`` = el`  
Computes the phonon-induced electron self-energy. This can be used to
compute the [renormalization of the electronic band
structure](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
and [electronic transport
properties](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

`ELPH_DRIVER`` = mels`  
Computes the electron-phonon matrix elements and writes them to the
[vaspelph.h5](../output-files/Vaspelph.h5.md) file. For performance
reasons, it is usually not recommended to write the matrix elements and
process them externally. However, this mode is still useful for
analyzing or plotting the matrix elements directly.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_DRIVER&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_DECOMPOSE](ELPH_DECOMPOSE.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)



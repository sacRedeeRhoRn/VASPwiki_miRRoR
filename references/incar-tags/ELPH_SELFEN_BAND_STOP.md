<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_BAND_STOP | revid: 27931 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_BAND_STOP


ELPH_SELFEN_BAND_STOP =
\[real\]  
Default: **ELPH_SELFEN_BAND_STOP** =
[ELPH_NBANDS](ELPH_NBANDS.md) 

Description: Compute the electron self-energy due to electron-phonon
coupling only for bands with indices until
ELPH_SELFEN_BAND_STOP.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This tag can be used in combination with
[ELPH_SELFEN_KPTS](ELPH_SELFEN_KPTS.md),
[ELPH_SELFEN_IKPT](ELPH_SELFEN_IKPT.md) or
[ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)
to limit the calculation of the electron-phonon self-energy to a
particular set of **k**-points and bands.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_BAND_STOP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_GAPS](ELPH_SELFEN_GAPS.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_KPTS](ELPH_SELFEN_KPTS.md)
- [ELPH_SELFEN_IKPT](ELPH_SELFEN_IKPT.md)
- [ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)



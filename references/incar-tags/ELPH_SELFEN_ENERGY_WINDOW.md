<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_ENERGY_WINDOW | revid: 32913 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_ENERGY_WINDOW


ELPH_SELFEN_ENERGY_WINDOW =
\[real, real\]  
Default: **ELPH_SELFEN_ENERGY_WINDOW** = 0.0 0.0 

Description: Specifies the energy window (in eV) around the band edges
within which the electron-phonon self-energy is computed.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The self-energy is evaluated for electronic states with energies in the
intervals around the valence band minimum (VBM) and the conduction band
minimum (CDM), with an energy window defined with
`ELPH_SELFEN_ENERGY_WINDOW`` = `*`a`*` `*`b`*:

- from VBM – *a* up to VBM, and
- from CBM up to CBM + *b*

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_ENERGY_WINDOW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_SCATTERING_APPROX](ELPH_SCATTERING_APPROX.md)
- [ELPH_SELFEN_IMAG_SKIP](ELPH_SELFEN_IMAG_SKIP.md)



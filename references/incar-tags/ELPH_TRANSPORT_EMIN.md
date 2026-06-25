<!-- Source: https://vasp.at/wiki/index.php/ELPH_TRANSPORT_EMIN | revid: 27944 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_TRANSPORT_EMIN


ELPH_TRANSPORT_EMIN =
\[real\] 

Description: Lower bound of the energy window in which states are
considered for transport calculations.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

In transport calculations, only a small amount of electronic states
around the chemical potential have a sizeable contribution. Therefore,
in order to improve performance, only states inside an energy window
centered around the chemical potential are considered during the
calculation. By default, the location and width of the energy window are
determined automatically by VASP. By setting
ELPH_TRANSPORT_EMIN and
[ELPH_TRANSPORT_EMAX](ELPH_TRANSPORT_EMAX.md),
one can control the energy window manually.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_TRANSPORT_EMIN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_TRANSPORT_EMAX](ELPH_TRANSPORT_EMAX.md)



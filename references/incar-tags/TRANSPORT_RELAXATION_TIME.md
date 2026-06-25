<!-- Source: https://vasp.at/wiki/index.php/TRANSPORT_RELAXATION_TIME | revid: 32865 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TRANSPORT_RELAXATION_TIME


TRANSPORT_RELAXATION_TIME =
\[real\]  
Default: **TRANSPORT_RELAXATION_TIME** = 1E-14 

Description: Value of the constant relaxation time in unit of seconds.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This value is only used when
[`ELPH_SCATTERING_APPROX`](ELPH_SCATTERING_APPROX.md)` = CRTA`,
so for the constant relaxation-time approximation.

## Related tags and articles\[<a
href="/wiki/index.php?title=TRANSPORT_RELAXATION_TIME&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_SCATTERING_APPROX](ELPH_SCATTERING_APPROX.md)



<!-- Source: https://vasp.at/wiki/index.php/ELPH_TRANSPORT | revid: 32891 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_TRANSPORT


ELPH_TRANSPORT = \[logical\]  
Default: **ELPH_TRANSPORT** = .FALSE. 

Description: Activates transport calculation involving electron-phonon
coupling

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

When
`ELPH_TRANSPORT`` = True`,
VASP calculates the transport coefficients from the linearized Boltzmann
transport equation. In this framework, the transport coefficients are
calculated from various relaxation-time approximations selectable via
[ELPH_SCATTERING_APPROX](ELPH_SCATTERING_APPROX.md).
A convenient way to start transport calculations is to set
[`ELPH_MODE`](ELPH_MODE.md)` = transport`, which
automatically provides reasonable default values for the required
[INCAR](../input-files/INCAR.md) tags.

For more information, visit the how-to page on [transport
calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_TRANSPORT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_MODE](ELPH_MODE.md)
- [ELPH_SCATTERING_APPROX](ELPH_SCATTERING_APPROX.md)
- [ELPH_TRANSPORT_DRIVER](ELPH_TRANSPORT_DRIVER.md)



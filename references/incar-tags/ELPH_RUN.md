<!-- Source: https://vasp.at/wiki/index.php/ELPH_RUN | revid: 32867 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_RUN
ELPH_RUN = \[logical\]  
Default: **ELPH_RUN** = .false. 

Description: Select whether to run and electron-phonon calculation.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This flag determined whether an electron-phonon calculation should be
performed. The most fundamental quantity we compute are the
electron-phonon matrix elements.

These can simply be written to file when
[`ELPH_DRIVER`](ELPH_DRIVER.md)` = MELS` for further
post-processing. Additionally, one can directly use these matrix
elements to compute the electron self-energy due to electron-phonon
coupling [`ELPH_DRIVER`](ELPH_DRIVER.md)` = EL`. The
self-energy can in turn be used to compute the [renormalization of the
electronic
bandstructure](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
or [transport coefficients involving electron-phonon
scattering](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

Additionally, the tag [ELPH_MODE](ELPH_MODE.md) sets
defaults for other [INCAR](../input-files/INCAR.md) tags depending on the
quantities of interest.

## Related tags and articles
- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Chemical potential in electron-phonon
  interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_MODE](ELPH_MODE.md)
- [ELPH_DRIVER](ELPH_DRIVER.md)

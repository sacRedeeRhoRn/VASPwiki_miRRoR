<!-- Source: https://vasp.at/wiki/index.php/ELPH_MODE | revid: 32938 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_MODE
ELPH_MODE = \[string\] 

Description: Meta tag that selects reasonable defaults for
electron-phonon calculations

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The required [INCAR](../input-files/INCAR.md) settings for electron-phonon
calculations depend on the type of calculation. For example, computing
the [renormalization of the electronic band
structure](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
requires a different set of options than computing [transport
properties](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).
The ELPH_MODE tag can help you get started with electron-phonon
calculations by selecting reasonable default values for other
[INCAR](../input-files/INCAR.md) tags based on the type of calculation.

The individual tags that are set by ELPH_MODE can still be overwritten
by specifying them explicitly in the [INCAR](../input-files/INCAR.md) file.

## Contents

- [1 Tag options](#Tag_options)
  - [1.1 ELPH_MODE = renorm - Band-gap
    renormalization](#ELPH_MODE_=_renorm_-_Band-gap_renormalization)
  - [1.2 ELPH_MODE = transport - Transport
    calculation](#ELPH_MODE_=_transport_-_Transport_calculation)
- [2 Related tags and articles](#Related_tags_and_articles)

## Tag options
### `ELPH_MODE`` = renorm` - Band-gap renormalization
- [`ELPH_RUN`](ELPH_RUN.md)` = True`
- [`ELPH_SELFEN_FAN`](ELPH_SELFEN_FAN.md)` = True`
- [`ELPH_SELFEN_DW`](ELPH_SELFEN_DW.md)` = True`
- [`ELPH_SELFEN_GAPS`](ELPH_SELFEN_GAPS.md)` = True`
- [`ELPH_NBANDS`](ELPH_NBANDS.md)` = -2`
- [`ELPH_SELFEN_DELTA`](ELPH_SELFEN_DELTA.md)` = 0.01`

### `ELPH_MODE`` = transport` - Transport calculation
- [`ELPH_RUN`](ELPH_RUN.md)` = True`
- [`ELPH_TRANSPORT`](ELPH_TRANSPORT.md)` = True`
- [`ELPH_SELFEN_FAN`](ELPH_SELFEN_FAN.md)` = True`
- [`ELPH_SELFEN_DW`](ELPH_SELFEN_DW.md)` = False`
- [`ELPH_SCATTERING_APPROX`](ELPH_SCATTERING_APPROX.md)` = serta mrta_lambda`
- [`ELPH_SELFEN_CARRIER_DEN`](ELPH_SELFEN_CARRIER_DEN.md)` = -1e21 -1e20 -1e19 -1e18 -1e17 -1e16 0 1e16 1e17 1e18 1e19 1e20 1e21`
- [`ELPH_SELFEN_DELTA`](ELPH_SELFEN_DELTA.md)` = 0`
- [`ELPH_SELFEN_IMAG_SKIP`](ELPH_SELFEN_IMAG_SKIP.md)` = True`
- [`ELPH_SELFEN_BROAD_TOL`](ELPH_SELFEN_BROAD_TOL.md)` = 1e-4`
- [`ELPH_WF_REDISTRIBUTE`](ELPH_WF_REDISTRIBUTE.md)` = True`

## Related tags and articles
- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_TRANSPORT_DRIVER](ELPH_TRANSPORT_DRIVER.md)
- [ELPH_DRIVER](ELPH_DRIVER.md)

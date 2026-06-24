<!-- Source: https://vasp.at/wiki/index.php/ELPH_NBANDS | revid: 31108 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_NBANDS
ELPH_NBANDS = \[integer\]  
Default: **ELPH_NBANDS** = [NBANDS](NBANDS.md) 

Description: Number of bands to compute on the dense **k** point grid
for the electron-phonon driver

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

For [transport
calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md),
this value should be as little as possible while including all the
states potentially participating in the transport calculation.

If ELPH_NBANDS=-2 then the number of bands is set to the maximum number
of plane waves. This setting is particularly useful for calculating the
[bandgap
renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md).
In this case, the final result converges slowly with the number of bands
in the calculation, similar to
[RPA](../methods/RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md),
and [BSE](../redirects/BSE_calculations.md) calculations.

## Related tags and articles
- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_NBANDS_SUM](ELPH_NBANDS_SUM.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)

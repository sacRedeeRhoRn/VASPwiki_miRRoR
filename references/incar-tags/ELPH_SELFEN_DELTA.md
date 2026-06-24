<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_DELTA | revid: 27934 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_DELTA
ELPH_SELFEN_DELTA = \[real array\]  
Default: **ELPH_SELFEN_DELTA** = 0.01 

Description: Complex imaginary shift to use when computing the
self-energy due to electron-phonon coupling.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

If the value is set to 0.0 then the tetrahedron method is used to
perform the Brillouin zone integrals and evaluate only the imaginary
part of the electron self-energy. This is the recommended option for
[transport
calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

For [bandgap
renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
since one is mainly interested in the real part of the self-energy due
to electron-phonon coupling, a small finite value should be used and a
dense **k** point mesh used.

If more than one value is specified, the number of self-energy
accumulators is increased such that one exists for each value in this
array. It is possible to compute the self-energy using the tetrahedron
method and a finite complex shift in the same run.

## Related tags and articles
- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_GAPS](ELPH_SELFEN_GAPS.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_STATIC](ELPH_SELFEN_STATIC.md)

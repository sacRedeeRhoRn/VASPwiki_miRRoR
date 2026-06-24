<!-- Source: https://vasp.at/wiki/index.php/TRANSPORT_NEDOS | revid: 32984 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TRANSPORT_NEDOS
TRANSPORT_NEDOS = \[integer\]  
Default: **TRANSPORT_NEDOS** = 501 

Description: Choose the number of points in the Gauss-Legendre
integration grid for the computation of the Onsager coefficients, which
in turn are used to compute the transport coefficients.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

By a variable change in the integral of the transport function, it is
possible to use Gauss-Legendre quadrature to evaluate the Onsager
coefficients. By increasing the number of points, one defines the energy
window inside which we need to compute the electron group velocities and
the electronic lifetimes due to electron-phonon coupling and the
precision of the integral.

A convergence study is recommended since having a very large number of
integration points can greatly increase the number of states for which
the electronic lifetimes need to be computed, sometimes without a
significant change in the final transport coefficients. Lower values of
the number of integration points can significantly speed up the
calculation, especially for very dense grids.

|  |
|----|
| **Mind:** **ELPH_TRANSPORT_NEDOS** is a valid alternative way of writing this tag. |

## Related tags and articles
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_TRANSPORT_DRIVER](ELPH_TRANSPORT_DRIVER.md)
- [ELPH_FERMI_NEDOS](ELPH_FERMI_NEDOS.md)

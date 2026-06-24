<!-- Source: https://vasp.at/wiki/index.php/ELPH_TRANSPORT_DFERMI_TOL | revid: 32753 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_TRANSPORT_DFERMI_TOL
ELPH_TRANSPORT_DFERMI_TOL = \[real\]  
Default: **ELPH_TRANSPORT_DFERMI_TOL** = 1e-6 

Description: choose the fraction of the integral weight of the
derivative of the Fermi–Dirac distribution that is excluded when
defining the energy window for the Onsager coefficients. Must be between
0 and 1, and is only used when
[ELPH_TRANSPORT_DRIVER](ELPH_TRANSPORT_DRIVER.md)=1.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Using this parameter,
[ELPH_TRANSPORT_EMIN](ELPH_TRANSPORT_EMIN.md)
and
[ELPH_TRANSPORT_EMAX](ELPH_TRANSPORT_EMAX.md)
are automatically computed from the chemical potentials and the
distribution $-\partial f^0/\partial \epsilon$. Formally, the integration window $\[\mu-e,\mu+e\]$ is chosen such that

$\int_{\mu-e}^{\mu+e} \left(-\frac{\partial
f^0}{\partial \epsilon}\right) d\epsilon = 1 - \alpha,$

where $\alpha \equiv$
ELPH_TRANSPORT_DFERMI_TOL. This gives

$e = k_B T \\
\ln\\\left(\tfrac{2-\alpha}{\alpha}\right).$

A small value means that only the tails of the derivative of the
Fermi-dirac distribution are excluded from the integral. A large value
means that only a small energy window around the chemical potential is
used.

The integral is then discretized with a number of energy points set by
[TRANSPORT_NEDOS](TRANSPORT_NEDOS.md) and evaluated
using the Simpson's rule.

## Related tags and articles
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_TRANSPORT_DRIVER](ELPH_TRANSPORT_DRIVER.md)
- [ELPH_TRANSPORT_EMIN](ELPH_TRANSPORT_EMIN.md)
- [ELPH_TRANSPORT_EMAX](ELPH_TRANSPORT_EMAX.md)
- [TRANSPORT_NEDOS](TRANSPORT_NEDOS.md)

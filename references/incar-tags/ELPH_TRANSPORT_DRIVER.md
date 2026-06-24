<!-- Source: https://vasp.at/wiki/index.php/ELPH_TRANSPORT_DRIVER | revid: 32881 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_TRANSPORT_DRIVER
ELPH_TRANSPORT_DRIVER = \[integer\]  
Default: **ELPH_TRANSPORT_DRIVER** = 2 

Description: choose method to compute the Onsager coefficients, which
are then used to compute the transport coefficients.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The Onsager coefficients can be computed using either of the options
below, each with its own advantages and disadvantages. They are defined
as

$L_{ij} = \int d\epsilon \\ \mathcal{T}(\epsilon)
\\ (\epsilon-\mu)^{i+j-2} \left( -\frac{\partial f^0}{\partial \epsilon}
\right),$

where $\mathcal{T}(\epsilon)$ is the
[transport distribution
function](../theory/Electronic_transport_coefficients.md),
$\mu$ the [chemical
potential](../theory/Chemical_potential_in_electron-phonon_interactions.md),
and $f^0$ the Fermi–Dirac distribution.

`ELPH_TRANSPORT_DRIVER`` = 1`  
The discretized Onsager coefficient is evaluated as

$L_{ij} \\\approx\\ \sum_{k=1}^{N} w_k \\
\mathcal{T}(\epsilon_k)\\ (\epsilon_k - \mu)^{\\i+j-2}\\ \left(
-\frac{\partial f^0}{\partial \epsilon} \right).$

with $\epsilon_k =
\epsilon_\text{min}+(k-1)\Delta \epsilon,\\\\ k=1,\dots,N$
and $\Delta \epsilon =
\tfrac{\epsilon_\text{max}-\epsilon_\text{min}}{N-1}$ and
$\epsilon_\text{min}$=[ELPH_TRANSPORT_EMIN](ELPH_TRANSPORT_EMIN.md)
and $\epsilon_\text{max}$=[ELPH_TRANSPORT_EMAX](ELPH_TRANSPORT_EMAX.md)
or alternatively both $\epsilon_\text{min}$ and $\epsilon_\text{max}$
are set by
[ELPH_TRANSPORT_DFERMI_TOL](ELPH_TRANSPORT_DFERMI_TOL.md),
$w_k$ the weights due to the Simpson
integration rule and
N=[TRANSPORT_NEDOS](TRANSPORT_NEDOS.md).

`ELPH_TRANSPORT_DRIVER`` = 2`  
Use Gauss-Legendre integration to evaluate the Onsager coefficients. The
convergence of the integral can be checked by performing a convergence
study with respect to
N=[TRANSPORT_NEDOS](TRANSPORT_NEDOS.md) alone. In
this case the Onsager coefficients are evaluated using the following
discretization

$L_{ij} \\\approx\\ \tfrac{1}{2} \sum_{k=1}^N
w_k \\ \left( \frac{k_B T}{-e} \ln \frac{1+x_k}{1-x_k} \right)^{i+j-2}
\mathcal{T}\\\left(\mu + k_B T \ln\frac{1+x_k}{1-x_k}\right),$

with $w_k$ and $x_k$ the weights and abcissae of the Gauss-Legendre quadrature
rule.

## Related tags and articles
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [TRANSPORT_NEDOS](TRANSPORT_NEDOS.md)
- [ELPH_TRANSPORT_DFERMI_TOL](ELPH_TRANSPORT_DFERMI_TOL.md)
- [ELPH_TRANSPORT_EMIN](ELPH_TRANSPORT_EMIN.md)
- [ELPH_TRANSPORT_EMAX](ELPH_TRANSPORT_EMAX.md)

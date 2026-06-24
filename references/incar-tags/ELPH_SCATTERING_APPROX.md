<!-- Source: https://vasp.at/wiki/index.php/ELPH_SCATTERING_APPROX | revid: 32864 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SCATTERING_APPROX
ELPH_SCATTERING_APPROX = \[string\]  
Default: **ELPH_SCATTERING_APPROX** = SERTA MRTA_LAMBDA 

Description: Select which type of approximation is used to compute the
electron scattering lifetimes due to electron-phonon coupling

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

There are different approximations to compute the electronic lifetimes
due to electron-phonon scattering. Each of these can lead to
significantly different transport coefficients. It is possible to select
more than one approximation in ELPH_SCATTERING_APPROX. In this case,
additional [electron-phonon
accumulators](../misc/Electron-phonon_accumulators.md)
are created for each scattering approximation.

## Options to select
`ELPH_SCATTERING_APPROX`` = CRTA` - *C*onstant *R*elaxation-*T*ime *A*pproximation  
The relaxation time is assumed constant. It needs to be specified via
[TRANSPORT_RELAXATION_TIME](TRANSPORT_RELAXATION_TIME.md).
In this case, the computation of electron-phonon matrix elements is
skipped entirely, which is a huge performance boost compared to the
other relaxation-time approximations.

|  |
|----|
| **Warning:** While the CRTA can be a reasonable approximation for metals, it will generally fail for insulators. |

`ELPH_SCATTERING_APPROX`` = SERTA` - *S*elf-*E*nergy *R*elaxation-*T*ime *A*pproximation  
Computes the relaxation time from the imaginary part of the Fan
self-energy, evaluated on the electronic eigenenergy:

$\frac{1}{\tau^{\mathrm{SERTA}}_{n\mathbf{k}}} =
\frac{2\pi}{\hbar} \sum_{n'\nu\mathbf{k}'}
w_{n\mathbf{k},n'\mathbf{k}'} \\
|g^{\nu}_{n\mathbf{k},n'\mathbf{k}'}|^2 \left\[ (n_{\nu\mathbf{q}} +
1 - f_{n'\mathbf{k}'}) \\ \delta(\varepsilon_{n\mathbf{k}} -
\varepsilon_{n'\mathbf{k}'} - \hbar\omega_{\nu\mathbf{q}}) +
(n_{\nu\mathbf{q}} + f_{n'\mathbf{k}'}) \\
\delta(\varepsilon_{n\mathbf{k}} - \varepsilon_{n'\mathbf{k}'} +
\hbar\omega_{\nu\mathbf{q}}) \right\]$

where ${\tau^{\mathrm{SERTA}}_{n\mathbf{k}}}$ is the relaxation time (or scattering time, or lifetime) for
state $(n,\mathbf{k})$,
$w_{n\mathbf{k},n'\mathbf{k}'}$ is the
scattering weight, $g^{\nu}_{n\mathbf{k},n'\mathbf{k}'}$ is the electron-phonon
coupling matrix element, $f_{n\mathbf{k}}$ is the population of the electronic state (Fermi-Dirac
distribution), $n_{\nu\mathbf{q}}$ is
the population of the phononic state (Bose-Einstein distribution),
$\varepsilon_{n\mathbf{k}}$ is the
energy of an electron band, $\omega_{\nu\mathbf{q}}$ is the phonon frequency, and
$\delta$ is the Dirac delta function.

For SERTA, the scattering weight is:

$w_{n\mathbf{k},n'\mathbf{k}'} = 1$

`ELPH_SCATTERING_APPROX`` = ERTA_LAMDBA` - *E*nergy *R*elaxation-*T*ime *A*pproximation (mean-free path approximation)  
Applies an energy-projected weight scaled by mean-free path (where
$\mu$ is the [chemical
potential](../theory/Chemical_potential_in_electron-phonon_interactions.md)):

$w_{n\mathbf{k},n'\mathbf{k}'} = \left(1 -
\frac{\mathbf{v}_{n\mathbf{k}} \cdot
\mathbf{v}_{n'\mathbf{k}'}}{|\mathbf{v}_{n\mathbf{k}}|
|\mathbf{v}_{n'\mathbf{k}'}|} \left|
\frac{\varepsilon_{n'\mathbf{k}'} - \mu}{\varepsilon_{n\mathbf{k}} -
\mu} \right|\right)$

[TABLE]

`ELPH_SCATTERING_APPROX`` = ERTA_TAU ` - *E*nergy *R*elaxation-*T*ime *A*pproximation (lifetime approximation)  
$w_{n\mathbf{k},n'\mathbf{k}'} = \left(1 -
\frac{\mathbf{v}_{n\mathbf{k}} \cdot
\mathbf{v}_{n'\mathbf{k}'}}{|\mathbf{v}_{n\mathbf{k}}|^2} \left|
\frac{\varepsilon_{n'\mathbf{k}'} - \mu}{\varepsilon_{n\mathbf{k}} -
\mu} \right|\right)$

[TABLE]

`ELPH_SCATTERING_APPROX`` = MRTA_LAMDBA` - *M*omentum *R*elaxation-*T*ime *A*pproximation (mean-free path approximation)  
$w_{n\mathbf{k},n'\mathbf{k}'} = \left(1 -
\frac{\mathbf{v}_{n\mathbf{k}} \cdot
\mathbf{v}_{n'\mathbf{k}'}}{|\mathbf{v}_{n\mathbf{k}}|
|\mathbf{v}_{n'\mathbf{k}'}|}\right)$

&nbsp;

`ELPH_SCATTERING_APPROX`` = MRTA_TAU ` - *M*omentum *R*elaxation-*T*ime *A*pproximation (lifetime approximation)  
$w_{n\mathbf{k},n'\mathbf{k}'} = \left(1 -
\frac{\mathbf{v}_{n\mathbf{k}} \cdot
\mathbf{v}_{n'\mathbf{k}'}}{|\mathbf{v}_{n\mathbf{k}}|^2}\right)$

## Related tags and articles
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Electronic transport
  coefficients](../theory/Electronic_transport_coefficients.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_TRANSPORT_DRIVER](ELPH_TRANSPORT_DRIVER.md)
- [TRANSPORT_RELAXATION_TIME](TRANSPORT_RELAXATION_TIME.md)

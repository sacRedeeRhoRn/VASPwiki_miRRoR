<!-- Source: https://vasp.at/wiki/index.php/ELPH_TRANSPORT_EMAX_PLOT | revid: 32962 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_TRANSPORT_EMAX_PLOT
ELPH_TRANSPORT_EMAX_PLOT = \[real\]  
Default: **ELPH_TRANSPORT_EMAX_PLOT** = $\max(\varepsilon_{n\mathbf{k}})$+5 

Description: Specifies the maximum energy (in eV) to be considered when
computing the [transport distribution
function](../theory/Electronic_transport_coefficients.md)
for plotting.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

By default, the upper energy limit is set to $\max(\varepsilon_{n\mathbf{k}})$ + 5 eV, where
$\varepsilon_{n\mathbf{k}}$ are the
electronic eigenvalues computed in the k-point mesh defined by the
[KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md) file. The transport
function for plotting is evaluated on a linear energy grid of energies
between
[ELPH_TRANSPORT_EMIN_PLOT](ELPH_TRANSPORT_EMIN_PLOT.md)
and ELPH_TRANSPORT_EMAX_PLOT and with
[ELPH_TRANSPORT_NEDOS_PLOT](ELPH_TRANSPORT_NEDOS_PLOT.md)
points. The transport function for plotting is computed additionally to
the one that is used to evaluate the [Onsager
coefficients](../theory/Electronic_transport_coefficients.md)
but allows choosing a different energy range, thus not compromising the
accuracy of the transport calculations.

The transport function and corresponding energy grids are written to
[vaspout.h5](../output-files/Vaspout.h5.md)

``` mw-collapsible
 $ h5ls -r vaspout.h5 | grep plot
 /results/electron_phonon/electrons/transport_1/energy_plot Dataset {501}
 /results/electron_phonon/electrons/transport_1/transport_function_plot Dataset {7, 1, 3, 3, 501}
```

## Related tags and articles
- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_TRANSPORT_EMIN_PLOT](ELPH_TRANSPORT_EMIN_PLOT.md)
- [ELPH_TRANSPORT_NEDOS_PLOT](ELPH_TRANSPORT_NEDOS_PLOT.md)
- [ELPH_SCATTERING_APPROX](ELPH_SCATTERING_APPROX.md)
- [TRANSPORT_RELAXATION_TIME](TRANSPORT_RELAXATION_TIME.md)

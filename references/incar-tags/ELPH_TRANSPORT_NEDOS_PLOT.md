<!-- Source: https://vasp.at/wiki/index.php/ELPH_TRANSPORT_NEDOS_PLOT | revid: 32965 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_TRANSPORT_NEDOS_PLOT


ELPH_TRANSPORT_NEDOS_PLOT =
\[integer\]  
Default: **ELPH_TRANSPORT_NEDOS_PLOT** = -1 

Description: Specifies the number of energy points used to sample the
[transport distribution
function](../theory/Electronic_transport_coefficients.md)
for plotting.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This parameter defines the resolution of the energy grid used to compute
and store the transport distribution function in
[vaspout.h5](../output-files/Vaspout.h5.md). The transport function for
plotting is evaluated on a linear energy grid of energies between
[ELPH_TRANSPORT_EMIN_PLOT](ELPH_TRANSPORT_EMIN_PLOT.md)
and
[ELPH_TRANSPORT_EMAX_PLOT](ELPH_TRANSPORT_EMAX_PLOT.md)
and with
ELPH_TRANSPORT_NEDOS_PLOT
points. A higher value increases the energy resolution of the plotted
transport quantities but also slightly increases the post-processing
time.

The default value of -1 means that the transport function for plotting
is not computed by default. If the number if positive (for example 501)
then it corresponds to the number of points in the dataset:

``` mw-collapsible
 $ h5ls -r vaspout.h5 | grep plot
 /results/electron_phonon/electrons/transport_1/energy_plot Dataset {501}
 /results/electron_phonon/electrons/transport_1/transport_function_plot Dataset {7, 1, 3, 3, 501}
```

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_TRANSPORT_NEDOS_PLOT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_TRANSPORT](ELPH_TRANSPORT.md)
- [ELPH_TRANSPORT_EMIN_PLOT](ELPH_TRANSPORT_EMIN_PLOT.md)
- [ELPH_TRANSPORT_EMAX_PLOT](ELPH_TRANSPORT_EMAX_PLOT.md)
- [ELPH_RUN](ELPH_RUN.md)
- [TRANSPORT_RELAXATION_TIME](TRANSPORT_RELAXATION_TIME.md)



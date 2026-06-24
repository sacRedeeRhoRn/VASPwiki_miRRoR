<!-- Source: https://vasp.at/wiki/index.php/NEDOS | revid: 27011 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NEDOS
NEDOS = \[integer\]  
Default: **NEDOS** = $301$ 

Description: Number of grid points for the electronic [density of
states](../redirects/Density_of_states.md) (DOS) and
[dielectric function](../redirects/Dielectric_function.md).

------------------------------------------------------------------------

The energy range between [EMIN](EMIN.md) and
[EMAX](EMAX.md) is divided into NEDOS intervals to obtain the
grid points. The DOS for the corresponding energy is written in the
[DOSCAR](../output-files/DOSCAR.md) file.

|  |
|----|
| **Tip:** Compare the DOS to the integrated DOS (also written on [DOSCAR](../output-files/DOSCAR.md)) to check if the default NEDOS is too small to resolve narrow peaks properly. At least one peak should show up at every step of the integrated DOS. |

The smallest peak widths from the dispersion of the respective bands can
be estimated by having a look at the Kohn-Sham eigenvalues written in
[OUTCAR](../output-files/OUTCAR.md). NEDOS has to be chosen sufficiently
large to resolve this dispersion. In addition, the energy interval
defined by [EMIN](EMIN.md) and [EMAX](EMAX.md) can
be modified.

NEDOS is also used to set the total number of frequency points when
calculating the [dielectric
function](../redirects/Dielectric_function.md).

## Related tags and articles
[EMIN](EMIN.md), [EMAX](EMAX.md),
[DOSCAR](../output-files/DOSCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NEDOS-_incategory-Examples)

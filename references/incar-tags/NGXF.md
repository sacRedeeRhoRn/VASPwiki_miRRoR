<!-- Source: https://vasp.at/wiki/index.php/NGXF | revid: 26995 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NGXF
NGXF = \[integer\]  
Default: **NGXF** = set in accordance with [PREC](PREC.md),
[NGX](NGX.md), [ENCUT](ENCUT.md) and
[ENAUG](ENAUG.md) 

Description: NGXF sets the number of grid points in the "fine" FFT grid
along the first lattice vector.

------------------------------------------------------------------------

On this "fine" FFT mesh the localized augmentation charges are
represented if ultrasoft pseudopotentials (USPPs) or the PAW method are
used. In case USPPs are used, the local potentials
(exchange-correlation, Hartree-potential and ionic potentials) are also
calculated on this "fine" FFT-mesh.

By default NGXF is set in accordance with the requested "precision" mode
[PREC](PREC.md), [NGX](NGX.md), and the plane wave
kinetic energy cutoffs [ENCUT](ENCUT.md) and
[ENAUG](ENAUG.md):

|  |  |  |
|----|:--:|:--:|
| [PREC](PREC.md) | [NGX](NGX.md) | NGXF |
| Normal | 3/2×$G_{\rm cut}$ | 2×[NGX](NGX.md) |
| Single (VASP.5) | 3/2×$G_{\rm cut}$ | [NGX](NGX.md) |
| Single (VASP.6) | 2×$G_{\rm cut}$ | [NGX](NGX.md) |
| SingleN (VASP.6) | 3/2×$G_{\rm cut}$ | [NGX](NGX.md) |
| Accurate | 2×$G_{\rm cut}$ | 2×[NGX](NGX.md) |
| Low | 3/2×$G_{\rm cut}$ | 3×$G_{\rm aug}$ |
| Medium | 3/2×$G_{\rm cut}$ | 4×$G_{\rm aug}$ |
| High | 2×$G_{\rm cut}$ | 16/3×$G_{\rm aug}$ |

where

$E_{\rm cut}=\frac{\hbar^2}{2m_e}G_{\rm cut}^2
\qquad E_{\rm aug}=\frac{\hbar^2}{2m_e}G_{\rm aug}^2$

with $E_{\rm cut}$=[ENCUT](ENCUT.md) and $E_{\rm aug}$=[ENAUG](ENAUG.md).

Alternatively, NGXF can be set to a specific value in the
[INCAR](../input-files/INCAR.md) file.

## Related tags and articles
[NGX](NGX.md), [NGY](NGY.md), [NGZ](NGZ.md),
[NGYF](NGYF.md), [NGZF](NGZF.md),
[PREC](PREC.md), [ENCUT](ENCUT.md),
[ENAUG](ENAUG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NGXF-_incategory-Examples)

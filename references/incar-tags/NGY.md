<!-- Source: https://vasp.at/wiki/index.php/NGY | revid: 26991 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NGY
NGY = \[integer\]  
Default: **NGY** = set in accordance with [PREC](PREC.md) and
[ENCUT](ENCUT.md) 

Description: NGY sets the number of grid points in the FFT grid along
the second lattice vector.

------------------------------------------------------------------------

By default NGY is set in accordance with the requested "precision" mode
[PREC](PREC.md) and the plane wave kinetic energy cutoff
[ENCUT](ENCUT.md):

|  |  |
|----|:--:|
| [PREC](PREC.md) | NGY |
| Normal | 3/2×$G_{\rm cut}$ |
| Single (VASP.5) | 3/2×$G_{\rm cut}$ |
| Single (VASP.6) | 2×$G_{\rm cut}$ |
| SingleN (VASP.6) | 3/2×$G_{\rm cut}$ |
| Accurate | 2×$G_{\rm cut}$ |
| Low | 3/2×$G_{\rm cut}$ |
| Medium | 3/2×$G_{\rm cut}$ |
| High | 2×$G_{\rm cut}$ |

where

$E_{\rm cut}=\frac{\hbar^2}{2m_e}G_{\rm cut}^2$

with $E_{\rm cut}$=[ENCUT](ENCUT.md).

Alternatively, NGY can be set to a specific value in the
[INCAR](../input-files/INCAR.md) file.

## Related tags and articles
[NGX](NGX.md), [NGZ](NGZ.md),
[NGXF](NGXF.md), [NGYF](NGYF.md),
[NGZF](NGZF.md), [PREC](PREC.md),
[ENCUT](ENCUT.md), [ENAUG](ENAUG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NGY-_incategory-Examples)

<!-- Source: https://vasp.at/wiki/index.php/NGYF | revid: 26997 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NGYF


NGYF = \[integer\]  
Default: **NGYF** = set in accordance with [PREC](PREC.md),
[NGY](NGY.md), [ENCUT](ENCUT.md) and
[ENAUG](ENAUG.md) 

Description: NGYF sets the
number of grid points in the "fine" FFT grid along the second lattice
vector.

------------------------------------------------------------------------

On this "fine" FFT mesh the localized augmentation charges are
represented if ultrasoft pseudopotentials (USPPs) or the PAW method are
used. In case USPPs are used, the local potentials
(exchange-correlation, Hartree-potential and ionic potentials) are also
calculated on this "fine" FFT-mesh.

By default NGYF is set in
accordance with the requested "precision" mode
[PREC](PREC.md), [NGY](NGY.md), and the plane wave
kinetic energy cutoffs [ENCUT](ENCUT.md) and
[ENAUG](ENAUG.md):

|  |  |  |
|----|:--:|:--:|
| [PREC](PREC.md) | [NGY](NGY.md) | NGYF |
| Normal | 3/2×$G_{\rm cut}$ | 2×[NGY](NGY.md) |
| Single (VASP.5) | 3/2×$G_{\rm cut}$ | [NGY](NGY.md) |
| Single (VASP.6) | 2×$G_{\rm cut}$ | [NGY](NGY.md) |
| SingleN (VASP.6) | 3/2×$G_{\rm cut}$ | [NGY](NGY.md) |
| Accurate | 2×$G_{\rm cut}$ | 2×[NGY](NGY.md) |
| Low | 3/2×$G_{\rm cut}$ | 3×$G_{\rm aug}$ |
| Medium | 3/2×$G_{\rm cut}$ | 4×$G_{\rm aug}$ |
| High | 2×$G_{\rm cut}$ | 16/3×$G_{\rm aug}$ |

where

$E_{\rm cut}=\frac{\hbar^2}{2m_e}G_{\rm cut}^2 \qquad E_{\rm
aug}=\frac{\hbar^2}{2m_e}G_{\rm aug}^2$

with $E_{\rm cut}$=[ENCUT](ENCUT.md) and
$E_{\rm aug}$=[ENAUG](ENAUG.md).

Alternatively, NGYF can be set
to a specific value in the [INCAR](../input-files/INCAR.md) file.

## Related tags and articles\[<a href="/wiki/index.php?title=NGYF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NGX](NGX.md), [NGY](NGY.md), [NGZ](NGZ.md),
[NGXF](NGXF.md), [NGZF](NGZF.md),
[PREC](PREC.md), [ENCUT](ENCUT.md),
[ENAUG](ENAUG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NGYF-_incategory-Examples)



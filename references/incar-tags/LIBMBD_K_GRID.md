<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_K_GRID | revid: 24448 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_K_GRID


LIBMBD_K_GRID = \[array of
three integers\]  
Default: **LIBMBD_K_GRID** = determined in libMBD according to the cell
shape 

Description: LIBMBD_K_GRID
sets the k-mesh of the collective oscillations defined in the methods
available in the library libMBD of many-body dispersion
methods[^libmbd_1-1][^libmbd_2-2][^hermann:jcp:2023-3].

------------------------------------------------------------------------

LIBMBD_K_GRID allows to choose
the k-mesh of the collective oscillations defined in the methods
available in the library libMBD of many-body dispersion methods. The
three integers correspond to the number of k-points along the axes of
the cell in the reciprocal space. The values are internally passed to
the libMBD input **k_grid** described at the page
[^libmbd_input-4].

|  |
|----|
| **Important:** This feature is available from VASP.6.4.3 onwards that needs to be compiled with [-DLIBMBD](../misc/Precompiler_options.md). |

libMBD is a separate library package that has to be
downloaded[^libmbd_2-2]
and compiled before VASP is compiled with the corresponding [precompiler
options](../misc/Precompiler_options.md) and
[links to the
libraries](../misc/Makefile.include.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=LIBMBD_K_GRID&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_METHOD](LIBMBD_METHOD.md),
[LIBMBD_K_GRID_SHIFT](LIBMBD_K_GRID_SHIFT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_K_GRID-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_K_GRID&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^libmbd_1-1]: [https://libmbd.github.io/](https://libmbd.github.io/)
[^libmbd_2-2]: [https://github.com/libmbd/](https://github.com/libmbd/)
[^hermann:jcp:2023-3]: [J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko, *libMBD: A general-purpose package for scalable quantum many-body dispersion calculations*, J. Chem. Phys. **159**, 174802 (2023).](https://doi.org/10.1063/5.0170972)
[^libmbd_input-4]: [https://libmbd.github.io/type/mbd_input_t.html](https://libmbd.github.io/type/mbd_input_t.html)

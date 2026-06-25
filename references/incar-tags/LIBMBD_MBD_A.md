<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_MBD_A | revid: 24443 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_MBD_A


LIBMBD_MBD_A = \[real\]  
Default: **LIBMBD_MBD_A** = 6.0 

Description: LIBMBD_MBD_A sets
the value of the damping parameter $a$ in the
many-body methods as implemented in the library libMBD of many-body
dispersion
methods[^libmbd_1-1][^libmbd_2-2][^hermann:jcp:2023-3].

------------------------------------------------------------------------

LIBMBD_MBD_A allows to choose
the value of the damping parameter $a$ in the
many-body methods as implemented in the library libMBD of many-body
dispersion
methods[^libmbd_1-1][^libmbd_2-2][^hermann:jcp:2023-3].
The value is internally passed to the libMBD input **mbd_a** described
at the page
[^libmbd_input-4].

|  |
|----|
| **Mind:** LIBMBD_MBD_A can be set only if [LIBMBD_XC](LIBMBD_XC.md)=none. |

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
href="/wiki/index.php?title=LIBMBD_MBD_A&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_METHOD](LIBMBD_METHOD.md),
[LIBMBD_XC](LIBMBD_XC.md),
[LIBMBD_MBD_BETA](LIBMBD_MBD_BETA.md), [Many-body
dispersion
energy](../methods/Many-body_dispersion_energy.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_MBD_A-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_MBD_A&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^libmbd_1-1]: [https://libmbd.github.io/](https://libmbd.github.io/)
[^libmbd_2-2]: [https://github.com/libmbd/](https://github.com/libmbd/)
[^hermann:jcp:2023-3]: [J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko, *libMBD: A general-purpose package for scalable quantum many-body dispersion calculations*, J. Chem. Phys. **159**, 174802 (2023).](https://doi.org/10.1063/5.0170972)
[^libmbd_input-4]: [https://libmbd.github.io/type/mbd_input_t.html](https://libmbd.github.io/type/mbd_input_t.html)

<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_XC | revid: 33442 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_XC


LIBMBD_XC = pbe \| pbe0 \| hse
\| blyp \| b3lyp \| revpbe \| am05 \| none 

Default: The functional set by the [GGA](GGA.md),
[METAGGA](METAGGA.md) or [XC](XC.md) tag

Description: LIBMBD_XC sets
the exchange-correlation functional for the setting of damping
parameters used in the methods available in the library libMBD of
many-body dispersion
methods[^libmbd_1-1][^libmbd_2-2][^hermann:jcp:2023-3].

------------------------------------------------------------------------

LIBMBD_XC allows to choose the
exchange-correlation functional that determines which set of damping
parameters is used in the methods available in the library libMBD of
many-body dispersion methods. The value is internally passed to the
libMBD input **xc** described at the page
[^libmbd_input-4].

The possible choices depend on the dispersion method selected with the
[LIBMBD_METHOD](LIBMBD_METHOD.md) tag and are listed
in the file mbd_damping.F90 of the libMBD source code. If
LIBMBD_XC=none is chosen, then
no set of damping parameters is selected and either
[LIBMBD_TS_SR](LIBMBD_TS_SR.md) or
[LIBMBD_MBD_BETA](LIBMBD_MBD_BETA.md) has to be
set.

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
href="/wiki/index.php?title=LIBMBD_XC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_METHOD](LIBMBD_METHOD.md),
[GGA](GGA.md), [METAGGA](METAGGA.md),
[XC](XC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_XC-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_XC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^libmbd_1-1]: [https://libmbd.github.io/](https://libmbd.github.io/)
[^libmbd_2-2]: [https://github.com/libmbd/](https://github.com/libmbd/)
[^hermann:jcp:2023-3]: [J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko, *libMBD: A general-purpose package for scalable quantum many-body dispersion calculations*, J. Chem. Phys. **159**, 174802 (2023).](https://doi.org/10.1063/5.0170972)
[^libmbd_input-4]: [https://libmbd.github.io/type/mbd_input_t.html](https://libmbd.github.io/type/mbd_input_t.html)

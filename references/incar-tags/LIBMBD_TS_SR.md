<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_TS_SR | revid: 24450 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_TS_SR


LIBMBD_TS_SR = \[real\]  
Default: **LIBMBD_TS_SR** = value that was determined for the
exchange-correlation functional set with
[LIBMBD_XC](LIBMBD_XC.md) 

Description: LIBMBD_TS_SR sets
the value of the scaling factor $s_R$ in the
Tkatchenko-Scheffler
method[^tkatchenko:prl:09-1]
as implemented in the library libMBD of many-body dispersion
methods[^libmbd_1-2][^libmbd_2-3][^hermann:jcp:2023-4].

------------------------------------------------------------------------

LIBMBD_TS_SR allows to choose
the value of the scaling factor $s_R$ in the
Tkatchenko-Scheffler
method[^tkatchenko:prl:09-1]
as implemented in the library libMBD of many-body dispersion
methods[^libmbd_1-2][^libmbd_2-3][^hermann:jcp:2023-4].
The value is internally passed to the libMBD input **ts_sr** described
at the page
[^libmbd_input-5].
LIBMBD_TS_SR is similar to the
[VDW_SR](VDW_SR.md) tag that is used for the VASP
implementation of the Tkatchenko-Scheffler method.

|  |
|----|
| **Mind:** LIBMBD_TS_SR can be set only if [LIBMBD_XC](LIBMBD_XC.md)=none. |

|  |
|----|
| **Important:** This feature is available from VASP.6.4.3 onwards that needs to be compiled with [-DLIBMBD](../misc/Precompiler_options.md). |

libMBD is a separate library package that has to be
downloaded[^libmbd_2-3]
and compiled before VASP is compiled with the corresponding [precompiler
options](../misc/Precompiler_options.md) and
[links to the
libraries](../misc/Makefile.include.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=LIBMBD_TS_SR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_METHOD](LIBMBD_METHOD.md),
[LIBMBD_XC](LIBMBD_XC.md),
[LIBMBD_TS_D](LIBMBD_TS_D.md), [Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_TS_SR-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_TS_SR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^tkatchenko:prl:09-1]: [A. Tkatchenko and M. Scheffler, Phys. Rev. Lett. **102**, 073005 (2009).](https://doi.org/10.1103/PhysRevLett.102.073005)
[^libmbd_1-2]: [https://libmbd.github.io/](https://libmbd.github.io/)
[^libmbd_2-3]: [https://github.com/libmbd/](https://github.com/libmbd/)
[^hermann:jcp:2023-4]: [J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko, *libMBD: A general-purpose package for scalable quantum many-body dispersion calculations*, J. Chem. Phys. **159**, 174802 (2023).](https://doi.org/10.1063/5.0170972)
[^libmbd_input-5]: [https://libmbd.github.io/type/mbd_input_t.html](https://libmbd.github.io/type/mbd_input_t.html)

<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_ALPHA | revid: 35876 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_ALPHA


LIBMBD_ALPHA = \[real array\] 

Description: LIBMBD_ALPHA
defines the free-atom polarizabilities $\alpha_{0}$
(bohr$^{3}$) used
in the
[Tkatchenko-Scheffler](../methods/Tkatchenko-Scheffler_method.md)
and [Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)
methods as implemented in the library libMBD of many-body dispersion
methods<sup>[\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)</sup>.

------------------------------------------------------------------------

LIBMBD_ALPHA allows to set
values for the free-atom polarizabilities $\alpha_{0}$
(bohr$^{3}$) used
in the
[Tkatchenko-Scheffler](../methods/Tkatchenko-Scheffler_method.md)
and [Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)
methods as implemented in the library libMBD of many-body dispersion
methods<sup>[\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)</sup>.
For each atom listed in the [POSCAR](../input-files/POSCAR.md) file, a
value has to be provided. The values are internally passed to the first
column of the libMBD input **free_values** described at the page
<sup>[\[4\]](#cite_note-libmbd_input-4)</sup>.

|  |
|----|
| **Important:** This feature is available from VASP.6.4.3 onwards that needs to be compiled with [-DLIBMBD](../misc/Precompiler_options.md). |

libMBD is a separate library package that has to be
downloaded<sup>[\[2\]](#cite_note-libmbd_2-2)</sup>
and compiled before VASP is compiled with the corresponding [precompiler
options](../misc/Precompiler_options.md) and
[links to the
libraries](../misc/Makefile.include.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=LIBMBD_ALPHA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_METHOD](LIBMBD_METHOD.md),
[LIBMBD_C6AU](LIBMBD_C6AU.md),
[LIBMBD_R0AU](LIBMBD_R0AU.md),
[Tkatchenko-Scheffler](../methods/Tkatchenko-Scheffler_method.md),
[Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_ALPHA-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_ALPHA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-libmbd_1_1-0)</sup>
    <sup>[b](#cite_ref-libmbd_1_1-1)</sup>
    <a href="https://libmbd.github.io/" class="external text"
    rel="nofollow">https://libmbd.github.io/</a>
2.  ↑
    <sup>[a](#cite_ref-libmbd_2_2-0)</sup>
    <sup>[b](#cite_ref-libmbd_2_2-1)</sup>
    <sup>[c](#cite_ref-libmbd_2_2-2)</sup>
    <a href="https://github.com/libmbd/" class="external text"
    rel="nofollow">https://github.com/libmbd/</a>
3.  ↑
    <sup>[a](#cite_ref-hermann:jcp:2023_3-0)</sup>
    <sup>[b](#cite_ref-hermann:jcp:2023_3-1)</sup>
    <a href="https://doi.org/10.1063/5.0170972" class="external text"
    rel="nofollow">J. Hermann, M. Stöhr, S. Góger, S. Chaudhuri, B. Aradi,
    R. J. Maurer, and A. Tkatchenko, <em>libMBD: A general-purpose package
    for scalable quantum many-body dispersion calculations</em>, J. Chem.
    Phys. <strong>159</strong>, 174802 (2023).</a>
4.  [↑](#cite_ref-libmbd_input_4-0)
    <a href="https://libmbd.github.io/type/mbd_input_t.html"
    class="external text"
    rel="nofollow">https://libmbd.github.io/type/mbd_input_t.html</a>


------------------------------------------------------------------------



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
methods<sup>[\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)</sup>.

------------------------------------------------------------------------

LIBMBD_K_GRID allows to choose
the k-mesh of the collective oscillations defined in the methods
available in the library libMBD of many-body dispersion methods. The
three integers correspond to the number of k-points along the axes of
the cell in the reciprocal space. The values are internally passed to
the libMBD input **k_grid** described at the page
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


1.  [↑](#cite_ref-libmbd_1_1-0)
    <a href="https://libmbd.github.io/" class="external text"
    rel="nofollow">https://libmbd.github.io/</a>
2.  ↑
    <sup>[a](#cite_ref-libmbd_2_2-0)</sup>
    <sup>[b](#cite_ref-libmbd_2_2-1)</sup>
    <a href="https://github.com/libmbd/" class="external text"
    rel="nofollow">https://github.com/libmbd/</a>
3.  [↑](#cite_ref-hermann:jcp:2023_3-0)
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



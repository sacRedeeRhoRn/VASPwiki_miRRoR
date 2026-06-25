<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_PARALLEL_MODE | revid: 24444 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_PARALLEL_MODE


LIBMBD_PARALLEL_MODE = auto \|
kpoints \| atoms 

Default:
LIBMBD_PARALLEL_MODE=auto
(default in libMBD)

Description:
LIBMBD_PARALLEL_MODE selects
the parallelization scheme used in the library libMBD of many-body
dispersion
methods<sup>[\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)</sup>.

------------------------------------------------------------------------

LIBMBD_PARALLEL_MODE allows to
choose the parallelization scheme used in the library libMBD of
many-body dispersion
methods<sup>[\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)</sup>.
The value is internally passed to the libMBD input **parallel_mode**
described at the page
<sup>[\[4\]](#cite_note-libmbd_input-4)</sup>.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span
style="color: var(--vpurple);">Important:</span></strong>
<ul>
<li>The <span class="mw-selflink selflink">LIBMBD_PARALLEL_MODE</span>
tag can be used only if libMBD was compiled with MPI parallelization
enabled.</li>
<li>This feature is available from VASP.6.4.3 onwards that needs to be
compiled with <a href="/wiki/Precompiler_options#-DLIBMBD"
title="Precompiler options">-DLIBMBD</a>.</li>
</ul></td>
</tr>
</tbody>
</table>

libMBD is a separate library package that has to be
downloaded<sup>[\[2\]](#cite_note-libmbd_2-2)</sup>
and compiled before VASP is compiled with the corresponding [precompiler
options](../misc/Precompiler_options.md) and
[links to the
libraries](../misc/Makefile.include.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=LIBMBD_PARALLEL_MODE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_METHOD](LIBMBD_METHOD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_PARALLEL_MODE-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_PARALLEL_MODE&amp;veaction=edit&amp;section=2"
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



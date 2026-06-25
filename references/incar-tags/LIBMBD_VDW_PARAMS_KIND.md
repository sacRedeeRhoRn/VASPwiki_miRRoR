<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_VDW_PARAMS_KIND | revid: 24441 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_VDW_PARAMS_KIND


LIBMBD_VDW_PARAMS_KIND = ts \|
tssurf 

Default:
LIBMBD_VDW_PARAMS_KIND=ts
(default in libMBD)

Description:
LIBMBD_VDW_PARAMS_KIND sets
the type of free-atom van der Waals parameters that are used for the
methods implemented in the library libMBD of many-body dispersion
methods<sup>[\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)</sup>.

------------------------------------------------------------------------

LIBMBD_VDW_PARAMS_KIND allows
to choose the set of van der Waals parameters from either the original
Tkatchenko-Scheffler
method<sup>[\[4\]](#cite_note-tkatchenko:prl:09-4)</sup>
(LIBMBD_VDW_PARAMS_KIND=ts) or
its variant that was designed to be more accurate for systems with
surface<sup>[\[5\]](#cite_note-ruiz:prb:2016-5)</sup>
(LIBMBD_VDW_PARAMS_KIND=tssurf).
The value is internally passed to the libMBD input **vdw_params_kind**
described at the page
<sup>[\[6\]](#cite_note-libmbd_input-6)</sup>.
LIBMBD_VDW_PARAMS_KIND is
similar to the [LTSSURF](LTSSURF.md) tag that is used for
the VASP implementation of the Tkatchenko-Scheffler method.

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
href="/wiki/index.php?title=LIBMBD_VDW_PARAMS_KIND&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_METHOD](LIBMBD_METHOD.md),
[Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
[Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_VDW_PARAMS_KIND-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_VDW_PARAMS_KIND&amp;veaction=edit&amp;section=2"
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
4.  [↑](#cite_ref-tkatchenko:prl:09_4-0)
    <a href="https://doi.org/10.1103/PhysRevLett.102.073005"
    class="external text" rel="nofollow">A. Tkatchenko and M. Scheffler,
    Phys. Rev. Lett. <strong>102</strong>, 073005 (2009).</a>
5.  [↑](#cite_ref-ruiz:prb:2016_5-0)
    <a href="https://doi.org/10.1103/PhysRevB.93.035118"
    class="external text" rel="nofollow">V. G. Ruiz, W. Liu, and A.
    Tkatchenko, <em>Density-functional theory with screened van der Waals
    interactions applied to atomic and molecular adsorbates on close-packed
    and non-close-packed surfaces</em>, Phys. Rev. B <em>93</em>, 035118
    (2016)</a>
6.  [↑](#cite_ref-libmbd_input_6-0)
    <a href="https://libmbd.github.io/type/mbd_input_t.html"
    class="external text"
    rel="nofollow">https://libmbd.github.io/type/mbd_input_t.html</a>


------------------------------------------------------------------------



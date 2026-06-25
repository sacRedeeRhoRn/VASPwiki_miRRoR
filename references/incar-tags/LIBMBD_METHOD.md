<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_METHOD | revid: 34767 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_METHOD


LIBMBD_METHOD = \[string\]  
Default: **LIBMBD_METHOD** = mbd-rsscs (default in libMBD) 

Description: LIBMBD_METHOD
selects one of the methods available in the library libMBD of many-body
dispersion
methods<sup>[\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)</sup>.
Only used when [`IVDW`](IVDW.md)` = 14`.

------------------------------------------------------------------------

LIBMBD_METHOD can be set to a
label (string) corresponding to one of the methods listed on the libMBD
website (see **method** at the page
<sup>[\[4\]](#cite_note-libmbd_input-4)</sup>).

|  |
|----|
| **Mind:** Note that the use of the mbd-nl method<sup>[\[5\]](#cite_note-hermann:prl:2020-5)</sup> is currently not possible, since the associated atomic polarizabilities and semilocal functional are currently not implemented in VASP. |

|  |
|----|
| **Important:** This feature is available from VASP.6.4.3 onwards that needs to be compiled with [-DLIBMBD](../misc/Precompiler_options.md). |

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vred); --box-emph-color: var(--vred); padding: 5px; color: var(--vdefault-text-nb); background: var(--vred-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vred);">Warning:</span></strong>
<ul>
<li>There is a severe bug in VASP.6.5.1 and previous versions: during a
geometry relaxation, the new atomic positions and cell parameters are
not passed to libMBD. See <a href="/wiki/Known_issues"
title="Known issues">known issues</a> for a patch.</li>
<li>It is recommended to compile libMBD without ScaLAPACK/MPI, otherwise
nudged elastic bands (NEB) calculations will not run properly and
produce wrong results.</li>
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
href="/wiki/index.php?title=LIBMBD_METHOD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBMBD_XC](LIBMBD_XC.md),
[LIBMBD_TS_D](LIBMBD_TS_D.md),
[LIBMBD_TS_SR](LIBMBD_TS_SR.md),
[LIBMBD_MBD_A](LIBMBD_MBD_A.md),
[LIBMBD_MBD_BETA](LIBMBD_MBD_BETA.md),
[LIBMBD_VDW_PARAMS_KIND](LIBMBD_VDW_PARAMS_KIND.md),
[LIBMBD_ALPHA](LIBMBD_ALPHA.md),
[LIBMBD_C6AU](LIBMBD_C6AU.md),
[LIBMBD_R0AU](LIBMBD_R0AU.md),
[LIBMBD_N_OMEGA_GRID](LIBMBD_N_OMEGA_GRID.md),
[LIBMBD_K_GRID](LIBMBD_K_GRID.md),
[LIBMBD_K_GRID_SHIFT](LIBMBD_K_GRID_SHIFT.md),
[LIBMBD_PARALLEL_MODE](LIBMBD_PARALLEL_MODE.md),
[Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
[Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_METHOD-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LIBMBD_METHOD&amp;veaction=edit&amp;section=2"
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
5.  [↑](#cite_ref-hermann:prl:2020_5-0)
    <a href="https://doi.org/10.1103/PhysRevLett.124.146401"
    class="external text" rel="nofollow">J. Hermann and A. Tkatchenko,
    <em>Density Functional Model for van der Waals Interactions: Unifying
    Many-Body Atomic Approaches with Nonlocal Functionals</em>, Phys. Rev.
    Lett. <strong>124</strong>, 146401 (2020).</a>


------------------------------------------------------------------------



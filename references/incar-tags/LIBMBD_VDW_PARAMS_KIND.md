<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_VDW_PARAMS_KIND | revid: 24441 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_VDW_PARAMS_KIND
LIBMBD_VDW_PARAMS_KIND = ts \| tssurf 

Default: LIBMBD_VDW_PARAMS_KIND=ts (default in libMBD)

Description: LIBMBD_VDW_PARAMS_KIND sets the type of free-atom van der
Waals parameters that are used for the methods implemented in the
library libMBD of many-body dispersion
methods^([\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)).

------------------------------------------------------------------------

LIBMBD_VDW_PARAMS_KIND allows to choose the set of van der Waals
parameters from either the original Tkatchenko-Scheffler
method^([\[4\]](#cite_note-tkatchenko:prl:09-4))
(LIBMBD_VDW_PARAMS_KIND=ts) or its variant that was designed to be more
accurate for systems with surface^([\[5\]](#cite_note-ruiz:prb:2016-5))
(LIBMBD_VDW_PARAMS_KIND=tssurf). The value is internally passed to the
libMBD input **vdw_params_kind** described at the page
^([\[6\]](#cite_note-libmbd_input-6)). LIBMBD_VDW_PARAMS_KIND is similar
to the [LTSSURF](LTSSURF.md) tag that is used for the VASP
implementation of the Tkatchenko-Scheffler method.

|  |
|----|
| **Important:** This feature is available from VASP.6.4.3 onwards that needs to be compiled with [-DLIBMBD](../misc/Precompiler_options.md). |

libMBD is a separate library package that has to be
downloaded^([\[2\]](#cite_note-libmbd_2-2)) and compiled before VASP is
compiled with the corresponding [precompiler
options](../misc/Precompiler_options.md) and
[links to the
libraries](../misc/Makefile.include.md).

## Related tags and articles
[LIBMBD_METHOD](LIBMBD_METHOD.md),
[Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
[Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_VDW_PARAMS_KIND-_incategory-Examples)

## References
1.  [↑](#cite_ref-libmbd_1_1-0)
    [https://libmbd.github.io/](https://libmbd.github.io/)
2.  ↑ ^([a](#cite_ref-libmbd_2_2-0)) ^([b](#cite_ref-libmbd_2_2-1))
    [https://github.com/libmbd/](https://github.com/libmbd/)
3.  [↑](#cite_ref-hermann:jcp:2023_3-0) [J. Hermann, M. Stöhr, S.
    Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko,
    *libMBD: A general-purpose package for scalable quantum many-body
    dispersion calculations*, J. Chem. Phys. **159**, 174802
    (2023).](https://doi.org/10.1063/5.0170972)
4.  [↑](#cite_ref-tkatchenko:prl:09_4-0) [A. Tkatchenko and M.
    Scheffler, Phys. Rev. Lett. **102**, 073005
    (2009).](https://doi.org/10.1103/PhysRevLett.102.073005)
5.  [↑](#cite_ref-ruiz:prb:2016_5-0) [V. G. Ruiz, W. Liu, and A.
    Tkatchenko, *Density-functional theory with screened van der Waals
    interactions applied to atomic and molecular adsorbates on
    close-packed and non-close-packed surfaces*, Phys. Rev. B *93*,
    035118 (2016)](https://doi.org/10.1103/PhysRevB.93.035118)
6.  [↑](#cite_ref-libmbd_input_6-0)
    [https://libmbd.github.io/type/mbd_input_t.html](https://libmbd.github.io/type/mbd_input_t.html)

------------------------------------------------------------------------

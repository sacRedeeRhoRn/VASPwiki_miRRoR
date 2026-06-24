<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_MBD_BETA | revid: 24445 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_MBD_BETA
LIBMBD_MBD_BETA = \[real\]  
Default: **LIBMBD_MBD_BETA** = value that was determined for the
exchange-correlation functional set with
[LIBMBD_XC](LIBMBD_XC.md) 

Description: LIBMBD_MBD_BETA sets the value of the scaling factor
$\beta$ (usually denoted
$s_R$) in the many-body methods as
implemented in the library libMBD of many-body dispersion
methods^([\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)).

------------------------------------------------------------------------

LIBMBD_MBD_BETA allows to choose the value of the damping parameter
$\beta$ in the many-body methods as
implemented in the library libMBD of many-body dispersion
methods^([\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)).
The value is internally passed to the libMBD input **mbd_beta**
described at the page ^([\[4\]](#cite_note-libmbd_input-4)).
LIBMBD_MBD_BETA is the same as the [VDW_SR](VDW_SR.md) tag
that is used for the VASP implementation of the many-body methods.

|  |
|----|
| **Mind:** LIBMBD_MBD_BETA can be set only if [LIBMBD_XC](LIBMBD_XC.md)=none. |

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
[LIBMBD_XC](LIBMBD_XC.md),
[LIBMBD_MBD_A](LIBMBD_MBD_A.md), [Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_MBD_BETA-_incategory-Examples)

## References
1.  ↑ ^([a](#cite_ref-libmbd_1_1-0)) ^([b](#cite_ref-libmbd_1_1-1))
    [https://libmbd.github.io/](https://libmbd.github.io/)
2.  ↑ ^([a](#cite_ref-libmbd_2_2-0)) ^([b](#cite_ref-libmbd_2_2-1))
    ^([c](#cite_ref-libmbd_2_2-2))
    [https://github.com/libmbd/](https://github.com/libmbd/)
3.  ↑ ^([a](#cite_ref-hermann:jcp:2023_3-0))
    ^([b](#cite_ref-hermann:jcp:2023_3-1)) [J. Hermann, M. Stöhr, S.
    Góger, S. Chaudhuri, B. Aradi, R. J. Maurer, and A. Tkatchenko,
    *libMBD: A general-purpose package for scalable quantum many-body
    dispersion calculations*, J. Chem. Phys. **159**, 174802
    (2023).](https://doi.org/10.1063/5.0170972)
4.  [↑](#cite_ref-libmbd_input_4-0)
    [https://libmbd.github.io/type/mbd_input_t.html](https://libmbd.github.io/type/mbd_input_t.html)

------------------------------------------------------------------------

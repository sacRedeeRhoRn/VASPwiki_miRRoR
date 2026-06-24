<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_N_OMEGA_GRID | revid: 24440 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_N_OMEGA_GRID
LIBMBD_N_OMEGA_GRID = \[integer\]  
Default: **LIBMBD_N_OMEGA_GRID** = 15 (default in libMBD) 

Description: LIBMBD_N_OMEGA_GRID sets the number of points on the grid
of imaginary frequencies used in the library libMBD of many-body
dispersion
methods^([\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)).

------------------------------------------------------------------------

LIBMBD_N_OMEGA_GRID allows to choose the number of points on the grid of
imaginary frequencies used in the library libMBD of many-body dispersion
methods. The value is internally passed to the libMBD input
**n_omega_grid** described at the page
^([\[4\]](#cite_note-libmbd_input-4)).

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
[LIBMBD_METHOD](LIBMBD_METHOD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_N_OMEGA_GRID-_incategory-Examples)

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
4.  [↑](#cite_ref-libmbd_input_4-0)
    [https://libmbd.github.io/type/mbd_input_t.html](https://libmbd.github.io/type/mbd_input_t.html)

------------------------------------------------------------------------

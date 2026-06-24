<!-- Source: https://vasp.at/wiki/index.php/LIBMBD_PARALLEL_MODE | revid: 24444 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LIBMBD_PARALLEL_MODE
LIBMBD_PARALLEL_MODE = auto \| kpoints \| atoms 

Default: LIBMBD_PARALLEL_MODE=auto (default in libMBD)

Description: LIBMBD_PARALLEL_MODE selects the parallelization scheme
used in the library libMBD of many-body dispersion
methods^([\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)).

------------------------------------------------------------------------

LIBMBD_PARALLEL_MODE allows to choose the parallelization scheme used in
the library libMBD of many-body dispersion
methods^([\[1\]](#cite_note-libmbd_1-1)[\[2\]](#cite_note-libmbd_2-2)[\[3\]](#cite_note-hermann:jcp:2023-3)).
The value is internally passed to the libMBD input **parallel_mode**
described at the page ^([\[4\]](#cite_note-libmbd_input-4)).

[TABLE]

libMBD is a separate library package that has to be
downloaded^([\[2\]](#cite_note-libmbd_2-2)) and compiled before VASP is
compiled with the corresponding [precompiler
options](../misc/Precompiler_options.md) and
[links to the
libraries](../misc/Makefile.include.md).

## Related tags and articles
[LIBMBD_METHOD](LIBMBD_METHOD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LIBMBD_PARALLEL_MODE-_incategory-Examples)

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

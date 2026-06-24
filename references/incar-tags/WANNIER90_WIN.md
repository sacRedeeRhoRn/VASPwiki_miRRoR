<!-- Source: https://vasp.at/wiki/index.php/WANNIER90_WIN | revid: 22341 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WANNIER90_WIN
  
WANNIER90_WIN = \[string\] 

|                            |        |     |
|----------------------------|--------|-----|
| Default: **WANNIER90_WIN** | = None |     |

Description: WANNIER90_WIN sets the content of the **wannier90.win**
file.

------------------------------------------------------------------------

The WANNIER90_WIN tag is a multiline string, where the content of the
**wannier90.win** file can be specified. For instance,

    WANNIER90_WIN = "
    exclude_bands 17-64

    Begin Projections
    Si:sp3
    End Projections

    # Disentanglement
    dis_win_min = -7
    dis_win_max = 16
    dis_num_iter = 100

    guiding_centres = true
    "

Additionally, the value of some [Wannier90
tags](https://github.com/wannier-developers/wannier90/raw/v3.1.0/doc/compiled_docs/user_guide.pdf)
is set automatically based on the VASP calculation, e.g., *kpoints*,
*atoms*, *unit_cell*, *mp_grid*, *spinors*, *num_bands*, *num_wann*.

Available as of VASP 6.2.0.

## Related tags and articles
[NUM_WANN](NUM_WANN.md),
[LWANNIER90](LWANNIER90.md),
[LWANNIER90_RUN](LWANNIER90_RUN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-WANNIER90_WIN-_incategory-Examples)

------------------------------------------------------------------------

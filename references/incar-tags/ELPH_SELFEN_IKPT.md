<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_IKPT | revid: 27939 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_IKPT
ELPH_SELFEN_IKPT = \[real array\]  
Default: **ELPH_SELFEN_IKPT** = All k-points 

Description: Compute the electron self-energy due to electron-phonon for
a list of k-points specified by their index in the irreducible Brillouin
zone generated from [KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md).

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

For example, to select to compute for 4 different **k** points we
specify their index in the [INCAR](../input-files/INCAR.md) file

    ELPH_SELFEN_IKPT = 1 3 6 8

This tag can be used in combination with
[ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)
and
[ELPH_SELFEN_BAND_STOP](ELPH_SELFEN_BAND_STOP.md)
to select the calculation of the electron-phonon self-energy for a
particular set of **k** points and bands. Instead of specifying the
indexes of the **k** points in the irreducible Brillouin zone, one can
specify their reduced coordinates with
[ELPH_SELFEN_KPTS](ELPH_SELFEN_KPTS.md).

Instead of specifying the index of the **k** point appearing the in
irreducible Brillouin zone, one can specify the reduced coordinates of
the desired k-points using
[ELPH_SELFEN_KPTS](ELPH_SELFEN_KPTS.md).

## Related tags and articles
- [ELPH_RUN](ELPH_RUN.md)
- [KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md)
- [ELPH_SELFEN_GAPS](ELPH_SELFEN_GAPS.md)
- [ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)
- [ELPH_SELFEN_BAND_STOP](ELPH_SELFEN_BAND_STOP.md)
- [ELPH_SELFEN_KPTS](ELPH_SELFEN_KPTS.md)

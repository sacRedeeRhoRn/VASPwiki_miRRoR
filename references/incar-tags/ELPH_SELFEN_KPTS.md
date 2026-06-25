<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_KPTS | revid: 27940 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_KPTS


ELPH_SELFEN_KPTS = \[real
array\]  
Default: **ELPH_SELFEN_KPTS** = All k-points 

Description: Computes the electron self-energy due to electron-phonon
for a list of k-points specified by their fractional coordinates.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

For example, to select 4 different **k**-points we specify their
coordinates in the [INCAR](../input-files/INCAR.md) file

    ELPH_SELFEN_KPTS = \
      0.0  0.0  0.0 \
      0.5  0.5  0.0 \
      0.5  0.5  0.0 \
      0.5  0.75 0.25

The matching of the user input coordinates with the ones generated from
the [KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md) file in VASP is
done by looking at the closest point in the full Brillouin zone, which
is then mapped to the point in the irreducible Brillouin zone. The user
should always check whether the matching found and reported in the
[OUTCAR](../output-files/OUTCAR.md) is correct.

This tag can be used in combination with
[ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)
and
[ELPH_SELFEN_BAND_STOP](ELPH_SELFEN_BAND_STOP.md)
to select the calculation of the electron-phonon self-energy for a
particular set of **k** points and bands.

Instead of specifying the reduced coordinates, one can specify the index
of the **k** point appearing the in irreducible Brillouin zone list
using [ELPH_SELFEN_IKPT](ELPH_SELFEN_IKPT.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_KPTS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_RUN](ELPH_RUN.md)
- [KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md)
- [ELPH_SELFEN_GAPS](ELPH_SELFEN_GAPS.md)
- [ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)
- [ELPH_SELFEN_BAND_STOP](ELPH_SELFEN_BAND_STOP.md)
- [ELPH_SELFEN_IKPT](ELPH_SELFEN_IKPT.md)



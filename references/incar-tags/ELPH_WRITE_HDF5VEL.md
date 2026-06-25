<!-- Source: https://vasp.at/wiki/index.php/ELPH_WRITE_HDF5VEL | revid: 31230 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_WRITE_HDF5VEL


ELPH_WRITE_HDF5VEL =
\[logical\]  
Default: **ELPH_WRITE_HDF5VEL** = .FALSE. 

Description: If set, writes the electron group velocities to the
[vaspout.h5](../output-files/Vaspout.h5.md) file.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The dataset is stored in the [vaspout.h5](../output-files/Vaspout.h5.md)
file

     $ h5ls -r vaspout.h5 | grep velocity
     /results/electron_phonon/electrons/velocity Dataset {3, 1, 20, 8}

The group velocities are written in ev Å units in cartesian coordinates.
This tag can be used independently of
[ELPH_WRITE_TEXTVEL](ELPH_WRITE_TEXTVEL.md). The
number of bands is the one set by
[ELPH_NBANDS](ELPH_NBANDS.md) which can in some cases
be different from [NBANDS](NBANDS.md). If both are set, both
outputs are written.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_WRITE_HDF5VEL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_WRITE_TEXTVEL](ELPH_WRITE_TEXTVEL.md)



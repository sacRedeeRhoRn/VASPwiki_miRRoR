<!-- Source: https://vasp.at/wiki/index.php/ELPH_WRITE_TEXTVEL | revid: 31231 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_WRITE_TEXTVEL


ELPH_WRITE_TEXTVEL =
\[logical\]  
Default: **ELPH_WRITE_TEXTVEL** = .FALSE. 

Description: If set, writes the electron group velocities to a
<a href="/wiki/index.php?title=Velocity&amp;action=edit&amp;redlink=1"
class="new" title="Velocity (page does not exist)">velocity</a>
human-readable text file.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The
<a href="/wiki/index.php?title=Velocity&amp;action=edit&amp;redlink=1"
class="new" title="Velocity (page does not exist)">velocity</a> file
contains the following information:

    # band kpoint spin direction energy(eV)  velocity
     1 1 1 1 e1 vel1
     2 1 1 1 e2 vel2
     ...
     8 1 1 1 e8 vel8
     ...

The group velocities are written in ev Å units in cartesian coordinates.
This tag can be used independently of
[ELPH_WRITE_HDF5VEL](ELPH_WRITE_HDF5VEL.md). The
number of bands is the one set by
[ELPH_NBANDS](ELPH_NBANDS.md) which can in some cases
be different from [NBANDS](NBANDS.md). If both are set, both
outputs are written.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_WRITE_TEXTVEL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_WRITE_HDF5VEL](ELPH_WRITE_HDF5VEL.md)



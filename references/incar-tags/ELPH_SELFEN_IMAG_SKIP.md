<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_IMAG_SKIP | revid: 32992 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_IMAG_SKIP


ELPH_SELFEN_IMAG_SKIP =
\[logical\]  
Default: **ELPH_SELFEN_IMAG_SKIP** = .FALSE. 

Description: Use the tetrahedron method to skip the computation of
electron-phonon matrix elements for which the energy-conserving delta
functions are zero.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

It is strongly recommended to enable this option when only the imaginary
part of the electron self-energy (linewidths) are required, for instance
in transport or scattering rate calculations. Using this tag can reduce
the computational cost by orders of magnitude, depending on the
electronic band structure.

When using this option, it is also recommended to set
[ELPH_WF_REDISTRIBUTE](ELPH_WF_REDISTRIBUTE.md)
= .TRUE.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_IMAG_SKIP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ELPH_WF_REDISTRIBUTE](ELPH_WF_REDISTRIBUTE.md),
[ELPH_SCATTERING_APPROX](ELPH_SCATTERING_APPROX.md),
[ELPH_RUN](ELPH_RUN.md), ((TAG\|ELPH_SELFEN_G_SKIP}}



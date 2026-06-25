<!-- Source: https://vasp.at/wiki/index.php/LASPH | revid: 35705 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LASPH


LASPH = .TRUE. \| .FALSE.  
Default: **LASPH** = .FALSE. 

Description: include non-spherical contributions related to the gradient
of the density in the PAW spheres.

------------------------------------------------------------------------

Usually VASP calculates only the spherical contribution to the gradient
corrections inside the PAW spheres (non-spherical contributions for the
LDA part of the potential and the Hartree potential are always
included).

For LASPH = .TRUE.,
non-spherical contributions from the gradient corrections inside the PAW
spheres will be included as well. For VASP.4.6, these contributions are
only included in the total energy, after self-consistency has been
reached disregarding the aspherical contributions in the gradient
corrections.

From VASP.5.X the aspherical contributions are properly accounted for in
the Kohn-Sham potential as well, if
LASPH = .TRUE. is set. This is
essential for accurate total energies and band structure calculations
for *f*-elements (e.g. ceria), all 3*d*-elements (transition metal
oxides), and magnetic atoms in the 2nd row (B-F atom), in particular if
DFT+U or hybrid functionals, meta-GGAs, or vdW-DFT are used, since these
functionals often result in aspherical charge densities.

## Related tags and articles\[<a href="/wiki/index.php?title=LASPH&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LMAXPAW](LMAXPAW.md), [LMAXTAU](LMAXTAU.md),
[LMIXTAU](LMIXTAU.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LASPH-_incategory-Examples)

------------------------------------------------------------------------



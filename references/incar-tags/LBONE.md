<!-- Source: https://vasp.at/wiki/index.php/LBONE | revid: 29600 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LBONE


LBONE = .TRUE. \| .FALSE.  
Default: **LBONE** = .FALSE. 

Description: LBONE adds the
small *B*-component to the chemical shift tensor.

------------------------------------------------------------------------

LBONE restores the small
*B*-component of the wave function inside the PAW spheres in the
linear-response calculation of the NMR chemical shift tensor. The
POTCARs used in VASP are scalar-relativistic and the AE-partial waves
are solutions of the scalar-relativistic Kohn-Sham equation for the
spherical atom. These have a large (*A*) and a small (*B*) component.
The latter is not retained on the POTCAR, but approximately restored
when LBONE=.TRUE.
[^dewijs:laskowski:jcp:2017-1].
LBONE only affects the
one-center valence contributions to the chemical shift. The contribution
of the core electrons includes the *B*-component by default.

## Related tags and articless\[<a href="/wiki/index.php?title=LBONE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articless">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md)

## References\[<a href="/wiki/index.php?title=LBONE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^dewijs:laskowski:jcp:2017-1]: [G. A. de Wijs, R. Laskowski, P. Blaha, R. W. A. Havenith, G. Kresse, and M. Marsman, *NMR shieldings from density functional perturbation theory: GIPAW versus all-electron calculations*, J. Chem. Phys. **146**, 064115 (2017).](https://doi.org/10.1063/1.4975122)

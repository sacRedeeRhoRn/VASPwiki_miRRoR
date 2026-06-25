<!-- Source: https://vasp.at/wiki/index.php/LMAXPAW | revid: 32795 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMAXPAW


LMAXPAW = \[integer\]  
Default: **LMAXPAW** = 2*l* <sub>max</sub>, where *l* <sub>max</sub> is
the maximum angular quantum number of the PAW partial waves in the
[POTCAR](../input-files/POTCAR.md) file. 

Description: The maximum *l*-quantum number for the evaluation of the
one-center terms on the radial grids in the
<a href="/wiki/PAW_method" class="mw-redirect" title="PAW method">PAW
method</a>.

------------------------------------------------------------------------

Useful settings for LMAXPAW are for instance:

    LMAXPAW= 0

In this case, only spherical terms are evaluated on the radial grid.
This does not mean that aspherical terms are totally neglected, because
the compensation charges are always expanded up to 2*l* <sub>max</sub>
on the plane wave grid.

    LMAXPAW=-1 

For `LMAXPAW`` = -1`, no
one-center correction terms are evaluated on the radial support grid,
which effectively means that the behavior of US-PP's is recovered with
PAW input datasets. Usually, this allows for somewhat faster
calculations, and this switch might be of interest for relaxations and
molecular dynamics runs. Energies should be evaluated with the default
setting for LMAXPAW. For
spinpolarized calculations, results using LMAXPAW=-1 might differ
significantly from conventional PAW calculations, hence the use of
`LMAXPAW`` = -1` is not
recommended for magnetic materials, spin-polarized molecules or atoms.

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMAXPAW-_incategory-Examples)



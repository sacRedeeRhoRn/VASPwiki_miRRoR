<!-- Source: https://vasp.at/wiki/index.php/NUM_WANN | revid: 30236 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NUM_WANN


NUM_WANN = \[integer\]  
Default: **NUM_WANN** = [NBANDS](NBANDS.md) 

Description: Controls the number of Wannier orbitals to be constructed.

------------------------------------------------------------------------

This tag is used to determine the number of Wannier orbitals to be
constructed in the [SCDM
method](../categories/Category-Wannier_functions.md) "Category:Wannier functions").

Since VASP 6.2.0, NUM_WANN
also determines the number of Wannier orbitals to be used with
wannier90. Note that the `num_wann` value written to the `wannier90.win`
file is always the value of
NUM_WANN known by vasp.

When using [LOCPROJ](LOCPROJ.md) for Wannierization, it is
not necessary to set NUM_WANN.
In this case, the number of Wannier orbitals is automatically set equal
to the number of local functions.

## Related tags and articles\[<a href="/wiki/index.php?title=NUM_WANN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LWANNIER90](LWANNIER90.md),
[LSCDM](LSCDM.md),
[CUTOFF_TYPE](CUTOFF_TYPE.md)

------------------------------------------------------------------------



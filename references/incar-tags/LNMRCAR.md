<!-- Source: https://vasp.at/wiki/index.php/LNMRCAR | revid: 34760 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNMRCAR


LNMRCAR = .TRUE. \| .FALSE.  
Default: **LNMRCAR** = .TRUE. 

Description: Write the
[NMRCAR.magres](NMRCAR.magres.md) file for [EFG
calculations](../tutorials/Calculating_the_electric_field_gradient.md)
and [chemical shielding
calculations](../tutorials/Calculating_the_chemical_shieldings.md).

------------------------------------------------------------------------

When [calculating the chemical
shieldings](../tutorials/Calculating_the_chemical_shieldings.md)
or [calculating the electric field
gradient](../tutorials/Calculating_the_electric_field_gradient.md),
`LNMRCAR`` = T` writes the
[NMRCAR.magres](NMRCAR.magres.md) in
<a href="https://www.ccpnc.ac.uk/docs/magres" class="external text"
rel="nofollow">Magres format</a>. Mind that, while the Magres format
does not clearly state if the [macroscopic
susceptibility](../categories/Category-NMR.md)
should be included, here it is included in the chemical shielding.

## Related tags and articles\[<a href="/wiki/index.php?title=LNMRCAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md), [LEFG](LEFG.md)

[Calculating the chemical
shieldings](../tutorials/Calculating_the_chemical_shieldings.md)

[Calculating the electric field
gradient](../tutorials/Calculating_the_electric_field_gradient.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LNMRCAR-_incategory-HowTo)



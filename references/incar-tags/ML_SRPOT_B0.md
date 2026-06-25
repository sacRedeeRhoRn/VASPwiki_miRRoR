<!-- Source: https://vasp.at/wiki/index.php/ML_SRPOT_B0 | revid: 35546 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_SRPOT_B0


ML_SRPOT_B0 = \[real\]  
Default: **ML_SRPOT_B0** = 1.0 

Description: Specifies the height of a soft repulsive exponential
potential used as an auxiliary potential in thermodynamic integration
([VCAIMAGES](VCAIMAGES.md)).

------------------------------------------------------------------------

This parameters sets the height $b$ of the
following repulsive exponential potential

$V(r) = b e^{-(r/\sigma)^n}.$

The height $b$ should be
chosen rather high, since the sole purpose of this potential is to
repell other atoms that come close to the selected atoms chosen by
[ML_NATOM_COUPLED](ML_NATOM_COUPLED.md).

  

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_SRPOT_B0&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_LCOUPLE](ML_LCOUPLE.md),
[ML_ICOUPLE](ML_ICOUPLE.md),
[ML_RCOUPLE](ML_RCOUPLE.md),
[ML_NATOM_COUPLED](ML_NATOM_COUPLED.md),
[ML_LEMPPOT](ML_LEMPPOT.md),
[ML_EMPPOT_RCUT](ML_EMPPOT_RCUT.md),
[ML_SRPOT_N0](ML_SRPOT_N0.md),
[ML_SRPOT_S0](ML_SRPOT_S0.md),
[ML_MOPOT_NM](ML_MOPOT_NM.md),
[ML_MOPOT_DM](ML_MOPOT_DM.md),
[ML_MOPOT_RM](ML_MOPOT_RM.md),
[ML_MOPOT_RKM](ML_MOPOT_RKM.md),
[ML_MOPOT_IJM](ML_MOPOT_IJM.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LCOUPLE-_incategory-Examples)

------------------------------------------------------------------------



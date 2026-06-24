<!-- Source: https://vasp.at/wiki/index.php/ML_MOPOT_RM | revid: 35110 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MOPOT_RM
ML_MOPOT_RM = \[real\]  
Default: **ML_MOPOT_RM** = 1.0 

Description: Specifies the equilibrium bond distance of the Morse
potentials used as auxiliary potentials in thermodynamic integration
([VCAIMAGES](VCAIMAGES.md)).

------------------------------------------------------------------------

This parameter sets the equilibrium bond distance $r_{e}$ of the following Morse potential

$V(r) = D_e (1-e^{-\beta(r-r_{e})})^2 - 1.$

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_LCOUPLE](ML_LCOUPLE.md),
[ML_ICOUPLE](ML_ICOUPLE.md),
[ML_RCOUPLE](ML_RCOUPLE.md),
[ML_NATOM_COUPLED](ML_NATOM_COUPLED.md),
[ML_LEMPPOT](ML_LEMPPOT.md),
[ML_EMPPOT_RCUT](ML_EMPPOT_RCUT.md),
[ML_SRPOT_B0](ML_SRPOT_B0.md),
[ML_SRPOT_N0](ML_SRPOT_N0.md),
[ML_SRPOT_S0](ML_SRPOT_S0.md),
[ML_MOPOT_NM](ML_MOPOT_NM.md),
[ML_MOPOT_DM](ML_MOPOT_DM.md),
[ML_MOPOT_RKM](ML_MOPOT_RKM.md),
[ML_MOPOT_IJM](ML_MOPOT_IJM.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LCOUPLE-_incategory-Examples)

------------------------------------------------------------------------

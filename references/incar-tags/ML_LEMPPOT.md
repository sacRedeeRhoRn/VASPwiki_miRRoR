<!-- Source: https://vasp.at/wiki/index.php/ML_LEMPPOT | revid: 34754 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LEMPPOT
ML_LEMPPOT = \[logical\]  
Default: **ML_LEMPPOT** = .FALSE. 

Description: Enables the use of auxiliary empirical potentials for
thermodynamic integration using
[VCAIMAGES](VCAIMAGES.md).

------------------------------------------------------------------------

ML_LEMPPOT=.TRUE. sets the following defaults:

- [ML_LCOUPLE](ML_LCOUPLE.md)=.TRUE.
- [ML_RCOUPLE](ML_RCOUPLE.md)=0.0

ML_LEMPPOT=.TRUE. requires
[ML_LCOUPLE](ML_LCOUPLE.md)=.TRUE., so no other values
for [ML_LCOUPLE](ML_LCOUPLE.md) are permitted.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_LCOUPLE](ML_LCOUPLE.md),
[ML_ICOUPLE](ML_ICOUPLE.md),
[ML_RCOUPLE](ML_RCOUPLE.md),
[ML_NATOM_COUPLED](ML_NATOM_COUPLED.md),
[ML_EMPPOT_RCUT](ML_EMPPOT_RCUT.md),
[ML_SRPOT_B0](ML_SRPOT_B0.md),
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

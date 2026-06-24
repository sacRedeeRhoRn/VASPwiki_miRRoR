<!-- Source: https://vasp.at/wiki/index.php/ML_LUSE_NAMES | revid: 26028 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LUSE_NAMES
ML_LUSE_NAMES = \[logical\]  
Default: **ML_LUSE_NAMES** = .FALSE. 

Description: Decides whether training structures are additionally
subdivided into groups internally due to their structure name.

------------------------------------------------------------------------

This tag is important if the normalization via averages over subset
standard deviations ([ML_IWEIGHT](ML_IWEIGHT.md)=3) is
employed. By default (ML_LUSE_NAMES=*.FALSE.*) the division into subsets
is based on the atom types and number of atoms per type. If two systems
contain the same atom types and the same number of atoms per type then
they are considered to be in the same subset. To further divide them
into subsets set ML_LUSE_NAMES=*.TRUE.* and choose different system
names in the first line of the [POSCAR](../input-files/POSCAR.md) file.
This can be useful if training is performed for widely different
materials, for instance, different phases with widely different
energies. Without the finer subset assignment, the overall energy
standard deviation might become large, reducing the weight of the
energies too much of given subsets.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_WTOTEN](ML_WTOTEN.md),
[ML_WTIFOR](ML_WTIFOR.md),
[ML_WTSIF](ML_WTSIF.md),
[ML_IWEIGHT](ML_IWEIGHT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_IWEIGHT-_incategory-Examples)

------------------------------------------------------------------------

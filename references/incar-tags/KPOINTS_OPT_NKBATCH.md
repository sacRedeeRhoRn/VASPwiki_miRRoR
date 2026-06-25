<!-- Source: https://vasp.at/wiki/index.php/KPOINTS_OPT_NKBATCH | revid: 22352 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINTS_OPT_NKBATCH


KPOINTS_OPT_NKBATCH =
\[integer\]

Default: KPOINTS_OPT_NKBATCH =
Number of k-points in the irreducible Brillouin zone of the
self-consistent calculation. 

Description:
KPOINTS_OPT_NKBATCH determines
the size of the batch of k-points for the KPOINTS_OPT driver.

------------------------------------------------------------------------

When the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) is present an
additional non-self-consistent calculation is performed after
self-consistency is reached. This one-shot calculation is done in
batches of N k-points to reduce memory usage. Increasing the size of the
batch leads to faster calculation times but higher memory usage in the
non-self-consistent calculation.

## Related tags and articles\[<a
href="/wiki/index.php?title=KPOINTS_OPT_NKBATCH&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LKPOINTS_OPT](LKPOINTS_OPT.md),
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md),
[PROCAR_OPT](../output-files/PROCAR_OPT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LKPOINTS_OPT-_incategory-Examples)

------------------------------------------------------------------------



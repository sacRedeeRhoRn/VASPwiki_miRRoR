<!-- Source: https://vasp.at/wiki/index.php/CUTOFF_SIGMA | revid: 32844 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CUTOFF_SIGMA


CUTOFF_SIGMA = \[real\] (
\[real\] ) 

|                           |       |     |
|---------------------------|-------|-----|
| Default: **CUTOFF_SIGMA** | = 0.1 |     |

Description: CUTOFF_SIGMA
specifies the broadening $\sigma$ in eV
for the cutoff function specified by
[CUTOFF_TYPE](CUTOFF_TYPE.md).

------------------------------------------------------------------------

Corresponds to a broadening of the cutoff function used in the <a
href="/wiki/Wannier_functions#One-shot_single_value_decomposition_(SVD)"
class="mw-redirect" title="Wannier functions">one-shot method</a> to
obtain Wannier functions. The meaning of $\sigma$
depends on the [CUTOFF_TYPE](CUTOFF_TYPE.md) tag.

For spin-polarized calculations ([`ISPIN`](ISPIN.md)` = 2`),
two values can be specified for
CUTOFF_SIGMA, one for each
spin channel. If only a single value is specified, it will be used for
both spin channels.

## Related tags and articles\[<a
href="/wiki/index.php?title=CUTOFF_SIGMA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CUTOFF_TYPE](CUTOFF_TYPE.md),
[CUTOFF_MU](CUTOFF_MU.md), [LSCDM](LSCDM.md),
[LOCPROJ](LOCPROJ.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CUTOFF_SIGMA-_incategory-Examples)

------------------------------------------------------------------------



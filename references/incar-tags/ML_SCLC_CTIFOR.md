<!-- Source: https://vasp.at/wiki/index.php/ML_SCLC_CTIFOR | revid: 25148 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_SCLC_CTIFOR


ML_SCLC_CTIFOR = \[real\]  
Default: **ML_SCLC_CTIFOR** = 0.6 

Description: Sets fraction by which the error threshold for the maximum
forces is lowered in the selection of local reference calculations.

------------------------------------------------------------------------

[ML_CTIFOR](ML_CTIFOR.md) determines whether a
first-principles calculation is performed when training an MLFF.
Whenever a first-principles calculation is performed, additional
functions are added to the sparse representation of the kernel
(local-reference configurations).
ML_SCLC_CTIFOR determines how
many local-reference configurations are added to the sparse
representation of the kernel. Specifically, the local environment of
those atoms with an estimated error larger than
ML_SCLC_CTIFOR \*
[ML_CTIFOR](ML_CTIFOR.md) are added as candidates for the
sparse representational of the kernel. Note that changing
ML_SCLC_CTIFOR does not change
the decision of whether a first-principles calculation is carried out or
not, since this decision is entirely based on
[ML_CTIFOR](ML_CTIFOR.md).

The default value of 0.6 is often a reasonably good compromise. If the
value is decreased, obviously more functions are used for the sparse
representation of the kernel. This always improves the initial learning
efficiency but might slow the force-field calculations. So
ML_SCLC_CTIFOR compromises
either learning efficiency or the speed of the evaluation of the MLFF.
For polymers and liquids, we found that decreasing
ML_SCLC_CTIFOR to values
around 0.4 (or even smaller) can significantly improve learning
efficiency.

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_SCLC_CTIFOR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_CTIFOR](ML_CTIFOR.md), [ML_CX](ML_CX.md),
[ML_EPS_LOW](ML_EPS_LOW.md)

------------------------------------------------------------------------



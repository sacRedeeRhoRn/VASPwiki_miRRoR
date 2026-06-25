<!-- Source: https://vasp.at/wiki/index.php/ML_W1 | revid: 16661 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_W1


ML_W1 = \[real\]  
Default: **ML_W1** = 0.1 

Description: This tag defines the weight $\beta$ for
the radial (and angular) descriptor within the machine learning force
field method (see [this
section](../methods/Machine_learning_force_field-_Theory.md)).

------------------------------------------------------------------------

The weight for the angular descriptor $W_{2}$ is
internally computed from the weight of the radial descriptor
$W_{1}$ as:

$W_{2}=1.0-W_{1}.$

The value for ML_W1 must be
chosen in the interval $\[0, 1\]$.

By default, the angular and radial descriptors are both used although
the latter is weighed less. In principle a weight of 0 for one of them
is selectable which allows the code to internally skip the respective
computation. However, it is generally recommended to use both
descriptors to achieve satisfying training results.

## Related tags and articles\[<a href="/wiki/index.php?title=ML_W1&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_RCUT1](ML_RCUT1.md),
[ML_RCUT2](ML_RCUT2.md),
[ML_SION1](ML_SION1.md),
[ML_SION2](ML_SION2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_W1-_incategory-Examples)

------------------------------------------------------------------------



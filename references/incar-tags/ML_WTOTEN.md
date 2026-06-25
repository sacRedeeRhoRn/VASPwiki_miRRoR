<!-- Source: https://vasp.at/wiki/index.php/ML_WTOTEN | revid: 20743 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_WTOTEN


ML_WTOTEN = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ML_WTOTEN** | = 0.005 | if [ML_IWEIGHT](ML_IWEIGHT.md)=1 |
|  | = 1.0 | otherwise |

Description: Sets a scaling of the fitted potential energy.

------------------------------------------------------------------------

For [ML_IWEIGHT](ML_IWEIGHT.md)=2 and 3 (default), the
potential energy in the training data set is multiplied by
ML_WTOTEN (unitless). We
recommend increasing ML_WTOTEN
if you plan to apply the force field in a simulation where the accuracy
of the total energy is most important. This puts a focus on the energy
error and is desirable, for instance, for the computation of
defect-formation energies.

For [ML_IWEIGHT](ML_IWEIGHT.md)=1,
ML_WTOTEN has the unit of
eV/atom, and the potential energy in the training data set is divided by
it.

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_WTOTEN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_IWEIGHT](ML_IWEIGHT.md),
[ML_WTIFOR](ML_WTIFOR.md),
[ML_WTSIF](ML_WTSIF.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md),
[ML_LMLFF](ML_LMLFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_WTOTEN-_incategory-Examples)

------------------------------------------------------------------------



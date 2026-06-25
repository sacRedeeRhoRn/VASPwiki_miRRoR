<!-- Source: https://vasp.at/wiki/index.php/ML_IWEIGHT | revid: 31943 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_IWEIGHT


ML_IWEIGHT = \[integer\]  
Default: **ML_IWEIGHT** = 3 

Description: This tag controls which procedure is used for normalizing
and weighting the energies, forces, and stresses in the machine learning
force field method.

------------------------------------------------------------------------

To achieve optimal training it is important to normalize the available
data. Furthermore, sometimes it may be desired to emphasize some
training quantities over others, e.g. one might want excellent force
predictions, even at the cost of sacrificing some energy and stress
accuracy. How normalizing and weighting are performed can be controlled
with the ML_IWEIGHT together
with weighting parameters [ML_WTOTEN](ML_WTOTEN.md),
[ML_WTIFOR](ML_WTIFOR.md) and
[ML_WTSIF](ML_WTSIF.md) for energies, forces, and
stresses, respectively. The following procedures can be selected via
ML_IWEIGHT:

- ML_IWEIGHT = 1: Manual
  control over normalization/weighting: the unnormalized energies,
  forces, and stress tensor training data are divided by the weights
  determined by the flags [ML_WTOTEN](ML_WTOTEN.md)
  (eV/atom), [ML_WTIFOR](ML_WTIFOR.md)
  (eV/$\AA$) and
  [ML_WTSIF](ML_WTSIF.md) (kBar), respectively.

<!-- -->

- ML_IWEIGHT = 2:
  Normalization via global standard deviations: The energies, forces,
  and stresses are normalized by their respective standard deviation
  over the entire training data. Then, the normalized quantities are
  weighted by [ML_WTOTEN](ML_WTOTEN.md),
  [ML_WTIFOR](ML_WTIFOR.md) and
  [ML_WTSIF](ML_WTSIF.md) when they are processed for
  learning in the design matrix $\mathbf{\Phi}$ (see [this
  section](../methods/Machine_learning_force_field-_Theory.md)).
  In this case the values of [ML_WTOTEN](ML_WTOTEN.md),
  [ML_WTIFOR](ML_WTIFOR.md) and
  [ML_WTSIF](ML_WTSIF.md) are unitless quantities.

<!-- -->

- ML_IWEIGHT = 3:
  Normalization via averages over subset standard deviations: Same as
  ML_IWEIGHT = 2 but the
  training data is divided into individual subsets. For each subset, the
  standard deviations are calculated separately. Then, the energies,
  forces, and stresses are normalized using the average of the standard
  deviations of all subsets (see also [this
  section](../output-files/ML_LOGFILE.md) for
  details). Finally, as for
  ML_IWEIGHT = 2 the
  normalized quantities are multiplied by
  [ML_WTOTEN](ML_WTOTEN.md),
  [ML_WTIFOR](ML_WTIFOR.md) and
  [ML_WTSIF](ML_WTSIF.md) for learning purposes. By
  default
  ([ML_LUSE_NAMES](ML_LUSE_NAMES.md)=*.FALSE.*) the
  division into subsets is based on the atom types and number of atoms
  per type. If two systems contain the same atom types and the same
  number of atoms per type then they are considered to be in the same
  subset. To further divide them into subsets set
  [ML_LUSE_NAMES](ML_LUSE_NAMES.md)=*.TRUE.* and
  choose different system names in the first line of the
  [POSCAR](../input-files/POSCAR.md) file. This can be useful if training
  is performed for widely different materials, for instance, different
  phases with widely different energies. Without the finer subset
  assignment, the overall energy standard deviation might become large,
  reducing the weight of the energies too much of given subsets.

For ML_IWEIGHT = 2, 3 the
weights are unitless quantities used to multiply the data, whereas for
ML_IWEIGHT = 1 they have a
unit. All three methods provide unitless energies, forces, and stress
tensors, which are then passed to the learning algorithm. Although the
defaults are usually rather sensible, it can be useful to explore
different weights. For instance, if vibrational frequencies are supposed
to be reproduced accurately, we found it helpful to increase
[ML_WTIFOR](ML_WTIFOR.md) to 10-100. On the other hand,
if the energy difference between different phases needs to be described
accurately by the force field, it might be useful to increase
[ML_WTOTEN](ML_WTOTEN.md) to around 10-100.

|  |
|----|
| **Tip:** On-the-fly learning implies that training structures accumulate along the running MD trajectory. Hence, also the standard deviations of energies, forces, and stresses change over time and will be recalculated whenever a learning step is triggered. We highly recommend using ML_IWEIGHT = 3 because this ensures that at any time learning is performed on an adequately normalized set. |

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_IWEIGHT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_WTOTEN](ML_WTOTEN.md),
[ML_WTIFOR](ML_WTIFOR.md),
[ML_WTSIF](ML_WTSIF.md),
[ML_LUSE_NAMES](ML_LUSE_NAMES.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_IWEIGHT-_incategory-Examples)

------------------------------------------------------------------------



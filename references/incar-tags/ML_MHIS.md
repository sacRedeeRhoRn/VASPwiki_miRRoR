<!-- Source: https://vasp.at/wiki/index.php/ML_MHIS | revid: 25142 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MHIS


ML_MHIS = \[integer\]  
Default: **ML_MHIS** = 10 

Description: This tag sets the number of estimated errors stored in
memory to determine the threshold for error estimation in the machine
learning force field method for
[ML_ICRITERIA](ML_ICRITERIA.md)=1. For
[ML_ICRITERIA](ML_ICRITERIA.md)=2, the history length
is 50 x ML_MHIS (or hard coded
to 400).

------------------------------------------------------------------------

The use of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field-_Theory.md).

[ML_ICRITERIA](ML_ICRITERIA.md)=1: The ML code stores
ML_MHIS errors from previous
training steps: immediately after a re-training of the ML-FF, the
estimated errors of the forces are reevaluated for the current structure
(that was also just added as training structure). The average and the
maximum error of the forces is stored in the history. After
ML_MHIS updates of the force
field, the threshold [ML_CTIFOR](ML_CTIFOR.md) is updated
the first time and is then updated after every further update of the
ML-FF. We recommend to read the section
[ML_ICRITERIA](ML_ICRITERIA.md) for further details.

[ML_ICRITERIA](ML_ICRITERIA.md)=2: Averaging is
performed over 50 x ML_MHIS
error predictions. Every MD step is considered in the averaging (as
opposed to above, where only structures after re-training are
considered).

## Related tags and articles\[<a href="/wiki/index.php?title=ML_MHIS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_CTIFOR](ML_CTIFOR.md), [ML_CX](ML_CX.md),
[ML_CSLOPE](ML_CSLOPE.md),
[ML_CSIG](ML_CSIG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_MHIS-_incategory-Examples)

------------------------------------------------------------------------



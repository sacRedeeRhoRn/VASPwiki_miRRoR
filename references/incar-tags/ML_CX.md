<!-- Source: https://vasp.at/wiki/index.php/ML_CX | revid: 25140 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_CX


ML_CX = \[real\]  
Default: **ML_CX** = 0.0 

Description: The parameter determines to which value the threshold
([ML_CTIFOR](ML_CTIFOR.md)) is updated within the machine
learning force field methods.

------------------------------------------------------------------------

The use of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).

If [ML_ICRITERIA](ML_ICRITERIA.md)\>0,
[ML_CTIFOR](ML_CTIFOR.md) is set to the average of the
errors of the forces stored in a history. Note that
[ML_ICRITERIA](ML_ICRITERIA.md)=1 and
[ML_ICRITERIA](ML_ICRITERIA.md)=2, average over
different data. In the first case the average is performed over errors
after updates of the force fields, and in the second case over all
recent error estimates (see
[ML_ICRITERIA](ML_ICRITERIA.md)). In both cases, if
[ML_CTIFOR](ML_CTIFOR.md) is updated, it is set to

[ML_CTIFOR](ML_CTIFOR.md) = (average of the stored errors
in the history) \*(1.0 +
ML_CX).

Obviously setting ML_CX to a
positive value will result in fewer first principles calculations and
fewer updates of the MLFF, whereas negative values result in more
frequent first principles calculations (as well as updates of the MLFF).
Typical values of ML_CX are
between -0.2 and 0.0 for
[ML_ICRITERIA](ML_ICRITERIA.md)=1, and 0.0 and 0.3 for
[ML_ICRITERIA](ML_ICRITERIA.md)=2 (a good starting
value is 0.2 for [ML_ICRITERIA](ML_ICRITERIA.md)=2).
For training runs using heating, the default usually results in very
well balanced machine learned force fields. When the training is
performed at a fixed temperature, it is often desirable to decrease to
ML_CX=-0.1, in order to
increase the number of first principle calculations and thus the size of
the training set (the default can result in too few training data).

The number of entries in the history are controlled by
[ML_MHIS](ML_MHIS.md) for
[ML_ICRITERIA](ML_ICRITERIA.md)=1, and it is currently
fixed to 400 for [ML_ICRITERIA](ML_ICRITERIA.md)=2 (in
future releases 50 x [ML_MHIS](ML_MHIS.md)).

## Related tags and articles\[<a href="/wiki/index.php?title=ML_CX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_CTIFOR](ML_CTIFOR.md),
[ML_MHIS](ML_MHIS.md), [ML_CSIG](ML_CSIG.md),
[ML_CSLOPE](ML_CSLOPE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LCRITERIA-_incategory-Examples)

------------------------------------------------------------------------



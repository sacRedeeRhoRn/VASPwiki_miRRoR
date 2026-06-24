<!-- Source: https://vasp.at/wiki/index.php/ML_ICRITERIA | revid: 36300 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_ICRITERIA
ML_ICRITERIA = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **ML_ICRITERIA** | = 3 | if [`ML_MODE`](ML_MODE.md)` = SELECT` and [`ML_CALGO`](ML_CALGO.md)` = 0` |
|  | = 1 | if [`ML_MODE`](ML_MODE.md)` != SELECT` and [`ML_CALGO`](ML_CALGO.md)` = 0` |
|  | = 0 | if [`ML_CALGO`](ML_CALGO.md)` = 1` |

  
Description: Decides how the error threshold
([ML_CTIFOR](ML_CTIFOR.md)) is updated within the machine
learning force field method. [ML_CTIFOR](ML_CTIFOR.md)
determines whether a first-principles calculation is performed.

------------------------------------------------------------------------

The use of this tag in combination with the learning algorithms is
described here:
[here](../methods/Machine_learning_force_field_calculations-_Basics.md).

The following options are possible for ML_ICRITERIA:

- `ML_ICRITERIA`` = 0`: The threshold
  [ML_CTIFOR](ML_CTIFOR.md) is not updated. This method
  is the only method used for
  [`ML_CALGO`](ML_CALGO.md)` = 1`. For
  [`ML_CALGO`](ML_CALGO.md)` = 0`, this method is only
  recommended for refining an existing force field. For example, if you
  know that [ML_CTIFOR](ML_CTIFOR.md) has taken a value
  of 0.03 in previous runs, you can continue to collect training data by
  now setting the threshold to
  [`ML_CTIFOR`](ML_CTIFOR.md)` = 0.03` to capture all
  contours and areas of the potential energy surface where
  first-principles data are still missing. To achieve extremely robust
  force fields, it is recommended to run
  [`NSW`](NSW.md)` = 100000` steps in this mode to slightly
  above the highest temperature to be considered.
- `ML_ICRITERIA`` = 1`: Set [ML_CTIFOR](ML_CTIFOR.md) to
  a value proportional to the average errors of the
  [ML_MHIS](ML_MHIS.md) steps. `ML_ICRITERIA`` = 1`, the
  average is calculated only for errors after updating the force field.
  Such updates are quite rare, so updates of
  [ML_CTIFOR](ML_CTIFOR.md) are also quite rare in this
  mode. Furthermore, since the first principle calculations are only
  performed for configurations with large errors ("outliers"), the force
  field is updated only after the outliers are taken into account.
  Therefore, the errors included in the averaging are typically larger
  than the average error in this mode. It is therefore recommended to
  set [ML_CX](ML_CX.md) to 0 (default) in this mode.
- `ML_ICRITERIA`` = 2`: Update the criteria using the moving average of
  all previous errors. This method gives the average of the errors of
  all previous predictions (i.e. all previously considered MD steps),
  while `ML_ICRITERIA`` = 1` gives only the average of the predictions
  immediately following the retraining. The length of the history in
  this mode is currently hard-coded and set to 400 steps (or
  [ML_MHIS](ML_MHIS.md) x 50 in the newer version). This
  mode tends to continue sampling, and is therefore somewhat prone to
  oversampling: as errors decrease, the threshold is steadily lowered
  and additional first-principles computations are initiated. The
  recommended values for [ML_CX](ML_CX.md) in this mode are
  approximately 0.1 to 0.3. For [`ML_CX`](ML_CX.md)` = 0.2`,
  a first-principles calculation is typically performed every 50 steps.
  This means that if the number of ionic steps is, say,
  [`NSW`](NSW.md)` = 50000`, then about 1000 first-principles
  calculations should be performed. For many materials, this results in
  a reasonably good and robust ML database.
- `ML_ICRITERIA`` = 3`: This mode is the default for reselecting local
  reference configurations from an existing [ML_AB](../input-files/ML_AB.md)
  file ([`ML_MODE`](ML_MODE.md)` = select`). The
  [ML_AB](../input-files/ML_AB.md) file shall contain a
  [ML_CTIFOR](ML_CTIFOR.md) for each structure stored in
  the [ML_AB](../input-files/ML_AB.md) file. These values are used by VASP
  as error thresholds for structure selection. This also means that the
  tags [ML_CTIFOR](ML_CTIFOR.md),
  [ML_CX](ML_CX.md),
  [ML_CSLOPE](ML_CSLOPE.md),
  [ML_CSIG](ML_CSIG.md) and
  [ML_MHIS](ML_MHIS.md) set in [INCAR](../input-files/INCAR.md)
  are ignored. This mode is only available when
  [`ML_MODE`](ML_MODE.md)` = select` is activated. It is
  important that the [ML_AB](../input-files/ML_AB.md) file contains a
  [ML_CTIFOR](ML_CTIFOR.md) value for each structure
  included. Otherwise, VASP will throw an error and will also indicate
  to the user that some [ML_CTIFOR](ML_CTIFOR.md) values
  are missing from the [ML_AB](../input-files/ML_AB.md) file.

As mentioned above, the [ML_CX](ML_CX.md) tag can be used to
fine-tune the update of [ML_CTIFOR](ML_CTIFOR.md). The
fact that the `ML_ICRITERIA`` = 1` or `ML_ICRITERIA`` = 2` is a matter
of taste. Just remember that [ML_CX](ML_CX.md) must be set
differently in both modes. While `ML_ICRITERIA`` = 1`, the
[`ML_CX`](ML_CX.md)` = 0.0`, `ML_ICRITERIA`` = 2`,
[`ML_CX`](ML_CX.md)` = 0.2` is a good default. Most of our
force fields use `ML_ICRITERIA`` = 1`, but this mode sometimes stagnates
and stops the first principle calculations. On the other hand, and as
already mentioned, using `ML_ICRITERIA`` = 2` is prone to oversampling,
i.e. it may perform too many first principle calculations.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_CTIFOR](ML_CTIFOR.md),
[ML_CSLOPE](ML_CSLOPE.md),
[ML_CSIG](ML_CSIG.md), [ML_MHIS](ML_MHIS.md),
[ML_CX](ML_CX.md), [ML_CALGO](ML_CALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_ICRITERIA-_incategory-Examples)

------------------------------------------------------------------------

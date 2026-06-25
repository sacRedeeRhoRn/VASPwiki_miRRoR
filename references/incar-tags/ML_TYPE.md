<!-- Source: https://vasp.at/wiki/index.php/ML_TYPE | revid: 35694 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_TYPE


ML_TYPE = kernel \| vasp \|
grace  
Default: **ML_TYPE** = kernel 

Description: String-based tag selecting type of machine-learned force
field to use.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

Given that machine-learned force fields are enabled
([`ML_LMLFF`](ML_LMLFF.md)` = .TRUE.`) this tag selects
which type of force field is used.

- `ML_TYPE`` = kernel, vasp`:

  Use VASP's native [machine-learned force
  fields](#Category:Machine-learned_force_fields) with theoretical
  background described
  [here](../methods/Machine_learning_force_field-_Theory.md).
  The strings `kernel` and `vasp` are synonymous in this context.

- `ML_TYPE`` = grace`:

  Use [GRACE force
  fields](../methods/Running_GRACE_force_fields_in_VASP.md),
  available only for [`ML_MODE`](ML_MODE.md)` = run` if
  [GRACE
  support](../misc/Makefile.include.md) is
  enabled at compile time.

## Related tags and articles\[<a href="/wiki/index.php?title=ML_TYPE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_GRACE_MODEL](ML_GRACE_MODEL.md)

------------------------------------------------------------------------



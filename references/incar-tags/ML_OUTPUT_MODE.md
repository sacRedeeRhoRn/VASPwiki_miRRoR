<!-- Source: https://vasp.at/wiki/index.php/ML_OUTPUT_MODE | revid: 32851 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_OUTPUT_MODE
|  |  |  |
|----|----|----|
| Default: **ML_OUTPUT_MODE** | = 0 | if [`ML_MODE`](ML_MODE.md)` = run` |
|  | = 1 | else |

Description: This tag allows to disable certain file output which helps
to increase performance in molecular-dynamics simulations with
machine-learned force fields in prediction-only mode
([`ML_MODE`](ML_MODE.md)` = run`).

|                                                        |
|--------------------------------------------------------|
| **Mind:** This tag is only available as of VASP.6.4.0. |

------------------------------------------------------------------------

This tag is useful in combination with
[ML_OUTBLOCK](ML_OUTBLOCK.md) to further reduce
per-time-step calculations and file output. The following options exist
for this tag:

- `ML_OUTPUT_MODE`` = 1`: **Normal operation**, output is written as
  usual in ab-initio molecular-dynamics simulations.
- `ML_OUTPUT_MODE`` = 0`: **Reduced file output mode**, in contrast to
  normal operation the following changes apply:
  - Pair-correlation functions are not computed.
  - No output to [PCDAT](../output-files/PCDAT.md) file.
  - No `pair_correlation` output section in
    [vaspout.h5](../output-files/Vaspout.h5.md).
  - No `structure`, `varray name="forces"` and `varray name="stress"`
    output sections in [vasprun.xml](../output-files/Vasprun.xml.md).

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_LFAST](ML_LFAST.md),
[ML_IERR](../redirects/ML_IERR.md),
[ML_OUTBLOCK](ML_OUTBLOCK.md)

------------------------------------------------------------------------

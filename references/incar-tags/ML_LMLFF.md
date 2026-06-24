<!-- Source: https://vasp.at/wiki/index.php/ML_LMLFF | revid: 22182 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LMLFF
ML_LMLFF = \[logical\]  
Default: **ML_LMLFF** = .FALSE. 

Description: Main control tag which enables/disables the use of machine
learning force fields.

|  |
|----|
| **Mind:** Machine learning force fields is available in VASP as of version 6.3.0 |

------------------------------------------------------------------------

If ML_LMLFF = .FALSE. machine learning force fields are disabled and all
related [INCAR](../input-files/INCAR.md) tags, i.e. all tags starting with
"**ML\_**", are ignored. If machine learning force fields are used by
setting ML_LMLFF = .TRUE., the VASP mode of operation depends on the
choice of [ML_MODE](ML_MODE.md). If
[ML_MODE](ML_MODE.md) is not supplied in the
[INCAR](../input-files/INCAR.md) file then the default mode of operation is
to run an MD simulation with on-the-fly machine learning, i.e.,
[`ML_MODE`](ML_MODE.md)` = train`. This training is started
"from scratch" if no [ML_AB](../input-files/ML_AB.md) file is provided,
otherwise a continuation run is performed.

## Related tags and articles
[ML_MODE](ML_MODE.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md),
[ML_IWEIGHT](ML_IWEIGHT.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_IREG](ML_IREG.md),
[ML_LSPARSDES](ML_LSPARSDES.md),
[ML_ISCALE_TOTEN](ML_ISCALE_TOTEN.md),
[ML_LCOUPLE](ML_LCOUPLE.md),
[ML_LHEAT](ML_LHEAT.md),
[ML_LEATOM](ML_LEATOM.md), [ML_MB](ML_MB.md),
[ML_MCONF](ML_MCONF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LMLFF-_incategory-Examples)

------------------------------------------------------------------------

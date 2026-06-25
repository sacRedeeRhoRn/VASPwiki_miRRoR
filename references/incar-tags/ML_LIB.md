<!-- Source: https://vasp.at/wiki/index.php/ML_LIB | revid: 29884 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LIB


ML_LIB = \[logical\] 

|  |  |  |
|----|----|----|
| Default: **ML_LIB** | = .TRUE. | if compiled with [VASPml library](../methods/VASPml_library.md) (precompiler flag `-Dlibvaspml`) |
|  | = .FALSE. | else |

Description: ML_LIB
enables/disables the use of the [VASPml C++
library](../methods/VASPml_library.md) for machine-learning
features.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Some machine learning modes of operation
([ML_MODE](ML_MODE.md)) are implemented twice in VASP, once
in the original Fortran code and again in a C++ rewrite as part of the
VASPml library. However, the supported features and
[INCAR](../input-files/INCAR.md) tags may be
[different](../methods/VASPml_library.md). For
example, the C++ library does not yet implement the thermodynamic
integration method. The ML_LIB
tag allows to switch seamlessly between the two code paths without the
need to recompile VASP.

## Related tags and articles\[<a href="/wiki/index.php?title=ML_LIB&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LIB-_incategory-Examples)

------------------------------------------------------------------------



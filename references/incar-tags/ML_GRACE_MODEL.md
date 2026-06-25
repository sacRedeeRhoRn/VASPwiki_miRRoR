<!-- Source: https://vasp.at/wiki/index.php/ML_GRACE_MODEL | revid: 35695 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_GRACE_MODEL


ML_GRACE_MODEL = \[string\]  
Default: **ML_GRACE_MODEL** = ./SavedModel 

Description: String-based tag specifying the GRACE force field name or
path.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

If [GRACE force
fields](../methods/Running_GRACE_force_fields_in_VASP.md)
are requested via [`ML_TYPE`](ML_TYPE.md)` = grace` this
tag allows to select the actual model to use in two ways:

1.  The ML_GRACE_MODEL tag may
    be used to provide just the model name. In this case the model is
    assumed to reside in the default `tensorpotential` download
    directory `~/.cache/grace`.
2.  If a full path is provided in the
    ML_GRACE_MODEL tag then
    the model at this exact location is used.

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_GRACE_MODEL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md), [ML_TYPE](ML_TYPE.md)

------------------------------------------------------------------------



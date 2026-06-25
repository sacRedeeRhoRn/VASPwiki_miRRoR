<!-- Source: https://vasp.at/wiki/index.php/LNMRSHIELD | revid: 34600 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNMRSHIELD


LNMRSHIELD = .TRUE.\| .FALSE. 

|                         |          |     |
|-------------------------|----------|-----|
| Default: **LNMRSHIELD** | = .TRUE. |     |

Description: LNMRSHIELD
controls whether the shielding or shift is printed.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

The chemical shielding $\sigma_{ij}$
is printed by default (i.e.
LNMRSHIELD = .TRUE.) in the
[OUTCAR](../output-files/OUTCAR.md) file. When
LNMRSHIELD = .FALSE. is set,
the chemical shift $\delta_{ij}$
is printed instead ($\delta_{i,j} = -\sigma_{ij}$), as was the default prior to VASP.6.6.0.

|  |
|----|
| **Mind:** The NICS is always shielding and is unaffected by LNMRSHIELD. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LNMRSHIELD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md)



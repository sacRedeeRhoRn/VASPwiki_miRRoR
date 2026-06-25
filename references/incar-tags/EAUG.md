<!-- Source: https://vasp.at/wiki/index.php/EAUG | revid: 25195 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EAUG


EAUG = \[real\]  
Default: **EAUG** = value read from [POTCAR](../input-files/POTCAR.md) 

Description: EAUG specifies
the energy cutoff for the plane-wave representation for the augmentation
charges in eV for the pseudopotential it is read from.

------------------------------------------------------------------------

For a multi-element [POTCAR](../input-files/POTCAR.md) file, the maximum
EAUG determines the cutoff
energy for the plane-wave representation of the augmentation charges.

|  |
|----|
| **Deprecated:** The value of EAUG can be overwritten by setting [ENAUG](ENAUG.md) in the [INCAR](../input-files/INCAR.md) file, but this functionality is deprecated and should not be used anymore. |

## Related tags and articles\[<a href="/wiki/index.php?title=EAUG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[POTCAR](../input-files/POTCAR.md),
<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a>

------------------------------------------------------------------------



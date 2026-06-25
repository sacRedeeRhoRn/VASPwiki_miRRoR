<!-- Source: https://vasp.at/wiki/index.php/LEXCH | revid: 25130 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LEXCH


LEXCH = \[string\] 
LEXCH = CA.OR.PBE 

|  |  |  |
|----|----|----|
| Default: **LEXCH** | = CA | for LDA <a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a> |
|  | = PE | for GGA <a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a> |

Definition: Set the default exchange-correlation functional.

------------------------------------------------------------------------

The functional specified by
LEXCH was used as a reference
when the PAW potential was created. The transferability of PAW
potentials to other
<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">exchange-correlation
functionals</a> is quite good. So, the functional used during the
calculation can be freely adjusted (despite the very prominent warning
in the stdout).

## Related tags and articles\[<a href="/wiki/index.php?title=LEXCH&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">Exchange-correlation
functionals</a>, [XC](XC.md), [XC_C](XC_C.md)
[GGA](GGA.md), [METAGGA](METAGGA.md),
[POTCAR](../input-files/POTCAR.md),
<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a>



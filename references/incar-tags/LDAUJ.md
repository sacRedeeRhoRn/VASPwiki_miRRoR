<!-- Source: https://vasp.at/wiki/index.php/LDAUJ | revid: 36500 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDAUJ


LDAUJ = \[real array\]  
Default: **LDAUJ** = NTYP\*0.0 

Description: Sets the effective on-site exchange interactions (eV).

------------------------------------------------------------------------

LDAUJ specifies the strength
of the effective on-site exchange interactions in eV. It must hold one
value for each atomic species.

|  |
|----|
| **Warning:** The total energy will depend on the parameters $U$ ([LDAUU](LDAUU.md)) and $J$ (LDAUJ). It is, therefore, not meaningful to compare the total energies resulting from calculations with different $U$ and/or $J$; or $U-J$ in the case of Dudarev's approach ([LDAUTYPE](LDAUTYPE.md)=2). |

|  |
|----|
| **Mind:** For [LDAUTYPE](LDAUTYPE.md)=3, the [LDAUU](LDAUU.md) and LDAUJ tags specify the strength (in eV) of the spherical potential acting on the spin-up and spin-down manifolds, respectively. |

## Related tags and articles\[<a href="/wiki/index.php?title=LDAUJ&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LDAU](LDAU.md), [LDAUTYPE](LDAUTYPE.md),
[LDAUL](LDAUL.md), [LDAUU](LDAUU.md),
[LDAUPRINT](LDAUPRINT.md),
[LMAXMIX](LMAXMIX.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LDAUJ-_incategory-Examples)

------------------------------------------------------------------------



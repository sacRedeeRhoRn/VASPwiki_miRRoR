<!-- Source: https://vasp.at/wiki/index.php/BEXX | revid: 34283 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BEXX


BEXX = \[real\] 

|                   |     |                                              |
|-------------------|-----|----------------------------------------------|
| Default: **BEXX** | = 1 | if [LHFCALC](LHFCALC.md)=.TRUE. |

Description: BEXX specifies
the fraction of short-range exact exchange in range-separated
hybrid-functionals constructed with
[LMODELHF](LMODELHF.md)=.TRUE.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

|  |
|----|
| **Important:** Until VASP.6.5.1, the fraction of short-range exact exchange (when [LMODELHF](LMODELHF.md)=.TRUE.) was fixed to 1 and could not be changed. |

------------------------------------------------------------------------

The BEXX tag specifies the
fraction of short-range exact exchange in range-separated
hybrid-functionals. This tag can be used only when
[LMODELHF](LMODELHF.md)=.TRUE. More details can be found
in the description of this class of [hybrid
functionals](../methods/Hybrid_functionals-_formalism.md)_with_different_mixings "Hybrid functionals: formalism").

## Related tags and articles\[<a href="/wiki/index.php?title=BEXX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[AEXX](AEXX.md), [LMODELHF](LMODELHF.md),
[ALDAX](ALDAX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md),
[HFSCREEN](HFSCREEN.md),
[LRHFCALC](LRHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-BEXX-_incategory-Examples)

------------------------------------------------------------------------



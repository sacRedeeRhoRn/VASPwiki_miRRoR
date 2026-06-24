<!-- Source: https://vasp.at/wiki/index.php/AGGAX | revid: 24206 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AGGAX
AGGAX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **AGGAX** | = 1.0-[AEXX](AEXX.md) | if [LHFCALC](LHFCALC.md)=.TRUE. |
|  | = 1.0 | if [LHFCALC](LHFCALC.md)=.FALSE. |

Description: AGGAX is a parameter that multiplies the gradient
correction in the GGA exchange functional.

------------------------------------------------------------------------

AGGAX can be used as the fraction of gradient correction in the GGA
exchange in a Hartree-Fock/GGA hybrid functional.

|  |
|----|
| **Important:** AGGAX can be used only if [LHFCALC](LHFCALC.md)=.TRUE. |

[TABLE]

## Related tags and articles
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AGGAX-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/ALDAX | revid: 24207 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ALDAX
ALDAX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ALDAX** | = 1.0-[AEXX](AEXX.md) | if [LHFCALC](LHFCALC.md)=.TRUE. |
|  | = 1.0 | if [LHFCALC](LHFCALC.md)=.FALSE. |

Description: ALDAX is a parameter that multiplies the LDA exchange
functional or the LDA part of the GGA exchange functional.

------------------------------------------------------------------------

ALDAX can be used as the fraction of LDA exchange in a Hartree-Fock/DFT
hybrid functional.

|  |
|----|
| **Important:** ALDAX can be used only if [LHFCALC](LHFCALC.md)=.TRUE. |

[TABLE]

## Related tags and articles
[AEXX](AEXX.md), [ALDAC](ALDAC.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ALDAX-_incategory-Examples)

------------------------------------------------------------------------

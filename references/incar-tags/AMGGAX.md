<!-- Source: https://vasp.at/wiki/index.php/AMGGAX | revid: 25513 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AMGGAX
AMGGAX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **AMGGAX** | = 1.0-[AEXX](AEXX.md) | if [LHFCALC](LHFCALC.md)=.TRUE. |
|  | = 1.0 | if [LHFCALC](LHFCALC.md)=.FALSE. |

Description: AMGGAX is a parameter that multiplies the meta-GGA exchange
functional (available as of VASP.6.4.0).

------------------------------------------------------------------------

AMGGAX can be used as the fraction of meta-GGA exchange in a
Hartree-Fock/DFT hybrid functional (possible since VASP.6.4.0).

|  |
|----|
| **Important:** AMGGAX can be used only if [LHFCALC](LHFCALC.md)=.TRUE. |

[TABLE]

## Related tags and articles
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AMGGAX-_incategory-Examples)

------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/ALDAC | revid: 23561 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ALDAC
ALDAC = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ALDAC** | = 1.0 | if [LHFCALC](LHFCALC.md)$=$.FALSE. or [AEXX](AEXX.md)$\neq$1.0 |
|  | = 0.0 | if [LHFCALC](LHFCALC.md)$=$.TRUE. and [AEXX](AEXX.md)$=$1.0 |

Description: ALDAC is a parameter that multiplies the LDA correlation
functional or the LDA part of the GGA correlation functional.

------------------------------------------------------------------------

ALDAC can be used as the fraction of LDA correlation in a
Hartree-Fock/DFT hybrid functional.

[TABLE]

## Related tags and articles
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ALDAC-_incategory-Examples)

------------------------------------------------------------------------

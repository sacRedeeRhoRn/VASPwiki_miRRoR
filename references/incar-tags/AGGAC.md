<!-- Source: https://vasp.at/wiki/index.php/AGGAC | revid: 23577 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AGGAC
AGGAC = \[real\] 

|  |  |  |
|----|----|----|
| Default: **AGGAC** | = 1.0 | if [LHFCALC](LHFCALC.md)$=$.FALSE. or [AEXX](AEXX.md)$\neq$1.0 |
|  | = 0.0 | if [LHFCALC](LHFCALC.md)$=$.TRUE. and [AEXX](AEXX.md)$=$1.0 |

Description: AGGAC is a parameter that multiplies the gradient
correction in the GGA correlation functional.

------------------------------------------------------------------------

AGGAC can be used as the fraction of gradient correction in the GGA
correlation in a Hartree-Fock/DFT hybrid functional.

[TABLE]

## Related tags and articles
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AMGGAX](AMGGAX.md), [AMGGAC](AMGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AGGAC-_incategory-Examples)

------------------------------------------------------------------------

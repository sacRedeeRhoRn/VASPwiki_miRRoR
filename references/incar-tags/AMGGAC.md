<!-- Source: https://vasp.at/wiki/index.php/AMGGAC | revid: 25514 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AMGGAC
AMGGAC = \[real\] 

|  |  |  |
|----|----|----|
| Default: **AMGGAC** | = 1.0 | if [LHFCALC](LHFCALC.md)$=$.FALSE. or [AEXX](AEXX.md)$\neq$1.0 |
|  | = 0.0 | if [LHFCALC](LHFCALC.md)$=$.TRUE. and [AEXX](AEXX.md)$=$1.0 |

Description: AMGGAC is a parameter that multiplies the meta-GGA
correlation functional (available as of VASP.6.4.0).

------------------------------------------------------------------------

AMGGAC can be used as the fraction of meta-GGA correlation in a
Hartree-Fock/DFT hybrid functional.

|  |
|----|
| **Mind:** Note the difference with respect to [AGGAC](AGGAC.md): AMGGAC multiplies the whole meta-GGA correlation functional, while [AGGAC](AGGAC.md) multiplies only the gradient-correction term of a GGA correlation functional. |

## Related tags and articles
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAX](AMGGAX.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AMGGAC-_incategory-Examples)

------------------------------------------------------------------------

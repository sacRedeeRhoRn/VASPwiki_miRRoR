<!-- Source: https://vasp.at/wiki/index.php/LEXCH | revid: 25130 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LEXCH
LEXCH = \[string\]  LEXCH = CA.OR.PBE 

|  |  |  |
|----|----|----|
| Default: **LEXCH** | = CA | for LDA [pseudopotentials](../redirects/Pseudopotentials.md) |
|  | = PE | for GGA [pseudopotentials](../redirects/Pseudopotentials.md) |

Definition: Set the default exchange-correlation functional.

------------------------------------------------------------------------

The functional specified by LEXCH was used as a reference when the PAW
potential was created. The transferability of PAW potentials to other
[exchange-correlation
functionals](../redirects/Exchange-correlation_functionals.md)
is quite good. So, the functional used during the calculation can be
freely adjusted (despite the very prominent warning in the stdout).

## Related tags and articles
[Exchange-correlation
functionals](../redirects/Exchange-correlation_functionals.md),
[XC](XC.md), [XC_C](XC_C.md) [GGA](GGA.md),
[METAGGA](METAGGA.md), [POTCAR](../input-files/POTCAR.md),
[pseudopotentials](../redirects/Pseudopotentials.md)

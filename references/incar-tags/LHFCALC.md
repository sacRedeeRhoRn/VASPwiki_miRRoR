<!-- Source: https://vasp.at/wiki/index.php/LHFCALC | revid: 34124 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LHFCALC
LHFCALC = .TRUE. \| .FALSE.  
Default: **LHFCALC** = .FALSE. 

Description: LHFCALC specifies whether a Hartree-Fock/DFT hybrid
functional type calculation is performed.

------------------------------------------------------------------------

If one does not specifically request a particular hybrid functional (see
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAX](AMGGAX.md),
[AMGGAC](AMGGAC.md), and the
[list_of_hybrid_functionals](../methods/List_of_hybrid_functionals.md))
VASP will default to the [PBE0 hybrid
functional](../methods/List_of_hybrid_functionals.md).

|  |
|----|
| **Tip:** For the most reliable convergence, select a "direct optimization" algorithm for HF/DFT hybrid functonal type calculations, i.e., [`ALGO`](ALGO.md)` = Damped` ([`IALGO`](IALGO.md)` = 53`) or [`ALGO`](ALGO.md)` = All` ([`IALGO`](IALGO.md)` = 58`) in the [INCAR](../input-files/INCAR.md) file. You may also consider [`ALGO`](ALGO.md)` = Normal` which in combination with [`LFOCKACE`](LFOCKACE.md)` = TRUE` (the default) can be a fast alternative. Do not use [`ALGO`](ALGO.md)` = Fast` which is not properly supported (note: no warning is printed). |

If the blocked-Davidson algorithm [`ALGO`](ALGO.md)` = Normal`
is used, in many cases the Pulay mixer will be unable to determine the
proper ground-state. We hence recommend to select the blocked-Davidson
algorithm only in combination with straight mixing or a Kerker-like
mixing (see the [section on
mixing](../redirects/Density_mixing.md)). The following
combination have been successfully applied for small and medium-sized
systems

    LHFCALC = .TRUE. ; ALGO = Normal ; IMIX = 1 ; AMIX = a

Decrease the parameter a until convergence is reached.

In most cases, however, it is recommended to use the "Damped" algorithm
with a suitably chosen timestep. The following setup for the electronic
optimization works reliably in most cases:

    LHFCALC = .TRUE. ; ALGO = Damped ; TIME = 0.5

If convergence is not obtained, it is recommended to reduce the timestep
[TIME](TIME.md).

|  |
|----|
| **Mind:** The stress tensor is not calculated by default for `LHFCALC`` = .TRUE.` (i.e., [`ISIF`](ISIF.md)` = 0`) as it is expensive for hybrid functionals. It can be turned on by setting [`ISIF`](ISIF.md)` = 2`. |

## Related tags and articles
[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAX](AMGGAX.md),
[AMGGAC](AMGGAC.md), [HFSCREEN](HFSCREEN.md),
[LTHOMAS](LTHOMAS.md),
[LRHFCALC](LRHFCALC.md),
[LFOCKACE](LFOCKACE.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LHFCALC-_incategory-Examples)

------------------------------------------------------------------------

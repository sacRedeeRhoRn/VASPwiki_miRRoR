<!-- Source: https://vasp.at/wiki/index.php/LFOCKSTD | revid: 33485 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LFOCKSTD


LFOCKSTD = \[logical\]  
Default: **LFOCKSTD** = .FALSE. 

Description: LFOCKSTD applies
to RPA and GW calculations. It forces VASP to evaluate the exact
exchange fully consistent with the standard treatment in HF
calculations.

------------------------------------------------------------------------

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

This feature is availabe for low-scaling
[ACFDT/random-phase-approximation
(RPA)](../methods/ACFDT__RPA_calculations.md) and
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a>, i.e.
[ALGO](ALGO.md)=ACFDTR, RPAR, EVGW0R, GWR.

VASP typically employs shape restoration (see
<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a> and
<a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a>) to calculate the RPA correlation
energy and the exact exchange energy during RPA/GW calculations.
However, this results in significant noise in the exact exchange energy
and its nuclear gradients. To mitigate this issue, the
LFOCKSTD option was
introduced, forcing VASP to use the standard HF treatment for the exact
exchange while continuing to use shape restoration for the correlation
energy. This reduces the noise in energies and RPA forces, and it leads
to an exact exchange energy that is fully compatible with the exact
exchange energy in standard HF calculations. This means that the energy
`HF-free energy      FHF` in RPA calculations is identical to the
`free  energy   TOTEN` when reading the WAVECAR file and performing a
single-step total energy evaluation ( [ALGO](ALGO.md) =
Eigenval; [LHFCALC](LHFCALC.md) = .TRUE. ;
[AEXX](AEXX.md) = 1.0 ; [NELM](NELM.md) = 1). In
other words, when using LFOCKSTD in RPA calculations, the exact exchange
energy is fully compatible with the stepwise evaluation explained here:
[step wise computation of the total
energy](../methods/ACFDT__RPA_calculations.md).

It is strongly recommended to activate
LFOCKSTD for all GW and RPA
calculations starting from version 6.6.0

Note that VASP uses one-center terms to correct the exact exchange
energy for the difference in shape between all-electron and pseudo
orbitals. Therefore, shape restoration is neither required nor
beneficial for the exact exchange term (see
<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a> and
<a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a>).

## Related tags and articles\[<a href="/wiki/index.php?title=LFOCKSTD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LRPAFORCE](LRPAFORCE.md)

------------------------------------------------------------------------



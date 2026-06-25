<!-- Source: https://vasp.at/wiki/index.php/LFINITE_TEMPERATURE | revid: 24255 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LFINITE_TEMPERATURE


LFINITE_TEMPERATURE =
\[logical\]  
Default: **LFINITE_TEMPERATURE** = .FALSE. 

Description:
LFINITE_TEMPERATURE switches
on the finite-temperature formalism of many-body perturbation theory for
adiabatic-connection-fluctuation-dissipation-theorem (ACFDT)/GW
calculations.

------------------------------------------------------------------------

This feature is available as of VASP.6.1.0 for
ACFDT/random-phase-approximation (RPA), i.e.,
[ALGO](ALGO.md)=ACFDT, ACFDTR, ACFDTRK, and low-scaling
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a>, i.e.,
[ALGO](ALGO.md)=EVGW0R, GWR\[K\].

For
LFINITE_TEMPERATURE=.TRUE., a
compressed
[Matsubara-frequency](https://vasp.at/wiki/index.php/Matsubara_formalism)
grid is used (instead of the zero-temperature formalism of many-body
perturbation theory). This allows for GW and RPA calculations for
metallic systems.
[^Kaltak:PRB:2020-1]
To this end, the electronic temperature is set with the k-point smearing
parameter [SIGMA](SIGMA.md) in units of eV, e.g. a value of
$\sigma=1 eV$ corresponds to a electronic temperature of
$T\approx 11 604 K$.

|  |
|----|
| **Warning:** Can only be used in combination with Fermi smearing [ISMEAR](ISMEAR.md) = -1. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LFINITE_TEMPERATURE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NOMEGA](NOMEGA.md),
[NOMEGAPAR](NOMEGAPAR.md),
[NTAUPAR](NTAUPAR.md), [ISMEAR](ISMEAR.md)

------------------------------------------------------------------------

[^Kaltak:PRB:2020-1]: [M. Kaltak and G. Kresse, Phys. Rev. B. **101**, 205145 (2020).](https://doi.org/10.1103/PhysRevB.101.205145)

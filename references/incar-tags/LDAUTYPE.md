<!-- Source: https://vasp.at/wiki/index.php/LDAUTYPE | revid: 36503 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDAUTYPE


LDAUTYPE = 1 \| 2 \| 4  
Default: **LDAUTYPE** = 2 

Description: LDAUTYPE
specifies the DFT+U variant that will be used.

------------------------------------------------------------------------

The following variants of the
[DFT+U](../methods/Category-DFT+U.md) are available:

- LDAUTYPE=1: The rotationally
  invariant DFT+U introduced by Liechtenstein *et
  al.*[^liechtenstein:prb:95-1]

<!-- -->

- LDAUTYPE=2: The simplified
  (rotationally invariant) approach to DFT+U, introduced by Dudarev *et
  al.*[^dudarev:prb:98-2]

<!-- -->

- LDAUTYPE=3: Linear response
  ansatz of Cococcioni et al.
  [^cococcioni:2005-3]
  to compute U. See [how to calculate
  U](../misc/Calculate_U_for_LSDA+U.md).

|  |
|----|
| **Mind:** For LDAUTYPE=3, the [LDAUU](LDAUU.md) and [LDAUJ](LDAUJ.md) tags specify the strength of the spherical potential acting on the spin-up and spin-down manifolds, respectively. |

- LDAUTYPE=4: Same as
  LDAUTYPE=1, but without
  exchange splitting.

A method to estimate the parameters for DFT+U is the
<a href="/wiki/Constrained-random-phase_approximation"
class="mw-redirect"
title="Constrained-random-phase approximation">constrained-random-phase
approximation</a>. Another method is the linear response ansatz with
LDAUTYPE=3, mentioned above.
On the other hand, in many applications, the DFT+U parameters are used
as tuning parameters to fit experimental data.

|  |
|----|
| **Tip:** For band-structure calculations, increase [LMAXMIX](LMAXMIX.md) to 4 ($d$ elements) or 6 ($f$ elements). |

This is because the [CHGCAR](../input-files/CHGCAR.md) file contains only
information up to angular momentum quantum number set by
[LMAXMIX](LMAXMIX.md) for the
<a href="#occmat" class="mw-selflink-fragment">on-site PAW occupancy
matrices</a>. When the [CHGCAR](../input-files/CHGCAR.md) file is read and
kept fixed in the course of the calculations
([ICHARG](ICHARG.md)=11), the results will necessarily not
be identical to a self-consistent run. The deviations are often large
for DFT+U calculations.

|  |
|----|
| **Warning:** The total energy will depend on the parameters $U$ ([LDAUU](LDAUU.md)) and $J$ ([LDAUJ](LDAUJ.md)). It is, therefore, not meaningful to compare the total energies resulting from calculations with different $U$ and/or $J$; or $U-J$ in the case of Dudarev's approach (LDAUTYPE=2). |

It is possible to use
LDAUTYPE=1, 2, and 3 for a
non–spin-polarized calculation with [ISPIN](ISPIN.md)=1.

## Related tags and articles\[<a href="/wiki/index.php?title=LDAUTYPE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LDAU](LDAU.md), [LDAUL](LDAUL.md),
[LDAUU](LDAUU.md), [LDAUJ](LDAUJ.md),
[LDAUPRINT](LDAUPRINT.md),
[LMAXMIX](LMAXMIX.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LDAUTYPE-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LDAUTYPE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^liechtenstein:prb:95-1]: [A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Phys. Rev. B **52**, R5467 (1995).](https://doi.org/10.1103/PhysRevB.52.R5467)
[^dudarev:prb:98-2]: [S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Phys. Rev. B **57**, 1505 (1998).](https://doi.org/10.1103/PhysRevB.57.1505)
[^cococcioni:2005-3]: [M. Cococcioni and S. de Gironcoli, Phys. Rev. B **71**, 035105 (2005).](https://doi.org/10.1103/PhysRevB.71.035105)

<!-- Source: https://vasp.at/wiki/index.php/EFERMI | revid: 32630 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EFERMI


EFERMI = MIDGAP \| LEGACY \|
\[real\]  
Default: **EFERMI** = LEGACY 

Description: Defines how the Fermi energy is calculated in VASP. It is
recommended to use EFERMI = MIDGAP.

------------------------------------------------------------------------


## Contents


- [1 Fermi energy
  in semiconductors](#Fermi_energy_in_semiconductors)
- [2 Fermi energy
  in metals](#Fermi_energy_in_metals)
- [3 Fixed Fermi
  energy](#Fixed_Fermi_energy)
- [4 Related tags
  and articles](#Related_tags_and_articles)


## Fermi energy in semiconductors\[<a href="/wiki/index.php?title=EFERMI&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Fermi energy in semiconductors">edit</a> \| (./index.php.md)\]

For semiconducting materials, the Fermi energy is not uniquely defined
in the bandgap of the material. Any value that produces the correct
number of electrons ([NELECT](NELECT.md)) is allowed. By
default, VASP places the Fermi energy at a somewhat arbitrary value
within the bandgap. The precise value depends on values chosen for the
smearing ([ISMEAR](ISMEAR.md) and
[SIGMA](SIGMA.md)) and the density of states
([EMIN](EMIN.md), [EMAX](EMAX.md), and
[NEDOS](NEDOS.md)). Typically, this places the Fermi energy
towards the bottom of the bandgap.

You can change this behavior by setting
EFERMI = MIDGAP (recommended).
VASP will then put the Fermi energy in the middle of the gap because
this is the most consistent with increasing the smearing
[SIGMA](SIGMA.md). This algorithm to determine the Fermi
energy was introduced in VASP.6.4. The value of the Fermi energy should
not affect the outcome of the calculation.

## Fermi energy in metals\[<a href="/wiki/index.php?title=EFERMI&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Fermi energy in metals">edit</a> \| (./index.php.md)\]

MIDGAP and LEGACY should yield the same value when your system does not
have a gap. The Fermi energy is placed precisely at the value so that
underneath are enough states to accommodate
[NELECT](NELECT.md) electrons. The evaluation of the Fermi
energy involves an integral over the 1. BZ. Therefore, the Fermi energy
in metals needs to be converged with respect to the
[KPOINTS](../input-files/KPOINTS.md) mesh and smearing
([ISMEAR](ISMEAR.md), [SIGMA](SIGMA.md)).

|  |
|----|
| **Tip:** If you are interested in the properties at the Fermi energy (e.g., for transport calculations), you should compute the Fermi energy with a very dense **k**-point mesh. To save computational time, you can fix the charge density ([ICHARG](ICHARG.md) = 11) once the Kohn-Sham states have converged with respect to the **k**-point density and increase the number of **k**-point further to converge the value of the Fermi energy. |

## Fixed Fermi energy\[<a href="/wiki/index.php?title=EFERMI&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Fixed Fermi energy">edit</a> \| (./index.php.md)\]

Occasionally, you want to compute systems with fixed Fermi energy for a
given charge density. To this end, set
EFERMI to a numeric value and
[ICHARG](ICHARG.md) = 11. A possible use case is to set
EFERMI to the converged Fermi
energy in a band-structure calculation. You may use this to introduce
electron doping/depletion to a system.

|  |
|----|
| **Warning:** The Fermi energy cannot be computed based on **k** points along a path. |

This is, in particular, important for band-structure calculation of
metallic systems because for gaped systems the Fermi energy often still
ends up at a valid value within the gap despite the inaccurate
computation. Hence, to plot a band structure the band energies should be
taken from the calculation with fixed charge density based on
**k**-points along a path, but the Fermi energy should be taken from the
calculation based on a **k** mesh (e.g., the scf calculation by which
the charge density was obtained or a more precisely converged Fermi
energy based on the same fixed charge density).
EFERMI can fix the Fermi
energy to the proper value during the band-structure calculation.

## Related tags and articles\[<a href="/wiki/index.php?title=EFERMI&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ISMEAR](ISMEAR.md), [SIGMA](SIGMA.md),
[EMIN](EMIN.md), [EMAX](EMAX.md),
[NEDOS](NEDOS.md), [Chemical potential in electron-phonon
interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)



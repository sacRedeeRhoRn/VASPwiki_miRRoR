<!-- Source: https://vasp.at/wiki/index.php/ISMEAR | revid: 32800 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ISMEAR


ISMEAR = -15 \| -14 \| -5 \|
-4 \| -3 \| -2 \| -1 \| 0 \| \[integer\]\>0  
Default: **ISMEAR** = 1 

Description: ISMEAR determines
how the partial occupancies *f*<sub>n**k**</sub> are set for each
orbital. [SIGMA](SIGMA.md) determines the width of the
smearing in eV.

------------------------------------------------------------------------

Please consider how-to guide to choose the optimal [smearing
technique](../tutorials/Smearing_technique.md).

## Tag options\[<a href="/wiki/index.php?title=ISMEAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Tag options">edit</a> \| (./index.php.md)\]

- `ISMEAR`` > 0`: method of
  Methfessel-Paxton order
  ISMEAR with width
  [SIGMA](SIGMA.md).

|  |
|----|
| **Mind:** Methfessel-Paxton can yield erroneous results for insulators because the partial occupancies can be unphysical. |

- `ISMEAR`` = 0`: Gaussian
  smearing with width [SIGMA](SIGMA.md).

<!-- -->

- `ISMEAR`` = -1`: Fermi
  smearing with width [SIGMA](SIGMA.md).

<!-- -->

- `ISMEAR`` = -2`: Partial
  occupancies are read in from the [WAVECAR](../input-files/WAVECAR.md)
  and kept fixed throughout run. Alternatively, you can also choose
  occupancies in the [INCAR](../input-files/INCAR.md) file with the tag
  [FERWE](FERWE.md) (and [FERDO](FERDO.md) for
  [`ISPIN`](ISPIN.md)` = 2` calculations).

<!-- -->

- `ISMEAR`` = -3`: perform a
  loop over [SMEARINGS](SMEARINGS.md) parameters supplied
  in the [INCAR](../input-files/INCAR.md) file.

<!-- -->

- `ISMEAR`` = -4`: Tetrahedron
  method without smearing.

<!-- -->

- `ISMEAR`` = -5`: Tetrahedron
  method with Blöchl corrections without smearing.

<!-- -->

- `ISMEAR`` = -14`:
  Tetrahedron method with Fermi-Dirac smearing
  [SIGMA](SIGMA.md).

<!-- -->

- `ISMEAR`` = -15`:
  Tetrahedron method with Blöchl corrections with Fermi-Dirac smearing
  [SIGMA](SIGMA.md).

|  |
|----|
| **Mind:** Use a [Γ-centered **k**-mesh](../input-files/KPOINTS.md) for the tetrahedron methods. |

## Related tags and articles\[<a href="/wiki/index.php?title=ISMEAR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[SIGMA](SIGMA.md), [EFERMI](EFERMI.md),
[FERWE](FERWE.md), [FERDO](FERDO.md),
[SMEARINGS](SMEARINGS.md), [Smearing
technique](../tutorials/Smearing_technique.md),
<a href="/wiki/K-point_integration" class="mw-redirect"
title="K-point integration">K-point integration</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ISMEAR-_incategory-Examples)



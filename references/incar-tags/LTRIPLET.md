<!-- Source: https://vasp.at/wiki/index.php/LTRIPLET | revid: 22325 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LTRIPLET


LTRIPLET = .TRUE. \| .FALSE. 

|                       |           |     |
|-----------------------|-----------|-----|
| Default: **LTRIPLET** | = .FALSE. |     |

Description: LTRIPLET selects
a triplet ansatz for
[Bethe-Salpeter-equations](../theory/Category-Bethe-Salpeter_equations.md)
(BSE) calculations. This is synonymous to
[LHARTREE](LHARTREE.md) = .FALSE.

------------------------------------------------------------------------

For a usual BSE calculation
([LHARTREE](LHARTREE.md)=.TRUE.;
LTRIPLET = .FALSE.), the
excited state corresponds to a singlet if the ground state is not
spin-polarized ([ISPIN](ISPIN.md)=1) or anti-ferromagnetic
([ISPIN](ISPIN.md)=2, total magnetic moment 0). This is so
because the ansatz for the BSE calculation involves a hole and an
electron pair prepared within each spin channel. For instance, an
electron with up spin is removed from the ground-state determinant and
placed with the same spin into a previously unoccupied orbital. If there
are no separate spin channels this ansatz results in a net spin-zero,
which corresponds to a singlet state.

If LTRIPLET=.TRUE., VASP
assumes that an *up* electron is removed from the ground-state
determinant and placed as a *down* electron into a previously unoccupied
orbital (spin flip). This ansatz corresponds to a triplet state as it
has a net spin of one. Without spin-orbit coupling
([LSORBIT](LSORBIT.md) = .FALSE.), the transition
probability from the singlet ground state to the triplet solutions will
be exactly zero. These excitations correspond to dark, potentially
long-lived triplet excitons. However, VASP calculates the transition
probabilities incorrectly, by assuming that a spin-flip excitation has
the same transition probabilities as a usual singlet excitation. The
reported transition probabilities ("optical transitions" in
[vasprun.xml](../output-files/Vasprun.xml.md)) are hence incorrect;
they should be all zero. Likewise, the contributions to the dielectric
function are zero for triplet excitations, and incorrectly reported in
the [vasprun.xml](../output-files/Vasprun.xml.md) file.

If a non-magnetic material is calculated using
[ISPIN](ISPIN.md)=2 for both the groundstate and BSE
calculation, and a usual BSE calculation is performed
([LHARTREE](LHARTREE.md)=.TRUE.;
LTRIPLET = .FALSE.), all
singlet transitions as well as one set of the triplet excitations (those
with $m_S=0$ ) are
calculated. All triplet transitions will have zero transition
probabilities. If LTRIPLET =
.TRUE. is set for the BSE calculation, the other two sets of triplet
excitations (those with $m_S=1$ and
$m_S=-1$) are determined. Note that as for
[ISPIN](ISPIN.md)=1 for [ISPIN](ISPIN.md)=2 and
LTRIPLET = .FALSE., incorrect
non-zero transition probabilities are reported in the
[vasprun.xml](../output-files/Vasprun.xml.md) file (they should be all
exactly zero, since the underlying pair states fed into the BSE can not
be excited by light).

To obtain meaningful transition probabilities for the singlet and
triplet excitations, include spin-orbit coupling by setting
[LSORBIT](LSORBIT.md) = .TRUE. in the
[INCAR](../input-files/INCAR.md) file throughout the calculation, i.e., for
the ground-state and BSE calculation. In this case, the singlet and all
three sets of triplet excitations are calculated simultaneously, and
proper transition probabilities are assigned to each transition. Small
transition probabilities might be observed even for triplet excitations
as a result of spin-orbit coupling.
LTRIPLET = .TRUE. should not
be used for calculations including spin-orbit coupling.

|  |
|----|
| **Warning:** LTRIPLET=.TRUE. has not been extensively tested in combination with spin-polarized ground states ([ISPIN](ISPIN.md)=2). |

|  |
|----|
| **Warning:** We are not sure whether the [BSEFATBAND](../output-files/BSEFATBAND.md) approach can be combined with the LTRIPLET tag. |

## Related tags and articles\[<a href="/wiki/index.php?title=LTRIPLET&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LHARTREE](LHARTREE.md), [ISPIN](ISPIN.md),
[LSORBIT](LSORBIT.md),
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LTRIPLET-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LTRIPLET&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------



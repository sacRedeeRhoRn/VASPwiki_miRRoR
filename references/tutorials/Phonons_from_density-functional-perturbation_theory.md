<!-- Source: https://vasp.at/wiki/index.php/Phonons_from_density-functional-perturbation_theory | revid: 34088 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Phonons from density-functional-perturbation theory


The phonon calculations using [density-functional-perturbation theory
(DFPT)](../theory/Phonons-_Theory.md)
are carried out by setting [**IBRION**=7 or
8](../incar-tags/IBRION.md) in the [INCAR](../input-files/INCAR.md)
file.

|  |
|----|
| **Mind:** Only zone-center (Γ-point) frequencies are calculated. |

In general, the DFPT routines in VASP are somewhat rudimentary and only
support displacements commensurate with the supercell, i.e., so-called
q=0 phonons. Therefore, this approach offers few advantages over
computing [phonons from finite
differences](Phonons_from_finite_differences.md).
In particular, the DFPT routines are limited to LDA and GGA functionals,
and they do not determine the elastic tensors, since the perturbation
with respect to the strain tensor is not implemented. The only advantage
of the linear response routines is that they eliminate the need to
choose the magnitude of the finite displacement
[POTIM](../incar-tags/POTIM.md). Therefore, it might be helpful to first
calculate phonon frequencies within DFPT and then switch to the [finite
differences
approach](Phonons_from_finite_differences.md)
in order to determine the largest displacement that will produce results
compatible with the linear response routines.

A few technical comments: VASP solves the [linear Sternheimer
equation](../theory/Phonons-_Theory.md) to
determine the linear response of the orbitals. Hence, unoccupied
orbitals are not required. Internally, the VASP routines for linear
response rely on finite differences in two places:

1.  The first place is the determination of the second derivative of the
    [exchange-correlation
    functional](../categories/Category-Exchange-correlation_functionals.md):
    Since most functionals do not support an algebraic determination of
    second derivatives, VASP always resorts to finite differences to
    determine the second-order change of the exchange
    correlation-potential and the PAW one-center terms for each atomic
    displacement.
2.  Second, after VASP has determined the first-order change of the
    orbitals, it computes all [second derivatives using finite
    displacements](../theory/Phonons-_Theory.md).

To this end, VASP displaces the selected atom in the selected directions
[adds the calculated linear response to the
orbitals](../theory/Phonons-_Theory.md), and
finally determines the differences in the forces and the stress tensor
for positive and negative displacements. It can be shown that this
yields precisely the [second-order force
constants](../theory/Phonons-_Theory.md)
and the [internal strain
tensor](../theory/Phonons-_Theory.md),
respectively.


## Contents


- [1
  Input](#input)
- [2
  Output](#output)
- [3 Related tags
  and sections](#related-tags-and-sections)
- [4
  References](#references)


## Input\[<a
href="/wiki/index.php?title=Phonons_from_density-functional-perturbation_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

To use DFPT, set the tag [**IBRION**=7 or
8](../incar-tags/IBRION.md) in the [INCAR](../input-files/INCAR.md)
file. There are two options for using the DFPT routines to compute the
second-order force-constants

- [IBRION](../incar-tags/IBRION.md)=7, all the atoms are displaced in all
  three Cartesian directions,
- [IBRION](../incar-tags/IBRION.md)=8, uses symmetry to reduce the number
  of displacements.

If [LEPSILON](../incar-tags/LEPSILON.md)=.TRUE. or
[LCALCEPS](../incar-tags/LCALCEPS.md)=.TRUE., additional dielectric
properties are computed.

## Output\[<a
href="/wiki/index.php?title=Phonons_from_density-functional-perturbation_theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The second derivates of the total energy with respect to ionic
displacements (interatomic force constants) are computed, the [dynamical
matrix](../theory/Phonons-_Theory.md) is
constructed, diagonalized and the phonon modes and frequencies of the
system are reported after the following lines:

     Eigenvectors and eigenvalues of the dynamical matrix
     ----------------------------------------------------

The mixed second derivative with respect to the strain and the ionic
displacement (internal strain tensor) are evaluated and reported.
Although the contributions from the ionic relaxations to the elastic
tensor are calculated, the ion-clamped elastic tensor (rigid ion) is not
determined because the perturbation with respect to the strain tensor is
not implemented.

Furthermore, the [Born effective
charges](../theory/Phonons-_Theory.md) are
determined analytically by contracting the linear response of the
orbitals over the "polarization" vector Eq. (30) in Ref.
<sup>[\[1\]](#cite_note-gajdos:prb:2006-1)</sup>.
These should agree well with the Born effective charges that were
previously determined when the linear response with respect to external
fields [LEPSILON](../incar-tags/LEPSILON.md)=.TRUE. was calculated
(there are two different routes to calculate mixed derivatives). The
final summary output towards the end of the
[OUTCAR](../output-files/OUTCAR.md) file writes the Born effective charges
determined from the linear response with respect to external fields.

It is possible to [obtain the phonon dispersion at different **q**
points](Computing_the_phonon_dispersion_and_DOS.md)
by computing the force constants on a sufficiently large supercell and
Fourier interpolating the dynamical matrices in the primitive cell.

It is also possible to use
phonopy<sup>[\[2\]](#cite_note-phonopy-2)</sup>
to use the results of a density-functional-perturbation theory
calculation done with
VASP.<sup>[\[3\]](#cite_note-phonopy_dfpt-3)</sup>

|  |
|----|
| **Mind:** [IBRION](../incar-tags/IBRION.md)=7 or 8 are supported by VASP.5.1 and later versions. |

## Related tags and sections\[<a
href="/wiki/index.php?title=Phonons_from_density-functional-perturbation_theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[IBRION](../incar-tags/IBRION.md), [LEPSILON](../incar-tags/LEPSILON.md),
[Phonons: Theory](../theory/Phonons-_Theory.md), [Phonons
from finite
differences](Phonons_from_finite_differences.md)

## References\[<a
href="/wiki/index.php?title=Phonons_from_density-functional-perturbation_theory&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-gajdos:prb:2006_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.73.045112"
    class="external text" rel="nofollow">M. Gajdoš, K. Hummer, G. Kresse, J.
    Furthmüller, and F. Bechstedt, Phys. Rev. B <strong>73</strong>, 045112
    (2006).</a>
2.  [↑](#cite_ref-phonopy_2-0)
    <a href="http://phonopy.github.io/phonopy/index.html"
    class="external text"
    rel="nofollow">http://phonopy.github.io/phonopy/index.html (2022).</a>
3.  [↑](#cite_ref-phonopy_dfpt_3-0)
    <a href="http://phonopy.github.io/phonopy/vasp-dfpt.html"
    class="external text"
    rel="nofollow">http://phonopy.github.io/phonopy/vasp-dfpt.html
    (2022).</a>



<!-- Source: https://vasp.at/wiki/index.php/Exciton_band_structure | revid: 35858 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Exciton band structure


<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Exciton_band_structure_hBN.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/1/17/Exciton_band_structure_hBN.png/300px-Exciton_band_structure_hBN.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/1/17/Exciton_band_structure_hBN.png 1.5x"
width="300" height="225" /></a>
<figcaption>Band structure of the two lowest excitons in bulkh
hBN</figcaption>
</figure>

Exciton band dispersion serves as a powerful tool for characterizing
excitations in a system and can be directly linked to the measured
dynamical structure
factor<sup>[\[1\]](#cite_note-gatti:prb:2013-1)</sup>.
The exciton band structure is a band structure plot where the exciton
energies are presented for different q-points. To find the exciton
energies at the required \$q\$-points, [the Bethe-Salpeter equation
(BSE)](../tutorials/Bethe-Salpeter-equations_calculations.md)
(or [the Casida equation in case of TDDFT
calculation](Time-dependent_density-functional_theory_calculations.md))
has to be solved for every such \$q\$-point.

### Excitons at finite q\[<a
href="/wiki/index.php?title=Exciton_band_structure&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Excitons at finite q">edit</a> \| (./index.php.md)\]

To solve the BSE ([ALGO](../incar-tags/ALGO.md)=BSE or TDHF) at a finite
momentum q, the index of the corresponding \$q\$-point has to be
provided via the [KPOINT_BSE](../incar-tags/KPOINT_BSE.md) tag. To
calculate the dispersion along a certain path, the q-points along this
path can be identified in the [OUTCAR](../output-files/OUTCAR.md) file from
a preceding
[GW](Practical_guide_to_GW_calculations.md)
step or a BSE calculation itself.

To be able to produce a smooth exciton band structure plot a large
number of k-points have to be included. For example, bulk hBN with
24x24x2 k-points grid has the following k-points in the irreducible
Brillouin zone:


       Subroutine IBZKPT returns following result:
     ===========================================

     Found    122 irreducible k-points:

     Following reciprocal coordinates:
                Coordinates               Weight
    ->0.000000  0.000000  0.000000      1.000000<--
      0.041667  0.000000  0.000000      6.000000
      0.083333  0.000000  0.000000      6.000000
      0.125000  0.000000  0.000000      6.000000
      0.166667  0.000000  0.000000      6.000000
      0.208333  0.000000  0.000000      6.000000
      0.250000  0.000000  0.000000      6.000000
      0.291667  0.000000  0.000000      6.000000
      0.333333  0.000000  0.000000      6.000000
      0.375000  0.000000  0.000000      6.000000
      0.416667  0.000000  0.000000      6.000000
      0.458333  0.000000  0.000000      6.000000
      0.500000  0.000000  0.000000      3.000000
    ->0.041667  0.041667  0.000000      6.000000<--
      0.083333  0.041667  0.000000     12.000000
      0.125000  0.041667  0.000000     12.000000
    ...


In GW and BSE calculations one can find two blocks for *Subroutine
IBZKPT returns following result:*. The first one corresponds to the
k-points with symmetries enabled and the second one when the symmetries
are turned off. The index in [KPOINT_BSE](../incar-tags/KPOINT_BSE.md)
should be provided according to the first block, i.e., with the
symmetries. If the symmetries are disabled ([ISYM](../incar-tags/ISYM.md)),
the blocks should be identical. The selected q-point with index and
coordinates in reciprocal coordinates is written in the BSE calculation
to the [OUTCAR](../output-files/OUTCAR.md) file:

    NQ=  61    0.3333    0.3333    0.0000

[KPOINT_BSE](../incar-tags/KPOINT_BSE.md) = 1 corresponds to the q=0
case, and [KPOINT_BSE](../incar-tags/KPOINT_BSE.md) \> 1 would result
in the BSE calculation for the specific q-point. The optional three
integers in [KPOINT_BSE](../incar-tags/KPOINT_BSE.md) can be used to
specify a point outside of the first Brillouin zone.

|  |
|----|
| **Warning:** With VASP, finite momentum calculations at TDDFT or BSE level, i.e. [ALGO](../incar-tags/ALGO.md)=TDHF or BSE, must always use [ANTIRES](../incar-tags/ANTIRES.md)=2 regardless of the solver, functional, or approximation used for the electron-hole interaction. Otherwise, the results will be unphysical! |

There are iteractive solvers available in BSE. However, to be able to
find the eigenvalues it is necessary to choose the exact diagonalization
algorithm, i.e., [IBSE](../incar-tags/IBSE.md) = 2. After the BSE is solved
for all the required q-points, the eigenvalues can be found in the
corresponding [vasprun.xml](../output-files/Vasprun.xml.md) files:

    <varray name="opticaltransitions" > 

The dispersion along G-K path for the two lowest excitons in bulk hBN is
shown in the figure.

## Related tags and sections\[<a
href="/wiki/index.php?title=Exciton_band_structure&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[KPOINT_BSE](../incar-tags/KPOINT_BSE.md),
[ANTIRES](../incar-tags/ANTIRES.md)

## References\[<a
href="/wiki/index.php?title=Exciton_band_structure&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-gatti:prb:2013_1-0)
    <a href="http://dx.doi.org/10.1103/PhysRevB.88.155113"
    class="external text" rel="nofollow">Matteo Gatti and Francesco Sottile,
    Phys. Rev. B <strong>88</strong>, 155113 (2013).</a>



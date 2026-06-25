<!-- Source: https://vasp.at/wiki/index.php/Phonons_from_finite_differences | revid: 36045 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Phonons from finite differences


The phonon calculations using a [finite differences
approach](../theory/Phonons-_Theory.md)
are carried out by setting [**IBRION**=5 or
6](../incar-tags/IBRION.md) in the [INCAR](../input-files/INCAR.md)
file. When these tags are set, the second-order force constants are
computed using finite differences. The [dynamical
matrix](../theory/Phonons-_Theory.md) is
constructed, diagonalized and the phonon modes and frequencies of the
system are reported in the [OUTCAR](../output-files/OUTCAR.md) file. If
[ISIF](../incar-tags/ISIF.md)\>=3, the internal strain tensors are computed
as well.

|  |
|----|
| **Mind:** Only zone-center (Γ-point) frequencies are calculated. |

It is possible to [obtain the phonon dispersion at different **q**
points](Computing_the_phonon_dispersion_and_DOS.md)
by computing the second-order force constants on a sufficiently large
supercell and Fourier interpolating the dynamical matrices in the unit
cell.


## Contents


- [1
  Input](#input)
- [2
  Output](#output)
- [3 Practical
  hints](#practical-hints)
- [4 Related tags
  and sections](#related-tags-and-sections)
- [5
  References](#references)


## Input\[<a
href="/wiki/index.php?title=Phonons_from_finite_differences&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

There are two options to compute the second-order force constants using
finite differences:

- [IBRION](../incar-tags/IBRION.md)=5, all atoms are displaced in all
  three Cartesian directions, resulting in a significant computational
  effort even for moderately sized high-symmetry systems.
- [IBRION](../incar-tags/IBRION.md)=6, only symmetry inequivalent
  displacements are considered, and the remainder of the force-constants
  matrix is filled using symmetry operations.

[POTIM](../incar-tags/POTIM.md) determines the step size. If too large
values are supplied in the input file, the step size defaults to 0.015 Å
(starting from VASP.5.1). Expertise shows that this is a very reasonable
compromise.

The [NFREE](../incar-tags/NFREE.md) tag determines how many displacements
are used for each direction and ion:

- [NFREE](../incar-tags/NFREE.md)=2 uses central differences, *i.e.*, each
  ion is displaced by a small positive and negative displacement,
  ±[POTIM](../incar-tags/POTIM.md), along each of the Cartesian directions.
- [NFREE](../incar-tags/NFREE.md)=4 uses four displacements along each of
  the Cartesian directions ±[POTIM](../incar-tags/POTIM.md) and
  ±2×[POTIM](../incar-tags/POTIM.md).
- [NFREE](../incar-tags/NFREE.md)=1 uses a single displacement (this is
  strongly discouraged).

If [ISIF](../incar-tags/ISIF.md)\>=3, the elastic and internal strain
tensors are computed.

The selective dynamics mode of the [POSCAR](../input-files/POSCAR.md) file
is presently only supported for [IBRION](../incar-tags/IBRION.md)=5; in
this case, only those components of the Hessian matrix are calculated
for which the selective dynamics tags are set to .TRUE. in the
[POSCAR](../input-files/POSCAR.md) file.

|  |
|----|
| **Important:** The selective dynamics always refer to the Cartesian components of the Hessian matrix, contrary to the behavior during ionic relaxation. |

For the following [POSCAR](../input-files/POSCAR.md) file, for instance,

    Cubic BN
       3.57
     0.0 0.5 0.5
     0.5 0.0 0.5
     0.5 0.5 0.0
       1 1
    selective
    Direct
     0.00 0.00 0.00  F F F
     0.25 0.25 0.25  T F F

atom 2 is displaced in the *x*-direction only, and only the
*x*-component of the second atom of the Hessian matrix is calculated.

If [LEPSILON](../incar-tags/LEPSILON.md)=.TRUE. or
[LCALCEPS](../incar-tags/LCALCEPS.md)=.TRUE., additional dielectric
properties are computed.

## Output\[<a
href="/wiki/index.php?title=Phonons_from_finite_differences&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The phonon modes and frequencies are written to the
[OUTCAR](../output-files/OUTCAR.md) file after the following lines:

     Eigenvectors and eigenvalues of the dynamical matrix
     ----------------------------------------------------

The following lines are repeated for each normal mode and should look
like the following example output:

       1 f  =   14.329944 THz    90.037693 2PiTHz  477.995462 cm-1    59.263905 meV
                 X         Y         Z           dx          dy          dz
          0.000000  0.000000  0.000000     0.009046   -0.082007   -0.006117
          0.000000  2.731250  2.731250     0.009046    0.106244    0.006563
          0.000000  5.462500  5.462500     0.009046    0.082007    0.006117
          0.000000  8.193750  8.193750     0.009046   -0.106244   -0.006563
          ...
       2 f  =   14.329944 THz    90.037693 2PiTHz  477.995462 cm-1    59.263905 meV
                 X         Y         Z           dx          dy          dz
          0.000000  0.000000  0.000000     0.003458    0.021825   -0.093181
          0.000000  2.731250  2.731250     0.003458    0.005416    0.094689
          0.000000  5.462500  5.462500     0.003458   -0.021825    0.093181
          0.000000  8.193750  8.193750     0.003458   -0.005416   -0.094689
          ...
       ...

The first number is the label of the normal mode. If this number is
followed by *f* it is a purely real mode, stating the mode is
vibrationally stable. Otherwise, if it is followed by *f/i*, the mode is
an imaginary mode ("soft mode"). These labels are followed by the
eigenfrequency of the mode in different units.

The following table labeled by (*x,y,z,dx,dy,dz*) contains the Cartesian
positions of the atoms and the normalized eigenvectors of the eigenmodes
in Cartesian coordinates.

There should be 3$N$ normal
modes, where $N$ is the
number of atoms in the supercell ([POSCAR](../input-files/POSCAR.md)). The
modes are ordered in descending order with respect to the
eigenfrequency. The last three modes are the translational modes (they
are usually disregarded).

Finally, [IBRION](../incar-tags/IBRION.md)=6 and
[ISIF](../incar-tags/ISIF.md)≥3 allows to calculate the elastic constants.
The elastic tensor is determined by performing six finite distortions of
the lattice and deriving the elastic constants from the strain-stress
relationship.[^lepage:prb:2002-1]
The elastic tensor is calculated both, for 'clamped' ions, as well, as
allowing for relaxation of the ions. The elastic moduli for rigid ions
are written after the line

    SYMMETRIZED ELASTIC MODULI (kBar)

The ionic contributions are determined by inverting the ionic Hessian
matrix and multiplying with the internal strain
tensor,[^wu:prb:2005-2]
and the corresponding contributions are written after the lines:

    ELASTIC MODULI CONTR FROM IONIC RELAXATION (kBar)

The final elastic moduli, including both, the contributions for
distortions with rigid ions and the contributions from the ionic
relaxations, are summarized at the very end:

    TOTAL ELASTIC MODULI (kBar)

There are a few caveats to this approach: most notably, the plane-wave
cutoff ([ENCUT](../incar-tags/ENCUT.md)) needs to be sufficiently large to
converge the stress tensor. This is usually only achieved if the default
cutoff is increased by roughly 30%, but it is strongly recommended to
increase the cutoff systematically, (e.g., in steps of 15%), until full
convergence is achieved.

## Practical hints\[<a
href="/wiki/index.php?title=Phonons_from_finite_differences&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Practical hints">edit</a> \| (./index.php.md)\]

The computation of the second-order force constants requires accurate
[forces](../methods/Category-Forces.md). Therefore, the tag
[PREC](../incar-tags/PREC.md)=Accurate is recommended in the
[INCAR](../input-files/INCAR.md). The
[ADDGRID](../incar-tags/ADDGRID.md)=TRUE should **not** be set without
careful testing.

A practical way to check for convergence is to monitor the Γ point
(**q**=0) optical mode frequencies while varying the
[ENCUT](../incar-tags/ENCUT.md), [PREC](../incar-tags/PREC.md), and **k** point
density ([KPOINTS](../input-files/KPOINTS.md)). Additionally, compare the
result to [phonons from density-functional-perturbation theory
(DFPT)](Phonons_from_density-functional-perturbation_theory.md).

To get the phonon frequencies quickly on the command line, simply type
the following:

    grep THz OUTCAR

To get an accurate phonon dispersion, perform the force-constants
calculation in a large enough supercell. When increasing the size of the
supercell, we recommend decreasing the **k**-point density in the
[KPOINTS](../input-files/KPOINTS.md) file to yield the same resolution.
For example, for the primitive cell of silicon, a 12x12x12
Gamma-centered **k**-point mesh is needed to obtain accurate phonon
frequencies at the Gamma point. When replicating the unit cell to a
2x2x2 supercell, a 6x6x6 **k** point mesh will produce an equivalent
sampling. For a 4x4x4 supercell, a 3x3x3 **k** point mesh will suffice.

It is possible to use
phonopy[^phonopy-3]
to post-process the results of a finite differences calculation done
with
VASP.[^phonopy_dfpt-4]

|  |
|----|
| **Tip:** In contrast to [computing phonons within DFPT](Phonons_from_density-functional-perturbation_theory.md), the finite difference approach can be used in combination with any <a href="/wiki/Exchange-correlation_functional" class="mw-redirect"
title="Exchange-correlation functional">Exchange-correlation
functional</a>. |

[IBRION](../incar-tags/IBRION.md)=5, is available as of VASP.4.5,
[IBRION](../incar-tags/IBRION.md)=6 starting from VASP.5.1. In some older
versions (pre VASP.5.1), [NSW](../incar-tags/NSW.md) (number of ionic steps)
must be set to 1 in the [INCAR](../input-files/INCAR.md) file, since
[NSW](../incar-tags/NSW.md)=0 sets the [IBRION](../incar-tags/IBRION.md)=−1
regardless of the value supplied in the [INCAR](../input-files/INCAR.md)
file. Although VASP.4.6 supports [IBRION](../incar-tags/IBRION.md)=5-6,
VASP.4.6 does not change the set of **k** points automatically (often
the displaced configurations require a different **k**-point grid).
Hence, the finite difference routine might yield incorrect results in
VASP.4.6.

If you obtain imaginary frequencies when you are not expecting them
(i.e., at a [transition
state](https://vasp.at/wiki/index.php/Category:Transition_states)),
then this is likely an issue with convergence. You should try increasing
the cell size or [k-points mesh](../input-files/KPOINTS.md). If this does
not work, consider the [smearing parameter](../incar-tags/ISMEAR.md),
increasing the precision with the {TAG\|PREC}} tag, or the
[ENCUT](../incar-tags/ENCUT.md). See [How to handle imaginary phonon
modes](How_to_handle_imaginary_phonon_modes.md)
for a step-by-step guide to identifying and resolving soft modes.

## Related tags and sections\[<a
href="/wiki/index.php?title=Phonons_from_finite_differences&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[IBRION](../incar-tags/IBRION.md), [ISIF](../incar-tags/ISIF.md),
[POTIM](../incar-tags/POTIM.md),

[Phonons: Theory](../theory/Phonons-_Theory.md)

[Phonons from density-functional-perturbation
theory](Phonons_from_density-functional-perturbation_theory.md),
[Computing the phonon dispersion and
DOS](Computing_the_phonon_dispersion_and_DOS.md),
[How to handle imaginary phonon
modes](How_to_handle_imaginary_phonon_modes.md)

## References\[<a
href="/wiki/index.php?title=Phonons_from_finite_differences&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^lepage:prb:2002-1]: [Y. Le Page and P. Saxe, Phys. Rev. B **65**, 104104 (2002).](http://doi.org/10.1103/PhysRevB.65.104104)
[^wu:prb:2005-2]: [X. Wu, D. Vanderbilt, and D. R. Hamann, Phys. Rev. B **72**, 035105 (2005).](https://doi.org/10.1103/PhysRevB.72.035105)
[^phonopy-3]: [http://phonopy.github.io/phonopy/index.html (2022).](http://phonopy.github.io/phonopy/index.html)
[^phonopy_dfpt-4]: [http://phonopy.github.io/phonopy/vasp-dfpt.html (2022).](http://phonopy.github.io/phonopy/vasp-dfpt.html)

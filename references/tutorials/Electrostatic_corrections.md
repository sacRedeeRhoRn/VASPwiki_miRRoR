<!-- Source: https://vasp.at/wiki/index.php/Electrostatic_corrections | revid: 34786 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Electrostatic corrections
For charged cells or for calculations of molecules and surfaces with a
large dipole moment, the energy converges very slowly with respect to
the size $L$ of the supercell. Using
methods discussed by Makov *et al.*^([\[1\]](#cite_note-Makov95-1)) and
Neugebauer *et al.*^([\[2\]](#cite_note-Neugebauer92-2)), VASP can
correct for the leading errors (in many details, we have taken a more
general approach, though).

## Contents

- [1 Suggested combination of tags for electrostatic
  corrections](#Suggested_combination_of_tags_for_electrostatic_corrections)
  - [1.1 Bulk](#Bulk)
  - [1.2 Surfaces](#Surfaces)
  - [1.3 Wires](#Wires)
  - [1.4 Molecules](#Molecules)
- [2 Current limitations](#Current_limitations)
- [3 Step-by-step instructions](#Step-by-step_instructions)
  - [3.1 Using the dipole correction for slab
    calculations](#Using_the_dipole_correction_for_slab_calculations)
- [4 Related Tags and Sections](#Related_Tags_and_Sections)
- [5 References](#References)

## Suggested combination of tags for electrostatic corrections
In cases where the system has no net charge and no net dipole moment, no
specific tags need to be set, and this section can be skipped.

### Bulk
If the system has a net dipole or net charge, please follow the
recommendations of
[this](Dipole_corrections_for_defects_in_solids.md)
wiki page.

### [Surfaces](../categories/Category-2D_materials.md)
If the system has a net dipole moment, a combination of
[IDIPOL](../incar-tags/IDIPOL.md)=1,2,3 and
[LDIPOL](../incar-tags/LDIPOL.md) tags may be used. The former corrects
the energies, while the latter corrects the potential and forces.
Optionally, [DIPOL](../incar-tags/DIPOL.md) may be set. The following
options may be used to improve convergence for this case.

1\. Use any of these tags only after pre-converging the orbitals without
the [LDIPOL](../incar-tags/LDIPOL.md) tag

2\. The center of charge should be set in the
[INCAR](../input-files/INCAR.md) file ([DIPOL](../incar-tags/DIPOL.md)= center
of mass)

3\. Ensure that the cell is sufficiently large to determine the dipole
moment with sufficient accuracy (see [DIPOL](../incar-tags/DIPOL.md)). If
the cell is too small, the charge might slosh into the vacuum, causing
very slow convergence. Often, convergence improves with the vacuum
width.

|  |
|----|
| **Warning:** Surface calculations with a net charge result in total energies that do not converge. Relative energies may still be useful. |

### Wires
Not implemented.

### Molecules
If the system has a net dipole moment, use the
[LDIPOL](../incar-tags/LDIPOL.md) tag. The former corrects the energies,
while the latter corrects the potential and forces. Optionally,
[DIPOL](../incar-tags/DIPOL.md) may be set.

## Current limitations
For the current implementation, there are several restrictions; please
read carefully:

- Charged systems:

Quadrupole corrections are only correct for cubic supercells (this means
that the calculated 1/*L*³ corrections are wrong for charged supercells
if the supercell is non-cubic). In addition, we have found empirically
that for charged systems with excess electrons
([NELECT](../incar-tags/NELECT.md)\>[NELECT](../incar-tags/NELECT.md)_(neutral))
more reliable results can be obtained if the energy after correction of
the linear error (1/*L*) is plotted against 1/*L*³ to extrapolate
results manually for *L*→∞. This is due to the uncertainties in
extracting the quadrupole moment of systems with excess electrons.

- Potential corrections are only possible for orthorhombic cells (at
  least the direction in which the potential is corrected must be
  orthogonal to the other two directions).

## Step-by-step instructions
### Using the dipole correction for slab calculations
In this section, we discuss step-by-step instructions to use the dipole
corrections for slab calculations.

**Step 1:** Create a system that has enough vacuum on either side of the
surface normal. An example for such a structure is shown below, for an
fcc-Aluminium with a carbon adsorbed on one of its surface terminations.

    Al3C
    1.0000000000000000
       2.8637824638055176    0.0000000000000000    0.0000000000000000
       1.4318912319027588    2.4801083645679673    0.0000000000000000
       0.0000000000000000    0.0000000000000000   20.0000000000000000
    Al C
    3 1
    Direct
       0.8333333333333333    0.5000000000000000    0.3380865704891008
       0.1666666666666666    0.8333333333333334    0.4550000000000000
       0.4999999999999999    0.1666666666666667    0.5719134295108992
       0.4999999999999999    0.1666666666666667    0.6619134295108993

Note that the system has plenty of vacuum on either side. This empty
space is important for the potential corrections needed for the
[LDIPOL](../incar-tags/LDIPOL.md) tag.

**Step 2:** Switch on the dipole corrections to the energy, potential,
and forces. Optionally set the [DIPOL](../incar-tags/DIPOL.md)

    LDIPOL    = T
    IDIPOL    = 3
    DIPOL     = 0.5 0.5 0.5

**Step 3 (Optional):** View the dipole moment for the system using the
following bash command,

    grep dipolmoment OUTCAR | tail -1

In this example, we get the following output:

     dipolmoment           0.000000      0.000000      0.128389 electrons x Angstroem

which refers to the dipole moment along the three axes. Consistent with
the [POSCAR](../input-files/POSCAR.md) used in this example, only the last
axis has a non-zero dipole moment.

## Related Tags and Sections
[NELECT](../incar-tags/NELECT.md), [EPSILON](../incar-tags/EPSILON.md),
[DIPOL](../incar-tags/DIPOL.md), [IDIPOL](../incar-tags/IDIPOL.md),
[LDIPOL](../incar-tags/LDIPOL.md), [LMONO](../incar-tags/LMONO.md),
[EFIELD](../incar-tags/EFIELD.md)

## References
1.  [↑](#cite_ref-Makov95_1-0) [G. Makov and M. C. Payne, Phys. Rev. B
    51, 4014 (1995).](http://dx.doi.org/10.1103/PhysRevB.51.4014)
2.  [↑](#cite_ref-Neugebauer92_2-0) [J. Neugebauer and M. Scheffler,
    Phys. Rev. B 46, 16067
    (1992).](http://dx.doi.org/10.1103/PhysRevB.46.16067)

<!-- Source: https://vasp.at/wiki/index.php/Born_effective_charges | revid: 35884 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Born effective charges
The change in polarization from the displacement of an atom is not
uniquely defined in periodic systems, where atoms are repeated in
different cells and the charge can be
generalized.^([\[1\]](#cite_note-ghosez:michenaud:gonze:1998-1)) Born
effective charges are one way of defining this dynamical charge.

## Contents

- [1 Introduction](#Introduction)
- [2 How to calculate](#How_to_calculate)
- [3 Excluding local field effects](#Excluding_local_field_effects)
  - [3.1 Related tags and articles](#Related_tags_and_articles)
  - [3.2 References](#References)

# Introduction
The dynamical charge is defined as the cell volume **Ω**, multiplied by
the partial derivative of the macroscopic polarization **P** in the
direction *i* with respect to a rigid displacement of the sublattice of
atoms *κ* in the direction *j*.

However, the polarization is not uniquely defined in periodic systems
and depends on the macroscopic electric field $\mathcal{E}_i$ fixed by the periodic boundary conditions. The
Born effective charge **Z\*** is the partial derivative of the
polarization with respect to position *u* for zero macroscopic electric
field.^([\[2\]](#cite_note-gonze:prb:1997-2)) As polarization is the
first derivative of the total energy with respect to the macroscopic
electric field, **Z\*** may be rearranged in terms of the partial
derivative of the force **F** in direction *j* on atom *κ* with respect
to $\mathcal{E}_i$:

$Z_{\kappa,ij}^\* =\frac{\Omega}{e}
\frac{\partial \mathcal{P}_i} {\partial u_{\kappa,j}(\textbf{q=0})}
=\frac{1}{e} \frac{\partial F_{\kappa,j}}{\partial \mathcal{E}_i},
\qquad {i,j=x,y,z}$

  

[TABLE]

# How to calculate
There are two ways of computing Born effective charges in VASP. The
first is done using [LCALCEPS](../incar-tags/LCALCEPS.md), where a
finite electric field is applied along the three cartesian directions
and the resultant forces on the atoms are calculated:

    LCALCEPS = .TRUE.

The other approach is done using [LEPSILON](../incar-tags/LEPSILON.md),
where the derivative of the wavefunction with respect to an electric
field is calculated using [density functional perturbation
theory](../theory/Electric_field_response_from_density-functional-perturbation_theory.md)
(DFPT):

    LEPSILON = .TRUE.

These may be used in combination with [IBRION](../incar-tags/IBRION.md) to
obtain additional dielectric properties:

    IBRION = 5 or 6 ! Calculated using finite differences.
    IBRION = 7 or 8 ! Calculated using DFPT

For more details, see the pages for each tag. The Born effective charges
including local field effects will be given in the
[OUTCAR](../output-files/OUTCAR.md) file:

    BORN EFFECTIVE CHARGES (including local field effects) (in |e|, cummulative output)

# Excluding local field effects
Previously, the local field effects have been included, that is, changes
in the orbitals due to the electric field induce changes in the Hartree-
and exchange-correlation potentials. This may be limited to changes in
the Hartree potential, by specifying:

    LRPA = .TRUE.
    LCALCEPS = .TRUE. ! N.B. LEPSILON does not output the final Born effective charges.

This prints out the Born effective charges excluding local field
effects:

    BORN EFFECTIVE CHARGES (excluding local field effects) (in |e|, cummulative output)

These are calculated normally but remain hidden unless explicitly
specified.

## Related tags and articles
[LEPSILON](../incar-tags/LEPSILON.md),
[LCALCEPS](../incar-tags/LCALCEPS.md), [IBRION](../incar-tags/IBRION.md),
[LRPA](../incar-tags/LRPA.md), [Berry phases and finite electric
fields](../theory/Berry_phases_and_finite_electric_fields.md),
[Static linear response:
theory](../theory/Static_linear_response-_theory.md)

## References
1.  [↑](#cite_ref-ghosez:michenaud:gonze:1998_1-0) [Ph. Ghosez, J.-P.
    Michenaud, and X. Gonze, *Dynamical atomic charges: The case of AB⁢O3
    compounds*, Phys. Rev. B **58**, 6224
    (1998).](https://doi.org/10.1103/PhysRevB.58.6224)
2.  [↑](#cite_ref-gonze:prb:1997_2-0) [X. Gonze and C. Lee, *Dynamical
    matrices, Born effective charges, dielectric permittivity tensors,
    and interatomic force constants from density-functional perturbation
    theory*, Phys. Rev. B **55**, 10355
    (1997).](http://doi.org/10.1103/PhysRevB.55.10355)

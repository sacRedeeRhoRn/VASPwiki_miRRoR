<!-- Source: https://vasp.at/wiki/index.php/LDIPOL | revid: 34205 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDIPOL
LDIPOL = .TRUE. \| .FALSE.  
Default: **LDIPOL** = .FALSE. 

Description: LDIPOL switches on corrections to the potential and forces.
Can be applied for charged molecules and slabs with a net dipole moment.

------------------------------------------------------------------------

The presence of a dipole in combination with periodic boundary
conditions leads to a slow convergence of the total energy with the size
of the supercell. Furthermore, finite-size errors affect the potential
and the forces. This effect can be counterbalanced by setting
LDIPOL=.TRUE. in the [INCAR](../input-files/INCAR.md) file. For
LDIPOL=.TRUE., a linear correction, and for charged cells, a quadratic
electrostatic potential is added to the local potential in order to
correct the errors introduced by the periodic boundary conditions. When
activating this tag the tag [IDIPOL](IDIPOL.md) has to be
specified, and optionally the tag [DIPOL](DIPOL.md) as well.

|  |
|----|
| **Mind:** This is in the spirit of Neugebauer *et al.* ^([\[1\]](#cite_note-neugebauer:prb:1992-1)), though more general. Note that the total energy is correctly implemented, whereas Ref. ^([\[1\]](#cite_note-neugebauer:prb:1992-1)) contains an erroneous factor 2 in the total energy. |

The biggest advantage of this mode is that leading errors in the forces
are corrected and that the work function can be evaluated for asymmetric
slabs. The disadvantage is that the convergence to the electronic ground
state might slow down considerably, i.e., more electronic iterations
might be required to obtain the required precision.

|  |
|----|
| **Important:** Dipole corrections can lead to slow convergence, since charge often needs to be moved from one side of a slab to the other. The convergence rate often improves by setting AMIN to a smaller value, for instance [`AMIN`](AMIN.md)` = 0.01`, since this dampens charge sloshing (charge moving back and forth from one to the other side of the slab in consecutive steps). Sometimes, it might also be necessary to increase the number of electronic steps using [NELM](NELM.md) and to tighten the energy convergence [`EDIFF`](EDIFF.md)` = 1E-6`. An unconverged dipole correction can lead to erroneous forces \[[\[1\]](https://vasp.at/forum/viewtopic.php?t=20300)\]. |

|  |
|----|
| **Warning:** For charged systems, the potential correction is currently only implemented for cubic supercells. VASP will stop if the supercell is not cubic and LDIPOL is used. |

## Related tags and articles
[Monopole Dipole and Quadrupole
corrections](https://vasp.at/wiki/index.php/Monopole_Dipole_and_Quadrupole_corrections),
[NELECT](NELECT.md), [EPSILON](EPSILON.md),
[IDIPOL](IDIPOL.md), [DIPOL](DIPOL.md),
[LMONO](LMONO.md), [EFIELD](EFIELD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LDIPOL-_incategory-Examples)

## References
1.  ↑ ^([a](#cite_ref-neugebauer:prb:1992_1-0))
    ^([b](#cite_ref-neugebauer:prb:1992_1-1)) [J. Neugebauer and M.
    Scheffler, Phys. Rev. B **46**, 16067
    (1992).](https://doi.org/10.1103/PhysRevB.46.16067)

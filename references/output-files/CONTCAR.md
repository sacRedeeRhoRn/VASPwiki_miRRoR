<!-- Source: https://vasp.at/wiki/index.php/CONTCAR | revid: 27205 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CONTCAR
The CONTCAR file contains information about the structure, e.g., the
ionic positions. It has a format that is compatible with the
[POSCAR](../input-files/POSCAR.md) file. The file is written after each
ionic step and at the end of a completed calculation. It can thus be
copied to the [POSCAR](../input-files/POSCAR.md) file to restart a
calculation.

## Molecular dynamics
For
[molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
(MD) runs ([IBRION](../incar-tags/IBRION.md)=0), the CONTCAR file contains
the MD trajectories. In particular, the structure parameters,
velocities, and predictor-corrector coordinates are needed as input to
restart an MD simulation.

- 1st block: Lattice parameters and ionic positions.
- 2nd block: Initial velocities for atoms.
- 3rd block: Predictor-corrector coordinates.

|  |
|----|
| **Mind:** Whether the ionic positions are rebased into the unit cell depends on the choice for the [MDALGO](../incar-tags/MDALGO.md) tag for historical reasons. |

|  |
|----|
| **Warning:** To continue an MD calculation from a CONTCAR file but with a different ensemble (e.g. switching from [NVT ensemble](../misc/NVT_ensemble.md) to [NpT ensemble](../misc/NpT_ensemble.md)) the predictor-corrector coordinates must be removed; otherwise the calculations will crash. If no velocities are copied to the [POSCAR](../input-files/POSCAR.md) file then random velocities are drawn from a Maxwell-Boltzmann distribution at the selected temperature [TEBEG](../incar-tags/TEBEG.md). |

## Structure relaxation
For [structure
relaxation](../categories/Category-Ionic_minimization.md),
the CONTCAR file contains the positions of the last ionic step of the
relaxation. If the relaxation run has not yet converged one should copy
CONTCAR to [POSCAR](../input-files/POSCAR.md) before continuing. For static
calculations, the CONTCAR file contains the same information as the
[POSCAR](../input-files/POSCAR.md) file.

## Related tags and articles
[POSCAR](../input-files/POSCAR.md), [structure
relaxation](../categories/Category-Ionic_minimization.md),
[structure
optimization](../tutorials/Structure_optimization.md),
[XDATCAR](XDATCAR.md), [IBRION](../incar-tags/IBRION.md)

------------------------------------------------------------------------

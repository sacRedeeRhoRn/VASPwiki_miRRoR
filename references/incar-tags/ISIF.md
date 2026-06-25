<!-- Source: https://vasp.at/wiki/index.php/ISIF | revid: 34129 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ISIF


ISIF = 0 \| 1 \| 2 \| 3 \| 4
\| 5 \| 6 \| 7 \| 8 

|  |  |  |
|----|----|----|
| Default: **ISIF** | = 0 | for [`IBRION`](IBRION.md)` = 0` (molecular dynamics) or [`LHFCALC`](LHFCALC.md)` = .TRUE.` (hybrid functionals) |
|  | = 2 | else |

Description: Determines if the stress tensor is calculated and which
ionic degrees of freedom are varied.

------------------------------------------------------------------------

For
ISIF$\ge$2, the
stress tensor is calculated. It is defined as the negative of the
derivative of the energy $E$ with
respect to the strain tensor $\eta_{ji}$:

$\sigma_{ij} = - \frac{\delta E} {\delta \eta_{ji}}$.

This might be different from other first principles codes. A positive in
the diagonals means that the system is under compressive strain and
wants to expand. A negative value implies that the system is under
tensile strain and wants to reduce its volume. The stress tensor is
symmetric $\sigma_{ij}=\sigma_{ji}$, and, thus, it has six independent entries. The
calculation of the stress tensor is relatively time-consuming, and,
therefore, by default, it is switched off in some cases (e.g., hybrid
functionals). The forces are always calculated.

|  |
|----|
| **Tip:** You can get information about the stress at each ionic step using [`NWRITE`](NWRITE.md)` = 0,1,2,3`. |

ISIF also determines which
degrees of freedom (ionic positions, cell volume, and cell shape) of the
structure are allowed to change.

|  |  |  |  |  |  |
|----|:--:|:--:|:--:|:--:|:--:|
| ISIF | calculate |  | degrees-of-freedom |  |  |
|  | forces | stress tensor | positions | cell shape | cell volume |
| 0 | yes | no | yes | no | no |
| 1 | yes | trace only | yes | no | no |
| 2 | yes | yes | yes | no | no |
| 3 | yes | yes | yes | yes | yes |
| 4 | yes | yes | yes | yes | no |
| 5 | yes | yes | no | yes | no |
| 6 | yes | yes | no | yes | yes |
| 7 | yes | yes | no | no | yes |
| 8 | yes | yes | yes | no | yes |

- For `ISIF`` = 1`, only the
  trace of the stress tensor is calculated. This means only the total
  pressure is correct and can be read off in the line:

<!-- -->

    external pressure =      ... kB

The individual components of the stress tensor are not reliable in this
case and must be disregarded.

- Accuracy

|  |
|----|
| **Warning:** The PAW basis for the [electronic minimization](../categories/Category-Electronic_minimization.md) is not adjusted when the structure is varied during a calculation. |

Therefore, carefully consider effects such as [Pulay
stress](../tutorials/Pulay_stress.md) and choose generous settings
for the [electronic
minimization](../categories/Category-Electronic_minimization.md).
Generally, volume changes should be done only with an increased energy
cutoff, e.g.,
[`ENCUT`](ENCUT.md)` = 1.3×max(`<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX"><code
class="vasp-dark-link-panel" style="padding: 2px">ENMAX</code></a>`)`,
and [`PREC`](PREC.md)` = High`.

- To further control the ionic degrees of freedom that can vary during
  the calculation, set `Selective dynamics` in the
  [POSCAR](../input-files/POSCAR.md) file.
- `ISIF`` = 8` is only
  available as of VASP.6.4.1.

## Related tags and articles\[<a href="/wiki/index.php?title=ISIF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBRION](IBRION.md), [structure
optimization](../tutorials/Structure_optimization.md),
[Ensembles](../categories/Category-Ensembles.md),
[NWRITE](NWRITE.md), Selective-dynamics mode of the
[POSCAR](../input-files/POSCAR.md) file,
[LATTICE_CONSTRAINTS](LATTICE_CONSTRAINTS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ISIF-_incategory-Examples)

------------------------------------------------------------------------



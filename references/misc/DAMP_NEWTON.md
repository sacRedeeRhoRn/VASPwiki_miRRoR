<!-- Source: https://vasp.at/wiki/index.php/DAMP_NEWTON | revid: 34930 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DAMP NEWTON
DAMP_NEWTON = real number 

|                          |       |         |
|--------------------------|-------|---------|
| Default: **DAMP_NEWTON** | = 0.8 | {{{3}}} |

Description: Sets the damping factor applied to the RPA forces during
Newton-step structure relaxation.

------------------------------------------------------------------------

DAMP_NEWTON controls the step size of the Newton-step geometry update
performed during [Random Phase
Approximation](https://vasp.at/wiki/ACFDT/RPA_calculations) (RPA) force
calculations. The updated atomic positions are computed as:

**x**_(new) = **x**_(current) + DAMP_NEWTON × **H**⁻¹ · **F**_(RPA)

where **H**⁻¹ is the inverse of the DFT Hessian (computed during the RPA
force calculation) and **F**_(RPA) are the RPA
forces.^([\[1\]](#cite_note-ramberger:prl:118-1)) The resulting updated
positions are written to the [CONTCAR](../output-files/CONTCAR.md) file
(provided [NSW](../incar-tags/NSW.md)=0). Iterating this procedure—by copying
[CONTCAR](../output-files/CONTCAR.md) to [POSCAR](../input-files/POSCAR.md)
and re-running—should converge the system toward its ground-state
structure.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.1.0 |

## Contents

- [1 Available options](#Available_options)
  - [1.1 DAMP_NEWTON=1.0: No damping](#DAMP_NEWTON=1.0:_No_damping)
  - [1.2 DAMP_NEWTON=0.8: Default
    damping](#DAMP_NEWTON=0.8:_Default_damping)
  - [1.3 DAMP_NEWTON\<0.8: Strong
    damping](#DAMP_NEWTON%3C0.8:_Strong_damping)
- [2 Related tags and articles](#Related_tags_and_articles)
- [3 References](#References)

## Available options
### DAMP_NEWTON=1.0: No damping
No damping is applied; the full Newton step is taken. This is
appropriate when the RPA forces

are well-behaved and the optimization is proceeding stably.

### DAMP_NEWTON=0.8: Default damping
The default value. A mild damping factor of 0.8 is applied to the Newton
step, providing a

small degree of stabilization during the iterative relaxation without
significantly slowing convergence.

### DAMP_NEWTON\<0.8: Strong damping
Use smaller values if numerical instabilities are observed during the
RPA relaxation.

[TABLE]

## Related tags and articles
[CONTCAR](../output-files/CONTCAR.md), [POSCAR](../input-files/POSCAR.md),
[NSW](../incar-tags/NSW.md), [IBRION](../incar-tags/IBRION.md) [Workflows that
use RPA force
relaxation](https://vasp.at/wiki/index.php/Special-Search/-DAMP_NEWTON-_incategory-HowTo)

## References
1.  [↑](#cite_ref-ramberger:prl:118_1-0) [B. Ramberger, T. Schäfer
    and G. Kresse, Phys. Rev. Lett **118**, 106403
    (2017).](https://doi.org/10.1103/PhysRevLett.118.106403)

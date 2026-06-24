<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/OCCUPANCIES | revid: 34750 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/OCCUPANCIES
PLUGINS/OCCUPANCIES = .True. \| .False.  
Default: **PLUGINS/OCCUPANCIES** = .False. 

Description: PLUGINS/OCCUPANCIES calls the Python plugin for the
occupancies interface for each ionic relaxation step

------------------------------------------------------------------------

When PLUGINS/OCCUPANCIES=.TRUE., VASP calls the `occupancies` Python
function at the end of each ionic relaxation step. The primary use-case
of this tag to recompute the occupancies after performing modifications
through other plugins such as
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md).
It also allows changing [NELECT](NELECT.md),
[EFERMI](EFERMI.md), [NUPDOWN](NUPDOWN.md),
[ISMEAR](ISMEAR.md), [SIGMA](SIGMA.md),
[EMIN](EMIN.md) and [EMAX](EMAX.md) at the end of
each SCF step, to be reflected in the next step.

## Expected inputs
The `occupancies` Python function expects the following inputs,

    def occupancies(constants, additions):
        ...

where `constants` and `additions` and [Python
dataclasses](https://docs.python.org/3/library/dataclasses.html). The
`constants` dataclass consists of the following inputs, listed here with
their associated
[datatypes](https://numpy.org/doc/stable/user/basics.types.html)

    @dataclass(frozen=True)
    class ConstantsOccupancies:
        NELECT: float
        EFERMI: float
        NUPDOWN: float
        ISMEAR: int
        SIGMA: float
        EMIN: float
        EMAX: float

The `additions` dataclass consists of the same quantities as the
`constants` tag.

|  |
|----|
| **Mind:** Calling this interface implicitly triggers a recalculation of the occupancies |

## Modifying quantities
Modify the quantities listed in additions by adding to them.

    import numpy as np
    def structure(constants, additions)
        additions.NELECT += 1

|  |
|----|
| **Warning:** You should not make modifications to quantities in `constants`. We implemented some safeguards to prevent accidental modifications. Intentional changes will lead to erratic behavior because we may change the VASP code assuming these quantities are constant. |

## Related tags and articles
[Plugins](../tutorials/Plugins.md),
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md),
[PLUGINS/STRUCTURE](PLUGINS__STRUCTURE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/OCCUPANCIES-_incategory-Examples)

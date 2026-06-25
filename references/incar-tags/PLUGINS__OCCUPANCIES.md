<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/OCCUPANCIES | revid: 34750 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/OCCUPANCIES


PLUGINS/OCCUPANCIES = .True.
\| .False.  
Default: **PLUGINS/OCCUPANCIES** = .False. 

Description:
PLUGINS/OCCUPANCIES calls the
Python plugin for the occupancies interface for each ionic relaxation
step

------------------------------------------------------------------------

When
PLUGINS/OCCUPANCIES=.TRUE.,
VASP calls the `occupancies` Python function at the end of each ionic
relaxation step. The primary use-case of this tag to recompute the
occupancies after performing modifications through other plugins such as
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md).
It also allows changing [NELECT](NELECT.md),
[EFERMI](EFERMI.md), [NUPDOWN](NUPDOWN.md),
[ISMEAR](ISMEAR.md), [SIGMA](SIGMA.md),
[EMIN](EMIN.md) and [EMAX](EMAX.md) at the end of
each SCF step, to be reflected in the next step.

## Expected inputs\[<a
href="/wiki/index.php?title=PLUGINS/OCCUPANCIES&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Expected inputs">edit</a> \| (./index.php.md)\]

The `occupancies` Python function expects the following inputs,


    def occupancies(constants, additions):
        ...


where `constants` and `additions` and
<a href="https://docs.python.org/3/library/dataclasses.html"
class="external text" rel="nofollow">Python dataclasses</a>. The
`constants` dataclass consists of the following inputs, listed here with
their associated
<a href="https://numpy.org/doc/stable/user/basics.types.html"
class="external text" rel="nofollow">datatypes</a>


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

## Modifying quantities\[<a
href="/wiki/index.php?title=PLUGINS/OCCUPANCIES&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Modifying quantities">edit</a> \| (./index.php.md)\]

Modify the quantities listed in additions by adding to them.


    import numpy as np
    def structure(constants, additions)
        additions.NELECT += 1


|  |
|----|
| **Warning:** You should not make modifications to quantities in `constants`. We implemented some safeguards to prevent accidental modifications. Intentional changes will lead to erratic behavior because we may change the VASP code assuming these quantities are constant. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PLUGINS/OCCUPANCIES&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Plugins](../tutorials/Plugins.md),
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md),
[PLUGINS/STRUCTURE](PLUGINS__STRUCTURE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/OCCUPANCIES-_incategory-Examples)



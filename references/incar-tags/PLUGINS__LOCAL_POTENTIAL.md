<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/LOCAL_POTENTIAL | revid: 34749 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/LOCAL_POTENTIAL


PLUGINS/LOCAL_POTENTIAL =
.True. \| .False.  
Default: **PLUGINS/LOCAL_POTENTIAL** = .False. 

Description:
PLUGINS/LOCAL_POTENTIAL calls
the Python plugin for the local potential interface for each SCF step

------------------------------------------------------------------------

When
PLUGINS/LOCAL_POTENTIAL=.TRUE.,
VASP calls the `local_potential` Python function at the end of each SCF
step. The primary use-case of this tag is to add a quantity on the real
space grid to the local potential and a scalar quantity to the total
energy of a VASP calculation through a Python plugin.

## Expected inputs\[<a
href="/wiki/index.php?title=PLUGINS/LOCAL_POTENTIAL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Expected inputs">edit</a> \| (./index.php.md)\]

The `local_potential` Python function expects the following inputs,


    def local_potential(constants, additions):
        ...


where `constants` and `additions` and
<a href="https://docs.python.org/3/library/dataclasses.html"
class="external text" rel="nofollow">Python dataclasses</a>. The
`constants` dataclass consists of the following inputs, listed here with
their associated
<a href="https://numpy.org/doc/stable/user/basics.types.html"
class="external text" rel="nofollow">datatypes</a>


    @dataclass(frozen=True)
    class ConstantsLocalPotential:
        ENCUT: float
        NELECT: float
        shape_grid: IntArray
        number_ions: int
        number_ion_types: int
        ion_types: IndexArray
        atomic_numbers: IntArray
        lattice_vectors: DoubleArray
        positions: DoubleArray
        ZVAL: DoubleArray
        charge_density: Optional[DoubleArray] = None
        hartree_potential: Optional[DoubleArray] = None
        ion_potential: Optional[DoubleArray] = None
        dipole_moment: Optional[DoubleArray] = None
        neighbor_list: List[Neighbors] = field(default_factory=list)


Note that the [INCAR](../input-files/INCAR.md) tags are capitalized.
`shape_grid` is a three dimensional integer array which stores the shape
of the real space grid, [NGXF](NGXF.md),
[NGYF](NGYF.md) and [NGZF](NGZF.md), `number_ions`
is the total number of ions listed in the
[POSCAR](../input-files/POSCAR.md) file, `number_ion_types` is the number
of ion corresponding to each ion type in the convention of the
[POSCAR](../input-files/POSCAR.md) file, `ion_types` stores the total
number of ion types, `atomic_numbers` contains the atomic number for
each atom type, `lattice_vectors` and `positions` contain the lattice
vectors and positions of the current SCF step
`charge_density`,`hartree_potential`,`ion_potential` contains the charge
density, the hartree potential and the ion potential respectively on the
real space grid. `dipole_moment` stores an array with three elements
consisting of the dipole moment along x, y and z cartesian directions.

|  |
|----|
| **Mind:** The dipole moment is provided only if [LDIPOL](LDIPOL.md)=.TRUE. |

`neighbor_list` contains a list of all neighbors near an atom up to a
cutoff
[PLUGINS/NEIGHBOR_CUTOFF](PLUGINS__NEIGHBOR_CUTOFF.md).

The `additions` dataclass consists of the following modifiable outputs


    @dataclass
    class AdditionsLocalPotential:
        total_energy: float
        total_potential: DoubleArray


## Modifying quantities\[<a
href="/wiki/index.php?title=PLUGINS/LOCAL_POTENTIAL&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Modifying quantities">edit</a> \| (./index.php.md)\]

Modify the quantities listed in additions by adding to them. For
example, if you wanted to add one to every real space local potential
grid point,


    import numpy as np
    def local_potential(constants, additions)
        additions.total_potential += np.ones(constants.shape_grid)


|  |
|----|
| **Warning:** You should not make modifications to quantities in `constants`. We implemented some safeguards to prevent accidental modifications. Intentional changes will lead to erratic behavior because we may change the VASP code assuming these quantities are constant. |

## Related tags and articles\[<a
href="/wiki/index.php?title=PLUGINS/LOCAL_POTENTIAL&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Plugins](../tutorials/Plugins.md),
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/NEIGHBOR_CUTOFF](PLUGINS__NEIGHBOR_CUTOFF.md),
[PLUGINS/OCCUPANCIES](PLUGINS__OCCUPANCIES.md),
[PLUGINS/STRUCTURE](PLUGINS__STRUCTURE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/LOCAL_POTENTIAL-_incategory-Examples)



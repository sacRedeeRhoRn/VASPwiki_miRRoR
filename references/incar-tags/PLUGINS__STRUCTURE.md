<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/STRUCTURE | revid: 34751 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/STRUCTURE
PLUGINS/STRUCTURE = .True. \| .False.  
Default: **PLUGINS/STRUCTURE** = .False. 

Description: PLUGINS/STRUCTURE calls the Python plugin for the structure
interface for each ionic relaxation step

------------------------------------------------------------------------

When PLUGINS/STRUCTURE=.TRUE., VASP calls the `structure` Python
function at the end of each ionic relaxation step. The primary use-case
of this tag is to modify the structure based on the computed energy,
force and stress tensor.

## Expected inputs
The `structure` Python function expects the following inputs,

    def structure(constants, additions):
        ...

where `constants` and `additions` and [Python
dataclasses](https://docs.python.org/3/library/dataclasses.html). The
`constants` dataclass consists of the following inputs, listed here with
their associated
[datatypes](https://numpy.org/doc/stable/user/basics.types.html)

    @dataclass(frozen=True)
    class ConstantsStructure:
        number_ions: int
        number_ion_types: int
        ion_types: IndexArray
        atomic_numbers: IntArray
        lattice_vectors: DoubleArray
        positions: DoubleArray
        POMASS: DoubleArray
        total_energy: float
        forces: DoubleArray
        stress: DoubleArray
        shape_grid: IntArray
        charge_density: DoubleArray
        neighbor_list: List[Neighbors] = field(default_factory=list)

Note that the [INCAR](../input-files/INCAR.md) tags are capitalized.
`number_ions` is the total number of ions listed in the
[POSCAR](../input-files/POSCAR.md) file, `number_ion_types` is the number
of ion corresponding to each ion type in the convention of the
[POSCAR](../input-files/POSCAR.md) file, `ion_types` stores the total
number of ion types, `atomic_numbers` contains the atomic number for
each atom type, `lattice_vectors` and `positions` contain the lattice
vectors and positions of the current SCF step `forces` and `stress` are
the computed forces and stress tensor and `charge_density` contains the
charge density on the real space grid. `shape_grid` is a three
dimensional integer array which stores the shape of the real space grid,
[NGXF](NGXF.md), [NGYF](NGYF.md) and
[NGZF](NGZF.md) and `charge_density` is the charge density on
this real space grid. `neighbor_list` contains a list of all neighbors
near an atom up to a cutoff
[PLUGINS/NEIGHBOR_CUTOFF](PLUGINS__NEIGHBOR_CUTOFF.md).

The `additions` dataclass consists of the following modifiable outputs

    @dataclass
    class AdditionsStructure:
        lattice_vectors: DoubleArray
        positions: DoubleArray

## Modifying quantities
Modify the quantities listed in additions by adding to them.

    def structure(constants, additions)
        additions.positions += np.ones((constants.number_ions,3))

|  |
|----|
| **Warning:** You should not make modifications to quantities in `constants`. We implemented some safeguards to prevent accidental modifications. Intentional changes will lead to erratic behavior because we may change the VASP code assuming these quantities are constant. |

## Related tags and articles
[Plugins](../tutorials/Plugins.md),
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md),
[PLUGINS/NEIGHBOR_CUTOFF](PLUGINS__NEIGHBOR_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/STRUCTURE-_incategory-Examples)

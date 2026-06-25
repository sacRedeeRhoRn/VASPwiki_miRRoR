<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/FORCE_AND_STRESS | revid: 34748 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/FORCE AND STRESS


PLUGINS/FORCE_AND_STRESS =
.True. \| .False.  
Default: **PLUGINS/FORCE_AND_STRESS** = .False. 

Description:
PLUGINS/FORCE_AND_STRESS calls
the Python plugin for the force and stress interface for each ionic
relaxation step

------------------------------------------------------------------------

When
PLUGINS/FORCE_AND_STRESS=.TRUE.,
VASP calls the `force_and_stress` Python function at the end of each
ionic relaxation step. You can use this tag to modify forces and the
stress tensor to be consistent with modifications to the potential
performed with
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md).
Furthermore, you could implement new force corrections like
van-der-Waals functionals or use it to run a machine-learned interatomic
potential as the force engine in VASP. Usually the forces and stress are
added to ones obtained by VASP, but you can set
[PLUGINS/ML_MODE](PLUGINS__ML_MODE.md) to overwrite
them instead.

## Expected inputs\[<a
href="/wiki/index.php?title=PLUGINS/FORCE_AND_STRESS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Expected inputs">edit</a> \| (./index.php.md)\]

The `force_and_stress` Python function expects the following inputs,


    def force_and_stress(constants, additions):
        ...


where `constants` and `additions` and
<a href="https://docs.python.org/3/library/dataclasses.html"
class="external text" rel="nofollow">Python dataclasses</a>. The
`constants` dataclass consists of the following inputs, listed here with
their associated
<a href="https://numpy.org/doc/stable/user/basics.types.html"
class="external text" rel="nofollow">datatypes</a>


    @dataclass(frozen=True)
    class ConstantsForceAndStress:
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
        POMASS: DoubleArray
        forces: DoubleArray
        stress: DoubleArray
        charge_density: Optional[DoubleArray] = None
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
vectors and positions of the current SCF step `forces` and `stress` are
the computed forces and stress tensor and `charge_density` contains the
charge density on the real space grid. `neighbor_list` contains a list
of all neighbors near an atom up to a cutoff
[PLUGINS/NEIGHBOR_CUTOFF](PLUGINS__NEIGHBOR_CUTOFF.md).

The `additions` dataclass consists of the following modifiable outputs


    @dataclass
    class AdditionsForceAndStress:
        total_energy: float
        forces: DoubleArray
        stress: DoubleArray


## Modifying quantities\[<a
href="/wiki/index.php?title=PLUGINS/FORCE_AND_STRESS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Modifying quantities">edit</a> \| (./index.php.md)\]

Modify the quantities listed in additions by adding to them. For
example, if you wanted to add one to the forces


    import numpy as np
    def force_and_stress(constants, additions)
        additions.forces += np.ones((constants.number_ions,3))


|  |
|----|
| **Warning:** You should not make modifications to quantities in `constants`. We implemented some safeguards to prevent accidental modifications. Intentional changes will lead to erratic behavior because we may change the VASP code assuming these quantities are constant. |

We provide a special helper class if you want to interface ASE
calculators with VASP. This class makes these use cases almost trivial


    from vasp.force_field import AseForceField

    def force_and_stress(constants, additions):
        calculator = ...  # setup your ASE calculator
        force_field = AseForceField(calculator)
        force_field.force_and_stress(constants, additions)


## Related tags and articles\[<a
href="/wiki/index.php?title=PLUGINS/FORCE_AND_STRESS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Plugins](../tutorials/Plugins.md),
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md),
[PLUGINS/OCCUPANCIES](PLUGINS__OCCUPANCIES.md),
[PLUGINS/ML_MODE](PLUGINS__ML_MODE.md),
[PLUGINS/NEIGHBOR_CUTOFF](PLUGINS__NEIGHBOR_CUTOFF.md),
[PLUGINS/STRUCTURE](PLUGINS__STRUCTURE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/FORCE_AND_STRESS-_incategory-Examples)



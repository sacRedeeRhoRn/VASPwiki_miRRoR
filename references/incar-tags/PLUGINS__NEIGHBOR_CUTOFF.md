<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/NEIGHBOR_CUTOFF | revid: 34742 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/NEIGHBOR CUTOFF


PLUGINS/NEIGHBOR_CUTOFF =
\[real\] 

Description:
PLUGINS/NEIGHBOR_CUTOFF
determines the cutoff up to which the neighbor list is computed that is
passed to the Python plugins. If not set, the neighbor list will be
empty.

------------------------------------------------------------------------

If set, VASP will compute pair distances between atoms in the unit cell
and include all pairs below the given cutoff in a neighbor list. You can
use this neighbor list in your plugin to make decisions based on the
interatomic distances.

In each plugin the `neighbor_list` is a list of length number of atoms,
where every element of the list is an instance of


    @dataclass(frozen=True)
    class Neighbors:
        neighbors: IndexArray
        distances: DoubleArray
        directions: DoubleArray


Here, `neigbors` are the indices of the atoms in vicinity of the
selected list element. Note that this can contain itself because of the
periodic boundary conditions. `distances` is the norm of the vector
between the atom and its neighbors. `directions` is the vector
describing the direction from the atom to its neighbor.

## Related tags and articles\[<a
href="/wiki/index.php?title=PLUGINS/NEIGHBOR_CUTOFF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Plugins](../tutorials/Plugins.md),
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md),
[PLUGINS/STRUCTURE](PLUGINS__STRUCTURE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/NEIGHBOR_CUTOFF-_incategory-Examples)



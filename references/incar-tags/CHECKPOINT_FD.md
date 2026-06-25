<!-- Source: https://vasp.at/wiki/index.php/CHECKPOINT_FD | revid: 34625 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CHECKPOINT_FD


CHECKPOINT_FD = CONTINUE \|
RESET \| NONE \| SINGLE  
Default: **CHECKPOINT_FD** = RESET 

Description: Enables a finite differences calculation to be restarted or
split up into displacements.

------------------------------------------------------------------------

<a href="/wiki/Phonons" class="mw-redirect" title="Phonons">Phonons</a>
can be calculated using [finite
differences](../tutorials/Phonons_from_finite_differences.md).
A series of displacements is made, DFT calculations are performed on
each of these, and then the second-order force constants are computed
and the dynamical matrix constructed, from which the phonon modes and
frequencies are calculated. Using
CHECKPOINT_FD (with
[`IBRION`](IBRION.md)` = 6`), it is possible to <a
href="/wiki/Construction:Restarting_finite_differences_calculations#Restarting_a_finite_difference_calculation"
class="mw-redirect"
title="Construction:Restarting finite differences calculations">restart
a calculation that crashed</a> from the last displacement, or <a
href="/wiki/Construction:Restarting_finite_differences_calculations#Splitting_a_finite_difference_calculation"
class="mw-redirect"
title="Construction:Restarting finite differences calculations">split
the calculation into individual displacements</a>. The displacements are
written to the [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md)
file.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

|  |
|----|
| **Important:** This feature requires [HDF5 support](../categories/Category-HDF5_support.md). |

|  |
|----|
| **Mind:** This is currently only available for [`IBRION`](IBRION.md)` = 6`. |

------------------------------------------------------------------------


## Contents


- [1 CHECKPOINT_FD
  = CONTINUE](#CHECKPOINT_FD_=_CONTINUE)
- [2 CHECKPOINT_FD
  = RESET (default)](#CHECKPOINT_FD_=_RESET_(default))
- [3 CHECKPOINT_FD
  = NONE](#CHECKPOINT_FD_=_NONE)
- [4 CHECKPOINT_FD
  = PREPARE](#CHECKPOINT_FD_=_PREPARE)
- [5 CHECKPOINT_FD
  = SINGLE](#CHECKPOINT_FD_=_SINGLE)
- [6 Related tags
  and articles](#Related_tags_and_articles)


### `CHECKPOINT_FD`` = CONTINUE`\[<a
href="/wiki/index.php?title=CHECKPOINT_FD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: CHECKPOINT_FD = CONTINUE">edit</a> \| (./index.php.md)\]

The [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file is read
(if it exists) and the calculation continues where it left off. If the
[vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file is missing,
a [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) is created and
the displacements are written to it. In both cases, the calculation will
finish with the complete
[vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md). Repeating
`CHECKPOINT_FD`` = CONTINUE`
will perform a single SCF at the equilibrium structure and read the
displacements from
[vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md).

This mode also detects if the calculation is a single VASP calculation
or if it was split into separate pieces. If it has been split, all the
calculations need to have finished, or an error will be produced.

### `CHECKPOINT_FD`` = RESET` (default)\[<a
href="/wiki/index.php?title=CHECKPOINT_FD&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: CHECKPOINT_FD = RESET (default)">edit</a> \| (./index.php.md)")\]

Overwrite the [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md)
file and start from scratch. The rest is identical to
`CHECKPOINT_FD`` = CONTINUE`.

### `CHECKPOINT_FD`` = NONE`\[<a
href="/wiki/index.php?title=CHECKPOINT_FD&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: CHECKPOINT_FD = NONE">edit</a> \| (./index.php.md)\]

No [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file is
written. This is the behavior of the code before VASP 6.6.0.

### `CHECKPOINT_FD`` = PREPARE`\[<a
href="/wiki/index.php?title=CHECKPOINT_FD&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: CHECKPOINT_FD = PREPARE">edit</a> \| (./index.php.md)\]

The [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file is
created (or overwritten) and filled with metadata. For each
displacement, a [CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md)
file is written containing the Nth displacement. The calculation stops
after performing one
<a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> to obtain
the SCF solution of the unperturbed structure.

To run the calculation for a specific displacement, create a directory
`disp-N`, copy across the corresponding
[CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md) file and rename
it to [POSCAR](../input-files/POSCAR.md). Then, run the calculation with
`CHECKPOINT_FD`` = SINGLE`.

### `CHECKPOINT_FD`` = SINGLE`\[<a
href="/wiki/index.php?title=CHECKPOINT_FD&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: CHECKPOINT_FD = SINGLE">edit</a> \| (./index.php.md)\]

This mode is used to run the individual single-shot VASP calculations
produced by
`CHECKPOINT_FD`` = PREPARE`.
This also produces a
[vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file in the
corresponding directory that contains the displaced data.

## Related tags and articles\[<a
href="/wiki/index.php?title=CHECKPOINT_FD&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Phonons from finite
differences](../tutorials/Phonons_from_finite_differences.md),
[Restarting finite differences
calculations](../tutorials/Restarting_finite_differences_calculations.md),
[IBRION](IBRION.md),
[vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md),
[CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CHECKPOINT_FD-_incategory-HowTo)



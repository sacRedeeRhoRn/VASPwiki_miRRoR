<!-- Source: https://vasp.at/wiki/index.php/Vaspcheckfd.h5 | revid: 34629 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# vaspcheckfd.h5


  
The vaspcheckfd.h5 file is
used to store the displacements for a restartable finite differences
calculation when using [`IBRION`](../incar-tags/IBRION.md)` = 6`. It
contains information related to the displacements (`displacements`) for
[phonons from finite
differences](../tutorials/Phonons_from_finite_differences.md).
The data for each displacement (`data-N`), and symmetry information
(`symmetry`). To generate or use the
vaspcheckfd.h5 file, refer to
how to [restart finite differences
calculations](../tutorials/Restarting_finite_differences_calculations.md)
with the [CHECKPOINT_FD](../incar-tags/CHECKPOINT_FD.md) tag.

You can view the contents of the file using `h5ls vaspcheckfd.h5`, which
contains the *N* displacements (in this case *N*=4):


     data-1                   Group
     data-2                   Group
     data-3                   Group
     data-4                   Group
     ...
     displacements            Group
     symmetry                 Group


## Related tags and articles\[<a
href="/wiki/index.php?title=Vaspcheckfd.h5&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [CHECKPOINT_FD](../incar-tags/CHECKPOINT_FD.md),
  [IBRION](../incar-tags/IBRION.md),
  [CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md)
- [Restarting finite differences
  calculations](../tutorials/Restarting_finite_differences_calculations.md)
- [Phonons from finite
  differences](../tutorials/Phonons_from_finite_differences.md)



<!-- Source: https://vasp.at/wiki/index.php/Vaspout.h5 | revid: 37343 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# vaspout.h5


The vaspout.h5 file is a
hierarchical HDF5 file containing the inputs and outputs of a VASP
calculation.

To analyze the data in this file we recommend using
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a>.

This file is only produced if your VASP version was compiled with [HDF5
support](../categories/Category-HDF5_support.md).

## Contents of the file\[<a
href="/wiki/index.php?title=Vaspout.h5&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Contents of the file">edit</a> \| (./index.php.md)\]

At the highest level, the
vaspout.h5 has the following
HDF5 groups:

1.  `input` - contains the parsed information of the
    [INCAR](../input-files/INCAR.md), [KPOINTS](../input-files/KPOINTS.md),
    and [POSCAR](../input-files/POSCAR.md) files, as well as a textual copy
    of the [POTCAR](../input-files/POTCAR.md) file. These are the actual
    inputs used by the calculation, which are not necessarily equivalent
    to the information given in the input files (e.g., if conflicting
    tags are used in the [INCAR](../input-files/INCAR.md) file).
2.  `original` - contains a textual copy of the provided
    [KPOINTS](../input-files/KPOINTS.md), [INCAR](../input-files/INCAR.md),
    and [POSCAR](../input-files/POSCAR.md) files that were provided to
    start the calculation.
3.  `intermediate` - contains information from MD and ionic relaxation
    calculations, including the positions of the ions, forces, stresses,
    and total energies for each ionic step.
4.  `results` - contains the final quantities of the calculation like
    the density of states, electronic eigenvalues, linear-response
    functions, etc...
5.  `version` - keeps track of which version of VASP was used to produce
    this file. This is needed for compatibility reasons with older
    files.

|  |
|----|
| **Warning:** Since the vaspout.h5 file contains the full [POTCAR](../input-files/POTCAR.md) file data, which are covered by the licence agreement, users are not allowed to make this file available to people who are not currently registered as licenced VASP users without removing these data first! |

## Related tags and sections\[<a
href="/wiki/index.php?title=Vaspout.h5&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[vaspin.h5](../input-files/Vaspin.h5.md),
[vaspwave.h5](Vaspwave.h5.md),
[OUTCAR](OUTCAR.md)



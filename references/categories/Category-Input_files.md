<!-- Source: https://vasp.at/wiki/index.php/Category:Input_files | revid: 25077 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Input files
As a minimal setup, VASP requires the following **input files**:

- the [INCAR](../input-files/INCAR.md) file,
- the [POSCAR](../input-files/POSCAR.md) file, and
- the [POTCAR](../input-files/POTCAR.md) file.

However, there are more optional **input files**, e.g., the
[KPOINTS](../input-files/KPOINTS.md) file, the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file, the
[ICONST](../input-files/ICONST.md) file, etc. A complete list is provided
below.

VASP calculations are often continued on top of a previous VASP
calculation. So, in case a calculation is restated, the [output
files](https://vasp.at/wiki/index.php/Category:Output_files) of the
previous calculation can be **input files** for the next calculation.
For instance, the [CHGCAR](../input-files/CHGCAR.md) file, the
[WAVECAR](../input-files/WAVECAR.md) file, the
[CONTCAR](../output-files/CONTCAR.md) file copied to
[POSCAR](../input-files/POSCAR.md), the [ML_ABN](../output-files/ML_ABN.md)
file copied to [ML_AB](../input-files/ML_AB.md), etc.

When [HDF5 support](Category-HDF5_support.md)
is enabled, the [vaspin.h5](../input-files/Vaspin.h5.md) file can
contain the same information and replace the
[INCAR](../input-files/INCAR.md), [POSCAR](../input-files/POSCAR.md),
[KPOINTS](../input-files/KPOINTS.md) and [POTCAR](../input-files/POTCAR.md)
files.

Finally, there is a special **input file** to induce a *soft stop* of
the calculation: the [STOPCAR](../incar-tags/STOPCAR.md) file. It is not
used in a standard workflow, but it might be convenient to stop a
calculation manually when it takes too long or a technical issue on the
compute engine arises.

<!-- Source: https://vasp.at/wiki/index.php/ML_EATOM | revid: 29874 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_EATOM


This file includes information on lattice constants, atom types, atom
positions, as well as kinetic and potential energy for each atom, for
every Molecular Dynamics (MD) step. In each MD step, the information is
structured as follows: first, the MD step is documented, followed by the
lattice constants. The subsequent section of the file is organized into
six columns. The initial column denotes the atom type, while columns two
to four present the atomic positions in Cartesian coordinates. The fifth
column indicates the kinetic energy, and the sixth column denotes the
potential energy for an individual atom.

The file is only written if
[ML_LEATOM](../incar-tags/ML_LEATOM.md)=**.TRUE.**.

------------------------------------------------------------------------



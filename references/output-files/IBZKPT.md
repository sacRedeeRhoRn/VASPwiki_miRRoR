<!-- Source: https://vasp.at/wiki/index.php/IBZKPT | revid: 29876 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IBZKPT


The IBZKPT file is compatible
with the [KPOINTS](../input-files/KPOINTS.md) file and is generated if the
automatic k-mesh generation is selected in the
[KPOINTS](../input-files/KPOINTS.md) file.
IBZKPT contains the k-point
coordinates and weights (and if the tetrahedron method was selected
additional tetrahedron connection tables are used) in the "Entering all
k-points explicitly" format used for providing k-points "by hand". This
file can also be generated with the external tool, *kpoints*.

IBZKPT maybe copied to
[KPOINTS](../input-files/KPOINTS.md) to save time, if one
[KPOINTS](../input-files/KPOINTS.md) set is used several times.

------------------------------------------------------------------------



<!-- Source: https://vasp.at/wiki/index.php/PROCAR_OPT | revid: 35403 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PROCAR_OPT
The PROCAR_OPT file contains the spd- and site-projected wave function
character at the **k** points of the
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) driver. It is written
whenever the [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) driver is
active, i.e., when a [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) file
is present or [KSPACING_OPT](../incar-tags/KSPACING_OPT.md) is set
in the [INCAR](../input-files/INCAR.md) file, and
[`LORBIT`](../incar-tags/LORBIT.md)` >= 10` or all
[RWIGS](../incar-tags/RWIGS.md) values are positive.

The PROCAR_OPT file has the same format as
[PROCAR](PROCAR.md); see that page for a detailed
description.

## Related tags and articles
Tags: [LKPOINTS_OPT](../incar-tags/LKPOINTS_OPT.md),
[KSPACING_OPT](../incar-tags/KSPACING_OPT.md),
[LORBIT](../incar-tags/LORBIT.md), [RWIGS](../incar-tags/RWIGS.md)

Files: [KPOINTS_OPT](../input-files/KPOINTS_OPT.md),
[PROCAR](PROCAR.md)

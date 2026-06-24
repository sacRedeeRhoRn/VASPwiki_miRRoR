<!-- Source: https://vasp.at/wiki/index.php/KPOINTS_OPT | revid: 25762 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINTS_OPT
KPOINTS_OPT is an optional input file to perform an additional one-shot
calculation after self-consistency is reached. The format is the same as
for the [KPOINTS](KPOINTS.md) file. VASP first performs a
self-consistent calculation using the **k** points specified in the
[KPOINTS](KPOINTS.md) file and then performs an additional
one-shot calculation to obtain the Kohn–Sham orbitals and eigenenergies
at the **k** points specified in the KPOINTS_OPT file.

[TABLE]

KPOINTS_OPT is read automatically when present. To avoid this, set
[LKPOINTS_OPT](../incar-tags/LKPOINTS_OPT.md)`=.FALSE.` in the
[INCAR](INCAR.md) file. VASP writes the
[PROCAR_OPT](../output-files/PROCAR_OPT.md) file when
[LORBIT](../incar-tags/LORBIT.md)\>10 and corresponding fields in the
[vaspout.h5](../output-files/Vaspout.h5.md) file indicated by the
keyword *kpoints_opt*.

|                                       |
|---------------------------------------|
| **Mind:** Available as of VASP 6.3.0. |

## Related tags and sections
[LKPOINTS_OPT](../incar-tags/LKPOINTS_OPT.md),
[KPOINTS](KPOINTS.md),
[KSPACING](../incar-tags/KSPACING.md),
[PROCAR_OPT](../output-files/PROCAR_OPT.md),
[KPOINTS_OPT_NKBATCH](../incar-tags/KPOINTS_OPT_NKBATCH.md)

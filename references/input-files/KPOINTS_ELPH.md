<!-- Source: https://vasp.at/wiki/index.php/KPOINTS_ELPH | revid: 27981 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINTS_ELPH
KPOINTS_ELPH is an optional input file to perform an additional one-shot
calculation after self-consistency is reached in the context of an
electron-phonon calculation. The format is the same as for the
[KPOINTS](KPOINTS.md) file. VASP first performs a
self-consistent calculation using the **k** points specified in the
[KPOINTS](KPOINTS.md) file and then performs an additional
one-shot calculation to obtain the Kohn–Sham orbitals and eigenenergies
at the **k** points specified in the KPOINTS_ELPH file.

The [KPOINTS](KPOINTS.md) file must contain a uniform **k**
mesh, when the KPOINTS_ELPH file should be used afterward.

Alternatively, it is possible to choose the k-point mesh by specifying
[ELPH_KSPACING](../incar-tags/ELPH_KSPACING.md) which determines
the smallest allowed spacing between **k** points in units of
$\AA^{-1}$.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

## Related tags and sections
- [ELPH_RUN](../incar-tags/ELPH_RUN.md)
- [KPOINTS](KPOINTS.md)
- [KPOINTS_OPT](KPOINTS_OPT.md)
- [ELPH_KSPACING](../incar-tags/ELPH_KSPACING.md)

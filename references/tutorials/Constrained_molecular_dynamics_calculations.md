<!-- Source: https://vasp.at/wiki/index.php/Constrained_molecular_dynamics_calculations | revid: 36200 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Constrained molecular dynamics calculations
Geometric constraints are introduced by defining one or more entries
with the STATUS parameter set to 0 in the
[ICONST](../input-files/ICONST.md)-file. Constraints can be used within a
standard NVT or NpT MD setting introduced by
[MDALGO](../incar-tags/MDALGO.md)=1\|2\|3. Note that fixing geometric
parameters related to lattice vectors is not allowed within an NVT
simulation (VASP would terminate with an error message). Constraints can
be combined with restraints, time-dependent bias potentials
([Metadynamics](../redirects/Category-Metadynamics.md)),
monitored coordinates and other elements available within the context of
MD.

## Related tags and articles
[ICONST](../input-files/ICONST.md),
[SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md),
[SHAKETOL](../incar-tags/SHAKETOL.md),
[SHAKETOLSOFT](../incar-tags/SHAKETOLSOFT.md),
[LBLUEOUT](../incar-tags/LBLUEOUT.md), [REPORT](../output-files/REPORT.md)

[Constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)

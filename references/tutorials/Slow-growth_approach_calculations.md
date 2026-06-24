<!-- Source: https://vasp.at/wiki/index.php/Slow-growth_approach_calculations | revid: 36213 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Slow-growth approach calculations
## Anderson thermostat
- For a slow-growth simulation, one has to perform a calcualtion very
  similar to [Constrained molecular
  dynamics](../theory/Constrained_molecular_dynamics.md)
  but additionally the transformation velocity-related
  [INCREM](../incar-tags/INCREM.md)-tag for each geometric parameter with
  `STATUS=0` has to be specified. For a slow-growth approach run with
  Andersen thermostat, one has to:

1.  Set the standard MD-related tags: [IBRION](../incar-tags/IBRION.md)=0,
    [TEBEG](../incar-tags/TEBEG.md), [POTIM](../incar-tags/POTIM.md), and
    [NSW](../incar-tags/NSW.md)
2.  Set [MDALGO](../incar-tags/MDALGO.md)=1, and choose an appropriate
    setting for [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)
3.  Define geometric constraints in the [ICONST](../input-files/ICONST.md)
    file, and set the **STATUS** parameter for the constrained
    coordinates to 0
4.  When the free-energy gradient is to be computed, set
    [LBLUEOUT](../incar-tags/LBLUEOUT.md)=.TRUE.

&nbsp;

5.  Specify the transformation velocity-related
    [INCREM](../incar-tags/INCREM.md)-tag for each geometric parameter
    with `STATUS=0`.

## Nose-Hoover thermostat
- For a slow-growth approach run with Nose-Hoover thermostat, one has
  to:

1.  Set the standard MD-related tags: [IBRION](../incar-tags/IBRION.md)=0,
    [TEBEG](../incar-tags/TEBEG.md), [POTIM](../incar-tags/POTIM.md), and
    [NSW](../incar-tags/NSW.md)
2.  Set [MDALGO](../incar-tags/MDALGO.md)=2, and choose an appropriate
    setting for [SMASS](../incar-tags/SMASS.md)
3.  Define geometric constraints in the
    [ICONST](../input-files/ICONST.md)-file, and set the `STATUS` parameter
    for the constrained coordinates to 0
4.  When the free-energy gradient is to be computed, set
    [LBLUEOUT](../incar-tags/LBLUEOUT.md)=.TRUE.

&nbsp;

5.  Specify the transformation velocity-related
    [INCREM](../incar-tags/INCREM.md)-tag for each geometric parameter
    with `STATUS=0`

  
VASP can handle multiple (even redundant) constraints. Note, however,
that a too large number of constraints can cause problems with the
stability of the [SHAKE algorithm](#SHAKE). In problematic cases, it is
recommended to use a looser convergence criterion (see
[SHAKETOL](../incar-tags/SHAKETOL.md)) and to allow a larger number of
iterations (see [SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md)) in
the [SHAKE algorithm](#SHAKE). Hard constraints may also be used in
[metadynamics simulations](../theory/Metadynamics.md) (see
[MDALGO](../incar-tags/MDALGO.md)=11 \| 21). Information about the
constraints is written onto the [REPORT](../output-files/REPORT.md)-file:
check the lines following the string: `Const_coord`

## Related tags and articles
[ICONST](../input-files/ICONST.md), [INCREM](../incar-tags/INCREM.md),
[SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md),
[SHAKETOL](../incar-tags/SHAKETOL.md),
[SHAKETOLSOFT](../incar-tags/SHAKETOLSOFT.md),
[LBLUEOUT](../incar-tags/LBLUEOUT.md), [REPORT](../output-files/REPORT.md)

[Slow-growth
approach](../theory/Slow-growth_approach.md)

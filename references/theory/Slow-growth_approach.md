<!-- Source: https://vasp.at/wiki/index.php/Slow-growth_approach | revid: 36202 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Slow-growth approach
The free-energy profile along a geometric parameter
$\xi$ can be scanned by an approximate
slow-growth approach^([\[1\]](#cite_note-woo:ziegler:1997-1)). In this
method, the value of $\xi$ is linearly
changed from the value characteristic for the initial state (1) to that
for the final state (2) with a velocity of transformation
$\dot{\xi}$. The resulting work needed
to perform a transformation $1 \rightarrow 2$ can be computed as:

$w^{irrev}_{1 \rightarrow
2}=\int_{{\xi(1)}}^{{\xi(2)}} \left ( \frac{\partial {V(q)}} {\partial
\xi} \right ) \cdot \dot{\xi}\\ dt.$

In the limit of infinitesimally small $\dot{\xi}$, the work $w^{irrev}_{1 \rightarrow 2}$ corresponds to the free-energy difference between the the
final and initial state. In the general case, $w^{irrev}_{1 \rightarrow 2}$ is the irreversible work related
to the free energy via Jarzynski's identity
^([\[2\]](#cite_note-jarzynski:prl:1997-2)):

$exp^{-\frac{\Delta A_{1 \rightarrow
2}}{k_B\\T}}= \bigg \langle exp^{-\frac{w^{irrev}_{1 \rightarrow
2}}{k_B\\T}} \bigg\rangle.$

Note that calculation of the free-energy via this equation requires
averaging of the term ${\rm exp} \left
\\-\frac{w^{irrev}_{1 \rightarrow 2}}{k_B\\T} \right \\$ over
many realizations of the $1 \rightarrow 2$ transformation. Detailed description of the simulation
protocol that employs Jarzynski's identity can be found in reference
^([\[3\]](#cite_note-overhofer:geissler:2005-3)).

## How to
- For a slow-growth simulation, one has to perform a calcualtion very
  similar to [Constrained molecular
  dynamics](Constrained_molecular_dynamics.md)
  but additionally the transformation velocity-related
  [INCREM](../incar-tags/INCREM.md) tag for each geometric parameter with
  `STATUS=0` has to be specified:

1.  Set the standard MD-related tags: [IBRION](../incar-tags/IBRION.md)=0,
    [TEBEG](../incar-tags/TEBEG.md), [POTIM](../incar-tags/POTIM.md), and
    [NSW](../incar-tags/NSW.md)
2.  Choose a thermostat:
    1.  Set [MDALGO](../incar-tags/MDALGO.md)=1, and choose an appropriate
        setting for [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)
    2.  Set [MDALGO](../incar-tags/MDALGO.md)=2, and choose an appropriate
        setting for [SMASS](../incar-tags/SMASS.md)
3.  Define geometric constraints in the [ICONST](../input-files/ICONST.md)
    file, and set the STATUS parameter for the constrained coordinates
    to 0
4.  When the free-energy gradient is to be computed, set
    [LBLUEOUT](../incar-tags/LBLUEOUT.md)=.TRUE.

&nbsp;

5.  Specify the transformation velocity-related
    [INCREM](../incar-tags/INCREM.md)-tag for each geometric parameter
    with `STATUS=0`.

## Related tags and articles
[ICONST](../input-files/ICONST.md), [INCREM](../incar-tags/INCREM.md),
[SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md),
[SHAKETOL](../incar-tags/SHAKETOL.md),
[SHAKETOLSOFT](../incar-tags/SHAKETOLSOFT.md),
[LBLUEOUT](../incar-tags/LBLUEOUT.md), [REPORT](../output-files/REPORT.md)

[Slow-growth approach
calculations](../tutorials/Slow-growth_approach_calculations.md)

## References
1.  [↑](#cite_ref-woo:ziegler:1997_1-0) [T. Woo, P. Margl, P. Blöchl, T.
    Ziegler. J. Phys. Chem., **101**, 40
    (1997)](https://doi.org/10.1021/jp9717296)
2.  [↑](#cite_ref-jarzynski:prl:1997_2-0) [C. Jarzynski, Phys. Rev.
    Lett. **78**, 2690
    (1997).](https://doi.org/10.1103/PhysRevLett.78.2690)
3.  [↑](#cite_ref-overhofer:geissler:2005_3-0) [Oberhofer, C.
    Dellago, P. L. Geissler, J. Phys. Chem. B 109, 6902
    (2005).](https://doi.org/10.1021/jp044556a)

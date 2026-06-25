<!-- Source: https://vasp.at/wiki/index.php/Constrained_molecular_dynamics | revid: 36201 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Constrained molecular dynamics



Constrained molecular dynamics is performed using the
SHAKE[^ryckaertt:jcp:1977-1]
algorithm. In this algorithm, the Lagrangian for the system
$\mathcal{L}$ is extended as follows:

$\mathcal{L}^\*(\mathbf{q,\dot{q}}) = \mathcal{L}(\mathbf{q,\dot{q}}) +
\sum_{i=1}^{r} \lambda_i \sigma_i(q),$

where the summation is over *r* geometric constraints,
$\mathcal{L}^\*$ is the Lagrangian for the extended
system, and λ<sub>*i*</sub> is a Lagrange multiplier associated with a
geometric constraint σ<sub>*i*</sub>:

$\sigma_i(q) = \xi_i({q})-\xi_i \\$

with ξ<sub>*i*</sub>(*q*) being a geometric parameter and
ξ<sub>*i*</sub> is the value of ξ<sub>*i*</sub>(*q*) fixed during the
simulation.

In the SHAKE algorithm, the Lagrange multipliers λ<sub>i</sub> are
determined in the iterative procedure:

1.  Perform a standard MD step (leap-frog algorithm):
    $v^{t+{\Delta}t/2}_i =
    v^{t-{\Delta}t/2}_i + \frac{a^{t}_i}{m_i} {\Delta}t$
    $q^{t+{\Delta}t}_i =
    q^{t}_i + v^{t+{\Delta}t/2}_i{\Delta}t$
2.  Use the new positions *q*(*t*+Δ*t*) to compute Lagrange multipliers
    for all constraints:
    ${\lambda}_k=
    \frac{1}{{\Delta}t^2} \frac{\sigma_k(q^{t+{\Delta}t})}{\sum_{i=1}^N
    m_i^{-1} \bigtriangledown_i{\sigma}_k(q^{t})
    \bigtriangledown_i{\sigma}_k(q^{t+{\Delta}t})}$
3.  Update the velocities and positions by adding a contribution due to
    restoring forces (proportional to λ<sub>k</sub>):
    $v^{t+{\Delta}t/2}_i =
    v^{t-{\Delta}t/2}_i + \left( a^{t}_i-\sum_k
    \frac{{\lambda}_k}{m_i} \bigtriangledown_i{\sigma}_k(q^{t}) \right
    ) {\Delta}t$
    $q^{t+{\Delta}t}_i =
    q^{t}_i + v^{t+{\Delta}t/2}_i{\Delta}t$
4.  repeat steps 2-4 until either \|σ<sub>*i*</sub>(*q*)\| are smaller
    than a predefined tolerance (determined by
    [SHAKETOL](../incar-tags/SHAKETOL.md)), or the number of iterations
    exceeds [SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md).


### Constrained molecular dynamics\[<a
href="/wiki/index.php?title=Constrained_molecular_dynamics&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Constrained molecular dynamics">edit</a> \| (./index.php.md)\]

For a description of constrained molecular dynamics see
Constrained molecular
dynamics.

- For a constrained molecular dynamics run with Andersen thermostat, one
  has to:

1.  Set the standard MD-related tags: [IBRION](../incar-tags/IBRION.md)=0,
    [TEBEG](../incar-tags/TEBEG.md), [POTIM](../incar-tags/POTIM.md), and
    [NSW](../incar-tags/NSW.md)
2.  Select the thermostat:
    1.  Set [MDALGO](../incar-tags/MDALGO.md) = 1 , and choose an
        appropriate setting for
        [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md).
    2.  Set [MDALGO](../incar-tags/MDALGO.md) = 2 , and choose an
        appropriate setting for [SMASS](../incar-tags/SMASS.md).
3.  Define geometric constraints in the
    [ICONST](../input-files/ICONST.md)-file, and set the STATUS parameter
    for the constrained coordinates to 0
4.  When the free-energy gradient is to be computed, set
    [LBLUEOUT](../incar-tags/LBLUEOUT.md)=.TRUE.

## Related tags and articles\[<a
href="/wiki/index.php?title=Constrained_molecular_dynamics&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ICONST](../input-files/ICONST.md),
[SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md),
[SHAKETOL](../incar-tags/SHAKETOL.md),
[SHAKETOLSOFT](../incar-tags/SHAKETOLSOFT.md),
[LBLUEOUT](../incar-tags/LBLUEOUT.md), [REPORT](../output-files/REPORT.md)

[Constrained molecular dynamics
calculations](../tutorials/Constrained_molecular_dynamics_calculations.md)

## References\[<a
href="/wiki/index.php?title=Constrained_molecular_dynamics&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^ryckaertt:jcp:1977-1]: [J. P. Ryckaert, G. Ciccotti, and H. J. C. Berendsen, J. Comp. Phys. **23**, 327 (1977).](http://dx.doi.org/10.1016/0021-9991(77)90098-5)

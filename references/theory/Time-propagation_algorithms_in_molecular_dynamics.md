<!-- Source: https://vasp.at/wiki/index.php/Time-propagation_algorithms_in_molecular_dynamics | revid: 32324 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Time-propagation algorithms in molecular dynamics


In <a href="/wiki/MD" class="mw-redirect" title="MD">molecular dynamics
simulations</a>, the ionic positions $\mathbf{r}_{i}(t)$ and velocities $\mathbf{v}_{i}(t)$ are monitored as functions of time
$t$. This time dependence is obtained by integrating
Newton's equations of motion. When integrating the equations of motions
it is important to use symplectic algorithms which conserve the
phase-space volume. To solve the equations of motion under symplectic
conditions, various integration algorithms have been developed. The time
dependence of a particle can be expressed in a Taylor expansion

$\mathbf{r}_{i}(t+\Delta t) = \mathbf{r}_{i}(t) +
\mathbf{v}_{i}(t)\Delta t + \frac{\mathbf{F}_{i}}{2m}(t)\Delta t^{2} +
\frac{\partial^{3} \mathbf{r}_{i}(t)}{\partial t^{3}}\Delta t^{3} +
\mathcal{O}(\Delta t^{4})$

A backward propagation in time by a time step
$\Delta t$ can be obtained in a similar way

$\mathbf{r}_{i}(t-\Delta t) = \mathbf{r}_{i}(t) -
\mathbf{v}_{i}(t)\Delta t + \frac{\mathbf{F}_{i}}{2m}(t)\Delta t^{2} -
\frac{\partial^{3} \mathbf{r}_{i}(t)}{\partial t^{3}}\Delta t^{3} +
\mathcal{O}(\Delta t^{4})$

Adding these two equation gives and rearrangement gives the Verlet
algorithm

$\mathbf{r}_{i}(t+\Delta t) =
2\mathbf{r}_{i}(t)-\mathbf{r}_{i}(t-\Delta
t)+\frac{\mathbf{F}_{i}}{2m}(t)\Delta t^{2}+\mathcal{O}(\Delta t ^{3})$

The Verlet algorithm can be rearranged to the Velocity-Verlet algorithm
by inserting $\mathbf{v}_{i}(t)=\frac{\mathbf{r}_{i}(t)-\mathbf{r}_{i}(t-\Delta
t)}{\Delta t}$

$\mathbf{r}_{i}(t+\Delta t) = \mathbf{r}_{i}(t)+
\mathbf{v}_{i}(t)\Delta t+\frac{\mathbf{F}_{i}}{2m}(t)\Delta t^{2}.$


## Contents


- [1
  Velocity-Verlet integration
  scheme](#velocity-verlet-integration-scheme)
- [2 Leap-Frog
  integration scheme](#leap-frog-integration-scheme)
- [3 Thermostats
  and used integrators](#thermostats-and-used-integrators)
- [4 Related tags
  and articles](#related-tags-and-articles)


## Velocity-Verlet integration scheme\[<a
href="/wiki/index.php?title=Time-propagation_algorithms_in_molecular_dynamics&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Velocity-Verlet integration scheme">edit</a> \| (./index.php.md)\]

The Velocity-Verlet algorithm can be decomposed into the following
steps:

1.  $\mathbf{v}_{i}(t +
    \frac{1}{2}\Delta
    t)=\mathbf{v}_{i}(t)+\frac{\mathbf{F}_{i}(t)}{2m_{i}}\Delta t$
2.  $\mathbf{r}_{i}(t +
    \Delta t) = \mathbf{r}_{i}(t) + \mathbf{v}_{i}(t +
    \frac{1}{2}\Delta t)\Delta t$
3.  compute forces $\mathbf{F}_{i}(t)$ from density functional theory or machine learning
4.  $\mathbf{v}_{i}(t + \Delta
    t)=\mathbf{v}_{i}(t+\frac{1}{2}\Delta
    t)+\frac{\mathbf{F}_{i}(t+\Delta t)}{2m_{i}}\Delta t$

From these equations it can be seen that the velocity and the position
vectors are synchronous in time.

## Leap-Frog integration scheme\[<a
href="/wiki/index.php?title=Time-propagation_algorithms_in_molecular_dynamics&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Leap-Frog integration scheme">edit</a> \| (./index.php.md)\]

Another form of the Verlet algorithm can be written in the form of the
Leap-Frog algorithm. The Leap-Frog algorithm consists of the following
steps:

1.  compute forces $\mathbf{F}_{i}(t)$ from density functional theory or machine learning
2.  $\mathbf{v}_{i}(t +
    \frac{1}{2}\Delta t)=\mathbf{v}_{i}(t- \frac{1}{2}\Delta
    t)+\frac{\mathbf{F}_{i}(t)}{m_{i}}\Delta t$
3.  $\mathbf{r}_{i}(t +
    \Delta t) = \mathbf{r}_{i}(t) + \mathbf{v}_{i}(t +
    \frac{1}{2}\Delta t)\Delta t$

In this form the velocity and the position vectors are asynchronous in
time.

## Thermostats and used integrators\[<a
href="/wiki/index.php?title=Time-propagation_algorithms_in_molecular_dynamics&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Thermostats and used integrators">edit</a> \| (./index.php.md)\]

|  |  |  |
|----|----|----|
| MDALGO | thermostat | integration algorithm |
| 0 | [Nosé-Hoover](../tutorials/Nosé-Hoover_thermostat.md) | [Velocity-Verlet](#velocity-verlet-integration-scheme) |
| 1 | [Andersen](../tutorials/Andersen_thermostat.md) | [Leap-Frog](#leap-frog-integration-scheme) |
| 2 | [Nosé-Hoover](../tutorials/Nosé-Hoover_thermostat.md) | [Leap-Frog](#leap-frog-integration-scheme) |
| 3 | [Langevin](../tutorials/Langevin_thermostat.md) | [Velocity-Verlet](#velocity-verlet-integration-scheme) |
| 4 | [Nosé-Hoover chain](../misc/Nosé-Hoover_chain_thermostat.md) | [Velocity-Verlet](#velocity-verlet-integration-scheme) |
| 5 | [CSVR](CSVR_thermostat.md) | [Leap-Frog](#leap-frog-integration-scheme) |
| 5 | [Multiple Andersen](../incar-tags/MDALGO.md) | [Leap-Frog](#leap-frog-integration-scheme) |

## Related tags and articles\[<a
href="/wiki/index.php?title=Time-propagation_algorithms_in_molecular_dynamics&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBRION](../incar-tags/IBRION.md), [MDALGO](../incar-tags/MDALGO.md),
<a href="/wiki/Thermostats" class="mw-redirect"
title="Thermostats">Thermostats</a>



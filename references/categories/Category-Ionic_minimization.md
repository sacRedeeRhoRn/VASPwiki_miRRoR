<!-- Source: https://vasp.at/wiki/index.php/Category:Ionic_minimization | revid: 27197 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Ionic minimization


By virtue of the Born-Oppenheimer approximation, the electronic and
ionic degrees of freedom are treated separately in VASP. Using the
Hellmann-Feynman theorem, VASP can approximate the forces on each ion
due to the electronic ground state. The most straightforward approach to
**ionic minimization** is to move the ionic positions such that the
force at each site vanishes. This is also known as structure
optimization.

Alternatively to the Hellmann-Feynman theorem, VASP can [machine learn
force
fields](Category-Machine-learned_force_fields.md)
and, thus, obtain forces approximately 1000 times faster compared to
performing an [electronic
minimization](Category-Electronic_minimization.md).
However, VASP first needs to train on the density-functional-theory
(DFT) solutions of similar structures to obtain a [machine-learned force
field](Category-Machine-learned_force_fields.md),
so it is still necessary to perform DFT calculations. Therefore, this
approach is beneficial for large supercells, where it is possible to
train on a smaller system.

Finally, **ionic minimization** does not generally follow the physical
path of an ion. For instance, the quasi-Newton RMM-DIIS algorithm
([IBRION](../incar-tags/IBRION.md)=1) and conjugate-gradient algorithm
([IBRION](../incar-tags/IBRION.md)=2) aim to minimize the total energy
without regarding any equation of motion. In contrast, there are various
algorithms based on [molecular
dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
that can be used to tackle the **ionic-minimization** problem.

## Theory\[<a
href="/wiki/index.php?title=Category:Ionic_minimization&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theory">edit</a> \| (./index.php.md)\]

- Forces:
  <a href="/wiki/Forces" class="mw-redirect" title="Forces">Forces</a>.

## How to\[<a
href="/wiki/index.php?title=Category:Ionic_minimization&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

- [Structure
  optimization](../tutorials/Structure_optimization.md)
- Effect of Pulay stress on volume optimizations: <a
  href="/wiki/index.php?title=Energy_vs_volume_Volume_relaxations_and_Pulay_stress&amp;action=edit&amp;redlink=1"
  class="new"
  title="Energy vs volume Volume relaxations and Pulay stress (page does not exist)">Energy
  vs volume Volume relaxations and Pulay stress</a>.

------------------------------------------------------------------------



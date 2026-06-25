<!-- Source: https://vasp.at/wiki/index.php/Category:Molecular_Dynamics | revid: 11071 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Molecular Dynamics


To get an idea about what basically molecular dynamics is and what the
main contents are we refer the reader to references
[^frenkel:book:1996-1]
and
[^allen:book:1991-2].
After understanding the theory behind molecular dynamics we refer the
reader to
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular dynamics
calculations</a>, which describes how to run standard molecular dynamics
simulations. Every advanced molecular dynamics method builds on the
knowledge in that tutorial and should be ideally only viewed after
understanding the basics.


## Contents


- [1 Important
  files](#important-files)
- [2
  Theory](#theory)
- [3 How
  to](#how-to)
- [4
  Compilation](#compilation)
- [5 Additional
  resources](#additional-resources)
  - [5.1
    Books](#books)
  - [5.2
    Tutorials](#tutorials)
  - [5.3
    Lectures](#lectures)
- [6
  References](#references)


## Important files\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Important files">edit</a> \| (./index.php.md)\]

The input files for standard molecular dynamics runs are the same as for
other calculational methods. However additionally to the structural data
the [POSCAR](../input-files/POSCAR.md) file can contain the initial
velocities as a separate block. It can also contain the input on which
atomic positions should be constrained or not.

Constrained and bias molecular dynamics ([Constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md),
[Metadynamics](../theory/Metadynamics.md) and [Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md))
also require an additional input file, the
[ICONST](../input-files/ICONST.md) file. This file specifies the collective
variables. The ([ICONST](../input-files/ICONST.md)) file is also required
for the monitoring of geometric parameters ([Monitoring geometric
parameters](../incar-tags/MDALGO.md)).

  
Besides the main output files, [OUTCAR](../output-files/OUTCAR.md) and
[OSZICAR](../output-files/OSZICAR.md), the
[XDATCAR](../output-files/XDATCAR.md) is an important output file. It
contains the trajectory of the MD. Another important output file for
molecular dynamics calculations is the [REPORT](../output-files/REPORT.md)
file. It contains various important information and is especially
important for calculations where the [ICONST](../input-files/ICONST.md)
file was used.

## Theory\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Theory">edit</a> \| (./index.php.md)\]

- Ensembles: [Ensembles](Category-Ensembles.md).
- Thermostats:
  [Thermostats](Category-Thermostats.md).
- Interface pinning: [Interface pinning
  calculations](../tutorials/Interface_pinning_calculations.md).
- Constrained molecular dynamics: [Constrained molecular
  dynamics](../theory/Constrained_molecular_dynamics.md).
- Metadynamics: [Metadynamics](../theory/Metadynamics.md).
- Biased molecular dynamics: [Biased molecular
  dynamics](../theory/Biased_molecular_dynamics.md).
- Slow-growth approach: [Slow-growth
  approach](../theory/Slow-growth_approach.md).

## How to\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

- Basic molecular dynamics calculations:
  <a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
  title="Molecular dynamics calculations">Molecular dynamics
  calculations</a>.
- Ensembles: [Ensembles](Category-Ensembles.md).
- Thermostats:
  [Thermostats](Category-Thermostats.md).
- Interface pinning: [Interface pinning
  calculations](../tutorials/Interface_pinning_calculations.md).
- Constrained molecular dynamics: [Constrained molecular
  dynamics](../theory/Constrained_molecular_dynamics.md).
- Metadynamics: [Metadynamics](../theory/Metadynamics.md).
- Biased molecular dynamics: [Biased molecular
  dynamics](../theory/Biased_molecular_dynamics.md).
- Slow-growth approach: [Slow-growth
  approach](../theory/Slow-growth_approach.md).
- Monitoring of geometric parameters: [Monitoring geometric
  parameters](../incar-tags/MDALGO.md).
- Thermodynamic integration: [Thermodynamic
  integration](Category-Thermodynamic_integration.md)
- Thermal conductivity [Müller-Plathe
  method](../tutorials/Müller-Plathe_method.md)

## Compilation\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Compilation">edit</a> \| (./index.php.md)\]

Many of the simulation methods described in this section are included in
VASP as of version 5.2.12, and require VASP to be compiled with the
<a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">preprocessor flag <code>-Dtbdyn</code></a>.
This is usually the case because all
[makefile.include](../misc/Makefile.include.md) templates
shipped with VASP since version 5.4.4 contain this flag by default.

## Additional resources\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Books\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Books">edit</a> \| (./index.php.md)\]

- *Statistical Mechanics: Theory and Molecular Simulation* by M.
  Tuckerman
  [^tuckerman:book:2023-3].
- *Understanding Molecular Simulation - From Algorithms to Applications*
  by D. Frenkel and B. Smit
  [^frenkel:smit:2023-4].

### Tutorials\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for <a href="https://www.vasp.at/tutorials/latest/md/part1"
  class="external text" rel="nofollow">MD calculations</a>.
- Tutorial for <a href="https://www.vasp.at/tutorials/latest/md/part2"
  class="external text" rel="nofollow">training a machine learning force
  field using MD</a>.
- Tutorial for chloromethane-chloride inversion
  <a href="https://www.vasp.at/tutorials/latest/md/part3"
  class="external text" rel="nofollow">using the slow-growth approach,
  blue-moon ensemble, and constrained MD</a>.
- Tutorial for a chemical reaction in a zeolite
  <a href="https://www.vasp.at/tutorials/latest/transition_states/part3"
  class="external text" rel="nofollow">using the slow-growth approach,
  blue-moon ensemble, and constrained MD</a>

### Lectures\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture for an
  <a href="https://youtu.be/8txbZcgm6pQ" class="external text"
  rel="nofollow">introduction to MD</a>.
- Lecture on
  <a href="https://youtu.be/HVeamQOmM-s" class="external text"
  rel="nofollow">advanced methods in MD</a>.

## References\[<a
href="/wiki/index.php?title=Category:Molecular_dynamics&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^frenkel:book:1996-1]: [D. Frenkel and B. Smit, Understanding Molecular Simulation (Academic Press, London, 1996).](https://doi.org/10.1016/B978-0-12-267351-1.X5000-7)
[^allen:book:1991-2]: [M. P. Allen and D. J. Tildesley, *Computer simulation of liquids* (Oxford university press: New York, 1991).](https://books.google.co.jp/books?id=WFExDwAAQBAJ&lpg=PP1&hl=ja&pg=PP1#v=onepage&q&f=false)
[^tuckerman:book:2023-3]: [M. Tuckerman, *Statistical Mechanics: Theory and Molecular Simulation (2nd edn)*, Oxford University Press (2023).](https://doi.org/10.1093/oso/9780198825562.001.0001)
[^frenkel:smit:2023-4]: [D. Frenkel, B. Smit, *Understanding Molecular Simulation - From Algorithms to Applications (2nd edn)*, Elsevier Science (2023).](https://doi.org/10.1016/B978-0-12-267351-1.X5000-7)

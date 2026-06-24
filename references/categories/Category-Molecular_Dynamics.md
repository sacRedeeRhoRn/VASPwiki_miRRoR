<!-- Source: https://vasp.at/wiki/index.php/Category:Molecular_Dynamics | revid: 11071 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Molecular Dynamics
To get an idea about what basically molecular dynamics is and what the
main contents are we refer the reader to references
^([\[1\]](#cite_note-frenkel:book:1996-1)) and
^([\[2\]](#cite_note-allen:book:1991-2)). After understanding the theory
behind molecular dynamics we refer the reader to [Molecular dynamics
calculations](../redirects/Molecular_dynamics_calculations.md),
which describes how to run standard molecular dynamics simulations.
Every advanced molecular dynamics method builds on the knowledge in that
tutorial and should be ideally only viewed after understanding the
basics.

## Contents

- [1 Important files](#Important_files)
- [2 Theory](#Theory)
- [3 How to](#How_to)
- [4 Compilation](#Compilation)
- [5 Additional resources](#Additional_resources)
  - [5.1 Books](#Books)
  - [5.2 Tutorials](#Tutorials)
  - [5.3 Lectures](#Lectures)
- [6 References](#References)

## Important files
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

## Theory
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

## How to
- Basic molecular dynamics calculations: [Molecular dynamics
  calculations](../redirects/Molecular_dynamics_calculations.md).
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

## Compilation
Many of the simulation methods described in this section are included in
VASP as of version 5.2.12, and require VASP to be compiled with the
[preprocessor flag
`-Dtbdyn`](../redirects/Precompiler_flags.md). This is usually
the case because all
[makefile.include](../misc/Makefile.include.md) templates
shipped with VASP since version 5.4.4 contain this flag by default.

## Additional resources
### Books
- *Statistical Mechanics: Theory and Molecular Simulation* by M.
  Tuckerman ^([\[3\]](#cite_note-tuckerman:book:2023-3)).
- *Understanding Molecular Simulation - From Algorithms to Applications*
  by D. Frenkel and B. Smit ^([\[4\]](#cite_note-frenkel:smit:2023-4)).

### Tutorials
- Tutorial for [MD
  calculations](https://www.vasp.at/tutorials/latest/md/part1).
- Tutorial for [training a machine learning force field using
  MD](https://www.vasp.at/tutorials/latest/md/part2).
- Tutorial for chloromethane-chloride inversion [using the slow-growth
  approach, blue-moon ensemble, and constrained
  MD](https://www.vasp.at/tutorials/latest/md/part3).
- Tutorial for a chemical reaction in a zeolite [using the slow-growth
  approach, blue-moon ensemble, and constrained
  MD](https://www.vasp.at/tutorials/latest/transition_states/part3)

### Lectures
- Lecture for an [introduction to MD](https://youtu.be/8txbZcgm6pQ).
- Lecture on [advanced methods in MD](https://youtu.be/HVeamQOmM-s).

## References
1.  [↑](#cite_ref-frenkel:book:1996_1-0) [D. Frenkel and B. Smit,
    Understanding Molecular Simulation (Academic Press, London,
    1996).](https://doi.org/10.1016/B978-0-12-267351-1.X5000-7)
2.  [↑](#cite_ref-allen:book:1991_2-0) [M. P. Allen and D. J. Tildesley,
    *Computer simulation of liquids* (Oxford university press: New York,
    1991).](https://books.google.co.jp/books?id=WFExDwAAQBAJ&lpg=PP1&hl=ja&pg=PP1#v=onepage&q&f=false)
3.  [↑](#cite_ref-tuckerman:book:2023_3-0) [M. Tuckerman, *Statistical
    Mechanics: Theory and Molecular Simulation (2nd edn)*, Oxford
    University Press
    (2023).](https://doi.org/10.1093/oso/9780198825562.001.0001)
4.  [↑](#cite_ref-frenkel:smit:2023_4-0) [D. Frenkel, B. Smit,
    *Understanding Molecular Simulation - From Algorithms to
    Applications (2nd edn)*, Elsevier Science
    (2023).](https://doi.org/10.1016/B978-0-12-267351-1.X5000-7)

  

------------------------------------------------------------------------

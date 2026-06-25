<!-- Source: https://vasp.at/wiki/index.php/Minimal_reproducible_example | revid: 22963 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Minimal reproducible example


A **minimal reproducible example** is a set of input and output files
that allow a bug, problem, or result to be demonstrated and reproduced.
A crucial point is that the **minimal reproducible example** should be
as small and simple as possible.

It is helpful to create a **minimal reproducible example** when
reporting an issue to a colleague, supervisor, or on the
<a href="https://www.vasp.at/forum/" class="external text"
rel="nofollow">VASP forum</a>, but also as a starting point to explore
more options and features based on a known system.


## Contents


- [1 How to create
  a minimal reproducible
  example](#how-to-create-a-minimal-reproducible-example)
  - [1.1 Step
    1](#step-1)
  - [1.2 Step
    2](#step-2)
  - [1.3 Step
    3](#step-3)
- [2 Related tags
  and articles](#related-tags-and-articles)


## How to create a minimal reproducible example\[<a
href="/wiki/index.php?title=Minimal_reproducible_example&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: How to create a minimal reproducible example">edit</a> \| (./index.php.md)\]

### Step 1\[<a
href="/wiki/index.php?title=Minimal_reproducible_example&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step 1">edit</a> \| (./index.php.md)\]

To reduce the complexity of a calculation, remove all preparatory and
unnecessary post-processing steps from the workflow and any
<a href="/wiki/INCAR_tag" class="mw-redirect" title="INCAR tag">INCAR
tags</a> that are unnecessary to reproduce the issue. This may mean
using a different structure ([POSCAR](../input-files/POSCAR.md)) with fewer
atoms. Or, for a magnetic calculation that may imply switching off
projections ([LORBIT](../incar-tags/LORBIT.md)), the use of spin-orbit
coupling ([LSORBIT](../incar-tags/LSORBIT.md)) or perhaps an on-site
Coulomb interaction ([LDAU](../incar-tags/LDAU.md)) if this is not essential
to what is demonstrated. For a molecular-dynamics run, reducing the
complexity may imply starting from an intermediate time step with a
random seed ([RANDOM_SEED](../incar-tags/RANDOM_SEED.md)) and
choosing a smaller supercell.

### Step 2\[<a
href="/wiki/index.php?title=Minimal_reproducible_example&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 2">edit</a> \| (./index.php.md)\]

Select parameters that reproduce the result with minimal computational
effort, even though it may reduce the accuracy of the calculation. For
instance, this often implies reducing ([ENCUT](../incar-tags/ENCUT.md)),
choosing a coarser k mesh ([KPOINTS](../input-files/KPOINTS.md)), lowering
[PREC](../incar-tags/PREC.md), etc.

### Step 3\[<a
href="/wiki/index.php?title=Minimal_reproducible_example&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 3">edit</a> \| (./index.php.md)\]

Finally, ensure to include

1.  all files to run the calculation (execution commands/submission
    script and input files that may include
    [INCAR](../input-files/INCAR.md), [POSCAR](../input-files/POSCAR.md),
    [POTCAR](../input-files/POTCAR.md), [KPOINTS](../input-files/KPOINTS.md),
    [ICONST](../input-files/ICONST.md), etc.),
2.  the main output files (stdout, [OUTCAR](../output-files/OUTCAR.md),
    [REPORT](../output-files/REPORT.md) for molecular-dynamics runs,
    [ML_LOGFILE](../output-files/ML_LOGFILE.md) for machine-learning
    force fields, etc.)
3.  and any problem-specific files that, e.g., include the specific data
    in focus or that extract and plot the data from the output files.

If the problem only occurs for specific hardware, versions of VASP, or
toolchains, it is also essential to include that information.

## Related tags and articles\[<a
href="/wiki/index.php?title=Minimal_reproducible_example&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Input files](../categories/Category-Input_files.md),
[Output files](https://vasp.at/wiki/index.php/Category:Output_files),
[Troubleshooting electronic
convergence](Troubleshooting_electronic_convergence.md)



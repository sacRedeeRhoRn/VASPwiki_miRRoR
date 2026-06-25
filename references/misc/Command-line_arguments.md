<!-- Source: https://vasp.at/wiki/index.php/Command-line_arguments | revid: 22456 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Command-line arguments


You provide command line arguments to the VASP executables. These
options give you access to some build information about the executables
without the need to provide all necessary input files to run VASP. You
can also use the [dry run mode](#--dry-run_/_-n) to quickly check the
sanity of your input files.


## Contents


- [1 --cpp-options
  / -c](#--cpp-options_/_-c)
- [2 --dry-run /
  -n](#--dry-run_/_-n)
- [3 --link-line /
  -l](#--link-line_/_-l)
- [4 --version /
  -v](#--version_/_-v)


## --cpp-options / -c\[<a
href="/wiki/index.php?title=Command-line_arguments&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: --cpp-options / -c">edit</a> \| (./index.php.md)\]

Print the CPP_OPTIONS set in the makefile.include during the build of
the executable to the standard output. The code exits after printing the
CPP_OPTIONS.

## --dry-run / -n\[<a
href="/wiki/index.php?title=Command-line_arguments&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: --dry-run / -n">edit</a> \| (./index.php.md)\]

Execute most of VASP setup routines but stop before doing any of the
computational expensive tasks. Use this mode to quickly test whether
your input files are correct e.g. before submitting the job to the queue
of an HPC. Among other things, this mode will:

- Assess your setup and inform you if the version of VASP is
  incompatible. This could be if you try to run the Γ-point version with
  multiple **k** points or the standard version with spin-orbit
  coupling.

<!-- -->

- Check whether your [INCAR](../input-files/INCAR.md) file can be parsed and
  understood. This can catch issues where you assigned a tag to an
  inappropriate type e.g. [ENCUT](../incar-tags/ENCUT.md)=F. The beginning
  of the [OUTCAR](../output-files/OUTCAR.md) file reports also the
  interpretation of the INCAR file and the parameters of the run which
  you can inspect for consistency.

<!-- -->

- Notify you about potential issues in your
  [POSCAR](../input-files/POSCAR.md) file. This includes incorrect
  formatting, missing atoms or types, and too small distances between
  atoms.

<!-- -->

- Parse the [KPOINTS](../input-files/KPOINTS.md) file to the
  [IBZKPT](../output-files/IBZKPT.md) file. If the parsing fails you can
  correct the [KPOINTS](../input-files/KPOINTS.md) setup. The
  [IBZKPT](../output-files/IBZKPT.md) reports the number of irreducible
  **k** points. You can use this information to choose an adequate
  [KPAR](../incar-tags/KPAR.md) setting.

<!-- -->

- Read the [POTCAR](../input-files/POTCAR.md) file to detect mismatches
  with the [POSCAR](../input-files/POSCAR.md) file.

|  |
|----|
| **Tip:** The output of a dry-run will typically not produce output that postprocessing tools can understand. You may consider [ALGO](../incar-tags/ALGO.md)=None as an alternative. |

## --link-line / -l\[<a
href="/wiki/index.php?title=Command-line_arguments&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: --link-line / -l">edit</a> \| (./index.php.md)\]

Print the LLIBS set in the makefile.include during the build of the
executable to the standard output. The code exits after printing the
LLIBS.

## --version / -v\[<a
href="/wiki/index.php?title=Command-line_arguments&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: --version / -v">edit</a> \| (./index.php.md)\]

Print the version string of this VASP executable. In addition, report
when the VASP executable was build and whether this is a gamma-only or a
complex version of VASP.

------------------------------------------------------------------------



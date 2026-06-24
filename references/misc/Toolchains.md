<!-- Source: https://vasp.at/wiki/index.php/Toolchains | revid: 34945 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Toolchains
Below we list the toolchains (compilers + assorted libraries) that we
have used to build and test VASP in our nightly tests during the
development. Starting from VASP.6.3.0, the toolchains are listed
separately for each version of VASP.

- These lists of toolchains are not comprehensive. They show what we
  have employed on a regular basis. Other/newer versions of the
  compilers and libraries than those listed below will, in all
  probability, work just as well (or better).

|  |
|----|
| **Tip:** We encourage using up-to-date versions of compilers and libraries since they are continuously improved and bugs are identified and fixed. |

- Also for older versions of VASP, we recommend using up-to-date
  versions of compilers and libraries. In most cases, this will not be a
  problem. Except in some cases, VASP code was adjusted, e.g., to
  accommodate changes in the behavior of a compiler. This happens when
  compilers became more strict and do not accept certain code constructs
  used in older VASP versions. Here are a few known examples:
  - Compilation with GCC \> 7.X.X is only possible as of VASP.6.2.0
    .^([\[1\]](#cite_note-gcc-beyond-7-support-1))
  - Compilation with GCC \> 14.2.X is currently (as of VASP.6.5.1) not
    possible since it dropped legacy code support in C and Fortran
    formatted strings. This can be worked around by adding the compiler
    flag `-std=legacy`

## Contents

- [1 VASP.6.6.0](#VASP.6.6.0)
- [2 VASP.6.5.1](#VASP.6.5.1)
- [3 VASP.6.4.3](#VASP.6.4.3)
- [4 VASP.6.3.0](#VASP.6.3.0)
- [5 Older versions of VASP.6](#Older_versions_of_VASP.6)
- [6 Footnotes and references](#Footnotes_and_references)
- [7 Related articles](#Related_articles)

## VASP.6.6.0
[TABLE]

  

## VASP.6.5.1
[TABLE]

## VASP.6.4.3
[TABLE]

## VASP.6.3.0
[TABLE]

## Older versions of VASP.6
[TABLE]

## Footnotes and references
1.  ↑ ^([a](#cite_ref-gcc-beyond-7-support_1-0))
    ^([b](#cite_ref-gcc-beyond-7-support_1-1)) Support for GCC \> 7.X.X
    was added with VASP.6.2.0. Do not use GCC-8.X.X compilers: the way
    we use the `CONTIGUOUS` construct in VASP is broken when using these
    compilers.
2.  ↑ ^([a](#cite_ref-nec-aurora-support_2-0))
    ^([b](#cite_ref-nec-aurora-support_2-1))
    ^([c](#cite_ref-nec-aurora-support_2-2))
    ^([d](#cite_ref-nec-aurora-support_2-3)) The NEC SX-Aurora TSUBASA
    vector engine is supported as of VASP.6.3.0.
3.  ↑ ^([a](#cite_ref-ompi-bug-1_3-0)) ^([b](#cite_ref-ompi-bug-1_3-1))
    ^([c](#cite_ref-ompi-bug-1_3-2)) ^([d](#cite_ref-ompi-bug-1_3-3))
    ^([e](#cite_ref-ompi-bug-1_3-4)) ^([f](#cite_ref-ompi-bug-1_3-5))
    ^([g](#cite_ref-ompi-bug-1_3-6)) ^([h](#cite_ref-ompi-bug-1_3-7))
    ^([i](#cite_ref-ompi-bug-1_3-8)) ^([j](#cite_ref-ompi-bug-1_3-9)) A
    bug in OpenMPI versions 4.0.4-4.1.1 causes a memory leak in some
    ScaLAPACK calls. This mainly affects long
    [molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
    runs. This issue is fixed as of openmpi-4.1.2.
4.  [↑](#cite_ref-omp-acc-bug-1_4-0) The NVIDIA HPC-SDK versions 22.1
    and 22.2 have a serious bug that prohibits the execution of the
    OpenACC GPU port of VASP in conjunction with OpenMP-threading. When
    using these compiler versions you should compile the OpenACC GPU
    port of VASP without OpenMP-support. This bug is fixed as of NVIDIA
    HPC-SDK version 22.3.

## Related articles
[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md),
[makefile.include](Makefile.include.md), [Compiler
options](Compiler_options.md), [Precompiler
options](Precompiler_options.md), [Linking to
libraries](Linking_to_libraries.md), [GPU
ports of VASP](GPU_ports_of_VASP.md), [Validation
tests](Validation_tests.md), [Known
issues](Known_issues.md), [Personal computer
installation](Personal_computer_installation.md)

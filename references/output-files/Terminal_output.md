<!-- Source: https://vasp.at/wiki/index.php/Terminal_output | revid: 32898 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Terminal output
The screen output of VASP consists of several sections and can contain
important warnings and error messages.

|  |
|----|
| **Tip:** Check the **stdout** (or [OUTCAR](OUTCAR.md)) for warning messages after a calculation finishes. Often a small oversight can lead to plausible, but incorrect results. |

## Contents

- [1 The header](#The_header)
  - [1.1 No of nodes, MPI ranks, OpenMP threads, and
    parallelization](#No_of_nodes,_MPI_ranks,_OpenMP_threads,_and_parallelization)
  - [1.2 GPU detection](#GPU_detection)
  - [1.3 Version number, build date, and executable
    type](#Version_number,_build_date,_and_executable_type)
  - [1.4 Structure information](#Structure_information)
  - [1.5 ScaLAPACK](#ScaLAPACK)
  - [1.6 LDA part of correlation](#LDA_part_of_correlation)
  - [1.7 Reading the WAVECAR header](#Reading_the_WAVECAR_header)
  - [1.8 Input file check](#Input_file_check)
  - [1.9 FFT planning](#FFT_planning)
  - [1.10 Reading WAVECAR and/or CHGCAR](#Reading_WAVECAR_and/or_CHGCAR)
- [2 The body](#The_body)
- [3 Error and warning messages](#Error_and_warning_messages)
- [4 Related tags and articles](#Related_tags_and_articles)

## The header
The header has a few sections, that may or may not get printed depending
on the calculation. Additional information and warnings may be present
depending on the calculation and setup. Some common blocks are described
below.

### No of nodes, MPI ranks, OpenMP threads, and parallelization
The first output details rank, threading, and
[parallelization](../categories/Category-Parallelization.md)
information. E.g. with [`KPAR`](../incar-tags/KPAR.md)` = 4` and OpenMP
threading:

    running   16 mpi-ranks, with    4 threads/rank, on    1 nodes
    distrk:  each k-point on    4 cores,    4 groups
    distr:  one band on    1 cores,    4 groups

or without OpenMP threading, but [`KPAR`](../incar-tags/KPAR.md)` = 1` and
[`NCORE`](../incar-tags/NCORE.md)` = 4`

    running   16 mpi-ranks, with    1 threads/rank, on    1 nodes
    distrk:  each k-point on   16 cores,    1 groups
    distr:  one band on    4 cores,    4 groups

### GPU detection
If the executable is
[installed](../misc/Installing_VASP.6.X.X.md) with
[support for GPU offloading](../categories/Category-GPU.md), and
VASP can detect the GPUs on the execution node, it will be mentioned
here:

    Offloading initialized ...    2 GPUs detected

### Version number, build date, and executable type
Note that both the standard and the
[noncollinear](../categories/Category-Noncollinear_magnetism.md)
version print out "complex", while the gamma-only version prints
"gamma-only": `vasp_std` and `vasp_ncl`:

    vasp.6.4.3 19Mar24 (build Sep 03 2024 17:30:01) complex

`vasp_gam`:

    vasp.6.5.0 16Dec24 (build Feb 28 2025 14:30:48) gamma-only

### Structure information
    POSCAR found type information on POSCAR CoSiTi
    POSCAR found :  3 types and       4 ions

### ScaLAPACK
This line is present if VASP is installed with [ScaLAPACK
support](../misc/Precompiler_options.md).

    scaLAPACK will be used

### LDA part of correlation
The following line prints the implementation selected for the LDA XC
energy. E.g.:

    LDA part: xc-table for (Slater+PW92), standard interpolation

or

    LDA part: xc-table for (Slater(with rela. corr.)+CA(PZ))
    , standard interpolation

### Reading the [WAVECAR](../input-files/WAVECAR.md) header
If a [WAVECAR](../input-files/WAVECAR.md) is present, the header is read
now

    found WAVECAR, reading the header

If the no of **k**-points changed, a warning is printed here

    number of k-points has changed, file:    20 present:     8
    trying to continue reading WAVECAR, but it might fail

|  |
|----|
| **Warning:** If the no of **k** points changes, we recommend restarting from a [CHGCAR](../input-files/CHGCAR.md) file and not from the [WAVECAR](../input-files/WAVECAR.md) file. |

In the case a [WAVECAR](../input-files/WAVECAR.md) is read in, but the
number of **k**-points *NK1* has changed to *NK2*, the orbitals of the
last **k**-point of the [WAVECAR](../input-files/WAVECAR.md) will be used
for all remaining **k** points if *NK2*\>*NK1*. If *NK2*\<*NK1*, the
first *NK2* **k**-points from the [WAVECAR](../input-files/WAVECAR.md)
will be mapped to the new **k** points. In both cases the coordinates of
**k** points are not considered.

### Input file check
If the [input files](../categories/Category-Input_files.md)
[POSCAR](../input-files/POSCAR.md), [INCAR](../input-files/INCAR.md), and
[KPOINTS](../input-files/KPOINTS.md) are consistent, the following line is
printed

    POSCAR, INCAR and KPOINTS ok, starting setup

### FFT planning
    FFT: planning ... GRIDC
    FFT: planning ... GRID_SOFT
    FFT: planning ... GRID

### Reading [WAVECAR](../input-files/WAVECAR.md) and/or [CHGCAR](../input-files/CHGCAR.md)
Depending on the availability of the files and the setting of
[ISTART](../incar-tags/ISTART.md) and [ICHARG](../incar-tags/ICHARG.md), the
[WAVECAR](../input-files/WAVECAR.md) or [CHGCAR](../input-files/CHGCAR.md)
are read.

    reading WAVECAR
    the WAVECAR file was read successfully
    charge-density read from file: unknown

If the no of bands increased, this is printed

    reading WAVECAR
    random initialization beyond band           13
    the WAVECAR file was read successfully

For [`ISPIN`](../incar-tags/ISPIN.md)` = 2` the magnetization density can
also be read from [CHGCAR](../input-files/CHGCAR.md)

    reading WAVECAR
    the WAVECAR file was read successfully
    charge-density read from file: GaAs                                    
    magnetization density read from file 1

## The body
After the line

    entering main loop

the body of the **stdout** begins. It is essentially equivalent to the
[OSZICAR](OSZICAR.md) file. Please consult the
[OSZICAR](OSZICAR.md) page for an explanation of the
presented data.

## Error and warning messages
Incorrect usage of [INCAR](../input-files/INCAR.md) tags will result in
errors printed to **stdout**, and VASP will terminate immediately. E.g.
[`KPAR`](../incar-tags/KPAR.md)` = .TRUE.` will result in:

     -----------------------------------------------------------------------------
    |                                                                             |
    |     EEEEEEE  RRRRRR   RRRRRR   OOOOOOO  RRRRRR      ###     ###     ###     |
    |     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
    |     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
    |     EEEEE    RRRRRR   RRRRRR   O     O  RRRRRR       #       #       #      |
    |     E        R   R    R   R    O     O  R   R                               |
    |     E        R    R   R    R   O     O  R    R      ###     ###     ###     |
    |     EEEEEEE  R     R  R     R  OOOOOOO  R     R     ###     ###     ###     |
    |                                                                             |
    |     Error reading item KPAR from file INCAR.                                |
    |     Error code was IERR= 5 ... .                                            |
    |                                                                             |
    |       ---->  I REFUSE TO CONTINUE WITH THIS SICK JOB ... BYE!!! <----       |
    |                                                                             |
     -----------------------------------------------------------------------------

If the problem is considered less severe, VASP will continue with the
execution, but can display a warning. E.g. if the
[KPOINTS](../input-files/KPOINTS.md) file is missing and
[KSPACING](../incar-tags/KSPACING.md) is not set in the
[INCAR](../input-files/INCAR.md) file, VASP will execute with a default,
quite coarse, mesh:

     -----------------------------------------------------------------------------
    |                                                                             |
    |           W    W    AA    RRRRR   N    N  II  N    N   GGGG   !!!           |
    |           W    W   A  A   R    R  NN   N  II  NN   N  G    G  !!!           |
    |           W    W  A    A  R    R  N N  N  II  N N  N  G       !!!           |
    |           W WW W  AAAAAA  RRRRR   N  N N  II  N  N N  G  GGG   !            |
    |           WW  WW  A    A  R   R   N   NN  II  N   NN  G    G                |
    |           W    W  A    A  R    R  N    N  II  N    N   GGGG   !!!           |
    |                                                                             |
    |     The requested file  could not be found or opened for reading            |
    |     k-point information. Automatic k-point generation is used as a          |
    |     fallback, which may lead to unwanted results.                           |
    |                                                                             |
     -----------------------------------------------------------------------------

Missing information on [magnetic moments](../incar-tags/MAGMOM.md) will
result in, probably the wrong, automatic ferromagnetic initialization:

     -----------------------------------------------------------------------------
    |                                                                             |
    |           W    W    AA    RRRRR   N    N  II  N    N   GGGG   !!!           |
    |           W    W   A  A   R    R  NN   N  II  NN   N  G    G  !!!           |
    |           W    W  A    A  R    R  N N  N  II  N N  N  G       !!!           |
    |           W WW W  AAAAAA  RRRRR   N  N N  II  N  N N  G  GGG   !            |
    |           WW  WW  A    A  R   R   N   NN  II  N   NN  G    G                |
    |           W    W  A    A  R    R  N    N  II  N    N   GGGG   !!!           |
    |                                                                             |
    |     You requested a magnetic or noncollinear calculation, but did not       |
    |     specify the initial magnetic moment with the MAGMOM tag. Note that      |
    |     a default of 1 will be used for all atoms. This ferromagnetic setup     |
    |     may break the symmetry of the crystal, in particular it may rule        |
    |     out finding an antiferromagnetic solution. Thence, we recommend         |
    |     setting the initial magnetic moment manually or verifying carefully     |
    |     that this magnetic setup is desired.                                    |
    |                                                                             |
     -----------------------------------------------------------------------------

## Related tags and articles
[OSZICAR](OSZICAR.md), [OUTCAR](OUTCAR.md)

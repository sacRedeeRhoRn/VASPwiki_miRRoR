<!-- Source: https://vasp.at/wiki/index.php/Restarting_finite_differences_calculations | revid: 34779 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Restarting finite differences calculations


It is possible to restart [finite difference
calculations](Phonons_from_finite_differences.md)
using [`IBRION`](../incar-tags/IBRION.md)` = 6` and
[CHECKPOINT_FD](../incar-tags/CHECKPOINT_FD.md). The displacements
are written to a [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md)
file. For details of a general finite difference calculation, see the
[phonons from finite
differences](Phonons_from_finite_differences.md).
Here, we will concern ourselves with restarting and splitting finite
difference calculations.

|  |
|----|
| **Mind:** This can only be done using [`IBRION`](../incar-tags/IBRION.md)` = 6`. We recommend using this generally over [`IBRION`](../incar-tags/IBRION.md)` = 5`. |

There are several options for the
[CHECKPOINT_FD](../incar-tags/CHECKPOINT_FD.md) tag. The default is
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = RESET`, which
creates a new [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md)
file and updates the file during the calculation after each
displacement.
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = CONTINUE`
continues from the last completed displacement and
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = PREPARE`
creates the displacements and stops after the electronic minimization
for the equilibrium structure.
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = SINGLE` is
used to run individual displacements.

We will describe the restart procedure and splitting a calculation
below. As an example, we take a 3x3x1 graphene supercell
[POSCAR](../input-files/POSCAR.md) file from the
<a href="https://www.vasp.at/tutorials/latest/phonon/part1/#phonon-e02"
class="external text" rel="nofollow">phonon tutorials</a>.


**Click to see POSCAR and INCAR**


    C18
    1.0
       7.3521657209830806    0.0000000000000000    0.0000000000000000
      -3.6760828604915403    6.3671622872044793    0.0000000000000000
       0.0000000000000000    0.0000000000000000    8.0000000000000000
    C
    18
    direct
       0.1111111111111133    0.2222222222222200    0.0000000000000000 C
       0.1111111111111133    0.5555555555555532    0.0000000000000000 C
       0.1111111111111133    0.8888888888888866    0.0000000000000000 C
       0.4444444444444466    0.2222222222222200    0.0000000000000000 C
       0.4444444444444466    0.5555555555555532    0.0000000000000000 C
       0.4444444444444466    0.8888888888888866    0.0000000000000000 C
       0.7777777777777801    0.2222222222222200    0.0000000000000000 C
       0.7777777777777799    0.5555555555555532    0.0000000000000000 C
       0.7777777777777799    0.8888888888888866    0.0000000000000000 C
       0.2222222222222200    0.1111111111111133    0.0000000000000000 C
       0.2222222222222200    0.4444444444444466    0.0000000000000000 C
       0.2222222222222199    0.7777777777777799    0.0000000000000000 C
       0.5555555555555532    0.1111111111111133    0.0000000000000000 C
       0.5555555555555534    0.4444444444444466    0.0000000000000000 C
       0.5555555555555532    0.7777777777777799    0.0000000000000000 C
       0.8888888888888866    0.1111111111111133    0.0000000000000000 C
       0.8888888888888866    0.4444444444444466    0.0000000000000000 C
       0.8888888888888866    0.7777777777777799    0.0000000000000000 C

along with a 4x4x1 **k**-mesh in our [KPOINTS](../input-files/KPOINTS.md)
file:

    K points
     0
    Gamma
    4  4  1
    0  0  0

and `PAW C_s 04May1998` [POTCAR](../input-files/POTCAR.md).

The following [INCAR](../input-files/INCAR.md) file with modifications will
be used thoughout:

    SYSTEM = graphene
    ENCUT = 400

    # electronic
    PREC = Accurate
    NELMIN = 5
    EDIFF = 1e-8
    ISMEAR = -1
    SIGMA = 0.2
    LREAL = .FALSE.
    LWAVE = .FALSE.
    LCHARG = .FALSE.

    # ionic (finite differences)
    IBRION = 6
    POTIM = 0.015


## Contents


- [1 Restarting a
  finite difference
  calculation](#restarting-a-finite-difference-calculation)
- [2 Splitting a
  finite difference
  calculation](#splitting-a-finite-difference-calculation)
  - [2.1 1.
    Preparing the displacements](#1-preparing-the-displacements)
  - [2.2 2. Single
    displacement
    calculations](#2-single-displacement-calculations)
  - [2.3 3.
    Collected finite
    differences](#3-collected-finite-differences)
- [3 Practical
  hints](#practical-hints)
- [4 Related tags
  and sections](#related-tags-and-sections)


## Restarting a finite difference calculation\[<a
href="/wiki/index.php?title=Restarting_finite_differences_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Restarting a finite difference calculation">edit</a> \| (./index.php.md)\]

The calculation failed after a certain point or has accidentally been
cancelled:

    DAV:   9    -0.181350430125E+03   -0.25600E-06   -0.38452E-08   848   0.118E-03    0.774E-04
    DAV:  10    -0.181350430581E+03   -0.45554E-06   -0.20686E-08   864   0.738E-04    0.208E-04
    DAV:  11    -0.181350430676E+03   -0.94857E-07   -0.22346E-09   704   0.354E-04    0.207E-04
    srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
    slurmstepd-test01: error: *** JOB 254054 ON test01 CANCELLED AT 2026-01-19T16:25:49 ***
    slurmstepd-test01: error: *** STEP 254054.0 ON test01 CANCELLED AT 2026-01-19T16:25:49 ***

In the directory, you will see the
[vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file. It
contains the displacement calculations that have been completed up to
the point of the crash:

    h5ls vaspcheckfd.h5

    data-1                   Group
    displacements            Group
    symmetry                 Group

Restart the calculation by adding
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = CONTINUE` to
the [INCAR](../input-files/INCAR.md):

    SYSTEM = graphene
    ENCUT = 400

    # electronic
    PREC = Accurate
    NELMIN = 5
    EDIFF = 1e-8
    ISMEAR = -1
    SIGMA = 0.2
    LREAL = .FALSE.
    LWAVE = .FALSE.
    LCHARG = .FALSE.

    # ionic (finite differences)
    IBRION = 6
    POTIM = 0.015
    CHECKPOINT_FD = CONTINUE

and resubmit your calculation in the directory. The finite differences
calculation will continue after an SCF step has been done and the
*stdout* reads

    Continuing from previous run

The calculation finishes as normal when all displacements have been
completed and the phonon modes calculated:

    h5ls vaspcheckfd.h5

    data-1                   Group
    data-2                   Group
    data-3                   Group
    data-4                   Group
    displacements            Group
    symmetry                 Group

## Splitting a finite difference calculation\[<a
href="/wiki/index.php?title=Restarting_finite_differences_calculations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Splitting a finite difference calculation">edit</a> \| (./index.php.md)\]

For large structures, it may be easier to split the displacements into
separate calculations. This is done in three steps:

1.  Preparing the separate displacements -
    [`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = PREPARE`
2.  Single displacement calculations -
    [`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = SINGLE`
3.  Collected finite differences -
    [`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = CONTINUE`

### 1. Preparing the displacements\[<a
href="/wiki/index.php?title=Restarting_finite_differences_calculations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: 1. Preparing the displacements">edit</a> \| (./index.php.md)\]

The displacements can be prepared using the
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = PREPARE` tag:

    SYSTEM = graphene
    ENCUT = 400

    # electronic
    PREC = Accurate
    NELMIN = 5
    EDIFF = 1e-8
    ISMEAR = -1
    SIGMA = 0.2
    LREAL = .FALSE.
    LWAVE = .FALSE.

    # ionic (finite differences)
    IBRION = 6
    POTIM = 0.015
    CHECKPOINT_FD = PREPARE

This creates [CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md)
files containing each of the displacements in the parent directory and
you can see the following in the **stdout**:

    Creating CONTCAR files for finite difference displacements

and in the [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file:

    h5ls vaspcheckfd.h5

    metadata                 Group
    subdir_prefix            Dataset {SCALAR}
    total_count              Dataset {SCALAR}

### 2. Single displacement calculations\[<a
href="/wiki/index.php?title=Restarting_finite_differences_calculations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: 2. Single displacement calculations">edit</a> \| (./index.php.md)\]

Create directories **disp-N** for each of the
[CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md) file and run the
calculations separately. To this end, copy all restart files in the
subdirectory, rename
[CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md) to
[POSCAR](../input-files/POSCAR.md), set
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = SINGLE` in the
[INCAR](../input-files/INCAR.md) file and run the calculation:


    max=$(printf "%s\n" CONTCAR_disp-* | sed 's/.*-//' | sort -n | tail -1)

    for i in $(seq 1 $max); do
      mkdir -p disp-$i
      cp CONTCAR_disp-$i disp-$i/POSCAR
      cp INCAR POTCAR KPOINTS vasp.run disp-$i/
      sed -i 's/PREPARE/SINGLE/g' disp-$i/INCAR
      echo """
    NCORE = 4 
    ICHARG = 1
    LCHARG = F
    """ >> disp-$i/INCAR
      ln -s ../CHGCAR disp-$i/CHGCAR
    done


Each [INCAR](../input-files/INCAR.md) file in the directories will then look
like:

    SYSTEM = graphene
    ENCUT = 400

    # electronic
    PREC = Accurate
    NELMIN = 5
    EDIFF = 1e-8
    ISMEAR = -1
    SIGMA = 0.2
    LREAL = .FALSE.
    LWAVE = .FALSE.

    # ionic (finite differences)
    IBRION = 6
    POTIM = 0.015
    CHECKPOINT_FD = SINGLE
    NCORE = 4
    ICHARG = 1
    LCHARG = F

|  |
|----|
| **Important:** You can set different [NCORE](../incar-tags/NCORE.md) settings in these calculations, offering parallelization that is not otherwise possible for finite differences. |

|  |
|----|
| **Tip:** It is optional to restart from [WAVECAR](../input-files/WAVECAR.md) or [CHGCAR](../input-files/CHGCAR.md) files. |

In each subdirectory, you can see that a single displacement has been
recorded in the **stdout**:

    Computing single independent displacement for finite differences

and to the [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file:

    h5ls vaspcheckfd.h5
     
    data-1                   Group

### 3. Collected finite differences\[<a
href="/wiki/index.php?title=Restarting_finite_differences_calculations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: 3. Collected finite differences">edit</a> \| (./index.php.md)\]

Return to the parent directory and combine these separate displacements
into one finite difference calculation using the
[`CHECKPOINT_FD`](../incar-tags/CHECKPOINT_FD.md)` = CONTINUE` tag:

    SYSTEM = graphene
    ENCUT = 400

    # electronic
    PREC = Accurate
    NELMIN = 5
    EDIFF = 1e-8
    ISMEAR = -1
    SIGMA = 0.2
    LREAL = .FALSE.
    LWAVE = .FALSE.
    LCHARG = .FALSE.

    # ionic (finite differences)
    IBRION = 6
    POTIM = 0.015
    CHECKPOINT_FD = CONTINUE

|  |
|----|
| **Warning:** It is possible to combine the finite difference calculations in a different directory but you must include the [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) from the **prepare** step (as it contains the name of the subdirectories as metadata) and the subdirectories including the corresponding [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md). |

Running this calculation, you can see that each of the **single**
displacements are combined into one calculation in the *stdout*:

     Combining displacements from subdirectories

and [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file:

    h5ls vaspcheckfd.h5

    metadata                 Group
    subdir_prefix            Dataset {SCALAR}
    total_count              Dataset {SCALAR}

The information about the computed phonon modes is written to *stdout*
and [OUTCAR](../output-files/OUTCAR.md) file below
`Eigenvectors and eigenvalues of the dynamical matrix` in the same way
as in [phonons from finite
differences](Phonons_from_finite_differences.md).

## Practical hints\[<a
href="/wiki/index.php?title=Restarting_finite_differences_calculations&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Practical hints">edit</a> \| (./index.php.md)\]

- The phonon frequencies will differ slightly between one run and the
  split calculation, on the order of the 4th or 5th significant figure.
  We do not expect this to be significant.
- You can use this method for any
  [electron-phonon](../categories/Category-Electron-phonon_interactions.md)
  calculations.
- You can set different [NCORE](../incar-tags/NCORE.md) settings in these
  calculations, offering parallelization that is not otherwise available
  for finite differences.
- Make sure to check that you are using the correct
  [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file with each
  calculation, particularly the split calculation. If data is read from
  an inappropriate
  [vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md) file, you will
  see it with the following warning:

<!-- -->

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
    |     Checkpoint file vaspcheckfd.h5 is incompatible: NIONS mismatch          |
    |     (file=54, current=128). Ensure that your calculational settings are     |
    |     identical between runs. In particular, check POSCAR, KPOINTS,           |
    |     POTCAR, and INCAR files.                                                |
    |                                                                             |
    |       ---->  I REFUSE TO CONTINUE WITH THIS SICK JOB ... BYE!!! <----       |
    |                                                                             |
     -----------------------------------------------------------------------------

- We recommend using the [CHGCAR](../input-files/CHGCAR.md) file from the
  parent directory of the split calculation for the individual
  displacements to speed up the calculation. Link this with
  `ln -s ../CHGCAR`, set [`LCHARG`](../incar-tags/LCHARG.md)` = .FALSE.`
  so that the original charge density is not overwritten. Also set
  [`ICHARG`](../incar-tags/ICHARG.md)` = 1` so that the charge density is
  used, rather than starting from scratch.

## Related tags and sections\[<a
href="/wiki/index.php?title=Restarting_finite_differences_calculations&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[CHECKPOINT_FD](../incar-tags/CHECKPOINT_FD.md),
[vaspcheckfd.h5](../input-files/Vaspcheckfd.h5.md),
[IBRION](../incar-tags/IBRION.md),
[CONTCAR_disp-N](../output-files/CONTCAR_disp-N.md)

[Phonons from finite
differences](Phonons_from_finite_differences.md)



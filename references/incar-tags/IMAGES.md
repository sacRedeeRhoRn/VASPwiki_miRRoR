<!-- Source: https://vasp.at/wiki/index.php/IMAGES | revid: 37269 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IMAGES


IMAGES = \[integer\]  
Default: **IMAGES** = 0 

Description: Defines the number of VASP calculations in separate
directories, (e.g., 01, 02, 03, etc.) for [nudged elastic
band](../tutorials/Nudged_elastic_bands.md) calculations,
[parallel tempering](LTEMPER.md), and [thermodynamic
integration](VCAIMAGES.md).

------------------------------------------------------------------------

|  |
|----|
| **Mind:** Available as of VASP 6.2.0 |

IMAGES sets the number of
independent VASP calculations in separate directories. The primary
[INCAR](../input-files/INCAR.md) file should be located in the root
directory. Other files such as [KPOINTS](../input-files/KPOINTS.md),
[POTCAR](../input-files/POTCAR.md), and [POSCAR](../input-files/POSCAR.md) can
be placed in subdirectories, e.g., 01, 02, 03, etc., or in the root
directory. Files in subdirectories take precedence over those in the
root directory.

See [use cases](#use-cases) described below.

## File handling\[<a href="/wiki/index.php?title=IMAGES&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: File handling">edit</a> \| (./index.php.md)\]

When VASP starts, it reads the file [INCAR](../input-files/INCAR.md) in the
root directory. Subsequently, VASP splits the MPI communicator into
subgroups for each image. If an [INCAR](../input-files/INCAR.md) file is
present in the subdirectories 01, 02, 03, ..., VASP will process those
afterward. Otherwise, VASP continues reading from the root
[INCAR](../input-files/INCAR.md) file. You can also provide image-specific
data in the root [INCAR](../input-files/INCAR.md) file if the files are very
similar

     # general INCAR tags
     IMAGES = 4
     TEBEG = 600
     
     # INCAR tags only on IMAGE 1
     IMAGE_1 {
       TEBEG = 400
     }
     
     # INCAR tags only on IMAGE 2
     IMAGE_2 {
       TEBEG = 500
     }

Here, images 3 and 4 would use [TEBEG](TEBEG.md)=600 because
the value is not specified for the image. The files
[KPOINTS](../input-files/KPOINTS.md) and [POTCAR](../input-files/POTCAR.md)
will be read from the subdirectory if available and from the root
directory otherwise. The [POSCAR](../input-files/POSCAR.md) file and all
other input files are always read from the subdirectories. All [output
files](https://vasp.at/wiki/index.php/Category:Output_files) (including
[OUTCAR](../output-files/OUTCAR.md) and [OSZICAR](../output-files/OSZICAR.md))
are always written to the subdirectories.

To summarize, to run a calculation with
IMAGES, you provide:

- an [INCAR](../input-files/INCAR.md) file in the root directory
- optionally an overwriting [INCAR](../input-files/INCAR.md) file in the
  subdirectories
- [POSCAR](../input-files/POSCAR.md) files in the subdirectories
- [KPOINTS](../input-files/KPOINTS.md) and [POTCAR](../input-files/POTCAR.md)
  either in the root or in the subdirectories

## Use cases\[<a href="/wiki/index.php?title=IMAGES&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Use cases">edit</a> \| (./index.php.md)\]

Nudged elastic bands  
If IMAGES is set without any
other tag, an elastic-band calculation is performed. This defaults to
the recommended nudged-elastic-band method, but other options are
available by modifying the [SPRING](SPRING.md) tag. Please
consider the [nudged-elastic-bands
how-to](../tutorials/Nudged_elastic_bands.md) and the
[SPRING](SPRING.md) tag for more information.

<!-- -->

Thermodynamic coupling-constant integrations  
When [VCAIMAGES](VCAIMAGES.md) is set in the
[INCAR](../input-files/INCAR.md) file, VASP computes a thermodynamic
coupling-constant integration. This, in turn, sets
IMAGES=2, running two VASP
calculations in the subdirectories 01 and 02. Since this is a special
case where the two calculations may have different computational costs,
[NCORE_IN_IMAGE1](NCORE_IN_IMAGE1.md) can be set to
force an unequal split of the processes across the two images. The tag
[VCAIMAGES](VCAIMAGES.md) describes in more detail how to
set up these calculations.

<!-- -->

Parallel tempering/replica-exchange method and performing independent calculations  
If the tag [LTEMPER](LTEMPER.md)=.TRUE. is set in the
[INCAR](../input-files/INCAR.md) file, VASP will perform parallel tempering
calculations. In this case, it is necessary to provide different
[POSCAR](../input-files/POSCAR.md) files in each subdirectory and modify
the [TEBEG](TEBEG.md) either by separate
[INCAR](../input-files/INCAR.md) files or nested
IMAGE\_*X*/[TEBEG](TEBEG.md) definitions in the root
[INCAR](../input-files/INCAR.md) file. For further details, refer to the
description of the [LTEMPER](LTEMPER.md) tag. The
combination [LTEMPER](LTEMPER.md)=.TRUE. and
[NTEMPER](NTEMPER.md)=0, also allows to run entirely
independent calculations in the individual subdirectories. This might be
helpful to make better use of nodes with many cores.

## Related tags and articles\[<a href="/wiki/index.php?title=IMAGES&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VCAIMAGES](VCAIMAGES.md),
[LTEMPER](LTEMPER.md), [nudged-elastic-bands
how-to](../tutorials/Nudged_elastic_bands.md),
[SPRING](SPRING.md), [IMAGE_1](IMAGE_1.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IMAGES-_incategory-Examples)

------------------------------------------------------------------------



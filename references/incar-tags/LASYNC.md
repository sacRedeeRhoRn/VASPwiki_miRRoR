<!-- Source: https://vasp.at/wiki/index.php/LASYNC | revid: 17936 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LASYNC
LASYNC = \[logical\]  
Default: **LASYNC** = .FALSE. 

Description: Controls the overlap in communication.

------------------------------------------------------------------------

If LASYNC=*.TRUE.* is set in the INCAR file, VASP will try to overlap
communication with calculations. This might improve performance or
degrade it depending on the MPI library and hardware you are running on.
Please do your own testing and compare the runtimes and results before
using this tag in production runs. Compiling VASP using the
[-DPROFILING](../misc/Precompiler_options.md)
precompiler switch provides a detailed timing of the different VASP
routines which helps in determining if there is a performance gain.
Please report any issues in the [VASP
forum](https://www.vasp.at/forum/).

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LASYNC-_incategory-Examples)

------------------------------------------------------------------------

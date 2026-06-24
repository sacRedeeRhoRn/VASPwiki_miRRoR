<!-- Source: https://vasp.at/wiki/index.php/NSUBSYS | revid: 16065 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NSUBSYS
NSUBSYS = \[integer array\] 

Description: NSUBSYS defines the atomic subsystems in calculations with
multiple Anderson thermostats (in case VASP was compiled with
[-Dtbdyn](../redirects/Precompiler_flags.md)).

------------------------------------------------------------------------

Up to three user-defined atomic subsystems may be coupled with
independent Andersen thermostats^([\[1\]](#cite_note-Andersen80-1))
([MDALGO](MDALGO.md)=13).

These subsystems are defined by specifying the last atom for each
subsystem (two or three values must be supplied). For instance, if total
of 20 atoms is defined in the [POSCAR](../input-files/POSCAR.md)-file, and
the initial 10 atoms belong to the subsystem 1, the next 7 atoms to the
subsystem 2, and the last 3 atoms to the subsystem 3, NSUBSYS should be
defined as follows:

    NSUBSYS= 10 17 20

Note that the last number in the previous example is actually redundant
(clearly the last three atoms belong to the last subsystem) and does not
have to be user-supplied.

## Related tags and articles
[TSUBSYS](TSUBSYS.md), [PSUBSYS](PSUBSYS.md),
[MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NSUBSYS-_incategory-Examples)

## References
1.  [↑](#cite_ref-Andersen80_1-0) [H. C. Andersen, J. Chem. Phys. 72,
    2384 (1980).](http://dx.doi.org/10.1063/1.439486)

------------------------------------------------------------------------

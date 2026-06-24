<!-- Source: https://vasp.at/wiki/index.php/TSUBSYS | revid: 16096 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TSUBSYS
TSUBSYS = \[real array\] 

Description: TSUBSYS sets the temperatures for the atomic subsystems in
calculations with multiple Anderson thermostats (in case VASP was
compiled with [-Dtbdyn](../redirects/Precompiler_flags.md)).

------------------------------------------------------------------------

Up to three user-defined atomic subsystems may be coupled with
independent Andersen thermostats^([\[1\]](#cite_note-Andersen80-1))
([MDALGO](MDALGO.md)=13).

The simulation temperature for the atomic subsystems is set by means of
the TSUBSYS tag (one has to specify one number for each subsystem).

## Related tags and articles
[NSUBSYS](NSUBSYS.md), [PSUBSYS](PSUBSYS.md),
[MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-TSUBSYS-_incategory-Examples)

## References
1.  [↑](#cite_ref-Andersen80_1-0) [H. C. Andersen, J. Chem. Phys. 72,
    2384 (1980).](http://dx.doi.org/10.1063/1.439486)

------------------------------------------------------------------------

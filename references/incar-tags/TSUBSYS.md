<!-- Source: https://vasp.at/wiki/index.php/TSUBSYS | revid: 16096 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TSUBSYS


TSUBSYS = \[real array\] 

Description: TSUBSYS sets the
temperatures for the atomic subsystems in calculations with multiple
Anderson thermostats (in case VASP was compiled with
<a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">-Dtbdyn</a>).

------------------------------------------------------------------------

Up to three user-defined atomic subsystems may be coupled with
independent Andersen
thermostats[^Andersen80-1]
([MDALGO](MDALGO.md)=13).

The simulation temperature for the atomic subsystems is set by means of
the TSUBSYS tag (one has to
specify one number for each subsystem).

## Related tags and articles\[<a href="/wiki/index.php?title=TSUBSYS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NSUBSYS](NSUBSYS.md), [PSUBSYS](PSUBSYS.md),
[MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-TSUBSYS-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=TSUBSYS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^Andersen80-1]: [H. C. Andersen, J. Chem. Phys. 72, 2384 (1980).](http://dx.doi.org/10.1063/1.439486)

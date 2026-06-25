<!-- Source: https://vasp.at/wiki/index.php/PSUBSYS | revid: 16074 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PSUBSYS


PSUBSYS = \[real array\] 

Description: PSUBSYS sets the
collision probabilities for the atoms in each atomic subsystem in
calculations with multiple Anderson thermostats (in case VASP was
compiled with <a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">-Dtbdyn</a>).

------------------------------------------------------------------------

Up to three user-defined atomic subsystems may be coupled with
independent Andersen
thermostats<sup>[\[1\]](#cite_note-Andersen80-1)</sup>
([MDALGO](MDALGO.md)=13).

The collision probabilities for the atoms in each atomic subsystem is
set by means of the PSUBSYS
tag (one has to specify one number for each subsystem).

Note: 0 ≤ PSUBSYS ≤ 1

## Related Tags and Sections\[<a href="/wiki/index.php?title=PSUBSYS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[NSUBSYS](NSUBSYS.md), [TSUBSYS](TSUBSYS.md),
[MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PSUBSYS-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=PSUBSYS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-Andersen80_1-0)
    <a href="http://dx.doi.org/10.1063/1.439486" class="external text"
    rel="nofollow">H. C. Andersen, J. Chem. Phys. 72, 2384 (1980).</a>


------------------------------------------------------------------------



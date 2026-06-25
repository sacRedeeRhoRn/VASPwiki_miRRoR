<!-- Source: https://vasp.at/wiki/index.php/PRJCAR | revid: 27289 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PRJCAR


The PRJCAR file stores the output of the **k**-point projection scheme
(for [LKPROJ](../incar-tags/LKPROJ.md)=.TRUE.).

------------------------------------------------------------------------

It has the following format:

- The header section lists the basis vectors of the reciprocal space
  belonging to the structure defined in the
  [POSCAR.prim](../misc/POSCAR.prim.md) file, and a list of the
  set of points {**k′**}, the projection scheme has found in the
  irreducible part of the Brillouin (IBZ) zone of the aforementioned
  reciprocal space cell (see the section on
  [LKPROJ](../incar-tags/LKPROJ.md)).

<!-- -->

- The body of the PRJCAR file
  lists:

$\Kappa_{n\mathbf{k}\sigma\mathbf{k}'}=\sum_{\mathbf{GG}'} |\langle
\mathbf{k}'+\mathbf{G}'| \mathbf{k}+\mathbf{G}\rangle \langle
\mathbf{k}+\mathbf{G} | \Psi_{n\mathbf{k}\sigma}\rangle |^2$

where *n* is the band index, **k** labels the `NKPTS` points in the IBZ
of the structure defined by the [POSCAR](../input-files/POSCAR.md) file, σ
is the spin index, and **k′** refers to the `NKPTS_PRIME` points in the
IBZ of [POSCAR.prim](../misc/POSCAR.prim.md) (see the section
of [LKPROJ](../incar-tags/LKPROJ.md)).

For each band *n* at **k**σ the body of the
PRJCAR lists the index *n* and
eigenenergy ε<sub>n**k**σ</sub>, followed by one or more rows with a
total of `NKPTS_PRIME` entries K<sub>n**k**σ**k′**</sub>, one for each
point **k′**.

## Related Tags and Sections\[<a href="/wiki/index.php?title=PRJCAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[LKPROJ](../incar-tags/LKPROJ.md)



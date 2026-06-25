<!-- Source: https://vasp.at/wiki/index.php/LDAUPRINT | revid: 36502 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDAUPRINT


LDAUPRINT = 0 \| 1  
Default: **LDAUPRINT** = 0 

Description: LDAUPRINT
controls the verbosity of a DFT+U calculation.

------------------------------------------------------------------------

- LDAUPRINT=0: No onsite
  occupancy matrix is written to the [OUTCAR](../output-files/OUTCAR.md)
  file.
- LDAUPRINT=1: The spin up and
  spin down onsite occupancy matrices of the atoms types to which a
  $U$ is applied are written to the
  [OUTCAR](../output-files/OUTCAR.md) file at each iteration (below "onsite
  density matrix"). The eigenvalues and eigenvectors of the total (spin
  up + spin down) onsite matrix is also written (below "occupancies and
  eigenvectors").

## Related tags and articles\[<a
href="/wiki/index.php?title=LDAUPRINT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LDAU](LDAU.md), [LDAUTYPE](LDAUTYPE.md),
[LDAUL](LDAUL.md), [LDAUU](LDAUU.md),
[LDAUJ](LDAUJ.md), [LMAXMIX](LMAXMIX.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LDAUPRINT-_incategory-Examples)

------------------------------------------------------------------------



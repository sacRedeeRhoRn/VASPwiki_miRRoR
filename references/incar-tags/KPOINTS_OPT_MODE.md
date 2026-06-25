<!-- Source: https://vasp.at/wiki/index.php/KPOINTS_OPT_MODE | revid: 32889 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINTS_OPT_MODE


KPOINTS_OPT_MODE = 0 \| 1 \|
2  
Default: **KPOINTS_OPT_MODE** = 1 

Description: Selects which diagonalization algorithm to use for the
optional k-points driver

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

Sometimes, the electronic Kohn-Sham orbitals are required on an
alternative k-point mesh, for example via
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) or
[KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md). In this case, the tag
KPOINTS_OPT_MODE selects which
diagonalization algorithm should be used to obtain these eigenvalues.

## Tag options\[<a
href="/wiki/index.php?title=KPOINTS_OPT_MODE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Tag options">edit</a> \| (./index.php.md)\]

`KPOINTS_OPT_MODE`` = 0`  
The diagonalization of the Hamiltonian at the alternative k-points is
skipped entirely

`KPOINTS_OPT_MODE`` = 1`  
Uses the [Blocked-Davidson
algorithm](../theory/Blocked-Davidson_algorithm.md)
(same as [`ALGO`](ALGO.md)` = Normal`)

`KPOINTS_OPT_MODE`` = 2`  
Performs an exact diagonalization (same as
[`ALGO`](ALGO.md)` = Exact`)

## Related tags and articles\[<a
href="/wiki/index.php?title=KPOINTS_OPT_MODE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [KPOINTS_OPT](../input-files/KPOINTS_OPT.md)
- [KPOINTS_ELPH](../input-files/KPOINTS_ELPH.md)
- [ALGO](ALGO.md)



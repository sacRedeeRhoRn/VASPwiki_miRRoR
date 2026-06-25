<!-- Source: https://vasp.at/wiki/index.php/NFREE | revid: 30399 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NFREE


NFREE = \[integer\] 

|                    |     |                                      |
|--------------------|-----|--------------------------------------|
| Default: **NFREE** | = 1 | if [IBRION](IBRION.md)=2 |
|                    | = 0 | else                                 |

Description: depending on [IBRION](IBRION.md),
NFREE specifies the number of
remembered steps in the history of ionic convergence runs, or the number
of ionic displacements in frozen phonon calculations.

------------------------------------------------------------------------

- [IBRION](IBRION.md)=1 (quasi-Newton algorithm for ionic
  relaxation):

\(i\) If NFREE is set, only up
to NFREE ionic steps are kept
in the iteration history (the rank of the approximate Hessian matrix is
not larger than NFREE).

\(ii\) If NFREE is **not**
specified, the criterion whether information is removed from the
iteration history is based on the eigenvalue spectrum of the inverse
Hessian matrix: if one eigenvalue of the inverse Hessian matrix is
larger than 8, information from previous steps is discarded.

For complex problems NFREE can
usually be set to a rather large value (i.e. 10-20), however systems of
low dimensionality require a careful setting of
NFREE (or preferably an exact
counting of the number of degrees of freedom). To increase
NFREE beyond 20 rarely
improves convergence. If NFREE
is set to too large, the RMM-DIIS algorithm might diverge.

- [IBRION](IBRION.md)=5 (from VASP.4.5) or
  [IBRION](IBRION.md)=6 (from VASP.5.1): frozen phonon
  approach to calculate the zone-center vibrational frequencies of a
  system.

NFREE determines how many
displacements are used for each direction and ion. The step size has to
be given in [INCAR](../input-files/INCAR.md), by the tag
[POTIM](POTIM.md). Displacements should be small enough to
ensure that the harmonic approximation is safely fulfilled. If too large
values are supplied in the input file, it is defaulted to 0.015 Å up
from VASP.5.1 (but *not* in all earlier releases). Expertise shows that
this is a very reasonable compromise.

NFREE = 2 uses central
difference, *i.e* each ion is displaced in each direction by a small
positive and negative displacement

$\pm$ [POTIM](POTIM.md) \*
$\hat{x}$,

$\pm$ [POTIM](POTIM.md) \*
$\hat{y}$,

$\pm$ [POTIM](POTIM.md) \*
$\hat{z}$,

For NFREE = 4, four
displacements are used

$\pm$ [POTIM](POTIM.md) \*
$\hat{x}$ and $\pm$ 2 \*
[POTIM](POTIM.md) \* $\hat{x}$,

$\pm$ [POTIM](POTIM.md) \*
$\hat{y}$ and $\pm$ 2 \*
[POTIM](POTIM.md) \* $\hat{x}$,

$\pm$ [POTIM](POTIM.md) \*
$\hat{z}$ and $\pm$ 2 \*
[POTIM](POTIM.md) \* $\hat{x}$,

For NFREE=1, only a single
displacement is applied (it is strongly recommend to avoid
NFREE=1).

## Related tags and articles\[<a href="/wiki/index.php?title=NFREE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBRION](IBRION.md), [POTIM](POTIM.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NFREE-_incategory-Examples)

------------------------------------------------------------------------



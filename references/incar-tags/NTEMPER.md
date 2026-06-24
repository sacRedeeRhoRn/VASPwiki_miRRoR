<!-- Source: https://vasp.at/wiki/index.php/NTEMPER | revid: 33095 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NTEMPER
NTEMPER = \[integer\]  
Default: **NTEMPER** = 200 

Description: NTEMPER specifies how often temperature swaps are attempted
during parallel tempering. The flag must be used in combination with
[IMAGES](IMAGES.md) and [LTEMPER](LTEMPER.md).
NTEMPER=0, allows to perform several completely independent
calculations.

------------------------------------------------------------------------

NTEMPER must be a positive integer or zero. Swaps are on average
attempted after NTEMPER molecular dynamics steps. Specifically, a random
number $r$ between \[0,1\[ is drawn. The
next temperature swaps are attempted after NTEMPER
$\times 2~ r -1$ steps. Obviously, for
NTEMPER=1 swaps are attempted at every MD step. In the present code
version, temperature swaps are alternatively performed between images
1,2 and 3,4 and 5,6 etc., or upon the next swap between images 2,3 and
4,5 and 6,7 etc. This implies that many swaps are attempted at the same
time.

Furthermore, no temperature swapping is attempted for NTEMPER=0. This
allows many independent calculations to be performed in directories 01,
02, 03, ... which can be useful when performing many similar
calculations for small systems or using machine-learned force fields on
many-core machines (strong scaling is sometimes not particularly good
for small systems).

A final note is in place. If INCAR files exist in the subdirectories,
the tag NTEMPER must be set in all [INCAR](../input-files/INCAR.md) files of
the subdirectories 01, 02, 03, and NTEMPER must be identical. Failure to
observe this rule can lead to unexpected behavior.

## Related tags and articles
[IMAGES](IMAGES.md), [LTEMPER](LTEMPER.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IMAGES-_incategory-Examples)

## References
------------------------------------------------------------------------

<!-- Source: https://vasp.at/wiki/index.php/WANPROJ | revid: 35465 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WANPROJ


The WANPROJ file is generated
after
[Wannierization](../tutorials/Constructing_Wannier_orbitals.md)
by setting
[`LWRITE_WANPROJ`](../incar-tags/LWRITE_WANPROJ.md)` = True`. It
contains the Wannier transformation matrices,
$U_{mn \mathbf{k}}$, that transform the Kohn-Sham Bloch
orbitals into the localized Wannier orbitals.

If WANPROJ is present, VASP
skips the Wannierization procedure and reads the transformation matrices
from this file instead.


## Contents


- [1
  Format](#Format)
  - [1.1
    Header](#Header)
  - [1.2
    Transformation
    matrix](#Transformation_matrix)
- [2 Related tags
  and articles](#Related_tags_and_articles)


## Format\[<a href="/wiki/index.php?title=WANPROJ&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Format">edit</a> \| (./index.php.md)\]

The file format is logically split into a header section and a section
that contains the actual transformation matrix,
$U_{mn \mathbf{k}}$. On each line of the file,
different values are separated by one or more whitespace characters.
There are no empty lines in the
WANPROJ file.

### Header\[<a href="/wiki/index.php?title=WANPROJ&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Header">edit</a> \| (./index.php.md)\]

The header section contains the array dimensions of
$U_{mn \mathbf{k}}$ as well as a list of k-points. It
is structured as follows:

- The first line contains a comment
- The second line contains a list of integers
  - `ISPIN`: number of spin channels (either 1 or 2)
  - `NKPTS`: number of k-points in the full first Brillouin zone
  - `NB_TOT`: number of Kohn-Sham bands
  - `NW`: number of Wannier orbitals
- The next `NKPTS` lines contain information about the k-points
  - The first value is an integer and gives the index of the
    corresponding k-point
  - The second, third and fourth values are the x, y and z coordinates
    of the k-point expressed in direct coordinates of the reciprocal
    lattice

### Transformation matrix\[<a href="/wiki/index.php?title=WANPROJ&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Transformation matrix">edit</a> \| (./index.php.md)\]

The transformation matrix is written as blocks of data. Each block
corresponds to a particular spin channel and a particular k-point.

- The first line in each block contains information about the block
  - The first value is an integer and labels the current spin channel
    (either 1 or 2)
  - The second value is also an integer and counts the total number of
    bands that participate in the Wannier transformation at the current
    k-point (some bands may not participate due to being outside an
    energy window or being explicitly excluded from the transformation)
  - The third, fourth and fifth values are the x, y and z coordinates of
    the current k-point expressed in direct coordinates of the
    reciprocal lattice
- Each subsequent line in the block contains one matrix element of
  $U_{mn \mathbf{k}}$
  - The first value is the index $n$ of the
    Kohn-Sham band
  - The second values is the index $m$ of the
    Wannier orbital
  - The third and fourth values are the real and imaginary part of the
    corresponding matrix element

|  |
|----|
| **Mind:** As of version 6.6.0, the content of WANPROJ can be written to [vaspwave.h5](../output-files/Vaspwave.h5.md) if the tag [LH5](../incar-tags/LH5.md) is set. |

## Related tags and articles\[<a href="/wiki/index.php?title=WANPROJ&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LWANNIER90](../incar-tags/LWANNIER90.md),
[LWANNIER90_RUN](../incar-tags/LWANNIER90_RUN.md),
[LWRITE_WANPROJ](../incar-tags/LWRITE_WANPROJ.md),
[LDOWNSAMPLE](../incar-tags/LDOWNSAMPLE.md),
[Constructing_Wannier_orbitals](../tutorials/Constructing_Wannier_orbitals.md),
[cRPA of SrVO3](../misc/CRPA_of_SrVO3.md)

------------------------------------------------------------------------


